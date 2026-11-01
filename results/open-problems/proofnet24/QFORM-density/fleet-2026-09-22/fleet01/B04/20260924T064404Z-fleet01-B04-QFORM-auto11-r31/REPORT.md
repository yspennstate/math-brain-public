# QFORM fleet01/B04 r31 — row-matroid half-cap packing gap and tight-flat Fourier compiler

Run: `20260924T064404Z-fleet01-B04-QFORM-auto11-r31`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: product Fourier rearrangement  
Status: supporting theorem candidate / full QFORM OPEN / independent review pending / `WITHOUT_VERIFIED_BRAIN`

## 1. Target and scope

The target remains: for independent real coordinates with densities bounded by one and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal bound on the density of `X^T A X`, or give a valid counterexample. No moment, support, Gaussian, log-concavity, or rotated-independence assumption is used here.

This report attacks the structural debt left by the global half-row-cap determinant-entropy currency and the disjoint-row-triple matching certificate. The result is not a full solution. It gives (i) an exact matroidal description of when the half-row-cap feasible set exists, (ii) a discrete gap away from the critical value, and (iii) a new exact tight-rank-two-flat Fourier compiler. On its paid branch the existing product-Fourier theorem gives a `C_0(R)` density.

## 2. Row-volume bases and half-cap currency

Let `M` be a literal physical cross block, with physical row vectors `m_i`. Discard zero rows and define

`z_S = det( M[S,:] M[S,:]^T ) >= 0`, `|S|=3`.

Thus `z_S>0` exactly when the three physical rows in `S` are linearly independent. Let `B` be the family of such triples. It is the base family of the rank-three truncation of the real row matroid of `M`. Its rank function is

`r(F)=min(3, dim span{m_i:i in F})`.

For a probability law `p` on `B`, write `alpha_i=P_p(i in S)`. The half-row-cap determinant-entropy currency proved earlier is

`G^*_{1/2}(M)=max exp( H(p)+sum_S p_S log z_S )`

over all `p` with every `alpha_i<=1/2`; if the feasible set is empty, set the currency to zero. The existing arbitrary-curvature product-Fourier theorem gives

`||p_Q||_infinity <= 6 sqrt(e) [G^*_{1/2}(M)]^(-1/6)`,

and its Fourier `L^1` conclusion gives a representative `p_Q in C_0(R)` whenever the currency is positive.

## 3. New theorem: QFORM-ROWMATROID-HALFCAP-PACKING-GAP-v1

### Theorem 3.1 (exact half-cap feasibility)

The following are equivalent.

1. There is a probability law on supported row triples with `alpha_i<=1/2` for every physical row.
2. The rank-three row matroid contains two disjoint bases, i.e. two disjoint supported physical row triples.
3. For every physical row set `F`,

`|E\F| >= 2(3-r(F))`.

Here `E` is the nonzero physical-row ground set.

### Proof

Assume (1). Every base `S` contains at least `3-r(F)` elements outside `F`, because at most `r(F)` elements of `S` can lie in `F`. Hence

`3-r(F) <= E_p |S\F| = sum_{i notin F} alpha_i <= |E\F|/2`,

which is (3).

The implication (3)=>(2) is exactly Edmonds' two-base packing theorem: a rank-three matroid has two disjoint bases iff `2 r(F)+|E\F|>=2r(E)=6` for every `F`. (This standard statement was source-checked during the run against a matroid base-packing reference; no special representability assumption is needed.)

Finally, if `S,T` are disjoint bases, put probability `1/2` on each. Then every element occurs with marginal at most `1/2`, proving (2)=>(1). QED.

### Corollary 3.2 (exact physical collapse when half-cap feasibility fails)

If the half-cap feasible set is empty, then at least one of the following holds:

- all but at most **one** nonzero physical row lie in a common two-dimensional row subspace;
- all but at most **three** nonzero physical rows lie in a common one-dimensional row subspace;
- there are at most **five** nonzero physical rows in total.

Indeed, failure of (3) gives a set `F` of rank `q=2,1,0` with `|E\F| <= 2(3-q)-1`, and replacing `F` by its closure gives the stated physical flat.

This is stronger than treating the supported triples as an arbitrary 3-uniform hypergraph: the row-volume support is a matroid base family.

## 4. Discrete fractional-packing gap

Let

`beta(M)=max sum_{S in B} w_S`

subject to `w_S>=0` and `sum_{S contains i} w_S<=1` for each physical row. The standard fractional base-packing formula gives

`beta(M)=min_{F:r(F)<3} |E\F|/(3-r(F))`.

Normalizing an optimal fractional packing gives a base distribution with `max_i alpha_i<=1/beta(M)`.

