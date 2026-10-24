# account02/B04 — exact fractional base-packing gate for third-volume weights

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement / complementary constructions  
Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / TARGET-VALID EXPLICIT ESTIMATE`  
Full unrestricted QFORM target: **OPEN**.

## 1. First unpaid implication

The previous B04 run proved the q=1 support criterion (two disjoint row bases) and left `QFORM-SUPPORT-DEFICIENT-DOUBLE-HUB-QUANTITATIVE-PAYMENT-v1`.

This run pays the **support** part for the entire fractional three-volume window. The first unpaid implication is now

`QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPOUND-HUB-PAYMENT-v1`:

> after the exact fractional support gate below, pay the only surviving exact support geometries (coloop; all but two active rows in one rank-one flat; at most four active rows), and pay the quantitative <=6-row/<=6-column compound hubs forced by account03/B04 r31 when determinant-entropy currency is small, without selecting a vanishing local coefficient.

The analytic three-volume gate itself is no longer the obstruction in every five-active-row uniform-matroid configuration.

## 2. Sources actually used

Pinned Claude/e5 source, read at the requested commit:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`
- `.../FOURIER_ROUTE_REPORT.md`
- `.../COUNTEREXAMPLE_SEARCH.md`.

Theorem D gives `6 sqrt(e) Z^(-1/6)` under row marginal cap `1/2`; D' permits cap `h<3/4` with

`6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) Z^(-1/6)`.

The sharper completed q-dependent natural-volume theorem used below is

- `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`
- `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`,

which gives, for `1<=q<3/2` and natural row marginals `alpha_i<=q/2`,

`||p_Q||inf <= [3e/((3-2q)sqrt(q))] E3(M^T M)^(-1/6)`.

The designated partner result actually applied is account03/B04 r31:

