"""T250 (agent A, 18 Oct): the first ReLU layer at an OBTUSE input angle theta0 in (pi/2, pi], the case the 12:2x review
found outside lemma (ii). x, y ~ N(0, 1) per coordinate with correlation cos theta0, r1 = relu(x), r2 = relu(y), theta1 = angle(r1, r2).
Prints n * bias and n * var of log theta1 - log F(theta0), F(t) = arccos((sin t + (pi - t) cos t) / pi), and the smallest theta1 seen,
plus the lower-tail ratio sin(theta1) / (|r1_S| / |r1|) on S = {x > 0, y <= 0} (should never go below 1). argv: n_list reps"""
import sys, numpy as np
ns = [int(a) for a in sys.argv[1].split(',')]; reps = int(sys.argv[2]); rng = np.random.default_rng(250)
F = lambda t: np.arccos((np.sin(t) + (np.pi - t) * np.cos(t)) / np.pi)
for t0 in (np.pi / 2, 1.9, 2.3, 2.7, 3.0, np.pi - 1e-3, np.pi):
    for n in ns:
        e = []; tmin = np.inf; rmin = np.inf; ch = max(1, 2_000_000 // n)
        for k in range(0, reps, ch):
            c = min(ch, reps - k)
            x = rng.standard_normal((c, n)); w = rng.standard_normal((c, n)); y = np.cos(t0) * x + np.sin(t0) * w
            r1, r2 = np.maximum(x, 0), np.maximum(y, 0)
            n1, n2 = np.linalg.norm(r1, axis=1), np.linalg.norm(r2, axis=1)
            cs = np.clip(np.einsum('ij,ij->i', r1, r2) / (n1 * n2), -1, 1); th = np.arccos(cs)
            e.append(np.log(th) - np.log(F(t0))); tmin = min(tmin, th.min())
            S = (x > 0) & (y <= 0); lb = np.linalg.norm(np.where(S, x, 0), axis=1) / n1
            rmin = min(rmin, (np.sin(th) / np.maximum(lb, 1e-300)).min())
        e = np.concatenate(e)
        print(f'theta0 {t0:.4f} F {F(t0):.4f} n {n:5d}: n*bias {n * e.mean():+.3f}+-{n * e.std() / np.sqrt(reps):.3f}  '
              f'n*var {n * e.var():.3f}  min theta1 {tmin:.4f}  min sin/lower {rmin:.4f}', flush=True)
