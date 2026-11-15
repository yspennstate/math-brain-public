"""coin_check.py - second, independent evaluation of fei_coin output lines, and conversion of a library gate.

  python coin_check.py W_table.txt FILE [FILE ...] [--top N] [--emit OUT.txt]
      for the N best lines (by slack) of each file: expand the labelled function to its explicit truth table on
      m + (coins used) inputs, take the full Walsh transform, and print value / slack next to the file's numbers.
      --emit appends the expanded gates as library lines "n hex".
  python coin_check.py --fromlib LIB.txt[:LINE] M OUT.lab
      write the gate (n inputs, the low M are the main ones, each setting of them constant or one coin) as "m k labels".
"""
import sys

import numpy as np


def walsh(tt):
    a = 1.0 - 2.0 * tt.astype(np.float64)
    h = 1
    while h < len(a):
        a = a.reshape(-1, 2, h)
        lo, hi = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :] = (lo + hi) / 2
        a[:, 1, :] = (lo - hi) / 2
        a = a.reshape(-1)
        h *= 2
    return a


def popcounts(n):
    c = np.zeros(1, dtype=np.int64)
    for _ in range(n):
        c = np.concatenate([c, c + 1])
    return c


def expand(m, labels):
    """labels: list of ints, one per x.  Returns (n, tt) with the used coins renumbered, tt index = x + (y << m)."""
    used = sorted({(l - 2) // 2 for l in labels if l >= 2})
    pos = {j: t for t, j in enumerate(used)}
    kk = len(used)
    N = 1 << m
    tt = np.zeros((1 << kk, N), dtype=np.uint8)
    ys = np.arange(1 << kk)
    for x, l in enumerate(labels):
        if l == 1:
            tt[:, x] = 1
        elif l >= 2:
            bit = (ys >> pos[(l - 2) // 2]) & 1
            tt[:, x] = bit if l % 2 == 0 else 1 - bit
    return m + kk, tt.reshape(-1)


def score(n, tt, wx, wy):
    a = walsh(tt)
    w = a * a
    size = popcounts(n)
    mu = a[0]
    var = 1 - mu * mu
    wn = w.copy()
    wn[0] = 0
    nz = wn > 0
    H = float(-(wn[nz] * np.log2(wn[nz])).sum())
    I = float((wn * size).sum())
    G = H / var + np.log2(var)
    J = I / var
    c = float(np.interp(0.0, wx, wy))
    p = (1 - mu) / 2
    W = c if mu == 0 else float(np.interp(np.log2(p / (1 - p)), wx, wy))
    return (G + W) / J, G - c * J + W, G, J, mu, H, I


def tohex(tt):
    b = np.packbits(tt, bitorder="little").tobytes()
    return "%x" % int.from_bytes(b, "little")


def fromlib(spec, m, out):
    path, _, ln = spec.partition(":")
    lines = [l.split() for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    n, hx = int(lines[int(ln or 0)][0]), lines[int(ln or 0)][1]
    tab = int(hx, 16)
    bits = np.unpackbits(np.frombuffer(tab.to_bytes((1 << n) // 8, "little"), dtype=np.uint8), bitorder="little")
    k = n - m
    T = bits.reshape(1 << k, 1 << m)
    ys = np.arange(1 << k)
    labs = []
    for x in range(1 << m):
        col = T[:, x]
        if not col.any():
            labs.append(0)
        elif col.all():
            labs.append(1)
        else:
            for j in range(k):
                bit = (ys >> j) & 1
                if np.array_equal(col, bit):
                    labs.append(2 + 2 * j)
                    break
                if np.array_equal(col, 1 - bit):
                    labs.append(3 + 2 * j)
                    break
            else:
                raise SystemExit("x = %d depends on the coins through more than one coin" % x)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("%d %d %s\n" % (m, k, "".join(chr(48 + l) for l in labs)))
    print("wrote", out, "m", m, "k", k, "coin points", sum(1 for l in labs if l >= 2))


def main():
    if sys.argv[1] == "--fromlib":
        fromlib(sys.argv[2], int(sys.argv[3]), sys.argv[4])
        return
    args = sys.argv[1:]
    top, emit = 3, None
    if "--top" in args:
        i = args.index("--top")
        top = int(args[i + 1])
        del args[i:i + 2]
    if "--emit" in args:
        i = args.index("--emit")
        emit = args[i + 1]
        del args[i:i + 2]
    t = np.loadtxt(args[0], comments="#")
    wx, wy = t[:, 0], t[:, 1]
    for f in args[1:]:
        rows, m = [], None
        for line in open(f, encoding="utf-8", errors="replace"):
            if line.startswith("# coin"):
                m = int(line.split("m=")[1].split()[0])
                continue
            a = line.split()
            if line.startswith("#") or len(a) < 12:
                continue
            rows.append((float(a[3]), float(a[2]), int(a[0]), a[-1]))
        if not rows:
            print(f, "no lines")
            continue
        rows.sort(reverse=True)
        seen = set()
        print("%s  lines %d  best slack in file %+.12f" % (f, len(rows), rows[0][0]))
        shown = 0
        for sl, val, run, ls in rows:
            if ls in seen:
                continue
            seen.add(ls)
            labels = [ord(ch) - 48 for ch in ls]
            n, tt = expand(m, labels)
            if n > 24:
                print("   run %d: %d inputs, too large to expand here; file slack %+.12f" % (run, n, sl))
            else:
                v2, s2, G, J, mu, H, I = score(n, tt, wx, wy)
                bal = "  H/(I-1) %.12f" % (H / (I - 1)) if mu == 0 else ""
                print("   run %3d  n %2d  file value %.12f slack %+.12f | explicit value %.12f slack %+.12f  G %.6f J %.6f mean %+.6f%s  diff %.1e" % (
                    run, n, val, sl, v2, s2, G, J, mu, bal, abs(v2 - val)))
                if emit and n <= 20:
                    with open(emit, "a", encoding="utf-8") as fh:
                        fh.write("%d %s\n" % (n, tohex(tt)))
            shown += 1
            if shown >= top:
                break


if __name__ == "__main__":
    main()
