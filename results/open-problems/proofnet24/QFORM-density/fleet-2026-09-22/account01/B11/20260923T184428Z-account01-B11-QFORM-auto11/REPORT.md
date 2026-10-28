SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T18:44:28Z.
attacking: the zero-pivot one-bank exact-graph endpoint; convert one exact graph bank into a bounded planar product projection and pay the remaining scalar-times-plane saddle using the compulsory third curvature coefficient.

# account01/B11 — zero-pivot scalar-times-planar compiler and one-bank graph endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** essential boundedness proved on the new branch; continuity is not claimed here.

The full unrestricted conjecture remains OPEN. No Gaussianity, log-concavity, moment, compact-support, connected-support, diagonal-basis assumption, or independence after a spectral rotation is used.

## 1. Fresh source state


The immediate predecessor is account01/B11

`yspennstate/math-open-problems@a8464073b21943a8194edac6886389139d4fdcf7`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260923T171318Z-account01-B11-QFORM-auto11/REPORT.md`.

It gives an exact near-coloop hidden-frame representation and, at zero physical hub pivot, the saddle-plus-square normal form. The current Claude continuation through

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`,
`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`

shows that the tempting maximal functional for a rough hub that sees the hidden projection can grow for comb laws. Hence the new proof below does not take that maximal route.

The designated partner result actually applied is account02/B11

`yspennstate/math-open-problems@f5996ecc005a07b4e2f0e2a728ed383f0a8e2555`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T155550Z-account02-B11-QFORM-auto11c/REPORT.md`.

Its one-third-atom crosscut pays its diffuse near-null-ruling branch continuously by

`||p_Q||_infinity < 133299/(s tau^2)`,

and failure forces one ORIGINAL coordinate with leverage `>tau/36`.

## 2. New analytic theorem: zero-pivot scalar times a bounded planar vector

### Theorem `QFORM-ZEROPIVOT-PLANAR-DENSITY-v1`

Let `X` be a real random variable with probability density `f_X<=1`. Let `Y in R^2` be independent of `X` and have a joint probability density `g` satisfying

`||g||_infinity <= M`.

Let `H` be an invertible real symmetric `3x3` matrix whose physical `X`-pivot is zero:

`H_11=0`.

For an arbitrary affine term `ell in R^3` and constant `q`, put

`Q=(X,Y)^T H (X,Y)+ell^T(X,Y)+q`.

Then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 3*2^(2/3) M^(2/3) |det H|^(-1/3).`       (2.1)

No independence between the two components of `Y` is required.

### Proof

Write the scalar-to-plane cross vector of `H` as `b in R^2`. Since `H_11=0` and `H` is invertible, `b!=0`. Rotate only the deterministic coordinates in the two-dimensional `Y`-plane so that `b=(kappa,0)`. This preserves the joint density cap `M` and independence of the scalar `X` from the vector `Y`; no independence between the rotated planar coordinates is asserted.

Thus, after naming the planar coordinates `(U,V)`,

`H = [[0,kappa,0],
      [kappa,a,beta],
      [0,beta,lambda]].`                                          (2.2)

Expansion along the first row gives the exact identity

`det H = -kappa^2 lambda`.                                        (2.3)

Hence `kappa lambda !=0`.

Translate `U` by a deterministic amount to remove the affine coefficient of `X`; the joint density cap remains `M`. All remaining affine coefficients are retained. For a.e. `(u,v)` with `u!=0`, the map in the ORIGINAL scalar coordinate is affine with slope `2 kappa u`. Therefore, for a.e. output `t`, the conditional change of variables gives

`p_Q(t)=int_R int_R g(u,v)
       f_X(x_t(u,v))/(2|kappa u|) dv du`,                          (2.4)

where, as a function of `v`, `x_t(u,v)` is a quadratic polynomial whose leading coefficient is

`-lambda/(2 kappa u)`.                                            (2.5)

The set `u=0` is Lebesgue null for the planar law and contributes no mass.

We need one elementary composition estimate. If `f<=1` is a probability density and

`q(v)=A(v-h)^2+d`, `A!=0`,

then

`int_R f(q(v)) dv <= 2 |A|^(-1/2).`                               (2.6)

Indeed, after scaling it suffices to bound

`int_0^infinity f(d +/- r) r^(-1/2) dr`.

