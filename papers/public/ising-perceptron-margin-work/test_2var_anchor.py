"""Anchor test at kappa = 0.05: S*(1,0) = 0 in ball arithmetic.
Locate (q0, psi0) at the deep alpha interval, configure the grid module,
and evaluate S_moment(a*, s0) with the exact dual (1,0):
  a* = (psi0(1-q0), q0),  s0 = sqrt(1-q0),  H(a*) = Phi(1,0) - a1*.
Expect a small ball containing 0 (Huang's lem:value-at-1-0 at kappa != 0)."""
import sys
sys.path.insert(0, '.')
import certify_km_slab as C
import huang_cert_grid as GK
from flint import arb

alpha = C.iv(C.dec('0.781073068'), C.dec('0.781074776'))
kappa = C.iv(C.dec('0.05'), C.dec('0.05'))
q_seed = C.iv(C.dec('0.565'), C.dec('0.578'))
loc = C.locate_fp_bisect(C.dec('0.781073068'), kappa, q_seed)
qb, pb = loc
# widen q/psi to cover the whole alpha interval: locate at the other end too
loc2 = C.locate_fp_bisect(C.dec('0.781074776'), kappa, q_seed)
qb2, pb2 = loc2
q_all = C.hull(qb, qb2)
p_all = C.hull(pb, pb2)
lo_q, hi_q = C.endpoints(q_all)
lo_p, hi_p = C.endpoints(p_all)
print('located q:', q_all, ' psi:', p_all)

GK.configure(arb(C.dec('0.05')), alpha, q_all, p_all)
a1s = GK.PSI * (1 - GK.Q)
a2s = GK.Q
s0 = GK.S1Q
Phi10 = GK.Phi_of(arb(1), arb(0))
duals = [(arb(1), arb(0), Phi10)]
val, T = GK.S_moment(a1s, a2s, s0, duals=duals)
print('T(a*, s0) =', T)
print('S*(1,0) ball =', val)
