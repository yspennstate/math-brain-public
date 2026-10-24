# The drawn length of the critical beta-splitting tree grows linearly

Companion material for the paper of the same title (Y. Shmalo, October 2026). [Read the paper](paper/main.pdf).

In the critical beta-splitting tree with n leaves, a clade of m leaves splits into clades of i and m − i leaves
with probability proportional to 1/(i(m − i)). The drawn length of a binary tree is the total length of the
vertical lines in its cladogram, with each vertex drawn at the level of its height. Open Problem 14 of D. J. Aldous
and S. Janson, *The critical beta-splitting random tree II: overview and open problems*, asks for a proof that the
expected drawn length L_n grows roughly like n log⁴ n. The paper shows that L_n/n converges to a finite constant λ,
with 4.800 < λ < 5.372 and λ ≈ 4.88 numerically.

The heuristic behind n log⁴ n counts n·a(n,m) clades of size m, where a(n,m) is the probability that a uniformly
chosen leaf lies in a clade of exactly m leaves; the expected number of such clades is (n/m)·a(n,m). The proof
combines an exponential moment bound for the height with a bound, uniform in n, on the time the harmonic descent
chain spends in a dyadic block, together with the convergence of a(n,m) as n → ∞ (Theorem 18 of Aldous and
Janson). A deterministic comparison with the sum of the leaf depths gives L_n = O(n log² n) directly.

## Contents

- `paper/` the LaTeX source and the compiled PDF.
- `code/check.py` checks of the computations in the paper. Exact rational arithmetic and enumeration cover the
  small cases: Lemma 2.1 on all 6918 ordered binary trees with at most 10 leaves, Lemma 2.2 and formula (2.2) for
  small n, and Table 1. Floating point covers the distribution of the height for trees with up to 4000 leaves:
  Lemmas 3.1 and 3.2, Table 2, the bracket for λ and the two estimates of λ in Section 5. `code/check.out` is its
  output.
- `lean/DrawnLength.lean` a proof of Lemma 2.1 for all finite rooted binary trees, in Lean 4 with the core library
  only (no Mathlib). `lean/DrawnLength.out` is the output, with the axioms each theorem depends on.

## Reproducing

    python code/check.py

needs Python 3.6 or later and numpy, and takes about a minute. For the Lean file, install the version pinned in
`lean/lean-toolchain` (Lean 4.33.1) and run

    cd lean
    lean DrawnLength.lean

which takes a few seconds. A successful run prints only the `#print axioms` lines at the end of the file.
