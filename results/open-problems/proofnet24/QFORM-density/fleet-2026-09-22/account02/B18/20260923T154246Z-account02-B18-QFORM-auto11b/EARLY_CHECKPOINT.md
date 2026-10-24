SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-23T15:42:46Z.
attacking: the exact-null heavy-anchor reroot-failure branch; use two-dimensional compression interlacing to force either a nonzero heavy scalar pivot or a uniformly conditioned indefinite physical pair.

# Early mathematical checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

Let `A=RMR^T`, `R^TR=I_3`, be exact rank three, with the three eigenvalues of `M` of modulus at least one. Suppose an ORIGINAL row `u_i` has `A_ii=0` and leverage `c_i=||u_i||^2>1/2`. Put `n=u_i/sqrt(c_i)`. Suppose the rerooted transverse-diffuse gate fails, so some ORIGINAL row `u_j` has

`q=||P_(n^perp)u_j||^2>1/2`.

Write `u_j=alpha n+beta t`, where `t` is a unit vector orthogonal to `n` in `span{u_i,u_j}` and `beta^2=q`. Orient the sign of `M` so its signature is `(2+,1-)`; density is unchanged by replacing `Q` by `-Q`. In the orthonormal basis `(n,t)`, the compression of `M` is

`C=[[0,gamma],[gamma,delta]]`.

By Cauchy interlacing its largest eigenvalue `p` satisfies `p>=1`. Since `det C=-gamma^2`, `delta=p-gamma^2/p>=1-gamma^2`. Also `||u_j||^2=alpha^2+beta^2<=1`, hence `2|alpha beta|<=1`. Therefore the second physical pivot `d=A_jj` obeys

`d=2 alpha beta gamma+beta^2 delta >= q(1-gamma^2)-|gamma|`.

Set `eta=1/8` and `g0=(sqrt(7)-2)/2`. If `|d|<eta`, then necessarily `|gamma|>g0`: otherwise `|gamma|<=g0<1`, so

`d > (1/2)(1-gamma^2)-|gamma| >= eta`,

a contradiction. The physical off-diagonal coefficient is

`b=A_ij=sqrt(c_i) beta gamma`,

hence `|b|>b0=(sqrt(7)-2)/4`. Thus the original-coordinate pair

`B=[[0,b],[b,d]]`

is indefinite and has

`|det B|=b^2>=b0^2`,

`sigma_min(B)=(sqrt(d^2+4b^2)-|d|)/2 >= k0`,

where

`k0=(sqrt(eta^2+4b0^2)-eta)/2 = 0.11061389959749726...`.

The completed pair-log theorem therefore gives

`||p_Q||_infinity <= 8 sqrt(5) (b0^2 k0)^(-1/4) <77.201`.

If instead `|d|>=eta`, the source-pinned orientation-free scalar-Schur/rank-two half-Riesz theorem gives, since `c_j>=q>1/2` and `|det M|>=1`,

`||p_Q||_infinity <=128[c_j |det M| |d|]^(-1/4) <256`.

Hence the reroot-failure branch is uniformly paid by `256`. Combined with compatible partner account03/B18 r28, which pays the complementary rerooted transverse-diffuse gate by `<9.525`, this will close the ENTIRE exact-null heavy-anchor branch. No post-rotation independence, moment, support, log-concavity, or coefficient-deletion step is used.
