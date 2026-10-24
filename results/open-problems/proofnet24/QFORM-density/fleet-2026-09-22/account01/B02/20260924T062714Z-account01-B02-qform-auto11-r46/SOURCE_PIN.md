# Source pins — account01/B02 r46

Run: `20260924T062714Z-account01-B02-qform-auto11-r46`

## Owner/control sources

- `yspennstate/math-research-brain`, branch `main`, startup head observed: `344c0eacd2eb32d9110b0035541dbda9c989e290`.
- OWNER CONTROL revision: `2026-09-22.15`.
- Programme: `QFORM-DENSITY-3EIG-20260922`.
- Assignment: `scheduled_tasks/work/shared/qform-density-2026-09-22/assignments/account01/B02.json`.

## Mathematical sources actually used

1. Immediate account01/B02 predecessor:
   - `yspennstate/math-open-problems@acf321dcae5b20ea42cf55f84ced68433498a9f5`
   - `proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260924T052052Z-account01-B02-qform-auto11-r45/REPORT.md`
   - used for the live full-cut inequalities `x1*x2>247/576` and `E2(N_(-i))>247/2304`, plus the `1/222` hub normalization.

2. Row-gate-free E2 source strengthened in this run:
   - `yspennstate/math-open-problems@cd0be625c8f7143a46ad14bb936e9c24bfb19a8d`
   - `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260923T192839Z-auto11/REPORT.md`
   - the proof's three exhaustive cases retain the pointwise full-characteristic-function envelopes reproduced in Section 2 of this run's `REPORT.md`.

3. Newest completed designated account02/B02 partner actually applied:
   - `yspennstate/math-open-problems@19a3d60ceb5d0989aa527b32d3e76f388b9419f6`
   - `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260924T060210Z-account02-B02-QFORM-auto12/REPORT.md`
   - theorem used: `QFORM-RANK2-ONEBANK-LINEAR-DENSITY-v1`;
   - actual inequality applied: `s1*s2=sqrt(x1*x2)>sqrt(247/576)`, yielding `||p_Q||_infinity<4.380627393` on the one-sided-twist branch.

## Corrections retained

- no law-uniform pointwise scalar quadratic-phase decay;
- no post-rotation independence;
- no arbitrary-joint coarea density bound;
- no fiber-sup dimension-free integration;
- no deletion of coefficient-small quadratic terms for rough laws;
- finite E2 / half-Riesz credit alone does not imply `L^infinity` density;
- all finite `L^r` norms are not silently promoted to `L^infinity`.

Full QFORM remains OPEN. Target-wide universal unweighted Fourier `L1` remains OPEN_NOT_REFUTED.
