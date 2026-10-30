SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B03, 2026-09-24T06:25:02Z.
attacking: the genuinely nonzero near-coloop hub-square collar — average the fresh physical hub against its random leaf slope by Plancherel in that slope, retaining every same-leaf phase exactly.

# Early substantive calculation

The previous B03 r49 half-Riesz report left the bare null-pivot near-coloop density as an apparent debt. Fresh source matching shows that exact zero-pivot implication is already closed by `QFORM-FRESH-HUB-DIVISIBLE-TWIST-ABSORPTION-v1` at `yspennstate/math-open-problems@be8062b160868bcc71aff45a77c56ff2d0501a9a`. The live B03 target is therefore the small **nonzero** physical hub square.

Let `H` be a genuine original-coordinate variable with density `f<=1`, independent of a light source object `W`. Let `L=L(W)` have marginal density at most `M`, let `R=R(W)` be arbitrary measurable and let

`Q = a H^2 + 2 gamma H L + R`,  `gamma != 0`.

For fixed `t!=0` and `l`, set

`I_t(l)=int f(h) exp(i t[a h^2+2 gamma l h]) dh`.

Then

`phi_Q(t)=E_W[exp(i t R(W)) I_t(L(W))]`,

so Cauchy--Schwarz and the marginal density cap give

`|phi_Q(t)|^2 <= E|I_t(L)|^2 <= M int |I_t(l)|^2 dl`.

With Fourier convention `hat g(xi)=int g(h)e^{i xi h}dh`, put `g_t(h)=f(h)e^{i t a h^2}`. Since `I_t(l)=hat g_t(2 gamma t l)`, Plancherel gives the exact identity

`int |I_t(l)|^2 dl = pi/(|gamma t|) int f(h)^2 dh <= pi/(|gamma t|)`.

Hence

`|phi_Q(t)|^2 <= min(1, pi M/(|gamma| |t|))`.

Writing `K=pi M/|gamma|`, direct integration at `|t|=K` yields

`int_R |t|^(-1/2)|phi_Q(t)|^2 dt <= 8 sqrt(K)
 = 8 sqrt(pi M/|gamma|)`.

This estimate is completely uniform in the hub-square coefficient `a` and in the dependence between `L` and the arbitrary remainder `R`. It uses no pointwise quadratic-phase decay and no independence after rotation.

For the live exact-rank-three near-coloop form

`Q=a(sqrt(c)X_0+S)^2+2b(sqrt(c)X_0+S)U+uU^2+2vUV+wV^2`,

expansion in the genuine physical hub gives the above form with `H=X_0`, `gamma=sqrt(c)`, `L=aS+bU`. The leaf coefficient vectors of `S,U` are orthogonal with squared norms `1-c,1`, hence

`sigma_L^2=a^2(1-c)+b^2`.

The standard one-dimensional product-projection bound gives

`||p_L||_infinity <= sqrt(2)/sigma_L`.

In the hard collar `c>63/64`, `D=|det Lambda|>=1`, `0<|a|D<2^-12`, and the spectral gap gives `a^2+b^2>=1`; therefore

`sigma_L^2>=1-ca^2>1-2^-24`.

Thus

`M/|gamma| <= sqrt(2)/(sqrt(63/64)*sqrt(1-2^-24))
 = 1.4253933326796289...`,

and the assigned weighted whole-copy time integral is uniformly below

`16.929038195804875...`.

This is an early calculation only; the final report will record the exact collision-Riesz consequence and a weighted-time splice that converts this resource to a genuine linear small-ball bound when a source-disjoint invertible two-bank crossing is present.
