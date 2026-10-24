SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B01, 2026-09-24T05:06:42Z.
attacking: the exact-zero/single-edge finite-leak endpoint; extract a law-uniform fractional-potential gain from one physical edge, upgrade a zero-diagonal edge to half-Riesz by rearrangement, then spend the proved square peel before any small determinant is inverted.

# account02/B01 — one physical edge gives quarter-Riesz; a zero-diagonal edge gives half-Riesz

Run: `20260924T050513Z-account02-B01-qform-auto11`.

Status: **NEW SUPPORTING THEOREMS / ESSENTIAL STEP APPLIED / FULL QFORM OPEN**.

The target throughout is the unrestricted product-law statement: independent original-coordinate inputs with densities at most one, arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one, no moment/log-concavity/compact-support/connected-support assumption, no rotation of the independent coordinates. Continuity is kept separate from essential boundedness.

The phase-aligned-density obstruction remains in force: no positive law-uniform pointwise power decay for a one-dimensional quadratic phase is used or claimed.

## 1. Input from the required 20260922T211500Z Fourier report

The source is exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

I use two proved statements from Section 4.

**Fractional-potential interface.** For `0<alpha<1`,

`H_alpha(Z):=sup_s E |Z-s|^(-alpha)
 <= c_alpha int_R |t|^(alpha-1) |phi_Z(t)| dt`,

`c_alpha = 2^(1-alpha) Gamma((1-alpha)/2)/(2 sqrt(pi) Gamma(alpha/2))`.

If `|phi_Z(t)| <= min(1,B |t|^(-b))` with `b>alpha`, then

`H_alpha(Z) <= c_alpha * 2b B^(alpha/b)/(alpha(b-alpha))`.

In particular for `alpha=1/4,b=1/2`,

`H_(1/4)(Z) <= 16 c_(1/4) B^(1/2)`.

**Square peel.** If a literal original coordinate has `A_00=a!=0`, scalar completion gives

`Q=a(X_0+h)^2+S`,

and

`||p_Q||_inf <= |a|^(-1/2) H_(1/2)(S)`.

These are the actual inequalities spent below.

## 2. Theorem: every nonzero physical edge gives a quarter-Riesz bound

### `QFORM-PHYSICAL-EDGE-QUARTER-RIESZ-v1`

Let `R` be an arbitrary real quadratic polynomial in independent original-coordinate cap-one variables. Suppose two distinct original coordinates `X,Y` have off-diagonal coefficient `mu!=0`, so the cross term is `2 mu X Y`. The diagonal coefficients of `X,Y`, all couplings to the other coordinates, all remaining quadratic terms, and all affine terms are arbitrary.

Then

`H_(1/4)(R) <= C_edge |mu|^(-1/4)`,

where

`C_edge = 16 c_(1/4) pi^(1/4)
        = 3.179662567631707...`.

### Proof

Condition on every coordinate except `X,Y`. For a fixed outside value, the remaining polynomial has the form

`R_z(X,Y)=aX^2+2mu XY+cY^2+lX+mY+d`.

For `t!=0`, put

`h_t(y)=f_Y(y) exp(i t(cy^2+my))`.

With the Fourier convention `hat h(xi)=int h(y)e^(i xi y)dy`, the conditional characteristic function is

`int f_X(x) exp(i t(ax^2+lx+d)) hat h_t(2mu t x) dx`.

Cauchy-Schwarz, `||f_X||_2<=1`, the change of variables `xi=2mu t x`, and Plancherel give

`|phi_(R_z)(t)|^2
 <= int |hat h_t(2mu t x)|^2 dx
 = (1/(2|mu t|)) int |hat h_t(xi)|^2 dxi
 = (pi/|mu t|) ||h_t||_2^2
 <= pi/(|mu t|)`.

The bound is uniform in the outside value, hence

`|phi_R(t)| <= min(1, sqrt(pi/|mu t|))`.

Now apply the required fractional-potential lemma with

`alpha=1/4`, `b=1/2`, `B=(pi/|mu|)^(1/2)`.

It yields

