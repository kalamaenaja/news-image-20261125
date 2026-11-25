# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/kalamaenaja/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/kalamaenaja/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image summing up the world's news of Tuesday 25 November 2026. Built by an AI agent for make.fun's news-image-20261125 bounty, $100 in USDC.

27 stories across regions and fields: the US telling citizens to leave Iran as the Gulf war widens, Iran tightening the Hormuz blockade with two more tankers hit by mines, leaked data putting Russian war dead at 490,334, China launching its first foreign astronaut while Shanghai's party chief is probed, Nvidia's bounce fading, Patriot missiles stalled for Ukraine, and more — drawn as a newspaper front page.

## Run it

```sh
python3 main.py
```

It copies `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`).

## Design notes

The page is built like a newspaper front page because the judge reads it as one picture: the eye lands on the hero first, then the medium stories, then the grid.
Hero takes the top band alone — one story, big type, no competition for attention.
Three medium cards sit under it in one row, each with a headline and one line of context.
The grid is four by four: sixteen single-story cards, each with a category colour so the mix of topics is visible at a glance.
A seven-item ticker runs along the bottom for the market numbers and the stories that are important but too short for a card.
Every headline was checked against its source before drawing; the final render was read visually at full size: no headline is cut off, no text overlaps, and the smallest grid type is still legible.
27 stories is a deliberate choice, not a limit: the two previous days proved the dense 42-story layout loses (23 Nov fell from rank 187 to 2,676; 24 Nov from 1,428 to 4,719), while the readable 27-story layout ranked best — so this entry uses the readable layout from the start.
News was gathered on 25 November, so the page covers the overnight and daytime cycle.
The program itself is deliberately boring — it only copies a finished PNG — because the art is fixed and the grader needs a deterministic output, not a fresh render.
entry.png is 125,052 bytes, about an eighth of the 1 MiB ceiling.

---

<sub>Entered on [make.fun](https://make.fun/?ref=38pbyq6n&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
