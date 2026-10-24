# account02/B01 r30 — anchored second-volume stress and grouped reciprocal-product payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T230122Z-account02-B01-qform-r30`  
**Assignment:** Oscillatory replacement  
**Control at start:** `yspennstate/math-research-brain@54b4ee79cb719323602acfc805017b7a4fad5414`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXPLICIT TARGET-VALID STRUCTURAL FALSIFIER / FULL TARGET OPEN`

## 1. Exact target and correction boundary

The target is unchanged: for every finite dimension, independent real original coordinates with probability densities `0<=f_i<=1`, and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has a density with one universal finite essential-supremum bound, or give a valid target counterexample.

No moment, compact-support, connected-support, Gaussian, log-concavity, identical-law, or post-rotation-independence assumption is used below. The law-uniform pointwise quadratic-phase decay remains false for phase-aligned fragmented densities and is not used. The arbitrary-joint coarea and positive conditional-fiber-moment interfaces remain refuted. The argument below is distributional: it uses product-preserving projection caps, `L^2` product densities, and convolution before any reciprocal coordinate-minor payment.

## 2. Fresh designated-partner frontier actually applied

The newest completed designated-partner handoff is account03/B01 `account03-B01-20260922T223030Z-auto12`, with canonical mathematics

`yspennstate/math-open-problems@ae53a672bb855b66e657c33139e63c2077a5c25b`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T223030Z-auto12/REPORT.md`.

For a physical cross block `N`, write

`E_2(N)=e_2(N^TN)=sum_{|S|=|T|=2} det(N[S,T])^2`

and let the normalized squared-minor law have row and column inclusion marginals `alpha_i,beta_j`. The partner proves an `L^3` residual density, and hence an outer-square `L^infinity` bound, whenever one orientation has every volume marginal at most `2/3`. In the complementary high-marginal branch it proves that there are genuine physical anchors `i,j` carrying more than one third of the total second-volume mass simultaneously. Its first unpaid implication is to spend that anchored mass before choosing one reciprocal `2x2` minor.

This run constructs an exact full-target family sitting maximally in that high-anchor branch: `alpha_i=beta_j=1`, total anchored mass is one, but every individual `2x2` minor tends to zero. The same family is nevertheless paid uniformly by grouping the diffuse bank before inversion.

## 3. Source-pinned analytic inputs

### 3.1 Product `L^2`

Account03/B07 proves `QFORM-PRODUCT-L2-v1` at

