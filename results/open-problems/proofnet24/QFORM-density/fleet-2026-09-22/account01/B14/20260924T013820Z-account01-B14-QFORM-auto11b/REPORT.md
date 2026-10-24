SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-24T01:38:20Z.
attacking: shared-receiver hybrid localization — let the third spectral direction split between self-curvature of one physical receiver and diffuse leakage into the same independent bank, and pay whichever whole-law mechanism is stronger before any fragment normalization.

# account01/B14 — shared-receiver hybrid localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control: revision `2026-09-22.15`  
Assignment: translations and localization.  
Status: **NEW SUPPORTING THEOREM / STRICT TARGET BRANCH / FULL QFORM OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 0. Scope and dependencies

The live target remains the full arbitrary-product-law conjecture: independent real original coordinates with densities at most one, arbitrary real symmetric coefficient matrix with at least three eigenvalues of modulus at least one, and no support, moment, centering, sign, log-concavity, connectedness, or post-rotation independence assumption.

Corrections consumed include: law-uniform pointwise quadratic Fourier decay is false; product independence is not preserved by spectral rotation; bounded-diameter and fixed-fragment-count localization are false; a uniformly good principal minor is not forced by the bare spectral hypothesis; projection and diagonal estimates are supporting controls only.

Two completed account02/B14 results are used at actual inequalities:

1. `account02/B14 r34`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T112750Z-account02-B14-QFORM-r34/REPORT.md`, read at blob `831ce9789e07dae4cc27275d0b1eb0993048e22f`.  Its arbitrary-self random-slope theorem plus the source-pinned product-projection estimate gives, for an invertible indefinite original-coordinate pair block `C`,

   `D=|det C|`, `kappa=sigma_min(C)`,

   and a remaining physical receiver `Z` with arbitrary self coefficient and slope `2 c^T Y + shift`,

   `||p_Q||_infinity <= 8/[2^(1/4) sqrt(kappa ||c||_2)] + C_*/sqrt(D)`,

   where

   `C_* = 2+log 2 + sqrt(2 pi e) erfc(1/sqrt 2) = 4.004506265397...`.

   This estimate is uniform in the receiver self coefficient, the bank remainder, all translations, and support geometry.

2. The newest completed `account02/B14` whole-product log-plus-square report,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T235641Z-account02-B14-QFORM-auto11b/REPORT.md`, proves for a hyperbolic pair the affine-uniform inequality

   `||p_(2aUV+hZ^2+affine)||_infinity <= |a|^(-1)+8/sqrt(|a h|)`.

   I apply it below to the hyperbolic specialization as an independent source-valid branch check. The stronger square estimate used for the final constant is derived directly here from the general physical-pair logarithmic envelope recorded in r34, retaining the mass cap before layer cake.

No refuted intermediate claim is used.

## 1. Setup: one indefinite physical pair and one shared receiver bank

Let `X=(X_1,X_2)` be two independent cap-one original-coordinate variables. Let `C` be a real symmetric invertible indefinite `2 x 2` matrix. Put

`D=|det C|`, `kappa=sigma_min(C)`.

Let `Z,Y_1,...,Y_m` be further independent cap-one original-coordinate variables, independent of `X`, and write `Y=(Y_1,...,Y_m)`. Fix arbitrary

`h in R`, `c in R^m`, `H=H^T`,

and arbitrary deterministic affine coefficients. Consider

`Q = X^T C X + h Z^2 + 2 Z c^T Y + Y^T H Y + (arbitrary affine function of X,Z,Y).`   (1.1)

The key point is that the same physical coordinate `Z` can carry both self-curvature `h` and diffuse leakage `c^T Y`. Previous single-mechanism proofs pay either `1/sqrt(|h|)` or `1/sqrt(||c||)` and can blow up when their chosen resource vanishes. Here the two mechanisms are kept simultaneously and the better one is paid.

The result below is completely insensitive to translations of every marginal, remote support components, unbounded support, and all moments.

## 2. General physical-pair plus square: a mass-aware logarithmic compiler

The completed physical-pair logarithmic envelope used in account02/B14 r34 says that, after arbitrary affine completion of the pair, for every cutoff `r>0`, the density of the pair core obeys

`p_pair(t) <= 2 sqrt(2)/r + D^(-1/2) log_+( 2 r^2/(kappa |t-t_0|) )`,   (2.1)

for a harmless output translation `t_0`. This uses the original pair coordinates and does not rotate their law.

Now add an independent cap-one variable `Z` through `hZ^2+gamma Z`. If `h != 0`, complete the square in `Z`; translating `Z` preserves the cap. The elementary square level-set estimate is

`|{z: |tau-z^2|<delta}| <= 2 sqrt(2 delta)`.   (2.2)

For a cap-one probability law of `Z`, layer cake with the trivial probability cap retained gives, for every `A,b>0`,

