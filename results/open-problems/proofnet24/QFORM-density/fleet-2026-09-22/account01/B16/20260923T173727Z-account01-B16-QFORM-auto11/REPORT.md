SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T17:37:27Z.
attacking: rank-(3,2) source-cut projection-product closure—combine genuine 3D/2D product projection caps with the dependence-safe cross2 overlap-square receiver, and isolate the exact isotropic-plane endpoint.

# account01/B16 — rank-(3,2) plane-determinant overlap compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM + PARTNER RESULT APPLIED / FULL QFORM OPEN`  
**Regularity:** the new theorem proves a continuous density on its stated branch; global QFORM continuity remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope, source discipline, and live corrections

The full owner target remains OPEN: arbitrary finite dimension, independent original-coordinate real variables with one-dimensional densities at most one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No support, moment, smoothness, log-concavity, identical-law, diagonal-basis, or post-rotation-independence hypothesis is introduced here.


- a bounded joint projected density alone does **not** control an indefinite quadratic level-set integral;
- a spectral/source rotation does **not** create independence among projected coordinates;
- normalized conditional projection caps can diverge and are not used;
- law-uniform pointwise quadratic-phase decay is false;
- the newest source-adapted-hub functional remains OPEN for arbitrary cap-one inputs.

The two mathematical inputs used below are source-pinned:

1. **Actual product-projection theorem.** `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T115514Z-qform-B18-a01/REPORT.md`, Theorem 3.1: for every full-row-rank `T`,

   `||p_(TX)||_infinity <= 2^(k/2)/sqrt(det(TT^T))`.

   In particular a genuine orthonormal three-dimensional product projection has cap `2 sqrt(2)` and a genuine orthonormal two-dimensional product projection has cap `2`. This statement supplies joint densities only; it supplies no independence after projection.

2. **Dependence-safe overlap-square receiver.** `yspennstate/math-open-problems@bfb102a2317191969c16cf336b53ed47a8a06c6d`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/account01-B16-20260923T170732Z-auto11/REPORT.md`, theorem `QFORM-CROSS2-OVERLAP-SQUARE-L1-v1`: for disjoint source banks, a rank-two crossing plus a nonzero square carried by a third, possibly dependent, projection of the same bank as one crossing pair has

   `||p_Q||_infinity <= C_* (MN)^(2/5)(s_1s_2)^(-2/5)|lambda|^(-1/5)`,

   `C_*=5(675/256)^(1/5)=6.069917185377548...`,

   and has a continuous density. Arbitrary same-side curvature on the opposite source bank is allowed.

The newest completed designated-partner source actually applied in Section 5 is account02/B16 at

`yspennstate/math-open-problems@c8258480a0bfb67e9b128e67c477c5c5dcdd38e8`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/account02-B16-20260923T163017Z-auto11b/REPORT.md`.

It supplies `QFORM-HUB-SCHUR-DIFFUSE-CROSS2-v1`, its near-null stress family, and the source-first true-density bound `<176` in that family.

## 2. New theorem: a rank-(3,2) source cut closes unless the occupied spectral plane is isotropic

### `QFORM-RANK32-PLANE-DET-OVERLAP-v1`

Let the quadratic form have exact rank three,

`A=R Lambda R^T`, `R^T R=I_3`,

where `Lambda` is real symmetric and invertible. Let `I,J,K` be disjoint original-coordinate sets whose union is all physical coordinates; `K` is allowed to be empty. Put

`G_I=R_I^T R_I`, `G_J=R_J^T R_J`.

Assume

`G_I>0`, `rank(G_J)=2`.                                           (2.1)

Let `t` be a unit vector spanning `ker(G_J)`, let `E` be a `3 x 2` orthonormal frame spanning `P=t^perp`, and set

`J_2=E^T G_J E>0`.

Define

`D=|det Lambda|`,
`C_P=E^T Lambda E`.

If

`det C_P !=0`,                                                    (2.2)

then for every independent cap-one original-coordinate input law,

`boxed:
 ||p_(X^T A X)||_infinity
 <= C_32 [det(G_I) pdet(G_J) D |det C_P|]^(-1/5),`               (2.3)

where

`C_32=10(675/256)^(1/5)
    =12.139834370755096... .`                                    (2.4)

The density is continuous. The same theorem holds with `I,J` interchanged when `rank(G_I)=2` and `G_J>0`.

Equivalently, because the cofactor identity gives

`t^T Lambda^(-1)t = det(C_P)/det(Lambda)`,                        (2.5)

(2.3) may be written

`boxed:
 ||p_Q||_infinity
 <= C_32 [det(G_I) pdet(G_J) D^2
          |t^T Lambda^(-1)t|]^(-1/5).`                           (2.6)

