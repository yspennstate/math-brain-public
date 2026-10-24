# The sharp diameter threshold for unimodality of free Brownian motion

Companion material for the paper of the same title (Y. Shmalo, September 2026), which answers Problem 3.3 of
Hasebe and Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*,
ALEA 15 (2018): for a compactly supported probability measure $\mu$ with support diameter $D$, the law
$\mu \boxplus S(0,t)$ of free Brownian motion started from $\mu$ is unimodal for every $t \ge D^2$, the constant is
sharp, and the symmetric two-point law is the only extremal measure.

Contents

- `paper/` the LaTeX source and the compiled PDF.
- `numerics/free_unimodality.py` the numerical companion: symbolic verification of every identity in the two proofs,
  a scan of the two-atom criterion, the level-set criterion, and the density of $\mu \boxplus S(0,t)$ computed from
  Biane's parametrisation with its modes counted; `numerics/results.md` is its output.
- `figures/` the two figures of the paper, produced by the script.
- `lean/FreeUnimodality.lean` the Lean 4 verification of the polynomial core of both proofs, with the build log and
  the axiom report in `lean/`. It compiles against Mathlib with Lean 4.33.1 (see `lean/lean-toolchain` and
  `lean/lake-manifest.json` for the pinned versions); the file is self-contained and can be dropped into any project
  with a Mathlib dependency.

To reproduce the numerics: `python numerics/free_unimodality.py` (numpy, sympy, matplotlib). To check the Lean
file: put it in a Lake project that depends on Mathlib at the pinned commit and run `lake env lean FreeUnimodality.lean`.
