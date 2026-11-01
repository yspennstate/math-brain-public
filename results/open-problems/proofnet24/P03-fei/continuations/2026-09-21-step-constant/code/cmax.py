"""Largest margin c this candidate supports, POINTWISE (a necessary condition, not a
certificate: the proof needs the interval machinery). Slack in (A) rises by c(1-p)(1-q),
so for each sampled (p,q) the candidate needs c >= -Phi_0(p,q)/((1-p)(1-q)) + c_0 ..."""
import numpy as np
from ladder import Phi

def worst(c, P, Q):
    v = Phi(P, Q, c)
    j = int(np.argmin(v))
    return v[j], P[j], Q[j]

def build_grid():
    """dyadic p, Hod ladder q, plus dense random - the places the report says are tight"""
    q = [0.5]
    for _ in range(14): q.append(1/(1+q[-1]))
    qs = np.array(sorted(set([round(t,12) for t in q] + [0.618034])))
    xs = np.concatenate([np.arange(1, 40.001, 1.0),          # every dyadic node
                         np.linspace(1, 12, 2201)])          # dense in the active band
    P = 2.0**(-xs)
    PP, QQ = np.meshgrid(P, qs, indexing='ij')
    PP = PP.ravel(); QQ = QQ.ravel()
    rng = np.random.default_rng(7)
    Pr = rng.uniform(1e-6, 0.5, 300000); Qr = rng.uniform(1e-6, 0.999999, 300000)
    # also both-large and both-small corners
    Pd = np.concatenate([PP, Pr]); Qd = np.concatenate([QQ, Qr])
    return Pd, Qd

if __name__ == '__main__':
    P, Q = build_grid()
    print("sampled points: %d  (dyadic x Hod ladder, plus 300k random)" % len(P))
    print("\n   c        worst Phi        at (p, q)                     constant C0+c/4")
    for c in (0.0030, 0.0035, 0.0040, 0.0041, 0.0042, 0.0045, 0.0050, 0.0060, 0.0100):
        w, pw, qw = worst(c, P, Q)
        print("  %.4f   %11.3e    p=%-12.6g q=%-10.6g   %.6f   %s"
              % (c, w, pw, qw, 6.4548 + c/4, "ok" if w >= 0 else "FAILS"))
    # bisect the largest c that is pointwise non-negative
    lo, hi = 0.0005, 0.02
    for _ in range(40):
        mid = (lo+hi)/2
        w, _, _ = worst(mid, P, Q)
        if w >= 0: hi = mid
        else: lo = mid
    print("\nsmallest pointwise-feasible c on this sample: %.6f  ->  constant %.6f" % (hi, 6.4548+hi/4))
    print("(currently proved: 6.4573 at c = 0.01; the failed attempt was c = 0.003 -> 6.455550)")
