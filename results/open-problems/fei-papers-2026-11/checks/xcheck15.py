"""Cross-check: full-state L_mod (lattice_np) at k=15 for small N against the per-h0 pieces."""
import re, sys
sys.path.insert(0, r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad")
from lattice_np import PRIMES, crt, L_mod

k = 15
txt = open(sys.argv[1], encoding="utf-8").read()
pieces = {}
for kk, N, h, a, b, c in re.findall(r"k=(\d+) N=(\d+) h0=(\d+) res=\[(\d+), (\d+), (\d+)\]", txt):
    pieces[(int(N), int(h))] = [int(a), int(b), int(c)]
for N in [int(t) for t in sys.argv[2].split(",")]:
    tot = [0, 0, 0]
    for h in range(N // 2 + 1):
        w = 1 if 2 * h == N else 2
        tot = [(t + w * r) % p for t, r, p in zip(tot, pieces[(N, h)], PRIMES)]
    a, b = crt(tot), crt(L_mod(k, N))
    print(f"N={N}: pieces {a}  full {b}  {'AGREE' if a == b else 'DIFFER'}", flush=True)