`int log_+(A/|t-bZ^2|) dP <= 2 psi( 2 sqrt(2A/b) )`,   (2.3)

where

`psi(x)=x` for `0<x<=1`,
`psi(x)=1+log x` for `x>=1`.   (2.4)

Indeed the layer-cake integrand is bounded by `min(1,K e^{-s/2})`, with `K=2 sqrt(2A/b)`, whose integral is exactly `2K` for `K<=1` and `2(1+log K)` for `K>=1`.

Convolving (2.1) with the translated square and taking `A=2r^2/kappa`, `b=|h|` gives

`||p_Q||_infinity <= 2 sqrt(2)/r + 2 D^(-1/2) psi(4r/sqrt(kappa |h|)).`   (2.5)

Put

`x = 4r/sqrt(kappa |h|)`,
`theta = 4 sqrt(2D/(kappa |h|))`.   (2.6)

Then (2.5) is

`||p_Q||_infinity <= (2/sqrt(D)) [ theta/x + psi(x) ].`   (2.7)

The minimization is explicit:

`boxed:
 B_sq(C,h) := ||p_Q||_infinity <=
   4 D^(-1/2) sqrt(theta),                 if 0<theta<=1,
   2 D^(-1/2) [2+log theta],               if theta>=1.             `   (2.8)

The first line uses `x=sqrt(theta)`; the second uses `x=theta`. This estimate is uniform in the linear term of `Z`, in all pair translations, and in the value of the bank coordinates after conditioning.

### Normalized pair consequence

If both eigenvalues of the indefinite `2 x 2` block `C` have modulus at least one, then

`D>=1`, `kappa>=1`.   (2.9)

For `|h|>=1/26`, (2.8) gives

`boxed: B_sq(C,h) <= 4 + 2 log(4 sqrt(2)) + log 26
                     = 10.723832440821... .}`   (2.10)

Proof of the uniformity in `D,kappa`: in the `theta<=1` branch the bound is at most `4/sqrt(D)<=4`. In the `theta>=1` branch, dropping `kappa>=1` only enlarges the logarithm. Writing `x=sqrt D>=1`, the right side is `2(A+log x)/x`, where `A>=2+log(4sqrt2)+(1/2)log26>1`; hence it decreases in `x`, so the maximum is at `D=1`.

This is a general-physical-pair version of the newest account02/B14 log-plus-square mechanism; no hyperbolic normal form or rotation is used.

## 3. The complementary arbitrary-self leakage branch from account02/B14

Now keep the same form (1.1), but do not pay `h`. Account02/B14 r34 applies directly with `Z` as the physical receiver and the untouched product bank `Y` as the slope bank. Its completed inequality gives

`boxed:
 B_leak(C,c) := ||p_Q||_infinity
 <= C_*/sqrt(D) + 8/[2^(1/4) sqrt(kappa ||c||_2)].
}`   (3.1)

This is the required designated-partner result applied to the actual quadratic inequality (1.1), not just cited as background. Crucially, it is uniform in the self coefficient `h`; the copy-difference argument in r34 turns `h` into a translation of the random slope rather than paying `1/sqrt(|h|)`.

If `D,kappa>=1` and

`||c||_2 >= sqrt(675/676)`,   (3.2)

then

`boxed:
 B_leak(C,c)
 <= C_* + 2^(11/4) (676/675)^(1/4)
 = 10.734167749364... < 10.735.
}`   (3.3)

The bank dimension does not appear. For example `c=m^(-1/2)(1,...,1)` has `||c||_2=1` even though every individual coefficient tends to zero.

## 4. Shared-receiver hybrid theorem

### Theorem — `QFORM-SHARED-RECEIVER-HYBRID-10735-v1`

Assume the two original-coordinate variables `X_1,X_2` have an invertible indefinite pair matrix `C` whose two eigenvalues have modulus at least one. For mutually independent cap-one `Z,Y_1,...,Y_m`, arbitrary symmetric `H`, and arbitrary affine terms, let `Q` be (1.1). If

`rho := sqrt(h^2+||c||_2^2) >= 1`,   (4.1)

then

`boxed: ||p_Q||_infinity < 10.735.`   (4.2)

### Proof

There are two cases.

**Case 1: `|h|>=1/26`.** Apply the square branch (2.10):

`||p_Q||_infinity <= 10.723832440821... <10.735.`

**Case 2: `|h|<1/26`.** From `h^2+||c||_2^2>=1`,

`||c||_2 > sqrt(1-1/26^2)=sqrt(675/676).`

Apply the completed account02/B14 arbitrary-self leakage estimate (3.3):

`||p_Q||_infinity <=10.734167749364...<10.735.`

No limiting or continuity argument is used at `h=0`; that endpoint belongs directly to the leakage branch. No reciprocal leakage payment is used at `c=0`; that endpoint belongs directly to the square branch. QED.

The mechanism is therefore a genuine max-resource closure on the **same receiver coordinate**:

`self curvature h  OR  whole-bank leakage c`,

rather than two disjoint third resources.

## 5. Strict full-target family and zero-tax ambient localization

Take an original-coordinate principal block

`A_* = C direct_sum S`,

where `C` is as above and

`S = [[h, c^T], [c, H]]`   (5.1)

acts on `(Z,Y)`. Suppose

- `C` is indefinite and both of its eigenvalues have modulus at least one;
- `sqrt(h^2+||c||_2^2)>=1`.

Then `C` contributes two eigenvalues of modulus at least one. Also

`||S||_op >= ||S e_Z||_2 = sqrt(h^2+||c||_2^2)>=1`,   (5.2)

so `S` contributes a third eigenvalue of modulus at least one. Hence `A_*` is itself inside the owner's exact spectral target.

Now embed `A_*` as a principal block of an arbitrary larger symmetric matrix. All outside quadratic coefficients and all active--outside couplings may be arbitrary. Condition on every outside **original coordinate**. The retained quadratic matrix remains exactly `A_*`; the outside variables create only arbitrary affine coefficients and an output constant in `(X_1,X_2,Z,Y)`. Both branches above are uniform in all such affine terms. Therefore each conditional output density is bounded by the same number, and averaging gives

`boxed: ||p_(X^T A X)||_infinity <10.735.`   (5.3)

Cauchy interlacing preserves the three threshold eigenvalues in the ambient matrix.

This is the localization statement required by this slot: arbitrary shifts, arbitrarily distant outside fragments, unbounded outside supports, arbitrary outside self-curvature, and absence of all moments cost **exactly zero**. The constant `<10.735` is the same before and after arbitrary ambient extension.

Even if the outside law is decomposed into finite or countably many subprobability pieces of masses `m_j`, the j-th unnormalized conditional output contribution is at most `10.735 m_j`; summing gives exactly the same constant. No fragment diameter, count, or separation enters. What remains unsafe is normalizing certificate-active fragments before the whole-law estimate, in agreement with the live correction corpus.

## 6. Actual latest-partner inequality on the hyperbolic specialization

As a direct check against the newest completed account02/B14 report, specialize

`C=[[0,a],[a,0]]`.

Conditioning on the whole bank `Y=y` turns (1.1) into

`2aUV+hZ^2+alpha(y)U+beta(y)V+gamma(y)Z+eta(y)`.

The newest partner theorem therefore gives, on every conditioning fibre,

`boxed: ||p_(Q | Y=y)||_infinity <= |a|^(-1)+8/sqrt(|a h|).}`   (6.1)

The right side is independent of `y`; integrating proves the same unconditional inequality. This is a literal application of the completed partner theorem to a quadratic form containing arbitrary `Y^T H Y`, arbitrary diffuse `Z-Y` couplings, arbitrary translations, and unbounded product laws. The general-pair square compiler in Section 2 and the r34 leakage compiler then remove the need to commit to a nonvanishing `h`.

## 7. Why this advances the localization debt

The previous whole-product/square result required a genuinely disjoint square coefficient bounded away from zero. The previous random-slope result could pay diffuse leakage but did not exploit a simultaneously available square pivot. The present theorem closes their overlap at a **single physical receiver**: the third direction may migrate continuously from diagonal self-curvature into a diffuse cross bank without any blow-up of the density constant.

A stress family is

`h=t`,
`c=sqrt(1-t^2) m^(-1/2)(1,...,1)`, `0<=t<=1`,

with arbitrary symmetric `H`. Every individual cross coefficient tends to zero as `m->infinity`, while

`sqrt(h^2+||c||_2^2)=1`

for every `t`. The new theorem gives one uniform `<10.735` density bound simultaneously for all `m` and all `t`, including both degenerate endpoints `t=0` and `t=1`.

This is not a good-single-minor argument and does not impose moments or compactness.

## 8. Remaining obstruction

This does **not** prove full QFORM. The unpaid implication is now matrix-structural:

`QFORM-PAIR-PLUS-SHARED-COLUMN-EXTRACTION-OR-AGGREGATE-EXIT-v1` — from bare `s_3(A)>=1`, before active fragmentation, force either

1. an original-coordinate indefinite physical pair with quantitative `D,kappa` together with a disjoint receiver bank whose Schur/physical column has quantitative Euclidean norm, so the shared-receiver hybrid applies; or
2. one of the already completed whole-law ridge/projected-volume/grouped-bank/hub/pair exits.

Diffuse examples in the correction inbox show that no uniformly conditioned fixed principal minor can simply be assumed. The theorem here removes the analytic blow-up when a *given* third column trades self-curvature against diffuse leakage; it does not manufacture that column from the spectral hypothesis.

No law-uniform pointwise quadratic Fourier decay, rotated independence, bounded support, bounded diameter, fixed fragment count, arbitrary-joint coarea, or moment hypothesis was used.
