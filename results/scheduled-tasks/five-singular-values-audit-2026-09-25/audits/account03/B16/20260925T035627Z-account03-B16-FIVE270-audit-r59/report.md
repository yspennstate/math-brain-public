# account03/B16 — pass 2 audit: Proposition 6.4 and Section 7

Run: `20260925T035627Z-account03-B16-FIVE270-audit-r59`
Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`
Pinned source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`, `short.tex` blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`, PDF SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`.
Status: `WITHOUT_VERIFIED_BRAIN`.

This begins B16's second whole-manuscript pass after pass 1 covered every physical source line. Following the cyclic lens rotation, I independently reconstructed Proposition 6.4 and Section 7 first, with emphasis on threshold boundaries, pivot/no-pivot exhaustiveness, affine terms, Schur losses, density existence, and final scaling. Audited source lines: 560–647.

## Verdict

No new fatal or local mathematical defect was found in lines 560–647. Proposition 6.4, Propositions 7.1–7.2, the proof of Theorem 1.1, and Remarks 7.3–7.4 reconstruct correctly, subject to the already-recorded local repairs in dependencies (notably C03 for Lemma 5.3). The theorem-level conclusion remains an essentially bounded density; continuity is proved in the no-pivot Fourier branch, not globally.

For Proposition 6.4, the factor 2 in `A-DAD=2C`, compression direction, Weyl bound, duplicated singular-value index `s_(2m-1)(C)=s_m(A_IJ)`, and `E_m` top-product extraction all check. Recomputed
`gamma_1=0.3846763769597...`, `gamma_2=0.2373624642125...`, `gamma_3=0.0900485514653...`.

Section 7's case split is exhaustive at equality boundaries because pivots use `>=` and no-pivot uses strict `<`. The pair-pivot branch conditions only on untouched original coordinates. The diagonal-pivot branch leaves independent original coordinates after removing `X_i`. Affine terms alter only linear/constant pieces under Schur complementation and do not change the residual quadratic matrix.

Key constants independently recompute:
- `sqrt(12)*77 = 266.735824365607... < 267`;
- `16*pi = 50.2654824574367... < 51`;
- indefinite-pair bound `16*(8+4 log2+2 log19)+1/e = 266.951346330334... < 269`.

The scaling `Y=KX`, `Q=(s/K^2) Qtilde` is correct and gives the density factor `K^2/s`.

After deriving the overlap independently, I compared it with the separately executed account03/B17 coverage at
`scheduled_tasks/work/shared/five-singular-values-audit-2026-09-25/audits/account03/B17/20260925T030419Z-account03-B17-fiveSV-audit-r13/coverage.jsonl`.
It agrees on Proposition 6.4, Propositions 7.1–7.2, Theorem 1.1, and Remarks 7.3–7.4; no disagreement was found.

Pass 2 is incomplete. Next: audit the one/two-coordinate endpoint lemmas feeding Section 7 using a rough-law/measurability and boundary-value lens, then continue until a second full 1–675 pass is complete.
