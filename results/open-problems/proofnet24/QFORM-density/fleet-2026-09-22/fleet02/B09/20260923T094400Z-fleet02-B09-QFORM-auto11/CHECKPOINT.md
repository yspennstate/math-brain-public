SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-23T09:44:00Z.
attacking: the exact small-disjointness endpoint of the two-hub mixed frame; classify rho=0 in source coordinates and test whether high leverage really forces a good physical minor while retaining a dense same-side smoother.

# Substantive checkpoint — exact rho=0 two-frame geometry and a strict-N3 obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

## 1. First unpaid implication

The newest completed designated-partner report is fleet03/B09 r26, `QFORM-K1-ANISOTROPY-TO-AUGMENTED-PLUCKER-OR-LOCALIZATION-v1`. It proves, for a whitened two-cross-column frame `U`, the exact collision identity

`rho = 1-sum_i ell_i^2 + sum_(i<j) w_ij^2`,

where `ell_i=||u_i||^2`, `w_ij=det(u_i,u_j)^2`, and `rho` is the probability that two iid Pluecker bases are disjoint. In particular small rho forces a high-leverage physical row. The still-unpaid implication is to understand what that localization means for the actual quadratic form without turning a small matrix coefficient into a small random perturbation.

This checkpoint resolves the **exact endpoint rho=0** structurally and shows that high leverage does *not* imply a universal-scale physical principal minor, even under the full three-large-eigenvalue hypothesis.

## 2. Exact support classification at rho=0

Let `U in R^(N x 2)` have orthonormal columns and let `w_ij=det(u_i,u_j)^2`. If `rho=0`, then any two positive-weight edges `{i,j}` and `{k,l}` intersect. A pairwise-intersecting simple graph is either a star or is supported on one triangle. Therefore exactly one of the following holds:

1. **star/coloop:** there is a physical index `s` contained in every positive Pluecker basis. Then all rows `u_j`, `j!=s`, are collinear. Since `U^T U=I_2`, the special row has leverage `||u_s||^2=1`, and after an orthogonal change of the deterministic two-dimensional coefficient labels one may write
   `u_s=(0,+/-1)`, `u_j=(a_j,0)` for `j!=s`, with `sum_(j!=s)a_j^2=1`;
2. **triangle:** there are three physical indices `{i,j,k}` outside of which every row of `U` is zero.

The coefficient-label rotation is only a deterministic description of the cross frame; no random coordinates are rotated or declared independent.

## 3. Target-valid rho=0 coloop family with no good physical minor

Fix integer `k>=2`, put `m=k^4`, and use disjoint original-coordinate blocks: physical hubs `h_1,h_2`, a bank `I_a` of size `m`, one physical leaf `s`, and a bank `I_c` of size `m`. Let

`a=m^(-1/2) 1_(I_a)`, `c=m^(-1/2)1_(I_c)`.

Define

`A_k = k^(-1) e_(h1)e_(h1)^T
     + k(e_(h1)a^T+a e_(h1)^T)
     + k^(-1)(e_(h2)e_s^T+e_s e_(h2)^T)
     + c c^T.`

In the grouped orthonormal basis `(e_h1,a,e_h2,e_s,c)`, the nonzero matrix is

`[[k^-1,k],[k,0]] direct_sum [[0,k^-1],[k^-1,0]] direct_sum [1]`.

Hence the spectrum is

`{ (k^-1 +/- sqrt(k^-2+4k^2))/2, +k^-1, -k^-1, 1 }`.

For every `k>=2`, the first two eigenvalues have magnitudes >1 and the final eigenvalue is exactly 1, so this is a literal full-target family.

The two hub-to-leaf cross vectors are `u=k a` and `v=k^-1 e_s`. Their Gram determinant is exactly

`Delta=||u||^2||v||^2-<u,v>^2=1`.

Whitening gives the two-frame `U=[a,e_s]`. Every positive Pluecker basis is `{s,j}` with `j in I_a`, each of weight `1/m`, so **rho=0 exactly** and the partner collision identity is saturated by `ell_s=1`, `ell_j=1/m`.

Nevertheless every physical matrix entry has magnitude at most `1/k`; every physical `2 x 2` principal determinant has magnitude at most `1/k^2`; and every physical `3 x 3` principal block has operator norm at most `3/k` by the row-sum bound. Thus for large `k` the family lies in the strict local no-pivot chamber and has no universal-scale physical triple. Exact Pluecker localization is therefore not the same thing as a good physical principal minor.

## 4. Required newest-Claude mixed-hub theorem pays the same obstruction

Treat `h_1` as the physical hub, take the active leaf bank `I=I_a union I_c`, and condition the disjoint coordinates `{h_2,s}`. On `I`,

`A_II=c c^T`,

while the hub-to-leaf column is `k a`; the hub self coefficient `k^-1` is allowed to remain arbitrary by Theorem H. The augmented frame `[c,k a]` has Gram determinant `k^2`, while its whitened rows are `[c,a]`, each of leverage `1/m<=1/2`.

The owner-required Theorem H at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` therefore gives

`|phi_(Q_k)(t)| <= 4 pi^(3/2) k^(-1) |t|^(-3/2)`.

Integrating `min(1,A|t|^-3/2)` exactly and applying Fourier inversion yields

`||p_(Q_k)||_infinity <= 3*2^(4/3) k^(-2/3)`,

and hence

`P{Q_k in L} <= 3*2^(4/3) k^(-2/3)|L|`

for every interval `L`. No probability squaring is used; the scale is directly linear in `|L|`. The dense same-side square `c c^T` is retained exactly.

This shows the correct route for this rho=0/high-leverage target family: the localized cross frame does not force a local spectral minor, but a *different source-coordinate mixed-hub partition* exposes an actual dense same-side smoother and gives a stronger bound.

Full proof and the remaining quantitative small-rho obligation will be recorded in the final report.
