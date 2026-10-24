# Round 151 log

Added two volume-sensitive gate-layer statements:

- `cor:volume-sensitive-weighted-separated-fan`
- `cor:volume-sensitive-gated-fan-obstruction`

Round 150 gave an unweighted separated fan at the improved logarithmic scale.
Round 151 repeats the weighted averaging step from the older weighted fan
proof, so the separated subfan retains root weight

```tex
sum_z tau_p(x,z)
  >= (sigma_j^2/(4 C_vol))
     chiBar_p^{1-2 theta log_Delta omega}.
```

Multiplying by the pointwise annular backscatter mass gives

```tex
W_p^{I_j}(x,K,Z_theta)
  >= (sigma_j^3/(8 C_vol))
     chiBar_p^{2-2 theta log_Delta omega}.
```

If `theta < B`, the improved scale `2^j > B log_Delta chiBar_p` implies
`r_p < 2^j`, so gate decomposition applies and yields the same lower bound for
the gated fan energy `G_{p,r_p}^{I_j}`.
