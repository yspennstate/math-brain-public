# T353 sub-1 Renyi orders, audit 2 (agent C, 20 Oct 2026). Own code, own model derivation, own tail bound.
# Model read from REFUTATION_T2.md "The construction", in its own (shifted) g1 coordinate; s = sigma:
#   x : B -> N(g1; -2) N(g2; 0)        not B -> N(g1; 0) N(g2; a),  a = 2 (ANTI) or 0 (SAME)
#   x': B -> N(g1; -1) N(g2; 0)        not B -> N(g1; 0) N(g2; c),  c = 1 (ANTI) or -1 (SAME)
# each branch with probability 1/2. (cert_renyi_sub1_arb_sigma.py works in g1 + 1 and per-branch g2 shifts; a g2 shift common
# to p and q at fixed g1 changes nothing, so its interval [u, v] is [u - 1, v - 1] here.)
# J(g1) = int p^al q^(1-al) dg2. Certificate: J_ANTI - J_SAME > 0 on every ball of a cover.
# Integral: Arb's acb.integral (rigorous Gauss-Legendre with holomorphy check, pow with analytic=True) on g2 in [-L, L],
# with g1 entering as an arb ball, so the enclosure holds for every g1 in the ball.
# Tail (not the subadditivity/Mills bound of the note): weighted AM-GM p^al q^(1-al) <= al p + (1-al) q, and the g2-mass of
# p or q beyond |g2| > L is at most (total weight) * 2 * Phibar((L - 2)/s), every g2 centre having |centre| <= 2.
# Usage: python sub1_cert_C.py SIGMA ALPHA(e.g. 1/4) DIR(PQ|QP) LO HI NBALLS
import sys
from flint import arb, acb, ctx
ctx.prec = 96
s = arb(sys.argv[1]); al = arb(sys.argv[2]); QP = sys.argv[3] == "QP"
lo, hi, nb = arb(sys.argv[4]), arb(sys.argv[5]), int(sys.argv[6])
c0 = 1 / ((2 * arb.pi()).sqrt() * s)
def Nr(x, m): return c0 * (-(x - m) ** 2 / (2 * s * s)).exp()
def Nc(z, m): return acb(c0) * (-(z - m) ** 2 / (2 * s * s)).exp()
L = 12 * s + 4
def phibar(t): return (t / (s * arb(2).sqrt())).erfc() / 2
def J(g1, anti):
    wb_x, wn = Nr(g1, -2) / 2, Nr(g1, 0) / 2
    wb_y = Nr(g1, -1) / 2
    a, c = (2, 1) if anti else (0, -1)
    def f(z, analytic):
        p = wb_x * Nc(z, 0) + wn * Nc(z, a)
        q = wb_y * Nc(z, 0) + wn * Nc(z, c)
        if QP: p, q = q, p
        return p.pow(acb(al), analytic=analytic) * q.pow(acb(1 - al), analytic=analytic)
    core = acb.integral(f, -L, L).real
    tot = al * (wb_x + wn) + (1 - al) * (wb_y + wn)
    if QP: tot = (1 - al) * (wb_x + wn) + al * (wb_y + wn)
    return core, tot * 2 * phibar(L - 2)
w = (hi - lo) / nb
mins, gain, bad = None, arb(0), 0
for k in range(nb):
    g1 = (lo + w * k).union(lo + w * (k + 1))
    (ca, ta), (cs, ts) = J(g1, True), J(g1, False)
    # J_ANTI - J_SAME >= (ca - cs) - ts  (tails are nonnegative and bounded by ta, ts)
    lower = (ca - cs - ts).lower()
    if lower <= 0: bad += 1
    mins = lower if mins is None or lower < mins else mins
    gain += arb(lower) * w if lower > 0 else 0
print("sigma %s order %s %s [%s, %s] balls %d: min lower end %s, failed balls %d, int(J_ANTI - J_SAME) >= %s, tail <= %s" %
      (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], nb, mins.str(3, radius=False), bad,
       gain.lower().str(3, radius=False), ts.upper().str(3, radius=False)), flush=True)
