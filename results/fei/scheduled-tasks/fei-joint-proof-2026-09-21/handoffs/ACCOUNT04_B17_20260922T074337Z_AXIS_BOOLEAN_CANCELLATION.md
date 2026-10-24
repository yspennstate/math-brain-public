# account04/B17 FEI handoff — exact Boolean axis cancellation

Status: `WITHOUT_VERIFIED_BRAIN`; full FEI remains OPEN / NOT PROVED.

Canonical scientific source:
`yspennstate/math-open-problems/proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T074337Z-axis-boolean-cancellation/REPORT.md`, report blob `126a21ac4efc950f9a2dd3df4c018402830eea4d`, creation commit `7c054a11dd972f9b64b0877482a91fedccd58338`.

Named newest compatible B15 input consumed:
`account03/B15/20260922T073015Z-axis-child-slack-kl/REPORT.md`, blob `fdef8360ab00c36a62d83f907a07045d7cb97bb0`, commit `545d4e87b9c946225b4d33ade8bd636c01819678`.

New proved inference: along a one-coordinate bias axis through the uniform point, exact regrouping of the all-gate defect collapses the separately bounded child-defect, branch-potential and branch-entropy motions to `C^dagger s (I_1-I_0)`. For Boolean four-bit restrictions with disagreement `d`, `|I_1-I_0| <= 8 min(d,1-d)`. Using the exact Fourier pair transport and `sum e_A^2=d`, `sum c_A^2=1-d`, the entropy shift is bounded by

`8|r| sqrt(d(1-d)) + 12 r^2 d + h_2(r^2) - (1-zeta) KL_2(rho||w0)`.

For an essential composition-prime five-input parent, `d=k/16` with `1<=k<=15`. The resulting worst linear coefficient is rigorously below `166.508925607`; retaining the KL credit yields the certified live-candidate collar

`|p_k-1/2| <= 2.94e-5`,

with reserve `>1.09915103142e-5 + (1-zeta) KL_2(rho||w0)`. This is 1.47 times the preceding B15 radius `2e-5`. The same refined envelope becomes negative at `2.95e-5`; that is only a proof-envelope boundary, not a Boolean counterexample.

Exact Boolean adversarial stress witness: negative truth-table mask `0xe72b10d4`, pivot fifth bit. It is essential and composition-prime by exhaustive proper-block response-pattern test; `d=15/16`, child influences `3/2` and `2`, so `|I_1-I_0|=1/2=8(1-d)`, and `sum_A |c_A e_A|=15/64`, with squared Cauchy saturation ratio `15/16`. Thus the hard lattice corner is physically Boolean and prime.

Checker source SHA-256 `cc083ee6d0c818d13409ce10df5bb6018195e892dd74031c3e23199b2fd5fd01`; captured PASS output SHA-256 `7e896075d629a9a1d800b446553a08f28332915a2ade1a1b92b0468a17fe4ccd`.

Next sharp step: spend the preserved KL credit or replace the global `|Gamma'|<85` payment by a source-certified local slope/shape estimate. Do not treat the `2.95e-5` envelope failure as a gate falsifier.
