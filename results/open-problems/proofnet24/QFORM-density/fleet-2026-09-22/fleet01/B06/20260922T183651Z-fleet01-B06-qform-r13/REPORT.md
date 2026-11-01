# QFORM curved-fiber report: volume-sampled two-bank closure and the exact high-leverage interface

Programme: `QFORM-DENSITY-3EIG-20260922`.
Worker: `fleet01/B06`.
Run: `20260922T183651Z-fleet01-B06-qform-r13`.
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / INTERMEDIATE_INTERFACE_REFUTED / FULL_TARGET_OPEN`.
Execution status: `WITHOUT_VERIFIED_BRAIN`.

The full target remains open: for arbitrary independent real coordinates with probability densities at most one and arbitrary symmetric A with at least three eigenvalues of modulus at least one, prove a dimension-independent density bound for X^T A X (and separately continuity), or produce a genuine counterexample. Nothing below discards additional spectral directions in the full target.

## Dependencies actually used

1. **fleet02/B06**, `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical source
   `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.
   If C has orthonormal columns in R^{m x k} and Y=C^T X for independent cap-one coordinates, then
   `||p_Y||_infinity <= exp(k/2)`.

2. `QFORM-CROSSBLOCK-RANK-r-FOURIER-v1`, canonical source
   `yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc`,
   `proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md`.
   For an original-coordinate partition S,T whose cross block has rank r>2 and product Delta of all nonzero singular values,
   `||p_Q||_infinity <= (2r/(r-2)) Delta^(-1/r)`, with a continuous density.

The current correction set was respected. In particular no arbitrary-joint 3D coarea bound, no conditional projection positive-moment bound, no post-rotation independence, no unrestricted fiber supremum, and no direct Pluecker-to-physical-pivot identification are used.

## 1. Compact conditional route

For exact rank three, write

`A = R Lambda R^T`, `R^T R=I_3`, `min_j |lambda_j|>=1`,

and let `r_i` be the physical rows, with leverage `c_i=||r_i||^2` and `alpha=max_i c_i`.

The desired exact-rank-three proof would follow from two complementary branches:

* **two-bank branch:** produce an original-coordinate partition S,T for which both three-dimensional frame determinants survive quantitatively, then apply the completed rank-three cross-block theorem;
* **heavy-row branch:** if one physical row is too large, preserve the original product law through the one-heavy-row disintegration and prove the remaining curved trace estimate from that stronger provenance.

This report proves the first branch all the way up to `alpha<1/3`, derives the exact product-preserving interface for the second branch using the designated partner theorem, and gives a rigorous counterexample showing that the resulting marginal/conditional density caps alone cannot close the second branch.

## 2. Volume sampling of a Parseval three-frame

For every three-element set I of physical coordinates define

`w_I = det(R_I)^2`.

Cauchy--Binet gives

`sum_{|I|=3} w_I = det(R^T R)=1`,

so `w` is a probability distribution on triples.

### Lemma 2.1 (exact one-coordinate marginals)

For each physical coordinate i,

`sum_{I: i in I} w_I = c_i`.

**Proof.** Let D_t be diagonal with entry t at i and one elsewhere. The matrix determinant lemma gives

`det(R^T D_t R)=det(I_3+(t-1) r_i^T r_i)=1+(t-1)c_i`.

On the other hand, Cauchy--Binet applied to `D_t^(1/2) R` gives

`det(R^T D_t R) = sum_{I not containing i} w_I + t sum_{I containing i}w_I`
`=1+(t-1) sum_{I containing i}w_I`.

Compare coefficients of t. QED.

Let I,J be independent triples drawn from w. Then

`E |I intersect J| = sum_i P(i in I)P(i in J)=sum_i c_i^2`
`<= alpha sum_i c_i = 3 alpha`.

Hence, for `alpha<1/3`,

`P(I intersect J = empty) >= 1-3 alpha`.                                    (2.1)

No determinantal-process machinery is needed; (2.1) follows from Lemma 2.1 and Markov's inequality for the nonnegative integer `|I intersect J|`.

## 3. A two-bank determinant identity

Let S be a random Bernoulli half-set of physical coordinates: each coordinate is put in S independently with probability 1/2, and T=S^c. Put

`G_S = R_S^T R_S = sum_{i in S} r_i^T r_i`,
`G_T = I_3-G_S`.

Cauchy--Binet gives the exact expansions

`det G_S = sum_{I subset S, |I|=3} w_I`,
`det G_T = sum_{J subset T, |J|=3} w_J`.

Therefore

`E_S[det G_S det G_T]`
`= sum_{I,J} w_I w_J P(I subset S, J subset T)`
`= 2^(-6) sum_{I intersect J=empty} w_I w_J`
`= (1/64) P(I intersect J=empty)`.

Combining with (2.1),

`E_S[det G_S det G_T] >= (1-3 alpha)/64`.                    (3.1)

Thus some deterministic original-coordinate partition S,T satisfies

`det G_S det G_T >= (1-3 alpha)/64`.                         (3.2)

This is the key weighted replacement for selecting one favorable physical triple. It aggregates all volume-carrying triples before any reciprocal curvature payment.

## 4. The exact-rank-three diffuse range extends to alpha<1/3

### Theorem 4.1 (`QFORM-VOLUME-SAMPLED-TWO-BANK-v1`)

Assume `A=R Lambda R^T` has exact rank three, `R^T R=I_3`, and `min_j |lambda_j|>=1`. If

`alpha=max_i ||r_i||^2 < 1/3`,

then for every permitted product input law, `Q=X^T A X` has a continuous density and

`||p_Q||_infinity <= 12 (1-3 alpha)^(-1/6) |det Lambda|^(-1/3)`
`                 <= 12 (1-3 alpha)^(-1/6)`.                 (4.1)

**Proof.** Choose S,T as in (3.2). Since the determinant product is positive, `R_S` and `R_T` both have column rank three. The original-coordinate cross block is

`B=A[S,T]=R_S Lambda R_T^T`.

Write the thin polar factorizations

`R_S=P G_S^(1/2)`, `R_T=U G_T^(1/2)`,

where P,U have orthonormal columns. Hence the three nonzero singular values of B are those of

`G_S^(1/2) Lambda G_T^(1/2)`.

Their product is exactly

`Delta = |det Lambda| sqrt(det G_S det G_T)`
`>= |det Lambda| sqrt((1-3 alpha)/64)`
`= |det Lambda| sqrt(1-3 alpha)/8`.

Apply `QFORM-CROSSBLOCK-RANK-r-FOURIER-v1` with r=3:

`||p_Q||_infinity <= 6 Delta^(-1/3)`
`<= 12 (1-3 alpha)^(-1/6)|det Lambda|^(-1/3)`.

The same source gives continuity. QED.

A clean fixed branch is

`alpha<=1/4  =>  ||p_Q||_infinity <= 12*2^(1/3) < 15.12`.    (4.2)

Thus the previous sufficiently-diffuse cutoff `alpha<=1/12` is not intrinsic: exact rank three is now closed throughout every fixed leverage range strictly below 1/3. The bound only deteriorates with the sixth root of the distance to 1/3.

## 5. Exact high-row product-provenance interface

Now let one row i have leverage `c=c_i>0`. Put

`e=r_i/sqrt(c) in R^3`

and choose a 3-by-2 isometry V with range `e^perp`. Let `X_-` denote all original coordinates except i and define

`Y = V^T R_-^T X_- in R^2`,
`Z = e^T R_-^T X_-`,
`T = sqrt(c) X_i + Z`.

Because `r_i^T r_i=c e e^T`,

`(R_- V)^T(R_- V) = V^T(I_3-c e e^T)V = I_2`.

Apply the designated partner theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` at k=2 to the genuine original-coordinate product source `X_-`:

`||p_Y||_infinity <= e`.                                    (5.1)

This is an actual use of the partner result, not a citation-only dependency.

Moreover `X_i` is independent of the pair `(Z,Y)`. Conditional on `Y=y`, the law of T is the convolution of the scaled original coordinate `sqrt(c) X_i`, whose density is bounded by `c^(-1/2)`, with the conditional law of Z. Hence for almost every y,

`||p_(T|Y=y)||_infinity <= c^(-1/2)`.                        (5.2)

Finally, with the orthogonal matrix O=[e V],

`Q = (T,Y)^T H (T,Y)`, `H=O^T Lambda O`,                    (5.3)

so H has exactly the original three eigenvalues. Equations (5.1)--(5.3) are a product-preserving one-heavy-row compression. For example, if `c>1/4`, then the marginal Y has density cap e and every conditional scalar T|Y has density cap <2.

This interface is stronger than an arbitrary three-dimensional joint-density cap, because the conditional cap (5.2) comes from a surviving independent physical coordinate. Nevertheless, the next subsection shows that **these two caps by themselves still do not control an indefinite quadratic trace**.

## 6. A source-valid falsifier for cap-only high-row closure

### Proposition 6.1 (`QFORM-SEMIPRODUCT-CAP-ONLY-FALSE-v1`)

