SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T12:20:51Z.
attacking: leakage-stable low-rank diffuse hubs via mixed Fresnel.

# B08 r37 handoff

Full target remains OPEN. Source mathematics is immutable at:

`yspennstate/math-open-problems@58b2a0752f409dd48ae5e39851ac84f13be4470b`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T122051Z-account03-B08-qform-diffuse-r37/REPORT.md`

Main result: `QFORM-MULTIHUB-TRANSVERSE-FRESNEL-v1`. For actual physical heavy coordinates H (`h=|H|`) and light coordinates L with

`A_LL=D+S Lambda S^T`, `S^T S=I_r`,

let `C=A_LH`, `C_perp=(I-SS^T)C`, `G=C_perp^T C_perp`, `U=C_perp G^(-1/2)`, and `d=2h+r>2`. If `rank C_perp=h` and

`max_l (||U_l||^2+||S_l||^2)<=1/2`,

then the full conditional quadratic form has a continuous `C_0` density and

`||p_Q||_infinity <= [4d/(d-2)] 2^(-2h/d) [det(G) prod_k |lambda_k|]^(-1/d).`

The exact identity behind the gate is

`w_l^T Gamma^(-1)w_l=||U_l||^2+||S_l||^2`, `det Gamma=det G`,

obtained by the block shear `(C_l,S_l)->(Cperp_l,S_l)`. Failure of the leverage gate gives an actual localized light coordinate with either transverse-hub leverage `>1/4` or child-frame leverage `>1/4`; loss of rank of `Cperp` is exact hub/child alignment. This is an aggregate-before-inversion router.

Concrete two-hub corollary (`h=2,r=0`): if `max_l C_l(C^TC)^(-1)C_l^T<=1/2`,

`||p_Q||_infinity <= 4 det(C^TC)^(-1/4) = 4[sigma_1(C)sigma_2(C)]^(-1/2)`, continuously.

Target-valid anisotropic family: for `m>=2,R>=3,L>0`,

`Q=L X0^2 +(2LR/sqrt(m))U1 sum_j V1j +(2L/(R sqrt(m)))U2 sum_j V2j`

has spectrum `{L,+LR,-LR,+L/R,-L/R,0,...}` and

`||p_Q||_infinity<=4/L`, with continuous density, uniformly in m,R and all cap-one coordinate laws.

Designated partner applied: account04/B08 commit `abbec61f52e1f4b4d367fd67e73e4d2501ac9c74` pays the missing `m=1` concentrated endpoint by `<7.251/L`; our diffuse gate fails there because both light leverages equal one.

Checker: `QFORM_B08_R37_CHECK_PASS`; 1200 seeded leverage/determinant identity tests had max errors `2.78e-15` and `7.21e-15`.

Next debt: `QFORM-ALIGNED-OR-LOCALIZED-MULTIHUB-LEAKAGE-RECEIVER-v1` — consume aligned/high-leverage low-rank survivors while retaining arbitrary non-diagonal same-bank light curvature. Global QFORM and global continuity remain OPEN. Status `WITHOUT_VERIFIED_BRAIN`.
