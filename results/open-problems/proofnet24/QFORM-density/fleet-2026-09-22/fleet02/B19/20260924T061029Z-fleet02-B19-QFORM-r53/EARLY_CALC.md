# Early calculation — maximal cross coloop, strict no-pivot, and three-frame leverage halving

Take a physical hub `h` and four pairwise disjoint size-`m` physical banks `U,V1,V2,W`. Let `u,v1,v2,w` be their flat unit vectors and put

`l1=e_h+v1`, `l2=u+v2`,

`A=l1 l2^T+l2 l1^T+w w^T`.

Then `l1,l2,w` are mutually orthogonal, `||l1||=||l2||=sqrt(2)`, so

`spec_nonzero(A)={2,-2,1}`.

On the physical cut `R={h} union U`, `C=V1 union V2`,

`N=A[R,C]=e_h v2^T+u v1^T`,

hence `sigma_1(N)=sigma_2(N)=1` and `dist_F(N,rank<=2)=0`. In the top-two left SVD frame, coordinate `h` has leverage exactly `1`; after peeling it, the light Gram has eigenvalues `{0,1}`. Thus the current partner-r50 heavy-peel theorem lands on its hub-star branch, and the literal star from `h` into `C` has norm exactly `1`.

Nevertheless the normalized eigenvectors

`r_+=(l1+l2)/2`, `r_-=(l1-l2)/2`, `r_3=w`

have three-frame leverage `1/2` at `h`, `1/(2m)` on `U,V1,V2`, and `1/m` on `W`. Therefore for `m>=2` the pinned `e5f71...` Theorem F applies with `G=I_3`, residual zero, coefficients `(2,-2,1)`, and gives

`||p_Q||_infinity <= 12*4^(-1/3)=7.55952629936924...`.

The same family is arbitrarily strict local no-pivot: the only diagonal entries are `1/m` on `W`; the largest off-diagonal entry is `1/sqrt(m)`; hence the largest absolute physical `2x2` principal determinant is `1/m`, and every core-only `3x3` principal determinant is zero while the largest triple using `W` is `1/m^2`.

For iid `Uniform[-1/2,1/2]` coordinates, the two-bank/core output is

`Q_core=2 <l1,X><l2,X>`.

The two factors use disjoint original-coordinate banks and have continuous densities positive at zero, so `p_{Q_core}(t)` diverges logarithmically as `t->0`. Thus even a maximal literal hub star plus an exact rank-two physical crossing cannot be scalarized to an `L^infinity` two-bank law before the third source is spent; the full sign-paired eigenframe is the correct currency in this exact aligned chamber.
