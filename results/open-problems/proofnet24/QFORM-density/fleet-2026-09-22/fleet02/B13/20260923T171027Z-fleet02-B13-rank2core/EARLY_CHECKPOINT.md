# Early checkpoint — four-anchor skeleton from the global cross-rank-two bound

Run: `20260923T171027Z-fleet02-B13-rank2core`.

The designated partner fleet03/B13 r29 proves that every disjoint original-coordinate cross block `B=A[L,R]` in a slab witness of ratio `rho=P(Q in J)/|J|` satisfies

` s_3(B) <= delta := 9 sqrt(3e)/rho. `

I apply this globally rather than selecting a single favorable cut.

Let

`D = max |det A[P,Q]|`,

where the maximum runs over disjoint physical two-sets `P,Q` (so `A[P,Q]` is a physical `2 x 2` cross minor). If `D>0`, choose maximizing `P={p1,p2}`, `Q={q1,q2}` and put `K=A[P,Q]`. For any two distinct indices `i,j` outside `P union Q`, the `3 x 3` matrix

`M=A[P union {i}, Q union {j}]`

is a disjoint physical cross block, hence `s_3(M)<=delta`. Every one of its nine `2 x 2` minors is also a disjoint physical minor, so its modulus is at most `D`. Therefore

`e_2(M M^T) = sum_(2x2 minors N of M) det(N)^2 <= 9 D^2`.

If the singular values of `M` are `t1>=t2>=t3`, then

`|det M|^2=t1^2 t2^2 t3^2 <= t3^2 e_2(MM^T) <= 9 delta^2 D^2`,

hence

`|det M| <= 3 delta D`.

The bordered determinant / Schur-complement identity gives

`det M = det K * ( A_ij - A[i,Q] K^{-1} A[P,j] )`.

Thus

`|A_ij - A[i,Q]K^{-1}A[P,j]| <= 3 delta = 27 sqrt(3e)/rho`.

Moreover, maximality of `D` and Cramer's rule give the dimension-free interpolation bounds

`||A[i,Q]K^{-1}||_infinity <= 1`,
`||K^{-1}A[P,j]||_infinity <= 1`.

So, outside four physical anchor coordinates, every off-diagonal entry is within `27 sqrt(3e)/rho` of a rank-two cross skeleton through the actual physical core `K`, with all left/right interpolation coefficients bounded by one. Symmetrizing the skeleton gives a diagonal + rank-at-most-four leaf model with the same entrywise error. No inverse small-minor loss survives in the interpolation coefficients, and no rotated random variables are introduced.

This is only a matrix reduction. The `O(1/rho)` entrywise remainder cannot be discarded for arbitrary unbounded/fragmented cap-one laws; a valid next analytic receiver must keep it. The pinned Fourier `D_5` theorem will be combined with this skeleton in the full report to constrain fifth exterior volume on every residual physical cut.
