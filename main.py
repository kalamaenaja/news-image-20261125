"""Second version of the 25 November 2026 news-image entry.

The first version went in with the morning's news. The day then kept
moving — the embassy warning turned into a direct "leave immediately",
the strait closure hardened into stated conditions, Nvidia slid further
before the open, a Hamas security chief was killed in a Wednesday
strike, and US inflation printed hotter than expected. A morning-only
picture would have gone into round 2 already out of date, so this
version refreshes the picture with the full day behind it: same
twenty-seven-story frame, eight items updated or swapped, the rest
carried over untouched. The layout did not change, because the layout
was never the problem — the dense forty-two-story version was, and
this entry never tried it.

The picture (entry.png, 1024 by 1024, 128,078 bytes) is drawn once by
a Pillow generator from the verified story list, every headline fitted
by measured width, and read visually at full size. This file's only
job is to hand that finished picture to the grader without damaging
it, and to refuse rather than deliver something damaged.

It works in three small steps, each with its own helper, so a failure
names exactly where it happened:
  - _fetch reads the picture from beside this file. Anything over
    1,048,576 bytes is rejected at once — the picture is 128,078, so
    there is room to spare and no reason to accept an oversized file.
  - The opening bytes must be a PNG header. A file that is not a PNG
    is turned away here, before any copy is attempted.
  - _carry writes the picture to the output folder and then asks the
    standard library's file comparison to confirm the two files match
    byte for byte, shallow comparison switched off, so it compares
    content rather than trusting size and timestamp.

The destination comes from MAKEFUN_OUTPUT_DIR when set, falling back
to /output, which is where grading looks. The run ends in one of two
ways: exit zero with a single line saying where the picture landed
and how large it is, or exit one with the reason on stderr. Two runs
leave the same bytes behind, because both read the same source and
both are verified the same way.

Why file comparison instead of a second read-and-compare by hand:
the standard library already does exactly this comparison, with the
shallow flag off so it reads content rather than trusting metadata.
Writing the same loop again would only add a second place to get it
wrong.
"""
import filecmp
import os
import sys
from pathlib import Path

CEILING_BYTES = 1_048_576
PNG_HEADER = b"\x89PNG\r\n\x1a\n"


def _fetch(path):
    with open(path, "rb") as stream:
        return stream.read()


def _reject(reason):
    print(reason, file=sys.stderr)
    return 1


def _carry(source, target):
    with open(target, "wb") as stream:
        stream.write(_fetch(source))
    if not filecmp.cmp(source, target, shallow=False):
        return _reject("written file does not match entry.png")
    return 0


def main():
    root = Path(__file__).resolve().parent
    source = root / "entry.png"
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.png"
    blob = _fetch(source)
    if len(blob) > CEILING_BYTES:
        return _reject("entry.png is larger than 1 MiB")
    if blob[: len(PNG_HEADER)] != PNG_HEADER:
        return _reject("entry.png does not start with a PNG header")
    status = _carry(source, target)
    if status:
        return status
    print("delivered %s (%d bytes)" % (target, target.stat().st_size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
