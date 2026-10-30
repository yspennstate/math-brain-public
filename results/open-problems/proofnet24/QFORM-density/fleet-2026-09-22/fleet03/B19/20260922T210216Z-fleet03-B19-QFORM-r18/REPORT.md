SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B19, 2026-09-22T21:02:16Z.
attacking: the quantitative two-Schur-pivot branch; remove the small-eigenvalue/kappa loss from an indefinite physical pair by sequential square smoothing and the surviving third-source small-ball estimate.

# fleet03/B19 r18 — sequential two-pivot smoothing closes the opposite-sign two-arm packet

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** universal proof assembly  
**Fresh owner revision:** `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL BRANCH CLOSED / FULL QFORM OPEN`.

The full owner target remains open: for every dimension, every product input with one-dimensional densities at most one, and every real symmetric `A` with `s_3(A)>=1`, prove one universal essential-supremum bound for the density of `X^T A X`, or produce a genuine target counterexample. Continuity is separate and is **not** proved by the theorem below.

This run changes mechanism from the preceding B19 two-bank/null-row work. It uses sequential original-coordinate Schur pivots and a translation-uniform small-ball estimate; it does **not** use the refuted arbitrary-joint 3D coarea statement, positive conditional projection-density moments, post-rotation independence, a worst fiber supremum, a fixed-good-minor premise, or law-uniform pointwise quadratic-phase decay.

## 1. Completed sources actually used

1. **Arbitrary-rank residual small ball.** The complete full-matrix pair extension at

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`,

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`

proves, for every nonzero real symmetric `S`, arbitrary affine terms and independent cap-one coordinates,

`sup_w P(|Z^T S Z+b^T Z+d-w|<rho)
 <= min(1,5 (rho/||S||_op)^(1/4)).`                              (1.1)

It also proves the rank-two approximation fact that if an invertible physical `2x2` block is Schur-completed from a matrix with `s_3(A)>=s`, then the remaining Schur matrix `T` obeys

`||T||_op>=s`.                                                    (1.2)

2. **Fresh two-arm packet.** fleet03/B20 at

