# fleet01/B10 r13 improvement — Fejer small-ball sharpening and a 2511 nine-direction constant

Run: `20260924T140550Z-fleet01-B10-fixedmult-r13`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **NEW CONSTANT SHARPENING OF THE NINE-EIGENVALUE CANDIDATE; NOT SELF-AWARDED INDEPENDENT VALIDATION.** The threshold `9` is not new in this report. The unrestricted three-eigenvalue conjecture and multiplicity `8` remain open.

## Theorem `QFORM-NINE-FEJER-2511-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K<infinity`. Let `A=A^T` be arbitrary, `b in R^n`, `c in R`, and suppose

` s_9(A) >= s > 0.`

Then `Q=X^TAX+b^TX+c` has an essentially bounded density and

`boxed: ||p_Q||_infinity < 2511 K^2/s.`

The no-pivot branch has a continuous `C_0` density. Global continuity is not claimed.

The only new analytic input needed beyond the already reconstructed nine-direction compiler is the following elementary replacement for the manuscript's Gamma-based quarter-power constant.

## 1. Fejer-kernel quarter-power concentration with constant 4

### Lemma

Let `S=S^T !=0`,

`R=X^T S X+b^T X+c`,

with independent coordinate densities bounded by one, and let `L=||S||>0`. Then for every `a in R`, `rho>0`,

`boxed: P{|R-a|<rho} <= min{1, 4 (rho/L)^(1/4)}.`

Consequently, if `L>=1`,

`boxed: sup_a E log_+(1/|R-a|) <= 4+8 log 2.`

### Proof

If some `|S_ii|>=L/2`, condition on all other original coordinates. The manuscript's scalar-square inverse-image estimate gives

`P{|R-a|<rho} <= 4 sqrt(rho/L)`.

For `rho<=L`, this is at most `4(rho/L)^(1/4)`; for `rho>L`, the trivial probability bound one is enough.

Assume instead that every `|S_ii|<L/2`. The manuscript's sign-partition argument gives a literal original-coordinate cross block `M` with `||M||>=L/4`. Retaining only its largest singular-value factor in the manuscript's regularized crossing determinant theorem gives, for `t!=0`,

`|phi_R(t)| <= (4*pi*e/(L|t|))^(1/4).`                                      (1.1)

No pointwise rough-law van-der-Corput estimate is used; (1.1) is the already proved integrated product-measure determinant estimate.

For `U>0`, put

`K_U(x) = (sin(Ux)/(Ux))^2`,

with its continuous value one at zero. Under the manuscript Fourier convention,

`hat K_U(t) = (pi/U) (1-|t|/(2U))_+.`                            (1.2)

Take

`U=3/(5 rho)`.

If `|x|<=rho`, then `|Ux|<=3/5`. Since `sin y/y` decreases on `[0,3/5]` and

`sin(3/5) > 3/5-(3/5)^3/6 = 141/250`,

we have

`K_U(x) >= (47/50)^2 = 2209/2500`.

Hence

`1_{|x|<rho} <= (2500/2209) K_U(x).`                             (1.3)

Fourier inversion of the nonnegative Fejer kernel and (1.1) give

```
P{|R-a|<rho}
 <= (2500/2209) (1/(2U))
    int_{-2U}^{2U} (1-|t|/(2U)) |phi_R(t)| dt
 <= C_F (rho/L)^(1/4),
```

where

`C_F = (2500/2209)*(16/21)*2^(3/4)*(5/3)^(1/4)*(4*pi*e)^(1/4).`  (1.4)

Indeed

`int_{-2U}^{2U}(1-|t|/(2U))|t|^(-1/4)dt
 = (32/21)(2U)^(3/4).`

It remains only to check `C_F<4`. Raise (1.4) to the fourth power and use the elementary rational bounds `pi<22/7` and `e<11/4`:

```
C_F^4
 < (2500/2209)^4 (16/21)^4 * 8 * (5/3) * (242/7)
 = 24780800000000000000000 / 97247699666584761861
 = 254.8214516637... <256.
```

The exact margin to `4^4` is

`114611114645699036416 / 97247699666584761861 >0.`

Thus the cross-block branch also satisfies the constant-four estimate, proving the first assertion.

If `L>=1`, layer cake yields

```
E log_+(1/|R-a|)
 = int_0^infinity P{|R-a|<e^(-u)} du
 <= int_0^infinity min(1,4e^(-u/4)) du
 = 4+4 log 4
 = 4+8 log 2.
```

This proves the lemma. QED.

## 2. Exact singular-convolution kernel

For later bookkeeping we also use the sharper exact estimate

`J(d)=int_{-1}^1 |x|^(-1/2)|x-d|^(-1/2) dx
      <= pi+4 log2+2 log_+(1/|d|)`                               (2.1)

for every `d!=0`.

Here is a self-contained derivation. By symmetry take `d>0`. If `0<d<=1`, set `r=d^(-1/2)>=1`. Direct substitutions on the three intervals separated by `0,d` give

`J(d)=2 asinh(r)+pi+2 acosh(r).`

Moreover

```
asinh(r)+acosh(r)-2log r
 = log[(1+sqrt(1+r^(-2)))(1+sqrt(1-r^(-2)))]
 <= log4,
```

because `sqrt(1+x)+sqrt(1-x)<=2` and `sqrt(1-x^2)<=1` for `0<=x<=1`. This gives (2.1). If `d>=1`,

`J(d)=2 asinh(d^(-1/2))+2 asin(d^(-1/2))`

is maximized at `d=1` and is below `pi+4log2`, again giving (2.1).

## 3. New pivot half-potential constant

Keep the manuscript's `eta=1/100`. Suppose a quadratic polynomial has at least two unit spectral directions and has an `eta`-pivot.

### Scalar pivot

