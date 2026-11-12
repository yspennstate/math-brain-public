# The stationary law of the leftmost particles in Aldous's drift-jump process

Yitzchak Shmalo

Paper: [paper/main.pdf](paper/main.pdf) (LaTeX source in `paper/main.tex`).

In Aldous's drift-jump process, k particles 0 < X_1 < ... < X_k move right with velocity equal to their position, and at the
events of a rate-one space-time Poisson process the nearest particle to the right of the event jumps to it. Aldous
(open problem, February 2018) asked for a fairly explicit description of the stationary distribution.

The paper proves:

1. The stationary distribution is unique, the law at time t converges to it in total variation from every start, and in
   stationarity X_i = Γ_{τ_i}, where Γ_1 < Γ_2 < ... is a rate-one Poisson process and, independently, τ_i is the first n
   at which the longest increasing subsequence of n independent uniforms reaches length i. This is a form of the
   representation (42) in the 1993 notes of Aldous and Diaconis.
2. Every joint survival probability P(X_{k_1} > s_1, ..., X_{k_r} > s_r) equals e^{-s_r} times a finite determinant with
   modified-Bessel-function entries, of size at most k(k-1) for the first k particles. For one particle it is Gessel's
   Toeplitz determinant.
3. E(X_i - X_{i-1}) is the constant c(i) of Aldous and Diaconis (1999, Proposition 9) in the logarithmic growth of the
   i-th pile in patience sorting.

## Files

- `code/checks.py` evaluates the determinant in 40-digit arithmetic and compares it with exhaustive enumeration over
  permutations, closed forms, Gessel's determinant and an exact simulation of the dynamics; `code/checks_output.txt` is
  its output (`python checks.py`, needs `mpmath`).
- `lean/GeneralBlockCertificate.lean` proves in Lean 4 with Mathlib the block determinant identity
  det [[A, F], [-G, -Q]] = det A · det(G A⁻¹ F - Q) used in the proof; `lean/lean_output.txt` records the check.
