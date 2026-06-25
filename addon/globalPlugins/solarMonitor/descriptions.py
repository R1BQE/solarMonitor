# Solar Monitor - parameter descriptions
# Translators: all strings marked with _() go into the .pot file for translation.

from typing import Optional

# NVDA add-ons use the standard gettext mechanism.
# At runtime _ is provided by NVDA's addonHandler.
# During scons pot generation the fake _ from buildVars is used.
try:
	from addonHandler import initTranslation
	initTranslation()
except ImportError:
	pass


def _(s: str) -> str:  # noqa: E302 - fallback for import-time use
	return s


# Each entry: key matches the data dict key from data.py
# Value is the translatable description string.

DESCRIPTIONS: dict[str, str] = {

	"sfi": _(
		# Translators: Description for the Solar Flux Index parameter
		"Solar Flux Index at 10.7 cm wavelength. Reflects overall solar activity and ionospheric ionization. "
		"Below 70: solar minimum, high bands are closed. "
		"70 to 100: low activity, only 40 and 80 meters work. "
		"100 to 150: moderate activity, 20 and 15 meters open. "
		"150 to 200: high activity, 10 meters works well. "
		"Above 200: solar maximum, F2 propagation on 6 meters is possible."
	),

	"sunspots": _(
		# Translators: Description for the Sunspot Number parameter
		"Wolf number - count of sunspots on the solar disk. "
		"0 to 10: solar minimum, high bands almost closed. "
		"10 to 50: low activity. "
		"50 to 100: moderate activity, 20 and 17 meters open. "
		"100 to 150: good activity, 15 and 10 meters work. "
		"Above 150: high activity, solar maximum."
	),

	"aindex": _(
		# Translators: Description for the A-index parameter
		"Planetary geomagnetic activity index for the past 24 hours. Averaged measure of magnetic field disturbance. "
		"0 to 7: quiet, propagation unaffected. "
		"8 to 15: minor disturbance, slight degradation on polar paths. "
		"16 to 29: moderate storm, noticeable degradation on 80 and 160 meters. "
		"30 to 49: strong storm, HF propagation seriously disrupted. "
		"50 and above: extreme storm, communication on many bands impossible."
	),

	"kindex": _(
		# Translators: Description for the K-index parameter
		"Current geomagnetic activity index, updated every 3 hours. Scale from 0 to 9. "
		"0 to 1: quiet, excellent conditions. "
		"2 to 3: minor disturbance, propagation unaffected. "
		"4: unsettled, slight degradation possible. "
		"5: minor storm, noticeable degradation at high latitudes. "
		"6 to 7: moderate storm, serious disruption on 80 and 160 meters and polar paths. "
		"8 to 9: severe storm, HF communication nearly impossible."
	),

	"xray": _(
		# Translators: Description for the X-ray flux parameter
		"Solar X-ray flux level. "
		"Class A: background level, no effect. "
		"Class B: low activity, no effect. "
		"Class C: minor flare, slight absorption on the sunlit side. "
		"Class M: moderate flare, noticeable HF signal absorption on the sunlit side for 1 to 2 hours. "
		"Class X: major flare, complete radio blackout on the sunlit side possible for several hours. "
		"X5 and above: extreme flare, blackout lasting the entire daylight period."
	),

	"bz": _(
		# Translators: Description for the Bz magnetic field component parameter
		"Z-component of the interplanetary magnetic field in nanoteslas. "
		"Positive values (northward): Earth's magnetic shield holds, no storm. "
		"0 to minus 5: weak southward field, no threat. "
		"Minus 5 to minus 10: moderate southward field, minor storm possible. "
		"Minus 10 to minus 20: strong southward field, storm at K5 to K6 level likely. "
		"Below minus 20: extreme value, severe storm highly probable. "
		"The longer the negative Bz persists, the stronger the storm."
	),

	"solar_wind": _(
		# Translators: Description for the Solar Wind speed parameter
		"Solar wind speed in km/s. "
		"300 to 400: background level, quiet. "
		"400 to 500: normal. "
		"500 to 600: elevated speed, minor disturbance possible with negative Bz. "
		"600 to 800: high speed, storm risk rises significantly with negative Bz. "
		"Above 800: extremely high speed, sign of a coronal hole or CME impact, storm nearly certain with negative Bz."
	),

	"proton_flux": _(
		# Translators: Description for the Proton Flux parameter
		"High-energy proton flux from the Sun in particle flux units (pfu). "
		"Below 1: background level, normal. "
		"1 to 10: slightly elevated, no threat. "
		"Above 10: proton event declared by NOAA. "
		"Above 100: strong event, polar cap absorption of HF signals, hazardous to satellites. "
		"Above 1000: extreme event, complete HF absorption on transpolar paths for several days."
	),

	"electron_flux": _(
		# Translators: Description for the Electron Flux parameter
		"Relativistic electron flux in the Earth's magnetosphere in pfu. "
		"Below 100: normal. "
		"100 to 1000: elevated, associated with moderate geomagnetic activity. "
		"1000 to 10000: high level, typical after storms. "
		"Above 10000: extreme level, hazardous to satellite electronics. "
		"Not directly critical for HF, but high values indicate increased auroral activity and degraded propagation on polar paths."
	),

	"helium_line": _(
		# Translators: Description for the Helium Line 304A parameter
		"Solar ultraviolet emission intensity in the ionized helium line at 304 angstroms, in arbitrary units. "
		"Below 80: low activity, weak ionospheric ionization. "
		"80 to 120: moderate activity. "
		"120 to 160: high activity, good ionization, dense F2 layer. "
		"Above 160: very high activity, correlates with SFI above 150. "
		"Used together with SFI to refine propagation forecasts, especially for MUF calculations."
	),

	"aurora": _(
		# Translators: Description for the Aurora index parameter
		"Auroral activity index in arbitrary units. "
		"1 to 3: weak activity, aurora only near the poles. "
		"4 to 5: moderate, aurora above 65 degrees latitude. "
		"6 to 7: strong, aurora reaches 60 to 62 degrees, Saint Petersburg in the zone. "
		"8 to 9: very strong, aurora reaches 55 to 57 degrees, Moscow in the zone. "
		"10: extreme activity. "
		"At values of 6 and above, aurora scatter propagation on VHF is possible, "
		"but HF propagation on polar paths degrades seriously."
	),

	"lat_degree": _(
		# Translators: Description for the Latitude Degree parameter
		"Geomagnetic latitude in degrees down to which auroral effects are currently present. "
		"Above 70: aurora near poles only, no interference. "
		"65 to 70: effects on sub-polar paths. "
		"60 to 65: Saint Petersburg and Scandinavia in the interference zone. "
		"Below 60: strong storm, effects reach mid-latitudes. "
		"Below 50: extreme storm, aurora visible across Europe down to Germany and below."
	),

	"geomag_field": _(
		# Translators: Description for the Geomagnetic Field status parameter
		"Current geomagnetic field status in plain text, based on K-index. "
		"QUIET: K 0 to 1, excellent conditions. "
		"UNSETTLD: K 2 to 3, minor disturbance. "
		"ACTIVE: K 4, slight degradation. "
		"MINOR STORM: K 5, noticeable degradation at high latitudes. "
		"MAJOR STORM: K 6 to 7, serious HF disruption. "
		"SEVERE STORM: K 8 to 9, communication on many bands impossible."
	),

	"signal_noise": _(
		# Translators: Description for the Signal Noise level parameter
		"Atmospheric and ionospheric noise level on HF bands on the S scale. "
		"S0: no noise, ideal conditions for weak signals. "
		"S1 to S2: low noise, good conditions. "
		"S3 to S4: moderate noise, weak stations hard to copy. "
		"S5 to S6: high noise, working weak stations is difficult. "
		"S7 and above: heavy noise, only strong stations workable."
	),

	"muf": _(
		# Translators: Description for the Maximum Usable Frequency parameter
		"Maximum Usable Frequency - the highest frequency at which ionospheric reflection is possible on the current path. "
		"Below 7 MHz: only 40 and 80 meters open. "
		"7 to 14 MHz: 40 meters open. "
		"14 to 21 MHz: 20 meters open. "
		"21 to 28 MHz: 15 meters open. "
		"Above 28 MHz: 10 meters open. "
		"No Report means no data available from the ionosonde."
	),
}