At a scalar pivot, the Schur complement has at least one unit spectral direction. Combining the manuscript conditional square profile with (2.1) and the new logarithmic-potential lemma gives the truncated half potential

```
H_scalar
 <= 10 [pi+4log2 + 2(4+8log2)]
 = 10 [pi+8+20log2].
```

Use the exact rational certificates

`pi<22/7`,

`log2 < 1733/2500`.

For the logarithm, the positive exponential series through order six satisfies

`sum_{k=0}^6 (1733/2500)^k/k! -2
 =15635577084913721569 / 175781250000000000000000 >0`,

so indeed `e^(1733/2500)>2`. Therefore

`H_scalar < 43762/175 =250.0685714...`                           (3.1)

and adding the region `|Q-a|>1`, on which the half kernel is at most one, gives

`sup_a E|Q-a|^(-1/2) < 43937/175 =251.0685714...`.              (3.2)

### Definite and indefinite pair pivots

The definite-pair branch of the pinned manuscript is already much smaller: its truncated half potential is `<160`, so the full half potential is `<161`.

For the indefinite-pair branch I independently checked the completed optimized physical-coordinate tail split in the current fleet03/B10 audit: with split parameter `q=2/9`, each hyperbola branch has the improved tail/Jacobian constant leading to

`H_ind <242`,

hence full half potential `<243`. This proof uses only original-coordinate density caps and the exact hyperbolic Jacobian; no rotated-coordinate independence is asserted.

Consequently every pivot under the two-unit-direction hypothesis satisfies the uniform full bound

`boxed: sup_a E|Q-a|^(-1/2) < 43937/175.`                        (3.3)

The scalar branch controls the maximum.

## 4. Nine eigenvalues with constant 2511

Normalize `K=s=1` and retain `eta=1/100`, `kappa=1/80^2`.

### No pivot

The audited baseline spectral-to-volume proposition at order three gives

`V_3(A)>=kappa^3`

from `s_9(A)>=1`. A fair original-coordinate cut therefore supplies a literal crossing block with

`E_3(M)>=4^(-3) kappa^3`,

so

`E_3(M)^(-1/6)<=160`.

The independently reconstructed marginal-free order-three grouped product-Fourier receiver gives

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6) <2400`,

with `C_3=3 sqrt(2)e(9/2)^(1/6)<14.819`. This branch has a continuous `C_0` density.

### Scalar pivot

If `|A_hh|>=eta`, its Schur complement has at least eight unit spectral directions.

- If that Schur complement has an `eta`-pivot, apply (3.3).
- If it has no pivot, then it has at least five unit directions. The baseline order-two spectral-to-volume proposition, a fair cut, and the already reconstructed marginal-free order-two half-Riesz receiver give full half potential `<153`, which is smaller than (3.3).

Thus in every scalar-pivot subcase the Schur remainder has full half potential below `43937/175`. The outer conditional square profile costs `eta^(-1/2)=10`, so

```
||p_Q||_infinity
 < 10*(43937/175)
 = 87874/35
 = 2510.685714... <2511.
```

The exact final margin is

`2511-87874/35 =11/35 >0.`                                      (4.1)

### Pair pivots

A definite physical pair gives `<10*pi<32`. An indefinite physical pair leaves at least seven unit Schur directions, hence a unit operator-norm direction; the manuscript's hyperbolic/log-potential argument gives a bound `<251`. Both are below (4.1).

Therefore the normalized theorem has density `<2511`. For general `K,s`, put `Y=KX` and

`Q=(s/K^2) Q_tilde`,

where the quadratic matrix of `Q_tilde` is `A/s` and its coordinate laws have caps one. This gives

`boxed: ||p_Q||_infinity <2511 K^2/s.`

No input moment, support, smoothness, log-concavity, sign, exact-rank, leverage, connected-support, or diagonal-basis assumption was introduced.

## 5. Why this does not yet lower nine to eight

I checked the current exact `s_8` terminal reduction. In the no-pivot chamber, either `V_3>=kappa^3` and the preceding density receiver pays immediately, or an order-two sampled seed produces a quantitative overlap-one / two-sided collar. The completion has

`rank R<=6`, `rank R[L,L]<=2`.

Under only `s_8>=1`, rank subtraction forces exactly two large diagonal residual coordinates, which is compatible with an invertible `2x2` block of rank two. The finite `4x4` example in the sibling B10 audit shows the analogous global/restricted rank constants can be simultaneously sharp; therefore changing only the rank bookkeeping cannot close multiplicity eight.

There is a useful but insufficient special identity: if three disjoint two-coordinate banks `S,H,T` have **no direct endpoint coupling** and their two chain blocks `B=A[S,H]`, `C=A[H,T]` are invertible, conditioning and two-dimensional Plancherel give an integrable `t^{-2}` envelope proportional to `|det B det C|^{-1/2}`. The actual terminal collar, however, comes with a nonzero direct seed block `A[S,T]`; that bilinear endpoint phase couples the two endpoint Fourier transforms and the preceding factorization is no longer valid for arbitrary fragmented rough laws. Dropping that phase by absolute values loses the second power. I therefore do not claim a collar receiver or an eight-direction theorem from this observation.

The remaining exact obligation is a genuinely product-preserving three-bank/collar receiver that tolerates the direct endpoint coupling without paying a reciprocal tiny seed determinant.

## 6. Review state

- Baseline seventeen-eigenvalue source: PASS in this run's independent full audit.
- Nine-eigenvalue threshold: already has multiple independent PASS reconstructions in the repository; this report does not reassign owner-level release status.
- New constant `2511`: **new in this run and pending independent review**.
- Multiplicity eight: **OPEN**.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity for the nine-eigenvalue theorem: **OPEN/not claimed**; the no-pivot Fourier branch is continuous.
