SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T02:54:11Z.
attacking: sharp Rogozin transfer for the designated partner's extreme-shear family, combined with exact capped-basis entropy factors.

# account01/B18 r22 — sharp scalar aggregation + exact capped-basis factor

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Literature-to-proof transfer  
**Status:** PROVED SUPPORTING TARGET-LEVEL SHARPENING / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Scope and source pins

The owner target remains open: arbitrary independent original-coordinate inputs with probability densities at most one, and arbitrary real symmetric A with at least three eigenvalues of modulus at least one. Continuity is tracked separately.

The designated partner result actually used is account02/B18 run `20260923T013147Z-bf13c29b`, canonical report

- `yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T013147Z-bf13c29b/REPORT.md`.

Its theorem `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1` states: if S has density cap K and is independent of a pair (C,D) with arbitrary joint density cap M, then for beta,gamma nonzero,

`Q=2 beta S C + alpha C^2 + 2 delta C D + gamma D^2`

has

`||p_Q||_infinity <= 3 (2 M K)^(2/3) |beta^2 gamma|^(-1/3)`.       (1.1)

The target-valid family to which I apply it is the same partner family. For ten independent cap-one variables, put

`Y_1=(X_1+X_2+X_3)/sqrt(3)`,
`Y_2=(X_4+X_5+X_6)/sqrt(3)`,
`Y_3=(X_7+X_8+X_9)/sqrt(3)`,
`S_r=(r X_0+Y_1)/sqrt(1+r^2)`,
`Q_r=2 S_r Y_2+Y_3^2`,                                               (1.2)

for r>0. Account03/B18 r21 proves that the physical matrix of Q_r has exactly the nonzero spectrum `{-1,1,1}` for every r, at

