SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T09:22:01Z.
attacking: the near-coloop transition by retaining a dependent projected pair and using one genuinely independent fresh-square source through an exact Schur-complement half-Riesz calculation.

# account03/B16 — dependent-pair / fresh-square Schur transducer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Run:** `20260923T092201Z-account03-B16-QFORM-r26`  
**Status:** `NEW SUPPORTING THEOREM / STRICTER NEAR-COLOOP RECEIVER / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** the theorem below proves absolute continuity and an essential `L^infinity` bound. It does not by itself prove continuity. Global continuity remains open.

## 1. Exact owner target and source boundary

The target remains: for every `n`, independent real original-coordinate variables `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove that `X^T A X` has a density bounded by one universal finite constant, or produce a valid counterexample.

Fresh owner control was reread before publication from `yspennstate/math-research-brain` main, OWNER CONTROL revision `2026-09-22.15`; QFORM is still the sole research target and account03/B16 is not paused. The live correction inbox was reread. In particular, nothing below uses post-rotation independence, arbitrary-joint coarea, positive conditional projection-density moments, worst-fiber suprema, coefficient deletion, or a law-uniform pointwise van-der-Corput estimate.

The immediate account03/B16 predecessor is

`yspennstate/math-open-problems@a398a1c2e6e97683e3fe594fa19476929a882be6`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T045948Z-account03-B16-QFORM-r26/REPORT.md`.

It closes every branch of the current exact-rank-three dominant-star compiler except the genuine near-coloop collar `c>63/64`. The present run changes mechanism from capped Pluecker basis weights to a direct curved half-Riesz/Schur calculation.

A second source used below is account02/B16's completed semi-aligned source-scalar theorem,

`yspennstate/math-open-problems@2eaaea917e087d7cf276dc37714e02af3a50d64a`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T082859Z-account02-B16-QFORM-r11/REPORT.md`.

That theorem pays `delta Y^2+2k UY+beta V^2` when `X`, `V`, and the possibly dependent pair `(H,U)` are separate source objects. The result below removes the semi-alignment: it permits every deterministic `YU`, `YV`, `UV`, `U^2`, `V^2` coupling and affine term, under one exact Schur-sign condition.

## 2. Main theorem

### Theorem `QFORM-DEPENDENT-PAIR-FRESH-SQUARE-SCHUR-v1`

Let `(H,U)` be an arbitrary real random pair; **no independence between `H` and `U` is assumed**. Let `X` and `V` be real random variables such that the three source objects

`X`, `(H,U)`, `V`

are mutually independent. Assume the one-dimensional marginal density caps

`||p_X||_infinity <= L_X`,
`||p_U||_infinity <= L_U`,
`||p_V||_infinity <= L_V`.                                      (2.1)

Let `gamma !=0` and put

`Y=gamma X+H`.                                                    (2.2)

Let

`B = [[a,k,m],[k,l,n],[m,n,b]]`                                  (2.3)

be a real symmetric invertible `3 x 3` matrix with `b!=0`, and allow an arbitrary deterministic affine term

`r_1 Y+r_2 U+r_3 V+r_0`.                                         (2.4)

Define the first diagonal of the Schur complement after the `V` coordinate,

`delta := a-m^2/b`.                                              (2.5)

Assume the **same-sign Schur gate**

`b delta >=0`.                                                    (2.6)

Then

`Q=(Y,U,V)^T B (Y,U,V)+r_1Y+r_2U+r_3V+r_0`                      (2.7)

is absolutely continuous and has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= 8 L_V sqrt(L_X L_U/|gamma|)
       (|b| |det B|)^(-1/4).
`                                                                    (2.8)

At the exact Schur-null endpoint `delta=0`, the factor `8` improves to `4`:

`boxed:
 ||p_Q||_infinity
 <= 4 L_V sqrt(L_X L_U/|gamma|)
       (|b| |det B|)^(-1/4).
