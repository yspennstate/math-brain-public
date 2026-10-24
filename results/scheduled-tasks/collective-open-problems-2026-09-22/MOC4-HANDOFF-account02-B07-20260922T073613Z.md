# MOC4 source-bound handoff — account02/B07 — full-Hessian LS cross-reserve

Run `20260922T073613Z-b07-2e219625`. Outcome **ESSENTIAL_STEP_APPLIED**; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**. Execution `WITHOUT_VERIFIED_BRAIN`.

Canonical science: `proofnet24/collective-MOC4/account02/B07/20260922T073613Z-b07-2e219625/REPORT.md`. Exact verifier: sibling `VERIFY_FULL_LS.py`; captured exact output: sibling `VERIFY_OUTPUT.txt`.

Inputs consumed: campaign lead account03/B07 `MOC4-KERNEL-QUARTIC-RESERVE-v1` (run `20260922T064004Z-account03-B07-MOC4-r12`); named partner account03/B08 `MOC4-GENERIC-FACET-LADDER-v1` (run `20260922T072320Z-account03-B08-MOC4-r12`); and directly applied OTHER-account result account03/B20 `MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1` (run `20260922T071802Z-account03-B20-MOC4-r12`), which proves same-pair trust gates add nothing beyond same-pair LS on `MSQR` and identifies cross-split/full-Hessian coupling as the missing mechanism.

New theorem **`MOC4-MIXED-SCHUR-FULL-LS-CROSS-RESERVE-v1`**: for a local maximum with full negative Hessian

`A=[[P,B],[B^T,C]] >= 0`

and a pair-block kernel vector `z` (`Pz=0`), set `S_c=C-B^TP^+B`, `ell=D^3F[z,z,.]=(u,v)`, `q=D^4F[z,z,z,z]`, and

`r=v-B^TP^+u`.

Then `ell in range A`, `r in range S_c`, and the exact block energy identity is

`ell^T A^+ell = u^TP^+u + r^TS_c^+r`.

The curved path `x(t)=tz+t^2y` therefore gives the full necessary gate

`q+3u^TP^+u+3r^TS_c^+r <= 0`.

If `Delta=-(q+3u^TP^+u)` is the lead's same-pair LS slack, then

`r^TS_c^+r <= Delta/3`.

Hence exact pair-LS saturation forces the new cross-split compatibility

`r=0`, i.e. `v=B^TP^+u`.

For the genuine 12-real-dimensional row-root tangent space, take `S` to be one four-dimensional complementary-pair Spin(4) block and `W` the other four root planes. Their exact pair gaps satisfy negative-Hessian diagonal blocks `2g_sigma I_2`, so

`lambda_max(S_c) <= 4 sum_{sigma in W}g_sigma`.

Thus

`||r||^2 <= (4 Delta/3) sum_W g_sigma`

and, using B07's exact pair-roof identity `g_sigma=2(gamma+rho_sigma)`,

`||r||^2 <= (8 Delta/3) sum_W(gamma+rho_sigma)`.

The argument is inverse-free and remains valid when `det(A+B)=0`. Repeated spectra remain closed by the preceding B07 pair-symmetrized common-lift theorem.

Exact calibration shows this is strictly stronger than pair-only LS: an exact PSD block jet has pair gate `-11/10 <=0` but full gate `73079/7700>0`, with cross reserve `27183/7700`.

First unpaid implication: **`MOC4-CROSS-SPLIT-CUBIC-PAYMENT-v1`**. On a zero-free simple-spectrum positive-gap true-unitary global maximizer in `MSQR`, use structured determinant/same-unitary identities, the other pair-root certificates, subgroup roofs and spectral conditioning to force `r^TS_c^+r>Delta/3` unless `gamma<=0`. At `Delta=0`, it suffices to show `r=0` plus the remaining strict pair structure forces the zero-face branch or contradiction. This is the cross-split mechanism explicitly left open by account03/B20; do not spend another pass re-optimizing the already-collapsed same singular pair orbit.
