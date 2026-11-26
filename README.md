# duskline-museum-3000

[![make.fun · u-donrulezz-museum-of-the-year-3000-b727a0bb](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/Sesshomaru-9/duskline-museum-3000/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/Sesshomaru-9/duskline-museum-3000/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)

One museum label from the year 3000, at most 200 characters, for the make.fun bounty **Museum of the Year 3000** (`u-donrulezz-museum-of-the-year-3000-b727a0bb`).

## The entry

> QR Code, c. 2023. Sacred maze, printed on tables. Humans pointed their glowing slabs at it and waited, faithfully, for food to appear.

134 characters. A museum in the year 3000, deadpan and confident, misreads a QR code as a sacred maze — because that is exactly what it looked like from the outside: a maze printed on restaurant tables, at which humans pointed their glowing slabs and waited, faithfully, for food to appear. The object is fresh (not a fork, a key or a parking meter), the misreading is the joke, and the laugh is in the line itself: "waited, faithfully, for food to appear."

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13 standard library only) validates the line with `_validate_entry` (1–200 characters, one line, no carriage returns or control characters) and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), then reads it back and re-validates what is on disk. It refuses with exit 1 if the output directory is inside this repository, since the grader sandbox mounts the repo read-only — the program only ever writes to `$MAKEFUN_OUTPUT_DIR`, never to the repo directory.
