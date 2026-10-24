# Tang Question 4.11 — periodic-tree counterexample

This folder packages the source-matching periodic-tree clause of Pengfei Tang, *A note on some critical thresholds of Bernoulli percolation*, arXiv:2012.01135v2 / Electronic Journal of Probability 28 (2023), Question 4.11 in the source PDF.

## Exact proved scope

For Bernoulli bond percolation, let `T_3` be a path of three edges from the root followed by a full rooted binary tree. In Tang's periodic-tree definition, `T_3` is 3-periodic. Its critical probability is `p_c=1/2`, and on `(1/2,1)` its root percolation probability is

`theta(p)=2p^2-p`,

so `theta''(p)=4>0`. Therefore the universal periodic-tree concavity assertion in Question 4.11 is false.

The package does **not** resolve the separate transitive-graph clause of the same question.

## Physical branch

The binary tail extinction probability satisfies `q=(1-p+p q)^2`. For `p>1/2` the physical extinction probability is the smaller fixed point `q=((1-p)/p)^2`; the always-present algebraic fixed point `q=1` is not selected. Multiplication by the probability `p^3` that all stem edges are open gives the stated `theta`.

## Files

- `main.tex` — self-contained statement and proof.
- `check.py` — exact `Fraction` arithmetic check of the finite recursion at `p=3/4`, including the physical branch and curvature.
- `check.out` — archived PASS output.

## Independent audits

Two distinct OTHER-track full-proof audits are recorded:

- `R08-AUDIT-R09-TANG-Q411-PERIODIC-01 = PASS`, in `runs/R08/20260916T1828Z_i0082_strictstable_firstvariation_c84d2e.md`.
- `P26-AUDIT-R09-TANG-Q411-PERIODIC-ENDTOEND-09 = PASS_FULL_MATHEMATICAL_PROOF / PERIODIC_CLAUSE_REFUTED / TRANSITIVE_CLAUSE_OPEN / PRIOR_ART_UNVERIFIED`, in `proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_02-58-08__run-report.md`.

## Prior-art status

A bounded current-literature search through 17 September 2026 checked the exact Tang title/question wording, periodic-tree concavity, Tang's later work, and citing/current percolation literature. No later primary source explicitly resolving this exact periodic-tree concavity clause was found. This negative search is **not** a novelty certificate. The branching-process calculation and finite-stem mechanism are elementary/classical in character; publication novelty of this specific counterexample remains unverified.

## Status

**Periodic-tree clause: REFUTED / proof complete / exact finite check PASS / 2 independent audits PASS.**

**Transitive-graph clause: OPEN in this package.**

No public posting is asserted by this folder.