`                                                                    (2.9)

The bounds are uniform in the **entire joint law of `(H,U)`**. Thus no conditional cap for `U|H` is required and no independence is inferred from a bounded projection density.

### Why this is stronger than the semi-aligned theorem

The entries `m` and `n` may both be nonzero. In particular, `V` may couple linearly in the quadratic form to both `Y` and `U`; these couplings are not perturbatively discarded. They are absorbed exactly by the Schur complement. Likewise the residual `U^2` coefficient and all deterministic affine terms are retained.

## 3. Proof

Multiplying the whole output by `-1` preserves density height. Hence, if necessary, replace `(B,r,r_0)` by its negative and assume

`b>0`.                                                            (3.1)

The sign gate (2.6) then says `delta>=0`.

### 3.1 Eliminate only the genuinely independent fresh square

Complete the square in the **random variable `V`**, conditionally on `(Y,U)`:

`bV^2+2mYV+2nUV+r_3V
 = b[V+(mY+nU+r_3/2)/b]^2
   -(mY+nU+r_3/2)^2/b`.                                          (3.2)

The shift in brackets may depend on `(Y,U)`, but conditional on `(Y,U)` it is deterministic. Since `V` is independent of `(Y,U)` and `p_V<=L_V`, translation preserves the cap. The square pushforward therefore gives, for the conditional output density,

`p_(Q|Y,U)(t)
 <= L_V b^(-1/2) [t-F(Y,U)]_+^(-1/2)`,                           (3.3)

where the exact Schur remainder is

`F(y,u)=delta y^2+2 kappa u y+lambda u^2+p y+q u+c`,             (3.4)

with

`kappa = k-mn/b`,
`lambda = l-n^2/b`,
`p = r_1-m r_3/b`,
`q = r_2-n r_3/b`,
`c = r_0-r_3^2/(4b)`.                                            (3.5)

Thus

`p_Q(t)
 <= L_V b^(-1/2)
    E [t-F(Y,U)]_+^(-1/2).`                                      (3.6)

This is the point where product provenance matters: the fresh source `V` is used before any projection-only compression.

### 3.2 A quadratic level-set lemma

We will use the elementary fact that for every quadratic polynomial

`D(u)=A+B_1 u+theta u^2`, `theta!=0`,                            (3.7)

and every `s>0`,

`|{u: 0<D(u)<s}| <= 2 sqrt(s/|theta|)`.                          (3.8)

Proof: complete the square. If `theta>0`, the set is either a centered interval or two shells outside the zero set; in either case

`sqrt(x+s)-sqrt(x) <= sqrt(s)`

bounds the total length by (3.8). If `theta<0`, the same calculation applies to the interval/shell inside the two roots. This estimate is uniform in the constant and linear coefficients.

Consequently, if `U` has density at most `L_U`, then

`E[D(U)_+^(-1/4)]
 <= int_0^infinity min(1, 2 L_U |theta|^(-1/2) z^(-2)) dz
 = 2 sqrt(2L_U) |theta|^(-1/4).`                                (3.9)

### 3.3 The nonzero Schur-pivot case `delta>0`

Condition on `(H,U)=(h,u)`. By (2.2), the conditional law of `Y` is simply a translate/rescale of the genuine independent scalar `X`, so it is a probability density with cap

`L_Y=L_X/|gamma|`.                                                (3.10)

No conditional information about `U|H` is requested.

For fixed `t,u`, put

`K(y)=[t-F(y,u)]_+^(-1/2)`.                                      (3.11)

Complete the deterministic quadratic in `y`. Define

`D_t(u)
 := delta(t-lambda u^2-q u-c)+(kappa u+p/2)^2`.                  (3.12)

For `D_t(u)<=0`, the positive set of (3.11) is empty up to a null point. For `D_t(u)>0`, a direct solution of the two boundary layers gives, for every `z>0`,

`|{y:K(y)>z}| <= 2/[sqrt(D_t(u)) z^2]`.                          (3.13)

Indeed, if `z^(-2)` exceeds the full quadratic height, the right side equals or exceeds the entire positive interval; otherwise the difference-of-square-roots bound gives (3.13).

Layer cake, the cap (3.10), and probability normalization give

`E[K(Y)|H=h,U=u]
 <= 2 sqrt(2L_Y) D_t(u)_+^(-1/4).`                              (3.14)

Crucially, the right side is independent of `h`. Expanding (3.12),

`D_t(u)=A_t+B_t u+theta u^2`,                                    (3.15)

where

`theta=kappa^2-delta lambda`.                                    (3.16)

The `2 x 2` Schur complement of the `V` coordinate is

`S=[[delta,kappa],[kappa,lambda]]`,                              (3.17)

so block determinant algebra gives

`det B=b det S=b(delta lambda-kappa^2)=-b theta`.                (3.18)

Because `B` is invertible, `theta!=0`, and

`|theta|=|det B|/b`.                                             (3.19)

Average (3.14) against the joint law of `(H,U)`. Since its bound depends only on `U`, only the **unconditional marginal cap** of `U` enters. Equations (3.9), (3.14), and (3.19) give

`E[t-F(Y,U)]_+^(-1/2)
 <= 8 sqrt(L_Y L_U) |theta|^(-1/4).`                            (3.20)

Substitute (3.10), (3.19) into (3.6):

`p_Q(t)
 <=8 L_V sqrt(L_XL_U/|gamma|)
      b^(-1/2)(|det B|/b)^(-1/4)
 =8 L_V sqrt(L_XL_U/|gamma|)
      (b|det B|)^(-1/4).`                                       (3.21)

This is (2.8).

### 3.4 Exact Schur-null endpoint `delta=0`

Now invertibility of `B` and (3.18) imply `kappa!=0`. The Schur remainder is affine in `y`:

`F(y,u)=(2kappa u+p)y+lambda u^2+q u+c`.                        (3.22)

For fixed `(h,u)`, the one-dimensional layer-cake estimate gives

`E([t-F(Y,u)]_+^(-1/2)|H=h,U=u)
 <=2 sqrt(L_Y) |2kappa u+p|^(-1/2).`                            (3.23)

The affine variable `2kappa U+p` has a density cap at most `L_U/(2|kappa|)`. The cap-one bathtub integral for `|x|^(-1/2)` yields

`E|2kappa U+p|^(-1/2)
 <=2 sqrt(L_U/|kappa|).`                                        (3.24)

Therefore

`E[t-F(Y,U)]_+^(-1/2)
 <=4 sqrt(L_YL_U)|kappa|^(-1/2).`                               (3.25)

At `delta=0`, (3.18) says `|det B|=b kappa^2`, so (3.6) becomes exactly (2.9).

The one-dimensional pushforward formulas and Tonelli establish absolute continuity throughout. No continuity assertion is made.

## 4. Product-projection corollary for the near-coloop compiler

Suppose a branch of an exact-rank-three original-product problem can be written with **three genuine source objects**:

1. an untouched original coordinate `X`;
2. one original-coordinate bank whose two projections are `(H,U)` and may be arbitrarily dependent;
3. a disjoint original-coordinate bank producing a normalized scalar projection `V`.

If the normalized scalar projections satisfy the standard product-projection caps

`||p_U||_infinity, ||p_V||_infinity <= sqrt(2)`,                (4.1)

and the hub coefficient obeys `|gamma|=sqrt(c)` with `c>63/64`, then Theorem 2.1 gives, whenever the same-sign Schur gate holds,

`||p_Q||_infinity
 <= 8*2^(3/4)c^(-1/4)(|b||det B|)^(-1/4)
 <13.508 (|b||det B|)^(-1/4).`                                  (4.2)

This bound is **uniform as `delta ->0`**. Thus the reciprocal nonzero-pivot loss is removed on this full-coupling fresh-square branch. At `delta=0`, the leading constant in (4.2) is halved.

The remaining connection to the full near-coloop collar is now explicit: one must either extract such a disjoint fresh scalar square with quantitative `|b det B|`, or prove a replacement receiver when every usable transverse square shares its original-coordinate source bank with `(H,U)`. The latter shared-bank case is not solved here.

## 5. Strict target-class stress family with nonzero `UV` coupling

The theorem is not merely a reformulation of the semi-aligned account02/B16 source. Here is a target-valid family with a genuine `UV` coupling.

Fix `c>63/64`, set `a=1-c`, choose even `m`, and let

`X_0,X_1,...,X_m,Z_1,...,Z_m`

be arbitrary independent real variables with densities at most one. Choose balanced signs `epsilon_j in {+1,-1}` and put

`T=m^(-1/2) sum_j X_j`,
`U=m^(-1/2) sum_j epsilon_j X_j`,
`V=m^(-1/2) sum_j Z_j`,                                         (5.1)

`Y=sqrt(c)X_0+sqrt(a)T`.                                         (5.2)

Then `(T,U)` may be strongly dependent, but the three source objects

`X_0`, `(T,U)`, `V`

are mutually independent. The completed one-dimensional product-projection theorem gives

`||p_U||_infinity,||p_V||_infinity <=sqrt(2)`.                  (5.3)

For `0<=r<=1/10`, define

`M_r=[[-r,1,0],[1,0,1],[0,1,-1]]`,
`B_r=6M_r`,                                                       (5.4)

and

`Q_r=(Y,U,V)^T B_r(Y,U,V)`.                                     (5.5)

The `UV` coefficient is nonzero (`2(B_r)_{23}=12`), so this is outside the semi-aligned model used in the predecessor account02/B16 theorem.

### 5.1 It is a genuine three-large-eigenvalue target

The deterministic spectral frame has physical rows

`r_0=(sqrt(c),0,0)`,
`r_j=(sqrt(a/m),epsilon_j/sqrt(m),0)`,
`r_(m+j)=(0,0,1/sqrt(m))`.                                      (5.6)

Balanced signs give `R^T R=I_3`; hence the three nonzero eigenvalues of the physical matrix `A=RB_rR^T` are exactly the eigenvalues of `B_r`.

Now

`det M_r=1+r>=1`,
`||M_r||_F^2=5+r^2<=501/100`.                                   (5.7)

For a `3 x 3` invertible matrix,

`s_min(M_r)
 >= |det M_r|/||M_r||_op^2
 >=1/||M_r||_F^2
 >=100/501`.                                                      (5.8)

Therefore

`s_min(B_r)>=600/501>1`.                                        (5.9)

So every `Q_r` is exactly inside the owner's target class.

### 5.2 Uniform bound across the nonzero-to-null transition

For `B_r`, take the fresh-square coordinate to be `V`. Then

`b=-6`, `det B_r=216(1+r)`,                                     (5.10)

and the first Schur-complement diagonal is

`delta=-6r`.                                                      (5.11)

Thus `b delta=36r>=0`, so the theorem applies for the entire interval including `r=0`. Furthermore

`|b det B_r|=1296(1+r)=6^4(1+r)`.                              (5.12)

Using (5.3), `L_X=1`, and `gamma=sqrt(c)`, (2.8) gives for every `0<r<=1/10`

`||p_(Q_r)||_infinity
 <=(4/3)2^(3/4)c^(-1/4)(1+r)^(-1/4)
 <2.252.`                                                        (5.13)

At the exact Schur-null endpoint `r=0`, (2.9) improves this to

`||p_(Q_0)||_infinity
 <=(2/3)2^(3/4)c^(-1/4)
 <1.126.`                                                        (5.14)

Thus a genuinely cross-coupled target family lying arbitrarily close to a physical null hub is controlled uniformly without replacing the small coefficient by zero and without conditioning on `U|T`.

The committed checker records the exact determinant/Schur identities, the spectral lower bound `600/501>1`, and the numerical constants in (5.13)-(5.14).

## 6. Required application of designated partner account04/B16

The designated partner report is

`yspennstate/math-open-problems@b111363ff02b67015d14db35482e0150591744cd`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T231542Z-account04-B16-QFORM-r1/REPORT.md`.

