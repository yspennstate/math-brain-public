"""Independent exact, LP and SDP checks for PAPER.tex.

Run: python3 -B referee_checks.py > referee_checks.out
Only small matrices; single-threaded solvers, one process, 240 s deadline.
Does not import, execute or copy any author checking code.
"""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
import signal
signal.alarm(240)
import time
import resource
import warnings
from itertools import combinations
import numpy as np
import sympy as sp
import scipy
from scipy import sparse
from scipy.optimize import linprog, minimize, OptimizeWarning
import clarabel

START = time.monotonic()
warnings.filterwarnings("ignore", category=OptimizeWarning,
                        message="Unrecognized options detected.*")
print("versions:", "numpy", np.__version__, "sympy", sp.__version__,
      "scipy", scipy.__version__, "clarabel", clarabel.__version__)


def walk(n, edges):
    weights = sp.zeros(n)
    for i, j, w in edges:
        weights[i, j] = weights[j, i] = sp.Rational(w)
    deg = list(weights * sp.ones(n, 1))
    pi = sp.Matrix([v / sum(deg) for v in deg])
    p = sp.diag(*[1 / v for v in deg]) * weights
    return p, pi


def lp(*args, **kwargs):
    ans = linprog(*args, **kwargs, method="highs", options={"threads": 1})
    assert ans.success, ans.message
    return ans


def svec(a):
    return np.array([a[i, j] * (1 if i == j else np.sqrt(2))
                     for j in range(len(a)) for i in range(j + 1)])


def unsvec(v, n):
    a = np.zeros((n, n))
    k = 0
    for j in range(n):
        for i in range(j + 1):
            a[i, j] = a[j, i] = v[k] / (1 if i == j else np.sqrt(2))
            k += 1
    return a


def programs(n, edges):
    pexact, piexact = walk(n, edges)
    p = np.array(pexact, dtype=float)
    pi = np.array(piexact, dtype=float).ravel()
    ce = np.array([pi[i] * p[i, j] for i, j, _ in edges])
    m = len(edges)
    pairs = list(combinations(range(n), 2))
    demands = [(a, b) for a in range(n) for b in range(n) if a != b]
    # Directed arc flows, independently for every ordered commodity.
    arcs = [(i, j) for i, j, _ in edges] + [(j, i) for i, j, _ in edges]
    nv = len(demands) * len(arcs) + 1
    ae = np.zeros((len(demands) * (n - 1), nv))
    be = np.zeros(len(ae))
    au = np.zeros((m, nv))
    for k, (a, b) in enumerate(demands):
        for v in range(n - 1):
            row = k * (n - 1) + v
            be[row] = pi[a] * pi[b] * ((v == a) - (v == b))
            for h, (i, j) in enumerate(arcs):
                ae[row, k * 2 * m + h] = (v == i) - (v == j)
        for h in range(m):
            au[h, k * 2 * m + h] = 1
            au[h, k * 2 * m + m + h] = 1
    au[:, -1] = -ce
    objective = np.zeros(nv)
    objective[-1] = 1
    flow = lp(objective, A_ub=au, b_ub=np.zeros(m), A_eq=ae, b_eq=be,
              bounds=(0, None))
    assert np.all(np.isfinite(flow.x))
    # Explicit contraction avoids spurious floating-point status warnings from
    # this machine's BLAS-backed matmul; also audit every residual as finite.
    conservation = np.einsum("ij,j->i", ae, flow.x, optimize=False) - be
    capacities = np.einsum("ij,j->i", au, flow.x, optimize=False)
    assert np.all(np.isfinite(conservation)) and np.all(np.isfinite(capacities))
    flow_res = max(np.max(np.abs(conservation)),
                   np.max(capacities), max(0, -np.min(flow.x)))
    # Independent all-pairs semimetric LP, including all triangle inequalities.
    index = {pair: k for k, pair in enumerate(pairs)}
    triangles = []
    for triple in combinations(range(n), 3):
        for a, b in combinations(triple, 2):
            c = next(v for v in triple if v not in (a, b))
            row = np.zeros(len(pairs))
            row[index[a, b]] = 1
            row[index[tuple(sorted((a, c)))]] = -1
            row[index[tuple(sorted((b, c)))]] = -1
            triangles.append(row)
    cc = np.array([pi[i] * p[i, j] for i, j in pairs])
    nn = np.array([2 * pi[i] * pi[j] for i, j in pairs])
    metric = lp(-nn, A_ub=np.array(triangles), b_ub=np.zeros(len(triangles)),
                A_eq=cc.reshape(1, -1), b_eq=[1], bounds=(0, None))
    metric_res = max(abs(cc @ metric.x - 1), max(0, np.max(np.array(triangles) @ metric.x)),
                     max(0, -np.min(metric.x)))
    # Squared Euclidean distances: anchored Gram G >= 0, x_(n-1) = 0.
    # C=tr(L_0 G), N=2 tr((diag(pi_0)-pi_0 pi_0^T) G).
    lap = np.diag(pi) - np.diag(pi) @ p
    lap = (lap + lap.T) / 2
    l0 = lap[:-1, :-1]
    mass = np.diag(pi[:-1]) - np.outer(pi[:-1], pi[:-1])
    dim = n * (n - 1) // 2
    aa = sparse.vstack([sparse.csc_matrix(svec(l0).reshape(1, -1)),
                        -sparse.eye(dim, format="csc")], format="csc")
    bb = np.r_[1.0, np.zeros(dim)]
    settings = clarabel.DefaultSettings()
    settings.verbose = False
    settings.max_threads = 1
    settings.max_iter = 150
    settings.time_limit = 30
    settings.tol_gap_abs = settings.tol_gap_rel = settings.tol_feas = 1e-10
    solver = clarabel.DefaultSolver(sparse.csc_matrix((dim, dim)), -2 * svec(mass),
                                   aa, bb, [clarabel.ZeroConeT(1),
                                            clarabel.PSDTriangleConeT(n - 1)], settings)
    sol = solver.solve()
    assert str(sol.status) in ("Solved", "AlmostSolved"), sol.status
    g = unsvec(sol.x, n - 1)
    full = np.zeros((n, n))
    full[:-1, :-1] = g
    distances = np.diag(full)[:, None] + np.diag(full)[None, :] - 2 * full
    numerator = pi @ distances @ pi
    denominator = sum(c * distances[i, j] for c, (i, j, _) in zip(ce, edges))
    dual = float(sol.z[0])
    dual_min_eig = np.linalg.eigvalsh(dual * l0 - 2 * mass)[0]
    gram_min_eig = np.linalg.eigvalsh(g)[0]
    s = np.sqrt(pi)[:, None] * p / np.sqrt(pi)[None, :]
    eigenvalues = np.linalg.eigvalsh((s + s.T) / 2)
    target = 2 / (1 - eigenvalues[-2])
    assert abs(flow.fun + metric.fun) < 1e-7
    assert max(flow_res, metric_res, abs(denominator - 1)) < 1e-7
    assert abs(numerator - target) < 1e-7
    assert gram_min_eig > -1e-7 and dual_min_eig > -1e-7
    assert abs(dual - numerator) < 1e-7
    return (flow.fun, -metric.fun, abs(flow.fun + metric.fun), target,
            numerator, abs(numerator - target), dual - numerator,
            flow_res, metric_res, abs(denominator - 1), gram_min_eig, dual_min_eig)


