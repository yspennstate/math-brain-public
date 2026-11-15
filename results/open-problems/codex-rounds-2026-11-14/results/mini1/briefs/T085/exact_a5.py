"""Exact A_5 witness with four distinct generators, including two charpoly methods."""
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
from exact_witness import action_matrix, factor_data, newton_from_word_returns, roots

ROOT = Path(__file__).resolve().parent
X = sp.Symbol("x")


def main():
    start = time.monotonic()
    s = Permutation(2, 3, 4, size=5)
    t = Permutation([4, 2, 0, 1, 3])
    group = PermutationGroup([s, t])
    elements = list(group.generate_schreier_sims())
    assert group.order() == len(elements) == 60
    generators = [s, ~s, t, ~t]
    assert len(set(generators)) == 4
    assert all(g.signature() == 1 for g in generators)
    reg = action_matrix(elements, lambda g, h: h*g, generators)
    nat = action_matrix(list(range(5)), lambda g, v: g(v), generators)
    subsets = list(itertools.combinations(range(5), 2))
    pairs = action_matrix(subsets, lambda g, v: tuple(sorted(g(i) for i in v)), generators)
    exterior = sp.zeros(10)
    ix = {v: i for i, v in enumerate(subsets)}
    for i, (a, b) in enumerate(subsets):
        for g in generators:
            ga, gb = g(a), g(b)
            exterior[i, ix[tuple(sorted((ga, gb)))]] += 1 if ga < gb else -1
    assert exterior == exterior.T
    wedge_basis = list(itertools.combinations(range(4), 2))
    ext_std = sp.zeros(6)
    for g in generators:
        b = sp.Matrix(4, 4, lambda i, j: int(i == g(j)) - int(i == g(4)))
        for i, row in enumerate(wedge_basis):
            for j, col in enumerate(wedge_basis):
                ext_std[i, j] += b.extract(row, col).det()
    matrices = {"regular": reg, "natural": nat, "two_subsets": pairs,
                "exterior_square_natural": exterior, "exterior_square_standard": ext_std}
    polys = {key: sp.Poly(a.charpoly(X).as_expr(), X) for key, a in matrices.items()}
    independent, traces = newton_from_word_returns(5, (0, 1, 3, 4, 2),
                                                   (4, 2, 0, 1, 3), 60, 60)
    assert independent == polys["regular"]
    std = polys["natural"].exquo(sp.Poly(X-4, X))
    assert polys["exterior_square_natural"] == std * polys["exterior_square_standard"]
    top = roots(polys["regular"].exquo(sp.Poly(X-4, X)))[-1]
    top_nat = roots(std)[-1]
    top_pairs = roots(polys["two_subsets"].exquo(sp.Poly(X-4, X)))[-1]
    assert top[3] == roots(polys["exterior_square_standard"])[-1][3]
    assert top[0] > top_nat[1] and top[0] > top_pairs[1]
    result = {
        "sigma_cycles_one_based": "(3 4 5)",
        "tau_cycles_one_based": "(1 5 4 2 3)", "group_order": 60,
        "four_distinct_generators": True,
        "characteristic_polynomials": {k: factor_data(v) for k, v in polys.items()},
        "full_charpoly_matches_word_return_newton": True,
        "trace_A_powers_1_through_8": traces[:8],
        "top_regular_interval": [str(v) for v in top[:2]],
        "top_natural_interval": [str(v) for v in top_nat[:2]],
        "top_two_subset_interval": [str(v) for v in top_pairs[:2]],
        "exterior_square_standard_adjacency": [list(map(int, ext_std.row(i))) for i in range(6)],
        "elapsed_seconds": time.monotonic() - start,
        "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "nice": os.getpriority(os.PRIO_PROCESS, 0),
    }
    # Keep every integer used by the Newton certificate, not just a prefix.
    with (ROOT / "exact_a5_newton.csv").open("w") as out:
        out.write("k,word_returns,trace_A_power,charpoly_coefficient\n")
        out.write("0,1,60,1\n")
        for k, tr in enumerate(traces, 1):
            out.write(f"{k},{tr//60},{tr},{independent.all_coeffs()[k]}\n")
    assert result["peak_rss_bytes"] < 1_000_000_000
    assert result["elapsed_seconds"] < 1100
    (ROOT / "exact_a5.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