Because the rank is three and all cardinalities are integral, there is a discrete gap:

- if `beta<2`, one of the three physical collapses in Corollary 3.2 occurs;
- if `beta=2`, there is a tight flat `F` with
  `|E\F|=2(3-r(F))`;
- if `beta>2`, automatically `beta>=7/3`, hence there is a supported-triple law with
  `max_i alpha_i<=3/7`.

For the last point, if `r(F)=2,1,0` and the ratio is strictly above two, its smallest possible value is respectively `3`, `5/2`, or `7/3`.

### Tight-face identity

Suppose `beta=2` and `F` is tight. For **every** half-cap feasible law,

`|S\F|=3-r(F)` almost surely,

and every physical row in `E\F` has marginal exactly `1/2`.

Proof: every base has at least `3-r(F)` outside elements, while

`E |S\F| = sum_{i notin F} alpha_i <= |E\F|/2 = 3-r(F)`.

Thus equality holds everywhere. Since the sum of the outside marginals equals the sum of their individual upper bounds, each outside marginal is exactly `1/2`. QED.

This is the structural bridge to complementary-face Fourier rearrangement: critical half-cap collapse is not diffuse; it lives on a literal minimal-outside matroid face.

## 5. New theorem: QFORM-TIGHT-RANK2-FLAT-FOURIER-v1

Consider the most important tight-flat case. Let `F` be a physical rank-two flat and assume the only physical rows outside it are `a,b`. Let `W=span{m_i:i in F}` and

`h_a=dist(m_a,W)`, `h_b=dist(m_b,W)`.

For `i,j in F`, set

`d_ij=det Gram(m_i,m_j)`,

and

`D_F=sum_{i<j in F} d_ij`.

Assume `D_F>0`. The elementary volume factorization is

`z_{aij}=h_a^2 d_ij`, `z_{bij}=h_b^2 d_ij`.

Define the canonical pair-volume marginal inside the flat by

`beta_i = D_F^(-1) sum_{j in F, j!=i} d_ij`.

### Theorem 5.1

If every `beta_i<=1/2`, then

`G^*_{1/2}(M) >= 2 h_a h_b D_F`.

Consequently the full ambient quadratic form, with arbitrary same-bank quadratic curvature and all affine terms retained, satisfies

`||p_Q||_infinity <= 6 sqrt(e) [2 h_a h_b D_F]^(-1/6)`,

and `p_Q` has a representative in `C_0(R)`.

### Proof

By the tight-face identity, any half-cap feasible law must use exactly one of `a,b` in every supported triple and must satisfy `alpha_a=alpha_b=1/2`. Define

`p_{aij}=d_ij/(2D_F)`, `p_{bij}=d_ij/(2D_F)`.

The outside marginals are exactly `1/2`; the flat-row marginals are exactly the `beta_i`, hence are at most `1/2`. This law is feasible.

Within each outside side it is the Gibbs law proportional to the corresponding determinant weight. Its determinant-entropy currency is therefore

`2 sqrt( (h_a^2 D_F)(h_b^2 D_F) ) = 2 h_a h_b D_F`.

Insert this law into the already-proved half-row-cap product-Fourier theorem. QED.

The important point is that this certificate remains stable when the two outside carriers become almost parallel to one another modulo the rank-two flat; it uses the two complementary one-carrier faces rather than a determinant involving both carriers simultaneously.

## 6. Genuinely rotated indefinite stress family with explicit constants

Use four physical flat rows

`f1=(1,0,0)`,
`f2=(0,1,0)`,
`f3=(3/5,4/5,0)`,
`f4=(-4/5,3/5,0)`.

They are the union of two orthonormal bases of the plane, so their pair-volume weights have total

`D_F=4`,

and every canonical pair-volume marginal is exactly `1/2`.

Take

`a=(0,0,2)`, `b_delta=(delta,2delta,2)`

and right-multiply all six rows by the dense orthogonal Householder matrix

`V=(1/7)[[6,-2,-3],[-2,3,-6],[-3,-6,-2]]`.

For `0<delta<=1` every displayed physical crossing entry is nonzero. Right rotation changes neither row Gram determinants nor singular values. Both outside heights above the flat are exactly two, so Theorem 5.1 gives the **delta-independent** exact tight-face currency

`G^*_{1/2}(M_delta)=32`.

Equality holds because every half-cap feasible law is confined to the tight face, while the Gibbs law on that face has all six physical row marginals exactly `1/2`.

Therefore

`||p_Q||_infinity <= 6 sqrt(e) 32^(-1/6)`

`= 5.551881163803895...`,

and `p_Q in C_0(R)`.

### Full target-valid dense symmetric matrix

Let `epsilon=1/100` and form

