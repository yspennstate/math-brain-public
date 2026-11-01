SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T13:01:29Z.
attacking: general indefinite physical-pair curved kernel — interpolate the zero-diagonal and nonzero-diagonal hyperbola regimes without taking any fiber supremum.

# fleet01/B06 — determinant-only quarter-Riesz receiver for every indefinite physical pair

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_ANALYTIC_THEOREM_PROVED / NEAR-NULL-PAIR-INTERPOLATION_CLOSED / FULL_TARGET_OPEN`.

The full arbitrary-dimensional QFORM conjecture is **not** proved or disproved here. The new theorem closes a specific analytic gap left by the newest Claude Fourier report: the missing interpolation between an exactly coordinate hyperbola and a nondegenerate but nearly coordinate indefinite quadratic form in two independent original coordinates. It yields a determinant-only quarter-Riesz physical-pair peel and, in exact rank three, removes the extra `sigma_min(B)` factor from the existing pair-log receiver.

Continuity is **not** claimed by the new direct argument. The conclusions below are essential-density bounds.

Execution label: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval was used, but no authenticated native learned-memory retrieval plus receiver use was established.

## 1. Fresh source boundary and inputs actually used


The source inputs used are:

1. **Newest Claude Fourier report**, `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. Its Lemma 4.3 proves the exactly zero-diagonal coordinate-hyperbola peel and Section 6.3 explicitly leaves the interpolation to products of two general linear forms unwritten.

2. **Pair-log theorem**, `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`. It proves the rank-one affine small-ball estimate

   `sup_t P(|R-t|<rho) <= min(1,10 sqrt(rho/|lambda|))`              (1.1)

   for `R=lambda (h dot X)^2+b dot X+d`, `||h||=1`, with arbitrary affine vector `b`, and it identifies the exact-rank-three Schur coefficient `|lambda|>=s`.

3. **Designated partner fleet02/B06.** The completed theorem `QFORM-191-STAR-HUB-INTERNAL-PAYMENT-v1`, canonical report `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260923T105551Z-182f201f81de/REPORT.md`, gives in its exact-rank-three heavy-star chamber the actual inequality

   `boxed: either ||p_Q||_inf <1447/s,
           or ||B_(i,L)||_2 >= s/(16sqrt(2)) for every heavy i.`     (1.2)

   Thus every failure of that partner robust-light gate is already paid. The new pair receiver below is relevant only after (1.2) has reduced the remaining geometry to robust light packets / physical-pair emergence; it is not being used to re-open the paid branch.

