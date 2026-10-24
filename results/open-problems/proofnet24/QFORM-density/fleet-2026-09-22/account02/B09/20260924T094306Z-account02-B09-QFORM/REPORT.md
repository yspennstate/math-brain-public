# account02/B09 — definite-star ledger collapse versus a fixed mixed frame

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-24T09:43:06Z.

attacking: the tiny definite-pair polynomial-star survivor by showing that even its full L2 pair ledger can collapse while a literal source-coordinate mixed-hub frame remains universal.

## Outcome

`ESSENTIAL_STEP_APPLIED`; the unrestricted QFORM target remains OPEN.

The first unpaid implication is

`QFORM-SMALL-NONNEGATIVE-STAR-TO-PREPAIR-MIXEDFRAME-OR-CROSSING-v1`:

> After the already-paid macroscopic physical-pair branches, a global structural compiler cannot close the small definite/nonnegative polynomial-star survivor merely by selecting a largest physical pair, or even by summing the squared polynomial-star resources over all definite pairs.  It must extract a source-coordinate aggregate resource *before pair selection*: a diffuse mixed Fresnel frame, a grouped crossing/volume receiver, or a genuinely bounded physical core, while retaining arbitrary same-bank quadratic curvature.

This run gives an explicit target-valid family proving that this pre-pair aggregation is structurally necessary.  In the family, every physical same-bank coupling is nonzero, the target spectrum is exactly `{-1,1,1,2}`, every definite physical pair has polynomial star `O(m^{-3/2})`, and the entire squared definite-pair star ledger is `O(m^{-1}) -> 0`; nevertheless the pinned source-coordinate mixed-frame theorem gives the uniform density constant `4*2^(1/4)<4.757`.

## 1. Source-valid dense construction

Let `m=2^k>=8`.  Choose three distinct flat orthonormal Sylvester–Walsh characters

`c,w1,w2 in R^m`,

and write

`c_i=tau_i/sqrt(m)`, `w1_i=sigma1_i/sqrt(m)`, `w2_i=sigma2_i/sqrt(m)`,

with signs `tau_i,sigma1_i,sigma2_i in {+1,-1}`.

Define the physical leaf block

`L = w1 w1^T + 2 w2 w2^T`

and the literal source-coordinate quadratic form

`Q_m = 2 U <c,Y> + <w1,Y>^2 + 2 <w2,Y>^2`,

where `U,Y_1,...,Y_m` are arbitrary independent real random variables with densities at most one.  No moments, bounded support, log-concavity, or post-rotation independence are used.

The same-bank block is physically dense: for every `i,j`,

`L_ij=(sigma1_i sigma1_j+2 sigma2_i sigma2_j)/m`,

which lies in `{+/-1/m,+/-3/m}` and is never zero.  Thus this is not a sparse-leaf escape.

The matrix is

`A_m=[[0,c^T],[c,L]]`.

In the deterministic orthonormal coefficient basis `(U,c,w1,w2)`, its active part is

`[[0,1],[1,0]] direct-sum [1] direct-sum [2]`.

Hence

`spec_nonzero(A_m)={-1,1,1,2}`.

So every member of the family satisfies the owner's exact target, in fact with four eigenvalues of modulus at least one.

## 2. Required pinned result: mixed-hub smoothing pays the law at linear small-ball scale

