# Round 152 log

Added `cor:volume-sensitive-point-gated-fan-obstruction`.

Round 151 produced the volume-sensitive gated fan energy lower bound

```tex
G_{p,r_p}^{I_j}(x,K,Z_theta)
  >= (sigma_j^3/(8 C_vol))
     chiBar_p^{2-2 theta log_Delta omega}.
```

Gate-pair selection loses the square of the sphere size at radius `r_p`.
Under `|B(u,R)| <= C_vol omega^R`,

```tex
M_{r_p} <= C_vol omega^{r_p}
        <= C_vol chiBar_p^{theta log_Delta omega}.
```

Therefore the point-gated energy satisfies

```tex
H_{p,r_p}^{I_j}(x,K,Z_theta,a,b)
  >= (sigma_j^3/(8 C_vol^3))
     chiBar_p^{2-4 theta log_Delta omega}.
```

This is the volume-sensitive analogue of the old point-gated fan obstruction,
with the exponent loss governed by `log_Delta omega` rather than the crude
maximum-degree exponent.
