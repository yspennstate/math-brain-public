# account01/B04 r34 deterministic checks

Marker: `QFORM_B04_R34_ZEROSELF_OPT_CHECK_PASS`

All exact identities below were checked symbolically or by direct arithmetic; decimals are audit values only.

## 1. Exact optimizer calculus

For

`Omega0(z)=z(2+log(1/z))` on `0<z<=1`, and `Omega0(z)=log z+2` on `z>=1`,

set

`F_rho(z)=rho z^(-1/2)+Omega0(z)`.

- On `z>=1`, `F'_rho(z)=z^(-1)[1-(rho/2)z^(-1/2)]`, so the unique interior critical point is `sqrt(z)=rho/2`, admissible exactly for `rho>=2`. The value is `4+2 log(rho/2)`.
- On `0<z<=1`, `F'_rho(z)=-(rho/2)z^(-3/2)+1-log z`. The critical equation is `rho=2z^(3/2)(1-log z)`. Writing `y=-log z` gives `rho=2(1+y)e^(-3y/2)`. The RHS is strictly decreasing from `2` to `0`. At the critical point the value is `e^(-y)(4+3y)`.
- At `rho=2` both formulas give `4`.

For the elementary envelope,

`Omega0(z)/sqrt(z)=e^(-t/2)(2+t)` with `t=|log z|>=0`; its derivative is `-(t/2)e^(-t/2)<=0`, hence `Omega0(z)<=2sqrt(z)`.

## 2. Six-coordinate clique carrier

Take

`B=[[3,1],[1,-3]]`, `u=(1,1,1,1)^T`, `v=(1/10,1/5)^T`,

`S=-2 I_4+2uu^T=2(J_4-I_4)`, `C=u v^T`, and `D0=S+C B^(-1)C^T`.

Exact arithmetic:

- `det(B)=-10`;
- `B^(-1)=(1/10)B`;
- `v^T B^(-1)v=-1/200`;
- `C B^(-1)C^T=-(1/200)J_4`;
- `D0=-2I_4+(399/200)J_4`;
- the Schur complement of `B` is exactly `S`;
- `N_H=det(B)S=-20(J_4-I_4)`;
- each row of `N_H` has off-diagonal Euclidean norm `R_i=20sqrt(3)`.

The resulting full matrix is

`[[3,1,1/10,1/10,1/10,1/10],`
` [1,-3,1/5,1/5,1/5,1/5],`
` [1/10,1/5,-1/200,399/200,399/200,399/200],`
` [1/10,1/5,399/200,-1/200,399/200,399/200],`
` [1/10,1/5,399/200,399/200,-1/200,399/200],`
` [1/10,1/5,399/200,399/200,399/200,-1/200]].`

Every entry is nonzero.

## 3. Target spectral check

For `A0=diag(B,S)`, the spectrum is exactly

`{-sqrt(10), -2,-2,-2, sqrt(10), 6}`.

Also

`||C||_op=1/sqrt(5)=0.447213595499958...`,
`||CB^(-1)C^T||_op=1/50=0.02`.

Hence

`||A-A0||_op <=1/sqrt(5)+1/50<0.468`,

so Weyl gives `min |lambda(A)|>2-0.468>1.53`. Direct diagonalization for audit gives

`[-3.17666914,-2,-2,-2,3.13839042,6.01827872]`.

## 4. New row-certificate constants

For the carrier,

`D=10`, `kappa=sqrt(10)`, `R_i=20sqrt(3)`.

Therefore

`rho_i=2^(11/4) D/sqrt(kappa R_i)`
`     =8 sqrt(5/(2sqrt(15)))`
`     =6.4274273515572138365... >2`.

The exact high-`rho` certificate is

`D^(-1/2)[4+2log(rho_i/2)]`
`=2.0032568402692141275...`.

The determinant-free envelope is

`2^(23/8)(kappa R_i)^(-1/4)`
`=2.2675850328589159810...`.

The partner r21 principal-triple comparison is

`3sqrt(pi)=5.3173615527165480819...`,

with ratio

`(3sqrt(pi))/2.003256840269214...=2.6543583657510226...`.

## 5. Fresh account02/B04 r22 same-matrix comparison carrier

Let `A_J1` be the partner r22 pure localized-J1 matrix with one zero-self anchor, 144 residual coordinates,

`v_i=1/12` for every `i`, and `a_i=+1/12` on 72 coordinates, `a_i=-1/12` on 72 coordinates,

so `A_J1=[[0,a^T],[a,vv^T]]`. Then `||a||=||v||=1` and `a dot v=0`, hence its nonzero spectrum is exactly `{1,1,-1}`.

Adjoin an independent outer hyperbolic physical pair `B0=[[0,1],[1,0]]` and write `Ahat=B0 direct_sum A_J1`. The partner r22 weighted mixed-hub theorem applies to the `A_J1` block and, using its globally optimized pair law with `G_*=1`, gives

`||p_(X^T Ahat X)||_infinity <=3*2^(4/3)`
`=7.559526299369239...`.

For the new exact-optimizer route, use `B0` as the outer pair. Then `D=kappa=1`, the residual zero-self hub has slope `2a^T X`, and the sharp scalar product-projection theorem gives `H<=1/sqrt(2)`. Thus

`rho=8*2^(-1/4)=6.727171322029716... >2`,

and the exact optimizer gives

`||p_(X^T Ahat X)||_infinity`
`<=4+2log(rho/2)`
`=6.426015131959808...`.

The displayed fresh-partner certificate divided by the new certificate is

`1.17639410180843...`.

This is only a same-matrix comparison of two valid sufficient receivers.