Thus the only endpoint left by this compiler is the exact inverse-Rayleigh null condition

`t^T Lambda^(-1)t=0`,                                            (2.7)

or equivalently the statement that the spectral plane occupied by the rank-two bank has singular restricted curvature `det(E^T Lambda E)=0`.

### Proof

Condition on the outside original coordinates `X_K`. This preserves the independent product law on `I union J`. Because `A=R Lambda R^T`, every interaction with the frozen outside coordinates becomes an affine term in the spectral aggregates `R_I^T X_I` and `R_J^T X_J`. The quadratic coefficient matrices below do not depend on the conditioning value.

Whiten the two genuine source-bank projections:

`Z=G_I^(-1/2) R_I^T X_I in R^3`,

`W=J_2^(-1/2) E^T R_J^T X_J in R^2`.                             (2.8)

The coefficient matrices producing `Z` and `W` have orthonormal rows. Therefore the actual product-projection theorem gives

`||p_Z||_infinity <=2 sqrt(2)`,
`||p_W||_infinity <=2`.                                          (2.9)

The two vectors are independent because `I` and `J` are disjoint original-coordinate banks. No independence is asserted among the three coordinates of `Z` or among the two coordinates of `W`.

In these whitened variables, the cross coefficient is

`L=G_I^(1/2) Lambda E J_2^(1/2)`,                                (2.10)

and the `I`-side quadratic matrix is

`B=G_I^(1/2) Lambda G_I^(1/2)`.                                  (2.11)

Since `Lambda`, `G_I`, and `J_2` are invertible on their stated spaces, `L` has rank two. Let `s_1,s_2>0` be its singular values and let `u` be the unit left-null vector,

`L^T u=0`.                                                        (2.12)

Put

`gamma=u^T B u`.                                                  (2.13)

We first compute the invariant `(s_1s_2)^2 gamma` exactly.

Set

`z=G_I^(1/2)u`.

Equation (2.12) says

`E^T Lambda z=0`,

so `Lambda z` is parallel to `t`. Hence for some scalar `kappa`,

`z=kappa Lambda^(-1)t`.                                          (2.14)

Define the positive scalar

`d=t^T Lambda^(-1) G_I^(-1) Lambda^(-1)t>0`.                     (2.15)

The normalization `||u||=1` implies `kappa^2=1/d`. Consequently

`gamma
 =z^T Lambda z
 =kappa^2 t^T Lambda^(-1)t
 =[t^T Lambda^(-1)t]/d`.                                         (2.16)

Next,

`(s_1s_2)^2=det(L^T L)`

`=det(J_2)
  det(E^T Lambda G_I Lambda E)`.                                 (2.17)

The matrix

`M=Lambda G_I Lambda`

is positive definite. In the orthonormal basis `[E,t]`, the standard `3 x 3` cofactor identity gives

`det(E^T M E)=det(M) t^T M^(-1)t`.                               (2.18)

Since

`det M=det(Lambda)^2 det(G_I)`,

`t^T M^(-1)t=d`,                                                  (2.19)

we obtain

`(s_1s_2)^2
 =pdet(G_J) det(Lambda)^2 det(G_I) d`.                            (2.20)

Multiplying (2.16) and (2.20) gives the key cancellation:

`boxed:
 (s_1s_2)^2 |gamma|
 =det(G_I) pdet(G_J) D^2
  |t^T Lambda^(-1)t|`

`=det(G_I) pdet(G_J) D |det C_P|.`                               (2.21)

Under (2.2), `gamma!=0`.

Now perform the left and right orthogonal singular-vector rotations of `L`. The source variable `Z` becomes `(Z_1,Z_2,T)` and `W` becomes `(W_1,W_2)`, still genuine orthonormal product projections of the same original banks with the same density caps (2.9). The cross term is

`2 s_1 Z_1W_1+2 s_2 Z_2W_2`,                                    (2.22)

and the third `I`-bank coordinate `T` has no cross interaction with `J`.

Write the rotated `I`-side quadratic and affine terms as

`gamma T^2+2T h^T Z_c+r(Z_c)+ell_T T`,

where `Z_c=(Z_1,Z_2)`. Since `gamma!=0`, complete the square in `T`:

`gamma [T+gamma^(-1)h^T Z_c+ell_T/(2gamma)]^2
 +r_1(Z_c)`.                                                      (2.23)

All `J`-side quadratic and affine terms are an arbitrary measurable function `H(X_J)` from the viewpoint of the overlap-square receiver. Therefore the conditioned form is exactly in `QFORM-CROSS2-OVERLAP-SQUARE-L1-v1` with

`M=2sqrt(2)`, `N=2`, `lambda=gamma`.

