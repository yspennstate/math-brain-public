# Round 154 log

Added `cor:volume-sensitive-high-one-gate-obstruction`.

Round 153 gave the volume-sensitive one-gate energy lower bound

```tex
J_{p,r_p}^{I_j}(x,K,Z_theta,a)
  >= p^{2r_p} (sigma_j^3/(8 C_vol^3))
     chiBar_p^{2 - 4 theta log_Delta omega}.
```

The existing high one-gate layer extraction applies once the root weights of
the selected gates sum to at most `chiBar_p`.  This follows from the
`2r_p`-separation of `Z_theta`: the balls `B(z,r_p)` are pairwise disjoint, so
the chosen gates `a_z` are distinct.

The extracted high layer `Z^sharp` therefore satisfies

```tex
sum_{z in Z^sharp} tau_p(x,a_z) >= kappa_j^vol(p),

sum_{y in K, d(y,z) in I_j} tau_p(y,a_z) >= kappa_j^vol(p)
  for every z in Z^sharp,
```

where

```tex
kappa_j^vol(p)
  = p^{2r_p} (sigma_j^3/(16 C_vol^3))
    chiBar_p^{1 - 4 theta log_Delta omega}.
```

I used the high-layer range `1 - 4 theta log_Delta omega > 0`, which is the
volume-sensitive analogue of the old `theta < 1/4` condition and keeps the
threshold growing with susceptibility.
