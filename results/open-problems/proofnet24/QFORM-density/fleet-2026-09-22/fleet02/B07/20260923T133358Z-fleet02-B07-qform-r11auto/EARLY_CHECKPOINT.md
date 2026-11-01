SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T13:33:58Z.
attacking: the partner's residual E3 branch — spend diffuse third-volume immediately, and in the concentrated case double-anchor the full determinant packet before any reciprocal minor selection.

# Early substantive checkpoint

Full QFORM remains open. Work is in ORIGINAL coordinates and retains arbitrary same-bank quadratic curvature, outside couplings, affine terms, signs, and additional spectrum.

Incoming completed partner result: fleet03/B07, `20260923T130749Z-fleet03-B07-qform-r30`, proves that one live rank-four branch contains a far physical cross block `D` with

`Z3:=E3(D) > (8/3) a^6`,

or is routed to other already-separated branches.

First new implication. Normalize all squared 3x3 minors of `D` to a probability law and let `alpha_i,beta_j` be row/column inclusion marginals. If `max alpha_i<=2/3` or `max beta_j<=2/3`, orient the constrained side appropriately and apply the completed pinned e5 theorem D' at `h=2/3`:

`||p_Q||_infinity <= 9 sqrt(3e) Z3^(-1/6)
                   < 9 sqrt(3e) (3/8)^(1/6) a^(-1)
                   < 21.826/a.`

Thus the only unspent residual-E3 state has physical `i,j` with `alpha_i>2/3`, `beta_j>2/3`. By the union bound under determinant-volume sampling, the entire doubly anchored packet

`G3^(i,j)=sum_{|R|=|T|=2} det D[{i} union R,{j} union T]^2`

satisfies

`G3^(i,j)>Z3/3>(8/9)a^6`.

Writing the actual physical block around `(i,j)` as

`D=[[b,r^T],[c,E]]`,

Laplace expansion plus the exterior-map estimate gives

`sqrt(G3^(i,j))
 <= |b| sqrt(E2(E)) + ||r|| ||c|| ||E||_F`.

Indeed the cofactor array `Psi_(R,T)=r_T^T adj(E[R,T])c_R` is the matrix of `(c wedge .) o E o i_r : wedge^2 -> wedge^2`, so

`sum Psi_(R,T)^2 <= ||c||^2 ||r||^2 ||E||_F^2`.

Consequently every still-unpaid concentrated residual-E3 state has at least one of

`|b| sqrt(E2(E)) > (sqrt(2)/3)a^3`,

`||r|| ||c|| ||E||_F > (sqrt(2)/3)a^3`.

This carries the determinant weight through concentration and does not select one minor. The next step in this run is to integrate bounded-support coordinate-core extraction directly at the anchored packet level, so a bounded residual support is paid before the two lower-compound survivors are exposed.