`yspennstate/math-open-problems@816c00139a183545a0f85c5b4a939eb52cabcfac`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T221112Z-account03-B07-qform-r18/REPORT.md`.

If `X,Y` are independent with density caps `M,N`, then for `kappa!=0`,

`||p_(kappa X Y)||_2 <= 2 sqrt(MN/|kappa|)`.                    (3.1)

Two independent such products therefore have a bounded continuous convolution with

`||p_(kappa_1 X_1Y_1+kappa_2 X_2Y_2)||_infinity
 <=4 sqrt(M_1N_1M_2N_2/|kappa_1kappa_2|)`.                    (3.2)

The proof allows arbitrary fragmented cap-one supports.

### 3.2 Product-preserving one-dimensional projection cap

The sharp product-projection input used in that report is source-pinned at

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

For a unit coefficient vector `u` and independent cap-one original coordinates,

`U=<u,X>` has density cap at most `sqrt(2)`.                    (3.3)

This is a theorem about an original-coordinate product source. No independence after a general spectral rotation is asserted.

## 4. A grouped reciprocal-product theorem

### Theorem 4.1 — `QFORM-RECIPROCAL-TWO-PRODUCT-GROUPING-v1`

Let `0<epsilon<=1`. Let `X_0,Y_0` be independent cap-one variables. Let `X=(X_1,...,X_r)` and `Y=(Y_1,...,Y_s)` be two further disjoint banks of independent cap-one original coordinates, also independent of `X_0,Y_0`. Let `u in R^r`, `v in R^s` be unit vectors and put

`U=<u,X>`, `V=<v,Y>`.

Let `W` be any random variable independent of all four displayed source groups. Then

`T = 2 epsilon X_0Y_0 + 2 epsilon^(-1) U V + W`                 (4.1)

has a bounded density satisfying

`boxed: ||p_T||_infinity <= 2 sqrt(2).`                         (4.2)

If `W` is absent, or if it has any independent probability law, the same bound holds. In particular an independent physical square may be added without cost.

More generally, after conditioning on an independent outside random object `Omega`, arbitrary `Omega`-dependent translations may be inserted into the four factors and an arbitrary additive `H(Omega)` may be added; the same bound remains valid because the conditional density caps are translation-invariant.

#### Proof

By (3.3),

`||p_U||_infinity, ||p_V||_infinity <=sqrt(2)`.                  (4.3)

Apply (3.1) to the first product with `M=N=1`, `kappa=2epsilon`:

`||p_(2epsilon X_0Y_0)||_2
 <=2 sqrt(1/(2epsilon))
 =sqrt(2) epsilon^(-1/2).`                                      (4.4)

Apply (3.1) to the second product with both density caps `sqrt(2)` and `kappa=2epsilon^(-1)`:

`||p_(2epsilon^(-1)UV)||_2
 <=2 sqrt(2/(2epsilon^(-1)))
 =2 epsilon^(1/2).`                                             (4.5)

The two products are genuinely independent because they use disjoint original-coordinate groups. Cauchy--Schwarz/Young therefore gives

`||p_(2epsilon X_0Y_0+2epsilon^(-1)UV)||_infinity
 <= [sqrt(2)epsilon^(-1/2)] [2epsilon^(1/2)]
 =2sqrt(2).`                                                     (4.6)

Convolution with the independent probability law of `W` cannot increase an `L^infinity` norm. This proves (4.2). Conditional translations do not change any one-dimensional density cap or any product `L^2` norm, so conditioning on `Omega` and averaging proves the stated extension. QED.

### Distributional meaning

The reciprocal coefficients in (4.1) are deliberately hostile to any single-factor estimate: the first product becomes more singular as `epsilon` decreases. The second product becomes correspondingly more spread out, and the two `L^2` costs cancel exactly before convolution. This is an averaged/distributional replacement for a nonexistent pointwise Fresnel envelope.

## 5. Exact high-anchor second-volume family

For every integer `m>=2`, put

`epsilon=m^(-1/2)`,
`u_m=v_m=m^(-1/2)(1,...,1) in R^m`,

and define the `(m+1)x(m+1)` physical cross block

`N_m = epsilon e_0 e_0^T + epsilon^(-1) u_m v_m^T`,             (5.1)

where the second term acts only on the last `m` rows and last `m` columns. Explicitly,

`N_m[0,0]=1/sqrt(m)`,
`N_m[k,l]=1/sqrt(m)` for `1<=k,l<=m`,

and the remaining first-row/first-column off-block entries are zero.

The two nonzero singular values are exactly

`sigma_1(N_m)=sqrt(m)`, `sigma_2(N_m)=1/sqrt(m)`.               (5.2)

Hence

`E_2(N_m)=sigma_1^2 sigma_2^2=1`.                               (5.3)

All nonzero `2x2` minors are precisely

`det N_m[{0,k},{0,l}] = 1/m`, `1<=k,l<=m`.                     (5.4)

There are `m^2` of them, so their squared masses sum exactly to one. Therefore the squared-minor volume law is uniform on those `m^2` minors and

`alpha_0=beta_0=1`,                                             (5.5)

while each nonanchor row and column has marginal `1/m`. Thus the partner's high-anchor alternative is saturated: the anchor intersection carries `100%` of `E_2`, but

`max_{|S|=|T|=2} |det N_m[S,T]| =1/m ->0`.                     (5.6)

This is a quantitative obstruction to any continuation of the partner's anchored-mass theorem by selecting one fixed physical `2x2` minor with a universal lower bound.

## 6. Embed the obstruction in the exact owner target

Define the symmetric physical matrix

`A_m = [1] direct_sum [[0,N_m],[N_m^T,0]]`.                     (6.1)

The bipartite block has eigenvalues `+sigma_1,-sigma_1,+sigma_2,-sigma_2` and zeros. Therefore

`spec(A_m)={1, sqrt(m),-sqrt(m), 1/sqrt(m),-1/sqrt(m),0,...,0}`. (6.2)

For every `m>=2`, **exactly three** eigenvalues have absolute value at least one: `1,+sqrt(m),-sqrt(m)`. Thus this is a target-valid spectral family, not merely an intermediate matrix gadget.

Moreover every nonouter nonzero physical coefficient is only `1/sqrt(m)`. In particular the strong spectral directions do not force a large physical edge or a large fixed cross minor in this family.

Let the corresponding independent cap-one source coordinates be

`Z, X_0,X_1,...,X_m, Y_0,Y_1,...,Y_m`.

Set

`U_m=m^(-1/2) sum_{k=1}^m X_k`,
`V_m=m^(-1/2) sum_{l=1}^m Y_l`.

Then exactly

`Q_m=X^T A_m X
    = Z^2 + 2m^(-1/2) X_0Y_0 + 2m^(1/2) U_m V_m`.              (6.3)

The groups in (6.3) are genuinely disjoint original-coordinate groups, so Theorem 4.1 gives

`boxed: ||p_(Q_m)||_infinity <=2sqrt(2)`                         (6.4)

for **every** choice of the cap-one marginal laws. The density is in fact continuous after the two-product convolution; adding the independent square preserves continuity.

Thus the family is not a counterexample to QFORM. It is a source-valid counterexample to a fixed-minor continuation of the new anchored-second-volume frontier, and simultaneously an exact model showing how grouping before inversion repairs the apparent loss.

## 7. Relation to the phase-aligned obstruction

The scalar pointwise quadratic-phase estimate remains false: a density may be supported on finitely many phase-aligned fragments and make `|E exp(itX^2)|` arbitrarily close to one at a prescribed large `t`. Nothing in Sections 4--6 contradicts or bypasses that construction by pointwise oscillation.

Instead, the proof of (6.4) uses two integrated facts that survive arbitrary fragmented supports: product variables have dimension-free `L^2` densities under density caps, and normalized product-source linear projections have a dimension-free density cap. Their reciprocal scale factors cancel only after the two product pieces are convolved. This is exactly the kind of aggregate/distributional currency the false pointwise route was missing.

## 8. What is and is not refuted

### Refuted intermediate implication

`QFORM-ANCHORED-E2-FIXED-MINOR-FALSE-v1`:

> Even under the exact three-large-eigenvalue owner target, a cross block can have `E_2=1`, a physical anchor row and column with inclusion marginals equal to one, and anchored squared-minor mass equal to one, while every individual physical `2x2` cross minor tends to zero.

The family (5.1)--(6.2) proves this with maximum minor `1/m`.

### Not refuted

- The full bounded-density conjecture is not refuted; this family obeys the stronger uniform bound (6.4).
- The designated partner theorem is not refuted. Its diffuse marginal gate correctly refuses this family and exposes the anchored branch.
- Aggregate anchored-mass payment remains plausible; indeed the family demonstrates one successful grouped payment.

## 9. First unpaid implication after this run

The next useful statement is not a fixed-minor extractor. It is

`QFORM-ANCHORED-E2-GROUPED-CURVATURE-v1`:

> Starting from the designated partner's high-anchor second-volume packet, identify a source-coordinate grouped decomposition that retains the reciprocal-scale cancellation of Theorem 4.1 while allowing the arbitrary same-side quadratic curvature and cross-core couplings present in the full Schur residual; or prove that failure forces an already-paid physical-pair, scalar-square, ridge, third-cross-volume, or grouped-star branch.

The stress family shows why the payment has to occur before reciprocal minor selection: the total second-volume is perfectly normalized while each minor is `1/m`. Theorem 4.1 shows that this diffuse reciprocal packet itself is harmless when its rank-two geometry separates into two disjoint product groups. The remaining difficulty is exactly the curvature/coupling splice, not the diffuse bank size.

Full QFORM remains **OPEN**. There is no full-proof candidate and therefore no pair of end-to-end reviews.

## 10. Exact arithmetic checks

For the uniform-bank specialization:

- `sigma(N_m)=(sqrt(m),1/sqrt(m),0,...)`;
- `E_2(N_m)=1`;
- exactly `m^2` nonzero `2x2` minors, each `1/m`;
- their squared sum is `m^2*(1/m^2)=1`;
- `max |N_m[k,l]|=1/sqrt(m)`;
- the two product `L^2` bounds are `sqrt(2)m^(1/4)` and `2m^(-1/4)`, whose product is exactly `2sqrt(2)`.

These calculations only check the displayed algebra. The proof is the exact singular-value/minor computation and the source-pinned analytic inequalities above.