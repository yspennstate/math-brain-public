# Deterministic checks — fleet01/B04 r21

These checks support finite algebra only; the universal inequalities are proved in REPORT.md.

## Pair/remainder constants

For `B=[[1,3],[3,1]]`, the eigenvalues are `4,-2`, so

- `D=|det B|=8`,
- `kappa=sigma_min(B)=2`,
- `||B^(-1)||_op=1/2`.

For

`u=(1,1,1)/sqrt(3)`, `v=(1,2,-3)/sqrt(14)`,
`M=2[u^T;v^T]`,

one has `u dot v=0`, `||u||=||v||=1`, hence

`M M^T=4 I_2`, so `s1(M)=s2(M)=2` and `||M||_F^2=8`.

The partner clean-bank theorem therefore gives

`K_partner=2sqrt(pi)/sqrt(4)=sqrt(pi)=1.7724538509055159...`.

The exact two-physical-coordinate projection cap is `L=1`, giving

`K_exact=sqrt(2*pi)/2=sqrt(pi/2)=1.2533141373155001...`.

For the pair-log bounded-remainder compiler,

`eta_partner=8*K_partner*D/kappa=32sqrt(pi)=56.71852322897651...`,

`B_partner=(1/sqrt(8))*(3+log eta_partner)=2.4883444173432583...`.

With the exact projection cap,

`eta_exact=8*K_exact*D/kappa=32sqrt(pi/2)=40.106052394096004...`,

`B_exact=(1/sqrt(8))*(3+log eta_exact)=2.365812149409690...`.

## Dense matrix

With

`F=0.1[[1,1],[1,-1]]`,
`L=0.01[[1,2,3,4,5],[2,3,5,7,11]]`,
`S=[[F,M],[M^T,0_3]]`,
`A_*=[[B,L],[L^T,S+L^T B^(-1)L]]`,

the numerical physical matrix is

```
[[ 1.0000000000,  3.0000000000,  0.0100000000,  0.0200000000,  0.0300000000,  0.0400000000,  0.0500000000],
 [ 3.0000000000,  1.0000000000,  0.0200000000,  0.0300000000,  0.0500000000,  0.0700000000,  0.1100000000],
 [ 0.0100000000,  0.0200000000,  0.1000875000,  0.1001625000,  1.1549505384,  1.1550380384,  1.1551505384],
 [ 0.0200000000,  0.0300000000,  0.1001625000, -0.0997125000,  0.5349724838,  1.0696574676, -1.6027174515],
 [ 0.0300000000,  0.0500000000,  1.1549505384,  0.5349724838,  0.0007000000,  0.0009500000,  0.0013000000],
 [ 0.0400000000,  0.0700000000,  1.1550380384,  1.0696574676,  0.0009500000,  0.0012875000,  0.0017500000],
 [ 0.0500000000,  0.1100000000,  1.1551505384, -1.6027174515,  0.0013000000,  0.0017500000,  0.0023000000]]
```

so every entry is nonzero and the smallest absolute entry is `0.0007=7/10000`.

Numerical eigenvalues are

`[-2.0809649359,-1.9960047033,-1.9256161802,0,1.9299357874,2.0687065342,4.0086059979]`.

The proof does not rely on those eigenvalues. Analytically,

`||F||=sqrt(2)/10`,
`||L||_op <= ||L||_F=sqrt(263)/100`,
`||L^T B^(-1)L|| <=263/20000`.

Therefore Weyl leaves six eigenvalues of absolute value at least

`2-sqrt(2)/10-sqrt(263)/100-263/20000
 =1.6832558963604218... >1`.

## Exact completion identity

Writing the last five coordinates as `z`,

`h^T B h+2 h^T L z+z^T(S+L^T B^(-1)L)z`

expands identically as

`(h+B^(-1)Lz)^T B(h+B^(-1)Lz)+z^T S z`.

Thus the Schur remainder used in the proof is exactly `z^T S z`, not an approximation or a small-tail replacement.
