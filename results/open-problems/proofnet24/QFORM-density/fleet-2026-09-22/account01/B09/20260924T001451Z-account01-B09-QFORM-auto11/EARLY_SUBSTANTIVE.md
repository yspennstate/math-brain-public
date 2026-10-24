# Early substantive calculation — account01/B09 — 2026-09-24

Target remains the unrestricted QFORM bounded-density conjecture; this file records a supporting calculation, not a full solution.

## A V-phase-stable square–hyperbola estimate

Let `(U,V)` have an arbitrary joint probability density `rho<=M`, let `W` be independent of `(U,V)` with density `<=S`, let `H:R->R` be arbitrary measurable, and let `a,b` be nonzero. Set

`T = a U^2 + H(V) + 2 b V W`.

The same bound as the account02/B09 square–hyperbola theorem survives the arbitrary `V`-only phase:

`||p_T||_infinity <= 3*2^(2/3) M^(2/3) S^(2/3) |a|^(-1/3)|b|^(-2/3)`.

Proof skeleton. Scale first to `a=b=1`. For a target `t`, split the coarea density at `|V|=r`.

For `|V|<=r`, integrate in `U`. The two roots contribute at most

`M (t-H(v)-2vw)_+^(-1/2)`.

For each fixed `v!=0`, the random variable `2vW` has density at most `S/(2|v|)`. The one-sided inverse-half bathtub inequality

`sup_c E (c-Z)_+^(-1/2) <= 2 sqrt(L)`

for every probability density `p_Z<=L` therefore gives

`E_W (t-H(v)-2vW)_+^(-1/2) <= sqrt(2S/|v|)`.

Hence the small-`V` contribution is at most

`M sqrt(2S) int_{-r}^r |v|^(-1/2) dv = 4 sqrt(2) M sqrt(Sr)`.

For `|V|>r`, integrate first in `W`; `H(v)` is only a translation of the target and the contribution is at most `S/(2r)` after integrating the hub density. Thus

`||p_T||_infinity <= 4 sqrt(2) M sqrt(Sr) + S/(2r)`.

Optimizing `r^(3/2)=sqrt(S)/(4 sqrt(2)M)` gives the displayed constant, exactly as in account02/B09 r15. Scaling gives the general `a,b` statement. The proof gives the same constant times interval length. Continuity is not claimed.

## Immediate near-singular physical-pair consequence

Let a literal physical pair be integrated in an orthonormal coefficient basis `(e,k)` with pair core

`B=tau e e^T + sigma k k^T`,

and suppose on an active disjoint leaf bank `I` the pair-to-leaf cross block is exactly kernel-aligned and rank one,

`A[I,H]= r k^T`,

while the active leaf block is zero. After the coefficient-space orthogonal change inside the two-dimensional hub integral,

`Q = tau U^2 + sigma V^2 + 2 V <r,X_I>`.

The hub joint density remains bounded by one (no independence is asserted after rotation), and the product-projection estimate gives

`||p_<r,X_I>||_infinity <= sqrt(2)/||r||_2`.

Applying the new estimate with `H(v)=sigma v^2` yields, uniformly in the second pair eigenvalue `sigma`,

`||p_Q||_infinity <= 6 |tau|^(-1/3)||r||_2^(-2/3)`.

Moreover the exact overlap-two packet is

`Omega_(2,H)=tau^2[(sum_i r_i^2)^2-sum_i r_i^4] <= tau^2 ||r||_2^4`,

so whenever the packet is positive,

`||p_Q||_infinity <= 6 Omega_(2,H)^(-1/6)`.

Thus the pure kernel-aligned collinear star does not acquire any determinant/minimum-singular-value loss as the second physical-pair eigenvalue passes through zero. The remaining singular-collar issue is genuinely the entangled same-leaf curvature/transverse-cross problem, not the small second eigenvalue by itself.