4. **Designated partner fleet02/B06 weighted projection theorem**, canonical `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, gives for a one-dimensional orthogonal projection of the original cap-one product law the actual bound

   `||p_(h dot X)||_inf <= sqrt(e)`.                                (1.3)

   Section 6 applies (1.3) to a quarter-Riesz inequality, not merely as a citation.

## 2. Main two-variable theorem

### Theorem 2.1 — `QFORM-GENERAL-HYPERBOLA-QUARTER-RIESZ-v1`

Let `X,Y` be independent real random variables with probability densities `f,g` satisfying `0<=f,g<=1`. Let

`q(x,y)=a x^2+bxy+c y^2`,                                           (2.1)

and suppose the quadratic form is nondegenerate indefinite:

`d:=sqrt(b^2-4ac)>0`.                                                (2.2)

Then `q(X,Y)` is absolutely continuous and, for almost every `u!=0`,

`boxed:
 p_q(u) <= C_hyp d^(-3/4)|u|^(-1/4),
 C_hyp=2^(7/4)sqrt(3)=5.8259012604... .`                            (2.3)

A stronger near-coordinate estimate proved below is

`p_q(u) <= (4sqrt(3)/d)
           log(1+(1/sqrt(2))*sqrt(d/|u|))`                          (2.4)

whenever `|a|,|c|<d/4`.

The theorem is uniform over arbitrary fragmented and unbounded supports. It uses the original product factors before any curved-fiber supremum.

### Proof

The critical set of the nondegenerate quadratic polynomial is the single point `(0,0)`, so coarea/one-variable conditioning gives an absolutely continuous pushforward away from the critical value, and the estimates below are locally integrable at zero. We prove (2.3) by two exhaustive cases.

### 2.1 Case A: one square coefficient is not small

Assume first

`|c|>=d/4`;                                                        (2.5)

the case `|a|>=d/4` is identical after interchanging `X,Y`.

Condition on `X=x`. Solving

`c y^2+bxy+a x^2=u`

for `y`, the discriminant is

`Delta_x=d^2 x^2+4cu`.                                              (2.6)

At every real root,

`|2cy+bx|=sqrt(Delta_x)`.                                           (2.7)

There are at most two roots and `g<=1`, hence

`p_q(u)
 <=2 int f(x) 1_(Delta_x>0)/sqrt(Delta_x) dx.`                     (2.8)

#### Same-sign subcase `cu>=0`

Put

`A=2sqrt(|cu|)/d`.

Then

`p_q(u)<= (2/d) int f(x)/sqrt(x^2+A^2) dx`.                         (2.9)

The kernel is symmetric decreasing in `|x|`. Since `0<=f<=1` and `int f=1`, the bathtub principle gives

`int f(x)/sqrt(x^2+A^2) dx
 <=int_(-1/2)^(1/2) dx/sqrt(x^2+A^2)
 =2 asinh(1/(2A))`.                                                 (2.10)

Thus

`p_q(u)<= (4/d) asinh(d/(4sqrt(|cu|)))`.                            (2.11)

From (2.5),

`d/(4sqrt(|cu|)) <=(1/2)sqrt(d/|u|)`.                              (2.12)

For `z>=0`,

`asinh(z/2)<=sqrt(z)`.                                              (2.13)

Indeed if `y=asinh(z/2)`, then `z=2sinh y`; `y^2<=2sinh y` for `0<=y<=2` because `sinh y>=y`, and for `y>=2` because `2sinh y-y^2` is positive at two and increasing thereafter. Hence

`p_q(u)<=4 d^(-3/4)|u|^(-1/4)`.                                   (2.14)

#### Opposite-sign subcase `cu<0`

Again put `A=2sqrt(|cu|)/d`. Real roots require `|x|>A`, and (2.8) gives

`p_q(u)<= (2/d) int_(|x|>A) f(x)/sqrt(x^2-A^2) dx`.                (2.15)

On the two rays the kernel is symmetric and decreases away from the singular endpoints `+-A`. Bathtub optimization with total available mass one therefore gives

`int_(|x|>A) f(x)/sqrt(x^2-A^2) dx
 <=2 int_A^(A+1/2) dx/sqrt(x^2-A^2)
 =2 arcosh(1+1/(2A))`.                                             (2.16)

By (2.5),

`A>=sqrt(|u|/d)`, so `1/(2A)<=(1/2)sqrt(d/|u|)`.                   (2.17)

Since `cosh y>=1+y^2/2`,

`arcosh(1+z/2)<=sqrt(z)`.                                          (2.18)

Equations (2.15)-(2.18) again yield (2.14).

Thus Case A satisfies (2.3) with the smaller constant four.

### 2.2 Case B: both square coefficients are small

Assume

`|a|<d/4`, `|c|<d/4`.                                               (2.19)

Then `b!=0`; otherwise `d^2=-4ac<d^2/4`, impossible. Also

`|b|>sqrt(3)d/2`,                                                    (2.20)

because `b^2=d^2+4ac>=d^2-4|a||c|>3d^2/4`.

Let `eps=sign(b)` and define

`B=(b+eps d)/2`, `s=c/B`, `t=a/B`.                                 (2.21)

The quadratic factors exactly:

`q(x,y)=B(x+s y)(y+t x)`.                                          (2.22)

Indeed `Bt=a`, `Bs=c`, and `B(1+st)=b` because `B` solves `B^2-bB+ac=0`.

Set

`lambda0=2-sqrt(3)`,
`m0=(2+sqrt(3))/4`.                                                 (2.23)

By (2.20),

`|B|>m0 d`,
`|s|,|t|<lambda0`.                                                  (2.24)

Let

`k=1-st`.

Since `|st|<1`, `k>0`, and comparison of discriminants in (2.22) gives the exact identity

`|B| k=d`.                                                          (2.25)

Make the deterministic linear change

`z=x+s y`, `w=y+t x`;                                               (2.26)

its Jacobian is `k`. The inverse is

`x=(z-s w)/k`, `y=(w-t z)/k`.                                      (2.27)

This is only a change of variables in a Lebesgue integral; no rotated random coordinates are declared independent. The transformed joint density is

`k^(-1) f((z-sw)/k) g((w-tz)/k)`.                                  (2.28)

Put `v=u/B`. The product coarea formula on `zw=v` therefore gives

`p_q(u)
 =1/d int_R
   f((z-sv/z)/k)
   g((v/z-tz)/k)
   dz/|z|`.                                                         (2.29)

Let `r=sqrt(|v|)` and split the integral into `|z|>=r` and `|z|<r`.

#### Outer hyperbola

On `|z|>=r`, define

`x(z)=(z-sv/z)/k`.

Because `|sv/z^2|<=|s|<lambda0`, each sign ray is monotone and

`|x'(z)|>=(1-lambda0)/k`.                                          (2.30)

