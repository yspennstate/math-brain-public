# account02/B15 — regularity endpoint barriers and threshold-nine revalidation

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T150156Z-account02-B15-fixedmult-auto11`  
Pinned baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **new B15 counterexample/regularity sharpening; threshold nine remains the lowest complete replacement proof checked here. Multiplicity eight and unrestricted three-eigenvalue QFORM remain OPEN.**

## 1. Zero-loss rough passage is an interval statement, not a continuity theorem

Let the original-coordinate joint density be `F=prod_i f_i`, with every `f_i` a probability density bounded by one. For a probability approximate identity define `f_i^eps=f_i*rho_eps` and `F_eps=prod_i f_i^eps`. Then

`0<=f_i^eps<=1`, `int f_i^eps=1`, and

`||F_eps-F||_1 <= sum_i ||f_i^eps-f_i||_1 ->0`.

For any deterministic Borel map `q`, in particular a quadratic polynomial,

`sup_B |q_#(F_eps dx)(B)-q_#(F dx)(B)| <= ||F_eps-F||_1`.

Therefore a smoothing-uniform interval estimate

`q_#(F_eps dx)(I) <= C |I|`

passes with the **same** `C` to the rough law. This proves absolute continuity and an essential height bound. It does not prove continuity of a density representative.

### Quadratic counterexample to continuity transfer

Take a single original coordinate `X~Unif[1,2]`, whose density cap is one, and `Q=X^2`. Then

`p_Q(z)=1_[1,4](z)/(2 sqrt z)`

(up to endpoint values). Hence `||p_Q||_infinity=1/2`, but there is no continuous representative: the left limit at `z=1` is zero and the right limit is `1/2`.

Let `rho_eps` be a smooth compactly supported probability mollifier and `f_eps=1_[1,2]*rho_eps`. For small `eps`, `f_eps` remains supported away from zero, is smooth, is bounded by one, and has mass one. The corresponding square pushforward has the continuous density

`p_eps(z)=[f_eps(sqrt z)+f_eps(-sqrt z)]/(2 sqrt z)` for `z>0`,

with the natural zero extension elsewhere. Yet `q_#(f_eps dx)` converges in total variation to `q_#(f dx)`, whose density is discontinuous. Thus

**smooth inputs + uniform essential height + total-variation convergence do not imply output continuity.**

The pinned manuscript is safe on this point: only its genuinely `L^1`-Fourier no-pivot branch concludes continuity; pivot branches conclude essential boundedness by measure domination.

## 2. Critical rank-two logarithm: finite Riesz potential still does not imply height

Let `U,V` be independent uniform variables on `[-1/2,1/2]`; both densities equal one on their supports. Set

`R=2UV`.

For `0<|t|<1/2`, direct product change of variables gives

`boxed: p_R(t)=log(1/(2|t|)).`

Indeed the product `Z=UV` has

`p_Z(z)=2 int_(2|z|)^(1/2) dx/x =2 log(1/(4|z|))`,

and `R=2Z` contributes the factor `1/2`.

This density is unbounded at zero, but its negative half moment is finite and explicit:

`E|R|^-1/2
 =2 int_0^(1/2) t^-1/2 log(1/(2t)) dt
 =sqrt(2) int_0^1 u^-1/2 log(1/u) du
 =4 sqrt(2).`

More generally, for every finite `r>=1`,

`||p_R||_r^r
 =2 int_0^(1/2) log(1/(2t))^r dt
 =int_0^1 (-log u)^r du
 =Gamma(r+1).`

Thus every finite `L^r` norm exists while `L^infinity` fails.

### Gaussian inversion cannot remove the endpoint logarithm

Let the manuscript Gaussian be

`g_eps(y)=(4 pi eps)^(-1/2) exp(-y^2/(4eps))`.

At zero,

`(p_R*g_eps)(0)
 =int_(-1/2)^(1/2) log(1/(2|y|)) g_eps(y) dy`.

Substitute `y=sqrt(eps) u`:

`(p_R*g_eps)(0)
 =(4pi)^(-1/2) int_(|u|<1/(2sqrt eps))
   [ (1/2)log(1/eps)+log(1/(2|u|)) ] exp(-u^2/4) du.`

