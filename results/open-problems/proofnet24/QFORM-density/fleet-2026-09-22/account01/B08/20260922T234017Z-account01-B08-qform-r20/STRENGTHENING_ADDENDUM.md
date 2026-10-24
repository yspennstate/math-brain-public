# r20 strengthening addendum — parametric spectral gate and the `1/81` corollary

This file is an immutable strengthening of `REPORT.md`. It does not alter the status: full QFORM remains open.

## A. Parametric theorem

### `QFORM-SPECTRAL-GATED-PARAMETRIC-SPLIT-v1`

Let `A` satisfy the owner target and fix a cutoff `kappa in (0,1)` such that the actual spectral projection

`P_kappa = 1_{ {|A|>=kappa} }`

has rank exactly three. Write `P_kappa=RR^T` with eigenvector columns, so

`A=R Lambda R^T+C`, `s_min(Lambda)>=1`, `||C||<kappa`.

Choose a leverage threshold `delta>0` and a target surviving Gram floor `b in (0,1)`. Put

`ell_i=(P_kappa)_ii`,
`H={i:ell_i>delta}`, `L=H^c`,
`M=R_L^T R_L`, `beta=lambda_min(M)`,
`m=delta/b`.

Assume

`m<1/3`,
`alpha_m=(1-sqrt(3m))/2`,
`rho_0=alpha_m b-kappa>0`,                              (A.1)

and

`( sqrt(m/alpha_m) + sqrt(6) kappa/rho_0 )^2 < 1/2`.    (A.2)

Then exactly the following exhaustive split is available.

**Diffuse branch:** if `beta>=b`, then every independent cap-one input gives `Q=X^TAX` a continuous `C_0` density with

`||p_Q||_infinity <= 9 sqrt(3e)/(2 rho_0)`.             (A.3)

**Localized branch:** if `beta<b`, then there is a unit `v in Ran P_kappa` satisfying

`||v_H||^2>1-b`,                                         (A.4)

and

`|H|<3/delta`.                                           (A.5)

### Proof

The localized alternative is the exact Gram identity from the newest Claude source. Since

`M=I-R_H^T R_H`,

if `beta<b` choose a unit `u` with `u^TMu=beta` and set `v=Ru`. Then `||v_L||^2=beta<b`, hence (A.4). Since `sum_i ell_i=3` and `ell_i>delta` on `H`, (A.5) follows.

Suppose `beta>=b`. Condition on `H`. Whiten the surviving selected frame:

`W=R_L M^{-1/2}`.

For every `i in L`,

`||w_i||^2 <= ell_i/beta <= delta/b = m`.                (A.6)

Apply account02/B08 `QFORM-DIFFUSE-APPROX-BLOCK-STABILITY-v1` with singleton blocks, `C0=0`, and `E=C[L,L]`. Its parameters obey

`mu<=m`, `tau<kappa`, `1-eta=beta>=b`.

Hence its `alpha` is at least `alpha_m`, its `rho` is strictly larger than `rho_0`, and its gate is bounded by the left side of (A.2). The partner theorem therefore yields (A.3) and continuity. This uses no moments and pays the arbitrary dense spectral remainder inside the original-coordinate theorem. QED.

## B. Stronger clean corollary: cutoff `1/81`

Take

`kappa=1/81`, `delta=1/32`, `b=1/2`.

Then `m=1/16`. If the actual projection

`P=1_{ {|A|>=1/81} }`

has rank exactly three, set `H={P_ii>1/32}`. Either

1. `lambda_min(R_{H^c}^T R_{H^c})>=1/2`, and `Q` has a continuous `C_0` density with

`||p_Q||_infinity < (14580/419) sqrt(3e) <100`;          (B.1)

or

2. some unit `v in Ran P` has `||v_H||^2>1/2`, with `|H|<=95` and therefore `max_{i in H}|v_i|^2>1/190`.

This strictly strengthens the `1/96` numerical corollary in `REPORT.md` by allowing a larger arbitrary low-spectrum tail.

### Exact rational verification of the partner gate

For `m=1/16`,

`alpha_m=(4-sqrt(3))/8`.

Since `sqrt(3)<26/15`,

`alpha_m>17/60`.

Therefore

`rho_0=alpha_m/2-1/81 >17/120-1/81=419/3240`.            (B.2)

For the first gate term,

`m/alpha_m < (1/16)/(17/60)=15/68 <64/289`,

so

`sqrt(m/alpha_m)<8/17`.                                  (B.3)

For the second term, `sqrt(6)<49/20`, and (B.2) gives

`sqrt(6)(1/81)/rho_0
 < (49/20)(40/419)
 =98/419`.                                               (B.4)

Thus the sum of the two square-root terms is less than

`8/17+98/419 = 5018/7123`,

whose square is

`25180324/50737129 <1/2`

(the gap is `376481/101474258`). Hence the partner gate is strictly satisfied.

Finally, (A.3) and (B.2) give

`||p_Q||_infinity
 < 9 sqrt(3e)/(2*(419/3240))
 = (14580/419)sqrt(3e)
 =99.3691029643... <100`.

The full conjecture remains open because the localized branch and all matrices whose `1/81` spectral window has rank larger than three remain unpaid by this theorem.
