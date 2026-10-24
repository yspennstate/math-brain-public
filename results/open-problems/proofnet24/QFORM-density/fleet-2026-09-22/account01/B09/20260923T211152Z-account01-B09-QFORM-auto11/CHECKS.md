# Deterministic checks — grouped rank-two kernel-derivative receiver

Run: `20260923T211152Z-account01-B09-QFORM-auto11`.

These checks are arithmetic/algebra regressions only; the proof is analytic.

## Constants

With

`C_KD=5*6^(3/5)/2^(11/10)=6.834830666196632...`,

and the arbitrary-right-bank projection cost `sqrt(2)` entering before the `4/5` tail optimization,

`C_G=2^(2/5) C_KD=5*6^(3/5)/2^(7/10)=9.018613132839628...`.

## Compound/adjugate identity

Fixed seed `20260923`: generated a random `3x9` rank-two matrix `C=U diag(1.7,0.6) V^T` with orthonormal two-frames `U,V`, and a random symmetric `3x3` matrix `P`.

For `G=CC^T`, the positive eigenvalues were

`0.36, 2.89`,

so

`e2(G)=1.0404000000000004`, `Delta=sqrt(e2)=1.0200000000000002`.

Directly summing over all physical column pairs gave

`max_abs( sum_{r<s}(c_r x c_s)(c_r x c_s)^T - adj(G) ) = 2.7755575615628914e-16`.

The aggregate kernel-derivative volume was

`V_L=sum_{r<s} ||P(c_r x c_s)||^2 = 1.7758980405534521`,

while the rank-two formula gave

`e2(G)||Pn||^2 = 1.7758980405534548`,

absolute discrepancy `2.6645352591003757e-15`.

## Exact spread-family regression

For even `m`, take

`P=[[0,0,1],[0,0,0],[1,0,0]]`,

and a `3xm` cross matrix whose first `m/2` columns are `sqrt(2/m)e1` and last `m/2` columns are `sqrt(2/m)e2`.

At `m=8`, direct calculation gives

`CC^T=diag(1,1,0)`, `e2(CC^T)=1`, and

`V_L=sum_{r<s} ||P(c_r x c_s)||^2=1`.

The active five-dimensional coefficient matrix is

`[[0,0,1,1,0],
  [0,0,0,0,1],
  [1,0,0,0,0],
  [1,0,0,0,0],
  [0,1,0,0,0]]`,

whose eigenvalues numerically are

`{-sqrt(2),-1,0,1,sqrt(2)}`

(up to `1.12e-16` numerical error at zero), so the family has four eigenvalues of modulus at least one.

For one physical cross pair from opposite halves, the completed account02/B09 packet theorem gives

`C_KD (4/m^2)^(-1/5)`.

At `m=8` this is `11.900131372982203...`.

The new grouped theorem instead uses all pairs before reciprocal payment and gives

`C_G [e2(G)V_L]^(-1/10)=C_G=9.018613132839628...`,

uniformly for every even `m`.