The Gaussian mass in the expanding interval tends to one, while the second term has a finite Gaussian integral. Therefore

`boxed: (p_R*g_eps)(0)=(1/2)log(1/eps)+O(1).`

So Gaussian regularization produces smooth densities but their heights diverge logarithmically. The Riesz half-potential remains finite throughout. This is a source-valid counterexample to either of the following proof shortcuts:

1. “finite `sup_a E|Z-a|^-1/2` implies bounded density”; or
2. “critical `|phi(t)|<=C/|t|` plus Gaussian smoothing can be inverted with a smoothing-uniform `L^infinity` bound.”

It is **not** a counterexample to an eight-direction theorem; it identifies the missing analytic gain required there.

## 3. Why the current multiplicity-eight endpoint is genuinely unpaid

The current source-backed `s_8` no-pivot terminal analysis reaches a critical split-row envelope of the form

`|phi_Q(t)| <= min(1,U/|t|)`,

hence all finite `L^r` output norms and `epsilon log(1/epsilon)` small-ball bounds. Separate overlap-one work supplies dimension-free aggregate shared-anchor currency. However, the example `R=2UV` proves that the functional information “critical `1/|t|` + every finite `L^r` + finite half-potential + smooth Gaussian approximants” is not enough for `L^infinity`.

Therefore a correct `s_8` proof must use the **extra overlap/shared-anchor product provenance before it is discarded**. It must yield either an integrable gain beyond `1/|t|`, or a direct linear small-ball estimate. Gaussian inversion/Riesz regularity alone cannot close the endpoint.

## 4. Fresh B15 revalidation of the complete threshold-nine replacement

The complete account02/B15 replacement proof is already immutable at

`improvements/account02/B15/20260924T140615Z-account02-B15-fixedmult-auto11/IMPROVEMENT.md`

(blob `3826ae990dd93e7a9d96b4c21b24d2b02a9e2a81`). I re-read its B15-sensitive steps against the pinned manuscript and the current package. The replacement retains arbitrary dimension, signs, remaining spectrum, affine terms and rough independent coordinate densities.

The closed dependency map is:

1. baseline Gaussian/Plancherel normalization and product projection;
2. grouped product-Fourier receiver on disjoint original-coordinate banks;
3. determinant-weighted entropy plus heavy-row promotion;
4. marginal-free `E_3` density receiver
   `||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`,
   `C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`;
5. marginal-free `E_2` **half-potential** receiver
   `sup_a E|Q-a|^-1/2 <= C_2 E_2(M)^(-1/8)`,
   `C_2=8 sqrt(e)2^(-1/8)=12.095072570796...`;
6. baseline order-three/order-two spectral-to-volume theorem, Schur count, scalar square profile and pair pivots.

Normalized branch closure under `s_9(A)>=1`:

- no pivot: `E_3^-1/6<=160`, hence height `<=160 C_3=2370.934026...<2400`;
- scalar pivot: Schur complement retains eight unit-scale directions. If it has a pivot, the baseline truncated-half-potential compiler applies; if it has no pivot, order-two volume plus the `E_2` receiver gives full half-potential `<153`. The conservative outer square-profile branch is `<=6010`;
- definite pair: `<32`;
- indefinite pair: `<251`.

Scaling `Y=KX` and `A->A/s` gives the complete theorem

`boxed: s_9(A)>=s>0 => ||p_Q||_infinity <=6010 K^2/s.`

The sharper constant work can lower `6010`, but the threshold claim does not depend on that optimization. The no-pivot grouped receiver has an integrable characteristic-function envelope and hence a `C_0` density; pivot branches require only essential density bounds, and this revalidation makes no global continuity claim.

## 5. Status

- Pinned 17-direction manuscript: **PASS**, modulo the harmless notation repair `A/B -> S` in the final indefinite-pair paragraph.
- Complete replacement threshold: **9**, with a conservative constant `6010 K^2/s` (sharper constants exist in sibling improvement files).
- Threshold 8: **OPEN**; additional shared-anchor analytic gain is required.
- Unrestricted three-eigenvalue QFORM: **OPEN**.
