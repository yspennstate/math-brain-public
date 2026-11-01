"""
Discrete test of Conjecture 8.3 (Schertzer-Sun-Swart 2015): potential most recent
common ancestors (PMRCAs) in the Brownian net.

Model: branching-coalescing random walks on Z^2_even.  Each site (x,s) carries a right
arrow to (x+1,s+1) w.p. (1-eps)/2, a left arrow to (x-1,s+1) w.p. (1-eps)/2, or both
w.p. eps.  All even sites at time 0 are occupied.  Diffusive scaling: space eps, time eps^2.

A PMRCA is a site z=(x,s+1) reached by two paths pi, pi' started at time 0 with
pi(u) < pi'(u) for all 0 < u < s+1 and pi(s+1) = pi'(s+1) = x.  Equivalently
(x-1,x+1) is an "ordered-reachable pair" at time s, (x-1,s) has a right arrow and
(x+1,s) has a left arrow.

DP: A_s[p,q] (p<q) = there exist paths from time 0 to (p,s) and (q,s) that are strictly
ordered on times 1..s.  A_{s+1}[p,q] = OR over predecessors p' of p and q' of q with p'<q'
of A_s[p',q'].  Cost O(L^2) per step, boolean numpy.

Counted in the continuum box x in [-XB, XB], t in [T0, T1]:
  pmrca      : PMRCAs (the conjecture says this stays finite as eps -> 0)
  meet_all   : all meeting points with both incoming sides occupied by time-0 paths
               (a countable dense set in the limit: should grow like 1/eps)
Control: eps = 0 is the coalescing walk / Brownian web, where the expected count in the
box is 2*XB*(1/sqrt(pi*T0) - 1/sqrt(pi*T1)).
"""
import numpy as np, sys, time, json, math
try:
    pass
except Exception:
    pass

def run(eps, XB=2.0, T0=0.25, T1=2.0, HALF=10.0, seed=0, eps_space=None):
    # eps_space: lattice spacing in continuum units (defaults to eps); for eps=0 control pass it.
    h = eps if eps_space is None else eps_space
    L = int(2*HALF/h)
    L += L % 2
    T = int(T1/h**2)
    s0 = int(T0/h**2)
    x_lo = int((HALF - XB)/h); x_hi = int((HALF + XB)/h)
    rng = np.random.default_rng(seed)
    # time 0: even sites occupied
    occ = np.zeros(L, dtype=bool); occ[0::2] = True
    A = None
    pmrca = 0; meet_all = 0
    t_start = time.time()
    for s in range(0, T):
        u = rng.random(L)
        R = u < (1 - eps)/2 + eps           # right arrow present
        Lf = u >= (1 - eps)/2               # left arrow present  (both when u in [(1-eps)/2, (1+eps)/2))
        # occupancy at s+1
        occ_new = np.zeros(L, dtype=bool)
        occ_new[1:] |= occ[:-1] & R[:-1]
        occ_new[:-1] |= occ[1:] & Lf[1:]
        if s >= 1:
            # meeting-site candidates at time s+1 at x = p'+1 with p' in [x_lo-1, x_hi-1]
            p = np.arange(x_lo - 1, x_hi)      # p' range
            diag = A[p, p + 2] & R[p] & Lf[p + 2]
            alld = occ[p] & occ[p + 2] & R[p] & Lf[p + 2]
            if s + 1 >= s0:
                pmrca += int(diag.sum()); meet_all += int(alld.sum())
            # propagate A
            B = np.zeros_like(A)
            # p' -> p'+1 (R), q' -> q'+1 (R)
            m = A & R[:, None] & R[None, :]
            B[1:, 1:] |= m[:-1, :-1]
            # p' -> p'+1 (R), q' -> q'-1 (Lf)
            m = A & R[:, None] & Lf[None, :]
            B[1:, :-1] |= m[:-1, 1:]
            # p' -> p'-1 (Lf), q' -> q'+1 (R)
            m = A & Lf[:, None] & R[None, :]
            B[:-1, 1:] |= m[1:, :-1]
            # p' -> p'-1 (Lf), q' -> q'-1 (Lf)
            m = A & Lf[:, None] & Lf[None, :]
            B[:-1, :-1] |= m[1:, 1:]
            # kill p >= q (only the diagonal can be produced, from q'=p'+2)
            np.fill_diagonal(B, False)
            A = B
        else:
            # s == 0: build A_1 from occ_new: all strictly ordered pairs of occupied sites
            A = occ_new[:, None] & occ_new[None, :]
            A = np.triu(A, 1)
        occ = occ_new
    return dict(eps=eps, h=h, L=L, T=T, HALF=HALF, T1=T1, seed=seed, pmrca=pmrca, meet_all=meet_all,
                secs=round(time.time() - t_start, 1))

if __name__ == "__main__":
    eps = float(sys.argv[1]); nseeds = int(sys.argv[2]); seed0 = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    hs = float(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] != 'None' else None
    half = float(sys.argv[5]) if len(sys.argv) > 5 else 10.0
    t1 = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0
    out = []
    for k in range(nseeds):
        r = run(eps, seed=seed0 + k, eps_space=hs, HALF=half, T1=t1)
        print(json.dumps(r), flush=True)
        out.append(r)
    with open(f"pmrca_eps{eps}_h{hs}_s{seed0}_half{half}_t1{t1}.jsonl", "a", encoding="utf-8") as f:
        for r in out: f.write(json.dumps(r) + "\n")
