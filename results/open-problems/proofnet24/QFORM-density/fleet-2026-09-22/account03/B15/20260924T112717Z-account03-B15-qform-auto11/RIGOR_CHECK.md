# Rigor check — account03/B15 20260924T112717Z

This file checks the new packaging and the two structural branches used for the qualitative `C_0` conclusion. It is not an independent end-to-end review of the full universal-height conjecture, which remains open.

## A. Principal-block certificate

For symmetric `A` with `rank(A)>=3`, an invertible principal block of order 3 or 4 exists.

If `B=A_[I,I]` is invertible and `|I|<rank(A)`, Schur complement rank additivity gives `rank(A)=|I|+rank(S)`, so `S!=0`. If `S_jj!=0`, the one-coordinate extension determinant is `det(B)S_jj`. If all diagonal entries of `S` vanish, choose `S_jk!=0`; the two-coordinate Schur determinant is `-S_jk^2`, so the extended principal block is invertible. Starting from a nonzero diagonal 1-block, or a nonzero off-diagonal 2-block when the whole diagonal is zero, reaches order 3 or 4. PASS.

The finite-block constants used are source-proved affine-uniform interval estimates:

- `C_3=2*pi+3*sqrt(3)` for invertible physical 3-blocks;
- `C_4=4*pi+8` for invertible physical 4-blocks.

Conditioning outside the selected original-coordinate block leaves independence and the density caps unchanged and turns all outside couplings into an affine vector/constant. Therefore the conditional interval estimate averages without loss. PASS.

Numerically `C_3=11.479337728...`, `C_4=20.566370614...`.

## B. Latest partner application

For `f_(i,m)=f_i*eta_m` with a nonnegative probability mollifier,

`0<=f_(i,m)<=1`, `integral f_(i,m)=1`, and `||f_(i,m)-f_i||_1 ->0`.

The product telescoping identity gives

`||prod_i f_(i,m)-prod_i f_i||_1 <= sum_i ||f_(i,m)-f_i||_1 ->0`.

Deterministic pushforward cannot increase total variation. The same selected block gives `mu_m(J)<=K_*(A)|J|` for every `m`. Account04/B15 r4 therefore applies exactly and yields `mu(E)<=K_*(A)|E|` for the rough target law. PASS.

This theorem produces essential boundedness only. Continuity is supplied separately below; no generic inference `L^infinity => C_0` is used.

## C. Nonzero-diagonal C0 branch

Source: account03/B15 commit `d73760eb784a86c356c64f05dd92f84655618f02`.

For an invertible selected 3/4 block with nonzero scalar pivot `b`, Schur complement `S` is invertible. Writing `R(u)=u^T S u`, `M(u)=v^T u`, the map `Psi=(R,M)` has differential rows `2Su` and `v`. If `v!=0`, rank drops only when `Su` is parallel to `v`, namely on `S^{-1}(span v)`, a one-dimensional subspace and hence null in active dimensions 2 or 3. Thus `(R,M)` is absolutely continuous by coarea away from that null critical set.

Convolving the `M` coordinate with the independent pivot density gives

`K(r,z)=integral H(r,m) f_Z(z-m) dm`.

For a.e. `r`, both factors are `L^1` in the convolution variable, hence `K(r,.) in C_0`; because `f_Z<=1`, `K(r,z)<=integral H(r,m)dm=p_R(r)`. PASS.

The square change of variables produces an endpoint kernel `|t-r|^(-1/2)`. If `p_R in L^3`, Holder on a length-`L` neighborhood gives

`integral_0^L p_R(t-s)s^(-1/2) ds <= ||p_R 1_[t-L,t]||_3 (integral_0^L s^(-3/4)ds)^(2/3)`

`=4^(2/3)||p_R 1_[t-L,t]||_3 L^(1/6)`.

This tends uniformly to zero as `L downarrow0` with global `||p_R||_3`, giving endpoint control. Away from the endpoint, `K(r,.)` continuity plus the integrable envelope gives dominated convergence. Vanishing at infinity follows by fixing `L`, using local `L^3` mass tending to zero in translated windows, and then sending `L to infinity` to remove the far tail. PASS.

Outside conditioning changes only affine terms. The finite-block height bound is uniform in them, so dominated convergence survives the mixture. PASS.

## D. Zero-diagonal triangle branch

Source: account02/B15 commit `9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`.

Start with

`P=2axy+2bxz+2cyz+l1 x+l2 y+l3 z+d`, `abc!=0`.

Set

