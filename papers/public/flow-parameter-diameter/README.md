# Multicommodity flow, the relaxation time and the diameter

Yitzchak Shmalo, Einstein Institute of Mathematics, The Hebrew University of Jerusalem.

For a finite reversible Markov chain, the flow parameter (the least congestion of a family of unit flows from each
state to the stationary distribution, measured by the quantity ψ of Lemma 4.21 of Aldous and Fill) is at most a
constant times the relaxation time τ₂ times log n. Open Problem 4.49(ii) of Aldous and Fill's *Reversible Markov
Chains and Random Walks on Graphs*, which they attribute to Sinclair, asks whether log n can be replaced by the
diameter Δ of the transition graph. For general chains the answer is negative for a simple reason: adding transitions
of small probability between all pairs of states of the random walk on an expander makes Δ = 1, does not increase τ₂,
and keeps the flow parameter of order log n. The paper shows that the answer is negative also for simple random walks,
for every constant and already on graphs of diameter two. On the cone over a d-regular Ramanujan graph on n vertices
(a hub joined to every vertex) the diameter is 2, the relaxation time is at most (d+1)/(d+1−2√(d−1)), and the flow
parameter tends to 2(d+1) as n → ∞, so the ratio of the flow parameter to τ₂Δ is at least d+1−2√(d−1) in the limit.
The length-weighted form of the flow parameter fails as well, on these graphs and already on bounded-degree expanders.

On the cone over the incidence graph of a projective plane of order s the flow parameter is

    F = (s+2)(5s³ + 19s² + 13s + 8) / ((s+3)(s+4)(s² + s + 1)),

attained by an explicit routing, and the ratio F/(τ₂Δ) increases with s to 5/2 and exceeds 2 exactly when s ≥ 38.
The first Desarguesian example is PG(2,41), whose cone has 3447 vertices. For simple random walks the diameter bound
holds on graphs of maximum degree D with a constant of order log D, and the cones show that this order cannot be
lowered below log D / log log D; it holds with constant 2 on edge-transitive graphs.

## Files

- `paper/main.pdf`, `paper/main.tex`: the paper (11 October 2026). All references are in the TeX file; run
  `pdflatex main.tex` twice to build it.
- `lean/`: a Lean 4 and Mathlib check of the algebraic identities and numerical inequalities in the proofs.
- `computations/`: the linear programs, the exact certificates and the exact check of the routing on
  projective-plane cones, with the result files behind Tables 1-3.

## Lean

```
cd lean
lake exe cache get
lake build
```

Lean v4.33.1 and Mathlib v4.33.1; the exact Mathlib revision is pinned in `lean/lake-manifest.json`. The file ends
with `#print axioms` for the main theorems, and `lean/FlowParameter.out` is the output of
`lake env lean FlowParameter.lean`: every theorem depends on `propext`, `Classical.choice` and `Quot.sound` only.
There is no `sorry`. The file checks

- `spectrum_quadratic`: the 2 × 2 block in the proof of Lemma 3.1;
- `hub_load`: the value 2(d+1)(1 − π_v) of the hub routing in Lemma 3.2;
- `lengths_sum`, `cert_lower`: the total length and the final inequality of the certificate in Lemma 3.3;
- `r_eq_3d_bound`, `explicit_quantifier`: the explicit quantifiers after the proof of Theorem 1.1;
- `V3_from_cert`, `one_sub_theta`, `theta_mem`, `loads_equal`, `load_eq_V3`: the certificate with r = 3 and the
  routing in the proof of Proposition 5.1, including the equality of the loads on spokes and on base edges;
- `V3_strictMono`, `ratio_strictMonoOn`, `ratio_37_lt_two`, `two_lt_ratio_38`, `two_lt_ratio_iff`: on
  projective-plane cones the ratio F/(τ₂Δ) increases with s and exceeds 2 exactly for s ≥ 38;
- `V3_37`, `V3_41`, `V3_49`: exact entries of Table 1;
- `degree_constant`, `log_constant`: the constants in Proposition 6.1.

The combinatorial inputs to these identities (the spectrum of a cone, the distance counts in the incidence graph of a
projective plane, the shape of the flows) and the duality of Lemma 2.1 are proved in the paper and are not
formalized.

## Computations

Python 3.14 with NumPy 2.4, SciPy 1.17 (the linear programs are solved by HiGHS through `scipy.optimize.linprog`),
NetworkX 3.6 and SymPy 1.14. Run each script from `computations/`.

- `flowlib.py`: the shared code (cones, incidence graphs of PG(2,q), the linear program, the certificates of
  Lemma 2.1 in exact arithmetic, the spectra).
- `pg_algebra.py`: the algebra of Proposition 5.1 in SymPy (the certificate with r = 3, the loads, the derivative of
  the closed form, the threshold s ≥ 38) and the closed-form entries of Table 1. A few seconds.
- `pg_routing_check.py`: builds the routing of Proposition 5.1 on the cones over PG(2,s), s = 2, 3, 4, 5, and checks
  in exact arithmetic that every flow is a unit flow to π and that the load is V₃ on every edge. A few seconds.
- `check_exact.py`: Table 1 at s = 49, the certificate of Lemma 3.3 on projective-plane cones, the Dijkstra evaluator
  of general certificates and the hub routing of Lemma 3.2 in exact arithmetic, and the spectrum of Lemma 3.1 in
  floating point (agreement to about 10⁻¹⁵).
- `sanity_checks.py`: the linear program on small graphs with known values, and on the cones over PG(2,s) for
  s = 2, 3, 4, 5, 7 against the closed form of Proposition 5.1 (about an hour, nearly all of it the linear program
  for s = 7).
- `rr_lp.py` → `rr_lp_results.csv`: Table 2 (cones over random regular graphs, linear program and certificates;
  under an hour).
- `rr_dual_large.py` → `rr_dual_large_results.csv` and `lps_cone.py` → `lps_results.csv`: Table 3 (exact certificates
  on larger random cones and on the cones over the Lubotzky-Phillips-Sarnak graphs X^{5,q}). On a laptop the first
  took between 16 and 58 minutes and the second between 5 and 43 minutes, depending on the other load on the
  machine; the largest graph accounts for most of each (the `seconds` column of each result file).
- `make_tables.py`: prints the rows of Tables 1-3 from the closed form and the result files.

The three table scripts rewrite their result files. The random graphs are those of
`networkx.random_regular_graph` (NetworkX 3.6.1) with seed 1; the scripts search upward from seed 1 for a connected
graph, and seed 1 is connected for every size used.

The linear-program values carry the solver's tolerance, about 10⁻⁸; the certificates are computed exactly and are lower bounds on F, printed
rounded to four decimals.
None of the computations reaches the regime of Theorem 1.2, which the proof covers.

## Funding

The research presented in this paper was supported by the European Research Council (ERC) under the European
Union's Horizon Europe research and innovation programme (grant agreement No. 101041711), by the Simons Foundation as
part of the Collaboration on the Mathematical and Scientific Foundations of Deep Learning, by Heights Labs, by Convex
Nexus Capital, by the Israel Science Foundation (grant number 2258/19), and by the Israel Science Foundation (ISF
Grant 4101/25). Computational resources were provided in part by Google Cloud through its education credits program
(credit 530550103).

The author holds equity in Heights Labs and in Convex Nexus Capital and has a management role at Convex Nexus
Capital. These entities are included in the funding declaration above.

## Citation

Y. Shmalo, *Multicommodity flow, the relaxation time and the diameter*, 2026.
https://github.com/yspennstate/flow-parameter-diameter
