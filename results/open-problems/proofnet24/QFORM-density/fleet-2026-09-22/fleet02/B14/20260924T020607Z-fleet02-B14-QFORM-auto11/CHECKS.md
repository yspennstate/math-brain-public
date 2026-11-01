# Checks — fleet02/B14 `20260924T020607Z-fleet02-B14-QFORM-auto11`

These are deterministic algebra/arithmetic checks for `REPORT.md`, not numerical evidence for the unrestricted conjecture.

## 1. Subprobability integral

For `m,C>0`, with threshold `t0=(C/m)^(4/5)`,

`int_R min(m,C|t|^(-5/4))dt`
`=2[m t0 + C int_(t0)^infinity t^(-5/4)dt]`
`=2[m t0+4C t0^(-1/4)]`
`=10 C^(4/5)m^(1/5)`.

Putting `C=pi sqrt(A m L)` and dividing by `2pi` gives

`5 pi^(-1/5) A^(2/5)m^(3/5)L^(2/5)`.

If `L=M0 m`, the mass exponent is `3/5+2/5=1`, giving exact mixture homogeneity.

## 2. Comb family spectrum

For

`A=[[0,1,1,0],[1,0,0,0],[1,0,0,0],[0,0,0,1]]`,

the vector `(0,1,-1,0)` is null. On the span of `e_X` and `(e_L+e_Z)/sqrt(2)`, the block is `[[0,sqrt(2)],[sqrt(2),0]]`, so the remaining two star eigenvalues are `+sqrt(2),-sqrt(2)`. The `Y` direction has eigenvalue `1`. Therefore

`spec(A)={sqrt(2),-sqrt(2),1,0}`.

## 3. Uniform-square slice constant

For `T=|t|>16`, set `a=T^(-1/2)`. The central interval has length `2a`. On `[a,1/2]`, integration by parts gives

`int_a^(1/2)e^(iTy^2)dy`
`=[e^(iTy^2)/(2iTy)]_a^(1/2) + int_a^(1/2)e^(iTy^2)/(2iTy^2)dy`.

The boundary terms are at most `1/T+1/(2sqrt(T))`; the last integral is at most

`(1/(2T))(1/a-2)=1/(2sqrt(T))-1/T`.

Hence each tail is at most `1/sqrt(T)`, both tails at most `2/sqrt(T)`, and the central interval at most `2/sqrt(T)`. Thus

`|int_(-1/2)^(1/2)e^(ity^2)dy|<=4|t|^(-1/2)`.

For `0<|t|<=16`, the trivial bound one is at most `4|t|^(-1/2)`.

## 4. Constants

- `C_* = 5 pi^(-1/5) 4^(2/5) = 6.924111078456212...`.
- `6 sqrt(pi) = 10.634723105433096...`.
- `12 sqrt(pi) = 21.269446210866192...`.

For `N` equal teeth, `m_j=1/N`, `L_j=1`, so the separate-piece compiler is exactly `C_* N^(2/5)`.

For an equal-coefficient `m`-coordinate slope and a `k`-coordinate anchor, `||a_H||=sqrt(k/m)`, hence the anchor bound deteriorates by `(m/k)^(1/5)`.
