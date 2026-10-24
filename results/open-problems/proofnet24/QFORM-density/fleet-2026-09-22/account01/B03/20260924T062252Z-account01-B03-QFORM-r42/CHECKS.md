# Checks for account01/B03 r42

Run: `20260924T062252Z-account01-B03-QFORM-r42`.

These are algebra/constant checks only; they are not numerical evidence for the unrestricted conjecture.

## 1. Tail exponent and optimization

From

`K=int |t|^-1/2 G(t)^2 dt`

and

`int_(|t|>T)|t|^-3/2 dt=4 T^-1/2`,

Cauchy-Schwarz gives

`int_(|t|>T)|t|^-1 G(t)dt <=2 sqrt(K) T^-1/4`.

Thus

`F(T)=2T+A T^-1/4`, `A=2 pi P sqrt(K)`.

`F'(T)=2-(A/4)T^-5/4`, so

`T_*=(A/8)^(4/5)=(pi P sqrt(K)/4)^(4/5)`.

At `T_*`, `A T_*^-1/4=8T_*`, hence `F(T_*)=10T_*`, and Fourier inversion gives

`||p||inf <=(5/pi)(pi P sqrt(K)/4)^(4/5)`.

## 2. Partner splice constant

Using

`P<=sqrt(2) D^-1/4`,

`K<=K0 E0^-1/12`,

`K0=29.1511643034760`,

the coefficient is

`C_mix=(5/pi)[(pi/4)sqrt(2)sqrt(K0)]^(4/5)`

`=6.670623008323879...`.

The exponents are

`D: (-1/4)*(4/5)=-1/5`,

`E0: (-1/24)*(4/5)=-1/30`.

Under `A -> sA`, `D -> s^4 D` and `E0 -> s^6 E0`, hence

`s^(-4/5) s^(-1/5)=s^-1`.

## 3. Density-cap posterior collision corollary

If `||p_Z||inf<=M`, then `||p_(Z-Z')||inf<=M`. The cap-one-dimensional bathtub estimate gives

`E|Z-Z'|^-1/2 <=2 sqrt(2M)`.

With the positive half-Riesz Fourier identity,

`int |t|^-1/2 |phi_Z(t)|^2dt
 <=sqrt(2pi)*2sqrt(2M)=4sqrt(pi M)`.

Substituting `K=4sqrt(pi M)` into the compiler gives

`||p_Q||inf
 <=5*2^(-4/5) P^(4/5) M^(1/5)`

with constant

`5*2^(-4/5)=2.871745887492587...`.

## 4. Six-coordinate hyperbolic matching exterior mass

For

`H_3=[[0,I3],[I3,0]]`,

every disjoint ordered triple pair in six coordinates has `T=S^c`. Direct determinant enumeration shows exactly eight ordered triples `S` with

`|det H_3[S,S^c]|=1`;

all other such determinants vanish. Therefore

`E0(c H_3)=8 c^6`.

For `B=kI2`, `D=k^4`, and `c=k^-4`,

`C_mix D^-1/5 E0^-1/30
 =C_mix k^-4/5 (8k^-24)^-1/30
 =C_mix 8^-1/30`

`=6.223911340870686...`.

## 5. Dependence boundary

The proof uses only:

- original-coordinate source disjointness of H, Y, W;
- two-dimensional Plancherel after pushing Y through the slope map;
- conditional whole-copy quantities `|psi_u(t)|^2`;
- Cauchy-Schwarz after the weighted time budget is formed.

It does **not** use independence of `X-X'` and `X+X'`, a conditional cap for either one, or a pointwise quadratic-phase decay bound.

The hub-conditional variant permits H-W coupling but not Y-W coupling. The bank-conditional variant permits Y-W coupling but not H-W coupling. A residual coupled simultaneously to both sides is not claimed.
