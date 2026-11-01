SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-23T01:30:54Z.
attacking: three-way overlapping product-provenance via source-bank randomization and averaged-frequency smoothing.

# Early substantive checkpoint: critical rank-two volume -> half-Riesz

Run: `fleet03-B01-20260923T013054Z-auto11`
Programme: `QFORM-DENSITY-3EIG-20260922`
Status: worked supporting implication; full QFORM remains OPEN.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Source boundary

Fresh owner control is QFORM-only, revision `2026-09-22.15`. This calculation consumes the sharp Jensen/volume-sampling Fourier argument in

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`

and the fractional-potential transducer in

`yspennstate/math-open-problems@2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

The pointwise law-uniform scalar Fresnel estimate remains false and is not used.

## The calculation

Let `M=A[I,J]` be a physical cross block between disjoint ORIGINAL-coordinate banks and set

`Z_2=e_2(M^T M)=sum_{|S|=|T|=2} det(M[S,T])^2 > 0`.

Give the squared `2 x 2` minors their normalized volume-sampling weights and let `alpha_i` be the row inclusion marginals, so `0<=alpha_i<=1` and `sum_i alpha_i=2`. Assume

`h:=max_i alpha_i < 1`.

Choose

`q=max(1,2h)`, so `1<=q<2` and `alpha_i<=q/2`.

Repeating the sharp Hausdorff-Young / Brascamp-Lieb proof of the current 3-volume theorem with 2-volume weights gives, for the corresponding quadratic-plus-affine residual `R`, retaining arbitrary self phases and outside-conditioned affine terms,

`|phi_R(t)| <= min(1, B_q |t|^{-1/q})`,

where

`B_q=[e^2 q^{-1} pi^2 Z_2^{-1/2}]^{1/(2q)}`.

Indeed the determinant expansion over 2-minors gives the BL factor

`Z_2^{-1/2} prod_i alpha_i^{-alpha_i/2} prod_j (1-beta_j)^{-(1-beta_j)/2}`,

sharp Hausdorff-Young at output exponent `q/alpha_i>=2` cancels the powers of `alpha_i`, and the row and column entropy factors each cost at most `e`, yielding

`E F_t^q <= e^2 q^{-1} (pi/|t|)^2 Z_2^{-1/2}`.

Because `q<2`, the decay exponent `1/q` is strictly larger than `1/2`. Applying the source fractional-Riesz formula with gamma=1/2,

`H_{1/2}(R):=sup_s E|R-s|^{-1/2}`

therefore gives

`H_{1/2}(R) <= C(q) Z_2^{-1/8}`,

with the explicit constant

`C(q)=4 sqrt(2e) q^{-1/4}/(2-q)`.

At the diffuse endpoint `h<=1/2` one may take `q=1`, hence

`H_{1/2}(R) <= 4 sqrt(2e) Z_2^{-1/8} < 9.327 Z_2^{-1/8}`.

This is the critical endpoint missed by the unconditional regularized-determinant rank-two envelope: a `|t|^{-1/2}` envelope alone logarithmically misses the half-Riesz integral, while the 2-volume marginal gate upgrades the coupled cross-block decay to `|t|^{-1/q}` with `q<2`.

## Immediate square-peel consequence

If one independent original coordinate has a nonzero physical pivot `a`, exact square completion writes

`Q=a(X_i+ell)^2+R`.

The dependence-safe square peel then yields

`||p_Q||_infinity <= |a|^{-1/2} H_{1/2}(R)`

and therefore

`||p_Q||_infinity <= C(q) |a|^{-1/2} Z_2^{-1/8}`.

For `max alpha_i<=1/2` this is

`||p_Q||_infinity < 9.327 |a|^{-1/2} Z_2^{-1/8}`.

This proves essential boundedness in the stated branch. Continuity is not yet claimed from this half-Riesz transducer alone.

## Remaining obligation

This does not close N3 because N3 does not supply a lower bound on the scalar pivot `|a|`, and a rank-two cross block may have a row volume marginal arbitrarily close to one. The useful new structural target is therefore: in the low-cross-rank N3 survivor, either obtain a rank-two cross block with `max alpha_i <= 1-delta` and enough `Z_2` before the scalar pivot vanishes, or route the high-marginal limit to the already-paid hub/null-coloop mechanisms. The calculation above identifies the exact analytic currency needed for that split.