print("\nEXACT SPECTRAL CHECKS")
z = sp.Symbol("z")
for name, n, edges in [
    ("P5", 5, [(i, i + 1, 1) for i in range(4)]),
    ("P6", 6, [(i, i + 1, 1) for i in range(5)]),
    ("C5", 5, [(i, (i + 1) % 5, 1) for i in range(5)]),
    ("K4", 4, [(i, j, 1) for i, j in combinations(range(4), 2)]),
    ("Petersen", 10, [(i, (i + 1) % 5, 1) for i in range(5)]
     + [(i, i + 5, 1) for i in range(5)]
     + [(5 + i, 5 + (i + 2) % 5, 1) for i in range(5)])]:
    p, pi = walk(n, edges)
    roots = sorted(p.eigenvals(), key=lambda x: float(x), reverse=True)
    tau = sp.simplify(1 / (1 - roots[1]))
    print(name, "charpoly =", sp.factor(p.charpoly(z).as_expr()),
          "; lambda2 =", roots[1], "; tau2 =", tau,
          "; minpoly(tau2) =", sp.minimal_polynomial(tau, z))
    if name == "P6":
        assert sp.simplify(tau - 3 - sp.sqrt(5)) == 0
        f = sp.Matrix([sp.cos(sp.pi * j / 5) for j in range(6)])
        assert all(sp.simplify(v) == 0 for v in p * f - roots[1] * f)
        c = [pi[i] * p[i, i + 1] for i in range(5)]
        cutloads = [sp.simplify(2 * sum(pi[:i + 1]) * (1 - sum(pi[:i + 1])) / c[i])
                    for i in range(5)]
        print("P6 independent tree-cut ratios =", cutloads,
              "; end-to-end unit energy =", sum(1 / v for v in c))

