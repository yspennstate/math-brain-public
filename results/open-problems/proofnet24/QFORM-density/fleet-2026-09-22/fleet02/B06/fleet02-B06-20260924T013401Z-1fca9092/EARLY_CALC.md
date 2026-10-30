# fleet02/B06 early calculation — singular shear-flat rank-one branch

Programme `QFORM-DENSITY-3EIG-20260922`.  Full conjecture remains OPEN.

Consider a literal invertible indefinite physical pair `H` in an ambient symmetric matrix `A` with at least three eigenvalues of modulus at least one.  Let the exact Schur residual on untouched original product coordinates be

`S = D + lambda w w^T`,

with `D` diagonal.  The completed Schur-complement spectral lemma in the pinned `e5f71d79...` RESULTS packet gives at least one eigenvalue of `S` of modulus at least one, hence `||S||op >= 1`.

Put `a_j=S_jj` and `R=S-diag(a_j)`.  If some `|a_j|>=1/2`, then after conditioning all other original coordinates the residual is a scalar quadratic with leading coefficient `a_j`.  Uniformly in the translated centre and target,

`P(|Y^T S Y-t|<rho) <= 2 sqrt(2 rho/|a_j|) <= 4 sqrt(rho)`.

Otherwise `||diag(a_j)||op<1/2`, so `||R||op>1/2` and therefore `||R||F>1/2`.  Since `R_ij=lambda w_i w_j` for `i!=j`, a Bernoulli random cut `I|J` obeys

`E ||R[I,J]||F^2 = ||R||F^2/4`.

Hence one literal original-coordinate cut has a rank-one cross block

`B=lambda w_I w_J^T`

with its unique singular value

`s=|lambda| ||w_I||_2 ||w_J||_2 = ||R[I,J]||F > 1/4`.

The checked grouped-projection theorem `NEW_PROJECTED_CROSSING.md`, rank `r=1`, retains arbitrary internal functions on both product banks.  With scalar projection-density caps at most `sqrt(2)`, it gives

`|phi_R(t)| <= min(1, sqrt(2 pi) s^(-1/2) |t|^(-1/2))`.

A direct triangular-kernel calculation then gives, for every `rho>0`,

`sup_t P(|Y^T S Y-t|<=rho)
 <= (32/(3 pi)) sqrt(2 pi) s^(-1/2) sqrt(rho)
 <= [64 sqrt(2 pi)/(3 pi)] sqrt(rho).`

Indeed `1_{|x|<=rho} <= 2(1-|x|/(2rho))_+`; the Fourier transform of the triangular majorant is `2rho (sin(rho t)/(rho t))^2`, and integrating the bound `K|t|^(-1/2)` on `(0,1/rho)` and the additional `(rho t)^(-2)` tail gives `(32/(3pi))K sqrt(rho)`.

Therefore the pinned physical-pair logarithmic receiver applies in both cases.  In the off-diagonal branch it yields

`||p_Q||infinity
 <= 4 sqrt( 128 sqrt(2 pi)/(3 pi) )
    ( |det H| sigma_min(H) )^(-1/4)
 < 23.339 ( |det H| sigma_min(H) )^(-1/4).`

In the diagonal branch the constant is only `8 sqrt(2)` in front of the same pair currency.

This pays the shared-coordinate diagonal-plus-rank-one Schur residual analytically without a `D_hh` pivot, without deleting any diagonal term, without post-rotation independence, and without a curved-fiber supremum.  It directly targets the singular-`T` shear-flat endpoint of partner fleet03/B06 r48.  Remaining work in this run: audit constants/scopes against the pinned source and current corrections, apply the statement to the exact r48 normal form, and stress-test whether the spectral Schur step is being used at its proved threshold.