- `yspennstate/math-open-problems@1c9eda73c97b03bf78aa6750726df00ce3768d21`
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T095028Z-account03-B04-qform-auto11-r31/REPORT.md`.

Its `QFORM-ENTROPY-WEIGHTED-DPRIME-v1` optimizes

`G_h(M)=sup exp(E_w log det(M_ST)^2 + H(w))`

over supported physical 3x3-minor laws with row marginals at most `h`, and yields

`||p_Q||inf <= 6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1) G_h(M)^(-1/6)`.

No pointwise one-dimensional quadratic-phase envelope, arbitrary-joint coarea bound, conditional projection-cap moment, or independence after a spectral rotation is used.

## 3. Exact support theorem for the full fractional window

### Theorem — `QFORM-THIRDVOLUME-FRACTIONAL-BASEPACKING-v1`

Let `M` be an original-coordinate cross block of rank at least three. Delete zero physical rows and let `N` be the rank-three truncation of the physical row matroid on active row set `E`. Define

`h_*(N)=inf { h : there is a probability law on nonzero physical 3x3 minors with every row marginal <=h }`.

Then

`boxed: h_*(N)=max_{A subset E, r(A)<3} (3-r(A))/|E\A|.`                       (3.1)

Equivalently, if

`nu_*(N)=min_{A subset E, r(A)<3} |E\A|/(3-r(A))`,

then `h_*=1/nu_*`.

Hence a fractional three-volume Fourier exponent `q` can pass the support gate exactly when

`q/2 >= h_*`.

In particular, some admissible cap `h<3/4` exists **unless** at least one of the following holds:

1. a physical row is a coloop (it belongs to every supported row basis);
2. all but two active physical rows lie in one rank-one flat;
3. there are at most four active physical rows.

These alternatives are exact at the support level.

### Proof

A physical row triple `S` supports some nonzero `3x3` minor iff the three rows are independent, i.e. iff `S` is a basis of `N`. Thus column labels do not affect row-cap feasibility: after choosing a supported row basis one may choose any column triple witnessing its nonzero determinant.

Consider the fractional base-packing LP

`nu = max sum_B y_B`,

subject to `y_B>=0` and `sum_{B contains i} y_B<=1` for every active row `i`. Its dual is

`min sum_i z_i`,

subject to `z_i>=0` and `sum_{i in B} z_i>=1` for every basis `B`.

For every `A subset E` with `r(A)<3`, putting weight `1/(3-r(A))` on every element of `E\A` and zero on `A` is dual-feasible, because every basis contains at least `3-r(A)` elements outside `A`. Therefore

`nu <= |E\A|/(3-r(A))`.

For the reverse inequality let `z` be any dual-feasible vector and set `A_t={i:z_i<t}`. The matroid greedy formula for minimum base weight gives

`min_B sum_{i in B}z_i = integral_0^infinity [3-r(A_t)] dt`.

The left side is at least one. If `nu_0` denotes the minimum ratio on the right side of (3.1), then for every `t`,

`|E\A_t| >= nu_0 [3-r(A_t)]`.

Integrating,

`sum_i z_i = integral_0^infinity |E\A_t|dt >= nu_0 integral_0^infinity [3-r(A_t)]dt >= nu_0`.

LP duality gives `nu=nu_0`.

Now a probability law `w_B` with row loads at most `h` becomes, after scaling by `1/h`, a fractional base packing of total mass `1/h` and vertex capacities one. Conversely any fractional base packing of total at least `1/h` can be rescaled to total exactly `1/h`, and then multiplied by `h`, to give such a probability law. Thus feasibility is equivalent to `nu>=1/h`, proving (3.1).

For the `3/4` classification, choose `A` attaining a ratio at least `3/4`. Since `r(A)` is `0,1`, or `2`:

- if `r(A)=2`, then `1/|E\A|>=3/4`, so `|E\A|=1`, a coloop;
- if `r(A)=1`, then `2/|E\A|>=3/4`, so `|E\A|<=2`; rank three forces exactly two outside rows;
- if `r(A)=0`, active rows cannot lie in `A`, and `3/|E|>=3/4`, so `|E|<=4`.

The converse is immediate from (3.1). QED.

### Relation to the previous q=1 theorem

At `h=1/2`, (3.1) recovers the previous support trichotomy: q=1 failure can occur for a coloop, all but at most three active rows in a rank-one flat, or at most five active rows. The new point is that the five-row case by itself disappears once the proved D' window is used: only the stronger `3/4` defects above survive every fractional exponent.

## 4. A five-row tight frame: q=1 impossible, fractional volume optimal

Let `theta_k=2 pi k/5`, `k=0,...,4`, and let the rows of `U0` be

`u_k=(1/sqrt(5), sqrt(2/5) cos(theta_k), sqrt(2/5) sin(theta_k))`.

Let

`V=(1/7) [[6,-2,-3],[-2,3,-6],[-3,-6,-2]]`,

so `V^T V=I`, and put

`U=U0 V`, `M=2U`.

The right multiplication by `V` is part of the deterministic physical coefficient matrix; no random input is rotated.

Discrete trigonometric orthogonality gives

`U^T U=I_3`,

and every physical row has

`||u_k||^2=3/5`.

For three distinct angles, the determinant of the unscaled rows is a nonzero constant times

`sin((theta_b-theta_a)/2) sin((theta_c-theta_b)/2) sin((theta_a-theta_c)/2)`,

so every one of the ten physical row triples is a basis. The fixed `V` preserves these determinants up to sign. Direct exact-radical checks also show all fifteen entries of `U` are nonzero, although that is not needed for the argument.

Since `M^T M=4I_3`,

`E3(M^T M)=64`.

For an exact rank-three block, the squared-minor volume law has row marginals equal to the diagonal of `UU^T`; hence every natural row marginal is exactly

`alpha_i=3/5`.

Every probability law on row triples has total marginal mass three. With only five active rows, `max alpha_i>=3/5`. Therefore

`boxed: h_*=3/5`,

and the natural squared-minor law is support-optimal.

Moreover, if `nu` is that natural law, then for every supported minor law `w`,

`log G(w)=log 64-D(w||nu)<=log64`.

Thus for every `h>=3/5`, the partner r31 optimizer is exactly

`G_h(M)=64`,

while for `h<3/5` the feasible set is empty. This is a global optimization over all admissible physical volume weights, not a symmetric ansatz.

## 5. Completed Fourier results applied to the actual inequality

The original pinned e5 Theorem D at cap `1/2` cannot apply to this matrix for **any** minor weighting: five row marginals summing to three cannot all be at most one half. This is an actual support obstruction to D, not a QFORM counterexample.

The pinned e5 D' extension and the designated partner account03/B04 r31 theorem do apply at the exact minimum `h=3/5`. Since `G_{3/5}=64`, r31 gives

`||p_Q||inf <= 6 sqrt(e)(6/5)^(-1/2)(3/5)^(-1)64^(-1/6)`

and therefore

`boxed: ||p_Q||inf <= 5 sqrt(e) sqrt(5/6) = 7.525348591675347... .`       (5.1)

This is the requested application of a completed partner result to an actual inequality.

The sharper completed natural-volume q theorem at `q=6/5` improves the same physical form to

`boxed: ||p_Q||inf <= (5e/2)sqrt(5/6) = 6.203601146264198... .`            (5.2)

The coefficient `3e/((3-2q)sqrt(q))` is strictly increasing for `q>=1`, and no `q<6/5` is support-feasible here, so `q=6/5` is the exact optimum inside that natural-volume q family.

## 6. Ridge certificate on the identical physical matrix, globally optimized

For this `M`, let

`kappa=4/(4+gamma^2)`.

Because `MM^T=4UU^T`,

`K_gamma=kappa UU^T`,

so

`max_i (K_gamma)_ii = 3kappa/5`,

`theta_gamma=3kappa`,

`D_gamma=(1-gamma-independent notation) = det(I+MM^T/gamma^2)=(1-kappa)^(-3)`.

The completed ridge theorem requires

`q >= 6kappa/5`, `q>=1`, and `q<3kappa/2`.

Its exact first bound is

`R(kappa,q)= e/(sqrt(2q) gamma) * [3kappa/(3kappa-2q)] * (1-kappa)^(1/(2kappa))`,

where `gamma=2 sqrt((1-kappa)/kappa)`.

For fixed `kappa`, the q-dependent factor `q^(-1/2)/(3kappa-2q)` is strictly increasing throughout the feasible interval, because its stationary point is `q=kappa/2`, below every feasible `q`. Hence

`q_min=max(1,6kappa/5)`.

If `2/3<kappa<=5/6`, then `q=1`; differentiating the resulting logarithm gives

`d/dkappa log R = [-4kappa/(3kappa-2)-log(1-kappa)]/(2kappa^2)<0`.

Indeed on this interval `4kappa/(3kappa-2)>=20/3>log6>=-log(1-kappa)`.

If `5/6<=kappa<1`, then `q=6kappa/5` and

`R=C (1-kappa)^((1-kappa)/(2kappa))`,

whose logarithmic derivative is

`[-log(1-kappa)-kappa]/(2kappa^2)>0`.

Therefore the global ridge optimum occurs exactly at

`kappa=5/6`, `q=1`, `gamma^2=4/5`.

At this point

`max diag K=1/2`, `theta=5/2`, `D=216`,

and the exact determinant-retaining ridge theorem gives

`boxed: ||p_Q||inf <= [5e sqrt(5)/(2sqrt(2))] 216^(-1/5)`

`                     = 3.667023935266282... .`                         (6.1)

Thus on this same physical matrix the optimized ridge certificate is substantially stronger than both fractional-volume certificates, even though the q=1 volume gate is structurally impossible.

## 7. Genuinely rotated indefinite target form

Let

`A_* = [[0_{5x5}, M],[M^T,0_{3x3}]]`.

Then for the eight original independent coordinates,

`Q_*=X^T A_* X=2 X_I^T M X_J`.

The nonzero spectrum of `A_*` is exactly the signed singular spectrum of `M`:

`{2,2,2,-2,-2,-2}`,

with two additional zeros. Thus six eigenvalues satisfy the exact target threshold `|lambda|>=1`. The matrix is indefinite and genuinely non-diagonal in the original product coordinates; no diagonal-basis or post-rotation independence is invoked.

For every independent cap-one product input law, (6.1) gives

`boxed: ||p_{Q_*}||inf <= 3.667023935266282... .`

For comparison, the same matrix has the source-valid volume hierarchy

`ridge optimum 3.6671 < sharp fractional volume 6.2037 < partner/e5 D' 7.5254`,

