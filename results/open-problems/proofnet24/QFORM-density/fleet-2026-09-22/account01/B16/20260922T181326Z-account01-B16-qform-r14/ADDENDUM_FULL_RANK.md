# Addendum — the conditional-moment obstruction persists for a genuinely full-rank form

The report's conditional-moment counterexample can be made literally full rank, so the failure is not an artifact of conditioning on zero-eigenvalue directions.

Retain the product cube and orthogonal decomposition `R^n=E direct_sum F` from the report, where

`E=span{e0,u1,u2}`

and the exact conditional moment satisfies

`E_Z ||rho_{E|Z}||_infinity^(2/3)
 = [m^(-1/3) Gamma(m+1)Gamma(4/3)/Gamma(m+1/3)]^2
 ~ Gamma(4/3)^2 m^(2/3)`.

For any `0<epsilon<1`, define

`A_epsilon = e0 e0^T + u1 u1^T - u2 u2^T + epsilon P_F`.

Then `A_epsilon` is full rank. Its spectrum is

`{1,1,-1}` together with `epsilon` of multiplicity `dim F=2m-2`,

so it has exactly three eigenvalues of modulus at least one. If `Z=P_F X`, then

`X^T A_epsilon X
 = Y_0^2+Y_1^2-Y_2^2 + epsilon ||Z||^2`.

Conditioning on the remaining `n-3` spectral coordinates is precisely conditioning on `Z` (up to an orthogonal change of coordinates inside the degenerate `epsilon` eigenspace). The conditional law of the rank-three variable `Y=P_E X` is unchanged, and the extra term `epsilon||Z||^2` is merely a conditional translation of the target level. Therefore any proposed full-rank proof whose universal step is

`E_Z ||rho_{E|Z}||_infinity^(2/3) <= C`

still fails on this genuinely full-rank target family, with the same exact divergence `~Gamma(4/3)^2 m^(2/3)`.

This refutes only that conditional-sup-moment interface, not the QFORM conjecture. A successful proof must retain product aggregation more finely than conditioning on the entire complementary spectral vector.