Because

`(MN)^(2/5)=(4sqrt(2))^(2/5)=2`,                                 (2.24)

the receiver gives

`||p_(Q|X_K)||_infinity
 <=2C_* (s_1s_2)^(-2/5)|gamma|^(-1/5)`

`=C_32 [(s_1s_2)^2|gamma|]^(-1/5)`.                              (2.25)

Insert (2.21) to obtain (2.3)-(2.6), uniformly in the outside conditioning. Averaging gives the same essential bound for `Q`.

For regularity, the overlap-square theorem supplies an `L^1` characteristic-function bound uniform in every affine parameter created by the outside conditioning. Tonelli therefore gives

`int |phi_Q(t)|dt
 <=E_K int |phi_(Q|X_K)(t)|dt<infinity`,                          (2.26)

so Fourier inversion supplies a continuous density. QED.

## 3. Balanced full-partition corollary and a numerical threshold

Assume now `K` is empty, so

`G_I+G_J=I_3`,                                                    (3.1)

and `rank(G_J)=2`. Let the two nonzero eigenvalues of `G_J` be `mu_1,mu_2`. Then `t` is also an eigenvector of `G_I` with eigenvalue one, and

`det(G_I) pdet(G_J)
 =mu_1mu_2(1-mu_1)(1-mu_2)`.                                     (3.2)

If

`1/4 <=mu_1,mu_2<=3/4`,                                         (3.3)

then

`det(G_I) pdet(G_J)
 >=(3/16)^2=9/256`.                                               (3.4)

For an exact-rank-three target, `D>=1`. Hence from (2.6), whenever

`|t^T Lambda^(-1)t|>=1/64`,                                     (3.5)

we get the literal universal inequality

`boxed:
 ||p_Q||_infinity
 <=12.1398343708 [(9/256)(1/64)]^(-1/5)
 =54.4813985486... <54.482.`                                     (3.6)

This is a dependence-safe use of the actual `3D x 2D` product projection. The bounded joint projection densities are not fed into an indefinite coarea integral; they enter only through the already-proved overlap-square Fourier receiver.

A deterministic numerical audit over 100 seeded random invertible symmetric `Lambda`, positive definite `G_I`, rank-two planes, and positive `J_2` matrices checked identity (2.21) to maximum relative discrepancy below `6.0e-15`. This is a finite arithmetic check of the derived identity, not an independent proof.

## 4. Geometric meaning of the remaining endpoint

The quantity left in (2.7) has an exact cofactor interpretation. In the spectral splitting `R^3=span(t) direct-sum P`, write

`Lambda=[[alpha,b^T],[b,C_P]]`.                                  (4.1)

Then

`t^T Lambda^(-1)t=det(C_P)/det(Lambda)`.                          (4.2)

Thus the new theorem pays every rank-(3,2) source cut for which the occupied rank-two spectral plane has nonzero quadratic determinant. The theorem stops only when

`det C_P=0`.                                                      (4.3)

At (4.3) the `J`-bank same-side quadratic has rank at most one. This is a substantially sharper description than “the cross block is only rank two”: the unspent endpoint is an **isotropic spectral plane**, where the third curvature resource has collapsed inside the two-dimensional bank and has to be combined with the original source weight before taking absolute values.

The endpoint is real in the target signature. For example

`Lambda=[[0,1,0],[1,0,0],[0,0,1]]`

has spectrum `{1,-1,1}` and, for `t=e_1`, both

`t^T Lambda t=0`, `t^T Lambda^(-1)t=0`.                           (4.4)

Hence no argument may simply assume a nonzero primal or inverse Rayleigh pivot.

## 5. Newest account02/B16 result applied to actual inequalities

The newest designated-partner report `c825848...` proves, in its true-near-coloop hard chamber with physical hub pivot `A_00!=0`,

`boxed:
 ||p_Q||_infinity
 <=13.0639452949 / sqrt(|A_00|).`                                (5.1)

This is `QFORM-HUB-SCHUR-DIFFUSE-CROSS2-v1`; it retains a true two-dimensional source-bank crossing after exact hub Schur completion and does not use a conditional projected-density cap.

Therefore, on any exact-rank-three near-coloop form that simultaneously admits the balanced rank-(3,2) cut of Section 3, both completed theorems apply to the **same** output law. Consequently

`boxed:
 ||p_Q||_infinity
 <=min{
   13.0639452949 |A_00|^(-1/2),
   12.1398343708 [(9/256)D^2
      |t^T Lambda^(-1)t|]^(-1/5)
 }.`                                                             (5.2)

In particular, because `D>=1`, if either

`|A_00|>=1/64`

or

`|t^T Lambda^(-1)t|>=1/64`,                                     (5.3)