`H_(1/4)(R)
 <= 16 c_(1/4) (pi/|mu|)^(1/4)
 = C_edge |mu|^(-1/4)`.

QED.

This is an averaged-frequency replacement for the false scalar quadratic-phase pointwise estimate. The `|t|^-1/2` gain comes from the literal bilinear edge and two-dimensional Plancherel, not from any uniform Fresnel decay of a single arbitrary law.

## 3. Theorem: zero diagonal at one endpoint upgrades the edge to half-Riesz

### `QFORM-ZERODIAG-EDGE-HALFRIESZ-v1`

Under the same product-law hypotheses, suppose for distinct literal original coordinates `X,Y`

`A_XX=0`, `A_XY=mu!=0`.

All other entries of the ambient matrix, including `A_YY`, all couplings to outside coordinates, and all affine terms are arbitrary. Then

`boxed: H_(1/2)(R) <= 4 sqrt(2) |mu|^(-1/2)`.

### Proof

Condition on every coordinate except `X,Y`. For fixed outside coordinates and any target value `s`, write

`R-s = 2 X(mu Y+r) + T(Y)`

for suitable real `r` and arbitrary quadratic/affine `T`.

Use the elementary cap-one rearrangement fact: if `W` has density at most one, then for every `k!=0` and every real `c`,

`E |kW+c|^(-1/2) <= 2 sqrt(2) |k|^(-1/2)`.

Indeed `kW+c` has density at most `1/|k|`; among probability densities with cap `M`, the integral against the symmetric decreasing kernel `|u|^-1/2` is maximized by density `M` on the centered interval of length `1/M`, and equals `2 sqrt(2M)`.

First integrate in `X`, keeping `Y` fixed. Since the coefficient of `X` is `2(mu Y+r)`,

`E_X |R-s|^(-1/2)
 <= 2 |mu Y+r|^(-1/2)`.

Then integrate in `Y` and use the same rearrangement lemma again:

`E_Y |mu Y+r|^(-1/2) <= 2 sqrt(2) |mu|^(-1/2)`.

Thus, uniformly in `s` and in every outside conditioning value,

`E |R-s|^(-1/2) <= 4 sqrt(2) |mu|^(-1/2)`.

Average over the outside coordinates and take the supremum over `s`. QED.

No diagonal assumption is made on `Y`; arbitrary same-bank quadratic curvature survives. The theorem is a value-space averaged estimate and is compatible with the phase-aligned-density refutation.

## 4. Full-target-relevant compiler obtained by spending the required square peel

### `QFORM-SQUARE-TO-ZERODIAG-EDGE-v1`

Suppose a literal original coordinate `X_0` has `A_00=a!=0`. Complete it exactly:

`Q=a(X_0+h)^2+S`.

If the scalar Schur complement `S` has two remaining literal original coordinates `j,k` with

`S_jj=0`, `S_jk=mu!=0`,

then the required source square peel and the preceding theorem give

`boxed: ||p_Q||_inf <= 4 sqrt(2) |a mu|^(-1/2)`.

All other coefficients of `S` are arbitrary. In particular there is no reciprocal determinant, no smallest-singular-value loss, no moment assumption, and no rotation of the input variables.

This directly removes the exact-zero-diagonal single-edge corner of the preceding B01 finite-leak endpoint whenever one earlier literal scalar pivot is available.

## 5. A concrete target family paid uniformly

For `K>=0`, set `mu=sqrt(K+1)` and

`A_K = [[1,0,0],
       [0,0,mu],
       [0,mu,K]]`.

The lower `2x2` block has characteristic polynomial

`lambda^2-K lambda-(K+1)=(lambda-(K+1))(lambda+1)`,

so

`spec(A_K)={1,-1,K+1}`.

Thus every `A_K` is in the exact owner target. The first coordinate is a pivot with `a=1`; its Schur complement is the lower block, which has one zero diagonal and edge `mu`.

Therefore, for every independent cap-one product law,

`boxed: ||p_(X^T A_K X)||_inf
 <= 4 sqrt(2) (K+1)^(-1/4)
 <= 4 sqrt(2)
 = 5.65685424949... .`

