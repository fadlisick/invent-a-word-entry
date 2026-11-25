"""draftgrave: one coined word and its definition, written out for judging.

The Invent a Word We Need bounty asks for a single invented English word
plus a one-line definition. This program carries that line and writes it
to the file the harness reads, nothing more.
"""

import os, sys

COINAGE = "draftgrave — a long message you typed out, then deleted instead of sending."
CEILING = 140
OUTFILE = "entry.txt"
OUTDIR_ENV = "MAKEFUN_OUTPUT_DIR"
OUTDIR_DEFAULT = "/output"


def outdir():
    chosen = os.environ.get(OUTDIR_ENV)
    if chosen:
        return chosen
    return OUTDIR_DEFAULT


def check_coinage(line):
    stripped = line.strip()
    if not stripped:
        raise SystemExit("coinage is empty")
    if line != stripped:
        raise SystemExit("coinage has leading or trailing whitespace")
    if len(line) > CEILING:
        raise SystemExit("coinage is longer than the 140 character gate")
    return line


def deliver(line):
    folder = outdir()
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, OUTFILE)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    with open(path, encoding="utf-8") as handle:
        stored = handle.read()
    if stored != line:
        raise SystemExit("entry.txt does not match the coinage")
    return path


def main():
    line = check_coinage(COINAGE)
    path = deliver(line)
    sys.stdout.write("wrote entry.txt (%d chars) to %s\n" % (len(line), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
