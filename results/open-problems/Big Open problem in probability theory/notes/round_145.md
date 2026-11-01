# Round 145 log

Added `cor:buffered-tube-log-scale-amplification`.

The buffered tube obstruction has

```tex
t >= (sigma_j^3/(432 Delta^8)) chiBar_p^{1-19 theta}
```

distinct anchor vertices `z_i` with `d(x,z_i) <= 2^{j+1}`.  If
`2^j <= B log_Delta chiBar_p`, then `sigma_j^3` only loses a polylogarithmic
factor, while bounded degree gives

```tex
t <= |B(x,2^{j+1})| <= Delta chiBar_p^{2B}.
```

For `2B < 1-19 theta` these inequalities are incompatible near criticality.
Thus every counterexample forces the buffered obstruction to occur at scale
`2^j > B log_Delta chiBar_p` for each `5 theta < a < B < (1-19 theta)/2`.
