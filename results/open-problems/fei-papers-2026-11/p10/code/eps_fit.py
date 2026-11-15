"""Read eps_scan_out.txt; for each k compare the ratio with the P = 1/2 value plus log2(eps 2^m)."""
import math, sys
rows = {}
for line in open(sys.argv[1] if len(sys.argv) > 1 else "eps_scan_out.txt", encoding="utf-8"):
    p = line.split()
    if len(p) == 5 and p[0].isdigit():
        rows.setdefault(int(p[0]), []).append((float(p[1]), float(p[2])))
print(f"{'k':>4} {'eps':>10} {'log2(eps 2^m)':>14} {'ratio-R_half':>13} {'2m-ratio':>9} {'slope':>7}")
for k, rs in sorted(rows.items()):
    m = (k - 1) // 2
    half = [r for e, r in rs if e == 0.0][0]
    rs = sorted((e, r) for e, r in rs if e > 0)
    prev = None
    for e, r in rs:
        x = math.log2(e) + m
        s = "" if prev is None else f"{(r - prev[1]) / (x - prev[0]):7.3f}"
        print(f"{k:>4} {e:>10.3e} {x:>14.3f} {r - half:>13.4f} {2*m - r:>9.4f} {s:>7}")
        prev = (x, r)
