# Phi-mixing implies interlaced rho-mixing for Markov chains

Yitzchak Shmalo, Einstein Institute of Mathematics, The Hebrew University of Jerusalem.

The paper proves that every phi-mixing Markov chain on a standard Borel space, stationary or not,
time-homogeneous or not, is interlaced rho-mixing, with the quantitative bound

    rho*(n) <= min{1, 2 sqrt(2 phi(n))}

and the sharper bound `rho*(n) <= 2 sqrt(2 phi(n) (1 - 2 phi(n)))` when `phi(n) <= 1/4`. This answers
Question 5 of Bradley's 2005 survey (Probability Surveys 2, 107-144) in the affirmative. Three
examples show what is sharp: a six-state chain with `phi(1) = eps` and `rho*(1) = sqrt(2 eps)`, a
countable reset chain in which the exponential rate is exactly halved, and a two-state chain in
which the leading coefficient two of the path estimate is attained to first order.

- `main.tex`, `main.pdf` - the manuscript (18 September 2026).
- `lean/` - the finite components of the argument, stated and proved in Lean 4 against Mathlib.
- `checks/` - the exact-arithmetic checker of the six-state identities and two adversarial
  floating-point checkers of the main inequalities on random finite chains, with saved outputs.
- `audit/` - the review record.

## Building the paper

```
pdflatex main.tex
pdflatex main.tex
```

All references are embedded in the TeX file. No external bibliography or figures are required.

## Lean

The three files are checked from a project that already has Mathlib built:

```
lake env lean lean/Analysis.lean
lake env lean lean/Finite.lean
lean env lean lean/Reset.lean
```

Toolchain: Lean 4 v4.33.1; the Mathlib revision is recorded in `lean/MATHLIB_REV.txt`, and the
compiler output with the axiom listing of every theorem is in `lean/*.out`. Every theorem depends on
`propext`, `Classical.choice` and `Quot.sound` only.

What is covered, by file:

- `Analysis.lean` - the envelope function Psi of the paper: `sin(2 arcsin r) = 2 r sqrt(1 - r^2)`,
  saturation on `[1/sqrt 2, 1]`, monotonicity, `Psi(r) <= 2r`, the identity
  `Psi(sqrt(2 phi)) = 2 sqrt(2 phi (1 - 2 phi))`, the derivation of both bounds of Theorem 1.1 from
  `rho* <= Psi(kappa)` and `kappa^2 <= 2 phi`, the thresholds `phi < 1/8` and `phi < 1/4`, the rate
  transfer of Corollary 5.2, the consistency of the envelope of Section 9, and the two-sided
  expansions behind Proposition 8.1.
- `Finite.lean` - the six-state chain of Section 6 (stochasticity, invariance, `K^2 = Pi`, row
  distances, the attained row diameter `2 eps`, the edge second moment and posterior mean, the
  posterior variance identity), the binary channel of Section 8 (the posterior variance formula and
  `rho^2 <= r^2`), the path matrix of Section 4 (the `2 kappa` bilinear bound, the quadratic-form
  bound, the sine eigenvector identity), and the finite case of Lemma 2.1 (Dobrushin's oscillation
  contraction, the eigenvalue bound by the row diameter, total-variation contraction under
  postprocessing).
- `Reset.lean` - the reset chain of Section 7: the recursion characterising the n-step kernel, its
  row sums, and the invariant law with its balance equations as convergent series.

The Lean development does not formalise the measure-theoretic parts of the argument (the row-good
set, side-separated conditioning, the prefix interface, Peyre's tensorization theorems, the
finite-coordinate approximation).

## Checks

```
python checks/check.py > checks/checks.json
python checks/break_main_theorem.py
python checks/break_small_diameter.py
```

`check.py` (Python 3.10+, numpy) verifies the six-state identities in exact rational arithmetic and
runs floating-point diagnostics of the channel inequality, the path norms and the two-state
covariance formulas. The two `break_*` scripts compute the exact maximal correlation of `(X_S, X_T)`
for random finite chains and random interlacings by a singular value decomposition of the
normalised joint law, and compare it with the bounds `Psi(sqrt Delta)`, `2 sqrt(Delta) cos(pi/(m+1))`
and `min(1, 2 sqrt(2 phi))` of the paper; the saved outputs record zero violations over about
24,000 tests. None of this proves the infinite-state theorem.
