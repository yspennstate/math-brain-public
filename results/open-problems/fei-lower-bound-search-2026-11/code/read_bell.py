"""read_bell.py - best Bellman value of each fei_bias output against the value table at the job's bias.
usage: python read_bell.py W_table.txt FILE [FILE ...]
A dictator gate scores exactly W(p), so only a positive excess (best - W(p)) matters.
"""
import sys

import numpy as np


def main():
    tabs = {}

    def W(p, name):
        # the table the job itself used (named in its header) when it is here, else the one on the command line
        if name not in tabs:
            try:
                tabs[name] = np.loadtxt(name, comments="#")
            except OSError:
                tabs[name] = np.loadtxt(sys.argv[1], comments="#")
        t = tabs[name]
        return float(np.interp(np.log2(p / (1 - p)), t[:, 0], t[:, 1]))

    for f in sys.argv[2:]:
        p, best, n, wname = None, None, 0, sys.argv[1]
        with open(f, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if line.startswith("# bellman"):
                    p = float(line.split("p=")[1].split()[0])
                    wname = line.split("wfile=")[1].split()[0]
                elif not line.startswith("#"):
                    a = line.split()
                    if len(a) > 7:
                        n += 1
                        v = float(a[2])
                        if best is None or v > best[0]:
                            best = (v, float(a[4]), float(a[5]), float(a[6]))
        if best and p:
            w = W(p, wname)
            print("%-34s runs %4d p %.6f best %.9f W(p) %.9f excess %+.6f  G %.4f J %.4f mean %+.5f  %s" % (
                f, n, p, best[0], w, best[0] - w, best[1], best[2], best[3], wname))


if __name__ == "__main__":
    main()