Its exact-rank-three theorem `QFORM-RULED-PLUECKER-ENDPOINT-v1` proves, for disjoint-Pluecker probability `d`,

`||p_Q||_infinity
 <=12 |det Lambda|^(-1/3)d^(-1/6).`                              (6.1)

Since the target normalization has `|det Lambda|>=1`, at the active branch threshold

`d>=1/64
 => ||p_Q||_infinity
 <=12(1/64)^(-1/6)
 =24.`                                                            (6.2)

This is the designated partner result applied at an actual inequality in the present run. Hence the new Schur transducer is only needed after the partner's `d>=1/64` exit has been removed. The same partner also retains the majority-sign one-sheet bound `pi sqrt(2)` in the `d=0` coloop endpoint.

## 7. What is now paid and what remains

The theorem supplies an exact dependence-preserving interface unavailable to the false bounded-joint-density route:

- one projected pair `(H,U)` may remain arbitrarily dependent;
- only an actual disjoint original-coordinate scalar source `V` is declared independent;
- all `YV` and `UV` quadratic couplings are kept and paid exactly by the Schur complement;
- the only cap used for `U` is its unconditional one-dimensional marginal cap;
- the estimate is uniform through `delta=0` on the same-sign Schur side.

It does **not** prove that every near-coloop exact-rank-three frame admits the required fresh-square decomposition with quantitative `|b det B|`, and it does not handle the opposite-sign Schur side by this argument. The latter is not a cosmetic restriction: the two-variable indefinite kernel has a genuine logarithmic endpoint and an absolute one-dimensional layer-cake bound loses control there.

The next B16 implication is therefore

`QFORM-NEAR-COLOOP-FRESH-SQUARE-OR-SHARED-BANK-v1`:

> In the residual exact-rank-three collar `c>63/64`, after the `d>=1/64` partner exit and the already-paid physical-pair/transverse exits, either extract a disjoint original-coordinate transverse scalar bank satisfying the same-sign Schur gate and a universal lower bound on `|b det B|`, so Theorem 2.1 applies, or force a quantitatively structured **shared-bank** endpoint and attack that endpoint without a conditional projection cap.

Arbitrary additional spectrum remains a separate full-target debt. Nothing in this report promotes the exact-rank-three result to the full arbitrary-rank matrix.

## 8. Verification and status

Checker: `CHECK.py`. Recorded current-run output: `CHECK_OUTPUT.txt`, ending `STATUS=PASS`. The repository connector does not execute code; the output file records an independent current-run evaluation of the exact formulas rather than claiming remote execution.

No target counterexample is supplied. The full conjecture remains **OPEN / NOT PROVED**. Global continuity remains **OPEN**. Native learned-memory receiver use was not observed, so the run remains **WITHOUT_VERIFIED_BRAIN**.
