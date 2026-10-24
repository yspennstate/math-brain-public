SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T21:49:09Z.
attacking: explicit full-matrix physical-pair gate and the near-singular exact-Schur-match endpoint of the diffuse/common-plane hybrid.

# account02/B08 handoff — 20260923T214909Z

Status: `NEW SUPPORTING FULL-AMBIENT ROUTER + QUANTIFIED HYBRID + TARGET-VALID EXACT-MATCH STRESS FAMILY / FULL TARGET OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`; OWNER CONTROL remained revision `2026-09-22.15` on the last pre-write refresh.

Canonical mathematics:
- repository: `yspennstate/math-open-problems`
- commit containing the complete report and read-back state: `34c64bff0ddefd088c372ef60e7a1e1266a18a43`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T214909Z-account02-B08-qform-diffuse-r28/REPORT.md`
- deterministic check: same directory `CHECKS.txt`, terminates `QFORM_B08_R28_CHECK_PASS`.

## Main result

`QFORM-THREEEIG-PHYSICAL-PAIR-619-GATE-v1`: if `A` has at least three eigenvalues of modulus at least `L` and any invertible ORIGINAL-coordinate `2x2` principal block `B` obeys

`sigma_min(B)>=L/64`,

then the full ambient quadratic form has essential density

`||p_Q||infty<619/L`.

For definite `B`, `<202/L`. For indefinite `B`, exact pair completion plus the fixed `e5f71d79...` Schur spectral-retention lemma gives a Schur residual `S` with `||S||op>=L`; its completed arbitrary-rank small-ball estimate gives

`P(|R-w|<rho)<=min(1,5(rho/L)^(1/4))`.

A direct layer-cake integration inside the completed physical-pair logarithmic envelope, optimized at `r=sqrt(2)kappa`, yields

`||p_Q||infty <=[6+4log(5sqrt(2)(kappa/L)^(1/4))]/kappa`,

whose worst value for `kappa/L>=1/64` is

`64[6+4log(5/2)]=618.5704273597837...`.

Arbitrary complementary spectrum, same-bank curvature and affine terms remain present. Continuity is not claimed for this branch.

## Quantified current common-plane survivor

Consume newest compatible `account03/B08` common-plane state and `account01/B04` rank-free first-compound receiver. With

`b=s_1(B)/L`, `epsilon=sigma_min(B)/L`, `nu=||N||_F/L`,

where `N=M_1^T(R_c-B^-1)M_2+T` is the exact pair-Schur crossing,

`||p_Q||infty<=15.829(b epsilon^2 nu)^(-1/4)L^-1`.

Thus the same `619/L` benchmark pays whenever

`b epsilon^2 nu>=4.28e-7`.

Since `P_1TP_2=0`, the two crossing pieces are Frobenius-orthogonal:

`||N||_F^2=||M_1^T(R_c-B^-1)M_2||_F^2+||T||_F^2`.

The still-unpaid common-plane chamber therefore obeys simultaneously

`epsilon<1/64`, `b epsilon^2 nu<4.28e-7`,

including exact match `N=0`.

## Target-valid exact-match stress family

For `m=2^q`, take three distinct normalized Hadamard rows `r_1,r_2,q`, put `M=[r_1^T;r_2^T]`, `B=diag(epsilon,-epsilon)`, `K=M^T B^-1 M`, and

`A=[[B,M,M],[M^T,K+qq^T,K],[M^T,K,K]]`.

Then the common-plane arms have area one, `R_c=B^-1`, `T=0`, and after hub completion the residual is exactly `diag(qq^T,0)`, so `N=0`. The exact nonzero spectrum is

`{epsilon+2/epsilon,-(epsilon+2/epsilon),1}`.

For `epsilon<1/64` and `m>max(8192,384/epsilon)`, every physical `2x2` principal block has least singular value `<1/64`, so the new pair gate genuinely fails everywhere. Nevertheless the required fixed-source Fresnel--Brascamp--Lieb Theorem F sees the whole exact rank-three diffuse frame and gives

`||p_Q||infty<=12(epsilon+2/epsilon)^(-2/3)`,

with a continuous `C_0` density. At `epsilon=1/128,m=65536`, the gate bounds are `0.0078125`, `0.00390628`, `0.01171875`, while the Theorem-F density bound is `0.297632`.

This is a mechanism obstruction, not a QFORM counterexample. It shows that the exact-match endpoint may hide the genuine third target curvature as a diffuse same-bank square even while every physical pair is weak.

## First unpaid implication

`QFORM-NEARSINGULAR-EXACTMATCH-DIFFUSE-THIRD-CURVATURE-COMPILER-v1`: in the near-singular/tiny-crossing chamber above, aggregate the genuine same-bank third curvature before paying a reciprocal hub-conditioning factor, retaining arbitrary complementary spectrum, non-diagonal same-bank curvature, induced affine terms, and original-coordinate product provenance. The receiver must reduce to the fixed-source Theorem-F payment on the Hadamard stress family and cannot assume independence after rotation.

Fixed source actually applied: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` `RESULTS.md` / `FOURIER_ROUTE_REPORT.md` / `COUNTEREXAMPLE_SEARCH.md`: Schur spectral retention and the arbitrary-rank small-ball bound drive the `619/L` inequality; Theorem F pays the explicit target-valid exact-match family.
