# Round 157 log

Added `cor:volume-sensitive-deterministic-gate-incidence-obstruction`.

Round 156 left one probabilistic aggregate:

```tex
sum_{z in Z^sharp} tau_p(x,a_z) >= kappa_j^vol(p).
```

Since each `tau_p(x,a_z) <= 1`, this gives the deterministic lower bound

```tex
|Z^sharp| >= kappa_j^vol(p).
```

The per-gate incidence lower bound is inherited:

```tex
|{ y in K : d(y,a_z) in I_gate }| >= kappa_j^vol(p)
  for every z in Z^sharp.
```

So the volume-sensitive chain now forces a deterministic anchored
gate-incidence configuration with at least `kappa_j^vol(p)` gates and at least
`kappa_j^vol(p)` incident vertices of `K` in each selected gate annulus.  The
threshold remains

```tex
kappa_j^vol(p)
  = p^{2r_p} (sigma_j^3/(16 C_vol^3))
    chiBar_p^{1 - 4 theta log_Delta omega}.
```
