# HARD7-02 analytic artifact — Gaussian smoothing bridge for the discrete periodic band

Freeze `N`, `0<=W<N/2`, `L=2W+1`, and the periodic hard-indicator support. Let `epsilon_ij` be independent symmetric Rademacher variables and `g_ij` independent standard real Gaussians. On the band define

`X_0(i,j)=epsilon_ij/sqrt(L)`

and, for `t>0`,

`X_t(i,j)=(epsilon_ij+sqrt(t) g_ij)/sqrt((1+t)L)`.

Off the band both matrices are zero. Thus every nonzero atom of `X_t` is centered, variance `1/L`, has a bounded density for fixed `t>0`, and converges in law to the Rademacher atom as `t downarrow 0`.

For `z in C`, let

`nu_{N,z}^{(t)} = (1/N) sum_{j=1}^N delta_{s_j(X_t-zI)}`

be the empirical singular-value measure.

## Lemma 1 — uniform Wasserstein-2 coupling

For every `N,W,z,t`, under the coupling above,

`E W_2(nu_{N,z}^{(t)},nu_{N,z}^{(0)})^2 <= q(t)`

where

`q(t)=2(1-(1+t)^(-1/2)) <= t`.

Hence for every 1-Lipschitz `f:[0,infinity)->R`,

`E |int f dnu_{N,z}^{(t)} - int f dnu_{N,z}^{(0)}| <= sqrt(q(t)) <= sqrt(t)`.

### Proof

Mirsky's singular-value inequality gives

`sum_j (s_j(X_t-zI)-s_j(X_0-zI))^2 <= ||X_t-X_0||_HS^2`.

The shift `-zI` cancels in the difference. For one in-band entry,

`E |X_t(i,j)-X_0(i,j)|^2`
`= L^(-1)[((1+t)^(-1/2)-1)^2 + t/(1+t)]`
`= L^(-1) 2(1-(1+t)^(-1/2))`
`=q(t)/L`.

There are exactly `NL` in-band entries, so

`E ||X_t-X_0||_HS^2 = N q(t)`.

Couple the ordered singular values; division by `N` proves the `W_2^2` bound. Kantorovich/Cauchy-Schwarz gives the Lipschitz-test estimate. Finally `(1+t)^(-1/2)>=1-t/2` for `t>=0`, so `q(t)<=t`. `QED`

## Consequence — the atom-deformation route has only a hard-edge debt

For every fixed `t>0`, Han's September 2026 periodic hard-indicator theorem applies to the smoothed atoms (fixed bounded density and finite moments) whenever `W_N->infinity`, yielding the circular law for `X_t`.

Lemma 1 shows that the singular-value measures for `X_t-zI` and the exact Rademacher matrix `X_0-zI` are uniformly close for all bounded Lipschitz singular-value observables as `t downarrow 0`, independently of `N`, `W`, and `z`.

This does **not** transfer Girko's logarithmic potential because `log s` is unbounded at `s=0`. A sufficient missing input is a uniform hard-edge log-integrability estimate for the discrete endpoint, for almost every fixed `z`, of the form

`lim_{delta downarrow 0} limsup_{N->infinity} P( int_{(0,delta)} |log s| nu_{N,z}^{(0)}(ds) > epsilon ) = 0`

for every `epsilon>0`, together with the corresponding upper-tail control (the latter is routine from second moments). With such a bound, truncate `log` to a Lipschitz function on `[delta,M]`, use Lemma 1 and then send `t downarrow 0`, `delta downarrow 0`, `M up infinity`; Girko Hermitization would transfer the known smoothed circular law to `t=0`.

Thus the bounded-density-to-Rademacher deformation is quantitatively successful away from the hard edge and fails only at the exact place highlighted by the source: discrete anti-concentration / small singular values. No circular-law exponent improvement is claimed here.