"""Exact certificate for sigma=(4 5), tau=(1 2 3 4 5) in S_5.

Two independent full characteristic polynomial calculations:
SymPy's integer-matrix algorithm and Newton identities from exact word returns.
"""
import os
for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
            "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[key] = "1"

import itertools
import json
import resource
import time
from pathlib import Path
import sympy as sp
from sympy.combinatorics import Permutation, PermutationGroup

ROOT = Path(__file__).resolve().parent
X = sp.Symbol("x")


def action_matrix(vertices, action, generators, signs=None):
    ix = {v: i for i, v in enumerate(vertices)}
    a = sp.zeros(len(vertices))
    if signs is None:
        signs = [1] * len(generators)
    for i, v in enumerate(vertices):
        for g, sign in zip(generators, signs):
            a[i, ix[action(g, v)]] += sign
    assert a == a.T
    return a


def factor_data(poly):
    return [{"factor": str(f.as_expr()), "multiplicity": m}
            for f, m in sp.factor_list(sp.Poly(poly, X))[1]]


def roots(poly):
    found = []
    for f, mult in sp.factor_list(sp.Poly(poly, X))[1]:
        for (a, b), m in f.intervals(eps=sp.Rational(1, 10**14)):
            found.append((a, b, mult*m, str(f.as_expr())))
    return sorted(found, key=lambda r: (r[0] + r[1]) / 2)


