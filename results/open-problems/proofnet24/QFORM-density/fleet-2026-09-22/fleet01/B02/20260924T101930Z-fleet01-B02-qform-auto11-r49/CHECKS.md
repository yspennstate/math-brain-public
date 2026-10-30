# Deterministic checks — fleet01/B02 r49

Run: `20260924T101930Z-fleet01-B02-qform-auto11-r49`.

These are algebra/arithmetic checks for `REPORT.md`; they are not a substitute for independent mathematical review.

## 1. Kernel domination constant

For `0<r<=1`, write `r=e^{-x}`, `x>=0`.

`(1+log(1/r)) r^(1/4)=(1+x)e^{-x/4}`.

Derivative:

`e^{-x/4}(1-(1+x)/4)`.

Unique maximum at `x=3`, value

`4e^{-3/4}=1.8894662109640588... >1`.

Therefore the same constant also dominates `r^{-1/4}` on `r>=1`.

## 2. Fractional-promotion constant

Translated-square source constant: `8`.

Kernel domination constant: `4e^{-3/4}`.

Product:

`32e^{-3/4}=15.11572968771247...`.

Thus

`H_(1/2)(d(X+h)^2+T)
 <=15.11572968771247 |d|^{-1/4} H_(1/4)(T)`.

## 3. Physical-edge quarter-Riesz constant

The source gives

`c_(1/4)=2^(3/4) Gamma(3/8)/(2 sqrt(pi) Gamma(1/8))
        =0.14927036108294767...`

and

`C_edge=16 c_(1/4) pi^(1/4)
       =3.179662567631707...`.

Therefore

`C_nested=(32e^{-3/4})C_edge
          =48.06291987045865...`.

## 4. Live threshold arithmetic

At

`|a|>1/228`, `|d|>1/912`, `|mu|>=1/912`,

Theorem 4.1 gives

`||p_Q||inf
 < C_nested sqrt(228) (912^2)^(1/4)`.

Since `912=4*228`,

`sqrt(228)*(912^2)^(1/4)
 =sqrt(228*912)
 =sqrt(207936)
 =456`.

Hence

`C_nested*456
 =21916.691460929145... <21916.692`.

## 5. Partner target matrix Schur checks

For

`A_*=[[1,0,1,0,0],
      [0,1,0,1,0],
      [1,0,1,0,0],
      [0,1,0,1,0],
      [0,0,0,0,1]]`,

pivoting coordinate five leaves the 4x4 coefficient

`S=[[1,0,1,0],
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1]]`.

On physical banks `U={1,2}`, `V={3,4}`, the cross block is `I_2`, so `s_2=1`; the designated fleet02/B02 theorem gives `||p||inf<201`.

Pivoting `U1` in `S` subtracts its row/column outer product. On remaining coordinates `(U2,V1,V2)` the exact second Schur coefficient is

`T=[[1,0,1],
    [0,0,0],
    [1,0,1]]`,

so the literal `U2-V2` edge is `mu=1` and the new nested theorem gives `||p||inf<48.06291987045865...`.

Status: PASS for the displayed algebra and constants.
