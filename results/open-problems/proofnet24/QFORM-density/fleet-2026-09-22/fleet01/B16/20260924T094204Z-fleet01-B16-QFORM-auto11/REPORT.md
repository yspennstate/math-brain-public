SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B16, 2026-09-24T09:42:04Z.
attacking: upgrade the shared-bank projected-square/hyperbolic curved receiver to arbitrary planar same-bank quadratic curvature, while retaining dependence and applying fleet02/B16's completed receiver to a strict target inequality.

# fleet01/B16 — one-sided curved-cap sharpening and full planar-curvature transducer

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING THEOREM / STRICT TARGET CLASS / PARTNER APPLIED / FULL QFORM OPEN**  
Continuity of the unrestricted target: **OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-pinned dependencies and correction boundary

Fresh owner/control source at start: `math-research-brain@0f67fb8650eb867f39967849c26ce0ae8e657e07`; owner control revision `2026-09-22.15`, programme revision `2026-09-22.5`.

The completed designated partner consumed here is fleet02/B16:

- repository/commit: `yspennstate/math-open-problems@e242a1718c8fe91f9ea9b2cdfa2a7961f25cd37b`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260924T084749Z-fleet02-B16-QFORM-auto11/REPORT.md`;
- theorem: `QFORM-SHAREDBANK-PROJECTEDSQUARE-HYPERBOLIC-CURVEDCAP-v1`.

That theorem proves, for an arbitrary dependent planar density `(S,U)` of height at most `M`, an independent scalar `V` of density height at most `N`, and

`Q=a(S+d)^2+2b(U+alpha)(V+beta)+r0`,

the bound

`||p_Q||_infinity <= 6(MN)^(2/3)(|a|b^2)^(-1/3)`.

The same pinned report also records the actual product-projection inputs used below:

`||p_(S,U)||_infinity <= 2 det(G)^(-1/2)`

for the two-dimensional projection of an original cap-one product bank, and

`||p_V||_infinity <= sqrt(2)/tau`

for a scalar projection with coefficient norm `tau` from a disjoint product bank. These are used only as true marginal density bounds; no projected independence and no conditional projected-density cap are inferred.

All live negative corrections are preserved. In particular this report does **not** use a generic bounded 3D joint density inside an indefinite coarea integral; does not assume post-projection independence; does not use worst conditional projection caps; does not use law-uniform pointwise oscillatory decay; and does not use the refuted absoluteized mixed norm `int |t|^(-1/2)||G_t||_2 dt`. The only source separation used below is genuine disjointness between the planar original-coordinate bank and the scalar original-coordinate bank.

## 2. Main theorem: arbitrary same-bank planar curvature survives the curved receiver

### Theorem 2.1 — `QFORM-SHAREDBANK-PLANAR-SCHUR-CURVEDCAP-v1`

Let `(S,U)` have an arbitrary joint probability density `rho` on `R^2` with

`||rho||_infinity <= M`.

Let `V` be independent of `(S,U)` and have density `f` with

`||f||_infinity <= N`.

Let `a,b` be nonzero real numbers. Let `h,R:R->R` be arbitrary measurable functions, and let `alpha,beta,r0` be arbitrary real constants. Define

`Q = a(S-h(U))^2 + R(U) + 2b(U+alpha)(V+beta) + r0`.          (2.1)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 3*2^(2/3) (MN)^(2/3) (|a|b^2)^(-1/3).`                   (2.2)

Numerically the abstract prefactor is

`3*2^(2/3)=4.762203155904598...`.

No regularity of `h` or `R` is required, no independence between `S` and `U` is required, and continuity of `p_Q` is **not** asserted by this theorem.

This strictly extends the completed fleet02/B16 curved receiver in two ways:

1. an arbitrary `U`-dependent translation of the square center is allowed;
2. an arbitrary same-bank `U`-only phase/curvature `R(U)` is allowed.

It also sharpens the partner constant `6` to `3*2^(2/3)` by keeping the half-Riesz kernel on its genuine one-sided support instead of symmetrizing it to the full absolute kernel.

### Proof

Translations in `U,V` and in the output preserve density heights, so absorb `alpha,beta,r0` into the notation. Replace `h,R` accordingly. It is enough to prove the result for

`Q=a(S-h(U))^2+R(U)+2bUV`.                                    (2.3)