# HF band condition descriptions (page 2)
HF_BAND_DESCRIPTIONS: dict[str, str] = {
	"80m-40m": _(
		# Translators: Description for the 80-40 meter HF band conditions
		"Propagation conditions for 80 and 40 meters. "
		"These are low bands that work best at night due to D-layer absorption during the day. "
		"Good night conditions are typical even at solar minimum. "
		"Geomagnetic storms affect these bands most severely."
	),
	"30m-20m": _(
		# Translators: Description for the 30-20 meter HF band conditions
		"Propagation conditions for 30 and 20 meters. "
		"20 meters is the most reliable DX band, often open around the clock at moderate solar activity. "
		"30 meters is a WARC band, good for long paths especially in the evening."
	),
	"17m-15m": _(
		# Translators: Description for the 17-15 meter HF band conditions
		"Propagation conditions for 17 and 15 meters. "
		"Daytime bands that open well at moderate to high solar activity. "
		"At solar maximum, 15 meters can provide excellent worldwide coverage during the day."
	),
	"12m-10m": _(
		# Translators: Description for the 12-10 meter HF band conditions
		"Propagation conditions for 12 and 10 meters. "
		"High bands that require SFI above 120 to 150 to open. "
		"At solar maximum they can be open for many hours with very low power. "
		"During solar minimum they are mostly closed."
	),
}


# VHF condition descriptions (page 3)
VHF_DESCRIPTIONS: dict[str, str] = {
	"Aurora": _(
		# Translators: Description for Aurora VHF propagation
		"Aurora scatter propagation. Signals reflect off the ionized curtain of the northern lights. "
		"Active when K-index is 5 or above. "
		"Signals sound distorted and buzzy. Works mainly on 144 MHz and up. "
		"Paths are oriented north-south toward the auroral zone."
	),
	"Sporadic E": _(
		# Translators: Description for Sporadic E VHF propagation
		"Sporadic E propagation. Sudden dense ionization patches in the E layer at 90 to 120 km altitude. "
		"Can open VHF bands at 50, 70 and 144 MHz for short periods, sometimes with very strong signals. "
		"Most common in Europe from May to August and December to January. "
		"Unpredictable in timing and duration."
	),
}


def get_description(key: str) -> Optional[str]:
	"""Return the description for a given data key, or None if not found."""
	return DESCRIPTIONS.get(key)


def get_hf_description(band: str) -> Optional[str]:
	"""Return the description for a given HF band name, or None if not found."""
	return HF_BAND_DESCRIPTIONS.get(band)


def get_vhf_description(phenomenon_name: str) -> Optional[str]:
	"""Return the description for a given VHF phenomenon name, or None if not found."""
	# phenomenon names from XML may be like "vhf_aurora", "vhf_sporadic_e"
	# try direct match first, then normalize
	if phenomenon_name in VHF_DESCRIPTIONS:
		return VHF_DESCRIPTIONS[phenomenon_name]
	normalized = phenomenon_name.replace("vhf_", "").replace("_", " ").title()
	return VHF_DESCRIPTIONS.get(normalized)
