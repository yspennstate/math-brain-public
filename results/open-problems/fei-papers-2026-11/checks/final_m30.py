"""Assemble m_30 from the per-h0 pieces (lattice_np3 on Mac mini 1), N = 0..7.
Usage: python final_m30.py pieces_file [pieces_file ...]"""
import re, sys
from fractions import Fraction as F
from math import factorial
sys.path.insert(0, r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad")
from lattice_np import PRIMES, crt, hstar_from

k = 15
pieces = {}
for fn in sys.argv[1:]:
    txt = open(fn, encoding="utf-8").read()
    for kk, N, h, a, b, c in re.findall(r"k=(\d+) N=(\d+) h0=(\d+) res=\[(\d+), (\d+), (\d+)\]", txt):
        if int(kk) == k:
            pieces[(int(N), int(h))] = [int(a), int(b), int(c)]
half = k // 2 + 1
L = []
for N in range(half):
    tot = [0, 0, 0]
    for h in range(N // 2 + 1):
        w = 1 if 2 * h == N else 2
        tot = [(t + w * r) % p for t, r, p in zip(tot, pieces[(N, h)], PRIMES)]
    L.append(crt(tot))
    print(f"  k={k} N={N}: L={L[-1]}")
hs = hstar_from(L, k + 1)
full = hs + [hs[k - i] for i in range(half, k + 1)]
assert all(x > 0 for x in full), "h* not positive"
m = F(sum(full), factorial(k + 1))
print(f"k={k}: L(0..{half-1}) = {L}  h* = {full}  m_{2*k} = {m} = {float(m):.10e}")
print("threshold 1.0424452950e+14:", "PASSES" if m >= F(10424452950, 100) * 10**6 else "FAILS",
      f"margin {float(m) - 1.0424452950e14:.6e}")
