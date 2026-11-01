# EARLY CHECKPOINT — fleet02/B07 r13

Status: substantive partial calculation; full QFORM remains open.

## First unpaid implication attacked

`QFORM-ANCHOR-H3-CURVATURE-COMPATIBLE-UPGRADE-v1`: after an actual physical anchor pair is completed, obtain a density receiver that uses only determinant/volume currency that survives the Schur correction. Do not reuse the pre-completion E2 bank, which fleet02/B07 r11 showed can collapse exactly.

## New calculation: arbitrary positive small-ball exponent smooths the indefinite pair logarithm

Use the proved physical-pair envelope from
`math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
For an invertible indefinite physical pair B, write
`Delta=|det B|`, `kappa=sigma_min(B)`. After completing the pair,

`Q=((U,V)+m(Z))^T B ((U,V)+m(Z))+R(Z)`

with U,V the original independent cap-one coordinates. For every r>0,

`p_Q(t) <= 2 sqrt(2)/r + Delta^(-1/2) E log_+(2 r^2/(kappa |t-R|)).`

If for some `0<alpha<1`

`sup_t P(|R-t|<rho) <= H rho^alpha` for all rho>0,

then layer cake gives, for `a>0`,

`E log_+(a/|t-R|) <= H a^alpha/alpha`.

Optimizing in r yields

`||p_Q||inf <= K_alpha H^(1/(2alpha+1)) Delta^(-1/(2(2alpha+1))) kappa^(-alpha/(2alpha+1))`,

where

`K_alpha = 2 sqrt(2) (2alpha+1)/(2alpha) * 2^((alpha-1/2)/(2alpha+1)).`

This recovers the published alpha=1/2 pair-log bound exactly. At `alpha=1/8`,

`K_(1/8)=10*2^(1/5)`.

## Apply the required e5 source to the Schur remainder

From
`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, Extension D_k with k=1 and q=2 is valid with no marginal obstruction, and Lemma 4.1 converts its `|t|^(-1/4)` decay to fractional potentials.

Let I,J be disjoint ORIGINAL-coordinate banks in the completed-pair remainder and put

`M=S[I,J]`, `L=||M||_F`, `Z_1=L^2`.

The k=1,q=2 calculation gives

`|phi_R(t)| <= (pi sqrt(2e))^(1/4) L^(-1/4) |t|^(-1/4)`

(up to min with 1), hence at alpha=1/8

`H_(1/8)(R) <= C_1 L^(-1/8)`,

`C_1=32 c_(1/8) (pi sqrt(2e))^(1/8)=2.777316075398203...`,

with `c_alpha=2^(1-alpha)Gamma((1-alpha)/2)/(2sqrt(pi)Gamma(alpha/2))`.

Substitution in the generalized pair-log estimate gives the curvature-safe full-form receiver

`boxed: ||p_Q||inf <= C_* Delta^(-2/5) kappa^(-1/10) L^(-1/10),`

`C_*=10*2^(1/5)*C_1^(4/5)=26.00795741955...`.

All same-bank curvature, affine terms, outside couplings and additional spectrum remain in R. No rotation of the product law and no reciprocal individual minor is used.

## Rank-two Schur-loss alternative

Before pair completion, write the far physical cross block as D. Pair completion changes it by a matrix of rank at most two:

`M=D-C_I B^(-1) C_J^T`.

Therefore, with singular values `s_1(D)>=s_2(D)>=...` and

`T_2(D)=sum_(j>=3) s_j(D)^2`,

Eckart-Young gives

`L=||M||_F >= dist_F(D,rank<=2)=sqrt(T_2(D))`.

Consequently

`boxed: ||p_Q||inf <= 26.007958 Delta^(-2/5) kappa^(-1/10) T_2(D)^(-1/20)`

whenever B is invertible indefinite and `T_2(D)>0`.

If `R0=max(||B||op,||D||F)`, then `kappa>=Delta/R0`. Thus if

`Delta>=delta R0^2` and `T_2(D)>=epsilon R0^2`,

`boxed: ||p_Q||inf <= 26.007958 delta^(-1/2) epsilon^(-1/20) R0^(-1).`

For a definite B the ellipse bound already gives `pi delta^(-1/2)R0^(-1)`. Hence a non-near-singular physical pair can fail this new receiver only when the far cross block lies in a quantitative rank-two tube.

## Partner r30 interface

Latest completed designated partner used here:
`math-open-problems@466a8413b3d1ec6ce723633be0fe14eafaa7175d:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T090613Z-fleet03-B07-qform-r30/REPORT.md`.
On its edge-E2 branch,

`|b| sqrt(E2(D)) >= sqrt(G)/2`, `G>gamma F^6`, `gamma=113246208^(-2)`, and `|b|<=F`,

so

`E2(D) > (gamma/4) F^4`.

If `T_2(D)<=epsilon F^2`, then

`E2(D)-s_1(D)^2 s_2(D)^2 <= ||D||F^2 T_2(D) <= epsilon F^4`,

hence

`s_1(D)s_2(D) > sqrt(gamma/4-epsilon) F^2`.

At `epsilon=gamma/8`, the low-tail survivor is therefore a genuine strong rank-two tube:

`boxed: s_1(D)s_2(D)>sqrt(gamma/8) F^2.`

So the r30 edge branch is reduced to: a paid non-near-singular/high-tail pair state, or a near-singular anchor pair, or a quantitatively strong rank-two far core. The exact r11 Schur-collapse family sits in the intended low-tail class (`rank D=2`), so it is not incorrectly excluded.

Next: finish constants/checks, verify no later partner/correction supersedes r30, and publish the full proof plus the sharpened remaining implication.
