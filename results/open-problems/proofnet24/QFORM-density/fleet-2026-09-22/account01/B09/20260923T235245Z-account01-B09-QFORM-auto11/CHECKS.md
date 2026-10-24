# Deterministic checks — B09 overlap-1/2 Schur-numerator compiler

Run `20260923T235245Z-account01-B09-QFORM-auto11`.

These checks are finite regression checks only; the report contains the exact algebraic proofs.

## Check 1: overlap-two pair identity

For five independently generated random symmetric `8 x 8` matrices and multiple physical pairs `H`, compute directly

`sum_(i!=j) det A[H union {i},H union {j}]^2`

and compare with

`||offdiag(det(B)D-U adj(B) U^T)||_F^2`.

Agreement was at floating error (typical discrepancy below `1e-13`). A separate global check on random sizes `n=5,7` verified

`Omega_2(A)=sum_H ||offdiag N_H||_F^2`

with errors `1.1e-14` and `1.1e-13`, respectively.

## Check 2: overlap-one scalar identity

For five random symmetric `8 x 8` matrices with nonzero physical pivot `a=A_hh`, compute directly

`Omega_(1,h)=sum_(I cap J=empty, |I|=|J|=2) det A[{h} union I,{h} union J]^2`.

Compare with

`a^2 sum_(I cap J=empty) det S_h[I,J]^2`,

where `S_h=D-vv^T/a`. Observed pairs `(direct, Schur)` were equal to floating error; representative values included

`240.46791014531965`,
`55.608677197086074`,
`633.751296866206`,
`78.6918064645684`,
`374.0669672853684`.

Largest observed absolute discrepancy in this batch was below `6e-13`.

## Check 3: designated partner regression

For `m=8`, take the physical pair core `diag(8,0)`, zero leaf block, and kernel-star couplings `q_i=2/sqrt(8)` for all eight leaves.

The full symmetric matrix has eigenvalues

`{-2, 0,0,0,0,0,0,0, 2, 8}`.

Thus it has three eigenvalues of modulus at least one. The exact overlap-two currency is

`Omega_(2,H)=8^2[(sum q_i^2)^2-sum q_i^4]=896`.

The designated account02/B09 receiver gives

`6*8^(-1/3)*2^(-2/3)=1.8898815748423097`.

## Check 4: constant in the invertible-indefinite overlap-two corollary

Combining the literal-cut lower bound

`||C0||_F >= omega^(1/2)/(2|det B|)`

with the completed constant `11.463` gives

`11.463*2^(1/10)=12.285739201053527 <12.286`.

The powers simplify as

`|det B|^(-2/5) * (2|det B|/sqrt(omega))^(1/10)
 =2^(1/10)|det B|^(-3/10) omega^(-1/20)`.
