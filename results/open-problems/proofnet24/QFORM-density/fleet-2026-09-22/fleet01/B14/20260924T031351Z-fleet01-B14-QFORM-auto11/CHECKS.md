# Checks — fleet01/B14 `20260924T031351Z-fleet01-B14-QFORM-auto11`

These are deterministic algebra/arithmetic checks for `REPORT.md`; they are not an independent review and are not numerical evidence for unrestricted QFORM.

## 1. Endpoint integral

For `B,C>0`, let `t0=(C/B)^(4/5)`. Then

`2[B t0 + int_(t0)^infinity C t^(-5/4)dt]
 =2[B(C/B)^(4/5)+4C(C/B)^(-1/5)]
 =10 C^(4/5)B^(1/5)`.

With `B=nm` and `C=pi sqrt(A M n m)`, division by `2pi` gives

`5 pi^(-1/5) A^(2/5)M^(2/5)(nm)^(3/5)`.

## 2. Uniform-[0,1] Fresnel bound

For `T>1`, `r=T^(-1/2)`. Integration by parts yields

`|int_r^1 exp(iTy^2)dy|
 <=1/(2T)+1/(2Tr)+(1/(2T))(1/r-1)
 =1/(Tr)=T^(-1/2)`.

The central interval contributes at most `r=T^(-1/2)`, hence

`|int_0^1 exp(iTy^2)dy|<=2T^(-1/2)`.

For `0<T<=1`, the trivial bound `<=1<=T^(-1/2)` is stronger. Negative `t` follows by conjugation.

## 3. Strict-target spectrum

For

`A_*=[[0,1,1,0],[1,0,0,0],[1,0,0,0],[0,0,0,1]]`,

the exact characteristic factors are the star block eigenvalues `sqrt(2),-sqrt(2),0` together with `1`, so

`spec(A_*)={-sqrt(2),0,1,sqrt(2)}`.

A direct finite check returned approximately

`[-1.41421356, 0, 1, 1.41421356]`.

Thus there are exactly three eigenvalues of modulus at least one.

## 4. Numerical constant

`5*pi^(-1/5)*2^(2/5)=5.24749493498713...`.

For reference,

`cos(1)=0.5403023058681398...`,
`zeta(3/2)=2.612375348685488...`.

## 5. Two-sided fragment divergence

With

`ell_j=j^(-3/2)/zeta(3/2)`,

one has

`ell_j^(3/5)=zeta(3/2)^(-3/5) j^(-9/10)`.

Because `9/10<1`,

`sum_j ell_j^(3/5)=infinity`.

For the slice pieces any valid half-order constant satisfies `A_j>=|I(1)|>=cos(1)>0`; for slope pieces the exact cap is `M_k=1`. Therefore the double positive endpoint sum diverges as the square of the preceding divergent series.

For `N` equal pieces on each side, each cell carries mass factor `(N^-1 N^-1)^(3/5)=N^-6/5`; there are `N^2` cells, so the fragment-first coefficient grows as `N^(4/5)`, while coherent reassembly leaves the aggregate constant unchanged.

## 6. Scope checks

- No post-rotation independence is used.
- No pointwise law-uniform quadratic Fourier decay is used.
- The coherent theorem assumes only the aggregate slice certificate and aggregate slope cap; it imposes no piecewise `A_j` or `M_k` bounds.
- The divergence is a proof-interface statement, not a counterexample to the target.
