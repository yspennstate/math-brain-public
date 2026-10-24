# account03/B13 repeated line audit r19

Run ID: `20260925T053340Z-account03-B13-lineaudit-r19`

Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`

Pinned source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`,
`proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/short/short.tex`
(blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`) and exact 14-page PDF
(blob `8be3aae36ecad7a9dc9b7c95978aad09499f32d0`, SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`).

## Fresh controls

Fresh main controls were re-read at invocation: AGENTS, CURRENT_OBJECTIVE, README, ORDER, MANIFEST, CORRECTIONS, ASSIGNMENTS. Exclusive audit-only objective unchanged.

## B13 reconstruction

Lemma 5.2: statement survives C01. Literal line 412 half-open polar chart global-diffeomorphism wording is FALSE; deleting one null ray gives a genuine chart, the critical point is null, the absolute Jacobian is 1/(2 sqrt(det B)), and the pi L/sqrt(det B) bound follows. q -> -q handles negative definiteness.

Lemma 5.3: off-critical calculation PASS. Hyperbola chart is branchwise bijective; absolute Jacobian is 1/(2 sqrt D); density factors stay in original coordinates; positive and negative tails use separately selected physical coordinates i and i'; monotonicity, half-line rearrangement, cutoffs, middle interval, (15/2)log2<6, and AGM all PASS. Literal proof retains C03 GAP at z=v; proposed repair PASS because the critical level is two affine lines and hence null under the joint density.

## New regression: affine/unbounded conditioning uniformity

Condition outside a physical pair H. With pair block B and cross block C, ell(y)=2Cy+beta, w0(y)=-(1/2)B^{-1}ell(y), and

v(y)=y^T D0 y+b_R^T y+c-(1/4)ell(y)^T B^{-1}ell(y).

The quadratic matrix of v is exactly D0-C^T B^{-1}C, the pair Schur complement. This identity was reproduced symbolically.

For each y, w0(y) is only a deterministic shift of the two original coordinates. Separate translations preserve independence and the cap-one marginals regardless of how large y or w0(y) is. Lemma 5.3 is uniform in w0(y); affine data enter only through the output shift v(y). Thus no hidden support, moment, or bounded-affine-term assumption is used in the final pair-pivot branch.

g(z,y)=D^{-1/2}[6+log_+(16 sqrt(D)/|z-v(y)|)] is extended-Borel measurable. After C03, conditional density domination implies Borel-set domination for every conditioning value, and Lemma 2.4/Tonelli does not require a common exceptional z-null set.

## Separate worker comparison

Only after the independent reconstruction, real peer evidence was read from account02/B04 run `20260925T031726Z-account02-B04-five-short-audit-r35`, coverage blob `6a75413ca13305784093466a0439c7bc66e0787c`. It independently records line 412 FALSE/C01, line 441 GAP/C03, and the intermediate hyperbola-tail lines PASS. No disagreement found.

## Remaining obligations

C07 remains UNCHECKED: fresh search did not establish the exact negative current-status claim that the three-large-eigenvalue question is open. Safe source-internal wording remains PASS.

Exact private PDF blob was re-fetched through authenticated GitHub and matches the manifest blob. Direct web PDF fetch was disabled, so no screenshot/render equivalence is claimed.

Complete whole-manuscript passes for this worker remain 0. Recurring audit continues.
