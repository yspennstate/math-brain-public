SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T03:21:56Z.
attacking: extreme-shear and low-rank grouped regimes via source-valid projection-density bounds and partner zero-pivot smoothing.

# account03/B18 r22 — source-separated isotropic shear closes the large-shear branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and scope

The owner target remains the unrestricted assertion for independent real original-coordinate random variables `X_i` with probability densities `0<=f_i<=1` and an arbitrary real symmetric matrix `A` having at least three eigenvalues of modulus at least one. The desired conclusion is a dimension- and law-independent density bound; continuity is tracked separately.

This report proves a new exact-rank-three branch inside the surviving Schur-isotropic zero-pivot geometry. It does **not** claim that its extra source-separation hypothesis follows from the three-large-eigenvalue assumption. The unrestricted conjecture remains open.


## 2. Primary literature transfer

The positive external input used below is the primary theorem of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949; Israel J. Math. 216 (2016), 877--889. If `X=(X_1,...,X_m)` has product probability density with every one-dimensional factor bounded by one, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. No moment, centering, bounded-support, connected-support, log-concavity, iid, Gaussian, or smoothness assumption is imposed. In particular a two-dimensional orthogonal projection has density cap `2`.

I also rechecked Banks--Garza-Vargas--Kulkarni--Srivastava, arXiv:2005.08930. Their non-Gaussian quadratic-density ingredient is a bilinear-plus-affine expression in two genuinely independent arrays, with singular-value/rank hypotheses. It does not by itself license absorption of an arbitrary same-side quadratic term after a spectral rotation, so it is not used outside its hypotheses here.

No exact published theorem located in this source check settles the owner's unrestricted target. This is not a novelty claim.

## 3. Canonical Schur-isotropic shear and a deterministic spectral ledger

Consider the exact-rank-three surviving zero-pivot form

`Q=(Y+u X_0)^T D (Y+u X_0)`,                                      (3.1)

where `X_0` is one original coordinate, independent of the residual original-coordinate product vector `X_R`; `Y=V^T X_R`; `V^T V=I_3`; `D=D^T` is nonsingular; and

`u^T D u=0`.                                                       (3.2)

Let `r=||u||>0`, `n=u/r`, and choose an orthonormal basis `(n,e_2,e_3)` in the three-dimensional spectral space with

`e_2 = Dn/||Dn||`.

This is well defined because `D` is nonsingular. Put `kappa=||Dn||`. In this basis

`D = [[0,kappa,0],[kappa,a,b],[0,b,c]]`.                           (3.3)

Let `L=[u,V^T]`. Then

`LL^T=I+uu^T`,                                                     (3.4)

and the nonzero eigenvalues of the physical matrix `A=L^T D L` equal the eigenvalues of

`B=(I+uu^T)^(1/2) D (I+uu^T)^(1/2)
  = [[0,k,0],[k,a,b],[0,b,c]],`                                   (3.5)

where `k=sqrt(1+r^2) kappa`.

If all three nonzero eigenvalues of `A` have modulus at least one, then all singular values of symmetric `B` are at least one, so `B^2 >= I`. Applying this to `e_1` gives

`k=||B e_1||>=1`.                                                  (3.6)

Moreover solving `B x=e_3` gives

`B^(-1)e_3=(-b/(kc),0,1/c)`.

Since `||B^(-1)||<=1`,

`|c|>=sqrt(1+b^2/k^2)>=1`.                                        (3.7)

Thus target normalization forces a genuine hyperbolic shear coefficient and a transverse quadratic coefficient even when every useful physical diagonal pivot is absent. This ledger alone is not yet a density theorem because the corresponding projected coordinates need not be independent.

A second exact identity is

`|pdet A|=(1+r^2)|det D|`.                                        (3.8)

Indeed the product of the three nonzero eigenvalues of `L^T D L` equals `det(D LL^T)`, and `det(LL^T)=1+r^2`. Hence the target normalization implies

`|det D| >= 1/(1+r^2)`.                                           (3.9)

## 4. New theorem: source-separated isotropic shear

### Theorem — `QFORM-ISOTROPIC-SHEAR-SOURCE-SEPARATED-v1`

