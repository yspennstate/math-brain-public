# Checks for QFORM-OVERLAP-HUB-SLOPE-TWO-PLANCHEREL-v1

Run: `20260924T010202Z-fleet03-B14-QFORM-auto11`.

## Plancherel constants

With `hat f(xi)=int exp(i xi x) f(x) dx`, Plancherel is

`int |hat f(xi)|^2 dxi = 2 pi int |f(x)|^2 dx`.

For `G_t(x)=hat F_t(2tx)`, the substitution `xi=2tx` gives

`int |G_t(x)|^2 dx
 = (1/(2|t|)) int |hat F_t(xi)|^2 dxi
 = (pi/|t|) int |F_t(l)|^2 dl`.

The identical computation applies to the slope-bank multiplier `K_t`.

## Slice L2 bound

The assumptions `|F_t(l)|<=A|t|^(-1/2)` and `|F_t(l)|<=nu_l(R)` imply pointwise

`|F_t(l)|^2 <= A |t|^(-1/2) nu_l(R)`.

Since `int nu_l(R) dl=1`,

`||F_t||_2^2 <= A |t|^(-1/2)`

and therefore

`||G_t||_2 <= sqrt(pi A) |t|^(-3/4)`.

## Complex pushforward bound

Let `eta_t(B)=E[e^{itR(Z)} 1_{S(Z) in B}]`. Then `eta_t << Law(S)`. If

`g_t(s)=E[e^{itR(Z)}|S=s]p_S(s)`,

then `|g_t(s)|<=p_S(s)`. Hence

`||g_t||_2^2 <= ||p_S||_infinity int p_S(s)ds <= M`.

Thus

`||K_t||_2 <= sqrt(pi M)|t|^(-1/2)`.

No independence between `R(Z)` and `S(Z)` is needed.

## Fourier endpoint integral

For `K>0`, the crossing point of `1` and `K t^(-5/4)` is `t0=K^(4/5)`. Hence

`int_0^infinity min(1,Kt^(-5/4))dt
 =t0+K[4t^(-1/4)]_{t0}^infinity
 =t0+4K t0^(-1/4)
 =5K^(4/5)`.

Doubling gives

`int_R min(1,K|t|^(-5/4))dt=10K^(4/5)`.

With `K=pi sqrt(AM)`, Fourier inversion yields

`||p_Q||_infinity <= (5/pi) K^(4/5)=5pi^(-1/5)(AM)^(2/5)`.

## Partner substitution

Fleet04/B14 r9 equation (3.6):

`|mu_hat_{v,g}(t)|<=4sqrt(pi)|gamma t|^(-1/2)`.

For `L=hV+q0`, the unnormalised slice is

`nu_l=|h|^(-1)mu_{(l-q0)/h,g}`,

so

`A=4sqrt(pi)/(|h|sqrt(|gamma|))`.

For `S=a^T Z`, the product-projection theorem gives

`M<=sqrt(2)/||a||_2`.

Therefore

`5pi^(-1/5)(AM)^(2/5)
 <=5pi^(-1/5)[4sqrt(pi)sqrt(2)]^(2/5)
   ||a||_2^(-2/5)|h|^(-2/5)|gamma|^(-1/5)
 =10||a||_2^(-2/5)|h|^(-2/5)|gamma|^(-1/5)`.

At `||a||_2>=1`, `|h|>=2^(-1/2)`, `|gamma|>=1`, this is

`10*2^(1/5)=11.48698354997035...`.

No stochastic simulation or histogram is used in any check.
