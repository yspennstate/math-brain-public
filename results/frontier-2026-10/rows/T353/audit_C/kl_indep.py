# agent C, 19 Oct: independent check of cert_kl_arb.py - densities rebuilt from the construction in
# REFUTATION_T2.md (x: B -> N(-2)xN(0), notB -> N(0)xN(a2-v2); x': B -> N(-1)xN(0), notB -> N(0)xN(-v2);
# ANTI a2-v2=2, -v2=1; SAME 0, -1), NO shift of g1 or g2, mpmath quad, sigma 1.
from mpmath import mp, quad, npdf, log, inf
mp.dps = 30
def joint(g1, same):
    a, c = (0, -1) if same else (2, 1)
    P = lambda z: npdf(g1, -2) / 2 * npdf(z, 0) + npdf(g1, 0) / 2 * npdf(z, a)
    Q = lambda z: npdf(g1, -1) / 2 * npdf(z, 0) + npdf(g1, 0) / 2 * npdf(z, c)
    return P, Q
def K(g1, same, qp):
    P, Q = joint(g1, same)
    if qp: P, Q = Q, P
    return quad(lambda z: P(z) * log(P(z) / Q(z)), [-inf, -3, 0, 3, inf])
for qp in (False, True):
    # the script's g1 is the construction's g1 + 1, so its [-1.51, -1.49] is [-2.51, -2.49] here
    d = lambda g: K(g, True, qp) - K(g, False, qp)
    print("QP" if qp else "PQ", "diff at script g1 -1.5:", mp.nstr(d(-2.5), 8), " at -1.51:", mp.nstr(d(-2.51), 8), " at -1.49:", mp.nstr(d(-2.49), 8))
    print("   gain over the interval:", mp.nstr(quad(d, [-2.51, -2.49]), 8))
    print("   whole-line KL adaptive(switch on [-2.51,-2.49]) - pair: same number by additivity")