Assume (3.1)--(3.2), exact rank three, and the target normalization that the three nonzero eigenvalues of `A` have modulus at least one. In addition assume the residual Parseval frame is **source-separated with respect to** `n=u/r`: every residual physical row `v_j in R^3` of `V` is either parallel to `n` or orthogonal to `n`.

Equivalently, after writing

`Z=(Z_1,Z_2,Z_3)=O^T Y`

in an orthonormal basis whose first vector is `n`, the scalar aggregate `Z_1` depends only on one subset `K` of the original residual coordinates and the pair `(Z_2,Z_3)` depends only on the disjoint complementary subset `J`.

Then for every admissible independent cap-one input law and every `r>=1`, `Q` has a **continuous density** and

`boxed: ||p_Q||_infinity <= 12.`                                  (4.1)

More precisely,

`||p_Q||_infinity
 <= 6*2^(2/3) ((1+r^2)/r^2)^(1/3).`                              (4.2)

### Proof

Rotate only the three-dimensional coefficient space so that `u=r e_1`. This is an algebraic reparametrization of the three aggregate coordinates; no independence after rotation is asserted. By the source-separation hypothesis the resulting scalar `Z_1` is a function of original coordinates in `K`, while `T=(Z_2,Z_3)` is a function of the disjoint original-coordinate block `J`. Therefore `Z_1` and `T` are genuinely independent, and both are independent of the original scalar `X_0`.

Because the residual rows form a Parseval frame and the `K` rows are parallel to `e_1`, the two coefficient rows defining `T` on `J` are orthonormal. Thus `T` is exactly a two-dimensional orthogonal marginal of the product law on `J`. Livshyts--Paouris--Pivovarov gives

`||p_T||_infinity <= 2`.                                         (4.3)

Now set

`S = X_0 + Z_1/r`.                                                (4.4)

Since `X_0` is independent of `Z_1`, `S` is a convolution of the cap-one density of `X_0` with a probability law. Hence

`||p_S||_infinity <= 1`.                                         (4.5)

Also `S` is genuinely independent of the entire pair `T`.

Writing `D'=O^T D O`, condition (3.2) says `D'_(11)=0`, and

`Q=(rS,Z_2,Z_3)^T D' (rS,Z_2,Z_3)
  =(S,Z_2,Z_3)^T K (S,Z_2,Z_3)`,                                (4.6)

where

`K=diag(r,1,1) D' diag(r,1,1)`.                                  (4.7)

Thus `K` is symmetric, nonsingular, and has zero first diagonal. Its determinant satisfies

`|det K|=r^2 |det D| >= r^2/(1+r^2)`                             (4.8)

by (3.9).

Now apply the completed account04/B18 zero-pivot theorem `QFORM-ZEROPIVOT-1PLUS2-DENSITY-v1` at its exact hypotheses: a cap-one scalar independent of a two-dimensional vector with joint density cap `M`, and a nonsingular symmetric zero-pivot `3x3` matrix. With `M=2`, (4.3)--(4.8) give

`||p_Q||_infinity
 <= 6*2^(2/3)|det K|^(-1/3)
 <= 6*2^(2/3)((1+r^2)/r^2)^(1/3).`                              (4.9)

For `r>=1`, `(1+r^2)/r^2<=2`, so the right side is exactly at most `12`. The partner theorem also gives a continuous representative. QED.

This application is dependence-safe: it uses actual independence between disjoint original-coordinate source blocks. A mere bounded conditional density is not substituted for independence.

## 5. Explicit target family beyond the partner's mixed-volume row gate

For every `r>=1`, put `s=sqrt(1+r^2)`, take independent cap-one `X_0,X_1,X_2,X_3`, and set

