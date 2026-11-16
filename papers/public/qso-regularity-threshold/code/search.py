"""Numerical searches of Section 6 of the paper.

cycles   For m = 3, 4 and a lower bound g on |X_1 - Y_1|, maximize the least coefficient of an operator V with
         V(X) = Y and V(Y) = X, and of one with V(X) = X and V(Y) = Y. For given points the inner problem is a linear program in the coefficients; the points
         are optimized by differential evolution and Nelder-Mead, then the coefficients and points are refined
         together by SLSQP. Writes data/search_cycles.json (Table 2 of the paper).
random   For m = 3, 4 and least coefficient L_m + 1e-4, (L_m + C_m)/2 and C_m + 1e-4, sample 240 operators for each
         of three Dirichlet concentrations (80 of them vertices of the coefficient polytope), iterate from the
         vertices and four random points, and record whether the trajectories reach a common limit.
         Writes data/search_random.json.

Run from the repository root: python code/search.py cycles   (about five minutes)
                              python code/search.py random   (about twenty seconds)
"""
import os

for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
import itertools
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import differential_evolution, linprog, minimize

OUT = Path(__file__).resolve().parent.parent / "data"
SEED = 130065
RNG = np.random.default_rng(SEED)


def bounds(m):
    """(L_m, C_m) of Theorems 1.2 and 1.3."""
    return (1 - 1 / math.sqrt(m + 1)) / (2 * m), 2 / (3 * m + 2 + math.sqrt(m * m + 12 * m + 4))


def pairs(m):
    return list(itertools.combinations_with_replacement(range(m), 2))


def weights(x):
    return np.array([x[i] * x[j] * (1 if i == j else 2) for i, j in pairs(len(x))])


def image(P, x):
    """V(x) by scalar sums, as a check on the vectorized code."""
    return np.array([math.fsum(float(P[r, k]) * float(x[i]) * float(x[j]) * (1 if i == j else 2)
                               for r, (i, j) in enumerate(pairs(len(x)))) for k in range(len(x))])


def lp_tensor(m, x, y, margin=0.0, fixed=False):
    """Largest least coefficient over all operators with V(x) = y and V(y) = x (fixed: V(x) = x and V(y) = y)."""
    pp = pairs(m)
    r = len(pp)
    n = r * m + 1
    eq, rhs = [], []
    for row in range(r):
        z = np.zeros(n)
        z[row * m:(row + 1) * m] = 1
        eq.append(z)
        rhs.append(1.0)
    for u, target in ([(x, x), (y, y)] if fixed else [(x, y), (y, x)]):
        w = weights(u)
        for k in range(m - 1):
            z = np.zeros(n)
            z[k:r * m:m] = w
            eq.append(z)
            rhs.append(target[k])
    ine = np.zeros((r * m, n))
    ine[:, :r * m] = -np.eye(r * m)
    ine[:, -1] = 1
    cost = np.zeros(n)
    cost[-1] = -1
    return linprog(cost, A_ub=ine, b_ub=np.zeros(r * m), A_eq=np.array(eq), b_eq=np.array(rhs),
                   bounds=[(margin, 1)] * (r * m) + [(margin, 1 / m)], method="highs",
                   options={"primal_feasibility_tolerance": 1e-9, "dual_feasibility_tolerance": 1e-9})


def state_pair(parameters, m, gap):
    """A pair of points of the simplex with x_1 - y_1 >= gap, from 2m - 2 numbers in [0, 1]."""
    x0 = gap + (1 - gap) * parameters[0]
    y0 = (x0 - gap) * parameters[1]
    states = []
    for first, pars in [(x0, parameters[2:m]), (y0, parameters[m:])]:
        tail, rem = [], 1 - first
        for u in pars:
            tail.append(rem * u)
            rem *= 1 - u
        states.append(np.array([first] + tail + [rem]))
    return states


def optimize(m, gap, fixed):
    def objective(v):
        x, y = state_pair(v, m, gap)
        sol = lp_tensor(m, x, y, fixed=fixed)
        return -sol.x[-1] if sol.success else 0.05

    res = differential_evolution(objective, [(0.0, 1.0)] * (2 * m - 2), seed=SEED + m + int(gap * 1000),
                                 popsize=9, maxiter=65, tol=2e-6, polish=False, workers=1, updating="immediate")
    local = minimize(objective, res.x, method="Nelder-Mead", bounds=[(0.0, 1.0)] * (2 * m - 2),
                     options={"maxiter": 900, "xatol": 1e-9, "fatol": 1e-10})
    v = local.x if local.fun < res.fun else res.x
    x, y = state_pair(v, m, gap)
    sol = lp_tensor(m, x, y, fixed=fixed)
    P, floor = sol.x[:-1].reshape(-1, m), float(sol.x[-1])
    a, b = (x, y) if fixed else (y, x)
    residual = max(np.max(abs(image(P, x) - a)), np.max(abs(image(P, y) - b)))
    assert sol.success and residual < 2e-8 and P.min() > floor - 2e-8
    return P, x, y, floor


