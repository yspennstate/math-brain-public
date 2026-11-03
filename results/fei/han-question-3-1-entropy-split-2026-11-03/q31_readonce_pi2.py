# T021: general read-once formulas. sup D_k/I_k over all read-once formulas = sup over sequences P_l in (0,1) of the
# general recursion (q31_readonce_general.stepP; exact against truth tables in q31_readonce_check.out). Here:
# 1. constant P = 1 - delta: D/I -> pi^2/2 as delta -> 0 (the continuum limit);
# 2. the continuum value as an integral and as a series: int_0^1 Phi(1, b^2)/b^2 db = (pi^2/2 - 2) + 2 = pi^2/2;
# 3. hybrids: a beam-found prefix (best 4.7702 at moderate P) followed by a near-1 tail, and constant P across (0, 1).
import mpmath as mp
from q31_tree_entropy import Phi
from q31_readonce_general import stepP
mp.mp.dps = 120
def run(Ps, tail_delta=None, Imin=mp.mpf("1e-12")):
    st = (mp.mpf(0), mp.mpf(1), mp.mpf(0)); best = mp.mpf(0)
    for P in Ps:
        st = stepP(st, mp.mpf(P)); best = max(best, st[2] / st[1])
    if tail_delta is not None:
        while st[1] > Imin:
            st = stepP(st, 1 - tail_delta); best = max(best, st[2] / st[1])
    return best, st[2] / st[1]
pi2 = mp.pi ** 2 / 2
print("1. constant P = 1 - delta, run until I < 1e-12 (sup over the run, final value):")
for d in ("0.3", "0.1", "0.03", "0.01", "0.003", "0.001"):
    b, f = run([], mp.mpf(d)); print("   delta=%-6s sup %s  final %s  (pi^2/2 - final = %s)" % (d, mp.nstr(b, 10), mp.nstr(f, 10), mp.nstr(pi2 - f, 4)))
print("   constant P elsewhere in (0,1):", [(p, mp.nstr(run([], 1 - mp.mpf(p))[0], 7)) for p in ("0.2", "0.4", "0.5", "0.6", "0.8")])
# 2. continuum: G(b) = (1+b)^2 ln(1+b) + (1-b)^2 ln(1-b) = 2 sum c_{2n} b^{2n}; Phi(1,b^2)/b^2 = -2 ln b + G(b)/b^2.
# int_0^1 G/b^2 = 2 sum c_{2n}/(2n-1) = 3 + 2 sum_{n>=2} [2/(2n-1)^2 - 1/(2n(2n-1)) - 1/((2n-2)(2n-1))]
#              = 3 + 4(pi^2/8 - 1) - 2(ln 2 - 1/2) - 2(1 - ln 2) = pi^2/2 - 2;   int_0^1 -2 ln b = 2.
c = lambda n: mp.mpf(2) / (2 * n - 1) - mp.mpf(1) / (2 * n) - mp.mpf(1) / (2 * n - 2)
ser = 3 + 2 * mp.nsum(lambda n: c(n) / (2 * n - 1), [2, mp.inf])
G = lambda b: (1 + b) ** 2 * mp.log(1 + b) + (1 - b) ** 2 * mp.log(1 - b)
with mp.workdps(60):
    a, e = mp.mpf("1e-6"), mp.mpf("1e-14")
    core = mp.quad(lambda b: G(b) / b ** 2, [a, mp.mpf("0.5"), 1 - e])
    head = 3 * a  # G/b^2 = 3 + O(b^2) near 0
    tail = 4 * mp.log(2) * e  # G/b^2 -> G(1) = 4 ln 2 at b = 1 (G(1) itself is 0 * log 0 in floating form)
    integral = core + head + tail + 2
print("2. series sum = %s, pi^2/2 - 2 = %s, diff %s;  quadrature of Phi(1,b^2)/b^2 on (0,1) = %s, pi^2/2 = %s" % (
    mp.nstr(ser, 25), mp.nstr(pi2 - 2, 25), mp.nstr(abs(ser - (pi2 - 2)), 3), mp.nstr(integral, 14), mp.nstr(pi2, 14)))
beamP = [0.8, 0.6, 0.45, 0.35, 0.525, 0.45, 0.35, 0.375, 0.5, 0.45, 0.5, 0.45, 0.5, 0.45, 0.5, 0.45, 0.5, 0.45, 0.5, 0.45,
         0.5, 0.45, 0.475, 0.475, 0.475, 0.475, 0.475, 0.475, 0.475, 0.5]
print("3. beam prefix alone: sup %s" % mp.nstr(run(beamP)[0], 10))
for cut in (0, 1, 2, 4, 8, 30):
    print("   beam prefix [:%2d] then P = 1 - 0.003 tail: sup %s" % (cut, mp.nstr(run(beamP[:cut], mp.mpf("0.003"))[0], 10)))
print("   near-1 then a moderate P, then near-1 again:", mp.nstr(run([mp.mpf(1) - mp.mpf("0.003")] * 3000 + [0.5] * 3, mp.mpf("0.003"))[0], 10))
