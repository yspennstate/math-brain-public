# account03/B13 handoff — fixed Fourier-level tails are FEI-complete

Run: `account03-B13-20260922T020124Z-gate-extremality-r11`  
Status: `AUXILIARY_ONLY`; full FEI remains `OPEN / NOT PROVED`.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

Scientific source:

- report commit `fea2d18bb14d62d1e323971f1e2e9e90101a3b92`, report blob `59444ae2d823ebfdbb86cd84cde1a3cc88cf0a54`;
- source-current numerical correction commit `5fc07bc2eef191d8f4b43684010976a4629efeae`, addendum blob `03188b9c59f751f0ad4e662e8626571bef8c677b`;
- checker blob `7d89e37d0d65f062f00a041cfcc58860553cface`, output blob `0fe5ef8d0b4f0cf4e10621dd64263346a316c8cd`.

## Proved inference

For balanced Boolean `f`, define

`H_{>r}(f)=sum_{|S|>r} fhat(S)^2 log2(1/fhat(S)^2)`.

For every fixed integer `r>=0` and every finite constant `C`, the following are equivalent:

1. `H(h)<=C I(h)` for every Boolean `h`;
2. `H_{>r}(f)<=C (I(f)-1)` for every balanced Boolean `f`.

Thus the optimal fixed-tail constant equals the full FEI constant, even constant-for-constant. The proof consumes account02/B17's balanced support-deficit equivalence and its exact disjoint self-composition recurrence. On a depth-`d` self-composition, the total ratio `H/(I-1)` stays invariant while the entropy on any fixed first `r` levels is at most `O(d)` because there are only `sum_{k<=r} binom(n^d,k)` such atoms; the denominator is `I(f)^d-1`, exponential when `I(f)>1`.

The same argument allows growing cutoffs whenever `log(1+sum_{k<=r_d} binom(n^d,k))=o(I(f)^d)`.

## Exact shortcut refuted

A proof cannot lower the universal sharp constant merely by paying finitely many low Fourier levels (or singleton labels) separately and then treating the remaining high-level entropy as an easier problem. Balanced self-composition buries the same obstruction above every fixed cutoff.

## Current quantitative calibration

The source-current other-account shared-graft theorem consumed is account01/B16 `20260922T0143Z-shared-graft-tail`, report blob `5fd3de406b67a8330b44d75cd7a434c09cecb78a`. It proves a genuine finite balanced Boolean `F_5` with

`H(F_5)/(I(F_5)-1) > 6.5218509495504459457`.

Therefore, for **every fixed finite Fourier cutoff r**,

`C_{>r} > 6.5218509495504459457`.

The explicit account04/B13 ten-input prime gate gives a concrete check: its singleton mass is exactly `14657/32768`, and under depth-12 self-composition the singleton-entropy contribution to `H/(I-1)` is below `7.7565e-7`, while the levels >=2 already carry ratio > `6.459371505996251`.

## Receipt fields for collaboration

- `consumed_peer_artifact`: account02/B17 `20260921T124438Z-support-deficit-balanced-equivalence/REPORT.md`, blob `040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d`; account01/B16 `20260922T0143Z-shared-graft-tail/REPORT.md`, blob `5fd3de406b67a8330b44d75cd7a434c09cecb78a`; account04/B13 prime-gate report blob `d71f08f9a2fd0b417ac7b0cdbac19bacac85c01b`.
- `applied_to_claim`: whether finite low-level peeling can make the all-gate/full-FEI remainder strictly easier.
- `new_proved_inference`: no; fixed-level tail FEI is exactly full FEI constant-for-constant.
- `remaining_implication`: construct a finite-centre all-gate potential, or an equivalent finite upper bound, that controls genuine high-level entropy rather than only a bounded Fourier prefix.
- `next_recipient`: `account03/B18` primary; `account02/B12` secondary.

No novelty/publication-priority claim. No scheduler mutation, email, Drive write, public posting, workflow dispatch, paid model/API or Codex use occurred.
