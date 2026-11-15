"""make_seeds.py - write seed files for fei_bias (first line "n0 hex", hex high index first as fei_bias prints it).
usage: python make_seeds.py ZOO_LIB.txt ZOO_RUN.txt REC18.txt OUTDIR
ZOO_LIB has "n hex" lines in the order zoo.gates() yields; the names are taken from zoo.gates() itself.
"""
import os
import sys

from zoo import gates


def hexof(U, n):
    tab = 0
    for x, b in enumerate(U):
        if b:
            tab |= 1 << x
    return "%0*x" % (max(1, (1 << n) // 4), tab)


def main():
    out = sys.argv[4]
    os.makedirs(out, exist_ok=True)
    want = {"match_K3,3": "k33", "pm_cube": "cube", "pm_octa": "octa", "match_K4,4": "k44", "pm_K4": "pmk4"}
    for name, n, U in gates():
        if name in want:
            with open(os.path.join(out, "seed_%s.txt" % want[name]), "w", encoding="utf-8") as fh:
                fh.write("%d %s\n" % (n, hexof(U, n)))
    with open(sys.argv[3], encoding="utf-8") as fh:
        n, hx = fh.readline().split()
    with open(os.path.join(out, "seed_rec18.txt"), "w", encoding="utf-8") as fh:
        fh.write("%s %s\n" % (n, hx.zfill((1 << int(n)) // 4)))
    for nm, n, hx in (("entry5", 5, "a8a8a888"), ("nor2", 2, "1"), ("nand2", 2, "7")):
        with open(os.path.join(out, "seed_%s.txt" % nm), "w", encoding="utf-8") as fh:
            fh.write("%d %s\n" % (n, hx))
    print(sorted(os.listdir(out)))


if __name__ == "__main__":
    main()