Also

`(1-lambda0)|z|/k <=|x(z)|<=(1+lambda0)|z|/k`.                     (2.31)

The positive and negative sign-ray images are disjoint. Using `g<=1`, changing from `z` to the original coordinate `x`, and combining (2.30)-(2.31),

`I_out
 <=[(1+lambda0)/(1-lambda0)]
   int_(|x|>=a0) f(x) dx/|x|`,                                    (2.32)

where

`a0=(1-lambda0)r/k`.                                                (2.33)

The same one-dimensional bathtub calculation used in the exact coordinate-hyperbola lemma gives

`int_(|x|>=a0) f(x) dx/|x|
 <=2 log(1+1/(2a0)).`                                               (2.34)

#### Inner hyperbola

On `|z|<r`, substitute `w=v/z`. Then `|w|>r` and

`|dz|/|z|=|dw|/|w|`.                                                (2.35)

Now

`y(w)=(w-tv/w)/k`

obeys the same estimates with `t` in place of `s`; use `f<=1` and the density `g`. Thus

`I_in
 <=2[(1+lambda0)/(1-lambda0)]
   log(1+1/(2a0)).`                                                 (2.36)

Adding (2.32)-(2.36), and using the exact constants

`(1+lambda0)/(1-lambda0)=sqrt(3)`,                                 (2.37)

and, from `k=d/|B|`, `r=sqrt(|u|/|B|)`, `|B|>=m0 d`,

`1/(2a0)
 =d/[2(1-lambda0)sqrt(|B||u|)]
 <=[1/(2(1-lambda0)sqrt(m0))]sqrt(d/|u|)
 =(1/sqrt(2))sqrt(d/|u|)`,                                         (2.38)

we obtain the sharper estimate (2.4):

`p_q(u)
 <=(4sqrt(3)/d)
   log(1+(1/sqrt(2))*sqrt(d/|u|)).`                                (2.39)

Finally, for every `x>=0`,

`log(1+x)<=sqrt(x)`,                                                (2.40)

because the derivative of `sqrt(x)-log(1+x)` is

`((sqrt(x)-1)^2)/(2sqrt(x)(1+x))>=0`.

Apply (2.40) to `x=(1/sqrt(2))*sqrt(d/|u|)` in (2.39). This gives

`p_q(u)
 <=4sqrt(3) 2^(-1/4)d^(-3/4)|u|^(-1/4)
 =2^(7/4)sqrt(3)d^(-3/4)|u|^(-1/4)`,                               (2.41)

which is (2.3). QED.

## 3. General affine indefinite physical pair

### Corollary 3.1 — `QFORM-INDEFINITE-PHYSICAL-PAIR-QUARTER-RIESZ-v1`

Let `X_1,X_2` be independent cap-one variables and let `B` be any invertible indefinite symmetric `2x2` matrix. Put

`D=|det B|`.

For arbitrary `ell in R^2` and `c in R`,

`F=X^T B X+2 ell^T X+c`                                            (3.1)

has a density satisfying

`boxed:
 p_F(t)
 <=2sqrt(3) D^(-3/8)|t-t0|^(-1/4),
 t0=c-ell^T B^(-1)ell.`                                            (3.2)

### Proof

Complete the square:

`F=(X+B^(-1)ell)^T B (X+B^(-1)ell)+t0`.                            (3.3)

The two translated coordinates remain independent and keep density cap one. If the quadratic coefficients are `a=B_11`, `b=2B_12`, `c=B_22`, then

`sqrt(b^2-4ac)=2sqrt(D)`.                                           (3.4)

Apply Theorem 2.1. Since

`2^(7/4)sqrt(3)*(2sqrt(D))^(-3/4)
 =2sqrt(3)D^(-3/8)`,                                                (3.5)