Put

`m(u)=int_R rho(s,u) ds`.

Since `U` has a density, the slice `u=0` is null. For `u!=0`, condition on `(S,U)` and change variables in the independent scalar `V`. For a.e. output level `q`,

`p_Q(q)
 = int_R [1/(2|bu|)] J_q(u) du`,                              (2.4)

where

`J_q(u)
 = int_R rho(s,u)
   f((q-R(u)-a(s-h(u))^2)/(2bu)) ds`.                         (2.5)

There are two complementary estimates.

#### 2.1 Hyperbolic/mass estimate

Using only `f<=N`,

`J_q(u) <= N m(u)`.                                           (2.6)

After the Jacobian in (2.4), this gives

`[1/(2|bu|)]J_q(u)
 <= [N/(2|b|)] m(u)/|u|`.                                    (2.7)

This is strong away from the hyperbolic singularity `u=0`.

#### 2.2 Curved joint-cap estimate with the **one-sided** half-potential

Using the actual joint cap before integrating the square,

`J_q(u)
 <= M int_R
 f((q-R(u)-a(s-h(u))^2)/(2bu)) ds`.                          (2.8)

The translation `s -> s-h(u)` is harmless. For arbitrary nonzero real `c` and arbitrary real `q0`, the exact square substitution gives

`int_R f((q0-a s^2)/c) ds
 = sqrt(|c|/|a|)
   int_{H_z} f(v)|v-z|^(-1/2) dv`,                            (2.9)

where `z=q0/c` and `H_z` is **one** of the two half-lines with endpoint `z`; which half-line occurs depends only on the signs of `a,c`.

This one-sided support matters. For every probability density `f<=N`,

`sup_z int_{v<=z} f(v)(z-v)^(-1/2) dv <= 2 sqrt(N)`,           (2.10)

and the identical bound holds on the right half-line. Indeed, writing `x=z-v>=0`, the decreasing kernel `x^(-1/2)` is maximized under the constraints `0<=g<=N`, `int g<=1` by taking `g=N` on `[0,1/N]`, giving exactly

`N int_0^(1/N) x^(-1/2) dx = 2 sqrt(N)`.                      (2.11)

Thus, with `c=2bu`,

`J_q(u)
 <= 2M sqrt(2N|bu|/|a|)`.                                    (2.12)

After the Jacobian in (2.4),

`[1/(2|bu|)]J_q(u)
 <= B |u|^(-1/2)`,                                            (2.13)

where

`B = sqrt(2) M sqrt(N) / sqrt(|ab|)`.                         (2.14)

This is locally integrable at `u=0`.

#### 2.3 Radius split and exact optimization

Let

`A=N/(2|b|)`.

For arbitrary `R0>0`, use (2.13) on `|u|<=R0` and (2.7) outside. Since `int m=1`,

`p_Q(q)
 <= 4B sqrt(R0) + A/R0`.                                     (2.15)

Put `x=sqrt(R0)`. The right side is

`4Bx + A/x^2`.

Its minimum occurs at

`x^3=A/(2B)`,                                                 (2.16)

and the minimum is

`3*2^(2/3) B^(2/3) A^(1/3)`.                                 (2.17)

Using (2.14) and the definition of `A`, the powers of `2` inside `B^(2/3)A^(1/3)` cancel exactly:

`B^(2/3)A^(1/3)
 = (MN)^(2/3)|a|^(-1/3)|b|^(-2/3)`.                          (2.18)

Substituting this into (2.17) proves (2.2), uniformly in `q`.

The conditional densities in (2.4) integrate to one off the null slice `u=0`, so Fubini gives an absolutely continuous law. QED.

### Why this does not violate the generic coarea correction

The theorem does **not** say that an arbitrary bounded three-dimensional density has a bounded indefinite quadratic trace. The special source structure is essential: `(S,U)` is one genuine source object, while `V` is an independent source object. The singular hyperbolic factor `1/|u|` is repaired by spending the **same planar joint cap** through the parabolic square before integrating in `u`. The special one-sided square geometry is what creates `|u|^(-1/2)`.

## 3. Full quadratic curvature in the dependent planar bank

The previous theorem immediately pays every quadratic form in the shared planar pair, not just a single projected square.