This is uniform even as the other diagonal coefficient `K` tends to infinity.

The required D/D'/D5 volume receivers are genuinely unavailable on this family for a structural reason: in dimension three every disjoint original-coordinate cross block has rank at most one, hence every third and fifth cross volume is exactly zero. Thus the completed 20260922T211500Z source is used both positively (fractional potential and square peel) and to identify the concrete volume obstruction.

## 6. The quarter exponent is genuinely needed for a generic edge

One cannot replace Theorem 2 by a law-uniform half-Riesz estimate for every nonzero edge. For example, with independent cap-one `X,Y` whose sum has positive density at zero (e.g. centered unit intervals), take

`R=(X+Y)^2 = X^2+2XY+Y^2`.

The physical edge is nonzero, but

`H_(1/2)(R) >= E |R|^(-1/2)=E |X+Y|^(-1)=infinity`.

So the generic edge only supplies a sub-half potential without an additional transverse resource. The zero-diagonal endpoint is exactly where the rearrangement argument upgrades the exponent to `1/2`.

This is a concrete obstruction to the stronger shortcut “one physical edge automatically pays an outer square peel”.

## 7. Newest designated partner account03/B01 applied at an actual inequality

The newest compatible account03/B01 result read in this run is

`QFORM-TWO-HUB-HUB-CONDITIONAL-LR-v1` and its two-sided corollary at

`yspennstate/math-open-problems@706d8b161a7c4c19ad423130b43ce67a50fac60f`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260924T045746Z-account03-B01-qform-auto11-r44/REPORT.md`.

At `r=2`, for two literal hubs, a row-rank-two slope bank `B`, and a source-disjoint hyperbolic pair with coefficient `c`, it proves—even when both hyperbolic variables shift both hubs and the bank phase is arbitrary—

`||p_Q||_inf <= 3 det(BB^T)^(-1/6) |c|^(-1/3)`.

Apply it to the target-valid family, for `k>=2`,

`Q_k=2k(H_1Y_1+H_2Y_2)+2H_1U+2H_2V+2k^(-2)UV`.

Here `B=k I_2`, so `det(BB^T)=k^4`, and `c=k^-2`. Hence the partner gives the scale-free inequality

`boxed: ||p_(Q_k)||_inf <= 3`.

Without the `UV` edge, the matrix is the direct sum of two three-coordinate stars with nonzero eigenvalues `+-sqrt(k^2+1)`. Adding the `UV` edge has operator norm `k^-2`, so Weyl gives four eigenvalues of modulus at least `sqrt(k^2+1)-k^-2>1` for `k>=2`; the family is therefore in the owner target. This uses the new two-sided-entanglement feature, not merely the older source-disjoint corollary.

Conversely, the three-coordinate stress family `A_K` above has only one coordinate outside any two chosen hubs, so every two-hub slope matrix into that bank has row rank at most one and `det(BB^T)=0`. The newest partner theorem does not cover that endpoint; the present zero-diagonal edge compiler does.

## 8. Remaining implication

The first unpaid B01 implication is now

`QFORM-FINITELEAK-NONZERO-DIAGONAL-SINGLEEDGE-OR-RANK1-ARROWHEAD-v1`.

What has been removed:

- any nonzero physical edge carries a universal quarter-Riesz currency, with arbitrary ambient curvature;
- a zero-diagonal endpoint upgrades that currency to half-Riesz;
- an earlier nonzero scalar pivot then converts the half-Riesz bound to an actual density bound with no determinant loss.

The genuine survivor is the single-edge / row-rank-one arrowhead geometry when both local diagonals remain and can approach the rank-one-square degeneracy. The example `(X+Y)^2` shows why a bare edge cannot supply half-Riesz there. The next mechanism has to force a third product-preserving resource from the target spectrum—another literal edge, grouped square, hub slope, or projected crossing—and combine it with the quarter-potential before paying any coefficient that may vanish.

Full QFORM remains OPEN. Continuity is not claimed by the new edge-to-half-Riesz compiler.
