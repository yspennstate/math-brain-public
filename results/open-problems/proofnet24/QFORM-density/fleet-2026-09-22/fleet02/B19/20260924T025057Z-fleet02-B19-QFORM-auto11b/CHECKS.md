# Deterministic checks — fleet02/B19 auto11b

All checks are exact algebra except the displayed decimal evaluations.

## 1. Bordered-Schur identity

For any 2-row set `I`, 2-column set `J` and scalar `b != 0`,

`det [[N[I,J],u_I],[v_J^T,b]] = b det(N[I,J]-u_I v_J^T/b)`.

Therefore summing squares gives

`D_pq=b^2 E2(N-uv^T/b)`.

This is the scalar Schur determinant formula and requires no probabilistic premise.

## 2. Exact-collapse family

Let `epsilon in (0,1)`, choose orthonormal `u,a` and `v,c`, and put

`N=uv^T/epsilon+ac^T`,

`B=[[N,u],[v^T,epsilon]]`.

Because `{u,a}` and `{v,c}` are orthonormal, the nonzero singular values of `N` are

`1/epsilon, 1`,

hence

`E2(N)=epsilon^-2`,

`epsilon sqrt(E2(N))=1`.

The corrected block is

`S=N-uv^T/epsilon=ac^T`,

so `rank S=1`, `E2(S)=0`, and the bordered minor aggregate is exactly zero.

Factor

`B=x1 y1^T+x2 y2^T`,

`x1=[u/epsilon;1]`, `x2=[a;0]`,

`y1=[v;epsilon]`, `y2=[c;0]`.

Then `x1 perp x2`, `y1 perp y2`, and

`||x1||||y1||=sqrt(epsilon^-2+1)*sqrt(1+epsilon^2)=(1+epsilon^2)/epsilon`,

`||x2||||y2||=1`.

Thus

`sigma(B)={(1+epsilon^2)/epsilon,1}`,

and for the symmetric bipartite matrix `A=[[0,B],[B^T,0]]`,

`spec_nonzero(A)={+((1+epsilon^2)/epsilon),+1,-1,-((1+epsilon^2)/epsilon)}`.

Also `rank B=2`, hence `E3(B)=E5(B)=0`.

## 3. Local pivot scale

For flat vectors on banks of size `m`,

`max |N_ij| <= (epsilon^-1+1)/m`,

`max |u_i|=max|v_j|=m^-1/2`,

and the anchor edge is `epsilon`.

Every diagonal is zero, every pair principal determinant is `-A_ij^2`, and every three-coordinate principal determinant is zero because the matrix is bipartite with zero same-side blocks.

For the checkpoint

`epsilon=1/64`, `m=2048`,

one has

`(epsilon^-1+1)/m = 65/2048 = 0.03173828125`,

`m^-1/2 = 0.022097086912079608...`,

`epsilon = 0.015625`.

Therefore

`max |A_ij|^2 <= (65/2048)^2 = 4225/4194304 = 0.0010073184967041016... < 1/256 = 0.00390625`.

## 4. Pure-bilinear density constant

For rank-two `M` with singular values `sigma1,sigma2`, put `d=sigma1 sigma2`. The checked cap-one product projection theorem gives

`||rho_Y||inf <=2`

for the 2D left projection, and density cap `sqrt(2)` for each unit 1D projection on the right.

Conditioning on `Y=y` gives

`||p_(2(Dy).Z | Y=y)||inf <=1/(sqrt(2)|Dy|)`.

After `z=Dy`, the transformed density has cap `2/d`. Among probability densities with cap `M=2/d`, the integral of `|z|^-1` is maximised by density `M` on a centered disk of radius

`R=(pi M)^-1/2=sqrt(d/(2pi))`.

Hence

`int q(z)|z|^-1 dz <= M*2pi R = 2 sqrt(2pi) d^-1/2`,

and multiplying by `1/sqrt(2)` gives

`||p_Q||inf <=2 sqrt(pi) d^-1/2`.

At `epsilon=1/64`,

`d=64+1/64=64.015625`,

so

`2 sqrt(pi)/sqrt(d) = 0.4430593816298541...`.

## 5. Partner-r47 constant

Partner r47's strong rank-two threshold is

`gamma0=28159/(4194304 sqrt(2)) = 0.00474725242887306...`.

The pure-bilinear rank-two theorem therefore gives

`2 sqrt(pi) gamma0^-1/2 = 51.44980929398639...`.

Terminal marker: `QFORM_B19_AUTO11B_BORDERED_SCHUR_COLLAPSE_CHECK_PASS`.