### Corollary 3.1 — `QFORM-SHAREDBANK-FULLPLANAR-ZEROSCALAR-v1`

Let `Y=(Y1,Y2)` have joint density at most `M`; let `V` be independent with density at most `N`. Let

`mathcal B = [[C,d],[d^T,0]]`,                                (3.1)

where `C` is an arbitrary real symmetric `2x2` matrix, `d in R^2`, and `mathcal B` is nonsingular. For an arbitrary affine functional `ell(Y,V)+c0`, put

`Q=(Y,V)^T mathcal B (Y,V)+ell(Y,V)+c0`.                       (3.2)

Then

`boxed:
 ||p_Q||_infinity
 <= 3*2^(2/3)(MN)^(2/3)|det mathcal B|^(-1/3).`               (3.3)

Again, continuity is not asserted.

### Proof

Nonsingularity implies `d!=0`. Choose `T in SL(2,R)` whose second row is `d^T`; this is possible because a first row can be chosen to have determinant one with `d^T`. Set

`(S,U)^T = T Y`.

Because `det T=1`, the joint density height is unchanged:

`||p_(S,U)||_infinity <= M`.                                  (3.4)

Under the congruence by `diag(T^(-1),1)`, the matrix becomes

`mathcal B'=
 [[a,c,0],
  [c,d0,1],
  [0,1,0]]`.                                                  (3.5)

The cross term is exactly `2UV`. Since the congruence has determinant one,

`det mathcal B' = det mathcal B`.                              (3.6)

But direct expansion of (3.5) gives

`det mathcal B'=-a`.                                          (3.7)

Hence `a=-det mathcal B !=0`.

Complete the planar quadratic, including the `S`-linear affine term:

`aS^2+2cSU+d0U^2+l1S+l2U
 = a(S-h(U))^2+R(U)`                                          (3.8)

for an affine `h` and a quadratic/affine `R`. Any affine term in `V` is absorbed by translating the hyperbolic `U` coordinate, while remaining constants translate the output. Theorem 2.1 with `b=1` now gives (3.3). QED.

This is the promised nonseparable-curvature transducer: arbitrary `Y1Y2`, `Y1^2`, and `Y2^2` terms in the dependent planar bank are retained exactly.

## 4. Insert the actual bounded-density projection theorem

Let `I,J` be disjoint original-coordinate product banks. On `I` take two linearly independent coefficient vectors `r,u` and define

`Y=(r^T X_I, u^T X_I)`.

Let

`G = [[||r||^2,<r,u>],[<r,u>,||u||^2]]`,                     (4.1)

so `det G>0`. On `J` let

`V=v^T X_J`,  `tau=||v||_2>0`.                               (4.2)

The completed bounded-density projection theorem gives the genuine marginal bounds

`||p_Y||_infinity <= 2 det(G)^(-1/2)`,                        (4.3)

`||p_V||_infinity <= sqrt(2)/tau`.                            (4.4)

The objects `Y` and `V` are independent because their **original source banks** are disjoint. No claim is made that the two coordinates of `Y` are independent.

Let `mathcal B` be any nonsingular symmetric `3x3` carrier with lower-right entry zero, written as in (3.1), and set

`A=[r,u,v] mathcal B [r,u,v]^T`.                              (4.5)

Then Corollary 3.1 gives

`boxed:
 ||p_(X^T A X)||_infinity
 <= 6*2^(2/3)
    [ det(G) tau^2 |det mathcal B| ]^(-1/3).`                 (4.6)

The three columns are linearly independent, and because the Gram matrix is `diag(G,tau^2)`, the nonzero pseudodeterminant satisfies

`|pdet A|
 = det(G) tau^2 |det mathcal B|`.                             (4.7)

Therefore

`boxed:
 ||p_(X^T A X)||_infinity
 <= 6*2^(2/3) |pdet A|^(-1/3).`                               (4.8)

Numerically

`6*2^(2/3)=9.524406311809196...`.

If this exact-rank-three core satisfies the owner's spectral hypothesis, all three nonzero eigenvalues have modulus at least one, so `|pdet A|>=1` and

`boxed: ||p_(X^T A X)||_infinity <= 9.524406311809196... .`    (4.9)

This improves the partner's no-leverage exact-rank-three constant `12` and, more importantly, permits **arbitrary quadratic curvature in the overlapping planar bank**.