- `yspennstate/math-open-problems@c7d99a5becf262e519f50bd221ab49c0bd807534`
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260923T005908Z-account03-B18-QFORM-r21/REPORT.md`.

Thus every Q_r is inside the exact owner target.

### Primary source 1: Juškevičius--Lee

T. Juškevičius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190, Theorem 1 and Corollary 1. The source hypothesis is independence plus specified maximum-density caps; in dimension one it gives the sharp Rogozin comparison with centered uniform intervals. Our X_i are independent and each has density cap one, so after scalar multiplication each summand satisfies exactly the required cap. No moment, centering, support, log-concavity or smoothness hypothesis is introduced.

### Primary source 2: Livshyts--Paouris--Pivovarov

G. Livshyts, G. Paouris and P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1. For a genuine product probability density with one-dimensional factors bounded by one, every k-dimensional orthogonal marginal has density cap at most `2^(k/2)`. This matches the owner source class exactly; it does not assert independence after projection. It validates the partner's generic two-dimensional projected-pair cap `M<=2` when needed.

I also checked Herry--Malicet--Poly, arXiv:2303.09488. Its quadratic-form regularity results assume iid inputs from a substantially smoother Gaussian-functional class and asymptotic operator hypotheses, so it is not an exact prior solution of the present arbitrary non-iid cap-one target.

## 2. Sharp scalar maximum-density transfer for S_r

Set

`a=r/sqrt(1+r^2)`, `b=1/(sqrt(3)*sqrt(1+r^2))`.

By Juškevičius--Lee, the maximum density of

`S_r=a X_0+b(X_1+X_2+X_3)`

is no larger than the maximum density of

`a U_0+b(U_1+U_2+U_3)`,                                             (2.1)

where the U_i are independent Uniform[-1/2,1/2]. This comparison is sharp over the allowed source class.

Let `W=U_1+U_2+U_3` and `q=a/(2b)=sqrt(3)r/2`. The Irwin--Hall density in centered coordinates is

`f_W(w)=3/4-w^2` for `|w|<=1/2`,
`f_W(w)=(3/2-|w|)^2/2` for `1/2<=|w|<=3/2`,
`f_W(w)=0` otherwise.                                                (2.2)

Since the comparator is symmetric unimodal, its maximum occurs at zero and

`K_*(r):=||p_(S_r)||_infinity
 <= a^(-1) P(|W|<=q)`.

Therefore

`K_*(r) <= sqrt(1+r^2)/r *
 { (3/2)q-(2/3)q^3,                 0<r<=1/sqrt(3),
   1-(3/2-q)^3/3,                   1/sqrt(3)<=r<=sqrt(3),
   1,                               r>=sqrt(3) }`,                   (2.3)

with `q=sqrt(3)r/2`.

The first branch equals

`(sqrt(3)/4) sqrt(1+r^2)(3-r^2)`.

It reaches `4/3` at `r=1/sqrt(3)`. In particular the source-valid sharp comparison gives the global scalar estimate

`boxed: ||p_(S_r)||_infinity <=4/3`                                  (2.4)

for every r>0, and at r=1 the sharper value is

`K_*(1)=(5/4)(sqrt(6)-sqrt(2))=1.2940952255126035...`.               (2.5)

This is a genuine literature-to-proof transfer: it replaces the partner's one-summand Young estimate by the exact maximum-density comparator for all four original-coordinate summands.

## 3. Actual application of account02/B18

Juškevičius--Lee also gives

`||p_(Y_2)||_infinity, ||p_(Y_3)||_infinity <= R_0=3sqrt(3)/4`.

The two banks use disjoint original coordinates, hence are genuinely independent and

`M:=||p_(Y_2,Y_3)||_infinity <= R_0^2=27/16`.                       (3.1)

Apply (1.1) to (1.2) with `S=S_r`, `(C,D)=(Y_2,Y_3)`, `beta=gamma=1`, `alpha=delta=0`. This gives the concrete target-level inequality

`boxed: ||p_(Q_r)||_infinity <=3 ((27/8) K_*(r))^(2/3).`             (3.2)

For example at r=1,

`||p_(Q_1)||_infinity
 <=3[(135/32)(sqrt(6)-sqrt(2))]^(2/3)
 =8.015819504288615...`,                                             (3.3)

improving the partner's direct null-pivot estimate at r=1.

For r>=sqrt(3), (2.3) is simply `K_*(r)=sqrt(1+r^(-2))`, so

`C_R(r):=(27/4)(1+r^(-2))^(1/3)`.                                  (3.4)

## 4. Exact Hausdorff--Young/Brascamp--Lieb factor on the same family

Account01/B18 r19 proved `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`, using Beckner's sharp Hausdorff--Young inequality and Lieb/Bennett--Carbery--Christ--Tao Brascamp--Lieb Gaussian exhaustion. For a rank-three factorization `A=L^T D L` and an admissible basis law with coordinate marginals alpha_i<=1/2,

`||p_Q||_infinity <=3 B_alpha^(2/3)(|det D| Z_w)^(-1/3)`,            (4.1)

where

`B_alpha=prod_i (1-alpha_i)^(-(1-alpha_i)/2)`,                       (4.2)

and this route supplies a continuous density.

Account03/B18 r21 gives, for the family (1.2), determinant-proportional basis laws whose marginals can be read exactly.

### 4.1 r<=1: full-volume law

Put `beta=r^2/(1+r^2)`. The marginals are

`alpha_0=beta`, three collinear residual rows have `alpha=(1-beta)/3`, and six transverse rows have `alpha=1/3`. Also `|det D|Z_w=1`. Thus

`B_vol(beta)
 =(1-beta)^(-(1-beta)/2)
  ((2+beta)/3)^(-(2+beta)/2)
  (3/2)^2`.                                                         (4.3)

A direct derivative gives

`d/d beta log B_vol = (1/2) log(3(1-beta)/(2+beta))`.                (4.4)

Hence on `0<=beta<=1/2` the unique maximum is at `beta=1/4`, i.e. `r=1/sqrt(3)`, and

`max B_vol =2sqrt(3)`.                                               (4.5)

Therefore every `0<r<=1` has a continuous density with

`||p_(Q_r)||_infinity <=3(2sqrt(3))^(2/3)
 =6.868285455319992...`.                                             (4.6)

### 4.2 r>=1: mixed half/half law

The partner's mixed residual/shear basis law has marginals

`alpha_0=1/2`, three collinear residual rows `alpha=1/6`, and six transverse rows `alpha=1/3`. Therefore

`B_mix=2^(1/4)(6/5)^(5/4)(9/4)
      =3.360598077357783...`.                                       (4.7)

Its score is `Z_w=2r`, while `|det D|=1/(1+r^2)`. Equation (4.1) therefore gives the continuous-density certificate

`C_F(r)=3 B_mix^(2/3) ((1+r^2)/(2r))^(1/3)`,                        (4.8)

with prefactor

`3 B_mix^(2/3)=6.730783753531773...`.

The function C_F is increasing on r>=1. The null-pivot estimate C_R in (3.4) is decreasing on r>=sqrt(3). Their intersection is beyond sqrt(3), so no middle-branch differentiation from (2.3) is needed. Solving `C_F(r)=C_R(r)` gives

`r_*=729/(32 B_mix^2)
    =9/[2sqrt(2)(6/5)^(5/2)]
    =2.0171788261496966... >sqrt(3)`.                               (4.9)

At this point

`C_*=(27/4)(1+r_*^(-2))^(1/3)
    =(27/4)[1+(8/81)(6/5)^5]^(1/3)
    =7.262986442948119...`.                                         (4.10)

For `1<=r<=r_*`, use the increasing C_F; for `r>=r_*`, use the decreasing C_R. Combining with (4.6) gives

`boxed: sup_(r>0) ||p_(Q_r)||_infinity <=7.262986443.`               (4.11)

This improves the designated account02/B18 run's `8.176373543` uniform bound for the same exact-target family by about `11.17%`.

## 5. Continuity, corrections, and remaining implication

Continuity is not inferred from the null-pivot kernel. It is supplied separately by the capped-basis theorem: the full-volume certificate covers `r<=1` and the mixed certificate covers `r>=1`. Thus every Q_r has a continuous density. Where the sharper essential bound (3.4) is used, that same continuous representative cannot exceed the essential bound at an isolated point: otherwise continuity would produce a positive-measure neighborhood above the essential supremum. Hence (4.11) may be taken as the pointwise supremum bound for the continuous representative as well.

Fresh corrections consumed include the prohibition on post-rotation independence, arbitrary-joint coarea, conditional projection-density moment gates, fixed-good-minor/rank-three-cross extraction, and treating a dependent remainder as an independent convolution. The newly posted `QFORM-COHEAVY-SINGLE-ROW-EXTRACTION-FALSE-v1` also does not affect this calculation: no single physical row or 2+1 determinant is extracted; the proof uses the exact disjoint-bank structure of (1.2).

No exact prior theorem settling all owner quantifiers was found in the primary-source check. That search miss is not used as novelty evidence.

The full QFORM conjecture remains OPEN. The first unpaid implication is still structural: for an arbitrary large-shear / high-leverage survivor, extract a product-preserving bounded-density scalar aggregate independent of a transverse two-dimensional projection with a nondegenerate null-pivot determinant, or prove that failure routes into an already-paid ridge, grouped-bank, physical-pair, or volume-tail branch. The present run strengthens the analytic payment once such a packet exists; it does not prove that every A admits it.
