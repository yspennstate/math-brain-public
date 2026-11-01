SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-23T08:31:31Z.
attacking: translation-uniform fractional-trace synthesis and a nested two-pivot bordered-volume compiler, applying fleet02/B13 r23 inside a second original-coordinate square.

# fleet01/B13 auto18 — singular-kernel extremal reduction and nested bordered-four-volume compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: extremal product laws / STRUCTURE  
Owner control observed: revision `2026-09-22.15`; QFORM only  
Status: **ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING TARGET-LEVEL DICHOTOMY / FULL_QFORM_OPEN / CONTINUITY_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full target remains the arbitrary-dimensional statement for independent original-coordinate real variables with densities `0<=f_i<=1` and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one. No moments, centering, interval support, bounded diameter, fixed fragment count, post-rotation independence, or continuity hypothesis is introduced.

Live corrections respected: no law-uniform pointwise quadratic oscillatory decay; no independence after rotations; no substitution of a projection-density cap for an indefinite quadratic pushforward; no arbitrary-joint coarea L-infinity claim; no positive conditional-projection-moment shortcut; and no deletion of small coefficients on translated/fragmented supports.

Completed designated partner actually applied below: `fleet02/B13` r23, canonical mathematics `yspennstate/math-open-problems@892bfe36756e09cbaff3f05070f7a3e20fea0fd1`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T040105Z-fleet02-B13-extremal-r23/REPORT.md`. Its theorem `QFORM-SCALAR-E2-LINF-OR-TRIHUB-v1` is inserted at an actual inner-Schur inequality in Section 4.

## 1. Exact extremal-product reduction extends to singular positive kernels

Let

`F={f:R-> [0,1] measurable : int f=1}`.

The previous B13 bounded-kernel front end gives, for every bounded nonnegative measurable `K` on `R^n`,

`sup_{f_1,...,f_n in F} int K(x) prod_i f_i(x_i) dx
 = sup_{|E_1|=...=|E_n|=1} int_{prod_i E_i} K(x) dx`.          (1.1)

The first new observation is that boundedness of `K` is unnecessary.

### Theorem 1.1 — `QFORM-EXTREMAL-PRODUCT-POSITIVE-KERNEL-v1`

For every measurable `K:R^n->[0,infinity]`,

`boxed:
 sup_{f_i in F} int K prod_i f_i
 = sup_{|E_i|=1} int_{prod_i E_i} K.
`                                                                     (1.2)

Both sides may be infinite.

### Proof

Put `K_m=min(K,m)`. By (1.1), for each `m`,

`S_m:=sup_{f_i in F} int K_m prod_i f_i
    =sup_{|E_i|=1} int_{prod E_i} K_m=:T_m`.                         (1.3)

For any fixed product density, monotone convergence gives

`int K prod_i f_i=sup_m int K_m prod_i f_i <=sup_m S_m`,             (1.4)

so the left side of (1.2) is at most `sup_m S_m`. The reverse inequality is immediate because `K_m<=K`. Exactly the same argument on product indicators gives the right side equal to `sup_m T_m`. Since `S_m=T_m`, (1.2) follows. QED.

This matters because the positive half-Riesz kernels used after physical square completion are singular:

`K_t(x)=|Q(x)-t|^{-1/2}`.                                           (1.5)

Thus the extremal reduction is available directly at the singular potential level, rather than only after an L-infinity density has already been proved.

### Strict violations still admit bounded finite-union witnesses

If a strict inequality against a finite constant is witnessed on either side of (1.2), first choose `m` so that the same strict gap survives for `K_m`. The bounded-kernel reduction supplies measurable unit-measure sets `E_i`. Approximate each `E_i` in symmetric difference by a bounded finite union of intervals and adjust its measure to exactly one by adding/removing a sufficiently small interval. If the resulting sets are `F_i`, then

`| int_{prod E_i} K_m-int_{prod F_i} K_m |
 <= m |(prod E_i) Delta (prod F_i)|
 <= m sum_i |E_i Delta F_i|`.                                      (1.6)

Hence bounded finite unions suffice for every strict violation, with no uniform bound on fragment count. There is still no reduction to one interval or to a centered uniform law.

## 2. Translation-uniform fractional-trace synthesis

The next lemma isolates the only exponent threshold needed to turn a small-ball estimate into the half-Riesz quantity naturally produced by one outer physical square.

### Lemma 2.1 — `QFORM-FRACTIONAL-TRACE-SMALLBALL-v1`

Let `R` be any real random variable. Suppose that for some `alpha>1/2` and `A>0`, uniformly in `t in R` and `r>0`,

`P(|R-t|<r) <= min(1,A r^alpha)`.                                   (2.1)

Then

`boxed:
 sup_t E|R-t|^{-1/2}
 <= [2 alpha/(2 alpha-1)] A^(1/(2 alpha)).