`u=r e_1`,
`D_r=[[0,1/s,0],[1/s,0,0],[0,0,1]],
`Y=(X_1,X_2,X_3)`.

Then

`Q_r = 2/s (X_1+rX_0)X_2 + X_3^2
    = 2(r/s)(X_0+X_1/r)X_2 + X_3^2`.                            (5.1)

The physical matrix, in the order `(X_0,X_1,X_2,X_3)`, is

`A_r=[[0,0,r/s,0],
      [0,0,1/s,0],
      [r/s,1/s,0,0],
      [0,0,0,1]].`                                               (5.2)

The `3x3` hyperbolic block has eigenvalues `-1,0,1`, because `(r/s)^2+(1/s)^2=1`; therefore

`spectrum(A_r)={-1,0,1,1}`                                      (5.3)

for every `r`. This is an exact target matrix with three eigenvalues of modulus one.

Here the source separation is literal: `Z_1=X_1` and `T=(X_2,X_3)`. In fact `T` has product density cap at most one, sharper than the general LPP cap `2`. Applying the same account04/B18 theorem with `M=1` gives

`boxed:
 ||p_(Q_r)||_infinity
 <= 6 ((1+r^2)/r^2)^(1/3)
 <= 6*2^(1/3)
 = 7.559526299369... .`                                         (5.4)

The density is continuous.

This family is genuinely complementary to account04/B18 r3's mixed-volume gate. With `V=I_3` and `n=e_1`, its residual leverage quantities are

`p=(1,1,1)`, `q=(0,1,1)`,

so `p_2+q_2=p_3+q_3=2>1`; the r3 hypothesis `p_j+q_j<=1` fails. Thus (5.4) closes an explicit large/extreme-shear target family left outside that partner gate.

Only one physical diagonal entry in (5.2) is nonzero (`A_33=1`), so this is not the elementary three-large-diagonal control.

## 6. Additional source-valid resource in the non-separated case

Even without source separation, the deterministic ledger (3.6) yields a useful aggregate density bound. In the basis of (3.3), let `L=r kappa Z_2`. The pair `(Z_2,Z_3)` is a two-dimensional orthogonal marginal of the residual product source, so by LPP it has density at most `2`. Scaling one coordinate gives

`||p_(L,Z_3)||_infinity <= 2/(r kappa)
 = 2 sqrt(1+r^2)/(r k)
 <= 2 sqrt(1+r^(-2))`,                                          (6.1)

using `k>=1`. Hence for `r>=1`,

`||p_(L,Z_3)||_infinity <= 2sqrt(2)`.                            (6.2)

This is a real product-projection resource, but it is **not** by itself a closure theorem: the remaining coordinate `Z_1` is generally dependent on `(L,Z_3)`, and the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` shows that bounded pair/conditional caps cannot be substituted for genuine independence in the hyperbolic-square step. I therefore do not claim more from (6.2).

## 7. Quantifier and correction audit

- Inputs remain arbitrary independent real variables with densities bounded by one; no moments, centering, support, smoothness, log-concavity, iid, or Gaussian assumptions are introduced.
- Independence is invoked only between disjoint sets of original product coordinates. No spectral rotation is declared to preserve independence.
- No arbitrary-joint coarea estimate, positive conditional-height moment, fiber-supremum integration, fixed-good-minor implication, perturbative `near zero = zero`, or law-uniform pointwise Fresnel decay is used.
- The extra source-separation condition in Theorem 4 is stated explicitly and is **not** asserted to follow from `s_3(A)>=1`.
- Continuity is proved for Theorem 4 via the completed partner theorem. No continuity conclusion is promoted to the full conjecture.

## 8. Remaining implication

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. For the exact-rank-three Schur-isotropic core, account04/B18 r3 pays moderate shear under `p_j+q_j<=1`, while Theorem 4 above pays all `r>=1` when the shear direction and transverse plane are exactly separated across original-coordinate source blocks. The first local debt is therefore a **non-separated large-shear transducer**: retain the actual product-projection provenance when rows have mixed components along `n` and `n^perp`, and convert the source-valid resource (6.2), together with the forced `|c|>=1`, into a bounded-density estimate without invoking conditional-cap-as-independence.

Beyond exact rank three, the global exhaustive product-preserving ridge/grouped-coordinate reduction for arbitrary additional spectrum is still unpaid.

## 9. Source pins

- Livshyts--Paouris--Pivovarov, arXiv:1507.07949; Israel J. Math. 216 (2016), 877--889.
- Banks--Garza-Vargas--Kulkarni--Srivastava, arXiv:2005.08930; used only as a scope audit, not as a proof premise.
- Designated partner account04/B18 r2: `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.
- Latest partner mixed-volume comparison: `yspennstate/math-open-problems@24a9362bd3f24a3849021093cf98611f95b5ab04`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260923T001857Z-account04-B18-QFORM-r3/REPORT.md`.

Repository synchronization is not native learned-memory ingestion; this run remains `WITHOUT_VERIFIED_BRAIN`.
