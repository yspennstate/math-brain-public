"""Combine per-h0 residues (lines 'k=14 N=n h0=h res=[a, b, c]') into L(N) and compare."""
import re, sys
sys.path.insert(0, r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad")
from lattice_np import PRIMES, crt

KNOWN = {5: 2689701322578797154997026, 6: 26300360702505389408263341}
txt = open(sys.argv[1], encoding="utf-8").read()
pieces = {}
for N, h, a, b, c in re.findall(r"N=(\d+) h0=(\d+) res=\[(\d+), (\d+), (\d+)\]", txt):
    pieces[(int(N), int(h))] = [int(a), int(b), int(c)]
for N in sorted({n for n, _ in pieces}):
    hs = range(N // 2 + 1)
    if not all((N, h) in pieces for h in hs):
        print(f"N={N}: incomplete")
        continue
    tot = [0, 0, 0]
    for h in hs:
        w = 1 if 2 * h == N else 2
        tot = [(t + w * r) % p for t, r, p in zip(tot, pieces[(N, h)], PRIMES)]
    v = crt(tot)
    print(f"N={N}: L={v}", "matches known" if KNOWN.get(N) == v else ("(no known value)" if N not in KNOWN else "MISMATCH"))
