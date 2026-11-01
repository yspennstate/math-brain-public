# fleet03/B03 r43 deterministic checks

Run: `20260923T235705Z-fleet03-B03-QFORM-r43`.

## 1. Fourier exponents and constants

For Theorem 2.1 set

`K=pi^(3/2) M0 (MR MC)^(1/2) |sigma alpha beta|^(-1/2)`.

The derived envelope is `min(1,K|t|^(-3/2))`. Its crossover is `t0=K^(2/3)` and

`2[t0 + K*int_t0^infinity t^(-3/2)dt]
 =2[t0+2K t0^(-1/2)]
 =6K^(2/3)`.

Thus Fourier inversion gives

`6K^(2/3)/(2pi)
 =3 M0^(2/3)(MR MC)^(1/3)|sigma alpha beta|^(-1/3)`.

For the assigned weighted whole-copy integral,

`2 int_0^t0 t^(-1/2)dt +2K^2 int_t0^infinity t^(-7/2)dt
 =4K^(1/3)+(4/5)K^(1/3)
 =(24/5)K^(1/3)`.

The Fourier/Riesz normalization is

`int_R e^(itx)|t|^(-1/2)dt=sqrt(2pi)|x|^(-1/2)`.

## 2. Partial-Plancherel normalization

With Fourier convention `hat f(xi)=int exp(i xi x)f(x)dx`,

`int |hat f(xi)|^2 dxi=2pi int|f|^2`.

For the rank-one bilinear operator

`(Lf)(y)=int exp(i2t sigma y w)f(w)dw`,

`||Lf||_2^2
 =(2|t sigma|)^(-1)||hat f||_2^2
 =pi/(|t sigma|)||f||_2^2`.

Hence `||L||_(2->2)=sqrt(pi/(|t sigma|))`, as used in the report.

For the partial transforms of complex pushforward densities,

`int G_R(xi)dxi=2pi int|b_t|^2<=2pi MR`,

and with `p_Z<=M0`,

`int p_Z(z)G_R(2t alpha z)dz
 <=M0/(2|t alpha|) int G_R
 <=pi M0 MR/(|t alpha|)`.

The same calculation holds on the C bank. Multiplying the three Plancherel factors gives exactly the `|t|^(-3/2)` envelope in Theorem 2.1.

## 3. Exact rank-one anchored determinant identity

Let `N=sigma u v^T`, with unit `u,v`. For physical two-sets `P,Q`, direct expansion gives

`det [[b,r_Q^T],[c_P,N_PQ]]
 = +/- sigma (c_p1 u_p2-c_p2 u_p1)
                 (r_q1 v_q2-r_q2 v_q1)`.

The `b det(N_PQ)` term is zero because `rank N=1`. Therefore

`J_sep
 =sigma^2 [sum_P det(c_P,u_P)^2]
           [sum_Q det(r_Q,v_Q)^2]
 =sigma^2 ||c wedge u||^2 ||r wedge v||^2
 =sigma^2 ||c_perp||^2 ||r_perp||^2`.

This is exactly `|sigma alpha beta|^2`.

A finite numerical spot check with random unit vectors and random `b,c,r`, dimensions `|R|=4, |C|=5`, and `sigma=1.7` gave identical values for the minor sum and the exterior-product formula to floating precision (`37.917187078726606` versus `37.91718707872661`). This is only a check; the proof is the exact exterior-algebra computation above.

## 4. Live-threshold constants

At `J_sep=1/2304`, `M0=1`, `MR=MC=2`:

- density constant:
  `3*4^(1/3)*2304^(1/6)=17.306994843688898`;
- assigned weighted time bound:
  `(24/5)*sqrt(pi)*2^(1/3)*2304^(1/12)=20.434611176605927`;
- whole-copy half-Riesz bound:
  previous line divided by `sqrt(2pi)` = `8.152230381911773`;
- partner collision coefficient:
  twice the density constant = `34.613989687377796`.

For comparison, the current grouped projected-crossing `k=1,ell=2` constant is

`3*2^(7/6)*exp(1/3)=9.39913188784886`,

whereas the marginal-free disjoint-`E3` constant is

`3*2^(4/3)*exp(1/3)=10.550168831164775`.

## 5. Residual compound-tail check

For squared singular values `lambda_1>=lambda_2>=...>=0`, put `E2=e_2(lambda)`, `E3=e_3(lambda)`, `T2=sum_(i>=3)lambda_i`. Counting every triple by its three contained pairs gives

`3E3=sum_(|I|=2)(prod_(i in I)lambda_i) sum_(j notin I)lambda_j`.

For every pair `I`, the complement sum is at least the tail remaining after deleting the two largest entries, namely `T2`. Therefore

`T2 E2<=3E3`.

If `E2>4/9` and `E3<=eta`, then `T2<(27/4)eta`, as stated.

## 6. Correction audit

- no conditional cap for `X-X'` given `X+X'` is used;
- no rotated projection coordinates are called independent inside a bank;
- only the three original source banks `X_j`, `X_R`, `X_C` are asserted independent;
- no scalar pointwise quadratic-phase decay is invoked;
- no small matrix tail is deleted as a small random quadratic perturbation;
- the arbitrary same-bank rank-one half-Riesz interface is not used;
- continuity is asserted only because this branch has `phi in L1`.

`QFORM_B03_R43_CHECK_PASS`
