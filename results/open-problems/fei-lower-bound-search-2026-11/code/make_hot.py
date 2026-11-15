"""make_hot.py - bases for the biased coin search: the matching cores and small gates, padded with idle inputs.

Writes hot_bases.txt (library lines "m hex") and hot_bases.tags (one tag per line, same order).
A gate padded by t idle inputs is its hex string repeated 2^t times.
usage: python make_hot.py SEEDDIR OUTDIR
"""
import os
import sys

PLAN = [("k33", 0), ("k33", 1), ("k33", 2), ("pmk4", 2), ("pmk4", 3), ("pmk4", 4), ("cube", 0), ("octa", 0),
        ("entry5", 3), ("entry5", 5), ("nor2", 6), ("nor2", 8), ("nand2", 6), ("nand2", 8)]


def main():
    sd, od = sys.argv[1], sys.argv[2]
    lines, tags = [], []
    for name, pad in PLAN:
        with open(os.path.join(sd, "seed_%s.txt" % name), encoding="utf-8") as fh:
            n, hx = fh.readline().split()[:2]
        n = int(n)
        if n < 2:
            continue
        hx = hx.zfill(max(1, (1 << n) // 4))
        lines.append("%d %s" % (n + pad, hx * (1 << pad)))
        tags.append("%s%s" % (name, ("x%d" % pad) if pad else ""))
    with open(os.path.join(od, "hot_bases.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(od, "hot_bases.tags"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(tags) + "\n")
    for t, l in zip(tags, lines):
        print(t, l[:50])


if __name__ == "__main__":
    main()
