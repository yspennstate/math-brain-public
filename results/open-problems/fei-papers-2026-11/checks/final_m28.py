"""Assemble m_28 from L(0..4) (lattice_np2 run, laptop) and the per-h0 pieces for
N=5,6,7 (lattice_np3 on Mac mini 1).  Prints the same final line as lattice_np2."""
import re, sys
from fractions import Fraction as F
from math import factorial
sys.path.insert(0, r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad")
from lattice_np import PRIMES, crt, hstar_from

k = 14
L = [213458046676875, 481500985656640950, 117629064493315916625, 7141213008396180313740,
     184106565736170444079335]
txt = open(sys.argv[1], encoding="utf-8").read()
pieces = {}
for N, h, a, b, c in re.findall(r"N=(\d+) h0=(\d+) res=\[(\d+), (\d+), (\d+)\]", txt):
    pieces[(int(N), int(h))] = [int(a), int(b), int(c)]
for N in (5, 6, 7):
    tot = [0, 0, 0]
    for h in range(N // 2 + 1):
        w = 1 if 2 * h == N else 2
        tot = [(t + w * r) % p for t, r, p in zip(tot, pieces[(N, h)], PRIMES)]
    L.append(crt(tot))
    print(f"  k={k} N={N}: L={L[-1]}")
half = k // 2 + 1
hs = hstar_from(L, k + 1)
full = hs + [hs[k - i] for i in range(half, k + 1)]
m = F(sum(full), factorial(k + 1))
print(f"k={k}: L(0..{half-1}) = {L}  h* = {full}  m_{2*k} = {m} = {float(m):.10e}")
