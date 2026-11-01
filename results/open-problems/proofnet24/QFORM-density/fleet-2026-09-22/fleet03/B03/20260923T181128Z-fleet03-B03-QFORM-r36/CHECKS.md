# fleet03/B03 r36 deterministic checks

Run: `20260923T181128Z-fleet03-B03-QFORM-r36`.

These checks verify the algebra/constants in the report; the analytic source theorem and the displayed proofs, not numerics, are the mathematical evidence.

## 1. Crossing Gram determinant

Let `x=beta r+sigma u`, `y=m r`, with `||u||=1`. Then

`det Gram(x,y)`
`= ||x||^2 ||y||^2 - <x,y>^2`
`= m^2[(beta^2||r||^2+2 beta sigma<r,u>+sigma^2)||r||^2`
`        -(beta||r||^2+sigma<r,u>)^2]`
`=m^2 sigma^2(||r||^2-<r,u>^2)`.

Because the physical pivot coordinate has `r_i=1` and `u_i=0`, the last bracket is `||P_(u^perp)r||^2>=1`. Hence `s_1(B)s_2(B)>=m|sigma|` exactly.

## 2. Effective-dimension integral

For `T=K^(2/d)` and `0<gamma<d`,

`2[ integral_0^T t^(gamma-1)dt + K^2 integral_T^infinity t^(gamma-d-1)dt ]`
`=2K^(2gamma/d)[1/gamma+1/(d-gamma)]`
`=2d/[gamma(d-gamma)] K^(2gamma/d)`.

At `gamma=1/2`, the coefficient is `8d/(2d-1)`. In particular:

- d=2: `16/3=5.333333333333333...`;
- d=3: `24/5=4.8`;
- d=4: `32/7=4.571428571428571...`.

## 3. Exact packet constants

With `K_2<=2pi(m|sigma|)^(-1/2)`, the half-Riesz coefficient is

`(16/3)sqrt(2pi)=13.368684131365335...`.

The Riesz identity divides by `sqrt(2pi)`, giving the exact collision-potential coefficient `16/3` in

`E|Q-Q'|^(-1/2) <=(16/3)(m|sigma|)^(-1/4)`.

Plancherel gives

`||p_Q||_2^2 <= (1/(2pi))*4K_2 <=4(m|sigma|)^(-1/2)`.

The fleet04/B03 collision lemma therefore gives coefficient 8 in

`P(|Q-Q'|<=eps)<=8(m|sigma|)^(-1/2)eps`.

The translation-uniform half-Riesz constant is

`C_H=6sqrt(6)/2^(2/3)=9.258491065302314...`,

and after `K_2/pi<=2(m|sigma|)^(-1/2)` becomes

`C_H sqrt(2)=13.093483631660659...`.

## 4. One-hub plus two projected crossings

For `(k,ell,d)=(1,2,3)`, the general grouped-crossing half-Riesz coefficient outside the scale factors is

`(24/5) 2^(7/12) sqrt(pi) exp(1/6)`
`=15.05911390259813...`.

The corresponding partner-consumed collision coefficient is

`3*2^(7/6)*exp(1/3)=9.39913188784886...`.

## 5. Projected residual vanishing

The light residual matrix is `A_G=a r r^T`. If a light split `I,J` keeps the two-row hub crossing full rank, the second crossing row is `m r_J`; hence `r_J` belongs to `row(M_J)`. Therefore

`A_G[I,J](I-Pi_row(M_J))`
`=a r_I r_J^T(I-Pi_row(M_J))`
`=0`.

So every projected crossing volume `Z_ell` is exactly zero in this natural `k=2` grouping. This is an exact algebraic zero, not a numerical near-zero.

`QFORM_B03_R36_CHECK_PASS`
