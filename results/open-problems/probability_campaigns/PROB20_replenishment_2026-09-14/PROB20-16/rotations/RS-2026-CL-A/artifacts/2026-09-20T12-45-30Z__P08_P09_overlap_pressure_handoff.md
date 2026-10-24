# RS-2026-CL-A -> P08/P09 handoff — overlap-pressure identities

**Timestamp:** 2026-09-20T12:45:30Z  
**Ownership:** RS-2026-CL-A retains source ownership. This file is a reusable lemma handoff only; do not relabel the source claim.

## 1. Boolean latent-product exact second moment

Let `U_N` be uniform on `{-1,+1}^N`. Suppose `P` is a latent mixture such that conditional on `Z`, coordinates are independent and

`E[X_i|Z]=b_i(Z)`.

Let `T_rho` be product noise with Fourier retention eigenvalue `rho`. Conditional on `Z`, the noised coordinate means are `rho b_i(Z)`. Therefore the conditional likelihood ratio is

`L_Z(x)=prod_i (1+rho b_i(Z)x_i)`.

For independent `Z,Z'`, orthogonality under `U_N` gives the exact identity

`1+chi^2(T_rho P || U_N)`

`= E_{Z,Z'} prod_i [1+rho^2 b_i(Z)b_i(Z')]`.

This is often substantially sharper than a bound through only `E||b||^2`, because mixture cancellation is retained inside the overlap product.

### Rank-one graph specialization

For graph-edge coordinates and latent vertex spins,

`b_{ij}(sigma)=theta sigma_i sigma_j`,

put `u_i=sigma_i tau_i` for two independent latent spin configurations. Then

`1+chi^2 = E_u prod_{i<j}(1+lambda u_i u_j)`,

with `lambda=rho^2 theta^2`. If `S=sum_i u_i` and `N=binom(n,2)`, this becomes exactly

`(1-lambda^2)^{N/2} exp(-beta n) E exp(beta S^2)`,

where

`beta=(1/2) artanh(lambda)`.

Using the Gaussian linearization and `cosh x <= exp(x^2/2)`,

`E exp(beta S^2) <= (1-2n beta)^(-1/2)`

when `2n beta<1`. Hence

`1+chi^2 <= [1-n artanh(lambda)]^(-1/2)`.

This is the overlap-pressure mechanism used by RS-2026-CL-A to turn low-degree cycle pressure into an all-test post-noise result.

## 2. Gaussian mean-mixture exact second moment

Let the null be `gamma_m=N(0,I_m)` and suppose

`X|Z ~ N(b(Z),I_m)`.

After OU correlation `rho`, conditional means become `rho b(Z)`. The likelihood ratio of `N(rho b,I_m)` against `gamma_m` is

`L_b(x)=exp(rho <b,x> - (rho^2/2)||b||^2)`.

Therefore, for independent `Z,Z'`,

`E_{gamma_m}[L_{b(Z)}L_{b(Z')}] = exp(rho^2 <b(Z),b(Z')>)`,

and hence exactly

**Gaussian overlap identity**

`1+chi^2(T_rho P || gamma_m)`

`= E_{Z,Z'} exp(rho^2 <b(Z),b(Z')>)`.

Thus an exponential-moment estimate for latent overlaps immediately yields an all-test contiguity statement. In particular, if

`sup_n E exp(rho^2 <b(Z),b(Z')>) < infinity`,

then any null-rare event remains planted-noise rare by Cauchy–Schwarz.

## 3. Tensor/correlation interpretation

The reusable pattern is:

1. low-degree moments constrain a hierarchy of contractions/cycles of a latent kernel;
2. the noisy `chi^2` norm is an exponential or product partition function of the overlap of two independent latent replicas;
3. fixed noise shrinks the overlap coupling by `rho^2`;
4. if low-degree control places the pre-noise coupling at or below the critical overlap pressure, fixed `rho<1` moves it strictly subcritical.

For Gaussian/tensor roles, the promising target is therefore **not** merely a global bound on `E||b||^2`; it is an exponential-moment bound on `<b(Z),b(Z')>` or the analogous tensor overlap. This can retain cancellations that energy-only Hellinger arguments lose.

## 4. Scope warning

These are exact identities, but they do not by themselves prove a Gaussian-process or tensor theorem. P08/P09 still need a model-specific way to bound the overlap partition function from their available covariance/contraction information. No RS-2026-CL-A source ownership is transferred.