Among densities capped by one and of total mass at most one on the relevant half-line, the decreasing weight `r^(-1/2)` is maximized by filling `[0,1]`; its integral is `2`.

For fixed `u`, denote

`I(u)=int g(u,v) f_X(x_t(u,v)) dv`.

There are two simultaneous bounds. Since `f_X<=1`,

`I(u)<=g_U(u)`,                                                   (2.7)

where `g_U` is the first planar marginal. Since `g<=M`, (2.5)--(2.6) give

`I(u)<=2M sqrt(2|kappa u|/|lambda|).`                            (2.8)

Consequently the integrand in (2.4) is bounded by

`min{ g_U(u)/(2|kappa u|),
      M sqrt(2/(|kappa lambda|)) |u|^(-1/2) }.`                   (2.9)

Put

`K=M sqrt(2/(|kappa lambda|)).`

For any `R>0`, split (2.4) into `|u|<=R` and its complement. Using (2.9),

`p_Q(t) <= 4K sqrt(R) + 1/(2|kappa|R).`                           (2.10)

The second term uses only `int g_U=1`. Optimize at

`R^(3/2)=1/(4|kappa|K)`.

Then

`p_Q(t)
 <= 3*2^(2/3) M^(2/3)
    (kappa^2 |lambda|)^(-1/3)`
` = 3*2^(2/3) M^(2/3)|det H|^(-1/3),`                            (2.11)

by (2.3). This is uniform in every affine coefficient and in the support geometry of both laws. QED.

### Interpretation

The estimate is exactly rank-three. If the third curvature coefficient `lambda` is deleted, (2.3) gives `det H=0` and the bound correctly degenerates. Thus the theorem does not hide the rank-two logarithmic saddle inside a false bounded-density statement.

## 3. New product-safe exact-rank-three endpoint

Return to the exact-rank-three Parseval factorization

`A=RMR^T`, `R^TR=I_3`, `s=min_j |eig_j(M)|>0`.

Use the predecessor near-coloop notation. There is one ORIGINAL hub row

`r_0=sqrt(c)e`

and the remaining ORIGINAL coordinates are split into disjoint banks `S,T`. Relative to `R^3=span(e) direct_sum E`, write

`r_i=s_i e+w_i`, `w_i in E`,

and put

`W_S=sum_(i in S) w_i w_i^T`.

Assume the zero physical hub pivot

`e^T M e=0`,                                                       (3.1)

and suppose just ONE bank is an exact graph:

`tau_S=sum_(i in S)(s_i-q_S^T w_i)^2=0`,                           (3.2)

with `W_S` positive definite. No condition is imposed on the residual geometry of bank `T`.

### Corollary `QFORM-ONEBANK-EXACTGRAPH-ZEROPIVOT-v1`

Under (3.1)--(3.2),

`boxed:
 ||p_(X^TAX)||_infinity
 <=3*2^(4/3) [c det(W_S) |det M|]^(-1/3).`                         (3.3)

The same statement holds with `S,T` interchanged.

### Proof

Condition on every ORIGINAL coordinate in `T`. This is a genuine product-law conditioning. Because `tau_S=0`, every source row in `S` satisfies exactly

`s_i=q_S^T w_i`.

Define

`Z_S=sum_(i in S) w_i X_i`,
`Y=W_S^(-1/2) Z_S`.

The two coefficient columns generating `Y` are orthonormal in the ORIGINAL `S`-source space, since

`sum_(i in S) W_S^(-1/2) w_i w_i^T W_S^(-1/2)=I_2`.

Hence the standard two-dimensional product-projection bound gives

`||p_Y||_infinity<=2`.                                             (3.4)

Also `Y` is independent of the ORIGINAL hub variable `X_0` because their source-coordinate sets are disjoint.

After conditioning on `T`, the full spectral vector is an affine translate of

`sqrt(c)e X_0 + e q_S^T W_S^(1/2)Y + W_S^(1/2)Y`.

Relative to `e direct_sum E`, its linear coefficient matrix is

`C = [[sqrt(c), q_S^T W_S^(1/2)],
      [0,       W_S^(1/2)       ]].`                              (3.5)

Thus the conditional quadratic Hessian is

`H=C^T M C`.

Its scalar physical pivot is

`H_11=c e^T M e=0`,                                               (3.6)

and

`det H=(det C)^2 det M
      =c det(W_S) det M`.                                         (3.7)