then

`boxed: ||p_Q||_infinity <104.512.`                              (5.4)

Indeed the partner branch gives `13.0639452949*8=104.5115623592...`, while the inverse-Rayleigh branch gives the sharper `54.4813985486...` from (3.6).

This leaves, in that structured chamber, a genuinely **doubly-null collar**: small physical hub pivot together with a small inverse-Rayleigh pivot. It is not empty and cannot be discarded.

The partner's fully admissible stress family makes this explicit. With

`0<delta<1/64`, `c=1-delta`,
`b=sqrt(1+epsilon)`,

`Lambda_epsilon=[[epsilon,b,0],[b,0,0],[0,0,1]]`,                (5.5)

its eigenvalues are exactly `{1+epsilon,-1,1}`. Moreover

`Lambda_epsilon^(-1)
 =[[0,1/b,0],[1/b,-epsilon/b^2,0],[0,0,1]]`,                     (5.6)

so for the hub spectral direction `e_1`,

`e_1^T Lambda_epsilon^(-1)e_1=0`                                (5.7)

**exactly**, while the physical hub pivot is

`A_00=c epsilon`,                                                 (5.8)

which can be arbitrarily small. The corresponding target-valid quadratic form is

`Q_epsilon
 =epsilon Y^2+2sqrt(1+epsilon)YU+V^2`,

`Y=sqrt(c)X_0+sqrt(delta)T`,                                     (5.9)

with `(T,U,V)` coming from the same balanced residual product bank. Despite lying in the exact inverse-null and arbitrarily small physical-pivot regime, the partner's source-first grouping proves the actual inequality

`boxed: ||p_(Q_epsilon)||_infinity <176`                         (5.10)

for every independent cap-one original source law in its stated admissible parameter range. This is direct evidence that the remaining null collar is a **source-provenance problem, not a spectral-density counterexample**.

If `W` is any additional random variable generated by disjoint original coordinates, then the same completed partner result immediately gives the genuine higher-dimensional inequality

`||p_(Q_epsilon+W)||_infinity
 =||p_(Q_epsilon)*mu_W||_infinity<176`.                           (5.11)

No property of `W` beyond independence is required.

## 6. What changed and the next unpaid implication

Before this run, a rank-two source crossing plus same-bank curvature was analytically available, but there was no invariant compiler saying when an exact-rank-three `3D x 2D` source cut actually supplies the required nonzero square after source whitening.

Equation (2.21) supplies that compiler exactly. It shows that the product of the squared rank-two crossing volume and the missing same-bank square pivot is

`det(G_I) pdet(G_J) D |det(Lambda|_P)|`,                          (6.1)

with no hidden conditional-density quantity. Hence every quantitatively balanced rank-(3,2) cut is paid unless its occupied spectral plane is isotropic.

The first unpaid B16 implication is now

`QFORM-RANK32-ISOTROPIC-PLANE-SOURCE-TRANSDUCER-v1`:

> In the exact endpoint `det(Lambda|_P)=0`, combine the rank-two crossing with the rank-one same-side curvature on the two-dimensional source bank and the null-direction coupling on the three-dimensional source bank, retaining the original product sources until after the nonlinear integration. A proof may not replace either bank by an arbitrary bounded joint density and may not condition to a normalized projection-height supremum.

For the true near-coloop problem beyond exact rank-(3,2), the analogous unresolved state is the partner's two-small-longitudinal-innovation source-adapted hub collar. The stress family (5.9) shows these two descriptions meet at the same primal/inverse-null hyperbolic geometry.

The full arbitrary-rank QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains OPEN.

## 7. Source pins and verification record

- product-projection theorem: `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401:proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T115514Z-qform-B18-a01/REPORT.md`;
- overlap-square theorem: `yspennstate/math-open-problems@bfb102a2317191969c16cf336b53ed47a8a06c6d:proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/account01-B16-20260923T170732Z-auto11/REPORT.md`;
- newest account02/B16 partner: `yspennstate/math-open-problems@c8258480a0bfb67e9b128e67c477c5c5dcdd38e8:proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/account02-B16-20260923T163017Z-auto11b/REPORT.md`;
- newest projected-crossing context read: `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`;
- current Claude continuation read from `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md`; its adapted-hub `(SP)` statement remains explicitly OPEN for arbitrary cap-one inputs and was not used as a theorem.

The algebraic identity (2.21) was independently checked numerically on 100 deterministic seeded random instances; maximum relative discrepancy was below `6.0e-15`. The numerical check is only a consistency audit; the proof is the exact derivation in Section 2.

No schedule, enabled/quiet state, notification, email, task, permission, public-release, paid/remote-call, account binding, or cross-account authentication setting was changed.