## 5. Strict target family with genuinely nonseparable shared-bank curvature

Take an arbitrary original cap-one product bank supporting an orthonormal pair `S,U`, and a disjoint product bank supporting a normalized scalar projection `V`. Consider

`Q_* = 2S^2 + 2SU + U^2 + 4UV`.                               (5.1)

The carrier matrix in `(S,U,V)` is

`B_* = [[2,1,0],[1,1,2],[0,2,0]]`.                            (5.2)

It has

`det B_*=-8`,                                                 (5.3)

and characteristic polynomial

`p(lambda)=lambda^3-3lambda^2-3lambda+8`.                     (5.4)

Exact sign checks give

`p(-2)=-6, p(-1)=7`,
`p(1)=3, p(2)=-2`,
`p(3)=-1, p(4)=12`.                                           (5.5)

Hence its three eigenvalues lie respectively in

`(-2,-1), (1,2), (3,4)`,                                     (5.6)

so this is a strict owner-target instance. Since `|pdet B_*|=8`, (4.8) gives

`boxed:
 ||p_(Q_*)||_infinity
 <= [6*2^(2/3)]/2
 =3*2^(2/3)
 =4.762203155904598... .`                                     (5.7)

The mixed `SU` term and the `U^2` term are not discarded or treated perturbatively; they are exactly absorbed into the planar completion (3.8).

## 6. Required literal application of the completed fleet02/B16 theorem

Before using the strengthening above, apply the designated partner theorem exactly as proved to

`Q_partner = 2S^2 + 4UV`,                                     (6.1)

where `(S,U)` is an orthonormal two-dimensional projection of one cap-one product bank and `V` is a normalized scalar projection of a disjoint product bank.

The actual projection theorem supplies

`M<=2`, `N<=sqrt(2)`.                                         (6.2)

The completed fleet02/B16 theorem has `a=2`, `b=2`; therefore

`||p_(Q_partner)||_infinity
 <=6(2sqrt(2))^(2/3)(2*2^2)^(-1/3)
 =6`.                                                         (6.3)

Its carrier is

`diag(2, [[0,2],[2,0]])`,

with exact spectrum

`{2,2,-2}`.                                                   (6.4)

Thus (6.3) is an actual strict-target inequality obtained by applying the completed designated partner result, not just by comparing formulas.

The new one-sided theorem then improves the same instance to

`||p_(Q_partner)||_infinity
 <=3*2^(2/3)=4.762203155904598...`,                            (6.5)

and extends it to the entire full-planar class of Sections 3--5.

## 7. What is and is not paid

Paid in this run:

- the projected square may share an original source bank with one hyperbolic factor;
- the two coordinates of that shared projection may be arbitrarily dependent;
- every quadratic `S^2,SU,U^2` term in that same planar projected bank is retained exactly;
- arbitrary affine terms are harmless;
- no diffuse-leverage condition is required once the true two-dimensional marginal cap is available;
- the no-leverage exact-rank-three class with an independent scalar **isotropic direction** (`B_33=0`) is bounded by `6*2^(2/3)<9.525` under the full cap-one source hypothesis.

Not paid:

- a nonzero `V^2` coefficient on the disjoint scalar resource; completing its square by shifting `V` with a function of the dependent planar bank would destroy the genuine source separation;
- additional quadratic degrees of freedom inside either original bank that are not functions of the selected projections `(S,U)` or `V`;
- the generic near-coloop survivor in which no source-valid partition produces a planar dependent block plus an independent isotropic scalar block;
- continuity for this curved-cap theorem under arbitrary rough input densities.

The first B16 implication is therefore sharpened to

`QFORM-SHAREDBANK-NONISOTROPIC-SCALAR-TRANSDUCER-v1`:

> Starting from the live near-coloop survivor, either extract a source-valid dependent planar projection plus a genuinely disjoint scalar direction whose carrier self-curvature is zero, in which case (4.9) pays the whole planar quadratic exactly; or use the nonzero scalar self-curvature / residual within-bank curvature itself as a previously paid Fresnel, rank-two, or cross-volume smoothing resource. Do not eliminate it by a source-dependent change of variables that destroys independence.

The unrestricted QFORM theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. The unrestricted continuity conclusion remains **OPEN**.
