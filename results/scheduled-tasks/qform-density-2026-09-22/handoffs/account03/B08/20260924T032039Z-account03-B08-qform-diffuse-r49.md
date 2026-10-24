# account03/B08 r49 handoff — diffuse deletion loss recycles to rank-four spill

Run: `20260924T032039Z-account03-B08-qform-diffuse-r49`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: supporting theorem/router proved; full QFORM OPEN; global continuity OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Canonical mathematics

Repository: `yspennstate/math-open-problems`  
Commit: `ec4f970f5cdd3f31a8e913474fbee5172fd7b603`  
Path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T032039Z-account03-B08-qform-diffuse-r49/REPORT.md`

Companion files: `CHECKS.py`, `CHECKS.txt`, `CLAIMS.json`, `FINISH.json` in the same immutable run directory.

## New theorem

Let `A=A^T`, `s_3(A)>=L`, let `U` be a top-three absolute-eigenvalue frame, and let `p_i=||U_{i,*}||^2`. For the literal ORIGINAL-coordinate deletion child `C=A[-i,-i]`,

`QFORM-DIFFUSE-DELETION-RANK4-SPILL-v1` proves

` s_3(C) >= (1-p_i)L - s_4(A). `

Hence if `p_i<=mu` and `s_3(C)<theta L`, then

` s_4(A) > (1-mu-theta)L. `

At the live gates `mu=1/48`, `theta=1/64`, child loss forces

` s_4(A)>185L/192. `

This is an exact deterministic spectral statement; no probability assumptions enter it.

## Designated partner application

The completed account04/B08 theorem `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` is applied to the same child. If `s_3(C)>=L/64` and its `|lambda|>=L/4096` projection has maximum physical leverage at most `1/32`, then

` ||p_Q||_infinity<4096/L `

and the density is continuous `C_0`.

If that child window is localized instead, the parent inherits an original-coordinate scalar/star witness `>L/32768`.

If the child instead loses its third direction, the new theorem gives a fourth parent eigenvalue `>185L/192`. Applying the reviewed global ridge-window theorem at scale `(185/192)L` gives either

` ||p_Q||_infinity<65.658/L, p_Q in C_0, `

or an ORIGINAL parent coordinate `k` with

` max{|A_kk|, ||A[k,-k]||_2} > 185L/98304 = 0.0018819173...L. `

Thus in the diffuse-selected-three portion of account03/B08 r48, raw child third-spectral loss is no longer a terminal obstruction; partner failure is converted into an explicit localized physical witness unless already paid.

## Regression

Seeded checker result: `QFORM_B08_R49_RANK4_SPILL_CHECK_PASS`.

- 9,900 dense random symmetric/deletion cases: zero violations of `s_3(C)>=(1-p_i)L-s_4(A)`.
- 9,600 exact-rank-three random-frame deletion cases: zero violations of `s_3(C)>=(1-p_i)L`.

The checks are regression evidence only; the report contains the analytic proof.

## Next implication

`QFORM-WEAK-CARRIER-PLUS-EXPLICIT-LOCALIZED-ROW-COMPILER-v3`: consume the r48 weak-carrier state after this router has replaced child spectral loss by a physical scalar/star witness, preserving arbitrary diagonal twists, signs and all remaining spectrum.

Source refresh before publication: `yspennstate/math-research-brain@32d2893a86cbf54ad2f0bbdb7313752b128d7ba9`, OWNER CONTROL revision `2026-09-22.15`; live corrections reread. No schedule/task state, notification, email, public-release, permission or paid-call setting was changed.