the result follows. QED.

This is the sought interpolation: no scalar diagonal is required to vanish, and no `sigma_min(B)` appears.

## 4. Weighted ambient receiver — curvature before supremum

### Theorem 4.1 — `QFORM-WEIGHTED-INDEFINITE-PAIR-RECEIVER-v1`

Let `X=(X_P,X_K)` have independent cap-one original coordinates, with `|P|=2`, and suppose the physical principal pair

`B=A_PP`

is invertible indefinite. Put `D=|det B|`. Conditional on `X_K=z`, complete the pair and write

`Q=((X_P)+m(z))^T B((X_P)+m(z))+R(z)`.                              (4.1)

Then for almost every `t`,

`boxed:
 p_Q(t)
 <=2sqrt(3)D^(-3/8)
   E |t-R(X_K)|^(-1/4).`                                           (4.2)

Consequently, with

`H_(1/4)(R)=sup_t E|t-R|^(-1/4)`,                                  (4.3)

`boxed:
 ||p_Q||_inf
 <=2sqrt(3)D^(-3/8) H_(1/4)(R).`                                  (4.4)

### Proof

For fixed outside coordinates `z`, the two original pair coordinates remain independent with their original density caps; only their deterministic translations change. Apply Corollary 3.1 conditionally and then Tonelli/Fubini. The singular kernel is averaged against the actual remainder law **before** any supremum over fibers. QED.

This theorem directly matches the B06 assignment: it retains the full ellipse/hyperbola geometry and replaces a worst-fiber maximum by a probability-weighted quarter-Riesz potential.

## 5. Exact-rank-three determinant-only pair theorem

The existing pair-log theorem shows that inside an exact-rank-three original-coordinate principal block whose three nonzero eigenvalue magnitudes are at least `s`, completing any invertible physical pair leaves a rank-one Schur remainder

`R=lambda (h dot W)^2+b dot W+d`,
`||h||=1`, `|lambda|>=s`.                                          (5.1)

Its completed rank-one affine small-ball estimate is (1.1). We now convert it to exactly the quarter-Riesz quantity required by Theorem 4.1.

For any fixed `t`, layer cake gives

`E|R-t|^(-1/4)
 =int_0^infinity P(|R-t|<v^(-4)) dv`.                              (5.2)

By (1.1), with `H=10/sqrt(s)`,

`P(|R-t|<v^(-4))<=min(1,H v^(-2))`.                                (5.3)

Therefore

`E|R-t|^(-1/4)
 <=int_0^infinity min(1,Hv^(-2))dv
 =2sqrt(H)
 <=2sqrt(10)s^(-1/4).`                                             (5.4)

Substituting (5.4) into (4.4) proves:

### Corollary 5.1 — `QFORM-RANK3-INDEFINITE-PAIR-DET-ONLY-v1`

Under the exact-rank-three physical-block hypotheses above,

`boxed:
 ||p_Q||_inf
 <=4sqrt(30) D^(-3/8)s^(-1/4).`                                   (5.5)

This applies uniformly after conditioning arbitrary ambient outside coordinates because the rank-one affine small-ball theorem already retains the induced affine vector.

The previous pair-log theorem gave

`8sqrt(5)(D*kappa*s)^(-1/4)`,                                      (5.6)

where `kappa=sigma_min(B)`. The new estimate (5.5) removes `kappa` entirely. The two estimates are complementary: (5.5) is especially useful for highly anisotropic physical pairs, where `kappa` is much smaller than the geometric mean encoded by `D`.

## 6. Designated-partner weighted projection applied at an equation

For the unconditioned exact-rank-three remainder with no extra affine component outside the rank-one direction, write

`R=lambda (h dot X)^2+d`,
`||h||=1`, `|lambda|>=s`.                                          (6.1)

The designated fleet02/B06 weighted affine-fiber Brascamp--Lieb theorem gives the actual projection-density inequality

`||p_(h dot X)||_inf <=sqrt(e)`.                                   (6.2)

Let `Y=h dot X`. If a scalar variable has density cap `M`, scaling `Y'=M Y` produces a density cap one. The newest-Claude square-potential calculation gives, for every cap-one scalar `Z`,

`sup_c E|Z^2-c|^(-1/4)<=4`.                                        (6.3)

Hence from (6.2),

