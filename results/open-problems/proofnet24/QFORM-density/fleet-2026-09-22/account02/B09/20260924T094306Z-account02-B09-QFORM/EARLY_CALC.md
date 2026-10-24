# account02/B09 — early substantive calculation

Run: `20260924T094306Z-account02-B09-QFORM`
Programme: `QFORM-DENSITY-3EIG-20260922`

## First unpaid implication

`QFORM-SMALL-NONNEGATIVE-STAR-TO-PREPAIR-MIXEDFRAME-OR-CROSSING-v1`:
a global compiler cannot close the small definite/nonnegative physical-pair polynomial-star survivor merely by choosing the largest pair star, or even by summing the squared pair stars.  One must extract source-coordinate aggregate currency before pair selection (mixed frame, grouped crossing/volume, or a bounded physical core), while retaining arbitrary same-bank curvature.

## Dense target-valid family

Let `m=2^k>=8`.  Choose three distinct flat orthonormal Sylvester–Walsh characters `c,w1,w2 in R^m`; write

`c_i=tau_i/sqrt(m)`, `w1_i=sigma1_i/sqrt(m)`, `w2_i=sigma2_i/sqrt(m)` with signs in `{+1,-1}`.

Set

`L = w1 w1^T + 2 w2 w2^T`

and

`Q_m = 2 U <c,Y> + <w1,Y>^2 + 2 <w2,Y>^2`.

All variables `U,Y_1,...,Y_m` are the original independent physical coordinates, with arbitrary densities bounded by one.

Every physical same-bank coupling is nonzero:

`L_ij = (sigma1_i sigma1_j + 2 sigma2_i sigma2_j)/m in {+/-1/m,+/-3/m}`.

In the orthonormal coefficient basis `(U,c,w1,w2)`, the active operator is

`[[0,1],[1,0]] direct-sum [1] direct-sum [2]`,

so the nonzero spectrum is exactly `{-1,1,1,2}`.  Thus the family satisfies the owner's target with four eigenvalues of modulus at least one.

## Pinned mixed-frame receiver

For the pinned mixed Fresnel theorem, take the literal hub `H={U}`, two leaf Fresnel directions `w1,w2`, and coefficients `lambda_1=1`, `lambda_2=2`.  The mixed rows are

`rho_i=(c_i,w1_i,w2_i)`.

Their Gram is `Gamma=I_3`, and each physical leaf leverage is

`rho_i^T Gamma^{-1} rho_i = 3/m <= 3/8 < 1/2`.

Therefore the pinned theorem gives

`|phi_Qm(t)| <= 4 sqrt(2) pi^2 |t|^{-2}`.

Integrating `min(1,4 sqrt(2) pi^2 |t|^{-2})` gives

`||p_Qm||_infty <= 4*2^(1/4) = 4.756828460010884...`,

and hence `P{Q_m in I} <= 4*2^(1/4)|I|`.  The characteristic function is in `L^1`, so this branch has a continuous density.  No probability squaring occurs.

## Exact classification of definite physical pairs

Hub–leaf pairs have

`B_i=[[0,c_i],[c_i,3/m]]`, `det B_i=-1/m<0`,

so they are indefinite.

For a leaf pair `{i,j}`, put

`p=sigma1_i sigma1_j`, `q=sigma2_i sigma2_j`.

Then

`B_ij=[[3/m,(p+2q)/m],[(p+2q)/m,3/m]]`.

If `p=q`, the pair is singular positive semidefinite.  If `p=-q`, then `(p+2q)=q` and

`det B_ij=8/m^2>0`,

so the pair is positive definite.  Since `w1,w2` are independent Walsh characters, each of the four `(sigma1,sigma2)` sign classes has size `m/4`; hence there are exactly `m^2/4` unordered definite leaf pairs.

## Partner polynomial-star size on every definite pair

For a definite pair, use pivot `i`.  Then `a=3/m`, `c_pair=q/m`, and the latest account03/B09 polynomial star is

`H_ij = a v - c_pair u`,

where `u,v` are the pair arms to the remaining original coordinates (including the physical hub `U`).

The full leaf-row combination is exactly

`a L[j,*] - c_pair L[i,*] = (4q/(m sqrt(m)))(-sigma1_i w1 + sigma2_i w2)`.

Its full leaf norm squared is `32/m^3`.  Its coordinate `i` is zero and its coordinate `j` equals `det B_ij=8/m^2`; after deleting the active pair, the remaining leaf contribution is

`32/m^3 - 64/m^4 = 32(m-2)/m^4`.

The hub component is

`(H_ij)_U=(3 tau_j-q tau_i)/m^(3/2)`,

whose square is either `4/m^3` or `16/m^3`.  Therefore, for every definite physical pair,

`||H_ij||^2 in {(36m-64)/m^4,(48m-64)/m^4}`,

and in particular

`0 < ||H_ij|| < 4 sqrt(3) m^(-3/2)`.

The complete squared definite-pair star ledger satisfies

`sum_{definite {i,j}} ||H_ij||^2 <= (m^2/4)*(48/m^3)=12/m -> 0`.

Thus both the largest definite-pair star and the entire L2 pair-star ledger collapse, while the source-coordinate mixed-frame determinant remains `det Gamma=1`.

Applying the latest partner bound pairwise,

`||p_Q||_infty <= 2^(5/4) pi sqrt(3) ||H||^(-1/2)`,

the best certificate available from any definite pair must obey

`best_pair_RHS >= pi*6^(1/4) m^(3/4) = 4.916858219004906... m^(3/4)`.

For `m=64`, every definite-pair certificate is at least `111.255801...`, while the pinned mixed-frame theorem gives `4.756828461` for the actual law.

This is not a counterexample to the partner theorem and not a counterexample to QFORM.  It is a source-valid obstruction to pair-first forcing/L2 aggregation of the definite polynomial-star currency.
