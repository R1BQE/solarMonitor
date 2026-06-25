# Solar Monitor - NVDA global plugin
# Author: r1bqe <r1bqe@mail.ru>

import globalPluginHandler
import ui
import scriptHandler
from scriptHandler import script
import inputCore

try:
	from addonHandler import initTranslation
	initTranslation()
except ImportError:
	pass

from . import data as solarData
from . import descriptions as desc

# Translators: Category shown in Input Gestures dialog
ADDON_SUMMARY = _("Solar Monitor")

_CONDITION_MAP = {
	"Good": _("Good"),
	"Fair": _("Fair"),
	"Poor": _("Poor"),
}

_VHF_VALUE_MAP = {
	"Band Closed": _("Closed"),
	"Closed": _("Closed"),
	"Open": _("Open"),
	"High MUF": _("High MUF"),
	"Aurora": _("Aurora"),
	"50MHz ES": _("50MHz ES"),
}

_KINDEX_MAP = {
	"Quiet": _("Quiet"),
	"Unsettled": _("Unsettled"),
	"Active": _("Active"),
	"Minor Storm": _("Minor Storm"),
	"Major Storm": _("Major Storm"),
	"Severe Storm": _("Severe Storm"),
	"Extreme Storm": _("Extreme Storm"),
}

_PAGE_NAMES = [
	# Translators: Page 1 name
	_("Solar indices"),
	# Translators: Page 2 name
	_("HF band conditions"),
	# Translators: Page 3 name
	_("VHF conditions"),
]

# Keys handled when monitor is active. All others pass through normally.
_NAV_KEYS = {
	"upArrow", "downArrow", "leftArrow", "rightArrow", "d",
}


def _tr(mapping, val):
	return mapping.get(val, val)


def _build_page1(d):
	ktext = _tr(_KINDEX_MAP, d.get("kindex_text", ""))
	kdisp = str(d["kindex"]) + (f", {ktext}" if ktext else "")
	muf = d.get("muf", "")
	muf_disp = _("No data") if not muf or muf.lower() == "no report" else muf
	return [
		(f"SFI: {d['sfi']}", "sfi"),
		(f"{_('Sunspots')}: {d['sunspots']}", "sunspots"),
		(f"{_('A-index')}: {d['aindex']}", "aindex"),
		(f"{_('K-index')}: {kdisp}", "kindex"),
		(f"{_('X-ray')}: {d['xray']}", "xray"),
		(f"{_('Magnetic field Bz')}: {d['bz']}", "bz"),
		(f"{_('Solar wind')}: {d['solar_wind']} km/s", "solar_wind"),
		(f"{_('Proton flux')}: {d['proton_flux']}", "proton_flux"),
		(f"{_('Electron flux')}: {d['electron_flux']}", "electron_flux"),
		(f"{_('Helium line')}: {d['helium_line']}", "helium_line"),
		(f"{_('Aurora')}: {d['aurora']}", "aurora"),
		(f"{_('LatDegree')}: {d['lat_degree']}°", "lat_degree"),
		(f"{_('Geomag field')}: {d['geomag_field']}", "geomag_field"),
		(f"{_('Noise level')}: {d['signal_noise']}", "signal_noise"),
		(f"{_('MUF')}: {muf_disp}", "muf"),
	]


def _build_page2(d):
	dl = _("day")
	nl = _("night")
	rows = []
	for band in d.get("hf_conditions", []):
		day = _tr(_CONDITION_MAP, band.get("day", ""))
		night = _tr(_CONDITION_MAP, band.get("night", ""))
		rows.append((f"{band['band'].upper()}: {dl} {day}, {nl} {night}", band["band"]))
	return rows


