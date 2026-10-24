# Round 149 log

Added `cor:volume-sensitive-logarithmic-backscatter-fan`.

Round 148 pushed the later buffered tube scale using volume growth.  Round 149
applies the same idea at the earlier backscatter-fan stage, where the original
finite set `K` and the annular two-point mass are still visible.

If

```tex
|B(u,R)| <= C_vol omega^R
```

and a fan scale satisfied `2^j <= B log_Delta chiBar_p`, then the root fan
would be trapped inside at most

```tex
C_vol chiBar_p^{2B log_Delta omega}
```

vertices.  But the fan extraction gives roughly

```tex
sigma_j^2 chiBar_p
```

vertices, with only a polylogarithmic loss at logarithmic scale.  Thus
`2B log_Delta omega < 1` forces

```tex
2^j > B log_Delta chiBar_p.
```

For maximum degree `Delta >= 3`, the universal tree-volume bound permits
`omega=Delta-1`, giving the range

```tex
B < 1/(2 log_Delta(Delta-1)).
```
