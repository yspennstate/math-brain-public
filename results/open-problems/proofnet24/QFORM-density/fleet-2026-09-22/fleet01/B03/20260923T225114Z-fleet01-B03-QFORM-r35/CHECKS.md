# Deterministic checks for fleet01/B03 r35

These checks verify displayed algebra/constants only; they are not numerical evidence for the unrestricted conjecture.

## 1. Six-variable geometric Brascamp--Lieb example

For

`U = [[0,I3],[I3,0]]`,

exact matrix multiplication gives `U^T=U`, `U^2=I6`, and `diag(U)=0`. Hence its eigenvalues are `(-1,-1,-1,+1,+1,+1)`.

For every `i`, with `L_i` having rows `e_i^T` and row `i` of `U`, direct multiplication gives

`L_i L_i^T = I2`,

and

`(1/2) sum_i L_i^T L_i = (1/2)(I+U^T U)=I6`.

Thus the geometric BL constant is exactly one. Scaling the second output coordinate by `c` gives `B(cU)=|c|^-3`, and the theorem gives

`||p||_infinity <= 6/(6-4) * (|c|^-3)^(2/6) = 3/|c|`.

The weighted whole-copy constant is

`(4*6/5)*sqrt(pi) = 8.507778484346476`.

A fixed-seed-free exact NumPy evaluation produced:

```
eig(U) = [-1,-1,-1,1,1,1]
max |U^2-I| = 0
max_i |L_i L_i^T-I2| = 0
max |(1/2)sum L_i^T L_i-I6| = 0
```

## 2. Time-integral algebra

If

`|phi(t)| <= min(1,K |t|^-alpha)`, `alpha=m/4>1`,

then `t0=K^(1/alpha)` and

`int_R |phi| <= 2 t0 [1 + 1/(alpha-1)] = 2 t0 alpha/(alpha-1)`.

With `K=pi^(m/4) B^(1/2)`, this is

`2*pi*m/(m-4) * B^(2/m)`.

Dividing by `2*pi` gives the density constant `m/(m-4) B^(2/m)`.

Likewise

`int_R |t|^-1/2 |phi(t)|^2 dt`

is bounded by

`4*m/(m-1) * sqrt(pi) * B^(1/m)`.

## 3. Partner constants

The fleet02/B03 grouped-family constants evaluate to

`3*4^(2/3) = 7.559526299369239`,

`(24/5)*4^(1/3)*sqrt(pi) = 13.505256515964009`.

These agree with the source-pinned partner handoff.

## 4. BL-dimension failure of the partner obstruction family

For the `m`-dimensional star-leaf difference subspace `W`, the `m` leaf maps each have image dimension one, the hub map has image dimension one, and the rank-one-bank maps vanish. With all BL exponents `1/2`,

`sum_i (1/2) dim L_i(W) = (m+1)/2 < m = dim W` for every `m>=2`.

Therefore the Brascamp--Lieb dimension condition fails and the phase-space BL constant is infinite on this family. This confirms that the partner grouped theorem is genuinely complementary to r35 rather than an application of the same criterion.