`yspennstate/math-open-problems@56f7a951d545e6639d4b89fbfa18b0a1158ffe44`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260922T204947Z-fleet03-B20-QFORM-r17/REPORT.md`

reduces its low-leverage direct-alignment survivor to two original-coordinate Schur pivots `a,d` with

`|a|>=m:=3501/8000`, `|d|>1/8`, `a d<0`.                       (1.3)

The same-sign case was already paid there. Its first unpaid implication was exactly to find a dependence-safe third-source payment for the opposite-sign state.

3. **Designated partner fleet04/B19.** `QFORM-FINITE-UNION-CORE-v1`, canonical source

`yspennstate/math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T122030Z-fleet04-B19-QFORM-r1/REPORT.md`,

proves that for every measurable output map the interval concentration supremum over arbitrary product cap-one densities is exactly the supremum over product indicators of bounded finite unions of intervals of measure one. I apply this to the new `<67` interval inequality in Section 6.

## 2. A one-dimensional square/half-Riesz envelope

The analytic point is that two sequential Schur squares do not need a well-conditioned eigenbasis for their physical `2x2` pair. The first square produces a half-Riesz kernel. The second square has a logarithmic critical singularity, and the third spectral source pays that logarithm through (1.1).

### Lemma 2.1 — `QFORM-SQUARE-HALFRIESZ-LOG-ENVELOPE-v1`

Let `Y` have a probability density `f` with `0<=f<=1`. For every `lambda>0`, every shift `h`, and every nonzero `u`,

`E |lambda (Y+h)^2-u|^(-1/2)
 <= (2 sqrt(2)/sqrt(lambda))
    [2+log_+( sqrt(lambda)/(2 sqrt(|u|)) )].`                    (2.1)

At `u=0` the left side may be infinite; this endpoint will have zero probability once the third-source small-ball estimate is applied.

### Proof

Translate `Y` and scale out `lambda`. It suffices to bound

`I(v)=int f(x)|x^2-v|^(-1/2) dx`, `v!=0`.

For `v=-r<0`, pointwise

`(x^2+r)^(-1/2)<=|x^2-r|^(-1/2)`,

so it is enough to take `v>0`. Put

`k_v(x)=|x^2-v|^(-1/2)`

and let

`m_v(t)=|{x:k_v(x)>t}|`.

Since `f<=1` and `int f=1`, layer cake gives the exact cap-one reduction

`I(v)<=int_0^infinity min(1,m_v(t)) dt`.                         (2.2)

Writing `delta=t^(-2)`, one has

`m_v(t)=2[ sqrt(v+delta)-sqrt((v-delta)_+) ].`                  (2.3)

Two elementary bounds are enough:

`m_v(t)<=2 sqrt(2)/t` for all `t>0`,                             (2.4)

and, when `delta<v`,

`m_v(t)<=4/(t^2 sqrt(v)).`                                      (2.5)

For (2.4), if `delta>=v` then (2.3) is at most `2sqrt(2delta)`; if `delta<v`, the squared inner difference is

`2v-2sqrt(v^2-delta^2)
 =2delta^2/[v+sqrt(v^2-delta^2)]<=2delta`.

Equation (2.5) follows by rationalizing (2.3) and lower-bounding its denominator by `sqrt(v)`.

Let `A=2sqrt(2)` and `t_0=sqrt(2/v)`. If `v<1/4`, integrate the cap `1` on `[0,A]`, (2.4) on `[A,t_0]`, and (2.5) on `[t_0,infinity)`:

`I(v)<=4sqrt(2)+2sqrt(2) log(1/(2sqrt(v))).`                    (2.6)

If `v>=1/4`, (2.5) is already available from `A` onward and gives `I(v)<=4sqrt(2)`. This is exactly

`I(v)<=2sqrt(2)[2+log_+(1/(2sqrt(v)))].`

Restoring `v=|u|/lambda` proves (2.1). QED.

## 3. Logarithmic critical value paid by a quarter-small-ball third source

### Lemma 3.1

Let a scalar random variable `R` obey, uniformly in `t`,

`P(|R-t|<rho)<=min(1,H rho^(1/4))`.                              (3.1)

Then for every `lambda>0`,

`E log_+( sqrt(lambda)/(2sqrt(|R-t|)) )
 <=2[1+log_+(H lambda^(1/4)/sqrt(2))].`                         (3.2)

### Proof

Set

`L=log_+( sqrt(lambda)/(2sqrt(|R-t|)) )`,
`K=H lambda^(1/4)/sqrt(2)`.

For `y>=0`,

`{L>y} subset {|R-t|<(lambda/4)e^(-2y)}`,

so (3.1) gives

`P(L>y)<=min(1,K e^(-y/2)).`

Integrating this tail yields `E L<=2K<=2` if `K<=1`, and

`E L<=2 log K+2`

if `K>1`. This is (3.2). QED.

The sign/source domain is explicit: (3.2) spends an **unconditional original-coordinate small-ball bound for the actual third-source residual `R`**. It does not use a positive conditional-density moment or a generic bounded joint density.

## 4. New target-level theorem: sequential two-Schur-pivot smoothing

### Theorem 4.1 — `QFORM-SEQUENTIAL-TWO-PIVOT-THIRD-SOURCE-v1`

Let `A` be real symmetric with

`s_3(A)>=s>0`.

Choose two ORIGINAL coordinates, ordered first and second, and write their physical principal block as

`B=[[a,b],[b,c]]`, with `a!=0` and `det B!=0`.

Let

`d=c-b^2/a=det(B)/a`                                             (4.1)

be the second scalar Schur pivot. Then for independent cap-one inputs and arbitrary affine terms, the full quadratic form has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= [4sqrt(2)/sqrt(|a d|)]
    [2+log_+( (5/sqrt(2)) (|d|/s)^(1/4) )].
`                                                                    (4.2)

