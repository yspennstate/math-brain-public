# T384 probability lemma: product-log tightness and a simultaneous event

Assume `0<alpha<2`; the pairs `(U_i,W_i)` are iid, and within each pair `U_i,W_i` are independent standard symmetric `alpha`-stable variables, with characteristic function `exp(-|t|^alpha)`. Write `U_+=max(U,0)`,

`a_m=(m log m)^(1/alpha),  f_m=a_m^(-1) sum_{i=1}^m W_i U_{i,+},`

`H_m=m^(-2/alpha) sum_{i=1}^m 1_{U_i>0}(U_i^2+W_i^2)` for `m>=2`, and

`E_m={there exists i: 0<U_i<1 and -2m^(1/alpha)<=W_i<=-m^(1/alpha)}`.

The only input about the stable law is its standard tail: for a constant `c_alpha=Gamma(alpha)sin(pi alpha/2)/pi>0`, `P(W<-t)~c_alpha t^(-alpha)` and `P(|U|>t)+P(|W|>t)<=C_alpha min(1,t^(-alpha))` for `t>=1`. (The upper bound can be restated as `C_alpha t^(-alpha)` for all `t>0` after enlarging C.) The one-sided asymptotic and normalization appear, for example, in [Bednorz--Lochowski--Martynek, arXiv:1802.00612v3](https://arxiv.org/html/1802.00612v3), Introduction, equations (68)--(77), and [arXiv:2008.04423v1](https://arxiv.org/html/2008.04423v1), preliminaries (1.7). Everything below derives from that input, without a limit theorem for sums of products.

## 1. The logarithmic product normalization is tight

Let `X=W U_+`. Conditioning on U and splitting at `U_+=t`, for `t>=e`,

`P(|X|>t) <= P(U_+>t)+C_alpha t^(-alpha) E[U_+^alpha 1_{U_+<=t}] <= C t^(-alpha)(1+log t).`  (1)

Indeed, the truncated moment is bounded by `alpha int_0^t s^(alpha-1)P(U_+>s)ds`, whose integral above 1 is `O(log t)`. The same bound with `1+log_+t` and an adjusted C holds at all positive t. Tail integration then gives, for `b>=e`,

`E[X^2 1_{|X|<=b}] <= 2 int_0^b t P(|X|>t)dt <= C b^(2-alpha)(1+log b).`  (2)

The truncated variable `X 1_{|X|<=b}` has mean zero: conditional on U it is an odd truncation of the symmetric W. For `M>=1`, put `b=M a_m`. By a union bound followed by Chebyshev, using independence across i,

`P(|f_m|>2M) <= m P(|X|>b)+m E[X^2 1_{|X|<=b}]/b^2`

`<= C m b^(-alpha)(1+log b) <= C_alpha M^(-alpha)(1+log M),`  (3)

uniformly for `m>=2`: `m/a_m^alpha=1/log m` and `log a_m/log m` is bounded. The right side tends to zero as M grows. Thus `{f_m}` is tight. The logarithm is essential in (1): replacing `a_m` by `m^(1/alpha)` would leave the variance/large-jump bound growing like `log m`.

## 2. The positive `alpha/2`-tail sum is tight

Put `beta=alpha/2 in (0,1)` and `Z=1_{U>0}(U^2+W^2)`. The union bound on the two squares yields

`P(Z>t)<= C t^(-beta)` for every `t>0`, after adjusting C. Consequently

`E[Z 1_{Z<=b}] <= int_0^b P(Z>t)dt <= C b^(1-beta)` for all `b>0`.  (4)

With `b=K m^(1/beta)=K m^(2/alpha)`, a union bound for a term above b and Markov's inequality for the truncated sum give

`P(H_m>K) <= mP(Z>b)+(m/b)E[Z 1_{Z<=b}] <= C K^(-beta)`  (5)

uniformly in m. This proves tightness without invoking convergence to a positive stable law.

## 3. The rare event has a nonzero limiting probability

Let `p_0=P(0<U<1)>0`: Fourier inversion of `exp(-|t|^alpha)` gives a continuous density with `f_U(0)=pi^(-1) int_0^infinity exp(-t^alpha)dt>0`, so a short interval inside `(0,1)` has positive mass. Let `c=1-2^(-alpha)>0`. A single sample qualifies with probability

`r_m=p_0[P(W<=-m^(1/alpha))-P(W<-2m^(1/alpha))]`,

so the stable tail asymptotic implies `m r_m -> lambda_* := p_0 c_alpha c >0`. The qualifying indicators are iid, hence

`P(E_m)=1-(1-r_m)^m -> p_*:=1-exp(-lambda_*)>0`.  (6)

In particular, this conclusion does not condition on the other observations or on f and H.

## 4. One fixed choice of y, R, K works simultaneously

By (3) choose `M>=1` so large that `sup_{m>=2}P(|f_m|>M)<p_*/4`. By (5) choose `K` so large that `sup_{m>=2}P(H_m>K)<p_*/4`. Take the fixed constants `y=M+1` and `R=2M+1`. If `|f_m|<=M`, then `1<=y-f_m<=R`. The union bound gives, without any independence assertion between the three events,

`P(E_m and 1<=y-f_m<=R and H_m<=K)`

`>=P(E_m)-P(|f_m|>M)-P(H_m>K).`

Therefore, by (6),

`liminf_{m->infinity}P(E_m intersect {1<=y-f_m<=R, H_m<=K}) >= p_*/2>0`.  (7)

This is exactly the claimed probability/tightness step. It does not claim a joint weak limit or independence of the rare event from the normalized sums.
