# Exact arithmetic checks — fleet02/B20 auto11c

These checks support `REPORT.md`; they are not a substitute for its proofs.

## D5 collar at T=1/1024

Let `c=1/4096`, `T=1/1024=4c`, and use `s1^2>361/1024`.

`T(T-c)(T-2c)(T-3c)/24 = (4c)(3c)(2c)(c)/24 = c^4 = 1/4096^4`.

Hence

`Z5 > (361/1024)/4096^4 = 361/288230376151711744 = 1.2524703496552547e-15`.

Pinned D5 gives

`5 sqrt(2e) Z5^(-1/10) = 360.45868813121774 < 360.459`.

Therefore every unpaid nested state has `||R||F^2<1/1024`, so `||R||F<1/32`.

The Q-arm improves exactly:

`31/64 - 1/32 = 29/64`.

The K-arm is

`sqrt(749373/2097152)-1/64 = 0.5821449321261905 > 37/64`.

## Route counterexample at m=8

`n=32`, plus/minus group sizes are `16,16`.
The cut has plus/minus row sizes `14,2` and plus/minus column sizes `2,14`.
The opposite-sign entry is `c=1/(2m)=1/16`.

The two cross singular values are

`c sqrt(14*14)=7/8`,
`c sqrt(2*2)=1/8`.

Thus

`E=49/64+1/64=25/32=0.78125`,
`11907/16384=0.72674560546875`,
`E-11907/16384=893/16384=0.05450439453125`.

`Z2=(7/8)^2(1/8)^2=49/4096=0.011962890625`.

Every nonzero physical principal pair determinant has magnitude

`c^2=1/256<1/64`.

The row- and column-pair disjointness probability is

`delta=(1-1/14)(1-1/2)=13/28=0.4642857142857143`.

The completed E2 half-Riesz theorem yields

`4 sqrt(2e) (49/4096)^(-1/8) (13/28)^(-1/16)`
`=17.014478057017296 <17.015`.

## Half-Riesz plus disjoint square constants

`sqrt(e)*38.907 = 64.14679847912988 <64.147`.

`sqrt(e)*39.919 = 65.81530440507841 <65.816`.
