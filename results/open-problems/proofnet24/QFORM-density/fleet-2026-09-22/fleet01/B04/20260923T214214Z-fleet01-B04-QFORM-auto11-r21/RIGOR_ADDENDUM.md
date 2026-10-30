# Rigor addendum: nonzero physical entries and branch constants

This note records exact finite checks used by REPORT.md.

For `B=[[1,3],[3,1]]`,

`B^(-1)=(1/8)[[-1,3],[3,-1]].`

Write the two integer rows of `100 L` as

`a=(1,2,3,4,5)`, `c=(2,3,5,7,11)`.

Then

`(L^T B^(-1)L)_(ij)
 =[-a_i a_j+3a_i c_j+3c_i a_j-c_i c_j]/80000.`

The numerator matrix is exactly

```
[[  7, 13, 20,  27,  36],
 [ 13, 23, 36,  49,  68],
 [ 20, 36, 56,  76, 104],
 [ 27, 49, 76, 103, 140],
 [ 36, 68,104, 140, 184]].
```

Thus every Y-Y entry (the bottom-right 3x3 part, indices 3,4,5 here) is strictly positive, with minimum `56/80000=7/10000`.

Every X-X entry of `F` has magnitude `1/10`, while every correction entry is at most `184/80000<1/400`, so no X-X entry can vanish. Every X-Y entry of `M` has magnitude at least `2/sqrt(14)>1/2`, while every correction entry has magnitude below `1/400`, so no X-Y entry can vanish. The pair block and L itself are visibly entrywise nonzero. Hence every physical entry of the full `A_*` is rigorously nonzero; the minimum absolute entry is indeed `7/10000`.

For the new compiler, set `eta=8KD/kappa`. The exact scalar objective after substituting `x=4Kr^2/kappa` is

`f(x)=A x^(-1/2)+D^(-1/2)F(x)`,
`A=4sqrt(2K/kappa)`,
`F(x)=x` for `x<=1`, `F(x)=1+log x` for `x>=1`.

On the first interval the stationary point is `x=(A sqrt(D)/2)^(2/3)` and is admissible exactly when `eta<=1`. On the second interval the stationary point is `x=A^2 D/4=eta` and is admissible exactly when `eta>=1`. At `eta=1`, both bounds equal `3/sqrt(D)`. Thus no endpoint is missed in the piecewise minimization.
