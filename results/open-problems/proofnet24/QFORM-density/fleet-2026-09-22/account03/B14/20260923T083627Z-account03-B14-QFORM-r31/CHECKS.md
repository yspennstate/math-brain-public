# Quantitative checks for account03/B14 r31

These are arithmetic/algebra sanity checks; the universal proof is in REPORT.md.

Let

`f_low(r)=2sqrt(2)/r + 4K r^2/(kappa sqrt(D))`.

Solving `f_low'(r)=0` gives

`r_*=sqrt(2) D^(1/6) kappa^(1/3)/(2K^(1/3))`.

Substitution gives

`f_low(r_*)=6 K^(1/3)/(D^(1/6) kappa^(1/3))`

and

`4K r_*^2/kappa = 2(DK/kappa)^(1/3)`.

Hence the low stationary point lies in the linear `Psi` branch exactly when `DK/kappa<=1/8`.

For the logarithmic branch,

`f_log(r)=2sqrt(2)/r + D^(-1/2)[1+log(4Kr^2/kappa)]`.

Solving `f_log'(r)=0` gives

`r_*=sqrt(2D)`,

`4K r_*^2/kappa=8DK/kappa`,

`f_log(r_*)=D^(-1/2)[3+log(8DK/kappa)]`.

Thus the log stationary point belongs to its branch exactly when `DK/kappa>=1/8`.

At `DK/kappa=1/8`, both branch values equal `3/sqrt(D)`.

For the diffuse normalized stress family in REPORT.md, `D=kappa=P=1` and `K=pi e`, so the log branch applies and

`G=3+log(8 pi e)=7.224171427529236...`.

The stress bank matrix `S0=a_m a_m^T+b_m b_m^T` has nonzero eigenvalues exactly `1,1`, hence `pdet_abs(S0)=1` for every `m`. The full block-diagonal matrix `[[0,1],[1,0]] direct_sum S0` has nonzero eigenvalues `1,-1,1,1`, independently of `m`.
