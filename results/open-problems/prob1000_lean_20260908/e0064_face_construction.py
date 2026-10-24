"""E0064: (a) m = 6 construction - faces {1,2,3} and {4,5,6} both invariant; each face's restriction is a strictly
non-Volterra 3-type operator (unique fixed point on that face by the source's Theorem 6), so V has >= 2 fixed points.
Verified numerically here.  (b) m = 5 with face {1,2,3} invariant: search for a second fixed point with x4, x5 > 0.
(c) m = 4 stress test: sparse operators (Dirichlet concentration 0.1) and face-invariant ones.
"""
import numpy as np
from e0064_fixed_point_search import V, fixed_points

def snv_with_invariant_faces(rng, m, faces, conc=1.0):
    P = np.zeros((m, m, m))
    face_of = {}
    for F in faces:
        for i in F: face_of[i] = F
    for i in range(m):
        for j in range(i, m):
            allowed = [k for k in range(m) if k not in (i, j)]
            F = face_of.get(i); G = face_of.get(j)
            if F is not None and F == G:                 # both in the same invariant face: land inside it
                allowed = [k for k in F if k not in (i, j)]
            w = rng.dirichlet(np.ones(len(allowed)) * conc)
            for k, wk in zip(allowed, w):
                P[i, j, k] = wk; P[j, i, k] = wk
    return P

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    rng = np.random.default_rng(11)
    print("== (a) m=6, two disjoint invariant faces")
    hist = {}
    ex = None
    for t in range(30):
        P = snv_with_invariant_faces(rng, 6, [(0, 1, 2), (3, 4, 5)])
        sols = fixed_points(P, rng, starts=150)
        hist[len(sols)] = hist.get(len(sols), 0) + 1
        if ex is None and len(sols) >= 2: ex = (P, sols)
    print("   histogram of fixed-point counts:", dict(sorted(hist.items())))
    if ex:
        P, sols = ex
        for x in sols: print("   x =", np.round(x, 5), " residual", f"{np.max(abs(V(P, x) - x)):.1e}")
        np.save("e0064_m6_two_fixed_points.npy", P)
    print("== (b) m=5, face {1,2,3} invariant, other entries random")
    hist = {}; ex = None
    for t in range(200):
        P = snv_with_invariant_faces(rng, 5, [(0, 1, 2)], conc=rng.choice([0.2, 1.0, 3.0]))
        sols = fixed_points(P, rng, starts=150)
        hist[len(sols)] = hist.get(len(sols), 0) + 1
        if len(sols) >= 2 and (ex is None or len(sols) > len(ex[1])): ex = (P, sols)
    print("   histogram:", dict(sorted(hist.items())))
    if ex:
        P, sols = ex
        for x in sols: print("   x =", np.round(x, 5), " residual", f"{np.max(abs(V(P, x) - x)):.1e}")
        np.save("e0064_m5_two_fixed_points.npy", P)
    print("== (c) m=4 stress: sparse (conc 0.1) and face-invariant")
    hist = {}; ex = None
    for t in range(300):
        if t % 2 == 0:
            P = snv_with_invariant_faces(rng, 4, [], conc=0.1)
        else:
            P = snv_with_invariant_faces(rng, 4, [(0, 1, 2)], conc=rng.choice([0.2, 1.0]))
        sols = fixed_points(P, rng, starts=150)
        hist[len(sols)] = hist.get(len(sols), 0) + 1
        if len(sols) >= 2 and ex is None: ex = (P, sols)
    print("   histogram:", dict(sorted(hist.items())))
    if ex:
        P, sols = ex
        for x in sols: print("   x =", np.round(x, 5), " residual", f"{np.max(abs(V(P, x) - x)):.1e}")
        np.save("e0064_m4_two_fixed_points.npy", P)