Equivalently, since `|ad|=|det B|`, the power cost is only `|det B|^(-1/2)`; **there is no factor involving `sigma_min(B)`**. No sign assumption on `a,d` is needed. The theorem is useful in particular for a quantitative opposite-sign Schur pair whose ordinary smallest eigenvalue may be arbitrarily small because of a huge off-diagonal shear.

Only essential boundedness is asserted; this proof does not establish continuity.

### Proof

Write the remaining original coordinates as `Z`. Consecutive completion of squares in the two ORIGINAL variables gives exactly

`Q
 =a (X+eta Y+l(Z))^2
  +d (Y+h(Z))^2
  +R(Z),`                                                        (4.3)

where `eta=b/a`, `l,h` are affine, and the quadratic matrix of `R` is the exact two-coordinate Schur complement `T` of `B` in `A`.

The rank-two approximation identity from the completed source (1.2) gives

`||T||_op>=s_3(A)>=s`.                                           (4.4)

Therefore (1.1), including its allowed affine terms, gives

`sup_t P(|R-t|<rho)<=min(1,5 s^(-1/4) rho^(1/4)).`              (4.5)

Fix `Y,Z` and integrate only the original coordinate `X`. Translation by `eta Y+l(Z)` does not change its density cap. The density of `a(X+shift)^2` is bounded on its supported half-line by

`|a|^(-1/2)|u|^(-1/2)`.                                        (4.6)

Consequently, by Tonelli, for almost every target `t`,

`p_Q(t)
 <=|a|^(-1/2)
   E |d(Y+h(Z))^2+R(Z)-t|^(-1/2).`                              (4.7)

Now condition only on `Z`. The second original variable `Y` is still independent of `Z`, still has density cap one, and its shift `h(Z)` is deterministic under that conditioning. Apply Lemma 2.1 with `lambda=|d|` and `u=t-R(Z)`; the sign of `d` is harmless because the absolute half-Riesz kernel reduces the opposite sign to the same envelope. By (4.5), `R` has no atoms, so the `u=0` exceptional value has probability zero. Thus

`p_Q(t)
 <= [2sqrt(2)/sqrt(|ad|)]
    [2+ E log_+(sqrt(|d|)/(2sqrt(|t-R|)))].`                    (4.8)

Apply Lemma 3.1 with

`H=5s^(-1/4)`.

Then

`E log_+(sqrt(|d|)/(2sqrt(|t-R|)))
 <=2[1+log_+((5/sqrt(2))(|d|/s)^(1/4))].`                      (4.9)

Substituting (4.9) into (4.8) gives exactly (4.2). The bound is uniform in `t`; the conditional square laws are absolutely continuous, and the finite majorant above makes their mixture an absolutely continuous law with the stated essential bound. QED.

### Why this is not the refuted same-square absorption route

