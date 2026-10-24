# B04 substantive checkpoint — balanced near-coloop separation

Programme: `QFORM-DENSITY-3EIG-20260922`. Run: `20260923T043800Z-account02-B04-qform-auto11`. Full QFORM remains open.

First unpaid implication attacked here: `QFORM-NEAR-COLOOP-STRUCTURAL-ROUTING-v2`. The question is whether a near-coloop third cross direction must be paid by three-volume/ridge, or whether an original-coordinate rank-two exit can discard it before any reciprocal weak scale is incurred.

Let `m>=4`. On the left bank of size `2m+2`, let `u1,u2,u3` have disjoint supports: `u1=m^{-1/2}1` on the first `m` rows, `u2=m^{-1/2}1` on the next `m`, and `u3=(e_{2m+1}+e_{2m+2})/sqrt(2)`. Put `U=[u1 u2 u3]`. On the three-coordinate right bank take the all-nonzero orthogonal Householder matrix

`V=I-(2/3)11^T=[[1/3,-2/3,-2/3],[-2/3,1/3,-2/3],[-2/3,-2/3,1/3]]`

and

`M_eps=U diag(2,2,eps) V^T`, `0<eps<=1/4`.

Every physical cross entry is nonzero. The singular values are exactly `2,2,eps`.

For the third-volume law, a nonzero `3x3` left minor must select exactly one row from each support of `u1,u2,u3`; the right triple is forced. Every nonzero squared minor equals `8 eps^2/m^2`, there are `2m^2` of them, and hence

`Z=e_3(M_eps^T M_eps)=16 eps^2`.

The volume law has strong-row marginals `1/m` and weak-pair marginals `1/2`, so the `q=1` marginal gate of the completed e5 Theorem D is exactly admissible. Since all nonzero minors have equal determinant magnitude, the uniform volume law also maximizes entropy among all weights; thus it is the globally optimal admissible three-volume weight and its entropy-adjusted volume is exactly `G=16 eps^2`.

The same cross block has ridge matrix

`K_gamma=U diag(k,k,h)U^T`,
`k=4/(4+gamma^2)`, `h=eps^2/(eps^2+gamma^2)`.

Hence `max diag K_gamma=max(k/m,h/2)<=1/2` for every `gamma>0`, while `theta=tr K_gamma=2k+h`. The latest completed partner `account03/B04` r24 therefore reduces the direct ridge certificate on this family to optimizing

`R_eps(gamma)=sqrt(e)/(sqrt(2) gamma) * theta/(theta-2)`

over `theta>2`.

The continuation will compare the *best possible certificate inside these two mechanisms* with a physical rank-two column exit on the same target-valid matrix. No pointwise scalar decay or post-rotation independence is used.
