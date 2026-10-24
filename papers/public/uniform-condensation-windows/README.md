# Uniform condensation windows for zero-radius random allocations

Yitzchak Shmalo, Einstein Institute of Mathematics, The Hebrew University of Jerusalem.

The paper proves that for any fixed nonnegative weight sequence with `w_0 > 0` and zero
radius of convergence there are arbitrarily large intervals of total masses on which a
single box carries almost all the mass, uniformly over box counts at densities in a compact
subset of `(0, infinity)`. Every admissible mass path of positive finite limiting density
therefore has a subsequence exhibiting complete condensation. This answers Problem 19.41 of
Janson's survey (Problem 18.40 in the preprint) in the negative. A matching sharpness
theorem shows that multiplicative density of a sampled index set is necessary and
sufficient for the universal subsequence statement.

- `main.tex`, `main.pdf` — the manuscript.
- `code/` — exact-arithmetic checks of the finite algebraic components. Python standard
  library only; every assertion is on rationals or integers, never on floats.
- `lean/` — ten of those components restated and proved in Lean 4 against Mathlib.
- `audits/` — the review record.

## Building

```
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
python code/check_uniform_windows.py
python code/check_full_path.py
python code/audit_stress_checks.py
```

The Lean files are checked against Mathlib on Lean 4.33.1:

```
lake env lean lean/PartA.lean
lake env lean lean/PartB.lean
```

Each theorem prints its axiom dependencies; all ten use nothing beyond `propext`,
`Classical.choice` and `Quot.sound`.

## Scope of the checks

The finite computations verify identities and inequalities on explicit finite data. They do
not establish the asymptotic theorem, and the Lean development does not formalize it. What
Lean covers is the finite algebraic skeleton: the falling-factorial numerator bound and the
exponent bookkeeping of the insertion lemma, the closed forms of the geometric tails, the
kernel coefficient total behind the contraction constant, the decay bound on the truncated
auxiliary weights, the Markov threshold, and the strict descent of the greedy residual
construction.

The review record in `audits/` contains five review passes made during drafting and three
later independent audit passes. Neither set is refereeing.
