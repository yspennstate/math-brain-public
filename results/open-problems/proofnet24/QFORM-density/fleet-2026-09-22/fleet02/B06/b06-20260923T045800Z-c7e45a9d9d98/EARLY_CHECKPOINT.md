# fleet02/B06 early checkpoint — non-null star fractional potential

Run `b06-20260923T045800Z-c7e45a9d9d98`; programme `QFORM-DENSITY-3EIG-20260922`; assignment Curved fiber integration.

First unpaid implication attacked: extend the exact-null scalar/dependent-pair mechanism into a genuinely non-null coupled scalar regime without taking a fiber supremum or assuming independence after rotation.

Let `X` be independent of `Y`, with density `f_X<=1`. Let `Z=z(Y)` have a one-dimensional density bounded by `L`, and let `W=w(Y)` be arbitrary. For any real `a`, set

`T=a X^2+2XZ+W`.

A direct original-coordinate split gives, for every interval `I` of length `eps`,

`P(T in I) <= 2 sqrt(2 L eps)`.

For `a=0`, split at `|Z|=r`: the two contributions are at most `2Lr` and `eps/(2r)`. For `a!=0`, write `u=X+Z/a`. On `|u|<=r`, independence of `X,Z` gives density cap `min(1,|a|L)` for `X+Z/a`, hence probability at most `2r min(1,|a|L)`. On `|u|>r`, each monotone branch of `a u^2` has derivative at least `2|a|r`, so the conditional preimage length is at most `eps/(|a|r)`. Optimizing yields the displayed bound, uniformly in `a` and in the arbitrary dependent shift `W(Y)`.

Consequently, for every `0<alpha<1/2`,

`H_alpha(T):=sup_t E|T-t|^{-alpha} <= 16^alpha L^alpha/(1-2alpha)`;
in particular `H_(1/4)(T)<=4 L^(1/4)`.

The endpoint `alpha=1/2` is genuinely unavailable under the same assumptions: for iid cap-one `X,C~Unif[-1/2,1/2]`,

`T=X^2+2XC+C^2=(X+C)^2`

has `E T^(-1/2)=E|X+C|^(-1)=infinity`. Thus a single non-null star supplies every subcritical half-Riesz potential but not the half-Riesz endpoint required by the square peel.

Planned full splice: Claude's completed coordinate-hyperbola peel at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` requires only `H_(1/4)`, so an exact zero-diagonal physical pair followed by such a star residual is paid dimension-free. Designated partner fleet03/B06 r25 (`math-open-problems@1e7aa194ee0cd3c2981afdeb2ddf66acf53b87fe`) separately pays the large-third-volume branch; the survivor is the low-Delta3/rank-two tube where the new hyperbola-or-second-curvature receiver is relevant.

Status: substantive checkpoint only; full QFORM remains open.