Apply the completed mixed Fresnel theorem from the required pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` with one literal physical hub `H={U}` and two physical-leaf Fresnel directions `w1,w2`, with coefficients

`lambda_1=1`, `lambda_2=2`.

The source-coordinate mixed rows are

`rho_i=(c_i,w1_i,w2_i) in R^3`.

Orthogonality gives the exact Gram identity

`Gamma=sum_i rho_i rho_i^T=I_3`,

and every *physical* leaf leverage is

`rho_i^T Gamma^{-1} rho_i=3/m<=3/8<1/2`.

The pinned theorem therefore gives, while retaining the whole dense same-side matrix `L` in the original coordinates,

`|phi_Qm(t)| <= (4pi)^2 2^{-1} (1*2)^(-1/2) |t|^{-2}`

or equivalently

`|phi_Qm(t)| <= 4 sqrt(2) pi^2 |t|^{-2}`.

There is no probability squaring and no square-root small-ball loss.  Integrating the exact envelope `min(1,K|t|^{-2})` with `K=4 sqrt(2) pi^2` gives

`||p_Qm||_infty <= (2/pi) sqrt(K)=4*2^(1/4)`

and hence

`||p_Qm||_infty <= 4.756828460010884...`,

`P{Q_m in I} <= 4*2^(1/4)|I|`

for every interval `I`.  Since the characteristic function is in `L^1`, this branch has a continuous density.  This is an actual full-law use of the completed pinned result, not merely a structural analogy.

## 3. Exact physical-pair classification

The only physical coordinates are the literal hub `U` and the leaves `Y_i`.

A hub–leaf pair `{U,Y_i}` has

`B_i=[[0,c_i],[c_i,3/m]]`,

so

`det B_i=-c_i^2=-1/m<0`.

Thus every hub–leaf pair is indefinite, not in the latest partner's definite-pair chamber.

For a leaf–leaf pair `{Y_i,Y_j}`, put

`p=sigma1_i sigma1_j`, `q=sigma2_i sigma2_j`.

Then

`B_ij=[[3/m,(p+2q)/m],[(p+2q)/m,3/m]]`.

If `p=q`, then `|p+2q|=3` and `det B_ij=0`; the pair is singular positive semidefinite.  If `p=-q`, then `p+2q=q`, so

`det B_ij=(9-1)/m^2=8/m^2>0`;

the pair is positive definite.

Because `w1,w2` are independent Walsh characters, the four sign classes `(sigma1_i,sigma2_i)` each contain exactly `m/4` coordinates.  Definite pairs are exactly pairs whose two sign classes differ in one of the two signs.  There are four edges in that sign square, hence exactly

`N_def=4(m/4)^2=m^2/4`

unordered definite physical pairs.

## 4. Latest partner applied: every definite polynomial star is tiny

The latest compatible completed designated-partner result observed in this run is account03/B09 `20260924T091232Z-account03-B09-QFORM-r47`, theorem `QFORM-DEFINITEPAIR-POLYNOMIAL-STAR-UNIFORM-v1`.  For a definite physical pair

`B=[[a,c_pair],[c_pair,b]]`

with original-coordinate arms `u,v`, it uses the polynomial star

`H=a v-c_pair u`

and proves

`||p_Q||_infty <= 2^(5/4) pi sqrt(3) ||H||_2^(-1/2)`

with arbitrary remaining quadratic curvature.  Its numerical coefficient is

`2^(5/4) pi sqrt(3)=12.941898654808462...`.

Apply it to any definite leaf pair in `Q_m`.  Use `i` as pivot.  Since the pair is definite, `p=-q`, and

`a=3/m`, `c_pair=q/m`.

Let `u,v` denote the arms from `Y_i,Y_j` to all remaining original coordinates, including the hub `U`.

For the leaf components, the complete row combination before deleting the pair is exactly

`a L[j,*]-c_pair L[i,*]`

`= (4q/(m sqrt(m)))(-sigma1_i w1+sigma2_i w2)`.

The two Walsh directions are orthonormal, so this full leaf vector has squared norm

`32/m^3`.

Its coordinate `i` is zero.  Its coordinate `j` is

`a L_jj-c_pair L_ij=det B_ij=8/m^2`.

After deleting the two active pair coordinates, the remaining leaf contribution therefore has squared norm

`32/m^3-64/m^4=32(m-2)/m^4`.

The hub component of the polynomial star is

`(H_ij)_U=(3 tau_j-q tau_i)/m^(3/2)`,

whose square is either `4/m^3` or `16/m^3`.  Consequently the *exact* definite-pair star size is

`||H_ij||^2 in {(36m-64)/m^4,(48m-64)/m^4}`.

In particular, every definite physical pair obeys

`0<||H_ij||<4 sqrt(3) m^(-3/2)`.

The partner theorem is therefore valid and applicable to every definite pair, but the scale of the resulting certificate necessarily deteriorates with `m`.

Indeed, even choosing the best definite pair gives

`best_pair_RHS >= 12.9418986548 * (4 sqrt(3) m^(-3/2))^(-1/2)`

`= pi*6^(1/4) m^(3/4)`

`=4.916858219004906... m^(3/4)`.

For the concrete target-valid member `m=64`,

`max_def ||H_ij|| <= 0.0135316469341...`,

so every partner definite-pair certificate is at least

`111.255801...`,

whereas the pinned source-coordinate mixed-frame estimate for the very same full law is

`||p_Q64||_infty <= 4.756828461`.

This is a real inequality comparison.  It neither contradicts nor weakens the partner theorem; it shows why a compiler cannot expect the spectral hypothesis to force a universal definite-pair polynomial-star scale.

## 5. Stronger obstruction: even the full squared definite-star ledger vanishes

The preceding point could in principle be repaired by summing resources over many tiny definite pairs.  This family rules out the simplest such L2 repair as well.

There are exactly `m^2/4` definite pairs, and for every one

`||H_ij||^2 < 48/m^3`.

Therefore

`sum_{definite {i,j}} ||H_ij||^2`

`<= (m^2/4)(48/m^3)`

`=12/m -> 0`.

At the same time, the pre-pair mixed-frame currency remains exactly

`Gamma=I_3`, `det Gamma=1`,

and all physical leverages are `3/m`.

This proves the new obstruction/result

`QFORM-DEFINITE-STAR-LEDGER-COLLAPSE-DENSEFRAME-v1`:

> The three-large-eigenvalue target, even together with a physically dense same-bank block and many definite physical pairs, does not force either one definite polynomial star of universal size or a universal L2 aggregate of all such definite stars.  A source-coordinate aggregate mixed frame can remain perfectly conditioned while every pair-first polynomial star, and the entire squared pair-star ledger, collapses to zero.

The order-of-operations issue is explicit.  Pair-first formation multiplies the remaining arm by the physical diagonal `a=3/m` (and subtracts the comparably small `c_pair u`), compressing each local star to `Theta(m^(-3/2))`.  The mixed frame spends the three original coefficient directions `c,w1,w2` jointly while their Gram is still exactly the identity.

## 6. What this pays, and what remains unpaid

This construction settles a proof-mechanism question left by the previous B09 step.  The tiny definite/nonnegative polynomial-star survivor cannot in general be closed by selecting a good physical pair, and cannot be repaired by the naive squared-star ledger.  The aggregate receiver must come first.

What is *not* proved is the required global structural extraction from an arbitrary symmetric `A` with `s_3(A)>=1`.  The remaining unpaid implication is therefore:

`QFORM-SMALL-NONNEGATIVE-STAR-TO-PREPAIR-MIXEDFRAME-OR-CROSSING-v1`.

A successful proof must show that, after the already-paid pair/core chambers are removed, the surviving coefficient mass forces one of the following without illegal assumptions: a literal source-coordinate low-rank-plus-diagonal packet with a universally nondegenerate mixed Gram and diffuse physical leverage; a grouped crossing/volume receiver; or a bounded physical core.  It must retain arbitrary same-bank curvature exactly.  A small coefficient or a small operator/Frobenius remainder cannot be treated as a probabilistically small quadratic perturbation for arbitrary cap-one laws.

## 7. Counterexample status and scope

No valid counterexample to the unrestricted QFORM target was found in this run.  The required pinned counterexample search also reports no valid full-target counterexample.  The construction here is instead a source-valid counterexample to a *proof strategy*: universal forcing, or L2 aggregation, of the latest definite-pair polynomial-star resource.

No diagonal-basis independence, post-rotation independence, moments, support bounds, or log-concavity were used.  Continuity was asserted only on the pinned mixed-frame branch where `phi in L^1`; the latest partner theorem was used only for its essential-density bound.  No probability was squared.

## 8. Source pins used

Owner-control brain main was freshly resolved during the invocation and the required control/assignment/correction files were read before publication.  Required fixed mathematical source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, using its completed mixed Fresnel theorem and counterexample search.  Latest compatible designated partner observed before publication: account03/B09 `20260924T091232Z-account03-B09-QFORM-r47`, using `QFORM-DEFINITEPAIR-POLYNOMIAL-STAR-UNIFORM-v1`.

The unrestricted conjecture remains OPEN.
