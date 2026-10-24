# Prepublication source refresh and no-pivot splice

Run `20260922T233555Z-qform-r19-b06`, account01/B06.

After the main theorem in `REPORT.md` was committed, the required path-specific source history was refreshed. The newest source in `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/` is not merely `e5f71d79eff325201dd0274053d20268ce65b837`; it also includes the later Claude-attributed commit

`yspennstate/math-open-problems@2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`

(`QFORM: n = 3 theorem, pivot reduction, hub bounds`). The synthesis index at `472b70df7d1edbb3afac23269bc2e4368ae0e371` explicitly pins both source commits and says the unrestricted conjecture is still open, reduced to a no-pivot obligation. I read the later source before final handoff. It does not invalidate `QFORM-CURVATURE-WEIGHTED-PHYSICAL-FIBER-COVER-v1`; instead it gives a sharper structural place to use it.

The later source proves, among other things:

* physical dimension `n=3` with all three eigenvalues of modulus at least one has density at most `20`, including arbitrary linear terms;
* a fixed-dimension `O(n log n)` bound;
* the full conjecture is equivalent to the no-pivot regime (for a fixed small threshold `c`): all physical diagonals and all physical `2x2` principal determinants are `<c` in magnitude;
* for exact rank three, leverage at most `1/50` everywhere is already paid by the volume-sampling Fourier theorem, with density at most `40`;
* the remaining no-pivot/hub gluing statement is still open.

## New structural splice — `QFORM-NOPIVOT-HEAVY-LEVERAGE-SPREAD-HUB-v1`

Let

`A=R Lambda R^T`, `R^T R=I_3`, `|lambda_k|>=1`

be exact rank three. Fix `0<c<=1/10` and assume the physical no-pivot inequalities

`|A_ii|<c` for every `i`,
`|A_ii A_jj-A_ij^2|<c` for every `i!=j`.                               (S.1)

If all row leverages `ell_i=||r_i||^2` are at most `1/50`, the later source already gives `||p_Q||_infinity<=40`. Otherwise choose `i` with

`ell_i>1/50`.                                                          (S.2)

Put the physical hub vector

`h=(A_ij)_{j!=i}`.                                                     (S.3)

Then

`||h||_2^2 = (A^2)_ii-A_ii^2
            = r_i^T Lambda^2 r_i-A_ii^2
            >= ell_i-c^2
            > 1/50-c^2`,                                              (S.4)

because `Lambda^2>=I_3`. On the other hand (S.1) gives, for every `j!=i`,

`A_ij^2 <= |A_ii A_jj|+|A_ii A_jj-A_ij^2|
          < c^2+c <=2c`,                                              (S.5)

so

`||h||_infinity < sqrt(2c)`.                                          (S.6)

Therefore every exact-rank-three no-pivot survivor outside the already-paid diffuse branch contains a quantitatively spread hub satisfying

`||h||_2 > sqrt(1/50-c^2)`,
`||h||_2^2/||h||_infinity^2 > (1/50-c^2)/(2c)`.                        (S.7)

For `c<=1/10`, the first lower bound is at least `0.1`, while the effective support ratio in (S.7) grows like `1/(100c)` as the no-pivot threshold is tightened.

This is an exact structural consequence, not a full density bound. It shows that the heavy-leverage alternative left by the later source cannot be an isolated physical spike: no-pivot forces it to couple to a genuinely spread original-coordinate linear form.

## Product-law payment for the hub linear form

The designated account02/B06 partner theorem is also applicable here at `k=1`. Since `X_i` is independent of `X_-i`, the scalar linear form

`L_i=sum_{j!=i} A_ij X_j = h dot X_-i`

has, after normalizing `h/||h||_2`, a one-dimensional orthogonal-product projection density cap at most `sqrt(e)`. Rescaling therefore gives the actual inequality

`||p_{L_i}||_infinity <= sqrt(e)/||h||_2
 < sqrt(e)/sqrt(1/50-c^2)`.                                           (S.8)

For `c<=1/10`, the right side is `<10 sqrt(e)`. This does **not** by itself bound `2X_i L_i+R(X_-i)`: the live corrections explicitly forbid replacing the dependent residual by an independent convolution, and a product term alone can have a logarithmic density singularity. What (S.8) supplies is a source-valid, dimension-free product-linear input for the later source's open hub-gluing step.

Thus the exact-rank-three no-pivot proof graph can now be stated more sharply:

1. `max ell_i<=1/50`: later-source Theorem D branch, density `<=40`;
2. `max ell_i>1/50`: (S.4)-(S.8) force a spread hub with a dimension-free scalar projection cap; the unpaid step is to glue this hub to the residual rank-two curvature without taking a conditional fibre supremum or assuming independence from the residual.

This splice is fully compatible with the curvature-weighted cover theorem in `REPORT.md`: the latter supplies two-dimensional transverse product caps and anisotropic reciprocal-gradient kernels; the new source says the global full-target reduction should now be driven through the no-pivot/hub survivor rather than through a search for a uniformly good physical pair.

No source correction observed at the refresh invalidates the main theorem. Full QFORM remains open, and continuity remains unproved here.