The live correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` shows that one nonzero square plus an arbitrary coupled quadratic on the same bank can collapse to a single square and remain unbounded. Theorem 4.1 spends an additional, quantitatively nonzero **third-source Schur residual** whose operator norm is forced by `s_3(A)>=s`; its unconditional quarter-small-ball estimate (4.5) is what integrates the logarithmic second-square critical value. If `s_3(A)=0`, this mechanism disappears, consistently with the rank-two logarithmic obstruction.

## 5. Direct application: the fresh fleet03/B20 opposite-sign packet is closed

In the fresh B20 state (1.3), take `s=1`,

`m=3501/8000`, `|a|>=m`, `|d|>=1/8`.

Since

`K_0=(5/sqrt(2))(1/8)^(1/4)
    =2.102241038134286...>1`,

the right side of (4.2), as a function of `lambda=|d|>=1/8`, is

`F(lambda)
 =[4sqrt(2)/(sqrt(m lambda))]
  [2+log((5/sqrt(2))lambda^(1/4))].`                            (5.1)

It is strictly decreasing on this range, because after removing the positive factor `lambda^(-3/2)` its derivative has sign

`1/4-(1/2)[2+log((5/sqrt(2))lambda^(1/4))]`,

which is already

`-1.1215019683...<0`

at `lambda=1/8` and decreases further. Therefore

`||p_Q||_infinity
 <=F(1/8)
 =66.3430374943...
 <67.`                                                           (5.2)

This removes the exact first unpaid implication named in fleet03/B20 r17, `QFORM-TWOARM-OPPOSITESIGN-THIRD-SOURCE-v1`. Combined with that run's `<13.433` same-sign theorem, **every quantitative two-pivot state in that direct two-arm packet is now paid**, with arbitrary same-bank curvature and arbitrary outside spectrum retained.

The key improvement over the ordinary physical-pair theorem is structural: a highly sheared pair can have `sigma_min(B)` arbitrarily small even when its two Schur pivots are bounded below. Sequential square smoothing uses the pivots themselves, so no `kappa` loss is paid.

## 6. Designated partner fleet04/B19 applied to the actual inequality

Restrict first to product indicators `1_{E_i}` with each `E_i` a bounded finite union of intervals of total length one. The proof above is valid verbatim and gives, throughout the B20 opposite-sign packet,

`|{x in prod_i E_i : x^T A x in I}| <67 |I|`                    (6.1)

for every interval `I`.

Apply the designated partner theorem `QFORM-FINITE-UNION-CORE-v1`: its equality of concentration suprema transfers (6.1), with **no constant loss**, from this finite-union testing core to every family of independent probability densities `0<=f_i<=1`. Thus the partner result is used on the actual new target inequality, not merely cited.

The direct proof of Theorem 4.1 already works for arbitrary cap-one densities, so this application is also an independent quantifier check on the extension step.

## 7. Compact conditional universal assembly after this run

The current proof tree can be shortened as follows, without promoting any supporting theorem beyond its stated scope.

1. Diffuse spectral-window/ridge states are paid by the completed regularized-determinant/ridge theorems.
2. Quantitatively useful definite physical pairs are paid by the elementary ellipse-area theorem.
3. Quantitatively useful indefinite physical pairs are paid by the completed full-matrix pair-log theorem; the new Theorem 4.1 is stronger on states with two quantitative sequential Schur pivots because it removes the pair `sigma_min` loss.
4. The fresh balanced two-arm direct packet is now completely paid: cross-dominated states by fleet04/B20, same-sign two-pivot states by fleet03/B20, and opposite-sign two-pivot states by (5.2).
5. Exact-rank-three scalar-pivot residual orientations are covered by the completed rank-two affine half-Riesz theorem; exact zero pivots require their separate product-preserving mechanisms and are not obtained by continuity.
6. Aggregate exterior `E_3` currency now gives a half-Riesz payment when a scalar Schur pivot and three residual cross directions are genuinely present.

This is still **not** an exhaustive reduction from only `s_3(A)>=1`. The surviving first global structural debt after the newly closed direct two-arm packet is to force, in the high-leverage/non-direct states, one of:

- a second quantitative original-coordinate Schur pivot (then Theorem 4.1 pays it),
- a quantitative indefinite pair/grouped row covered by pair-log,
- a diffuse ridge/cross bank covered by the regularized-determinant theorems,
- or one of the exact-null/grouped-coordinate branches already isolated by B10/B13/B19.

Concretely, fleet03/B20 still lists the **high-leverage augmented-bank branch** and the **pivot-star/heavy-edge branch** as separate debts. The old B19 exact-null residual-diffuse two-bank endpoint also remains a distinct zero-first-pivot debt; Theorem 4.1 deliberately does not call a small pivot an exact zero.

Thus the full QFORM conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`. Full continuity remains OPEN.

## 8. Exact computation / regression check

The accompanying checker verifies the B20 constants, monotonicity on `|d|>=1/8`, and the two level-set inequalities used in Lemma 2.1. It terminates with

`QFORM_B19_SEQUENTIAL_TWO_PIVOT_CHECK_PASS`.

The computation is a regression check only; the proof of Lemmas 2.1 and 3.1 and Theorem 4.1 is analytic above.
