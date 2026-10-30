# fleet03/B13 — entropic three-volume rebalancing versus six physical hubs

Run: `20260923T003350Z-fleet03-B13-qform-r20`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Extremal product laws  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW STRUCTURAL/ANALYTIC SUPPORTING THEOREM / FULL QFORM OPEN / FULL CONTINUITY OPEN**

## 1. Target and source-safe scope

The target is the full owner conjecture: for every finite `n`, arbitrary independent real coordinates with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension-free finite essential density bound for `Q=X^T A X`, or give a genuine counterexample. No moment, compact-support, connected-support, log-concavity, Gaussian, or post-rotation-independence assumption is used here.


Three completed inputs are used at their exact scopes.

1. **Previous B13 reduction.** `yspennstate/math-open-problems@d21000e145ff5e4756c0abc8727a7c7aa1a02e4d`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260922T233245Z-fleet03-B13-qform-r19/REPORT.md`: full QFORM essential boundedness has been reduced, through the supplied full-to-no-pivot synthesis, to a countable strict no-`1/16`-pivot rational-grid extreme-product slab problem. This does not bound fragment count, support radius, separation, or grid denominator.
2. **Designated partner fleet04/B13.** `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T231352Z-fleet04-B13-rough-geometric-transfer-r5/REPORT.md`: for every bounded measurable product kernel, the supremum over cap-one mass-one marginals equals the supremum over indicators of bounded finite unions of intervals of measure one. There is no asserted optimizer, interval extremality, diameter bound, or uniform fragment count.
3. **Mixed-order minor Fourier theorem.** `yspennstate/math-open-problems@66b5ff888a219c7c8e754dd25062fac6aecb2f22`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T001242Z-b01-qform-auto11/REPORT.md`. If a probability law `Omega` on nonzero physical square minors of a cross block has mean order `kbar>2`, all row marginals at most `1/2`, and entropy-determinant currency `K(Omega)=exp(E log det(M_ST)^2+H(Omega))`, then `||p_Q||_infinity <= 2 sqrt(e) kbar/(kbar-2) K(Omega)^(-1/(2 kbar))`, with a bounded continuous density in that scope. For fixed order three this is `6 sqrt(e) K(Omega)^(-1/6)`.

The new result below is a quantitative structural theorem for the exact obstruction left by the last input: clustered/co-heavy three-volume. It says that a failure to rebalance three-volume at bounded entropy cost forces almost all of that three-volume onto at most six original physical rows.

## 2. Setup: the natural three-volume law

Let `M` be any finite real matrix whose rows are indexed by a set `I` and columns by `J`. Put

`Z = e_3(M^T M) = sum_{|S|=|T|=3} det(M_ST)^2`.

Assume `Z>0`. Let `A_3` denote the finite set of nonzero physical `3x3` minors `a=(S,T)`, and define the natural probability law

`w_a = det(M_ST)^2 / Z`.

For any probability law `mu` on `A_3`, define the physical-row load

`alpha_i(mu)=P_mu(i in S)`

and relative entropy

`D(mu||w)=sum_a mu_a log(mu_a/w_a)`.

The determinant-entropy currency of `mu` is

`K(mu)=exp(H(mu)+E_mu log det(M_ST)^2)`.

Because `w_a=det(M_ST)^2/Z`, there is the exact identity

`boxed: K(mu)=Z exp(-D(mu||w)).`                                      (2.1)

Thus an entropy-bounded way of capping every physical-row load immediately gives a dimension-free fraction of the total three-volume currency.

## 3. Main theorem

### Theorem 3.1 — `QFORM-ENTROPIC-3VOLUME-OR-SIX-HUB-v1`

Fix `L>0`. At least one of the following conclusions holds for every `M` with `Z>0`.

**Paid entropic three-volume branch.** There is a probability law `mu` on nonzero physical `3x3` minors such that

`alpha_i(mu)<=1/2` for every physical row `i`,

and

`D(mu||w)<=L`.

Consequently

`K(mu)>=e^(-L) Z`,                                                   (3.1)

and every quadratic polynomial whose original-coordinate cross block is this `M` obeys

`boxed: ||p_Q||_infinity <= 6 sqrt(e) e^(L/6) Z^(-1/6).`              (3.2)

The conclusion is uniform over arbitrary self blocks, outside couplings, affine terms, signs, and arbitrary independent cap-one original-coordinate laws. The mixed-order source gives a continuous density in this paid branch.

