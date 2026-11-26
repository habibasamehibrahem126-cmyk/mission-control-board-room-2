# Launch data: what is in each file

Two files describe Falcon 9 launches. One row is one launch. They come from two different sources, so they use different names, formats and coverage.

| File | Source | Rows | Period |
|---|---|---|---|
| `launches_api.csv` | The SpaceX public API | 90 | June 2010 to November 2020 |
| `launches_wikipedia.csv` | The Wikipedia page "List of Falcon 9 and Falcon Heavy launches" (archived revision) | 121 | June 2010 to June 2021 |

Both files are given as collected. Nothing has been filled in, converted or labelled.

## `launches_api.csv` (17 columns)

| Column | Meaning | Values |
|---|---|---|
| `FlightNumber` | The launch's number in the API's list of all SpaceX launches. It starts at 6 because the first five launches used the older Falcon 1 rocket. A gap means that launch is not in this file. | 6 to 106 |
| `Date` | Launch date in UTC | `YYYY-MM-DD` |
| `BoosterVersion` | The rocket model | Always `Falcon 9` |
| `PayloadMass` | Mass of the payload (what the rocket carries) in kilograms. 5 launches have no value. | 350 to 15,600 |
| `Orbit` | The orbit the payload was sent to. See the orbit table below. | 11 codes |
| `LaunchSite` | The launch pad | `CCAFS SLC 40` (Cape Canaveral), `KSC LC 39A` (Kennedy Space Center), `VAFB SLC 4E` (Vandenberg) |
| `Outcome` | What happened to the first stage after launch, written as two words: `<landing result> <landing place>`. First word: `True` the landing succeeded, `False` it failed, `None` no result. Second word: `Ocean` a landing in the ocean, `RTLS` a ground pad at the launch site (return to launch site), `ASDS` a drone ship at sea (autonomous spaceport drone ship), `None` no place. | `True ASDS`, `None None`, `True RTLS`, `False ASDS`, `True Ocean`, `False Ocean`, `None ASDS`, `False RTLS` |
| `Flights` | Which flight this is for this booster: 1 is its first flight, 2 its second, and so on | 1 to 6 |
| `GridFins` | Whether the booster had grid fins (the small steering fins) | `True` / `False` |
| `Reused` | Whether the booster had already flown before this launch | `True` / `False` |
| `Legs` | Whether the booster had landing legs | `True` / `False` |
| `LandingPad` | The ID code of the landing pad that was used. It is a code, not a name. Blank when no pad was used, which is a real answer and not a mistake. | 5 different codes, 26 blank |
| `Block` | The design version of the booster | 1 to 5 |
| `ReusedCount` | How many times this booster has been reused in total. The value is the same on every row of the same booster, so it is not the count at the time of that launch. | 0 to 5 |
| `Serial` | The booster's serial number. A booster that flew several times appears on several rows. | for example `B1049` |
| `Longitude` | Longitude of the launch site, in degrees | -120.6 to -80.6 |
| `Latitude` | Latitude of the launch site, in degrees | 28.6 to 34.6 |

## `launches_wikipedia.csv` (11 columns)

All values are text, exactly as they appear on the page.

| Column | Meaning | Examples |
|---|---|---|
| `Flight No.` | The launch's number in Wikipedia's list. It is not the same numbering as `FlightNumber` in the API file. | `1` to `121` |
| `Launch site` | The launch site, abbreviated. The same pad can be written in more than one way. | `CCAFS`, `CCSFS`, `Cape Canaveral`, `KSC`, `VAFB` |
| `Payload` | The name of the payload or mission | `SpaceX CRS-22` |
| `Payload mass` | The payload mass as written on the page, with the unit. `0` means the page gave no value. | `3,328 kg`, `~5,000 kg` |
| `Orbit` | The orbit, written in words or letters | `LEO`, `GTO`, `Polar`, `Sub-orbital` |
| `Customer` | The organisation that ordered the launch. `SpaceX` for its own missions. | `NASA`, `Sirius XM` |
| `Launch outcome` | Whether the launch itself succeeded. This is about the mission, not about the booster landing. | `Success`, `Failure` |
| `Version Booster` | The booster version and serial number, as scraped from the page. Some values contain leftover marks from footnotes. | `F9 B5B1046.2` |
| `Booster landing` | What happened to the booster, as written on the page. `Controlled` and `Uncontrolled` describe a descent into the ocean without a landing. `Precluded` means a landing was ruled out in advance. | `Success`, `Failure`, `No`, `No attempt`, `Controlled`, `Uncontrolled`, `Precluded` |
| `Date` | Launch date in words | `4 June 2010` |
| `Time` | Launch time in UTC | `18:45` |

## Orbit codes (API file)

| Code | Orbit |
|---|---|
| `LEO` | Low Earth orbit, 2,000 km altitude or less |
| `VLEO` | Very low Earth orbit, below about 450 km |
| `ISS` | The orbit of the International Space Station, which is in low Earth orbit |
| `PO` | Polar orbit, passing over or near both poles |
| `SSO`, `SO` | Sun-synchronous orbit, a nearly polar orbit. `SO` is used for the same orbit in this course. |
| `MEO` | Medium Earth orbit, between 2,000 km and the geosynchronous height |
| `GTO` | Geosynchronous transfer orbit, on the way to a geosynchronous orbit about 35,786 km above the equator |
| `GEO` | Geostationary orbit, circular, about 35,786 km above the equator |
| `HEO` | Highly elliptical orbit |
| `ES-L1` | Earth-Sun Lagrange point 1, between the Earth and the Sun |

## How the two files relate

- They describe the same launches, so launches that appear in both can be matched by date. The API file holds 90 of them. The Wikipedia file has 31 more, because it covers launches up to June 2021 and includes launches that the API file leaves out.
- They do not always agree. The same launch can be described with different words, different orbit names or a different landing result.
- Each file has information the other lacks. The API file has booster details such as block, grid fins, legs and serial number, and the site coordinates. The Wikipedia file has the payload name, the customer, the launch time and the mission outcome.
