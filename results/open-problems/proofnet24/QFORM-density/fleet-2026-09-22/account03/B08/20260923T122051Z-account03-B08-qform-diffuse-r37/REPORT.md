SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T12:20:51Z.
attacking: the leakage-stable low-rank survivor — pay physical hub stars transverse to a diffuse child subspace by mixed Fresnel, and route failure to a genuinely localized coordinate or an aligned low-rank packet.

# account03/B08 r37 — transverse multi-hub mixed-Fresnel compiler and a target-valid anisotropic diffuse-arm family

Programme: `QFORM-DENSITY-3EIG-20260922`. Owner control revision: `2026-09-22.15`. Run: `20260923T122051Z-account03-B08-qform-diffuse-r37`. Status: `NEW SUPPORTING FULL-CONDITIONAL RECEIVER + TARGET-VALID DIFFUSE FAMILY / FULL TARGET OPEN`. Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. Everything below stays in ORIGINAL independent coordinates and assumes only one-dimensional density caps `0<=f_i<=1`. No Gaussian, moment, compact-support, connected-support, log-concavity, iid, post-rotation independence, arbitrary-joint coarea, law-uniform pointwise quadratic-phase decay, fiber-supremum, or pre/post-Schur currency transfer is used. The new receiver proves a continuous `C_0` density on its stated branch. It does not by itself absorb arbitrary non-diagonal same-bank curvature on the retained light bank; that is recorded as the remaining interface rather than silently discarded.

## 1. Source-valid inputs


The analytic input actually used is the completed mixed-Fresnel theorem in `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, path `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. Split original coordinates into heavy coordinates `H` and light coordinates `L`. Suppose

`A_LL = D + S Lambda S^T`,

where `D` is arbitrary diagonal, `S` has orthonormal columns, and `Lambda=diag(lambda_1,...,lambda_r)` is nonsingular. Put `C=A_LH`, row `s(l)=S_(l,*)`, `w_l=(C_(l,*),s(l))`, and

`Gamma=sum_l w_l w_l^T=[[C^T C,C^T S],[S^T C,I_r]].`

If `Gamma` is invertible and `max_l w_l^T Gamma^(-1)w_l<=1/2`, then, with no condition on `A_HH`, `D`, affine terms, or constants,

`|phi_Q(t)| <= (4pi)^(|H|+r/2) 2^(-|H|) |t|^(-|H|-r/2) prod_k |lambda_k|^(-1/2) det(Gamma)^(-1/2).`  (1.1)

The immediate B08 predecessor is `yspennstate/math-open-problems@3c4c6882813d9530dc5c3884ce3e25f5993c7062`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T115108Z-account03-B08-qform-diffuse-r36/REPORT.md`. It paid the physical-pair branch whenever exact post-pair Schur completion leaves aggregate `E_2`, and showed that rank-two pair-Schur leakage cannot erase fourth-singular-tail mass. Its remaining obstruction was leakage-stable low-rank grouped smoothing.

The designated partner is completed at `yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T091414Z-account04-B08-QFORM-r1/REPORT.md`. It proves the maximally anisotropic original-coordinate family

`Q_R=X_0^2+2R U_1V_1+2R^(-1)U_2V_2`, `R>=3`,

satisfies `||p_(Q_R)||_infinity<7.251` for every admissible product law. Continuity is not asserted in that grouped endpoint.

## 2. Exact transverse Gram reduction

Let `h=|H|>=1`. Define `P_S=SS^T`,

`C_parallel=P_S C`, `C_perp=(I-P_S)C`.

Assume `C_perp` has full column rank `h`, put

`G=C_perp^T C_perp>0`, `U=C_perp G^(-1/2)`.

Then `U` has orthonormal columns and `U^T S=0`; hence `F=[U,S]` is an original-coordinate `(h+r)`-frame with orthonormal columns.

### Lemma 2.1 — exact mixed-Fresnel leverage identity

For every physical light coordinate `l`,

`boxed: w_l^T Gamma^(-1)w_l = ||U_(l,*)||_2^2 + ||S_(l,*)||_2^2`,  (2.1)

and

`boxed: det Gamma = det G`.                                      (2.2)

**Proof.** Write `A=S^T C`, so `C_perp=C-SA`. Apply the invertible block shear

`T=[[I_h,0],[-A,I_r]].`

For every row, `(C_l,s(l))T=(Cperp_l,s(l))`, while

`T^T Gamma T=diag(Cperp^T Cperp,I_r)=diag(G,I_r)`

because `S^T Cperp=0`. Since `det T=1`, (2.2) follows. The quadratic leverage is invariant under the same invertible parameter change, giving

`w_l^T Gamma^(-1)w_l=Cperp_l G^(-1)Cperp_l^T+||s(l)||^2=||U_l||^2+||s(l)||^2`.

QED.

Thus the relevant diffuseness is exactly the row leverage of the augmented physical frame `[Cperp G^(-1/2),S]`, not a heuristic angle condition.

## 3. Main theorem: transverse multi-hub mixed-Fresnel payment

Put `d=2h+r`.

### Theorem 3.1 — `QFORM-MULTIHUB-TRANSVERSE-FRESNEL-v1`

Assume:

1. `rank(Cperp)=h`;
2. `d=2h+r>2`;
3. `max_l (||U_l||^2+||S_l||^2)<=1/2`.

Then the full quadratic form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity <= C_(h,r) [ det(Cperp^T Cperp) prod_(k=1)^r |lambda_k| ]^(-1/d),`