def refine(m, gap, P0, x0, y0, floor0, fixed):
    r = len(pairs(m))
    n = r * m

    def unpack(z):
        return z[:n].reshape(r, m), z[n:n + m], z[n + m:n + 2 * m], z[-1]

    def equality(z):
        P, x, y, _ = unpack(z)
        a, b = (x, y) if fixed else (y, x)
        return np.r_[P.sum(axis=1) - 1, x.sum() - 1, y.sum() - 1,
                     weights(x) @ P[:, :m - 1] - a[:m - 1], weights(y) @ P[:, :m - 1] - b[:m - 1]]

    def inequality(z):
        P, x, y, ell = unpack(z)
        return np.r_[P.ravel() - ell, x[0] - y[0] - gap]

    sol = minimize(lambda z: -z[-1], np.r_[P0.ravel(), x0, y0, floor0], method="SLSQP",
                   bounds=[(0, 1)] * (n + 2 * m) + [(0, 1 / m)],
                   constraints=[{"type": "eq", "fun": equality}, {"type": "ineq", "fun": inequality}],
                   options={"maxiter": 1000, "ftol": 1e-12})
    P, x, y, ell = unpack(sol.x)
    a, b = (x, y) if fixed else (y, x)
    residual = float(max(np.max(abs(image(P, x) - a)), np.max(abs(image(P, y) - b))))
    assert max(abs(equality(sol.x))) < 1e-8 and residual < 1e-8 and min(inequality(sol.x)) > -1e-8
    return P, x, y, float(ell), residual


def cycles():
    report = []
    for fixed in [False, True]:
        for m in [3, 4]:
            L, C = bounds(m)
            for gap in [0.04, 0.008]:
                P, x, y, floor = optimize(m, gap, fixed)
                P2, x2, y2, floor2, residual = refine(m, gap, P, x, y, floor, fixed)
                rec = dict(kind="fixed points" if fixed else "two-cycle", m=m, gap=gap, L=L, C=C, lp_floor=floor, refined_floor=floor2, residual=residual,
                           above_L=bool(floor2 > L), X=x2.tolist(), Y=y2.tolist(), P=P2.tolist(),
                           lp_feasible_at_L_plus_1e4=bool(lp_tensor(m, x2, y2, L + 1e-4, fixed=fixed).success))
                print(json.dumps({k: v for k, v in rec.items() if k not in ("X", "Y", "P")}), flush=True)
                report.append(rec)
    return report


def step_all(x, P, m):
    w = np.stack([x[:, :, i] * x[:, :, j] * (1 if i == j else 2) for i, j in pairs(m)], axis=2)
    y = np.einsum("nsr,nrk->nsk", w, P)
    assert np.isfinite(y).all() and y.min() >= 0
    return y / y.sum(axis=2, keepdims=True)


def random_orbits():
    report = []
    for m in [3, 4]:
        L, C = bounds(m)
        for floor in [L + 1e-4, (L + C) / 2, C + 1e-4]:
            for concentration in [0.04, 0.4, 2.0]:
                n = 240
                q = RNG.dirichlet(np.full(m, concentration), size=(n, len(pairs(m))))
                q[:80] = np.eye(m)[RNG.integers(m, size=(80, len(pairs(m))))]
                P = floor + (1 - m * floor) * q
                starts = np.concatenate([np.eye(m), RNG.dirichlet(np.ones(m), 4)])
                x = np.broadcast_to(starts, (n, len(starts), m)).copy()
                for _ in range(1200):
                    x = step_all(x, P, m)
                step = np.max(abs(step_all(x, P, m) - x), axis=(1, 2))
                diameter = np.max(np.ptp(x, axis=1), axis=1)
                flagged = np.flatnonzero((step > 1e-7) | (diameter > 1e-7))
                for index in flagged:
                    # slow convergence near a flip bifurcation: continue the flagged operators much longer
                    state = x[index].copy()
                    for it in range(1, 200001):
                        w = np.stack([state[:, i] * state[:, j] * (1 if i == j else 2) for i, j in pairs(m)], axis=1)
                        nxt = w @ P[index]
                        nxt /= nxt.sum(axis=1, keepdims=True)
                        err = np.max(abs(nxt - state))
                        state = nxt
                        if it % 500 == 0 and err < 1e-11:
                            break
                    nxt = np.array([image(P[index], z) for z in state])
                    nxt /= nxt.sum(axis=1, keepdims=True)
                    step[index] = np.max(abs(nxt - state))
                    diameter[index] = np.max(np.ptp(state, axis=0))
                rec = dict(m=m, floor=floor, concentration=concentration, operators=n, starts=len(starts),
                           continued=int(len(flagged)), nonconverged=int(sum((step > 1e-7) | (diameter > 1e-7))),
                           max_step=float(step.max()), max_start_diameter=float(diameter.max()))
                print(json.dumps(rec), flush=True)
                report.append(rec)
    return report


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "cycles"
    start = time.time()
    result = {"cycles": cycles, "random": random_orbits}[which]()
    out = dict(results=result, seconds=round(time.time() - start, 1), seed=SEED,
               numpy=np.__version__, scipy=scipy.__version__)
    OUT.mkdir(exist_ok=True)
    (OUT / f"search_{which}.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
