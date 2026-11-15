"""Describe extremal truth tables found by fei_p2: decode the integer, list the
ON-set (inputs where f = -1 in the +-1 convention, i.e. bit set), find
irrelevant coordinates, and print the per-coordinate ratios Delta_i H / Inf_i.
Usage: fei_describe.py N INT [INT ...]  or  fei_describe.py --json file.json --n N
"""
import json, sys
import numpy as np
import fei_p2


def describe(n, val):
    cube = fei_p2.Cube(n)
    F = fei_p2.tables_from_ints([val], n)
    s = cube.stats(F)
    on = [x for x in range(1 << n) if (val >> x) & 1]
    irrelevant = [i for i in range(n) if not s["relevant"][0, i]]
    ratios = []
    for i in range(n):
        if s["relevant"][0, i]:
            ratios.append((i, float(s["dH"][0, i]), float(s["Inf"][0, i]), float(s["dH"][0, i] / s["Inf"][0, i])))
    k = len(on)
    print(f"n={n} int={val} |ON|={k} (f=-1 on {k} inputs; f=+1 on {(1<<n)-k})  H={s['H'][0]:.6f} I={s['I'][0]:.6f} H/I={s['H'][0]/s['I'][0]:.6f} rho0={s['rho0'][0]:.6f} pmax={s['pmax'][0]:.4f} W<=1={s['w1'][0]:.4f}")
    print("   ON-set (as bit strings, LSB = x_0):", [format(x, f'0{n}b')[::-1] for x in on][:24], "..." if k > 24 else "")
    print("   irrelevant coords:", irrelevant)
    for i, dh, inf, r in ratios:
        print(f"   coord {i}: dH={dh:+.6f} Inf={inf:.6f} ratio={r:+.4f}")


if __name__ == "__main__":
    if sys.argv[1] == "--json":
        data = json.load(open(sys.argv[2], encoding="utf-8"))
        n = int(sys.argv[4])
        seen = set()
        for rho, val in data["best"][:10]:
            if val in seen:
                continue
            seen.add(val); describe(n, val)
    else:
        n = int(sys.argv[1])
        for v in sys.argv[2:]:
            describe(n, int(v))