where

`boxed: C_(h,r)=4d/(d-2) * 2^(-2h/d).`                           (3.1)

The statement allows arbitrary `A_HH`, arbitrary light diagonal `D`, arbitrary affine/constant terms, and also arbitrary coordinates outside `H union L`: condition those outside ORIGINAL coordinates. Their couplings only change affine/constant terms in the retained principal form, and the bound above is uniform in those terms. Thus outside spectrum and outside curvature are retained rather than dropped.

**Proof.** Lemma 2.1 makes the leverage hypothesis exactly the source mixed-Fresnel condition and gives `det Gamma=det(Cperp^T Cperp)`. Set

`a=h+r/2=d/2>1`,

`B=(4pi)^a 2^(-h) [det(Cperp^T Cperp) prod|lambda_k|]^(-1/2).`

The source theorem gives

`|phi_Q(t)|<=min(1,B|t|^(-a)).`

At the optimal split `T=B^(1/a)`,

`int_R min(1,B|t|^(-a))dt = 2a/(a-1) B^(1/a).`

Fourier inversion yields

`||p_Q||_infinity <= a/[pi(a-1)] B^(1/a).`

Since

`B^(1/a)=4pi 2^(-h/a) [det(Cperp^T Cperp)prod|lambda_k|]^(-1/(2a))`,

and `h/a=2h/d`, `2a=d`, this is exactly (3.1). The envelope is integrable, so Fourier inversion also gives a continuous density vanishing at infinity. QED.

The constants specialize to

`C_(1,1)=3*4^(2/3)=7.559526299369239...`,
`C_(1,2)=4sqrt(2)=5.656854249492381...`,
`C_(2,0)=4`,
`C_(3,0)=3`.

## 4. Quantitative diffuse/localized/aligned router

Let `L0>0` be the target scale. If

`sqrt(det(Cperp^T Cperp)) >= rho^h L0^h`

and, when `r>0`,

`prod_k |lambda_k| >= c^r L0^r`,

then the diffuse branch gives

`boxed:
 ||p_Q||_infinity <= C_(h,r) rho^(-2h/d)c^(-r/d) L0^(-1).`       (4.1)

If the augmented leverage gate fails, some actual physical light coordinate `l` obeys

`||U_l||^2+||S_l||^2>1/2`,

so at least one of

`boxed: ||U_l||^2>1/4` or `boxed: ||S_l||^2>1/4`                 (4.2)

holds. This is a genuine localized ORIGINAL coordinate: it carries more than one quarter of the normalized transverse hub-coupling subspace or more than one quarter of the child spectral frame.

If instead `Cperp` loses rank, there is `z!=0` with `Cperp z=0`, hence `Cz in range(S)`: a nonzero physical-hub combination is exactly aligned with the child span. Quantitatively small `det(Cperp^T Cperp)` is the corresponding low transverse-volume survivor. No reciprocal local minor is selected.

Thus:

`transverse volume + diffuse augmented frame -> continuous Linfinity payment;`
`high augmented leverage -> localized physical coordinate;`
`small transverse volume -> aligned low-rank grouped survivor.`

This complements r36's high-singular-tail theorem: r36 pays far curvature that legitimate rank-two Schur leakage cannot hide; Theorem 3.1 pays a genuinely low-rank mixed hub/child state **before any Schur division**.

## 5. One-hub special case

For one physical hub and one child direction, write `S=s`, `||s||=1`, `g=C`,

`c=<g,s>`, `hvec=g-cs`, `tau=||hvec||`.

Then `det Gamma=tau^2` and

`w_l^T Gamma^(-1)w_l=s_l^2+hvec_l^2/tau^2`.

If the maximum is at most `1/2`,

`boxed:
 ||p_Q||_infinity <=3*4^(2/3)|lambda|^(-1/3)tau^(-2/3)
 <7.56 |lambda|^(-1/3)tau^(-2/3).`                              (5.1)

If the gate fails, some original coordinate satisfies `|s_l|>1/2` or `|hvec_l|>tau/2`.

## 6. Two-hub / no-child corollary

