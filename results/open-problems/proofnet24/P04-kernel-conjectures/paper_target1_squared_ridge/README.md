# P04/P21 Target 1 — restricted two-view squared-ridge closure package

Date: 2026-09-16
Repository: `yspennstate/math-open-problems`, branch `master`
Category: PERSONAL FINISHING (owner's 2026 kernel note / kernel paper 9). This is not an external-source assignment.

## Exact proved scope

This folder packages only the restricted Target-1 theorem authorized by the 2026-09-16 fleet instructions:

- exactly two augmentations per original sample;
- fixed augmentation strength `Delta>0` and fixed ridge `lambda>0`;
- smooth bounded odd activation with the derivative bounds used in the proof, with `tanh` canonical;
- iid Gaussian feature entries of variance `1/d`;
- `n/d -> alpha>0`, `m/d -> beta>0`;
- unit-norm linear teacher;
- whole-original-sample block replacement preserving the shared latent dependence of both augmentations;
- optimized squared-ridge objective equivalence to the matched correlated Gaussian surrogate, total error `O(d^-1/2)`;
- a separate clean prediction-risk comparison against a jointly matched clean-test surrogate, leading transfer `O(d^-1/2)` (and `O(M^-1/2)` additional sampling error for an iid clean test block of size `M`).

The exact loss normalization is `N=2n` and coefficient `1/(2N)=1/(4n)` per augmented row. The exact rank-two restored-block identity is

`L_i^* - L_-^* = (1/(2N)) e^T (I_2+Q)^(-1)e`.

An unscaled current-block mismatch `K/sqrt(d)` therefore costs `K/(2N sqrt(d))` per original sample, and `n=N/2` replacements total exactly `K/(4 sqrt(d))` at first order.

No claim is made here for ReLU, nonlinear teachers, vanishing ridge, arbitrary augmentation counts, per-view replacement, or independence of the actual plus/minus channels. Targets 2-4 and all broader kernel conjectures are outside this package.

## Files

- `target1_squared_ridge.tex` — self-contained theorem statement and analytic proof, including normalization, rank-two Woodbury completion, finite-feature Hermite/Schur factorization, dimension bookkeeping, dependence-aware leverage freezing, total training telescope, and the separate clean-test telescope.
- `target1_symbolic_checker.py` — exact symbolic finite-core checker; no floating-point decisions.
- `target1_symbolic_checker.out` — archived executed output, `EXACT_SYMBOLIC_CHECK=PASS`.

No Lean file is included because the finite core is the symbolic 2x2 matrix/rational normalization identity rather than a finite combinatorial enumeration. The theorem-sized asymptotic argument is written on the page in `target1_squared_ridge.tex`.

## Primary source and prior art checked

The motivating source is Oussama Dhifallah and Yue M. Lu, *On the Inherent Regularization Effects of Noise Injection During Training*, PMLR 139 (ICML 2021). Its equation (3) has coefficient `1/(2 n ell)`; at `ell=2` this is exactly `1/(4n)=1/(2N)`. Its correlated Gaussian surrogate shares original-sample latent terms across augmentation index `j`, and the paper explicitly describes the correlated Gaussian equivalence as a conjectural ingredient.

Hong Hu and Yue M. Lu, *Universality Laws for High-Dimensional Learning with Random Features*, arXiv:2009.07669, is the rigorous architectural precedent for leave-one-out/Lindeberg/Stein random-feature universality, but does not justify splitting two views that share an original latent.

A bounded current literature check dated 2026-09-16 also found Lucas Morisset, Alain Durmus and Adrien Hardy, *Characterizing the Generalization Error of Random Feature Regression with Arbitrary Data-Augmentation*, arXiv:2605.10290 (submitted 2026-05-11). It gives proportional-regime generalization characterizations for arbitrary augmentation through population augmentation statistics. The bounded check did not locate an exact theorem subsuming this finite empirical two-draw, shared-latent replacement statement. This package therefore retains the label `PROVED`, not `KNOWN`.

## Independent OTHER-task audits

Both frozen required outside audits are now complete.

1. `P26-AUDIT-P04-T1-ENDTOEND-17 = PASS`
   - report: `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_04-37-56__run-report.md`
   - creation commit: `7127886502112192812294d55ed05862dc057b8b`
   - report blob: `7eb36f5261274ccd7a392d363b4d001258e858c3`
   - independently rederived the source normalization, two-row Woodbury identity, shared-latent replacement unit, dimension/moment estimates, total telescope, and separate clean-test transfer.

2. `P03-AUDIT-P04-T1-ENDTOEND-193 = PASS`
   - report: `proofnet24/P03-fei/runs/2026-09-16/2026-09-16_15-27-05__run-report.md`
   - creation commit: `4dbcb14d1b71aa3470a21ecdd278137f82255b47`
   - report blob: `d4e8712e460b2686e2380c207ca6f00ce0ebbdc8`
   - independently checked the frozen P04/P21 package and primary source, including dependence-aware leverage freezing, Hermite/Stein dimension count, feature-coordinate fourth moments, exact total `K/(4 sqrt(d))` normalization, and the separate clean-risk theorem.

Neither auditor reported a repair debt. P04/P21 self-checks are not counted as these outside audits.

## Closure status

Frozen audit metric: `required claim-scoped OTHER-audit obligations unresolved = 1 -> 0`.

The mathematical package is `PROVED / AUDIT-COMPLETE` under the current fleet closure rule: full theorem proof on page, exact finite-core certificate executed and archived, dated prior-art check recorded, and two distinct OTHER-track end-to-end PASS audits. Packaging and the retirement/handoff are recorded in the corresponding immutable P04 run report.

This folder is the narrow closure deliverable for the owner's personal exception. It is not a new kernel research programme and does not reopen already excluded or retired kernel targets.
