# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SpeechDictionaries, SymbolDictionaries

from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
	addon_name="solarMonitor",
	# Translators: Summary/title for this add-on
	addon_summary=_("Solar Monitor"),
	# Translators: Long description to be shown for this add-on on add-on information from add-on store
	addon_description=_(
		"Solar activity monitor for radio amateurs. "
		"Provides quick access to solar indices (SFI, K-index, X-ray, solar wind and more), "
		"HF band propagation conditions for 80-10 meters, "
		"and VHF propagation via a virtual keyboard interface designed for screen readers. "
		"No visual elements. Data from hamqsl.com."
	),
	addon_version="2025.7.15",
	# Translators: what's new content for the add-on version to be shown in the add-on store
	addon_changelog=_(
		"Исправлены мелкие ошибки в коде и документации. Обновлена версия."
	),
	addon_author="r1bqe <r1bqe@mail.ru>",
	addon_url="https://github.com/R1BQE/solarMonitor",
	addon_sourceURL="https://github.com/R1BQE/solarMonitor",
	addon_docFileName="readme.html",
	addon_minimumNVDAVersion="2025.1",
	addon_lastTestedNVDAVersion="2026.1.1",
	addon_updateChannel="stable",
	addon_license="GPL v2",
	addon_licenseURL="https://www.gnu.org/licenses/old-licenses/gpl-2.0.html",
)

pythonSources: list[str] = [
	"addon/globalPlugins/solarMonitor/*.py",
]

i18nSources: list[str] = pythonSources + ["buildVars.py"]

excludedFiles: list[str] = []

baseLanguage: str = "en"

markdownExtensions: list[str] = []

brailleTables: BrailleTables = {}

symbolDictionaries: SymbolDictionaries = {}

speechDictionaries: SpeechDictionaries = {}