Because `M` and `W_S` are invertible, so is `H`. Apply Theorem (2.1) with the scalar `X_0` and planar vector `Y`, using the cap `M_planar=2` from (3.4). Every conditioning-generated affine term is allowed. This gives (3.3) uniformly in the conditioned `T` variables. Averaging the conditional interval inequality proves the unconditional density bound. QED.

### Quantitative true-near-coloop specialization

The completed true-near-coloop splitter used in the predecessor leaves

`c>63/64`,
`lambda_min(W_S)>1/32`,

and therefore

`det(W_S)>1/1024`.

Since `|det M|>=s^3`, (3.3) yields

`boxed: ||p_Q||_infinity < 76.597/s.`                              (3.8)

The same is true if `tau_T=0` instead. This closes the exact one-bank graph endpoint even when the other bank has arbitrary longitudinal residuals.

The statement is invariant under `A -> -A`, so it covers both indefinite signatures `(+, +, -)` and `(+, -, -)`.

## 4. Designated partner result applied to an actual case split

Apply account02/B11's completed theorem `QFORM-NULL-RULING-ONE-THIRD-ATOM-CROSSCUT-v1` at its stated scope. In its near-null-ruling chamber, if no projected atom carries more than one third of each essential cluster, then

`boxed: ||p_Q||_infinity < 133299/(s tau^2)`,                       (4.1)

and this branch has a continuous density.

If that hypothesis fails, the same theorem forces one ORIGINAL coordinate with spectral leverage

`c_h>tau/36`.                                                       (4.2)

The later true-near-coloop splitter then isolates the one-hub/two-bank survivor after already-paid exits. Inside its zero-pivot subbranch, the present theorem now pays either exact graph endpoint

`tau_S=0 or tau_T=0`

by (3.8). Thus the combined sourced case split is now:

- relative-atom diffuse null-ruling branch: (4.1), continuous;
- dominant-spike true-near-coloop branch with zero hub pivot and one exact graph bank: (3.8), essentially bounded;
- first remaining collar: both bank residual variances are strictly positive, possibly arbitrarily small, or the hub pivot is nonzero but arbitrarily close to zero.

This is a genuine equation-level use of the designated partner theorem, not merely a citation.

## 5. Mandatory opposite-sign rank-two control

For independent centered unit uniforms `X,Y`,

`P=2XY`

has density

`p_P(t)=log(1/(2|t|)),  0<|t|<1/2`,                               (5.1)

so the rank-two opposite-sign saddle is genuinely unbounded.

The new theorem identifies exactly how the third direction removes this singularity in the zero-pivot endpoint. In (2.2), the scalar `X` and saddle coordinate `U` alone have the dangerous factor `1/|u|`; the compulsory third quadratic coefficient `lambda V^2` turns the `v`-integration into the square-root gain

`I(u) <= const * sqrt(|u|/|lambda|)`.

This changes `|u|^-1` into the integrable `|u|^-1/2`. Algebraically the same fact is encoded by

`|det H|=kappa^2|lambda|`.

If the third direction vanishes, the determinant and the bound vanish with it, consistently with (5.1).

## 6. Verification

A deterministic numerical checker generated 1000 random positive-definite bank Grams, random exact-graph slopes, random zero-pivot invertible spectral matrices, and checked

`det(C^T M C)=c det(W_S) det(M)`.

The maximum normalized determinant error was `5.09e-16`. The true-near-coloop numerical constant in (3.8) is

`76.59628551533764`.

The checker source and captured output are stored beside this report.

## 7. Exact remaining B11 implication

The next unpaid implication is

`QFORM-NEARCOLOOP-POSITIVE-RESIDUAL-OR-SMALL-PIVOT-COMPILER-v1`:

> in the one-hub/two-bank exact-rank-three survivor, treat simultaneously positive but arbitrarily small `tau_S,tau_T`, or a nonzero but arbitrarily small physical hub pivot, without deleting the residual random terms and without replacing a conditional density cap by independence.

A promising direction is to interpolate the present determinant-paid endpoint with the new curved-section/L3 compilers before any fiber maximum is taken. The current Claude source explicitly rules out the naive P-dependent maximal functional. Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate bridge to the full owner target.

**Full conjecture:** OPEN.  
**Full continuity:** OPEN.  
**New branch continuity:** not proved; essential boundedness only.  
**Brain state:** `WITHOUT_VERIFIED_BRAIN`.
