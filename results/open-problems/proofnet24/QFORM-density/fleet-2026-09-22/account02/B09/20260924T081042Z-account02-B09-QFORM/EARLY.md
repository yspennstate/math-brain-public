# account02/B09 — early substantive checkpoint

Run: `20260924T081042Z-account02-B09-QFORM`.

## First unpaid implication

`QFORM-NEARSINGULAR-GENERAL-CURVATURE-COMPILER-v1`: account03/B09 r46 pays the exact singular physical-pair face by the polynomial Schur star. The next analytic face is a nonzero near-singular Schur coefficient. The key issue is not the small scalar coefficient itself: it can be retained uniformly whenever the post-completion leaf geometry forms a mixed frame. The remaining debt is to compile arbitrary same-bank curvature into that frame or a grouped-crossing/core exit without deleting a small square.

## New lemma: joint-hub extension of pinned Theorem H

The proof of pinned Theorem H (`e5f71d79eff325201dd0274053d20268ce65b837`) uses the hub laws only through the pointwise inequality `prod_h f_h(x_h)<=1` before the change of variables `y=2t x_H`. Therefore the identical estimate holds if the hub vector has an arbitrary *joint* density `F_H<=M`, independent of the product leaf bank: the right-hand side acquires only the prefactor `M`.

In particular a determinant-one linear shear of physical hub coordinates preserves the joint cap `M=1`, although it destroys independence among the sheared hub coordinates. This is legal because no post-shear independence is used.

For `h=2,r=1`, leaf square coefficient `lambda`, mixed Gram `G`, and leaf leverages at most `1/2`,

`|phi_Q(t)| <= 8 pi^(5/2) M |lambda|^(-1/2) det(G)^(-1/2) |t|^(-5/2)`.

Hence

`||p_Q||_infinity <= (5/3) 2^(6/5) M^(2/5) |lambda|^(-1/5) det(G)^(-1/5)`.

The same coefficient multiplies interval length; the characteristic function is integrable, so this branch has a continuous density.

## Near-singular determinant-one physical-pair family

Let `m>=8` be a Walsh size and let `c,d,w in R^m` be flat orthonormal Walsh vectors. Fix `M0=4` and `0<=delta<=1`. With original independent cap-one coordinates `X1,X2,Y`, define

`Q_delta = X1^2 + 2 X1 X2 + (1+delta) X2^2
           + 2 M0 X1 <c,Y> + 2 M0 X2 <c+d,Y> + <w,Y>^2`.

The literal physical pair core is

`B_delta=[[1,1],[1,1+delta]]`, `det B_delta=delta`.

Set the determinant-one shear `u=X1+X2`, `v=X2`. Its joint density is

`F_{u,v}(u,v)=f_1(u-v)f_2(v)<=1`,

and

`Q_delta=u^2+delta v^2+2 M0 u<c,Y>+2 M0 v<d,Y>+<w,Y>^2`.

The mixed rows are `(w_i,M0 c_i,M0 d_i)`, so

`G=diag(1,M0^2,M0^2)`, `det G=M0^4`, and every normalized leverage is exactly `3/m<=3/8`.

Thus the joint-hub Theorem H gives, uniformly through `delta=0`,

`||p_{Q_delta}||_infinity <= (5/3) 2^(6/5) M0^(-4/5) < 1.264`.

No small square is deleted. The dense physical same-side block `w w^T` remains in source coordinates.

For target validity, write `z'=(u,v,Y)=T z` with hub shear `S=[[1,1],[0,1]]`. In the orthonormal deterministic coefficient basis `(u,v,c,d,w)`, the transformed quadratic matrix is

`A'=[[1,M0],[M0,0]] direct_sum [[delta,M0],[M0,0]] direct_sum [1]`.

For `0<=delta<=1`, the four eigenvalues from the two 2x2 blocks have modulus at least `(sqrt(65)-1)/2`. The least singular value squared of `S` is `(3-sqrt(5))/2`. Since `A=T^T A' T`,

`s_4(A) >= sigma_min(T)^2 s_4(A') >= ((3-sqrt(5))/2)*((sqrt(65)-1)/2) > 1.34`.

Hence every `Q_delta` has at least four eigenvalues of modulus greater than one. This is a genuine target-valid near-singular physical-pair interpolation.

The construction also exposes why completing the small pair and then treating the remainder perturbatively is the wrong order: completion produces the term `-delta^{-1}<...>^2` when one instead completes the small `delta v^2` direction, whereas the mixed-frame estimate is completely uniform in `delta`.
