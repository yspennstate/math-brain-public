# fleet03/B03 r48 checks

These are diagnostics for `REPORT.md`; the theorem itself is proved exactly there.

## A. Exact aligned-family calculation

For

`H=K=diag(1,0)`, `S=I_2`,

`M_car=[[H,I],[I,H]]`.

Because equal diagonal/off-diagonal block matrices split into the symmetric and antisymmetric subspaces, the spectrum is the union of the spectra of

`H+I=diag(2,1)` and `H-I=diag(0,-1)`.

Therefore

`spec(M_car)={2,1,0,-1}`,

its singular values are `{2,1,1,0}`, and

`E3(M_car)=(2*1*1)^2=4`.

For the exact balanced split all four carrier Grams equal `(1/2)I_2`, hence the cross core is `(1/2)M_car`. Therefore

`E3(B)=(1/2)^6 E3(M_car)=4/64=1/16`.

With

`C_E3=8.45302122552817687470491804598...`,

`C_E3*(1/16)^(-1/6)=13.418334785712947...`.

The whole-copy density-cap conversion gives

`4 sqrt(pi*13.418334785712947...)=25.970734910265183...`.

The designated partner control is

`8 sqrt(2pi)=20.053026197048002...`.

## B. Random deterministic sanity check of the exterior-power inequality

A fixed-seed numerical check generated random orthonormal `m x 2` and `n x 2` carrier frames, random symmetric `H,K`, random invertible `S`, and a fixed even/odd physical split. For each trial it formed the **literal** aligned physical cross block

`B=[[U0 H U1^T, U0 S V1^T],
    [V0 S^T U1^T, V0 K V1^T]]`

and compared

`lhs=E3(B)`

with

`rhs=g^6 E3(M_car)`,

where `g` is the minimum eigenvalue over the four restriction Grams.

Fixed seed: `12345`.

Accepted nonsingular trials: `901`.

Violations of `lhs>=rhs` beyond numerical tolerance: `0`.

Minimum observed ratio `lhs/rhs`: `3.599969052568097`.

The ratio is usually strictly above one because `g` uses only the smallest of the four Gram eigenvalues, while the exact exterior scaling keeps all four actual eigenvalues.

## C. Robust Weyl check

The robust statement in the report is deterministic:

if `B=B0+E`, `||E||op<=epsilon`, then Weyl gives

`s_j(B)>=s_j(B0)-epsilon`.

The exact aligned factorization and the balanced-Gram condition give

`s_j(B0)>=g s_j(M_car)`,

hence

`s_j(B)>= [g s_j(M_car)-epsilon]_+`, `j=1,2,3`.

Taking the top singular triple immediately yields

`E3(B)>=prod_(j=1)^3 [g s_j(M_car)-epsilon]_+^2`.

No probabilistic approximation is used in this check.

Terminal marker: `QFORM_B03_R48_BALANCED_CARRIER_E3_CHECK_PASS`.