**Six-hub concentration branch.** There is a set `H` of at most six original physical rows such that, after deleting those rows,

`boxed: e_3(M_{I\H,J}^T M_{I\H,J}) < e^(-L) Z.`                      (3.3)

If no row-capped probability law exists at all, the conclusion sharpens to `|H|<=5` and the left side of (3.3) is exactly zero.

For the concrete choice `L=log 64`, either

`boxed: ||p_Q||_infinity <= 12 sqrt(e) Z^(-1/6)
                         = 19.7846552484015... Z^(-1/6),}`             (3.4)

or at most six physical rows capture more than `63/64` of the entire natural three-volume currency:

`e_3(M_{I\H,J}^T M_{I\H,J}) < Z/64.`                                (3.5)

### Proof

Let

`F={mu probability on A_3: alpha_i(mu)<=1/2 for all i}`.

There are two cases.

#### Case A: `F` is empty

Forget the column label `T` and regard each supported row triple `S` as an edge of a 3-uniform hypergraph on `I`. If a row-capped `mu` existed, then `x_a=2 mu_a` would give a fractional matching of total weight two with every vertex load at most one. Therefore emptiness of `F` implies that the fractional matching number is strictly less than two.

By finite linear-program duality, the fractional vertex-cover number is also strictly less than two. Hence there are nonnegative weights `y_i` with

`sum_i y_i <2`,

and

`sum_{i in S} y_i >=1` for every supported row triple `S`.

Set

`H={i:y_i>=1/3}`.

Every supported row triple meets `H`, since otherwise its three `y`-weights would sum to less than one. Moreover

`|H| <= 3 sum_i y_i <6`,

so `|H|<=5`. Every nonzero `3x3` minor therefore uses a row from `H`. After deleting `H` every `3x3` minor vanishes, and Cauchy--Binet gives

`e_3(M_{I\H,J}^T M_{I\H,J})=0`.

This proves the strengthened hub conclusion in the infeasible case.

#### Case B: `F` is nonempty

Let

`D_* = inf_{mu in F} D(mu||w)`.

The infimum is attained because `F` is a compact finite-dimensional polytope and relative entropy is lower semicontinuous. If `D_*<=L`, choose a minimizer `mu`. Identity (2.1) gives (3.1). Applying the completed fixed-order-three instance of the mixed-order minor theorem gives

`||p_Q||_infinity <= 6 sqrt(e) K(mu)^(-1/6)
                    <= 6 sqrt(e) e^(L/6) Z^(-1/6)`,

which is (3.2).

It remains to treat `D_*>L`. The finite-alphabet entropy projection with linear upper constraints has the exact convex dual

`D_* = sup_{lambda_i>=0} [ -log E_w exp(-Lambda(S))
                           - (1/2) sum_i lambda_i ],`                  (3.6)

where

`Lambda(S)=sum_{i in S} lambda_i`.

Equation (3.6) is the Gibbs variational formula for relative entropy followed by Lagrange duality for the finite set of inequalities `E_mu 1_{i in S}<=1/2`; equivalently it follows by finite-dimensional Fenchel duality. No limiting measure or optimizer on the real line is involved.

Since `D_*>L`, choose nonnegative `lambda_i` for which the bracket in (3.6) is greater than `L`. Put

`R=sum_i lambda_i`.

Necessarily `R>0`, and

`E_w exp(-Lambda(S)) < exp(-L-R/2).`                                  (3.7)

Define the heavy dual-row set

`H={i:lambda_i>=R/6}`.

Then `|H|<=6`. For every row triple disjoint from `H`, each of its three weights is strictly below `R/6`, hence

`Lambda(S)<R/2`

and therefore

`exp(-Lambda(S))>exp(-R/2)`.

Using (3.7),

`P_w(S cap H = empty) exp(-R/2)
 < E_w exp(-Lambda(S))
 < exp(-L-R/2)`.

Thus

`P_w(S cap H = empty)<e^(-L).`                                       (3.8)

But the left probability is exactly the fraction of total Cauchy--Binet three-volume surviving after rows `H` are deleted:

`P_w(S cap H = empty)
 = e_3(M_{I\H,J}^T M_{I\H,J})/Z`.

This proves (3.3). The theorem follows. QED.

## 4. Actual application of the designated fleet04/B13 result

The preceding analytic branch can be expressed first on the extreme-product geometry required by B13. Fix a matrix/cross block satisfying the paid branch and an interval `J0`. For every tuple of unit-measure measurable sets `E_i`, the fixed-order-three Fourier theorem applied to the product-indicator input gives

