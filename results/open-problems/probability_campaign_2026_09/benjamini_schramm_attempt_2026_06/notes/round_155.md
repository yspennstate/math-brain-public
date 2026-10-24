# Round 155 log

Added `cor:volume-sensitive-expanded-gate-annulus-obstruction`.

Round 154 produced a high one-gate layer with

```tex
sum_{z in Z^sharp} tau_p(x,a_z) >= kappa_j^vol(p),

sum_{y in K, d(y,z) in I_j} tau_p(y,a_z) >= kappa_j^vol(p)
  for every z in Z^sharp.
```

The only new step is the triangle-inequality enlargement from annuli centered
at the remote anchor `z` to annuli centered at the selected gate `a_z`.  Since
`d(a_z,z)=r_p`,

```tex
d(x,z), d(y,z) in (2^j,2^{j+1}]
  => d(x,a_z), d(y,a_z) in (2^j-r_p, 2^{j+1}+r_p].
```

Thus the same threshold

```tex
kappa_j^vol(p)
  = p^{2r_p} (sigma_j^3/(16 C_vol^3))
    chiBar_p^{1 - 4 theta log_Delta omega}
```

now holds directly at the gate vertices:

```tex
sum_{y in K, d(y,a_z) in I_gate} tau_p(y,a_z) >= kappa_j^vol(p).
```

No additional volume-growth or degree loss occurs in this bridge.
