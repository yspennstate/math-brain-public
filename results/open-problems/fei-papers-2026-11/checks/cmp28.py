"""Read m_28 from lnp14.out and compare it with the order-28 threshold.

The threshold is recomputed exactly from the even Hankel block of the
free cumulants (indices 2..14), as in verify/order28_threshold.py.
Also checks the h* palindrome the run printed: h*_0 = 27!! and
sum h* = 15! m_28.
"""
import re
import sys
from fractions import Fraction as Fr
from math import factorial

S = r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/"
sys.path.insert(0, S + "zen8/toeplitz-hankel-section-profiles/verify")
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from order24_threshold import free_cumulants, solve, mT as mT22

mT = dict(mT22)
mT[24] = Fr(1112571762134554, 75075)
mT[26] = Fr(2032842751996209, 7700)
r0 = free_cumulants(mT, 28, m_top_zero=True)
C = r0[28]
core = [2, 4, 6, 8, 10, 12]
A = [[r0[i + j] for j in core] for i in core]
v = [r0[i + 14] for i in core]
x = solve([row[:] for row in A], v[:])
TH = sum(a * b for a, b in zip(v, x)) - C
print("threshold =", float(TH))

txt = open(S + "lnp14.out", encoding="utf-8").read()
m = re.search(r"m_28 = (\d+)/(\d+)", txt) or re.search(r"m_28 = (\d+) ", txt)
if not m:
    print("m_28 not printed yet")
    raise SystemExit(1)
m28 = Fr(int(m.group(1)), int(m.group(2))) if m.lastindex == 2 else Fr(int(m.group(1)))
h = re.search(r"h\* = \[([0-9, ]+)\]", txt)
if h:
    hs = [int(t) for t in h.group(1).split(",")]
    df = 1
    for j in range(1, 28, 2):
        df *= j
    print("h* length 15:", len(hs) == 15, " palindrome:", hs == hs[::-1],
          " h*_0 = 27!!:", hs[0] == df, " all positive:", all(t > 0 for t in hs),
          " sum = 15! m28:", Fr(sum(hs), factorial(15)) == m28)
print("m28 =", m28, "=", float(m28))
print("m28 - threshold =", float(m28 - TH), " relative", float((m28 - TH) / TH))
print("m28/m26 =", float(m28 / mT[26]), " diff of ratios =", float(m28 / mT[26] - mT[26] / mT[24]))
print("VERDICT:", "PASSES" if m28 >= TH else "FAILS")
