SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-24T13:33:00Z.
attacking: audit the fixed-multiplicity candidate and combine the new order-three product-Fourier receiver with sharper definite/hyperbolic pivot constants to lower the proved threshold and constant.

# fleet03/B13 improvement r4 — nine eigenvalues with constant 3078

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Run: `20260924T133300Z-fleet03-B13-fixedmult-audit-r4`.
Pinned baseline source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
Fresh source tree used for this run: `yspennstate/math-open-problems@d2ae3d3878703809e7d7b70cf47f0db7a6740553` before this write.

Status: **proved candidate improvement, not a claim about the unrestricted three-eigenvalue conjecture and not a self-awarded independent-validation certificate.**

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K<infinity`. Let `A=A^T` be arbitrary, let `b in R^n`, `c in R`, and assume

` s_9(A) >= s > 0.`

Then `Q=X^T A X+b^T X+c` has an essentially bounded density and

`||p_Q||_infinity < 3078 K^2/s.`

The no-pivot branch has a continuous `C_0` density. Global continuity is not claimed by this argument.

The proof preserves arbitrary dimension, signature, the remaining spectrum, affine terms, and arbitrary rough independent coordinate laws. It never rotates the random coordinates.

## 1. New order-three/order-two product receiver used

I checked the complete grouped product-Fourier argument of fleet03/B04 at

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet03/B04/20260924T121940Z-fleet03-B04-fixedmult-audit-r1/REPORT.md`.

The interfaces needed here are:

1. For every literal original-coordinate cross block `M`,

`||p_Q||_infinity <= C3 E_3(M)^(-1/6),`

where

`C3 = 3 sqrt(2) e (9/2)^(1/6) = 14.818337662843...`.

This conclusion keeps arbitrary same-bank quadratic and affine phases inside complex pushforwards and has a continuous `C_0` density.

2. For every literal original-coordinate cross block `M`,

`sup_a E |Q-a|^(-1/2) <= C2 E_2(M)^(-1/8),`

where

`C2 = 8 sqrt(e) 2^(-1/8) = 12.095072570796...`.

This is a half-potential conclusion, not a rank-two density assertion.

The weighted-subset proof was rechecked at the equation level. If the inclusion marginals are `alpha_i<=1/2`, weighted Holder uses the functions with powers `1/alpha_i`; the map `D -> (M_JD,(<c_i,D>)_{i in T})` has Gram determinant `S^2 det(C_T C_T^T)`; the baseline product-projection lemma supplies the Jacobian factor; and the scalar Fourier-power estimate at `p=1/alpha_i` supplies

`int |psi_i(2t(y+u))|^(1/alpha_i) dy <= pi sqrt(2e alpha_i)/|t|.`

The determinant-weighted geometric mean is exactly

`Z_ell^(-1/2) exp(H(w)/2)`,

and entropy subadditivity for the uniformly ordered sampled `ell`-subset gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!).`

Thus the compiler's exponent `|t|^{-(k+ell)/2}` and its constants are consistent. The promotion identities at orders three and two are ordinary Gram--Schmidt determinant identities, so the marginal-free receivers above follow without choosing a small local minor.

## 2. Sharpened B13 pivot estimate

Use the baseline `eta=1/100`. My preceding B13 audit proved the sharper singular-kernel and hyperbolic estimates

`J(d) < 7+2 log_+(1/|d|),`

`P{|R-a|<rho} <= min{1,(9/2)(rho/L)^(1/4)},`

and, for an indefinite physical pair with `D=|det B|`,

`p_q(z) <= D^(-1/2)[(15/2)log 2 + log_+(16 sqrt(D)/|z-v|)].`

The quarter-power estimate yields

`L0* := sup_a E log_+(1/|R-a|) <= 4+4 log(9/2)`

whenever the surviving quadratic matrix has operator norm at least one.

### 2.1 Scalar pivot

The baseline conditional square profile and the sharper `J` bound give

`H(Q) <= 10 [7+2L0*] = 10[15+8 log(9/2)] < 278.`

The last inequality is elementary; for example `log(9/2)<8/5` because the positive Taylor partial sum of `e^(8/5)` exceeds `9/2`.

### 2.2 Definite pair

The exact two-dimensional polar Jacobian gives

`H(Q) <= 40 pi < 126 < 307.`

No independence of rotated coordinates is used: the rotation occurs only in the deterministic integral after conditioning on the two original coordinates.

### 2.3 Indefinite pair

Combining the exact hyperbolic Jacobian with the shifted logarithmic-kernel integral gives

`H(Q) <= D^(-1/2)[8+30 log2+4 log(16 sqrt D)]`

for every `D>=1/100`; the `log_+` can be removed because `16 sqrt D >=8/5>1`.

Put `y=sqrt D>=1/10`. The function

`F(y)=[8+30 log2+4 log(16y)]/y`

is decreasing on this range, because its derivative has numerator

`4-[8+30 log2+4 log(16y)]<0`.

Hence the maximum is at `y=1/10`:

`H(Q) <= 10[8+30 log2+4 log(8/5)].`

For a fully rational certification of the numerical comparison, put

`r1=13863/20000=0.69315`, `r2=117501/250000=0.470004`.

The seventh positive Taylor partial sums satisfy

`sum_{k=0}^7 r1^k/k! > 2`,

`sum_{k=0}^7 r2^k/k! > 8/5`.

Therefore `log2<r1` and `log(8/5)<r2`. Moreover

`30 r1+4 r2 = 22.674516 < 22.675`.

Consequently

`H(Q) < 10(8+22.675)=306.75.`

All three pivot types therefore satisfy the uniform strengthened statement

`boxed: H(Q)<306.75.`

This is the only new numerical input needed below.

## 3. Nine large eigenvalues

Normalize first to `K=s=1`.

### 3.1 No coordinate pivot

If `A` has no `eta`-pivot and `s_9(A)>=1`, the pinned baseline spectral-to-volume proposition at order three gives

`V_3(A)>=kappa^3`, `kappa=1/80^2`.

A fair original-coordinate cut gives a literal cross block `M` with

`E_3(M)>=4^(-3) kappa^3`,

so

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160.`

