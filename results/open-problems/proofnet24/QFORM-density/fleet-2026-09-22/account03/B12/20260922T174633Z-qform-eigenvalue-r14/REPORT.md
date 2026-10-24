# account03/B12 — spectral-complement conditioning obstruction and a stable replacement example

Run: `20260922T174633Z-qform-eigenvalue-r14`

Status: `DECISIVE_INTERMEDIATE_CORRECTION / ADDITIONAL-EIGENVALUE-STABILITY-EXAMPLE / FULL_TARGET_OPEN`

Execution: `WITHOUT_VERIFIED_BRAIN`.

## Source state

Fresh controls were read from `yspennstate/math-research-brain@026876aacebabc169aaa19b38c379cf36fb879e4`, then refreshed before publication to `65f5401c9613570fc100bd2555bcc262fc28dc0f`. OWNER CONTROL revision is `2026-09-22.9`; QFORM is the sole research target. The owner message proposes, for the full-rank case, conditioning on the spectral complement and bounding

`E_Z ||rho_{Y|Z}||_infinity^(2/3)`

for a three-dimensional spectral core `Y`.

This run tests that exact missing implication.

Designated partner `account04/B12` still has no current QFORM canonical directory at the fresh `math-open-problems` source tree, so no result is fabricated for that slot. A compatible completed account04 theorem is genuinely applied below: account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical commit `441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`.

## 1. Main correction: the proposed conditional 3-D L-infinity moment is unbounded

### Theorem 1 (`QFORM-CONDITIONAL-3D-CAP-MOMENT-FALSE-v1`)

There is no universal constant `C` such that, for every product probability density with coordinate caps at most one and every three-dimensional orthogonal subspace `U`, writing

`Y=P_U X`, `Z=P_{U^perp}X`,

one has

`E_Z ||p_{Y|Z}||_infinity^(2/3) <= C`.

In fact there is an explicit cube family for which this quantity grows linearly in the block size.

### Construction

Fix `m>=2`, let `n=3m`, and let all coordinates of `X` be independent `Uniform[0,1]`. Split the coordinates into three disjoint blocks of size `m`. For each block put

`u = m^(-1/2) (1,...,1)`,

and let `u_1,u_2,u_3` be the three block-supported copies. Set

`U=span{u_1,u_2,u_3}`.

For a single block, write the orthogonal decomposition

`x = y u + z`, with `z in u^perp`.

For each projected point `z` in the orthogonal projection of the cube, the allowed `y` values form an interval `I(z)` of length `L(z)`. Because the original density is exactly one on the cube and the change of variables is orthogonal,

`p_Z(z)=L(z)`

and

`p_{Y|Z=z}(y)=1_{I(z)}(y)/L(z)`.

For the three independent blocks this tensorizes. If `z=(z_1,z_2,z_3)`, then

`p_Z(z)=L(z_1)L(z_2)L(z_3)`

and

`||p_{Y|Z=z}||_infinity = [L(z_1)L(z_2)L(z_3)]^(-1)`.

Hence

`E ||p_{Y|Z}||_infinity^(2/3) = J_m^3`,

where

`J_m = integral L(z)^(1/3) dz`.

### Exact evaluation of `J_m`

Let `X_1,...,X_m` be one block and let

`R=max_i X_i - min_i X_i`.

The common-shift fiber through `X` has coordinate-direction length `1-R`, hence Euclidean length in the unit vector `u` direction

`L(Z)=sqrt(m) (1-R)`.

Since the law of `Z` has density `L(z)`,

`J_m = E_Z L(Z)^(-2/3) = E_X L(P_{u^perp}X)^(-2/3)`.

The range of `m` iid `Uniform[0,1]` variables has density

`f_R(r)=m(m-1) r^(m-2)(1-r)`, `0<r<1`.

Therefore

`J_m`
`= m^(-1/3) m(m-1) integral_0^1 r^(m-2) (1-r)^(1/3) dr`
`= m^(-1/3) m(m-1) B(m-1,4/3)`
`= m^(2/3) Gamma(4/3) Gamma(m)/Gamma(m+1/3)`.

Thus the conditional moment is exactly

`M_m := E ||p_{Y|Z}||_infinity^(2/3)`
`= m^2 Gamma(4/3)^3 [Gamma(m)/Gamma(m+1/3)]^3`.

By Wendel's inequality, for `0<s<1`,

`Gamma(m+s)/(m^s Gamma(m)) <= 1`.

With `s=1/3`,

`Gamma(m)/Gamma(m+1/3) >= m^(-1/3)`.