Take `h=2,r=0`. Let `C` be the physical light-by-two coupling matrix, rank two, and `G=C^T C`. If

`max_l C_l G^(-1)C_l^T<=1/2`,

then

`boxed:
 ||p_Q||_infinity <=4 det(C^T C)^(-1/4)
 =4 [sigma_1(C)sigma_2(C)]^(-1/2),`                              (6.1)

with a continuous `C_0` density. The heavy-heavy `2x2` block is arbitrary and the light-light block may be any diagonal matrix. The estimate is anisotropy-blind: only the product of the two cross singular values appears.

## 7. Target-valid anisotropic diffuse-arm family

Fix `m>=2`, `R>=3`, `L0>0`, and independent cap-one variables. Define

`Q_(m,R,L0)
 =L0 X_0^2
 +(2L0 R/sqrt(m)) U_1 sum_(j=1)^m V_(1j)
 +(2L0/(R sqrt(m))) U_2 sum_(j=1)^m V_(2j).`                    (7.1)

The two coupling columns have disjoint supports and norms

`sigma_1=L0R`, `sigma_2=L0/R`,

so `det(C^T C)=L0^4`. Every light coordinate has normalized projection leverage exactly `1/m<=1/2`. Hence the arm part has a continuous density with

`||p_arm||_infinity<=4/L0`.

The independent square `L0X_0^2` is convolved with that law and cannot increase the sup norm; convolution by a probability measure preserves the `C_0` property. Therefore

`boxed:
 ||p_(Q_(m,R,L0))||_infinity<=4/L0,
 p_(Q_(m,R,L0)) in C_0(R),
 m>=2,R>=3.`                                                     (7.2)

The matrix spectrum is

`{L0,+L0R,-L0R,+L0/R,-L0/R,0,...,0}`,

so `L0,+L0R,-L0R` are three eigenvalues of modulus at least `L0`. This is a genuine scaled target instance, uniform in dimension `2m+3`, anisotropy `R^2`, and every admissible product law. No probabilistic rotation occurs; the singular values are only a deterministic spectral calculation of the coefficient matrix.

## 8. Designated partner applied to the missing m=1 endpoint

At `m=1`, (7.1) is exactly the scaled designated-partner family

`Q_(1,R,L0)=L0X_0^2+2L0R U_1V_11+2L0R^(-1)U_2V_21.`            (8.1)

The new diffuse theorem intentionally does not apply: the two light-coordinate leverages are both one, although `det(C^T C)=L0^4`. Applying the completed `account04/B08` theorem and exact density scaling gives the actual inequality

`boxed: ||p_(Q_(1,R,L0))||_infinity<7.251/L0, R>=3.`             (8.2)

Thus one concrete anisotropic family is now covered at both endpoints:

* `m=1` (maximally localized arms): `<7.251/L0` by the designated partner;
* `m>=2` (diffuse arms): `<=4/L0`, with continuity, by Theorem 3.1.

Fixed transverse second-volume and unbounded anisotropy are therefore not themselves the obstruction. What remains is the interaction of partially localized/aligned low-rank arms with arbitrary non-diagonal same-bank leakage.

## 9. Remaining debt

The unrestricted conjecture remains OPEN and global continuity remains OPEN. Theorem 3.1 is a full-conditional receiver: arbitrary heavy-heavy curvature, arbitrary light diagonal curvature, all affine terms, and arbitrary outside coordinates/couplings/spectrum are retained. It does **not** absorb an arbitrary non-diagonal extra matrix inside the retained light-light block. Such a term cannot be discarded as a small perturbation because high Fourier frequencies can amplify its phase.

The sharpened next debt is:

`QFORM-ALIGNED-OR-LOCALIZED-MULTIHUB-LEAKAGE-RECEIVER-v1` — OPEN.

Starting from the high-leverage/low-cross-rank survivors, either show that a retained low-rank light principal block can be brought into Theorem 3.1's `diagonal + child-frame` form by ORIGINAL-coordinate conditioning without losing target currency, or consume the aligned state `Cperp` small/rank-deficient and high-augmented-leverage state by the existing localized/grouped machinery while retaining arbitrary same-bank leakage.

## 10. Checks and provenance

`CHECKS.py` and `CHECKS.txt` verify the constants above, the exact shear/leverage identity on seeded random frames, `det(C^T C)=L0^4` and row leverage `1/m` in (7.1), and the partner grouped constant `7.250055108887958...`. These are arithmetic regression checks only.

Repository retrieval and native learned-memory ingestion remain separate. No authenticated native receiver use occurred, so execution remains `WITHOUT_VERIFIED_BRAIN` / `full_brain_connected=false`. Model self-report is GPT-5.6 Sol; configured reasoning level was not exposed and remains `UNKNOWN`; thinking counters are unavailable/null.