`                                                                     (2.2)

### Proof

For `z!=0`,

`|z|^{-1/2}=(1/2) int_0^infinity r^(-3/2) 1_{|z|<r} dr`.             (2.3)

Tonelli and (2.1), with `r_0=A^(-1/alpha)`, give

`E|R-t|^-1/2
 <=(1/2)[ A int_0^{r_0} r^{alpha-3/2}dr
             +int_{r_0}^infinity r^-3/2 dr ]
 = [2alpha/(2alpha-1)] A^(1/(2alpha)).`                              (2.4)

QED.

At `alpha=1`, if `R` has density cap `M`, then `A=2M`, and (2.2) becomes

`sup_t E|R-t|^-1/2 <=2 sqrt(2M)`,                                   (2.5)

exactly the sharp cap-to-half-Riesz estimate from the preceding B13 run.

## 3. Two nested original-coordinate pivots

Fix two distinct original coordinates `k,i`. Write

`d=A_kk`, and assume `d!=0`.                                        (3.1)

After pivoting only the physical coordinate `k`, let

`S=A[-k,-k]-A[-k,k]A[k,-k]/d`.                                    (3.2)

Assume that the next physical diagonal pivot is

`a=S_ii!=0`.                                                        (3.3)

Let

`K={k,i}`, `B=A[K,K]`, `Delta=det B`.                              (3.4)

The scalar determinant identity gives

`Delta=d a`,                                                        (3.5)

so (3.1)-(3.3) are equivalent to `d!=0` and `Delta!=0`.

Let `T` be the Schur complement of the coordinate `i` inside `S`. By associativity of Schur complements, `T` is exactly the Schur complement of the original physical principal block `B=A[K,K]` inside `A`.

Choose disjoint original-coordinate banks `I,J subset K^c` and set

`M=T[I,J]`,
`E=e_2(M^T M)=sum_{|P|=|Q|=2} det T[P,Q]^2`.                       (3.6)

All coordinates used here are physical/original coordinates. No rotation is applied to the source law.

## 4. Designated partner theorem inserted into the outer square

Let

`R=X_{-k}^T S X_{-k}`.                                               (4.1)

The variables `X_{-k}` are still independent with density caps one. Apply the designated completed `fleet02/B13` r23 theorem to the actual scalar pivot `a=S_ii` and actual inner-Schur cross block `M=T[I,J]`.

Its `QFORM-SCALAR-E2-LINF-OR-TRIHUB-v1` gives the dichotomy:

**Paid branch**

`||p_R||_infinity
 <= C_0 |a|^-1/2 E^-1/8`,
`C_0=29.922421174319`;                                               (4.2)

or **structural branch**, in which more than half of the natural squared `2x2`-minor mass `E` is jointly incident to at most three physical row hubs and at most three physical column hubs of `M`.

Now return to the outer original coordinate `X_k`. Physical square completion gives

`Q=X^T A X
 =d (X_k+d^-1 A[k,-k]X_-k)^2+R`.                                  (4.3)

Conditional on `X_-k`, the translated scalar in parentheses has a density bounded by one. Hence the conditional density of its `d`-weighted square is bounded by

`|d|^-1/2 |u|^-1/2`                                                  (4.4)

on the appropriate sign half-line. Therefore, without asserting independence between the translated square and `R`,

`p_Q(t)<=|d|^-1/2 E|t-R|^-1/2`.                                    (4.5)

In the partner paid branch, (2.5) and (4.2) yield

`||p_Q||_infinity
 <=2 sqrt(2) |d|^-1/2 ||p_R||_infinity^1/2
 <=C_1 |d|^-1/2 |a|^-1/4 E^-1/16`,                                (4.6)

where

`C_1=2 sqrt(2 C_0)=15.471889651705508 <15.472`.                     (4.7)

This is `QFORM-NESTED-PIVOT-E2-FRACTIONAL-TRACE-v1`.

The exponent gain is the useful point: the inner `E_2` estimate need only be square-rooted by the outer positive half-Riesz trace. The argument is dependence-safe because the outer square is treated conditionally in the original coordinate, while the inner partner theorem acts on the unrotated independent remainder.

## 5. Exact bordered-four-volume identity

For every `P subset I`, `Q subset J` with `|P|=|Q|=2`, the block determinant formula for the invertible physical block `B` gives

`det A[K union P,K union Q]
 =det(B) det T[P,Q]
 =Delta det T[P,Q]`.                                                 (5.1)

Define the selected-cut anchored four-volume

`V_{4,K}(I,J)
 :=sum_{|P|=|Q|=2} det A[K union P,K union Q]^2`.                    (5.2)

Then exactly

`boxed: V_{4,K}(I,J)=Delta^2 E.`                                    (5.3)

Combining (3.5), (4.6), and (5.3), the paid branch becomes

`boxed:
 ||p_Q||_infinity
 <15.472 |d|^-1/4 |Delta|^-1/8 V_{4,K}(I,J)^-1/16
 =15.472 (|d|^4 |Delta|^2 V_{4,K}(I,J))^-1/16.
