# fleet03/B06 r36 finite algebra checks

These are sanity checks only. The exact determinant and pseudodeterminant identities are proved symbolically in `REPORT.md`.

## 1. Same-bank discriminant determinant

For 1,000 pseudorandom parameter tuples `(beta,k,theta,zeta,delta_0)`, with

`Delta=delta_0+beta theta^2`,
`w=(k+beta theta zeta,beta theta)`,
`q=(zeta,1)`,

we compared

`det(w w^T-Delta beta q q^T)`

against

`-beta k^2 Delta`.

Maximum relative discrepancy, normalized by `max(1,|rhs|)`: `2.2093438190040615e-14`.

## 2. Transverse pseudodeterminant

For 1,000 pseudorandom physical coefficient triples, we formed

`c=(k+beta theta zeta)u+beta theta v`,
`d=zeta u+v`,

orthogonalized a nonzero `w` against `span{c,d}`, and set

`S=[[2a,b,1],[b,beta,0],[1,0,0]]`,
`B=[c d w] S [c d w]^T`.

The product of the three nonzero eigenvalues of `B` was compared with

`-beta k^2 det Gram(u,v) ||w||^2`.

Maximum relative discrepancy, normalized by `max(1,|rhs|)`: `5.245026910699538e-13`.

## 3. Explicit collar constants

For `c>63/64`, `|Delta|>=1/64`, `k^2>=1`, the in-range rank-two half-Riesz payment evaluates to

`16 sqrt(30) sqrt(64/63) 64^(1/4)
 =249.83041867482453 <249.831`.

On the opposite-sign branch, the fleet04/B18 square splice evaluates to

`2 sqrt(2 pi) sqrt(64/63) 64^(1/4)
 =14.291724494734481 <14.292`.

No Monte Carlo histogram or numerical density estimate is used anywhere in the proof.
