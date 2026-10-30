# fleet02/B07 early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.
Run: fleet02-B07-20260923T100305Z-r11.

## First unpaid implication attacked

Partner fleet03/B07 r30 leaves `QFORM-ANCHOR-H3-LOWERORDER-CURVATURE-RECEIVER-v1`: an actual double-anchored third-minor bank is compressed into edge-times-E2 or four-bank resources, but a nonlinear receiver must preserve arbitrary within-bank curvature.

## Calculation 1: unconditional fractional-volume currency

The proved D_k argument in
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`
can be run with Jensen exponent q=2 for every k, since every k-volume inclusion marginal is <=1=q/2. For disjoint original-coordinate sets I,J and `Z_k=e_k(A[I,J]^T A[I,J])>0`, conditioning all other coordinates and retaining arbitrary self-blocks/affine terms gives

`|phi(t)| <= min(1, B_k |t|^{-k/4})`,

`B_k=[e^(k/2)(2 pi)^k 2^(-k/2) Z_k^(-1/2)]^(1/4)`.

Combining with the proved Fourier fractional-potential lemma yields, for every `0<alpha<k/4`,

`H_alpha(Q):=sup_s E|Q-s|^(-alpha)
 <= C_(k,alpha) Z_k^(-alpha/(2k))`,

`C_(k,alpha)=c_alpha * k/[2 alpha(k/4-alpha)] * (pi sqrt(2e))^alpha`,

where `c_alpha=2^(1-alpha) Gamma((1-alpha)/2)/(2 sqrt(pi) Gamma(alpha/2))`.
In particular

`H_(1/4)(Q) <= 3.929132 Z_2^(-1/16)`

with no 2-volume marginal gate, and

`H_(1/2)(Q) <= 12.956789 Z_3^(-1/12)`

with no 3-volume marginal gate. This is fractional currency, not a density theorem.

## Calculation 2: exact target family showing why a pair peel cannot simply inherit partner r30's E2 bank

For even integer m>=12 let `N=m^2`, choose flat orthonormal vectors `p,u in R^N` and `q,v in R^N` (constant and alternating-sign vectors), and set

`b=1/m`, `S=sqrt(m)`, `a=m^(-1/4)`,
`D=S(p q^T+u v^T)`.

Use physical coordinates `(x,y,U,V)` and define the symmetric matrix by

- `A_xy=b`;
- `A_xU=a p^T`, `A_yV=a q^T`;
- `A_UV=D`;
- all other entries, including every diagonal, are zero.

For the physical cut `I={x} union U`, `J={y} union V`, the cross block is `diag(b,D)`. It has singular values `S,S,b`, so every nonzero third minor contains both anchors and

`G3^(x,y)=E3(A[I,J])=b^2 S^4=1`,
`E2(D)=S^4=m^2`,
`|b| sqrt(E2(D))=1`.

But the physical zero-diagonal anchor pair `P=[[0,b],[b,0]]` has Schur correction `(a^2/b) p q^T=S p q^T`; hence the far Schur cross block is exactly

`D-(a^2/b)pq^T=S u v^T`,

which has rank one and `E2=0`. Thus a zero-diagonal/hyperbolic pair peel cannot transfer the incoming edge-times-E2 determinant bank to the Schur remainder, even in the no-pivot target class.

The full matrix is target-valid: in the modal span `(x,y,p,q)` the eigenvalues are `+(S+b),-(S+b),0,0` because `a^2=bS`, and the `(u,v)` block contributes `+S,-S`; all other eigenvalues vanish. Hence it has four eigenvalues of modulus >=1.

Moreover this is genuinely N3 at tau=1/128: all diagonals vanish and every physical off-diagonal entry is at most `max(1/m,m^(-5/4),2m^(-3/2))=1/m`, so every physical pair determinant has magnitude at most `1/m^2<1/128`.

No fixed-cardinality physical spectral core is forced. For every `|H|<=M`, subtracting the rank-two anchor edge leaves operator norm at most

`2 sqrt(M) m^(-5/4)+2 M m^(-3/2)`,

so `s_3(A[H,H])` is bounded by the same quantity and tends to zero as m->infinity.

This does NOT refute QFORM. It identifies the exact failure of E2-through-Schur and bounded-core extraction. The same family is actually paid by the completed e5 Theorem F: condition on x,y. The far quadratic block is the symmetric bipartite rank-four matrix with eigenvalues `+S,+S,-S,-S`, range leverage `2/N<=1/2`, and arbitrary resulting affine terms. Therefore

`||p_Q||_infinity <= 8/S = 8/sqrt(m) <= 8`.

Next: record a full proof/check and sharpen the remaining receiver to arbitrary same-bank curvature without assuming the E2 bank survives pair completion.
