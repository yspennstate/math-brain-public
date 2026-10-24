"""Exact witness with H > 4 I.  g = balanced 4-bit function with H(g)=3, I(g)=3/2 (H/(I-1)=6).
For balanced g, (f o g)^ spectrum: T ~ fhat^2, then independent S_i ~ ghat^2 for i in T, so
H(f o g) = H(f) + I(f) H(g),  I(f o g) = I(f) I(g)   (exact; checked here by FWHT for g o g).
Then G = g o g o g (64 variables): H = 3(1 + 3/2 + 9/4) = 57/4, I = 27/8, H/I = 38/9 > 4."""
import numpy as np
from fractions import Fraction
from fei_lib import fwht_int, entropy_from_W, influence_from_W, H_interval
ones = [6, 7, 9, 11, 12, 13, 14, 15]
g = np.ones(16, dtype=np.int64); g[ones] = -1
W = fwht_int(g)
print('ghat*16:', W.tolist())
print('H(g)=', entropy_from_W(W, 4), ' interval', H_interval(W, 4), ' I(g)=', influence_from_W(W, 4), ' mean=', g.mean())
# g o g on 16 variables: outer g applied to four inner copies on disjoint blocks of 4
n = 16
idx = np.arange(1 << n)
inner = []
for blk in range(4):
    sub = (idx >> (4 * blk)) & 15
    inner.append(g[sub])          # +-1
# outer input bit j = 1 iff inner_j = -1
oidx = np.zeros(1 << n, dtype=np.int64)
for blk in range(4):
    oidx |= ((inner[blk] == -1).astype(np.int64) << blk)
gg = g[oidx]
W2 = fwht_int(gg)
H2 = entropy_from_W(W2, n); I2 = influence_from_W(W2, n)
print('g o g: H=', H2, ' I=', I2, ' predicted H=', 3 + 1.5 * 3, ' I=', Fraction(9, 4))
print('H interval(g o g):', H_interval(W2, n))
H3 = Fraction(3) * (1 + Fraction(3, 2) + Fraction(9, 4)); I3 = Fraction(27, 8)
print('G = g o g o g: H=', H3, ' I=', I3, ' H/I=', H3 / I3, ' 4I=', 4 * I3)
