"""Regression: the general-kappa port at kappa=0 vs the original huanggrid."""
import sys
sys.path.insert(0, '.')
import core
import huanggrid as G0
import huang_cert_grid as GK
from flint import arb

GK.configure(arb(0), core.ALPHA, core.Q, core.PSI)
pts = [(arb('1.1'), arb('0.5'), arb('0.66')),
       (arb('0.3'), arb('0.2'), arb('0.9')),
       (arb('-0.8'), arb('-0.4'), arb('0.5'))]
for a1, a2, s in pts:
    t0 = G0.T_of(a1, a2, s)
    tk = GK.T_of(a1, a2, s)
    print(f'a=({float(a1):+.2f},{float(a2):+.2f}) s={float(s):.2f}')
    print('  orig:', t0)
    print('  port:', tk)
v0, _ = G0.S_moment(arb('1.1'), arb('0.5'), arb('0.66'))
vk, _ = GK.S_moment(arb('1.1'), arb('0.5'), arb('0.66'))
print('S_moment orig:', v0)
print('S_moment port:', vk)
