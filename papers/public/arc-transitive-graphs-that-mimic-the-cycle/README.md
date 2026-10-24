# Arc-transitive graphs that mimic the cycle

Companion material for the paper of the same title (Y. Shmalo, September 2026), which answers Open Problem 7.27
of Aldous and Fill, *Reversible Markov Chains and Random Walks on Graphs*: over arc-transitive graphs other than
the cycles, the maximal mean commute time need not be O(n log n), the relaxation time need not be O(n), and the
ratio of the maximal mean commute time to twice the average hitting time need not tend to one. The graphs
C_m[K_r-bar], the m-cycle with every vertex replaced by r pairwise non-adjacent copies, are arc-transitive of
degree 2r and behave like the cycle: mean hitting times j(m-j)+(r-1)m at cycle-distance j, and rm between
copies of the same vertex. The paper also gives the hitting times, the average hitting time and the relaxation
time of the blow-up H[K_r-bar] of any regular graph H in terms of those of H, and shows that every arc-transitive
graph is such a blow-up of a twin-free arc-transitive graph, so that the question reduces to twin-free graphs.

Contents

- `paper/` the LaTeX source and the compiled PDF.
- `numerics/blowup_walks.py` exact rational mean hitting times on C_m[K_r-bar] and on blow-ups of K_2, K_4,
  K_{3,3}, the 3-cube, the Petersen graph and C_6; the parameters tau*, tau_0, tau_2; an arc-transitivity check
  by computing the orbit of one arc; `numerics/results.md` is its output.
- `figures/ratio.pdf` the ratio tau*/(2 tau_0) for C_m[K_2-bar].
- `lean/P0208.lean` and `lean/BlowUpArithmetic.lean` the Lean 4 verification of the arithmetic (harmonic equation
  of the hitting-time formula, the twin and neighbour values, the cycle sum, the formula for tau_0, the limit of
  the ratio), with the build log and axiom report. They compile against Mathlib with Lean 4.33.1
  (`lean/lean-toolchain`, `lean/lake-manifest.json`).

To reproduce the numerics: `python numerics/blowup_walks.py` (numpy, matplotlib). To check the Lean files: put them
in a Lake project depending on Mathlib at the pinned commit and run `lake env lean P0208.lean` and
`lake env lean BlowUpArithmetic.lean`.