while the original e5 q=1 Theorem D has no admissible minor weighting at all.

## 8. Proof-map consequence

The exact support obstruction for the full proved fractional window is now much narrower than the previous q=1 obstruction. A mere five-row physical cross support is **not** hard: if its rank-three truncation is not more degenerate, fractional volume already has an admissible exponent, and in the symmetric tight-frame case it is globally entropy-optimal.

Combining this run with account03/B04 r31 leaves the structural analytic frontier:

- exact support-infeasible: coloop; rank-one flat plus only two transverse active rows; or at most four active rows;
- support-feasible but poor determinant-entropy currency: r31 compresses the third volume into a bounded <=6-row hub (and, after transposition, a bounded compound row/column hub);
- quantitative currency not poor: r31/D' or the sharper natural-volume theorem exits by Fourier inversion.

What remains is to pay the finite exact/compound hubs from the three-large-eigenvalue hypothesis without selecting a vanishing physical coefficient. This is the first unpaid implication stated in Section 1.

## 9. Scope and checks

All self blocks and outside couplings allowed by the cited Fourier/ridge theorems remain unrestricted; the displayed target family sets them to zero only to make the same-matrix comparison exact. Continuity follows for this displayed family from the integrable characteristic-function theorems; no unrestricted continuity statement is promoted.

Exact/scalar checks are in `CHECKS.json` in this run directory. They verify `V^TV=I`, `U^TU=I`, row norm squares `3/5`, nonzero row triples, `E3=64`, the target spectrum, and the displayed constants. They are not an independent proof certificate.
