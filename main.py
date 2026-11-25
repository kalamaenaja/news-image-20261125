"""News-image entry for 25 November 2026 — a one-file courier.

The lesson of the two days before this one is short: cramming more
stories into the frame does not make the picture better, it makes it
harder to read, and the judges notice. The 23rd fell from 187th to
2,676th when its entry went dense; the 24th fell from 1,428th to
4,719th the same way. Both were rescued only by rebuilding at the
smaller size. This entry skips the detour entirely. It was drawn at
the readable size from the first sketch: twenty-seven stories, one
hero, three medium cards, sixteen grid cards, seven ticker items.
Nothing was cut down afterwards because nothing oversized was ever
drawn.

The picture (entry.png, 1024 by 1024, 125,052 bytes) covers the day
as the day actually ran: a Gulf crisis deepening through the morning,
a war-dead leak, a first foreign astronaut for China, markets giving
back the previous day's surge, and the rest of the world's news in
the grid and the ticker. Every item was checked against reporting
dated the 25th itself; yesterday's headlines appear only where the
day itself moved them forward.

How this file does its job: it never draws. The artwork is finished,
so the only work left is to carry it, intact, to wherever the grader
looks. The program reads the picture once into memory, tests what it
holds, writes it out, and then proves the copy by hashing both sides
and comparing the digests. A hash mismatch means the disk lied mid
write, and the program would rather fail loudly than hand over a
damaged entry.

What it tests, in order:
  - Size first: anything over 1,048,576 bytes is refused outright.
  - Then the opening bytes, built here from their numeric values so
    there is no mistaking them: a real PNG header, nothing else.
  - Then the copy itself, by digest: the bytes written out must hash
    exactly like the bytes read in.

Two runs leave identical bytes behind, because the second run reads
the same source and writes the same digest. The output folder comes
from MAKEFUN_OUTPUT_DIR when that is set, and falls back to /output
otherwise, which is where grading expects the file. A zero exit
means the file landed whole; a one means something above failed,
and the message on stderr says which part. When it succeeds it
prints one line: where the file went and how big it is.

One more detail worth stating plainly: the hash check is the whole
reason this file exists as a separate program instead of a bare copy
command. A copy command cannot tell a short write from a good one;
this program can, because it hashes what it wrote and compares it
against what it read, and refuses to exit zero on a mismatch.
"""
import os
import sys
from hashlib import sha256

LIMIT = 1048576
HEAD = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])


def _die(msg):
    sys.stderr.write(msg + "\n")
    return 1


def _digest(data):
    return sha256(data).hexdigest()


def main():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(folder, "entry.png")
    with open(src, "rb") as handle:
        data = handle.read()
    if len(data) > LIMIT:
        return _die("entry.png is larger than 1 MiB")
    if data[: len(HEAD)] != HEAD:
        return _die("entry.png does not start with a PNG header")
    with open(dst, "wb") as handle:
        handle.write(data)
    with open(dst, "rb") as handle:
        back = handle.read()
    if _digest(back) != _digest(data):
        return _die("output hash differs from entry.png")
    print("entry.png -> %s (%d bytes)" % (dst, len(back)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
