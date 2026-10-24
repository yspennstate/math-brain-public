# Deterministic checks for QFORM-MULTIHUB-PLUCKER-SMOOTHING-v1

Run: `20260923T084809Z-account01-B09-QFORM-auto13`.

## Constant algebra

Let

`alpha=h+r/2=(r+2h)/2`, `d=r+h`.

The source-coordinate hub/Fresnel/Pluecker factors multiply as

`(2|t|)^(-h) * (4pi|t|)^(-r/2) * (2pi)^d`

`=2^(-h-r+r+h) pi^(-r/2+r+h) |t|^(-h-r/2)`

`=pi^alpha |t|^(-alpha)`.

Thus

`A=pi^alpha e^(d/2) K^(-1/2)`,

where

`K=rho det(G) prod_k |lambda_k|`.

For `alpha>1`,

`int_R min(1,A|t|^(-alpha)) dt`

`=2 A^(1/alpha) + 2A int_(A^(1/alpha))^infinity t^(-alpha)dt`

`=2 alpha/(alpha-1) A^(1/alpha)`.

After the Fourier factor `(2pi)^(-1)`, the density constant is

`alpha/[pi(alpha-1)] A^(1/alpha)`

`=alpha/(alpha-1) e^(d/(2alpha)) K^(-1/(2alpha))`

`=((r+2h)/(r+2h-2)) e^((r+h)/(r+2h)) K^(-1/(r+2h))`.

For `h=2`, this is exactly

`((r+4)/(r+2)) e^((r+2)/(r+4)) K^(-1/(r+4))`,

matching account02/B09 r13.

For `h=3,r=0`,

`C_(3,0)=(6/4)e^(3/6)=(3/2)sqrt(e)=2.473081906...`.

For `h=1,r=1`,

`C_(1,1)=3e^(2/3)=5.843202...`.

## Pluecker disjointness for disjoint flat groups

For `h` mutually disjoint groups of size `m` and one unit-flat hub-coupling column on each group, a Pluecker basis contains exactly one coordinate from each group, uniformly and independently. Two iid bases are disjoint iff their choices differ in every group, hence

`rho=(1-1/m)^h`.

For `h=3,r=0`, the theorem therefore gives

`(3/2)sqrt(e) rho^(-1/6)`

`=(3/2)sqrt(e) (1-1/m)^(-1/2)`.

At `m=16` this equals `2.5541880096... <2.555`.

For the designated-partner `h=2,r=0` theorem, the same construction gives

`2sqrt(e)(1-1/m)^(-1/2)`.

At `m=16` this equals `3.4055840128... <3.406`.

## Target spectral check

For every `epsilon>0`, each grouped two-dimensional block

`B_epsilon=[[epsilon,1],[1,0]]`

has eigenvalues

`lambda_+=(epsilon+sqrt(epsilon^2+4))/2`,
`lambda_-=(epsilon-sqrt(epsilon^2+4))/2`.

Since `sqrt(epsilon^2+4)>2`, one has `lambda_+>1`. Thus three orthogonal copies of `B_epsilon` give at least three eigenvalues of modulus at least one. For the two-hub designated-partner stress, two copies plus an independent `[1]` square give at least three eigenvalues of modulus at least one.

These are exact symbolic checks; no Monte Carlo or histogram is used.