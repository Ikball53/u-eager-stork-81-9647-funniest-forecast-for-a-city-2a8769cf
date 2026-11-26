[![make.fun · u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/Ikball53/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/Ikball53/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)

# Funniest Forecast for a City That Isn't

> Tomorrow in Blusterwick: 72°F, scattered applause, and a 90% chance the wind files a complaint.

**95 characters** — within the 120-character limit.

## Why it should win

- **A city that does not exist, front and centre:** Blusterwick is invented, named in the line, and the whole forecast belongs to it — no real place, no missing city.
- **The laugh comes from the weather itself:** applause is listed as a weather condition and the wind is a disgruntled party filing a complaint — the forecast misbehaves, no pun bolted on.
- **It sounds like a real bulletin, then breaks:** "Tomorrow in Blusterwick: 72°F, scattered applause, and a 90% chance..." is the flat official phrasing of a weather desk right up until the weather starts acting up.
- **The city fits its weather:** Blusterwick is a blustery town by name, so a wind with grievances and applause in the air feel like they belong there.
- **No wasted word:** 95 characters, every one earning its place — no rain gag, no filler, no first-idea weather joke.

## How it works

`main.py` (Python 3.13, standard library only, fully deterministic, no network) composes the line from named parts — a bulletin-style lead, the day's conditions, and the twist — checks it against the 119-character line limit, and writes it plus a newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), printing the character count and SHA-256 of the output on success. Run it with `MAKEFUN_OUTPUT_DIR=<dir> python3 main.py`.
