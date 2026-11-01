# Round 146 log

Added `cor:matched-count-buffered-scale-amplification`.

Round 145 used the final buffered count
`chiBar_p^{1-19 theta}` to force `2^j > B log_Delta chiBar_p` for
`2B < 1-19 theta`.  Round 146 pushes this to the stronger pre-thinning matched
count.  Before the packing and cross-separation losses, the matched anchored
incidence obstruction has

```tex
m >= (sigma_j^3/(16 Delta^3)) chiBar_p^{1-6 theta}
```

distinct anchors in `B(x,2^{j+1})`.  Therefore `2^j <= B log_Delta chiBar_p`
contradicts bounded degree whenever `2B < 1-6 theta`.  The subsequent
deterministic thinning steps preserve the same `p,x,j`, so the final buffered
tube obstruction inherits

```tex
2^j > B log_Delta chiBar_p
```

for every `5 theta < B < (1-6 theta)/2`.
