# World news in one image — Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/katherinecoco02-dotcom/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/katherinecoco02-dotcom/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entry for [make.fun](https://make.fun/bounty/news-image-20261120) bounty `news-image-20261120`:
sum up 20 November 2026's world news in one image.

## The image

A newspaper front page, 1024×1024, with the date at the top and six
stories from that day:

1. **World Court, The Hague** — ICJ rules Myanmar committed genocide
   against the Rohingya, the first such ruling against a state.
2. **Shenzhen summit** — Trump, Xi and Putin meet and issue a joint
   peace declaration, their first three-way summit.
3. **Markets fall, New York** — Anthropic closed its debut at $97, then
   fell about 10% on Friday to about $87; Bitcoin fell below $60,000,
   the first time since July; the S&P fell a fifth straight day.
4. **Kyiv attacked** — Russian overnight strikes hit Kyiv bridges;
   8 killed, 28 injured across nine regions.
5. **Riyadh hit** — A Houthi missile damages the Saudi wealth-fund
   tower in Riyadh's financial district.
6. **Ebola ends, Kenya** — Kenya discharges its last Ebola patient,
   37 days after its first case.

## How it is built

- `draw.py` draws `entry.png` with Pillow (local build tool only).
- `main.ts` (Node 22, standard library only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`, so both runs write identical bytes.

Test locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