There is no universal C with the following property: whenever a scalar T has conditional density cap one given a two-dimensional Y, `||p_Y||_infinity<=1`, and H has eigenvalues `(1,1,-1)`, the density of `(T,Y)^T H(T,Y)` is bounded by C. This remains false even when T and Y are independent.

**Construction.** Fix `0<delta<=1/2`. Use coordinates

`s=y_1+y_2`, `d=y_1-y_2`,

for which `y_1^2-y_2^2=sd` and `dy_1 dy_2=(1/2) ds dd`. Define

`E_delta = {1<=s<=exp(4/delta), -delta/(2s)<=d<=0}`.

Its area is exactly

`(1/2) int_1^(exp(4/delta)) delta/(2s) ds =1`,

and throughout E_delta,

`-delta/2 <= y_1^2-y_2^2 <=0`.

Let Y have density `1_(E_delta)`, and independently let T be Uniform[-1/2,1/2]. Then `||p_Y||_infinity=1` and `||p_(T|Y=y)||_infinity=1`. For

`Q=T^2+Y_1^2-Y_2^2`,

whenever `|T|<=sqrt(delta/2)` one has

`Q in [-delta/2,delta/2]`.

Therefore

`P(Q in [-delta/2,delta/2]) >= sqrt(2 delta)`.

If Q had density cap C, the left side would be at most `C delta`, forcing

`C >= sqrt(2/delta) -> infinity`.

QED.

This is **not** a counterexample to the owner conjecture: the two-dimensional Y in this construction is an arbitrary dependent joint law, not shown to be an orthogonal projection of an independent cap-one product source. It refutes only the tempting interface that throws away the original product-projection provenance after (5.1)--(5.2).

## 7. What changed and the first unpaid implication

The exact-rank-three geometry is now quantitatively split as follows.

* If `max_i c_i<1/3`, Theorem 4.1 closes the branch by a volume-sampled original-coordinate two-bank partition. In particular `max_i c_i<=1/4` gives the explicit continuous bound `<15.12`.
* Therefore any still-unpaid exact-rank-three configuration may be forced into a genuinely high-leverage physical row after choosing a fixed cutoff below 1/3.
* In that high-row branch, the partner theorem gives the exact 2D product-projection marginal cap (5.1), while the independent heavy physical coordinate gives the conditional scalar cap (5.2).
* Proposition 6.1 proves that one must retain more than those two numerical caps: the **orthogonal-product-projection provenance of `(Z,Y)` must enter the curved trace estimate itself**.

The first exact missing implication for this worker is therefore

`QFORM-HIGH-ROW-PRODUCT-TRACE-v1`:

For the special disintegration (5.1)--(5.3) arising from an actual Parseval frame and an original coordinate product law, establish a translation-uniform curved-trace/small-ball estimate in the near-isotropic-pivot regime, using the full joint projection structure of `(Z,Y)` rather than replacing it by `||p_Y||_infinity` and `||p_(T|Y)||_infinity`.

This is compatible with the existing scalar-pivot/rank-two half-Riesz theorem when the physical diagonal is quantitatively nonzero and with the completed zero-pivot subcases, but it does not assume either branch covers the near-zero transition.

After exact rank three is exhausted, the full owner target still needs an arbitrary-additional-spectrum bridge. The present report therefore does not claim the full theorem.

## Status

* Essential bounded density: proved only in Theorem 4.1's exact-rank-three leverage scope.
* Continuity: proved in Theorem 4.1's scope through the cross-block Fourier theorem.
* Full arbitrary-rank target: OPEN.
* Universal counterexample: NOT found.
* Intermediate cap-only high-row closure: rigorously refuted by Proposition 6.1.
