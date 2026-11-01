# Hasebe–Ueda–Wang Problem 4.3 — closure package

Status: **source statement REFUTED; ProofNet24 closure gates complete (2/2 OTHER-track end-to-end audits)**.

Outside source: Takahiro Hasebe, Yuki Ueda and Jiun-Chau Wang, *Log-unimodality for free positive multiplicative Brownian motion*, arXiv:2009.13848 (2020 preprint), *Colloquium Mathematicum* 169 (2022), 209–226, Problem 4.3.

## What the source asks

Problem 4.3 asks whether the free positive multiplicative convolution `mu boxtimes nu` must be log-unimodal whenever both inputs are multiplicatively symmetric and log-unimodal on `(0,infinity)`. This is not the paper's already-proved Brownian-factor theorem `sigma_t boxtimes nu` and is not Problem 4.7.

## What is proved here

Take

`mu(dx) = (1/(12x)) 1_[exp(-6),exp(6)](x) dx`.

Then `log_* mu` is uniform on `[-6,6]`, so `mu` is multiplicatively symmetric and log-unimodal. Nevertheless, for `rho=mu boxtimes mu`, the logarithmic density `g` has

`g''(0)>0`.

Thus the symmetry point is a strict local minimum, so `rho` is not log-unimodal. This single explicit admissible pair refutes Problem 4.3 as stated.

The proof in `main.tex` is self-contained at the source-refutation level. It uses the elementary eta/Sigma-transform calculation for the log-uniform law, anchors the physical inverse branch on the negative axis, continues it along the noncritical unit-circle arc, and proves the center curvature sign by explicit inequalities.

## Exact finite certificate

The finite arithmetic was already certified in the canonical track artifact and is deliberately **not duplicated as a new checker** in this paper folder:

- script: `../artifacts/2026-09-16/log_uniform_L6_family_exact_check_v2.py`
- script blob: `255185509491dbde099fca88d4006b5b52725b48`
- output: `../artifacts/2026-09-16/log_uniform_L6_family_exact_check_v2.out`
- output blob: `76fb7f17fda4806985170813f545ee8baf860a6a`

The archived output is `PASS` and verifies exactly the only finite inequalities needed here, including

`(163/60)^6>400`, `(22/7)^2<10`, `1993/401>0`, and

`67712000000/76034875203 < 1`.

This pointer arrangement follows the owner instruction not to archive the same checker again; the canonical script/output are already immutable within this P20 root.

## Independent audits

Two distinct OTHER tracks independently checked the complete source-level refutation.

1. **P26:** `P26-AUDIT-P20-I0081-LOGUNIFORM-FAMILY-03 = PASS` in
   `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_19-58-22__run-report.md`, creation commit `93fa5183bb82a3aa614b5b83f8b5f70d775ff6fb`.
   P26 independently rederived the admissibility, exact eta inverse, physical branch, curvature formula and exact rational core for the full `L>=6` family.

2. **P19:** `P19-AUDIT-P20-I0081-L6-ENDTOEND-18 = PASS (source-level)` in
   `proofnet24/P19-closure-smr-optimal/runs/2026-09-16/2026-09-16T18-58-43Z__run-report.md`, creation commit `93e5007c4bac538855650601b8786d237a49bb63`, report blob `030119d726fa8b5cb8413c8389c0b1301821feff`.
   P19 independently rederived the fixed `L=6` counterexample from the transform definitions through the source-level contradiction.

These audits are independent of P20 self-checks. Stronger P20 results about arbitrarily many or infinitely many modes are not needed for closure and are not claimed to have two outside audits.

## Prior-art status

A dated bounded search on 16 September 2026 checked the original arXiv/journal source, exact Problem 4.3 wording/terminology, author/follow-up searches, and later free-multiplicative regularity/subordination literature. No later source explicitly resolving exact Problem 4.3 or matching this log-uniform counterexample was located in that bounded search. **This is not a publication-grade novelty certificate.** The mathematical source refutation does not depend on a novelty claim.

## Files

- `main.tex` — self-contained proof of the fixed `L=6` source counterexample.
- canonical exact checker/output — referenced above, not redundantly copied.

No Lean file is needed: there is no finite combinatorial core beyond the exact rational inequalities already certified by the Python artifact.
