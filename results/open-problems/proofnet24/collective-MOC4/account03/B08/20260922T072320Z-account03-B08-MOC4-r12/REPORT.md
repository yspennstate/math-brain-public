# account03/B08 MOC4 — generic-facet exact unitary ladder

Run: `20260922T072320Z-account03-B08-MOC4-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **AUXILIARY_ONLY**; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and assigned adversary role

For every complex normal `4 x 4` pair, after diagonalization the target is

`D(U)=det(D_a+U D_b U*) in conv{v_sigma: sigma in S_4}`,

where

`v_sigma=prod_i(a_i+b_{sigma(i)})`

for every genuine unitary `U`.  A support counterexample therefore requires one real-linear functional `L` for which the same true-unitary determinant satisfies

`L(D(U)) > max_sigma L(v_sigma)`.

This run follows account03/B08's exact assignment: true-unitary / complex-spectrum adversaries checked against all 24 spectral products in one common direction. It uses no arbitrary bistochastic or free compound-minor surrogate.

The assigned OTHER-account partner result consumed and applied is account04/B09 run `20260922T060924Z-b09-moc4-r12`, theorem `MOC4-ROOT-SATURATION-EXCLUSION-v1`: a genuinely support-violating global maximizer must have strict left/right elementary pair gates; saturation would force a flat SU(2) orbit and the exact twirl lift would contradict violation. The current team-lead input also used is account03/B07 run `20260922T064004Z-account03-B07-MOC4-r12`, which sharpens the remaining global-max obstruction to the mixed-Schur boundary `MSQR` versus the all-negative-definite branch `NDI` and supplies `MOC4-KERNEL-QUARTIC-RESERVE-v1` on the singular branch.

## 2. Integrity correction to the previous B08 calibration

The previous B08 report used the spectra

`a=(18-17i,-20+2i,15-22i,-21+2i)`,

`b=(-19+4i,25-5i,18-i,-18+i)`

and support direction

`L_0(z)=-5782 Re(z)+19099 Im(z)`.

Its prose described `1234` as the unique maximizing permutation. Fresh exact `Fraction` arithmetic shows that this uniqueness statement was false: the top face has **exactly two** maximizers,

`1234` and `1342`,

both with value `-61633500`.

The old exact unitary, determinant, positive support gap and three-vertex hull certificate remain valid; only the word **unique** is withdrawn. The old verifier checked the first maximizing index but did not assert uniqueness, which is why this slipped through. This run adds an explicit exact uniqueness test to the verifier.

## 3. Generic common direction: all 24 support values distinct

Keep the same simple spectra but replace the common direction by

`L(z)=-6032 Re(z)+19799 Im(z)`.

Exact enumeration gives 24 pairwise-distinct support values. The unique maximum and minimum are

`M=-63921000` at one-line permutation `1342`,

`m=-62046835110`,

so the full support width is

`M-m=61982914110`.

The runner-up lies exactly `4261400` below the unique maximum. Thus this direction removes the exposed-edge degeneracy rather than hiding behind it.

## 4. Exact true-unitary improvement ladder

Start from the exact rational-complex Cayley unitary `U_0` of B08 r11. For a rational parameter `t`, let `G_rs(t)` be the identity except on coordinates `r,s`, where it equals

`[[ (1-t^2)/(1+t^2), 2t/(1+t^2) ],
 [ -2t/(1+t^2), (1-t^2)/(1+t^2) ]]`.

This is an exact real orthogonal, hence unitary, two-plane gate. Apply the five genuine pair moves

1. left `G_23(73/5000)`,
2. right `G_13(19/1000)`,
3. left `G_23(71/5000)`,
4. left `G_12(-9/1000)`,
5. right `G_13(119/10000)`.

The exact verifier recomputes `D(U)` after every move and proves that **every step strictly raises the same common support functional**. Let the final unitary be `U_*`.

It verifies exactly that

- `U_* U_*^*=I`;
- every one of the 16 entries of `U_*` is nonzero;
- `min_ij |(U_*)_ij|^2 > 1/500`;
- all eigenvalues in each spectrum are distinct;
- all 16 sums `a_i+b_j` are nonzero;
- all 24 spectral products are distinct.

Thus this is a dense genuine-unitary/simple-spectrum stress point, not a support-zero or bistochastic artifact.

## 5. Common-direction gap below four parts in 100,000

For `D_*=D(U_*)`, exact arithmetic gives

`0 < M-L(D_*) < 4261400`,

and more sharply

`(M-L(D_*))/(M-m)`

`= 10239482728813948546658642303339895618268083282313233556945971239221386922961742637415667710`

`  / 268638129308945869089054097119463180272888985230443937772742497635154887853612305909135043983041`

`≈ 3.811626724454325e-05`.

Hence the true-unitary determinant is only about **0.003812% of the full support width inside** the unique exposed support line. This improves the previous B08 calibration by a factor of about `2.821` in normalized gap while simultaneously removing the old top-face tie.

Moreover, the determinant support value lies **above every spectral permutation vertex except the unique maximizer**, because the determinant gap is strictly smaller than the `4261400` runner-up separation. That observation is not a counterexample: convex combinations can of course lie above the second-best vertex in one direction.

## 6. Exact hull rescue

The candidate is rigorously inside the actual target hull. Exact Gaussian-rational elimination produces strictly positive coefficients `lambda_1,lambda_2,lambda_3` summing to one such that

`D_*=lambda_1 v_1234 + lambda_2 v_1342 + lambda_3 v_2314`.

Numerically the three exact rational weights are approximately

`(0.17896921093762108, 0.5336947294992813, 0.2873360595630976)`.

The verifier checks the complex identity exactly, not by floating-point tolerance. Thus this near-facet stress point is definitively **not** an MOC4 counterexample.

## 7. Applying the named partner's strict-pair lesson

A true global support maximizer must be stationary against every genuine elementary pair orbit, and account04/B09's strict-root theorem says a hypothetical support violator cannot sit on the saturation/flat branch.

The present candidate deliberately tests that requirement. A sixth exact genuine unitary move,

left `G_23(89/10000)`,

raises the **same** support functional by a strictly positive exact rational amount while the resulting determinant still remains strictly below `M`. Therefore `U_*` is not pair-stationary and cannot be a global maximizer of this support functional.

This is the useful adversarial conclusion: very small common-direction gaps, even with a unique exposed permutation, dense true unitaries and simple spectra, are cheap to manufacture unless the search enforces the exact elementary-pair stationarity/strictness gates. The partner theorem and the lead's `MSQR/NDI` split therefore belong inside the candidate generator, not as an audit after a tiny gap is found.

## 8. Mechanism change and next exact obligation

This run changes mechanism from the prior static Cayley/pair-envelope calibration to an **exact generic-facet rational pair-gate ladder with an explicit hull rescue and stationarity rejection**. The old face-degenerate calibration is preserved with its corrected interpretation.

Next candidate version: `MOC4-PAIR-STATIONARY-GENERIC-FACET-v1`.

The next adversary search should enforce, before interpreting a support gap:

1. 24 distinct spectral support values and a unique maximizing permutation;
2. exact or rigorously enclosed stationarity for all six left and six right elementary `SU(2)` pair orbits;
3. the account04/B09 strict pair-gate conditions;
4. classification into the lead's `MSQR` or `NDI` branch;
5. only then a rigorous test of `L(D)>M` against all 24 vertices.

If such a candidate has a strict negative target gap `M-L(D)<0`, it is a genuine MOC4 counterexample. If the stationarity constraints force the gap nonnegative, that supplies information directly to the lead's residual proof tree.

## 9. Verification and verdict

`verify_generic_facet_ladder.py` uses only Python standard-library exact rational arithmetic. `VERIFY_OUTPUT.txt` is the captured output of the exact verifier. It checks the corrected two-vertex old face, all 24 distinct new support values, unique new maximum, exact unitarity, entry nonvanishing/density bound, strict five-step support improvement, the exact near-facet gap, exact three-vertex Caratheodory rescue, and the exact sixth support-improving pair move.

Verdict: **AUXILIARY_ONLY / TARGET STILL OPEN.** No proof or disproof of MOC4 is claimed.
