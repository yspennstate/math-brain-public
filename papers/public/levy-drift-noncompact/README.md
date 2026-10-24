# A Lévy random drift destroys compactness for every confining power

Yitzchak Shmalo

Paper: [paper/main.pdf](paper/main.pdf) (LaTeX source in `paper/main.tex`).

Let V be a two-sided semi-selfsimilar Lévy process of index α in (0,2) and let L^{w+V} = ½(Δ − ∇(w+V)·∇) act on L²(ℝ; e^{−(w+V)}dx). For w₁ = |x|^δ and w₂ = −|x|^δ the unperturbed semigroups are compact exactly when δ > 1. Shiozawa and Wang (arXiv:2607.07410, Proposition 5.2) proved that the perturbed semigroups are noncompact when δ ≤ 1/α, and left δ > 1/α open (their Remark 5.3(ii)).

**Theorem.** Let δ > 1/α. If the Lévy measure of V on one of the two half-lines charges (−∞,0), then the bottom of the essential spectrum of −L^{w₁+V} is 0 almost surely. If one of them charges (0,∞), the same holds for −L^{w₂+V}. In either case the semigroup is noncompact.

**Corollary.** If V changes sign and either α < 1 or the jumps of V go both ways (for instance V symmetric), then both semigroups are noncompact for every δ > 0.

The case α in [1,2) with both Lévy measures on the same half-line is left open for one of the two operators.

The proof builds test functions with disjoint supports around large jumps of V: a jump of size m at distance τ lowers a Rayleigh quotient by a factor e^{−m/2}, the confining power costs only a factor τ^{2δ−2}, and the process has jumps of size of order τ^{1/α} at every scale.

## Computations

`code/checks.py` (Python 3 with NumPy and SciPy; output in `code/checks_output.txt`) checks the energy identity used in the test functions, the unperturbed benchmark (Dirichlet bottom eigenvalues on [x,2x] for δ = 2, 1, 1/2), finite-element bottom eigenvalues for a planted jump against the Rayleigh quotient of the test function, and the first term of the bound on simulated symmetric stable environments. The proofs do not depend on it. The argument is analytic throughout and has no finite or algebraic step suited to a Lean check.

`SHA256SUMS.txt` lists the hashes of the files.