def newton_from_word_returns(n, s, t, degree, group_order):
    identity = tuple(range(n))
    def inverse(p):
        return tuple(p.index(i) for i in range(n))
    gs = (s, inverse(s), t, inverse(t))
    distribution = {identity: 1}
    traces = []
    coefficients = [1]
    for k in range(1, degree + 1):
        nxt = {}
        for h, count in distribution.items():
            for g in gs:
                gh = tuple(g[h[i]] for i in range(n))
                nxt[gh] = nxt.get(gh, 0) + count
        distribution = nxt
        assert sum(distribution.values()) == 4**k
        traces.append(group_order * distribution.get(identity, 0))
        numerator = sum(coefficients[k-i] * traces[i-1] for i in range(1, k+1))
        assert numerator % k == 0
        coefficients.append(-numerator // k)
    return sp.Poly.from_list(coefficients, X), traces


def main():
    start = time.monotonic()
    s = Permutation(3, 4, size=5)
    t = Permutation(0, 1, 2, 3, 4)
    group = PermutationGroup([s, t])
    elements = list(group.generate_schreier_sims())
    assert group.order() == len(elements) == 120
    generators = [s, ~s, t, ~t]
    reg = action_matrix(elements, lambda g, h: h*g, generators)
    nat = action_matrix(list(range(5)), lambda g, v: g(v), generators)
    signed = action_matrix(list(range(5)), lambda g, v: g(v), generators,
                           [g.signature() for g in generators])
    subsets = list(itertools.combinations(range(5), 2))
    pairs = action_matrix(subsets, lambda g, v: tuple(sorted(g(i) for i in v)), generators)
    signed_pairs = action_matrix(subsets, lambda g, v: tuple(sorted(g(i) for i in v)),
                                 generators, [g.signature() for g in generators])
    # Exterior square of the natural action: orientation, not permutation sign.
    exterior = sp.zeros(10)
    subset_index = {v: i for i, v in enumerate(subsets)}
    for i, (a, b) in enumerate(subsets):
        for g in generators:
            ga, gb = g(a), g(b)
            exterior[i, subset_index[tuple(sorted((ga, gb)))]] += 1 if ga < gb else -1
    assert exterior == exterior.T
    # Independently restrict to standard basis e_i-e_5, then take 2x2 minors.
    wedge_basis = list(itertools.combinations(range(4), 2))
    exterior_standard = sp.zeros(6)
    for g in generators:
        b = sp.Matrix(4, 4, lambda i, j: int(i == g(j)) - int(i == g(4)))
        for i, row in enumerate(wedge_basis):
            for j, col in enumerate(wedge_basis):
                exterior_standard[i, j] += b.extract(row, col).det()
    matrices = {"regular": reg, "natural": nat, "signed_natural": signed,
                "two_subsets": pairs, "signed_two_subsets": signed_pairs,
                "exterior_square_natural": exterior,
                "exterior_square_standard": exterior_standard}
    polys = {key: sp.Poly(a.charpoly(X).as_expr(), X) for key, a in matrices.items()}
    independent, traces = newton_from_word_returns(
        5, (0, 1, 2, 4, 3), (1, 2, 3, 4, 0), 120, 120)
    assert independent == polys["regular"]
    # Constants: eigenvalue 4 in natural action, 0 in its sign twist.
    standard = polys["natural"].exquo(sp.Poly(X-4, X))
    sign_standard = polys["signed_natural"].exquo(sp.Poly(X, X))
    regular_nontrivial = polys["regular"].exquo(sp.Poly(X-4, X))
    subset_nontrivial = polys["two_subsets"].exquo(sp.Poly(X-4, X))
    top_regular = roots(regular_nontrivial)[-1]
    top_subset = roots(subset_nontrivial)[-1]
    top_signed_subset = roots(polys["signed_two_subsets"])[-1]
    top_std = roots(standard)[-1]
    top_sign_std = roots(sign_standard)[-1]
    assert polys["exterior_square_natural"] == standard * polys["exterior_square_standard"]
    top_exterior = roots(polys["exterior_square_standard"])[-1]
    print("FACTORS", json.dumps({k: factor_data(v) for k, v in polys.items()}), flush=True)
    print("TOP_FACTORS", top_regular, top_subset, top_signed_subset, flush=True)
    assert top_regular[3] == top_exterior[3]
    assert top_regular[0] > top_std[1]
    assert top_regular[0] > top_sign_std[1]
    assert top_regular[0] > 0  # Sign representation has adjacency eigenvalue 0.
    gap_interval = (1 - top_regular[1]/4, 1 - top_regular[0]/4)
    # Rational spectral certificates avoid reliance on displayed decimals.
    assert sp.Rational(938, 10000) < gap_interval[0]
    assert gap_interval[1] < sp.Rational(939, 10000)
    assert top_std[1] < sp.Rational(27, 10)
    assert top_sign_std[1] < sp.Rational(27, 10)
    result = {
        "sigma_cycles_one_based": "(4 5)", "tau_cycles_one_based": "(1 2 3 4 5)",
        "group_order": 120,
        "characteristic_polynomials": {k: factor_data(v) for k, v in polys.items()},
        "full_charpoly_matches_word_return_newton": True,
        "trace_A_powers_1_through_8": traces[:8],
        "largest_nontrivial_adjacency_factor": top_regular[3],
        "largest_nontrivial_adjacency_interval": [str(v) for v in top_regular[:2]],
        "gap_interval": [str(v) for v in gap_interval],
        "gap_decimal": [float(v) for v in gap_interval],
        "standard_top_interval": [str(v) for v in top_std[:2]],
        "sign_standard_top_interval": [str(v) for v in top_sign_std[:2]],
        "two_subset_contains_top_factor": top_regular[3] == top_subset[3],
        "signed_two_subset_contains_top_factor": top_regular[3] == top_signed_subset[3],
        "exterior_square_standard_contains_top_factor": True,
        "exterior_square_standard_adjacency": [list(map(int, exterior_standard.row(i)))
                                               for i in range(6)],
        "elapsed_seconds": time.monotonic() - start,
        "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "nice": os.getpriority(os.PRIO_PROCESS, 0),
    }
    assert result["peak_rss_bytes"] < 1_000_000_000
    assert result["elapsed_seconds"] < 1100
    (ROOT / "exact_witness.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    main()
