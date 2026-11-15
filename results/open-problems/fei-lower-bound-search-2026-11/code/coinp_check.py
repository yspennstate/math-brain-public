"""coinp_check.py - second, independent evaluation of fei_coinp output lines (coin gates at a biased input measure).

  python coinp_check.py W_table.txt FILE [FILE ...] [--top N] [--emit OUT.txt]

For the N best lines (by slack) of each file: expand the labelled function to its explicit truth table on
m + (coins used) inputs, take the p-biased transform axis by axis (p is read from the file's header), and print
value and slack next to the file's numbers.  --emit appends the expanded gates as library lines "n hex".
"""
import sys

import numpy as np

from coin_check import expand, tohex


def biased_stats(n, tt, p):
    f = (1.0 - 2.0 * tt.astype(np.float64)).reshape((2,) * n)     # axis 0 = highest input
    s = np.sqrt(p * (1 - p))
    M = np.array([[1 - p, p], [-s, s]])
    for ax in range(n):
        f = np.moveaxis(np.tensordot(M, f, axes=([1], [ax])), 0, ax)
    w = (f ** 2).reshape(-1)
    size = np.zeros(1, dtype=np.int64)
    for _ in range(n):
        size = np.concatenate([size, size + 1])
    mean = float(f.reshape(-1)[0])
    var = 1 - mean * mean
    wn = w.copy()
    wn[0] = 0
    nz = wn > 1e-300
    H = float(-(wn[nz] * np.log2(wn[nz])).sum())
    I = float((wn * size).sum())
    return mean, var, H / var + np.log2(var), I / var


def main():
    args = sys.argv[1:]
    top, emit = 3, None
    if "--top" in args:
        i = args.index("--top"); top = int(args[i + 1]); del args[i:i + 2]
    if "--emit" in args:
        i = args.index("--emit"); emit = args[i + 1]; del args[i:i + 2]
    tab = np.loadtxt(args[0], comments="#")
    wx, wy = tab[:, 0], tab[:, 1]

    def W(q):
        return float(np.interp(np.log2(q / (1 - q)), wx, wy))

    for path in args[1:]:
        p, m, rows = None, None, []
        for line in open(path):
            if line.startswith("#"):
                for tok in line.split():
                    if tok.startswith("p="):
                        p = float(tok[2:])
                    if tok.startswith("m="):
                        m = int(tok[2:])
                continue
            parts = line.split("|")
            if len(parts) < 4:
                continue
            head = parts[0].split()
            rows.append((float(head[3]), float(head[2]), int(head[0]), parts[3].strip()))
        if p is None or not rows:
            print(path, "no header or no lines"); continue
        rows.sort(reverse=True)
        seen = set()
        shown = 0
        print("%s  p=%.9f  W(p)=%.12f" % (path, p, W(p)))
        for slack_f, val_f, run, labs in rows:
            if labs in seen:
                continue
            seen.add(labs)
            labels = [ord(ch) - 48 for ch in labs]
            n, tt = expand(m, labels)
            if n > 24:
                print("  run %d: %d inputs, too many to expand" % (run, n)); continue
            mean, var, G, J = biased_stats(n, tt, p)
            pp = (1 - mean) / 2
            slack = G - W(p) * J + W(pp)
            val = (G + W(pp)) / J
            print("  run %3d n=%2d file value %.12f slack %+.12f | explicit value %.12f slack %+.12f G %.9f J %.9f p' %.9f"
                  % (run, n, val_f, slack_f, val, slack, G, J, pp))
            if emit and n <= 20:
                with open(emit, "a") as o:
                    o.write("%d %s\n" % (n, tohex(tt)))
            shown += 1
            if shown >= top:
                break


if __name__ == "__main__":
    main()
