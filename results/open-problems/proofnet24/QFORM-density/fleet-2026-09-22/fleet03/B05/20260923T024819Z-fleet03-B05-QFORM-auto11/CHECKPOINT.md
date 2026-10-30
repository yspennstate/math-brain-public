# fleet03/B05 auto11 — early substantive checkpoint

Run: `20260923T024819Z-fleet03-B05-QFORM-auto11`

Status: `SUBSTANTIVE_CHECKPOINT / SUPPORTING ANALYTIC BRIDGE / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

The current differentiated B05 obligation is the uncovered indefinite two-sheet curved integral. The calculation below does not reprove the ruled one-sheet or semidefinite cases. It extends the completed physical-pair logarithmic coarea theorem so that an indefinite two-coordinate saddle can be smoothed by any residual `L^p` density with `p>=2`, even when the completed pair translations depend arbitrarily on the same variables generating the residual.

## 1. Pair-log small-ball interpolation

Let `U,V` be two original independent cap-one coordinates, let `Z` denote all remaining original coordinates, and suppose that after completing an invertible indefinite physical pair `B` one has

```
Q=((U,V)+m(Z))^T B ((U,V)+m(Z))+R(Z),
D=|det B|,
kappa=sigma_min(B)>0.
```

The completed pair-log theorem gives, for every `r>0` and a.e. output `t`,

```
p_Q(t) <= 2 sqrt(2)/r
 +D^(-1/2) E log_+(2 r^2/(kappa |t-R|)).              (1)
```

Assume more generally that for some `beta in [1/2,1]` and `H>0`,

```
sup_t P(|R-t|<rho) <= min(1,H rho^beta),  rho>0.      (2)
```

For `a>0`, layer cake and `min(1,x)<=x^theta` with

```
theta=1/(2 beta) in [1/2,1]
```

give

```
E log_+(a/|t-R|)
 = integral_0^infinity P(|t-R|<a e^(-v)) dv
 <= integral_0^infinity (H a^beta e^(-beta v))^theta dv
 = 2 H^(1/(2 beta)) sqrt(a).                              (3)
```

Using `a=2r^2/kappa` in (1),

```
p_Q(t)
 <= 2 sqrt(2)/r
   +2 sqrt(2) H^(1/(2 beta)) r / sqrt(D kappa).            (4)
```

Optimizing in `r` yields the dimension-free bound

```
boxed:
||p_Q||_infinity
 <= 4 sqrt(2) H^(1/(4 beta)) (D kappa)^(-1/4).             (5)
```

This recovers the completed square-root small-ball theorem exactly at `beta=1/2` and exposes the same logarithmic saddle as a receiver for stronger residual smoothing.

## 2. L^p corollary

If `R` has density `p_R in L^p`, `2<=p<=infinity`, Holder gives

```
P(|R-t|<rho)
 <= (2rho)^(1-1/p) ||p_R||_p.
```

Putting `beta=1-1/p` in (5), including the `p=infinity` limit, gives

```
boxed:
||p_Q||_infinity
 <= 2^(11/4) (D kappa)^(-1/4)
    ||p_R||_p^[p/(4(p-1))].                                (6)
```

For `p=infinity` the exponent is interpreted as `1/4`. No independence between `R(Z)` and the pair translation `m(Z)` is used.

## 3. Actual application to same-side curved residuals

The completed `QFORM-E3-CROSS-L3-v1` theorem gives, for a residual original-coordinate cross block `H_0` with arbitrary same-side quadratic/affine curvature,

```
F=E_3(H_0)>0,
||p_R||_3 <= (9e/2)^(2/3) F^(-1/9).
```

Substituting this at the actual `p=3` inequality (6) gives

```
boxed:
||p_Q||_infinity
 <= 4 sqrt(6) e^(1/4)
    (D kappa)^(-1/4) F^(-1/24)
 < 12.581 (D kappa)^(-1/4) F^(-1/24).                      (7)
```

Thus arbitrary same-side curvature in the completed remainder is not itself an obstruction once that remainder retains aggregate third exterior cross-curvature.

## 4. Actual application of the newest volume/tail receiver

The required current volume-stability continuation proves, under its stated leverage/tail gate for a residual cross block `M`,

```
G=s_1(M)^2 s_2(M)^2 T_2,
T_2=sum_(j>=3)s_j(M)^2,
||p_R||_infinity <= (9 sqrt(3)e/2) G^(-1/6),
```

with arbitrary same-side and outside curvature retained. Applying (6) with `p=infinity` gives

```
boxed:
||p_Q||_infinity
 <= 2^(11/4)(9 sqrt(3)e/2)^(1/4)
    (D kappa)^(-1/4) G^(-1/24)
 < 14.433 (D kappa)^(-1/4) G^(-1/24).                      (8)
```

Likewise its baseline residual estimate `||p_R||_infinity<23/a` yields

```
||p_Q||_infinity
 < 2^(11/4) 23^(1/4)
   (D kappa)^(-1/4) a^(-1/4)
 <14.733 (D kappa a)^(-1/4).                               (9)
```

Equations (8)-(9) are an equation-level use of the newest required source, not a copied citation.

## 5. Precise remaining factor

This bridge does **not** complete N3 or the full conjecture. To apply it exhaustively one still needs a product-coordinate structural implication of the following form:

`QFORM-SCHUR-STABLE-PAIR-OR-AGGREGATE-TAIL-v1`: from an unpaid indefinite/no-pivot state, either find an invertible indefinite physical pair with `D*kappa` quantitatively compatible with a residual E3 or volume-tail resource **after the exact pair Schur completion**, or route the failure to an already-paid grouped-bank/hub mechanism.

A lower bound on curvature before pair completion is insufficient by itself: Schur completion is a low-rank but not value-small matrix update, and arbitrary product inputs are unbounded. No small-coefficient perturbation principle is used here.

Continuity is not claimed by (5)-(9); only an essentially bounded density is proved in this bridge. The full target remains open.