`                                                                     (5.4)

This is a target-level physical certificate. It involves only original-matrix anchored minors and one explicitly identified original diagonal entry.

## 6. Random-cut globalization and a quantitative hub alternative

Define the total disjoint anchored four-volume

`Omega_{4,K}^perp(A)
 :=sum_{P,Q subset K^c, |P|=|Q|=2, P cap Q=empty}
      det A[K union P,K union Q]^2`.                                (6.1)

Color every coordinate in `K^c` independently red/blue with probability `1/2` and take `I=red`, `J=blue`. Every ordered disjoint pair `(P,Q)` with two coordinates in each is captured with probability `2^-4=1/16`. Therefore some original-coordinate cut satisfies

`V_{4,K}(I,J)>=Omega_{4,K}^perp(A)/16`.                             (6.2)

Apply the designated partner dichotomy on that cut.

### Theorem 6.1 — `QFORM-PAIR-BORDER4-LINF-OR-TRIHUB-v1`

Assume `A_kk!=0` and `Delta=det A[{k,i},{k,i}]!=0`. Then for every independent cap-one product law, either

`boxed:
 ||p_Q||_infinity
 <18.400 (|A_kk|^4 |Delta|^2 Omega_{4,K}^perp(A))^-1/16,
`                                                                     (6.3)

or, on a cut satisfying (6.2), at most three physical row hubs and at most three physical column hubs carry more than half of the selected inner-Schur `E_2` mass. In original bordered-minor currency that hub packet carries strictly more than

`Omega_{4,K}^perp(A)/32`                                            (6.4)

of anchored squared determinant mass: multiply the partner `>E/2` statement by `Delta^2` and use (6.2).

The numerical constant is

`15.471889651705508 *16^(1/16)
 =18.399281256345162 <18.400`.                                      (6.5)

Thus a nonsingular two-pivot physical anchor plus diffuse disjoint anchored order-four volume is paid; if it does not pay, the relevant order-four volume is quantitatively localized onto a finite physical hub packet.

## 7. Exact geometric product-set form

By Theorem 1.1 (indeed already by the bounded slab specialization), every paid inequality above has zero-loss geometric form. For arbitrary measurable `E_l subset R` with `|E_l|=1` and every interval `J`, the paid branch of Theorem 6.1 gives

`boxed:
 |{x in prod_l E_l : x^T A x in J}|
 <18.400 (|A_kk|^4 |Delta|^2 Omega_{4,K}^perp(A))^-1/16 |J|.
`                                                                     (7.1)

There is no single-interval, centered-uniform, bounded-diameter, or fixed-fragment hypothesis. The singular-kernel extension in Section 1 additionally shows that the positive half-Riesz potentials themselves may be extremized over arbitrary unit-measure product indicators without first regularizing the kernel.

## 8. What this does and does not close

This run does **not** prove full QFORM. The bare spectral hypothesis does not presently force a physical pair `K` for which the quantity in (6.3) is universally bounded below. Nor may the finite hub alternative be conditioned away, because that could discard the global third-curvature resource.

The new first unpaid implication is

`QFORM-PAIR-BORDER4-TRIHUB-THIRD-CURVATURE-CLOSURE-v1`:

Starting from the structural branch of Theorem 6.1, combine the `>Omega/32` anchored four-volume carried by at most three row and three column hubs with the third large spectral direction, without conditioning away the hubs and without perturbatively deleting the remaining coefficients. A successful closure should force an already-paid physical square/pair, grouped-bank, null-Schur mixed-edge, or diffuse spectral-window certificate. Along a divergent slab sequence, every non-hub pair anchor must instead have the scale `|A_kk|^4|Delta|^2 Omega_{4,K}^perp` collapse at the corresponding sixteenth-power rate.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Continuity of a density representative: **separate OPEN question**.  
Independent end-to-end review status of the new auto18 lemmas: **not yet performed**.
