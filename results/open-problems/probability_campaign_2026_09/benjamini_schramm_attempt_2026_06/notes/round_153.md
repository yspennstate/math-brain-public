# Round 153 log

Added `cor:volume-sensitive-one-gate-fan-obstruction`.

Round 152 produced explicit gate pairs with

```tex
H_{p,r_p}^{I_j}(x,K,Z_theta,a,b)
  >= (sigma_j^3/(8 C_vol^3))
     chiBar_p^{2 - 4 theta log_Delta omega}.
```

The existing gate-coalescence lemma applies without any new geometric loss:

```tex
J_{p,r_p}^{I_j}(x,K,Z_theta,a)
  >= p^{2r_p} H_{p,r_p}^{I_j}(x,K,Z_theta,a,b).
```

Therefore the volume-sensitive one-gate obstruction is

```tex
J_{p,r_p}^{I_j}(x,K,Z_theta,a)
  >= p^{2r_p} (sigma_j^3/(8 C_vol^3))
     chiBar_p^{2 - 4 theta log_Delta omega}.
```

I kept the exact factor `p^{2r_p}` rather than replacing it by a rough
susceptibility power.  This matches the older maximum-degree reduction and
sets up the high one-gate layer extraction with threshold

```tex
kappa_j^vol(p)
  = p^{2r_p} (sigma_j^3/(16 C_vol^3))
    chiBar_p^{1 - 4 theta log_Delta omega}.
```