`U=x+(c/a)z+l2/(2a)`, `V=y+(b/a)z+l1/(2a)`.

Expanding `2aUV` gives the `2axy`, `2bxz`, `2cyz`, `l1 x`, and `l2 y` terms, plus a `z^2` coefficient `2bc/a`. Therefore `P=2aUV+H(z)` with quadratic coefficient of `H` equal to `-2bc/a`. PASS.

For a one-coordinate absolute density difference `h` satisfying `0<=h<=1`, `integral h=delta`, and an independent probability density `g<=1`, the product density at nonzero `s` is

`k(s)=integral h(u)g(s/u) du/|u|`.

Splitting at `|u|=r`, the exterior bathtub maximum is

`<=2 log(1+delta/(2r))`;

after substituting `v=s/u`, the interior bathtub maximum is

`<=2 log(1+r/(2|s|))`.

Taking `r=sqrt(delta |s|)` gives

`k(s)<=Phi_delta(s)=4 log(1+(1/2)sqrt(delta/|s|))`. PASS.

For `Psi(r)=4log(1+1/(2sqrt r))`, direct differentiation gives

`-Psi'(r)=2/[r(2sqrt r+1)]`.

If `P(R<=r)<=min(1,a sqrt r)`, integration by parts and `x=sqrt r` reduce the expectation to

`integral_0^infinity min(1,a x) 4/[x(2x+1)] dx`.

Splitting at `x=1/a` gives exactly

`2a log(1+2/a)+4log(1+a/2)=Omega(a)`.

Since `Omega(a)->0` as `a->0`, this is a true marginal-to-output sup-norm continuity modulus. PASS.

For `W=(t-H(Z))/(2a)`, the coefficient of `Z^2` is `bc/a^2` in absolute value. The preimage under `alpha z^2+beta z+gamma` of an interval of radius `rho` has total length at most `2sqrt(2rho/|alpha|)`; with cap-one `Z` this gives the stated square-root small-ball coefficient `2sqrt(2)|a|/sqrt(|bc|)`. PASS.

## E. Zero-diagonal triangle-free branch

Choose a nonzero edge `{i,j}`, `a=A_ij`, and pivot `P=[[0,a],[a,0]]`. Since `rank(A)>=3`, the Schur complement `S` is nonzero. For a remaining coordinate `k`,

`S_kk=A_kk-[A_ki,A_kj]P^{-1}[A_ik,A_jk]^T=-2A_ki A_kj/a`.

The physical diagonal is zero, and triangle-freeness prevents both `A_ki` and `A_kj` from being nonzero, so `S_kk=0`. Thus some off-diagonal `S_kl!=0`; the four-coordinate principal block extending the pivot by `k,l` has determinant `det(P)(-S_kl^2)!=0`. PASS.

Any triangle-free graph on four vertices is bipartite. A `1+3` bipartite zero-diagonal symmetric matrix has rank at most two, so invertibility forces the `2+2` form `[[0,C],[C^T,0]]` with `C in GL_2`. PASS.

For fixed planar `u`, the scalar `2u^T C V` is a linear form in two independent cap-one coordinates. If `w=2C^T u`, conditioning on the coordinate with largest `|w_j|` gives density cap `1/max_j|w_j| <= sqrt(2)/|w|=1/(sqrt(2)|C^T u|)`. Hence

`<=1/(sqrt(2)sigma_min(C)|u|)`.

For `F<=1` of planar mass `delta`, radial bathtub maximization gives

`integral F(u)/|u| du <= integral_(|u|<=sqrt(delta/pi)) du/|u| =2sqrt(pi delta)`.

Multiplication yields `sqrt(2*pi*delta)/sigma_min(C)`. PASS.

## F. Exhaustion and logical conclusion

Every symmetric matrix has either some nonzero physical diagonal or all physical diagonals zero. Sections C and D/E therefore cover every fixed `rank(A)>=3` matrix. They are QFORM-specific structural regularity results, not consequences of essential boundedness. PASS.

The target hypothesis `s_3(A)>=1` implies `rank(A)>=3`, so qualitative `C_0` continuity holds for every owner-target instance. The shared claim marking full-target continuity OPEN is stale relative to these completed source-pinned theorems and the current owner continuation's explicit statement that fixed-matrix `C_0` regularity is proved. The universal-height conjecture remains open because `K_*(A)` is not uniformly controlled. PASS.

No pointwise law-uniform oscillatory decay, arbitrary-joint coarea height bound, post-rotation independence, moment/support/log-concavity assumption, fixed fragment-count reduction, or numerical extremality claim is used.