`A_delta = [[epsilon J_6, M_delta],[M_delta^T, epsilon J_3]]`.

Every physical entry is nonzero. Before the `epsilon` perturbation, the nonzero eigenvalues are `+/-` the three singular values of `M_delta`. Since

`M_delta^T M_delta = V^T [ diag(2,2,4) + b_delta^T b_delta ] V >= 2 I_3`,

all three singular values are at least `sqrt(2)`. The same-bank perturbation has operator norm at most `6/100=3/50`; Weyl therefore leaves at least three positive and three negative eigenvalues with absolute value at least

`sqrt(2)-3/50 > 1`.

Thus this is a fully dense, genuinely rotated, indefinite family satisfying the owner's exact spectral hypothesis.

## 7. Actual partner application: fleet02/B04 pair-anchored E3 theorem

Fresh designated partner source read in this run:


That completed result states that for a physical pair `a,b`, with pair-anchored third volume

`W_ab=sum_{r notin {a,b}} det Gram(m_a,m_b,m_r)>0`,

one has

`||p_Q||_infinity <= 3*2^(5/6) W_ab^(-1/6)`

for arbitrary ambient same-bank curvature/affine terms.

For the same stress family,

`a x b_delta = (-4 delta, 2 delta, 0)`.

Because the four flat rows form a unit-norm tight frame with frame operator `2 I_2`,

`W_ab = 2 ||a x b_delta||^2 = 40 delta^2`.

At `delta=1/100`,

`W_ab=1/250`,

so the completed partner theorem gives exactly

`||p_Q||_infinity <= 3*2^(5/6)*(1/250)^(-1/6) = 6 sqrt(5)`

`=13.416407864998739...`.

The new tight-flat rearrangement theorem gives `5.551881163803895...` on the **same matrix**, an improvement factor `2.416551700073931...`. More structurally, as `delta -> 0`, the partner pair-anchored E3 certificate deteriorates like `delta^(-1/3)` and disappears at `delta=0`, while the new complementary-face currency remains exactly `32`.

This comparison is not a claim that the partner theorem is globally weaker; it shows that the new mechanism pays a different, genuinely complementary near-parallel-carrier regime.

## 8. Exact arithmetic checks

For `delta=1/100`, the rotated crossing is

`M = [[6/7,-2/7,-3/7],
      [-2/7,3/7,-6/7],
      [2/7,6/35,-33/35],
      [-6/7,17/35,-6/35],
      [-6/7,-12/7,-4/7],
      [-299/350,-299/175,-83/140]]`.

All entries are nonzero. Exact symbolic checks give

`sum z_S = E_3(M)=8001/250`,

`tight one-outside mass through a =16`,
`tight one-outside mass through b =16`,
`pair-anchored mass W_ab=1/250`.

The normalized tight-face Gibbs law has every one of the six physical row marginals exactly `1/2`; hence `G^*_{1/2}=32` exactly.

The exact checks and a reproducible script are saved beside this report.

## 9. What this does and does not close

This run does **not** prove the full three-large-eigenvalue conjecture. It closes an exact combinatorial ambiguity in the half-row-cap route and pays a concrete tight-rank-two-flat branch with a stable product-Fourier estimate.

The first unpaid implication is now:

`QFORM-WEIGHTED-BASEPACKING-TO-HUB-OR-CURRENCY-v1`.

Starting from a literal cross block whose determinant-entropy currency is small, use the new packing trichotomy as follows:

- `beta<2`: route the explicit physical collapse (rank-two flat plus <=1 outside row, rank-one flat plus <=3 outside rows, or <=5 nonzero rows) into an already-paid hub/rank-two/pair/square-bank receiver;
- `beta=2`: treat the remaining tight rank-one/rank-zero faces and the tight rank-two case when an internal pair-volume marginal is >1/2;
- `beta>=7/3`: exploit the uniform support-level cap `3/7` together with determinant weights to prove target-scale currency or force a weighted heavy-basis/hub endpoint.

The unresolved issue is quantitative determinant **weight** concentration, not support combinatorics. No small rough quadratic remainder has been deleted, and no rotated coordinate has been treated as independent.

## 10. Source/correction discipline

Fresh control and current research/corrections were read before publication. The argument does not use the refuted pointwise van-der-Corput claim, arbitrary-joint coarea claim, conditional projection-density moment claim, bare-square plus half-Riesz shortcut, or Monte Carlo extremality. It uses only original-coordinate row determinants, matroid packing structure, the already-proved half-row-cap product-Fourier receiver, and one completed designated partner theorem at the explicit inequality above.

Repository transport is not native brain ingestion. Status remains `WITHOUT_VERIFIED_BRAIN` unless a later authenticated native receiver actually retrieves and uses this run.