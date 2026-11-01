# Round 148 log

Added `cor:volume-sensitive-matched-scale-amplification`.

Round 146 used the crude bounded-degree estimate

```tex
|B(x,2^{j+1})| <= Delta chiBar_p^{2B}
```

when `2^j <= B log_Delta chiBar_p`.  Round 148 records the sharper version
available whenever the graph has a ball-growth bound

```tex
|B(u,R)| <= C_vol omega^R.
```

The same matched-count contradiction now uses

```tex
|B(x,2^{j+1})| <= C_vol chiBar_p^{2B log_Delta omega}.
```

Thus the buffered obstruction is forced to satisfy

```tex
2^j > B log_Delta chiBar_p
```

whenever `2B log_Delta omega < 1-6 theta`.  In particular, the universal
tree-volume bound for maximum degree `Delta >= 3` gives `omega=Delta-1`, so
the allowed logarithmic threshold improves to

```tex
B < (1-6 theta)/(2 log_Delta(Delta-1)).
```
