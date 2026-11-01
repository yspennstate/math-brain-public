"""Search small integer frames (w, v, q) in Z^m, mutually orthogonal, for a shear: on the lattice image
(a, b, c) = (<w,K>, <v,K>, <q,K>), K in Z^m, the residue of c modulo g is a fixed linear function of (a, b) for a
large modulus g relative to the trivial one. Measured as the index: the number of distinct values of c mod G over
lattice points with a = b = 0, compared with G, for G = gcd-scale."""
import itertools, math
import numpy as np

def image_lattice_info(w, v, q, box=3):
    # enumerate K in a box; collect (a,b,c)
    m = len(w)
    rng = range(-box, box + 1)
    pts = set()
    for K in itertools.product(rng, repeat=m):
        a = sum(wi * ki for wi, ki in zip(w, K)); b = sum(vi * ki for vi, ki in zip(v, K)); c = sum(qi * ki for qi, ki in zip(q, K))
        pts.add((a, b, c))
    return pts

best = []
m = 5
vals = range(-2, 3)
W = (1, 1, 1, 1, 1)
cands = [x for x in itertools.product(vals, repeat=m) if sum(xi * wi for xi, wi in zip(x, W)) == 0 and any(x)]
for v in cands:
    for q in cands:
        if sum(a * b for a, b in zip(v, q)) != 0:
            continue
        if q <= v:
            continue
        # fibre over (a, b) = (0, 0): values of c; the step of c there vs the step of c overall
        pts = image_lattice_info(W, v, q, box=2)
        c_all = sorted({c for (a, b, c) in pts})
        c_00 = sorted({c for (a, b, c) in pts if a == 0 and b == 0})
        if len(c_00) < 2:
            continue
        step_all = min(np.diff(c_all)) if len(c_all) > 1 else 0
        step_00 = min(np.diff(c_00))
        ratio = step_00 // max(step_all, 1)
        best.append((ratio, v, q, step_all, step_00))
best.sort(reverse=True)
for r in best[:8]:
    print(r)
