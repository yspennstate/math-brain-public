"""X008 two-address witness: check Theorem G, U/I, G/I.  Construction from sources/ONE_BIT_ENDPOINT.md sec.3."""
import numpy as np
from fractions import Fraction
from feilib import *
from upward import Uprime
from sweepG import evalf
g = [1,-1,-1,0,-1,0,0,1,-1,-1,-1,0,-1,0,0,1]
def h_edge(low):  # indicator of the edge with low-three-bit value `low`, bit3 free
    return [1 if (x & 7) == low else 0 for x in range(16)]
h1, h2, h3 = h_edge(3), h_edge(5), h_edge(6)
# variables order: y1 (bit0), y2 (bit1), x0..x3 (bits 2..5)
t = []
for idx in range(64):
    y1 = 1 - 2 * (idx & 1); y2 = 1 - 2 * ((idx >> 1) & 1); x = idx >> 2
    t.append(g[x] + y1 * h1[x] + y2 * h2[x] + y1 * y2 * h3[x])
t = np.array(t); assert set(t.tolist()) <= {-1, 1}
p = spectrum(t); n = 6; H = float(entropy(p)); I = float(total_influence(p, n)); U = float(Uprime(p, n)); Var = float(1 - p[0])
print('X008: H=', H, 'I=', I, 'exact I =', exact_total_influence(t), 'U=', round(U, 6), 'U/I=', round(U / I, 4),
      ' Theorem G RHS 2(I-Var)+2U =', round(2 * (I - Var) + 2 * U, 4))
r = evalf(t); print('G/I=', round(r['GI'], 4), 'minloc', round(r['minloc'], 4), 'maxloc', round(r['maxloc'], 4))