print("\nSMALL QP ATTEMPTS (exact algebra plus independent SLSQP)")
x, y = sp.symbols("x y", real=True)
probes = [
    ("singular_unconstrained", (x + y) ** 2 - 2 * (x + y),
     (sp.Rational(1, 2), sp.Rational(1, 2)), -1,
     [], [(None, None), (None, None)]),
    ("strip_no_optimal_vertex", x ** 2 - x,
     (sp.Rational(1, 2), sp.Integer(1)), sp.Rational(-1, 4),
     [], [(0, 1), (1, None)]),
    ("optimal_affine_face_no_vertices", x ** 2,
     (sp.Integer(1), sp.Integer(0)), 1,
     [], [(1, None), (None, None)]),
    ("flat_objective_lineality", sp.Integer(0),
     (sp.Integer(2), sp.Integer(-1)), 0,
     [{"type": "eq", "fun": lambda v: v[0] + v[1] - 1}],
     [(None, None), (None, None)]),
]
for name, objective, rational_point, expected, constraints, bounds in probes:
    exact = sp.expand(objective - expected)
    assert objective.subs({x: rational_point[0], y: rational_point[1]}) == expected
    fun = sp.lambdify((x, y), objective, "numpy")
    grad = sp.lambdify((x, y), [sp.diff(objective, x), sp.diff(objective, y)], "numpy")
    res = minimize(lambda v: float(fun(*v)), [2.3, 1.7],
                   jac=lambda v: np.array(grad(*v), dtype=float),
                   constraints=constraints, bounds=bounds, method="SLSQP",
                   options={"ftol": 1e-12, "maxiter": 100})
    assert res.success and abs(res.fun - float(expected)) < 1e-9, res
    print(name, "; rational minimizer =", rational_point,
          "; exact minimum =", expected, "; g-min =", sp.factor(exact),
          "; numerical =", f"{res.fun:.12g}")
print("Excluded convex QCQP: min x subject to x^2 <= 2 has optimum -sqrt(2).")
print("Excluded open feasible set: min x subject to x > 0 has infimum 0, unattained.")

print("\nCOUNTEREXAMPLES TO AUXILIARY SENTENCES")
print("Triangle chain pi=(1/3,1/3,1/3), c_e=1/6:",
      "lengths (4,1,1), C(lengths)=1; shortest distances (2,1,1), C=2/3.")
points = [sp.Integer(0), sp.Integer(1), sp.Integer(2)]
print("Squared Euclidean triangle: distances d01=1, d12=1, d02=4 > 1+1.")
d = sp.Matrix(5, 5, lambda i, j: 0 if i == j else
              (2 if (i < 2) == (j < 2) else 1))
alpha = sp.Matrix([3, 3, -2, -2, -2])
print("K2,3 graph metric: sum alpha =", sum(alpha),
      "; alpha^T d alpha =", (alpha.T * d * alpha)[0], "> 0 (not negative type).")

print("\nINDEPENDENT LP / SDP OPTIMA")
print("name | congestion | metric_max | abs_gap_i | 2tau | SDP_max | abs_gap_ii | SDP_dual_minus_primal")
cases = {}
for n in (3, 5, 6):
    cases[f"P{n}"] = (n, [(i, i + 1, 1) for i in range(n - 1)])
for n in (3, 4, 5, 6):
    cases[f"C{n}"] = (n, [(i, (i + 1) % n, 1) for i in range(n)])
for n in (4, 6):
    cases[f"star{n}"] = (n, [(0, j, 1) for j in range(1, n)])
cases["K4"] = (4, [(i, j, 1) for i, j in combinations(range(4), 2)])
# Draw every possible integer weight once: zero means an absent edge.
rng = np.random.default_rng(88421)
weighted = [(i, j, int(rng.integers(0, 5))) for i, j in combinations(range(5), 2)]
weighted = [(i, j, w) for i, j, w in weighted if w]
cases["weighted5"] = (5, weighted)
print("weighted5 edges (i,j,w) =", weighted)
worst = np.zeros(5)
for name, (n, edges) in cases.items():
    values = programs(n, edges)
    print(name, "|", " | ".join(f"{v:.12g}" for v in values[:7]), flush=True)
    worst = np.maximum(worst, [values[7], values[8], values[9],
                                max(0, -values[10]), max(0, -values[11])])
print("maximum residuals: flow, metric, SDP C=1, negative Gram eigenvalue, negative dual eigenvalue:",
      [float(v) for v in worst])
print("elapsed_seconds =", round(time.monotonic() - START, 3))
print("peak_RSS_bytes_on_macOS =", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print("ALL INDEPENDENT CHECKS PASSED")
