# Round 156 log

Added `cor:volume-sensitive-root-weighted-gate-incidence-obstruction`.

Round 155 gave, for every selected gate,

```tex
sum_{y in K, d(y,a_z) in I_gate} tau_p(y,a_z)
  >= kappa_j^vol(p).
```

Since each two-point function satisfies `tau_p(y,a_z) <= 1`, this implies the
deterministic incidence lower bound

```tex
|{ y in K : d(y,a_z) in I_gate }| >= kappa_j^vol(p)
```

for every `z in Z^sharp`, while the root-weighted visibility

```tex
sum_{z in Z^sharp} tau_p(x,a_z) >= kappa_j^vol(p)
```

is preserved.

Thus the volume-sensitive obstruction has reached the same mostly
combinatorial form as Round 129, with threshold

```tex
kappa_j^vol(p)
  = p^{2r_p} (sigma_j^3/(16 C_vol^3))
    chiBar_p^{1 - 4 theta log_Delta omega}.
```

The remaining probabilistic feature is the aggregate root-to-gate weight.
