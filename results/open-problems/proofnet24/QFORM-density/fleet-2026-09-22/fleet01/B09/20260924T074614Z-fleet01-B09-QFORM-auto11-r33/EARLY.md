# fleet01/B09 r33 early substantive checkpoint

Status: supporting calculation only; full QFORM conjecture OPEN.

## Exact first missing implication attacked

Let physical mixed rows `x_i in R^d` have positive Gram `G_R=sum_(i in R) x_i x_i^T`. Put

`D(R)=det G_R` and `ell_i(R)=x_i^T G_R^{-1}x_i`.

By Cauchy--Binet,

`D(R)=sum_{B subset R, |B|=d} det(X_B)^2`.

For a literal row `i in R`, define its current basis-star volume

`S_i(R)=sum_{B subset R, |B|=d, i in B} det(X_B)^2`.

Then the matrix determinant lemma and Cauchy--Binet give the exact identity

`S_i(R)=D(R)-D(R\{i})=D(R) ell_i(R)`.

Hence a leverage violation `ell_i(R)>1/2` is not merely a failed Brascamp--Lieb gate: it produces a literal physical basis-star carrying more than one half of the current determinant currency.

More generally, fix `0<eta<1` and greedily promote any row with leverage `>1/2`, but execute a promotion only while the new determinant stays at least `eta D(R_0)`. Then exactly one of the following occurs:

1. the process reaches a residual set `R_*` with every leverage `<=1/2` and `D(R_*)>=eta D(R_0)`; or
2. at the first forbidden promotion there is a literal row `i` with `S_i(R)>eta D(R_0)/2`.

This is a determinant-or-star stopping lemma with no bound on the number of promoted coordinates and no reciprocal scalar pivot.

### Rank-one fixed-hub specialization

For the preceding B09 rank-one packet, take `x_j=(v_j,c_j) in R^2`, leaf-curvature coefficient `lambda`, and

`T=det(sum_j x_jx_j^T)=sum_{i<j}(c_i v_j-c_j v_i)^2`.

The completed fixed-hub disjoint one-overlap currency satisfies

`Omega_(1,h)^dis <= lambda^2 T^2`,

so `|lambda|T >= sqrt(Omega_(1,h)^dis)`.

Therefore a current leverage violation at the initial frame gives a literal source-coordinate star

`|lambda| sum_(j!=i)(c_i v_j-c_jv_i)^2 > (1/2) sqrt(Omega_(1,h)^dis)`.

If instead all initial leverages are `<=1/2`, the completed promoted-leaf retained-hub theorem from r32 applies with no promotion and gives

`||p_Q||_infinity <= 3*2^(4/3) [|lambda|T]^(-1/3) <= 3*2^(4/3) [Omega_(1,h)^dis]^(-1/6)`,

with a continuous density and the same coefficient multiplying interval length.

The current task is to route the macroscopic literal star endpoint without using a tiny pivot; no full-target claim is made here.
