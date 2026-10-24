# Two obstructions to the proposed rank-three coarea reduction

Programme: QFORM-DENSITY-3EIG-20260922. Interactive record 20260922T180015Z-pair-log.

Status: explicit counterexamples to intermediate statements, not to the independent-input conjecture. The full conjecture remains unresolved by this report.

## Source being tested

The owner-message text in `yspennstate/math-research-brain@94e277612994fca8b76e71bcc1ee2b79db95f1d5:scheduled_tasks/README.md`, blob `8eaee588745992a04a6dec7d2f822e392b2d6268`, control revision 2026-09-22.9, proposes:

1. A rank-three quadratic pushforward bound `||p_Q||_infinity <= K ||rho||_infinity^(2/3)` for any joint probability density rho, and uses this to label the general exact-rank-three independent-input case proved.
2. A dimension-free bound on `E ||rho_(Y|W)||_infinity^(2/3)` for a three-dimensional orthogonal projection Y of a product law, conditioned on its orthogonal complement W.

Neither intermediate statement is true with these quantifiers. The source message and all historical work should be preserved, but its proposed deductions must not be treated as proved premises. The target conjecture and the exclusive QFORM assignment are unchanged.

## 1. A unit joint density with arbitrarily large quadratic output density

Fix delta>0 and set `R=1/(2*pi*delta)`. Let

`E_delta = {(x,y,z): |z|<=R, 0<=x^2+y^2-z^2<=delta}`.

For each fixed z the planar section is the annulus with squared radii z^2 and z^2+delta; its area is exactly pi*delta. Therefore

`vol(E_delta)=2*R*pi*delta=1`.

Thus `rho_delta=1_(E_delta)` is a compactly supported probability density with essential supremum one. For `Q=x^2+y^2-z^2`, and every Borel set H, planar polar coordinates give

`P(Q in H)=2*R*pi*Leb(H intersect [0,delta])`
`           =delta^(-1)*Leb(H intersect [0,delta])`.

Consequently Q is exactly uniform on [0,delta], and

`||p_Q||_infinity=1/delta`, while `||rho_delta||_infinity=1`.

The eigenvalues are exactly 1,1,-1. Letting delta tend to zero refutes the proposed inequality for every finite K, including the corrected exponent 2/3. Scaling determines a possible exponent; it does not prove an inequality with that exponent.

This is NOT a counterexample to the original QFORM conjecture: the three coordinates under rho_delta are dependent. The example pinpoints why an unconditional projection-density cap alone cannot prove the conjecture. Cancellation of the singularity at the cone vertex is only a local fact; the measure can concentrate in a long, thin shell away from the vertex. Total probability one does not bound shell probability by a constant times shell width.

The failure persists for smooth compactly supported joint densities with the same cap. Convolve rho_delta with a nonnegative smooth probability bump supported in a sufficiently small ball. The convolved density still has supremum at most one. On the compact support, choose the bump radius so that the change in Q is at most delta/4. The new output lies in [-delta/4,5*delta/4], and any output density must have essential supremum at least 2/(3*delta).

Claim ID: QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1.

## 2. The conditional 2/3 moment diverges for independent uniform inputs

Let m>=2, n=3m, and let all X_i be independent Uniform[0,1]. Split the coordinates into three disjoint blocks of m. In each block let `u=(1,...,1)/sqrt(m)`. Let E be the three-dimensional space spanned by these three block-constant unit vectors. Set `Y=P_E X` (using any orthonormal coordinates on E) and `W=P_(E_perp)X`.

Orthogonal coordinates (Y,W) preserve the unit joint density of the cube. If V(w) is the three-dimensional volume of the cube fiber over w, then

`p_W(w)=V(w)`,
`||p_(Y|W=w)||_infinity=1/V(w)`

for almost every w with V(w)>0. Hence the proposed moment equals

`E ||p_(Y|W)||_infinity^(2/3)=integral V(w)^(1/3) dw`.       (2.1)

Here dw is Euclidean Lebesgue measure on E-perp. This is an unnormalized fiber integral, not an assertion that conditional densities remain bounded by one.

### Exact one-block fiber integral

For one m-dimensional cube, let L(w) be its fiber length in direction u. Up to a null set, each fiber enters the cube through a unique lower facet x_i=0. The orthogonal projection of that facet onto u-perp has (m-1)-dimensional Jacobian `|u_i|=1/sqrt(m)`. Writing the other facet coordinates as t_1,...,t_(m-1) in [0,1], the fiber length is

`L=sqrt(m)*(1-max_j t_j)`.

The interiors of the projected entering facets are disjoint. Therefore, for alpha>-1,

`J_m(alpha):= integral L(w)^alpha dw`
` = m^((alpha+1)/2) * integral_[0,1]^(m-1) (1-max t)^alpha dt`
` = m^((alpha+1)/2) * Gamma(m)*Gamma(alpha+1)/Gamma(m+alpha)`. (2.2)

The last identity follows directly by integrating the maximum, whose distribution function is r^(m-1). The checks `J_m(0)=sqrt(m)` and `J_m(1)=1` recover the projection volume and cube volume respectively.

The three coordinate blocks are orthogonal and independent, so V is the product of their fiber lengths and (2.1) factorizes. Taking alpha=1/3 gives the exact formula

`E ||p_(Y|W)||_infinity^(2/3)`
` = m^2 [Gamma(m)*Gamma(4/3)/Gamma(m+1/3)]^3`
` ~ Gamma(4/3)^3 * m -> infinity`.                          (2.3)

An elementary proof of the asymptotic, avoiding any gamma-ratio theorem, follows from (2.2): substitute x=m(1-r) into the maximum integral. The rescaled integrand tends to exp(-x)*x^alpha and is dominated, for m>=4, by exp(-x/2)*x^alpha; dominated convergence gives `J_m(alpha) ~ Gamma(alpha+1)*m^((1-alpha)/2)`.

This falsifier DOES use independent cap-one inputs. The false statement is the proposed conditional-moment bound, not the QFORM conclusion. It applies equally to an admissible full-rank matrix: choose

`A=P_1+P_2-P_3+(1/128)*(I-P_E)`.

The eigenvalues are 1,1,-1 and 1/128 repeated 3m-3 times; Y is exactly its three-large-direction projection. Thus the proposed conditional-moment gate fails even inside the original matrix/input class.

For m>=32 this family lies within the earlier spectral-window supporting theorem, because the high-window projection is P_E and its coordinate diagonal is 1/m. Its divergent conditional moment therefore should not be confused with large output density.

More generally, for 0<s<2 the same calculation gives `E ||p_(Y|W)||_infinity^s=J_m(1-s)^3`, asymptotic to `Gamma(2-s)^3*m^(3s/2)`. In particular reducing the positive exponent below 2/3 does not produce a dimension-free bound for this family.

Claim ID: QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1.

## Consequence for the programme

Do not claim the unrestricted exact-rank-three conjecture solved by an arbitrary joint-density coarea bound. Do not use a universal positive conditional-density moment as an unpaid premise with the expectation that it is true. Preserve the actual product-source geometry through or before the curved integration.

The companion PAIR_LOG_THEOREM.md supplies a constructive alternative for a genuinely product-preserving two-coordinate pivot. It handles zero scalar pivots when a quantitative indefinite two-coordinate block is available. It does not claim an exhaustive reduction for arbitrary admissible A.
