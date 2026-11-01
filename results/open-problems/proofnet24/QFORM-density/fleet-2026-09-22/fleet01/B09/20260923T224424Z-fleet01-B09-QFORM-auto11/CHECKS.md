# Deterministic regression checks

Run: `20260923T224424Z-fleet01-B09-QFORM-auto11`.

These checks are diagnostic only and are not substitutes for the symbolic proof in `REPORT.md`.

## Constants

Using direct high-precision evaluation:

- `C3 = 3*2^(4/3)*e^(1/3) = 10.550168831164775`.
- `2*C3*(1/4)^(-1/6) = 26.58475958065858`.
- `c_* = 1-sqrt(3)/2 = 0.1339745962155614`.
- `216*c_*^(-1/3) = 422.1300464529374`.
- `C_KD = 5*6^(3/5)/2^(11/10) = 6.834830666196632`.
- `C_KD*8^(-1/5) = 4.509306566419814`.

## Partner example

For

`A_*=[[0,0,2,1,0],
      [0,0,0,0,2],
      [2,0,0,0,0],
      [1,0,0,0,0],
      [0,2,0,0,0]]`,

exact symbolic calculation gives

`charpoly(A_*) = lambda*(lambda-2)*(lambda+2)*(lambda^2-5)`.

For `L={1,2,3}`, `R={4,5}`,

`C=[[1,0],[0,2],[0,0]]`,
`w=c1 x c2=(0,0,2)`,
`Pw=(4,0,0)`,

hence `||w||*||Pw||=8` exactly.

## Third-compound identity regression

A fixed-seed (`260923`) random real symmetric `6x6` matrix was used. Enumerating all physical triples and constructing the compound matrix `C3[S,T]=det A[S,T]` gave:

`Omega_0 = 1.3226823206618095`
`Omega_1 = 56.0525680516826`
`Omega_2 = 119.73108189552161`
`Omega_3 = 53.8172214133936`

and

`||C3-diag(C3)||_F^2 = 177.10633226786607`,
`Omega_0+Omega_1+Omega_2 = 177.10633226786604`.

Also

`||C3||_op = 8.34118030108643`,
`s1(A)s2(A)s3(A) = 8.341180301086426`.

The displayed differences are floating-point roundoff. The exact proof is the standard exterior-power/Cauchy-Binet identity.
