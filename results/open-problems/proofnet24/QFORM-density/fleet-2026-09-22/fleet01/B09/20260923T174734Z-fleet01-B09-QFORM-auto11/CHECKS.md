# Deterministic checks — fleet01/B09 `QFORM-FIXEDPAIR-AGGREGATE-FOURVOLUME-v1`

These checks support arithmetic and exact identities only; the proof is in `REPORT.md`.

## 1. Exact constants

With

`c0=16/729`, `a0=c0/2=8/729`,
`c1=256/3125`, `a1=c1/2=128/3125`,

the three normalized branch constants are

`C_A=4 exp(1/4)c0^(-1/8)=8.278650626819047`,

`C_B=2^(7/4)c1^(-1/8)a0^(-1/8)=8.083202188513717`,

`C_C=2 sqrt(2)(a0 a1)^(-1/8)=7.412329088907925`.

Thus `C_A` is the maximum and `8.279` is safe.

Symbolically,

`C_A=2 sqrt(2) exp(1/4) 3^(3/4)`,

`C_B=2^(3/8)3^(3/4)5^(5/8)`,

`C_C=2^(1/4)3^(3/4)5^(5/8)`.

## 2. Numerical Gram-Schur / Cauchy-Binet identity check

A fixed-seed symmetric `10 x 10` real matrix was used with hubs `H={0,1}`, row bank `I={2,3,4}`, and column bank `J={5,6,7,8,9}`. Direct evaluation gave

`Delta * e2(CC^T) = 43.722817408144195`,

while direct summation of all squared physical `4 x 4` minors

`sum_{S subset I, |S|=2} sum_{T subset J, |T|=4} det A[H union S,T]^2`

gave exactly the same floating-point value

`43.722817408144195`,

with computed difference `0.0` at machine precision.

This is only a regression check; the exact proof is equations (3.4)-(3.5) in `REPORT.md`.

## 3. Walsh target-family check at m=8

Using a Sylvester-Hadamard matrix of order `8`, choose flat orthonormal rows `c1,c2,q1,q2` on `T` and `u1,u2` on disjoint `S`. For

`Q=2Xa<c1,XT>+2Xb<c2,XT>+2<u1,XS><q1,XT>+2<u2,XS><q2,XT>`,

the cross block from `(a,b,S)` to `T` has exactly four singular values equal to one, so the symmetric coefficient matrix has nonzero spectrum

`(+1,+1,+1,+1,-1,-1,-1,-1)`.

The anchored-four-volume sub-sum using row pairs entirely in `S` and columns entirely in `T` equals exactly `1` by Cauchy--Binet. Direct full enumeration at `m=8` gave total fixed-pair `U_H=3.8125`, decomposed by row-pair type as

`SS: 1.0000000000`,
`ST: 2.2500000000`,
`TT: 0.5625000000`.

Only the rigorous lower bound `U_H>=1` is used in the theorem application.

For the designated fleet02/B09 mixed-frame theorem, the six frame columns are orthonormal, so `G=I_6`; row leverages are `2/m` on `S` and `4/m` on `T`. At `m=8`, the maximum is exactly `1/2`. The theorem therefore gives

`C_4=4*(8/6)*2^(-1/2)=8 sqrt(2)/3=3.771236166328254`.

## 4. Scaling check

Under `A -> sA`, every physical `4 x 4` determinant scales by `s^4`; therefore `U_H -> |s|^8 U_H` and `U_H^(-1/8) -> |s|^(-1) U_H^(-1/8)`, exactly the output-density scaling.