The order-three product receiver yields

`||p_Q||_infinity <=160 C3 =2370.93402605488... < 2371.`

This branch has a continuous `C_0` density.

### 3.2 Scalar pivot

Suppose `|A_hh|>=eta`. Complete the square in the literal original coordinate `X_h`. The Schur complement `S` has at least eight singular/eigenvalue magnitudes at least one by the baseline Schur-count lemma.

If `S` has an `eta`-pivot, the strengthened pivot bound above gives its truncated half potential `<306.75`; on `|R-a|>1`, the kernel `|R-a|^(-1/2)` is at most one. Hence

`sup_a E|R-a|^(-1/2) < 307.75.`

If `S` has no pivot, then in particular `s_5(S)>=1`. The baseline order-two spectral-to-volume proposition and a fair cut give

`E_2(M_S)>=4^(-2)kappa^2`,

and the marginal-free order-two receiver gives

`sup_a E|R-a|^(-1/2)
 <= C2 sqrt(160)
 =152.99191115498... <153.`

Thus in every scalar-pivot subcase the full Schur half potential is `<307.75`. The conditional square profile therefore gives

`||p_Q||_infinity < eta^(-1/2) 307.75 =3077.5 <3078.`

### 3.3 Pair pivots

If a definite physical pair has determinant magnitude at least `eta`, the baseline two-dimensional bound gives

`||p_Q||_infinity <= pi/sqrt(eta)=10 pi<32.`

If an indefinite physical pair has determinant magnitude at least `eta`, its Schur complement keeps at least seven eigenvalue magnitudes at least one, hence operator norm at least one. The sharpened hyperbolic envelope and `L0*` give a finite bound far below 3078 (the direct worst case is below 157). Thus the pair branches do not control the final constant.

Combining the three exhaustive branches proves the normalized theorem.

### 3.4 Scaling

For general `K,s`, put `Y=KX`. Then the coordinates of `Y` have densities at most one and

`Q=(s/K^2) Q_tilde`,

where

`Q_tilde=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`.

Since `s_9(A/s)>=1`, the normalized theorem gives

`||p_Q||_infinity <3078 K^2/s.`

No input moment, support, regularity, log-concavity or diagonal-basis assumption was introduced.

## 4. Designated fleet04/B13 result applied to an actual inequality

The completed fleet04/B13 no-attainment purification theorem is at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T231352Z-fleet04-B13-rough-geometric-transfer-r5/REPORT.md`.

For

`D={f: 0<=f<=1, integral f=1}`

it proves, without any optimizer assumption, that for every measurable `0<=K(x)<=1`,

`sup_{f_i in D} int K(x) prod_i f_i(x_i) dx`

is exactly the supremum over bounded finite-union sets `E_i` of measure one of the integral of `K` over `prod_i E_i`.

Apply this with the actual slab kernel

`K_J(x)=1_{ {x^T A x+b^T x+c in J} }`.

The theorem above therefore yields the exact extremal-product geometric inequality

`boxed:
 sup_{f_i in D} P_f{Q in J}
 = sup_{|E_i|=1, E_i bounded finite unions}
   |{x in prod_i E_i: Q(x) in J}|
 < 3078 |J|`

whenever `s_9(A)>=1`.

This is a zero-loss application of the designated partner result to an actual inequality. It does **not** say that one interval, a centered interval, bounded diameter, or any fixed fragment count is extremal.

## 5. Why this run stops at nine, not eight

The newly proved fleet03/B08 terminal theorem for `s_8(A)>=1` shows exactly where the current interpolation mechanism saturates if the order-three crossing volume fails. In that chamber the only bad sampled ratio is `r=2`; after completion,

`rank R<=6`, `rank R[L,L]<=2`, `s_2(D)>=77/80`, `s_3(D)<=519/1400`, and `s_6(R)>=1657/2800`.

Moreover three disjoint physical two-banks `S,H,T` satisfy

`|det A[H,T]| |det A[S,H]| >= (857233/980000)|det A[S,T]|`.

This does not yet give an absolute lower bound for one pair determinant because the seed `|det A[S,T]|` may be arbitrarily small. An order-two indefinite endpoint alone cannot give a bounded density because the logarithmic singularity is real. Thus a valid `9 -> 8` theorem still needs a new three-bank/cycle receiver that uses the determinant ratio before paying any reciprocal local minor, or another genuinely different structural argument.

## 6. Review status and limits

- Baseline 17-eigenvalue manuscript: no new fatal defect found in this run; see the sibling audit artifact for line-by-line statuses.
- Candidate nine-eigenvalue theorem: **proved in this report by combining the audited baseline with the checked grouped receiver and the B13 pivot improvement.** It remains subject to the owner's independent-review gate; this report does not award that status.
- New numerical constant: `3078 K^2/s` under `s_9(A)>=s`.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity under the nine-eigenvalue theorem: **OPEN/not claimed**; the no-pivot Fourier branch is continuous.
- Native brain ingestion: **WITHOUT_VERIFIED_BRAIN**; repository retrieval/use is separate from receiver-memory ingestion.
