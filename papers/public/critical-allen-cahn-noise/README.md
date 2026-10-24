# Maximal energy bounds fail for the stochastic Allen-Cahn equation with critical quadratic noise

Yitzchak Shmalo

The paper (`paper/main.pdf`) answers Problems 4 and 5 of A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal
regularity: an extended survey*, NoDEA Nonlinear Differential Equations Appl. 32 (2025), Paper No. 123
([arXiv:2501.18561](https://arxiv.org/abs/2501.18561)), in the negative.

The equation is du = (u_xx + u - u^3) dt + sqrt(2) u^2 dW on the one-dimensional torus, driven by one real Brownian
motion, with a constant initial value a > 0.

- **Theorem 1.1.** The squared running maximum Z_T = sup_{t <= T} u(t)^2 satisfies c/y <= P(Z_T >= y) <= K/y for
  large y, with explicit constants c and K. The maximal moments E sup |u|^p are finite exactly for p < 2, and the
  moments at a fixed time are finite exactly for p < 4.
- **Corollary 1.2.** The equation satisfies the hypotheses of Theorem 6.4 of the survey; by Remark 4.1, sqrt(2) is
  the largest noise constant for which it does. Since E sup_{t <= T} ||u(t)||^2 is infinite, no bound
  E sup ||u||^2 <= C_T (1 + E ||u_0||^2) holds (Problem 4). The solutions started at 1/n converge to 0 in
  L^p(Omega; L^2(0,T;H^1) and C([0,T];L^2)) for every p < 2, while their norms in L^2(Omega; C([0,T];L^2)) are
  infinite (Problem 5).
- **Remark 3.3.** For noise gamma u^2 with gamma^2 < 2 the same construction, with a Bessel process of dimension
  3 + 2/gamma^2, gives E sup_{t <= T} u(t)^2 <= a^2 e^{2T} (2 + gamma^2)/(2 - gamma^2).

The solution started from a constant is e^t/sqrt(2) times the reciprocal of a time-changed four-dimensional Bessel
process.

## Contents

- `paper/`: the LaTeX source and the PDF.
- `lean/EndpointCore.lean`: a Lean 4 / Mathlib check of the measure-theoretic and algebraic steps. These are the
  dominated-convergence lemma behind the second proof, the Gaussian expectation defect, the coercivity identity, the
  interpolation indices, the Ito coefficients of 1/U, and the deduction of the two-sided hitting bounds. Section 6 of
  the paper lists what is and is not formalized. `EndpointCore.out` records the axioms each theorem depends on
  (`propext`, `Classical.choice`, `Quot.sound` only).

## Reproducing

Lean (toolchain in `lean/lean-toolchain`, Mathlib pinned in `lean/lake-manifest.json`):

```
cd lean
lake exe cache get
lake env lean EndpointCore.lean
```

The paper builds with `pdflatex main.tex` (three passes) in `paper/`.
