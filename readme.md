# Solar Monitor

NVDA add-on for radio amateurs. Provides quick access to solar activity data, HF band propagation conditions, and VHF propagation via a virtual keyboard interface.

## Features

* Solar indices: SFI, sunspot number, A-index, K-index, X-ray flux, solar wind, proton and electron flux, helium line, aurora index, geomagnetic field status, noise level, MUF
* HF band conditions for 80-40M, 30-20M, 17-15M, 12-10M with separate day and night values
* VHF propagation conditions: aurora scatter, sporadic-E for Europe and North America
* Virtual keyboard interface with no visual elements, designed entirely for screen readers
* Context-sensitive parameter descriptions (press D on any parameter)
* Data from hamqsl.com, updated automatically with 15-minute local cache
* Full Russian and English interface
* Configurable gesture via NVDA Input Gestures

## Installation

Download the `.nvda-addon` file from the [releases page](https://github.com/R1BQE/solarMonitor/releases) and open it. NVDA will ask to confirm installation and will restart.

## Usage

### Assigning a gesture

After installation, open NVDA menu, go to Preferences, then Input Gestures. Find the Solar Monitor category and assign any gesture to "Open or close the Solar Monitor virtual interface".

### Keyboard controls

Press the assigned gesture to open the virtual monitor. NVDA will announce "Solar Monitor. Loading data..." and then read the first parameter when data arrives.

Inside the monitor:

* Down arrow: move to the next parameter
* Up arrow: move to the previous parameter
* Right arrow: switch to the next page (Solar Indices, HF Band Conditions, VHF Conditions)
* Left arrow: switch to the previous page
* D: read a detailed description of the current parameter including normal ranges and their effect on radio propagation
* Assigned gesture again: close the monitor

### Pages

**Page 1: Solar Indices**

* SFI: Solar Flux Index
* Sunspots: Wolf number (sunspot count)
* A-index: 24-hour geomagnetic activity index
* K-index: current geomagnetic activity index with text status
* X-ray: solar X-ray flux class
* Magnetic field Bz: Z-component of interplanetary magnetic field in nanoteslas
* Solar wind: speed in km/s
* Proton flux: high-energy proton flux in pfu
* Electron flux: relativistic electron flux in pfu
* Helium line: solar UV emission at 304 angstroms
* Aurora: auroral activity index
* LatDegree: geomagnetic latitude of current auroral zone boundary in degrees
* Geomag field: geomagnetic field status in plain text (QUIET, UNSETTLD, ACTIVE, MINOR STORM, MAJOR STORM, SEVERE STORM)
* Noise level: HF band noise level on S scale
* MUF: Maximum Usable Frequency

**Page 2: HF Band Conditions**

Propagation quality for each band, separately for day and night:

* 80M-40M
* 30M-20M
* 17M-15M
* 12M-10M

Values: Good, Fair, Poor.

**Page 3: VHF Conditions**

* Aurora scatter propagation (Northern Hemisphere)
* Sporadic-E propagation for Europe, North America, and 50/70 MHz bands

### Parameter descriptions

Press D on any parameter to hear a detailed description. For solar indices this includes: what the parameter measures, normal range, threshold values, and effect on radio propagation. For HF and VHF conditions: which factors affect this band and what to expect.

## Data source

Data is fetched from [hamqsl.com](http://www.hamqsl.com/solarxml.php), a dedicated solar data service for radio amateurs. Data is cached locally for 15 minutes to avoid unnecessary requests to the server.

## Requirements

* NVDA 2025.1 or later
* Windows 10 or later
* Internet connection for data updates

## Author

r1bqe <r1bqe@mail.ru>

Amateur radio callsign: R1BQE, Saint Petersburg, Russia.

## License

GPL v2. See [COPYING.txt](https://github.com/R1BQE/solarMonitor/blob/master/COPYING.TXT) for details.

## Source code

[https://github.com/R1BQE/solarMonitor](https://github.com/R1BQE/solarMonitor)