`H_(1/4)(lambda Y^2)
 <=4 e^(1/4)|lambda|^(-1/4)
 <=4 e^(1/4)s^(-1/4).`                                             (6.4)

The weighted receiver (4.4) therefore gives the concrete partner-applied inequality

`boxed:
 ||p_Q||_inf
 <=8sqrt(3)e^(1/4) D^(-3/8)s^(-1/4)
 <17.792 D^(-3/8)s^(-1/4).`                                       (6.5)

Equation (6.5) is a direct mathematical use of the designated partner result, not a status citation. For arbitrary induced affine terms, use the fully robust bound (5.5) instead.

## 7. Relation to the current proof map

### 7.1 The newest-Claude R2 interpolation gap

The Fourier report Section 6.3 asks for a uniform density estimate for

`L_1(X,Y)L_2(X,Y)`,                                                 (7.1)

where `L_1=alpha X+beta Y`, `L_2=gamma X+delta Y`, and

`Delta=alpha delta-beta gamma !=0`.                                 (7.2)

Here

`L_1L_2=(alpha gamma)X^2
 +(alpha delta+beta gamma)XY
 +(beta delta)Y^2`,                                                  (7.3)

and its discriminant is exactly `Delta^2`. Theorem 2.1 therefore supplies the previously missing uniform interpolation:

`boxed:
 p_(L_1L_2)(u)
 <=2^(7/4)sqrt(3)
   |Delta|^(-3/4)|u|^(-1/4),
 u!=0.`                                                            (7.4)

It also supplies the logarithmic near-coordinate envelope (2.4). Thus the **analytic product-of-two-general-linear-forms subproblem** recorded as R2 is closed at the quarter-Riesz strength needed by the peel calculus. This does **not** by itself prove the whole bounded-dimensional reduction or the unrestricted QFORM theorem; the structural glue R1 and other unpaid regimes remain.

### 7.2 The current fleet01/B06 r32 two-sided packet hub

The immediate B06 predecessor reduces a high-collision bordered packet to one physical coordinate carrying target-scale two-sided incidence mass, but it does not guarantee one physical pair determinant `D` bounded below. The new theorem removes the additional conditioning parameter `kappa` once an indefinite pair is exposed, but it does not justify selecting such a pair from incidence mass alone. Therefore it genuinely strengthens the receiver without violating the correction against premature single-minor selection.

### 7.3 The current fleet02/B06 robust-light hub

Apply partner (1.2) first. If its paid alternative occurs, the branch is closed by `1447/s`. Otherwise every heavy row retains light-bank norm at least `s/(16sqrt(2))`. If subsequent structural work exposes an invertible indefinite physical pair of determinant `D`, the only analytic cost of that pair is now `D^(-3/8)` through (5.5), rather than `(D*kappa)^(-1/4)`. The remaining problem is therefore structural aggregation, not a near-zero-diagonal analytic discontinuity.

## 8. What remains unpaid

The full conjecture remains **OPEN**. This run does not prove that the three-large-eigenvalue hypothesis always produces a physical indefinite pair with target-scale determinant, and it does not convert the r32 incidence sums into one such pair. The principal remaining B06 implication is

`QFORM-AGGREGATE-PAIR-DET-OR-MIXED-FRESNEL-v1`:

> Starting from a robust light packet or the r32 two-sided one-index bordered packet, either aggregate the determinant mass into the quarter-Riesz receiver (4.4) without selecting a tiny minor first, or route the complementary geometry into the already-proved mixed-Fresnel / volume exits.

A valid proof must retain original-coordinate product provenance and the full outside quadratic curvature. The new theorem has not yet received an independent end-to-end mathematical review.

## 9. Claims established in this run

- `QFORM-GENERAL-HYPERBOLA-QUARTER-RIESZ-v1` — PROVED SUPPORTING THEOREM.
- `QFORM-INDEFINITE-PHYSICAL-PAIR-QUARTER-RIESZ-v1` — PROVED SUPPORTING THEOREM.
- `QFORM-WEIGHTED-INDEFINITE-PAIR-RECEIVER-v1` — PROVED SUPPORTING THEOREM.
- `QFORM-RANK3-INDEFINITE-PAIR-DET-ONLY-v1` — PROVED SUPPORTING THEOREM, using the existing rank-one affine small-ball result.
- Full QFORM — OPEN.
- Global continuous-density conclusion — OPEN.