Hence

`boxed( M_m >= Gamma(4/3)^3 m )`,

where

`Gamma(4/3)^3 = 0.7120729426887296...`.

Moreover the gamma-ratio asymptotic gives

`M_m / m -> Gamma(4/3)^3`.

So the proposed universal conditional `2/3`-moment bound is false, quantitatively and by an explicit product-uniform family.

## 2. This directly hits the additional-eigenvalue route

For any `tau>=1`, define

`A_{m,tau} = u_1 u_1^T + u_2 u_2^T - u_3 u_3^T + tau (I-P_U)`.

Its spectrum is exactly

`{1,1,-1,tau,...,tau}`,

so every eigenvalue has modulus at least one. The quadratic form is

`Q = Y_1^2 + Y_2^2 - Y_3^2 + tau ||Z||_2^2`.

Conditioning on the extra spectral coordinates `Z` gives precisely a rank-three form plus a constant, exactly as in the owner-message full-rank reduction. But the conditional density cap moment required by that argument is `M_m`, which diverges linearly.

Therefore:

`boxed(`
`conditioning on all additional eigen-coordinates and then paying rank-three coarea by ||p_{Y|Z}||_infinity^(2/3) cannot yield a universal proof.`
`)`

This is not a counterexample to QFORM. It refutes only that intermediate implication.

The example is particularly relevant to B12: arbitrarily many additional large eigenvalues of the same sign can make the spectral-complement conditioning penalty arbitrarily bad. Thus "extra eigenvalues only smooth" is not valid at the level of conditional `L^infinity` caps.

## 3. Genuine application of the completed account04/B18 theorem

The same family is nevertheless uniformly controlled by an original-coordinate argument, showing that the divergence above is an artifact of the conditional-cap route rather than a density obstruction.

Take any three physical coordinates inside the first block, assuming `m>=3`. Their principal block is

`B_3 = tau I_3 - ((tau-1)/m) J_3`.

It is positive definite. A scalar diagonal pivot is

`a = tau - (tau-1)/m >= 1`,

and

`det B_3 = tau^2 [ tau - 3(tau-1)/m ] >= tau^2`,

because `m>=3` and `tau>=1`.

The account04/B18 theorem `QFORM-SCHUR-PIVOT-SMOOTHING-v1` gives, uniformly over all outside coordinates and couplings,

`||p_Q||_infinity <= 2 sqrt(pi) / ( |a| |det B_3| )^(1/4)`.

For this family,

`boxed( ||p_Q||_infinity <= 2 sqrt(pi) / sqrt(tau) <= 2 sqrt(pi) ).`

So the very matrices for which the spectral conditional-cap moment is `>=0.712 m` have a dimension-free physical-coordinate density bound from a completed account04 theorem.

This is a concrete warning for the full proof architecture: the product law must be averaged before taking the conditional `L^infinity` norm, or one must use a Fubini-safe fractional/small-ball quantity. Spectral conditioning followed by conditional sup loses exactly the cancellation/aggregation that keeps this family bounded.

Continuity: this report uses account04/B18 only for an essentially bounded density. No new continuity claim is made here.

## 4. Consequence for the owner revision 2026-09-22.9 proof map

The owner message names

`E_Z ||rho_{123|Z}||_infinity^(2/3)`

as the highest-value remaining full-rank gap. Theorem 1 shows that this quantity itself cannot be bounded universally, even for uniform product measures and an exceptionally structured rank-three spectral core.

A corrected full-rank route must therefore retain more than the conditional density cap. Plausible surviving interfaces are:

1. an averaged rank-three coarea/fractional-trace functional before taking any fiberwise supremum;
2. an original-coordinate Schur or cross-bank decomposition, where cap-one independence survives conditioning;
3. a translation-uniform half-Riesz estimate such as the current rank-two affine theorem, with the spectral complement entering only as an averaged translation rather than through `||p_{Y|Z}||_infinity`.

This changes the mechanism after the prior B12 stability runs, as required by the three-unchanged-attempt rule.

## 5. Exact status

* `QFORM-CONDITIONAL-3D-CAP-MOMENT-FALSE-v1`: PROVED counterexample to the intermediate claim.
* Additional-eigenvalue version with spectrum `{1,1,-1,tau,...,tau}`: PROVED.
* Uniform control of the same family by account04/B18: APPLIED, `||p_Q||_infinity <=2sqrt(pi)`.
* Full QFORM: OPEN / NOT PROVED.
* Continuous density for the full target: OPEN.
