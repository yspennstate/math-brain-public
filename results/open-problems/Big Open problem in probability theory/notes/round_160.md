# Round 160 log

Added `cor:volume-sensitive-improved-logarithmic-gate-scale`.

Round 159 localized the obstruction and gave

```tex
|A| >= hat{kappa}_j^vol(p)
  = (sigma_j^3/(16 C_vol^3))
    chiBar_p^{1 - 2 theta - 4 theta log_Delta omega}.
```

If `2^j < a L`, where `L = log_Delta chiBar_p`, then

```tex
A subset B(x, 2^{j+1} + r_p)
```

and the volume-growth assumption gives

```tex
|A| <= C_vol omega^{2^{j+1}+r_p}
     < C_vol chiBar_p^{(2a+theta) log_Delta omega}.
```

The lower bound contradicts this upper bound near criticality whenever

```tex
(2a + theta) log_Delta omega
  < 1 - 2 theta - 4 theta log_Delta omega.
```

Therefore the localized obstruction can be chosen with

```tex
2^j >= a log_Delta chiBar_p.
```

This is the volume-sensitive analogue of Round 133, replacing the crude
maximum-degree exponent by `log_Delta omega`.