def _build_page3(d):
	rows = []
	for ph in d.get("vhf_conditions", []):
		name = ph.get("name", "")
		loc = ph.get("location", "")
		val = _tr(_VHF_VALUE_MAP, ph.get("value", ""))
		label = f"{name}, {loc}: {val}" if loc else f"{name}: {val}"
		rows.append((label, name))
	return rows


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = ADDON_SUMMARY

	def __init__(self):
		super().__init__()
		self._active = False
		self._loading = False
		self._pages = [[], [], []]
		self._page = 0
		self._row = 0
		# Hook into NVDA gesture execution to intercept keys when active
		inputCore.decide_executeGesture.register(self._on_gesture)

	def terminate(self):
		inputCore.decide_executeGesture.unregister(self._on_gesture)
		super().terminate()

	# ------------------------------------------------------------------
	# Gesture hook
	# ------------------------------------------------------------------

	def _on_gesture(self, gesture):
		"""Called by NVDA before executing any gesture. Return False to block."""
		if not self._active or self._loading:
			return True  # pass through
		if not hasattr(gesture, "mainKeyName"):
			return True
		if gesture.modifierNames:
			return True  # don't intercept modified keys (e.g. ctrl+arrows)
		key = gesture.mainKeyName
		if key not in _NAV_KEYS:
			return True  # pass through
		# Handle the key ourselves
		self._handle_nav(key)
		return False  # block original action

	def _handle_nav(self, key):
		if key == "upArrow":
			page = self._pages[self._page]
			if page:
				self._row = (self._row - 1) % len(page)
				ui.message(self._row_text())
		elif key == "downArrow":
			page = self._pages[self._page]
			if page:
				self._row = (self._row + 1) % len(page)
				ui.message(self._row_text())
		elif key == "rightArrow":
			self._page = (self._page + 1) % 3
			self._row = 0
			ui.message(f"{_PAGE_NAMES[self._page]}. {self._row_text()}")
		elif key == "leftArrow":
			self._page = (self._page - 1) % 3
			self._row = 0
			ui.message(f"{_PAGE_NAMES[self._page]}. {self._row_text()}")
		elif key == "d":
			self._speak_desc()

	def _row_text(self):
		page = self._pages[self._page]
		if not page:
			return _("No data")
		return page[self._row][0]

	def _row_key(self):
		page = self._pages[self._page]
		if not page:
			return ""
		return page[self._row][1]

	def _speak_desc(self):
		key = self._row_key()
		if not key:
			return
		if self._page == 0:
			text = desc.get_description(key)
		elif self._page == 1:
			text = desc.get_hf_description(key)
		else:
			text = desc.get_vhf_description(key)
		ui.message(text if text else _("No description available."))

	# ------------------------------------------------------------------
	# Toggle script
	# ------------------------------------------------------------------

	@script(
		# Translators: Description in Input Gestures dialog
		description=_("Open or close the Solar Monitor virtual interface"),
		gesture=None,
	)
	def script_toggleMonitor(self, gesture):
		if self._active:
			self._close()
		elif not self._loading:
			self._open()

	# ------------------------------------------------------------------
	# Open / close / data loading
	# ------------------------------------------------------------------

	def _open(self):
		self._loading = True
		# Translators: Spoken when monitor starts loading
		ui.message(_("Solar Monitor. Loading data..."))
		solarData.get_data_async(
			callback=self._on_data_loaded,
			error_callback=self._on_data_error,
		)

	def _on_data_loaded(self, d):
		import wx
		self._loading = False
		self._pages = [_build_page1(d), _build_page2(d), _build_page3(d)]
		self._page = 0
		self._row = 0
		self._active = True
		updated = d.get("updated_raw", "")
		msg = _("Ready. Updated: {updated}. {page}. {row}").format(
			updated=updated,
			page=_PAGE_NAMES[0],
			row=self._row_text(),
		)
		wx.CallAfter(ui.message, msg)

	def _on_data_error(self, exc):
		import wx
		self._loading = False
		wx.CallAfter(
			ui.message,
			# Translators: Spoken when data fetch fails
			_("Solar Monitor: failed to load data. Check your internet connection."),
		)

	def _close(self):
		self._active = False
		# Translators: Spoken when monitor is closed
		ui.message(_("Solar Monitor closed."))
