# Solar Monitor - data fetching module
# Source: hamqsl.com XML feed (http://www.hamqsl.com/solarxml.php)
# Update interval: every 3 hours (solar indices) / every hour (flux)
# Please do not poll more often than every 15 minutes.

import threading
import urllib.request
from datetime import datetime
from xml.etree import ElementTree

DATA_URL = "http://www.hamqsl.com/solarxml.php"
CACHE_TTL_SECONDS = 900  # 15 minutes

_cache_lock = threading.Lock()
_cache_data = None
_cache_time = None


class SolarDataError(Exception):
	pass


def _fetch_raw_xml() -> bytes:
	try:
		with urllib.request.urlopen(DATA_URL, timeout=10) as resp:
			return resp.read()
	except Exception as e:
		raise SolarDataError(f"Failed to fetch data: {e}") from e


def _parse_xml(raw: bytes) -> dict:
	try:
		root = ElementTree.fromstring(raw)
	except ElementTree.ParseError as e:
		raise SolarDataError(f"Failed to parse XML: {e}") from e

	sd = root.find("solardata")
	if sd is None:
		raise SolarDataError("No <solardata> element found in XML")

	def text(tag: str, default: str = "") -> str:
		el = sd.find(tag)
		return el.text.strip() if el is not None and el.text else default

	def flt(tag: str, default: float = 0.0) -> float:
		try:
			return float(text(tag))
		except (ValueError, TypeError):
			return default

	def intval(tag: str, default: int = 0) -> int:
		try:
			return int(text(tag))
		except (ValueError, TypeError):
			return default

	# HF band conditions: <calculatedconditions><band name="80m-40m" time="day">Good</band>...
	hf_conditions = []
	calc = sd.find("calculatedconditions")
	if calc is not None:
		bands_raw = {}
		for band_el in calc.findall("band"):
			name = band_el.get("name", "")
			time = band_el.get("time", "")
			condition = band_el.text.strip() if band_el.text else ""
			if name not in bands_raw:
				bands_raw[name] = {}
			bands_raw[name][time] = condition
		# Fixed order matching what hamqsl provides
		for band_name in ("80m-40m", "30m-20m", "17m-15m", "12m-10m"):
			if band_name in bands_raw:
				hf_conditions.append(
					{
						"band": band_name,
						"day": bands_raw[band_name].get("day", ""),
						"night": bands_raw[band_name].get("night", ""),
					}
				)

	# VHF conditions: <calculatedvhfconditions><phenomenon name="..." location="...">value</phenomenon>
	vhf_conditions = []
	vhf = sd.find("calculatedvhfconditions")
	if vhf is not None:
		for ph in vhf.findall("phenomenon"):
			vhf_conditions.append(
				{
					"name": ph.get("name", ""),
					"location": ph.get("location", ""),
					"value": ph.text.strip() if ph.text else "",
				}
			)

	# Try to parse update time
	updated_str = text("updated")
	try:
		updated = datetime.strptime(updated_str, "%d %b %Y %H%M GMT")
	except ValueError:
		updated = None

	return {
		"updated": updated,
		"updated_raw": updated_str,
		# Page 1 - Solar Indices
		"sfi": intval("solarflux"),
		"sunspots": intval("sunspots"),
		"aindex": intval("aindex"),
		"kindex": intval("kindex"),
		"kindex_text": text("kindexnt"),  # e.g. "Quiet", "Unsettled", "Storm"
		"xray": text("xray"),  # e.g. "C1.1", "B5.2"
		"bz": flt("magneticfield"),  # Bz component of IMF, nT
		"solar_wind": flt("solarwind"),  # km/s
		"proton_flux": flt("protonflux"),
		"electron_flux": flt("electonflux"),  # note: typo in hamqsl XML is intentional
		"helium_line": flt("heliumline"),  # 304A helium line
		"aurora": intval("aurora"),
		"lat_degree": flt("latdegree"),
		"geomag_field": text("geomagfield"),  # e.g. "QUIET", "UNSETTLD", "STORM"
		"signal_noise": text("signalnoise"),  # e.g. "S0-S1", "S2-S3"
		"muf": text("muf"),  # Maximum Usable Frequency, or "No Report"
		# Page 2 - HF conditions
		"hf_conditions": hf_conditions,
		# Page 3 - VHF conditions
		"vhf_conditions": vhf_conditions,
	}


def get_data(force_refresh: bool = False) -> dict:
	"""Return cached solar data, refreshing if cache is stale or missing."""
	global _cache_data, _cache_time

	with _cache_lock:
		now = datetime.utcnow()
		cache_expired = _cache_time is None or (now - _cache_time).total_seconds() > CACHE_TTL_SECONDS
		if force_refresh or cache_expired:
			raw = _fetch_raw_xml()
			_cache_data = _parse_xml(raw)
			_cache_time = now

	return _cache_data


def get_data_async(callback, error_callback=None):
	"""Fetch data in a background thread. Calls callback(data) or error_callback(exc)."""

	def _worker():
		try:
			data = get_data()
			callback(data)
		except SolarDataError as e:
			if error_callback:
				error_callback(e)

	t = threading.Thread(target=_worker, daemon=True)
	t.start()
