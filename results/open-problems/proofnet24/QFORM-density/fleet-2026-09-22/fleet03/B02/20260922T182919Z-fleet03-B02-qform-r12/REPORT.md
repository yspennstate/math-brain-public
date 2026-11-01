# fleet03/B02 — square plus one hyperbolic packet via an integrated/fractional estimate

Run: `20260922T182919Z-fleet03-B02-qform-r12`

Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM TARGET OPEN / WITHOUT_VERIFIED_BRAIN**.

## Exact target and correction-aware scope

The full target remains: for every dimension, every product law of independent real coordinates with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential-supremum bound for the density of `X^T A X`, or give a valid counterexample. No moment, compact-support, log-concavity, Gaussian, connected-support, or rotated-coordinate independence hypothesis is used here.

The live correction state rules out law-uniform pointwise quadratic-phase decay and also rules out the arbitrary-joint rank-three coarea bound and the proposed positive conditional-projection-density moment. This report does not use any of those interfaces. It also does not claim that a universal unweighted `L^1_t` characteristic-function estimate has been proved. Instead it derives a direct fractional-potential estimate that is strong enough for a new product-preserving branch.

## Completed compatible peer result actually used

The designated partner `fleet04/B02` had no completed current-QFORM handoff visible at the observation point, so none is invented.

I apply the completed compatible `fleet02/B02` theorem `QFORM-AFFINE-HYPERBOLIC-L2-v1`, source:

- `yspennstate/math-open-problems@81e2e89635a42476da8b2344c61f22d05436b726`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260922T170646Z-fleet02-B02-QFORM-r11/ADDENDUM_FRESH_O1_CORRECTION.md`
- read-back blob `2e193c242cb5edae6a0ebe59c1ea9c54088f1286`.

That result proves the `p=2` endpoint below. I re-run the same proof at general `p>1`, obtaining the `p=3` credit needed for the square-potential closure.

## Lemma 1: affine hyperbolic packet in every `L^p`, `p>1`

Let `X,U` be independent real random variables. Assume `X` has density `f` with `0<=f<=1`, and `U` has density `g` with `||g||_infinity<=M`. Let `a!=0`, let `h:R->R` be arbitrary measurable, and put

`T = 2 a X U + h(X)`.

Then for every `p>1`, `T` has an `L^p` density satisfying

`||p_T||_p <= p |a|^{-(1-1/p)} M^{1-1/p}.`                         (1)

### Proof

Set `beta=1-1/p`. Conditional on `X=x`, for `x!=0`,

`p_x(z) = [1/(2|a x|)] g((z-h(x))/(2 a x))`,

hence

`||p_x||_p=(2|a x|)^(-beta)||g||_p`.

Minkowski gives

`||p_T||_p <= (2|a|)^(-beta)||g||_p int f(x)|x|^(-beta) dx`.       (2)

Since `g` has mass one and cap `M`,

`||g||_p <= M^beta`.                                                (3)

Since `f` has mass one and cap one, the bathtub/rearrangement bound for the symmetric decreasing function `|x|^-beta` gives

`int f(x)|x|^-beta dx
 <= int_{-1/2}^{1/2}|x|^-beta dx
 = 2^beta/(1-beta)
 = 2^beta p`.                                                       (4)

Substituting (3)-(4) into (2) proves (1). For `p=2`, this is exactly

`||p_T||_2 <= 2 sqrt(M/|a|)`,

so the completed peer theorem is recovered as the endpoint actually used and extended here. For `p=3`,

`||p_T||_3 <= 3 |a|^(-2/3) M^(2/3)`.                              (5)

No pointwise oscillatory estimate occurs.

### Conditional-bank extension

Let `V` be any random element independent of `(X,U)`, and let `H(x,v)` be arbitrary measurable. Conditioning on `V=v`, applying (1), and then using Minkowski to mix over `v` gives

`||p_{2aXU+H(X,V)}||_p <= p |a|^{-(1-1/p)} M^{1-1/p}`.             (6)

This permits arbitrary additional terms and couplings that, after conditioning the independent `V` bank, enter only through the `X`-side function `H(X,V)`. It does not permit silently reusing coordinates from the `U` bank inside `V`.

## Lemma 2: a sharp-enough half-Riesz potential from an `L^3` density

Let `r` be a probability density with `||r||_3<=L`. Then uniformly in `y`,

`int r(s)|y-s|^(-1/2) ds <= 4 (4L/3)^(3/4)`.                       (7)

### Proof

For arbitrary `R>0`, split into `|y-s|<=R` and its complement. Holder with exponents `3` and `3/2` yields

`int_{|y-s|<=R} r(s)|y-s|^-1/2 ds
 <= L (int_{|u|<=R}|u|^-3/4 du)^(2/3)
 = 4 L R^(1/6)`.                                                    (8)

The complementary integral is at most `R^-1/2`, since `r` has mass one. Thus

`I(y)<=4 L R^(1/6)+R^-1/2`.                                        (9)

The minimizing radius satisfies `R^(2/3)=3/(4L)`. At this radius the first term is three times the second, giving exactly (7).

## Theorem: `QFORM-SQUARE-ONE-HYPERBOLIC-L3-v1`

Let `Z,X,U` be mutually independent real random variables and let `V` be any further random element independent of `(Z,X,U)`. Assume `Z` and `X` have probability densities bounded by one and `U` has density bounded by `M`. Let `d,a` be nonzero real numbers. Let

- `eta=eta(X,U,V)` be arbitrary measurable;
- `H=H(X,V)` be arbitrary measurable.

Define

`Q = d (Z+eta(X,U,V))^2 + 2 a X U + H(X,V)`.                       (10)

Then `Q` has an essentially bounded density and

`boxed(||p_Q||_infinity <= 8 sqrt(2) sqrt(M/(|a d|))).`            (11)

No independence is assumed between the completed-square shift `eta` and the residual term.

### Proof

Put

`R=2a XU+H(X,V)`.

By (6) at `p=3`,

`||p_R||_3 <= L := 3 |a|^-2/3 M^2/3`.                              (12)

Condition on `W=(X,U,V)`. For fixed `W=w`, the random variable

`Y_w=d(Z+eta(w))^2`

has a density on the appropriate half-line satisfying

`p_{Y_w}(u) <= |d|^-1/2 |u|^-1/2`.                                 (13)

Indeed, for `d>0`, the two inverse branches contribute at most

`[1+1]/[2 sqrt(d u)] = 1/sqrt(d u)`;

for `d<0` reflect the output. Therefore

`p_Q(y) <= |d|^-1/2 E |y-R|^-1/2
         = |d|^-1/2 int p_R(s)|y-s|^-1/2 ds`.                       (14)

Apply Lemma 2 and (12):

`||p_Q||_infinity
 <= 4 |d|^-1/2 (4L/3)^(3/4)
 = 4 |d|^-1/2 [4 |a|^-2/3 M^2/3]^(3/4)
 = 8 sqrt(2) sqrt(M/(|a d|))`.                                     (15)

This proves (11).

## Matrix/product-law interpretation

The theorem applies after completing one genuine original-coordinate square pivot `Z`: if the Schur residual contains one product-preserving hyperbolic packet `2a XU`, where `X` and `U` arise from disjoint independent original-coordinate banks and `U` has a dimension-free density cap `M`, while all remaining coordinates can be placed in an independent bank `V` whose interaction with this packet enters through `H(X,V)`, then the output density is bounded by (11). The square shift may depend arbitrarily on the entire remaining collection `(X,U,V)`.

This is strictly a different closure interface from the peer's two-hyperbolic-packet `L^1_t` theorem. The peer theorem requires two disjoint hyperbolic packets and gets direct `L^1_t`; the present theorem requires only one hyperbolic packet but also one nonzero physical square pivot. Thus it covers overlap geometries where a second disjoint hyperbolic packet is unavailable but a usable scalar pivot survives.

As a simple coefficient corollary, if `U=cY+U_0` with `Y` an original cap-one coordinate independent of `U_0`, then conditioning on `U_0` gives `||p_U||_infinity<=1/|c|`. Hence (11) becomes

`||p_Q||_infinity <= 8 sqrt(2) / sqrt(|a d c|)`                    (16)

for that product-preserving square-plus-star packet.

## Sanity application and comparison

For the five-coordinate family

`Q = epsilon X0^2 + 2 X0(X1+X3) + 2 X2 X4`,

when `epsilon!=0`, complete the first square:

`Q = epsilon [X0+(X1+X3)/epsilon]^2
    - (X1+X3)^2/epsilon + 2X2X4`.

The theorem with `Z=X0`, `X=X2`, `U=X4`, `a=1`, `M=1`, `d=epsilon` gives

`||p_Q||_infinity <= 8 sqrt(2) |epsilon|^-1/2`.                    (17)

This is intentionally not advertised as the best bound on this family: the completed fleet02/B02 two-hyperbolic theorem gives the stronger uniform bound `4`, including `epsilon=0`. Equation (17) is only a consistency check showing that the new one-packet mechanism is mathematically compatible with the known branch.

## What this does and does not settle

1. **Full conjecture:** OPEN. No universal structural extraction from the bare three-large-eigenvalue hypothesis is proved here.
2. **Essential boundedness:** proved for the precise square-plus-one-hyperbolic branch (10).
3. **Continuity:** not proved by this argument. The estimate is a fractional-potential/L^3 argument rather than direct `L^1_t` Fourier inversion.
4. **Universal unweighted characteristic-function `L^1`:** not proved here. Live owner control warns that this sufficient criterion should not be treated as the universal target. I do not convert a non-product or phase-Wiener example into a claimed exact-target counterexample without a valid product-law derivation.
5. **Product provenance:** preserved explicitly. `U` and `V` cannot secretly share original coordinates unless one separately proves the required conditional density statement.

## First unpaid implication

The next B02 structural obligation is now sharper:

`QFORM-SQUARE-ONE-HYPERBOLIC-EXTRACTION-v1` — from the surviving full-matrix three-large-eigenvalue geometry, prove a product-preserving dichotomy that yields either

- a nonzero physical square pivot and one hyperbolic packet with a dimension-free lower bound on `|ad|/M`, so that (11) closes the density; or
- one of the already completed pair/ridge/diffuse/two-hyperbolic branches,

without assuming a uniformly good fixed minor, a good Schur rank-two extraction, post-rotation independence, or the refuted conditional-density moment.

The dangerous residual regime is therefore the simultaneous near-zero-pivot / no-single-hyperbolic-packet branch, not the analytic smoothing of a square plus one packet.

## Source integrity

Mathematical dependency used: the completed fleet02/B02 affine-hyperbolic `L^2` proof cited above. The present proof extends its exact conditional-density/Minkowski/bathtub calculation to general `p>1`, then adds Lemma 2 and the physical-square fiber bound. No external numerical evidence is used as proof. No claim of novelty or full theorem is made.
