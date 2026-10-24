# Round 150 log

Added `cor:volume-sensitive-separated-backscatter-fan`.

Round 149 produced a raw backscatter fan at scale

```tex
2^j > B log_Delta chiBar_p
```

whenever `2B log_Delta omega < 1`.  Round 150 extracts a `2r_p`-separated
subfan using the same volume-growth bound

```tex
|B(u,R)| <= C_vol omega^R.
```

With `r_p=floor(theta log_Delta chiBar_p)`, the packing denominator is now

```tex
C_vol omega^{2r_p} <= C_vol chiBar_p^{2 theta log_Delta omega}
```

instead of the old crude `Delta chiBar_p^{2 theta}`.  Thus the separated fan
has size

```tex
|Z_theta| >= (sigma_j^2/(4 C_vol))
             chiBar_p^{1-2 theta log_Delta omega}.
```

It preserves the improved logarithmic scale, the annular relation
`d(x,z) in I_j`, and the per-anchor backscatter mass
`(sigma_j/2) chiBar_p`.
