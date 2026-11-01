# r44 deterministic arithmetic checks

These are finite arithmetic/regression checks only; the proof is in `REPORT.md`.

Using

- `rho_*=0.0006247538095703261`,
- `gamma_*=rho_*/16`,
- `tau_0=sqrt(3/8)`,
- `m_0=sqrt(47/48)`,
- `c_*=sqrt(47)*sqrt(3/8)*sqrt(47/48)/32`,

one obtains

```
gamma_* = 0.00003904711309814538
m_0     = 0.9895285072531598
c_*     = 0.1298203856084677
c_*/gamma_* = 3324.711491017598
(c_*/gamma_*)^2 = 11053706.498504458
```

Thus on `r<=L/2`,

```
N_eff > 11053706.498504458*(L/r)^2
      >= 44214825.99401783.
```

The maximum single-edge squared-mass ratio on that chamber is

```
eps_max=(gamma_*/c_*)^2*(1/2)^2
       =2.2616848025938122e-8.
```

For `M=16`, the greedy partition lower fraction is

```
1/16 - 15*eps_max
=0.06249966074727961,
```

hence every bank has norm fraction at least

```
sqrt(0.06249966074727961)
=0.2499993214936385.
```

The scalar product-projection cap on each bank is consequently at most

```
sqrt(2)/0.2499993214936385
=5.656869602380427
```

times `1/B`.

For the transverse-router inversion, with `x=r/m`,

```
theta(zeta)=zeta*tau_0/(8+4*zeta*tau_0)
```

and solving `x=theta(zeta)` gives exactly

```
zeta=8*x/(tau_0*(1-4*x)).
```

The small-`x` leading coefficient is

```
8/tau_0 = 13.063945294843617.
```

No random simulation or histogram is used.