`|{x in product_i E_i : x^T A x in J0}|
 <= 6 sqrt(e) e^(L/6) Z^(-1/6) |J0|.`                               (4.1)

Now apply fleet04/B13 Corollary 2.2 to the bounded kernel

`K(x)=1_{x^T A x in J0}`.

Its exact supremum identity transfers (4.1), with **zero constant loss**, to every independent cap-one mass-one marginal law:

`boxed: P(X^T A X in J0)
 <= 6 sqrt(e) e^(L/6) Z^(-1/6) |J0|.`                               (4.2)

At `L=log64`, this is precisely the slab inequality corresponding to (3.4). This application retains arbitrary fragmented and unbounded one-dimensional laws. It does not assume a single interval, centered uniform law, bounded diameter, or bounded fragment count.

The fleet01/B01 source theorem directly gives `phi in L1` in this same paid branch, so a continuous density is available there. The fleet04/B13 transfer itself is only needed for the rough-law extreme-product passage and by itself would establish essential boundedness, not continuity.

## 5. Consequence for the live no-pivot finite-grid problem

Apply Theorem 3.1 to any physical cross block arising from a strict no-`1/16`-pivot rational-grid extreme-product witness from the previous B13 reduction. For every such cross block with `Z>0`, at `L=log64` there is a rigorous dichotomy:

1. **Paid cross-volume:** the entire rough-law branch is closed with the explicit density/slab bound `12 sqrt(e) Z^(-1/6)`; or
2. **Six-row hub concentration:** at most six original coordinates carry at least `63/64` of that block's natural three-volume currency.

This strictly improves the previous structural description of the co-heavy obstruction. One no longer needs to reason about an uncontrolled collection of individually heavy three-volume rows: if entropy rebalancing cannot pay them at bounded cost, the obstruction collapses quantitatively onto a bounded physical hub set.

This also meshes with the newest independent fleet evidence. Fleet02/B03 exhibits exact no-pivot star-plus-square target families on which every order-three/five cross-volume certificate vanishes but a genuine mixed-hub/Fresnel theorem gives a uniform density bound. Fleet02/B19 proves a robust D5 exit for the complementary dense-twist branch. The theorem here supplies a deterministic bridge from a failed three-volume rebalancing attempt to the bounded-hub geometry those mechanisms are designed to address.

## 6. What remains

This is not a proof of full QFORM. In the six-hub branch, (3.3) is a statement about **three-volume currency**, not an operator-norm perturbation and not a permission to delete the residual block on unbounded supports. The live corrections explicitly forbid treating small coefficients or small aggregate minors as a harmless random perturbation without a product-preserving analytic estimate.

The first unpaid B13 implication is now:

**`QFORM-SIX-HUB-LOW-3VOLUME-GLUING-v1`.** In the strict no-`1/16`-pivot rational-grid extreme-product class, suppose every candidate useful cross block is in the six-hub branch of Theorem 3.1. Prove that the bounded hub set plus the low residual three-volume can be routed, with a universal constant and before reciprocal local-minor payment, to one of the completed mixed-hub/Fresnel, D5, determinant-pair, grouped-bank, or localized branches. The estimate must be uniform in grid mesh, support radius, translations, gaps, and fragment count.

One useful iterative corollary is immediate: if the paid branch fails at each stage, after `r` successive applications one can remove at most `6r` physical rows and reduce the surviving three-volume by a factor `64^(-r)`. This is a structural concentration statement only; converting it into a universal density bound without allowing the number of hubs to grow with the ambient matrix is the next substantive debt.

Full QFORM therefore remains **OPEN / NOT PROVED**. The full continuous-density conclusion also remains **OPEN**. Continuity is proved only in the paid entropic-three-volume branch through the source `L1` characteristic-function theorem.

## 7. Deterministic arithmetic / sanity check

The companion standard-library checker verifies:

- `exp(log(64)/6)=2`;
- the paid-branch prefactor is `12 sqrt(e)=19.784655248401538...`;
- an all-edges-through-one-row 3-uniform support is correctly infeasible for row cap `1/2` and has a one-row exact cover;
- two disjoint row triples with half-half mass have every row load exactly `1/2`;
- the identity `K=Z exp(-D(mu||w))` holds numerically to floating-point precision on a nontrivial two-atom example.

The checker is corroborating evidence only; the theorem is analytic.