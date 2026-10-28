SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B13, 2026-09-22T18:20:42Z.
attacking: group-before-condition control for an arbitrary high-cardinality rank-two cross bank, after the exact extreme-product reduction.

# account03/B13 — aggregate zero-pair cross-bank theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T182042Z-account03-B13-qform-r14`  
**Assignment:** Extremal product laws  
**Classification:** `PROVED_SUPPORTING_THEOREM / FULL-RANK_DIFFUSE-CROSSBANK_BRANCH / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full quadratic-form bounded-density conjecture remains **OPEN / NOT PROVED**. The full continuous-density conclusion remains open. The result below is a target-valid scoped theorem for arbitrary ambient rank and arbitrary extra spectrum.

## 1. Sources and live corrections actually used


The designated partner `account04/B13` completed the fixed-volume random-set representation and continuity transfer at the source-pinned report

`yspennstate/math-open-problems@722a87d180720473e3c3e08010d62caedf298484:proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T171018Z-b13-fixed-volume-mixture-r4/REPORT.md`.

It proves that every one-dimensional probability density `0<=f<=1` is an exact barycenter of indicators `1_E` with `|E|=1`, independently across coordinates. Consequently every product law is an exact mixture of arbitrary unit-measure product indicators. It also proves that a uniform continuous output-density bound on all such indicator components transfers, with no constant loss, to all admissible product densities.

A second completed input is the two-dimensional product-projection theorem from `account02/B11`, source

`yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2:proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260922T135203Z-b11-qform-6080e0b3/REPORT.md`.

If independent cap-one coordinates are mapped to `R^2` by coefficient vectors `b_k` satisfying `sum b_k b_k^T=I_2`, the resulting joint density is at most `e`. By target-plane whitening, for any rank-two coefficient matrix with Gram matrix `G`, the joint density cap is `e/sqrt(det G)`.

## 2. Sharp two-dimensional reciprocal-radius lemma

### Lemma 2.1 — `QFORM-LINF2-RECIPROCAL-RADIUS-v1`

Let `Y=(Y_1,Y_2)` have a probability density `g` satisfying `0<=g<=M`. Put `R=max(|Y_1|,|Y_2|)`. Then

`boxed( E R^(-1) <= 4 sqrt(M). )`

The constant `4` is sharp under only the density-cap and mass-one hypotheses.

Indeed, `P(R<=r)<=min(1,4Mr^2)`. Layer cake gives

`E R^(-1)=int_0^infinity P(R<1/s) ds`
`<=2sqrt(M)+int_(2sqrt(M))^infinity 4M s^(-2) ds=4sqrt(M)`.

Equality is attained by the density `M` on the centered square of area `1/M`. This is the step that lets the entire two-dimensional cross bank be aggregated before any reciprocal local-minor cost is paid.

## 3. Main arbitrary-ambient theorem

### Theorem 3.1 — `QFORM-ZERO-PAIR-CROSSBANK-AGGREGATE-v1`

Let `A` be any real symmetric `n x n` matrix. Choose distinct physical coordinates `i,j` such that the entire physical `2x2` principal pair is zero:

`A_ii=A_jj=A_ij=0`.

Let `K={1,...,n}\{i,j}` and form the two-row original-coordinate cross bank

`C=[(A_ik)_(k in K);(A_jk)_(k in K)]`.

Define

`Delta_ij:=det(C C^T)=sum_(k<l, k,l in K)(A_ik A_jl-A_il A_jk)^2`.

Assume `Delta_ij>0`. Then for arbitrary independent real coordinates with probability densities bounded by one, the law of `Q=X^T A X` has a **continuous** density and

`boxed( ||p_Q||_infinity <= 2 sqrt(e) Delta_ij^(-1/4). )`

No rank assumption on `A` is made. All additional spectrum and all coefficients among the remaining coordinates are arbitrary. No support, moment, centering, connectedness, fragment-count, log-concavity, or post-rotation independence assumption is used.

### Proof on one extreme product component

Use the assigned account04/B13 reduction and first take each input density to be `1_(E_r)` for arbitrary measurable `|E_r|=1`. Write `Z=X_K`. Because the selected physical pair is identically zero, conditioning on `Z=z` gives

`Q=c(z)+U(z)X_i+V(z)X_j`,

where

`U=2 sum_(k in K) A_ik X_k`,
`V=2 sum_(k in K) A_jk X_k`.

For fixed `z` with `U,V !=0`, the density of `U X_i+V X_j` is a convolution of two scaled probability densities, hence

`||p_(Q|Z=z)||_infinity<=min(|U|^(-1),|V|^(-1))=1/max(|U|,|V|)`.

Aggregate the entire cross bank. Coordinate `k` contributes `b_k=2(A_ik,A_jk)^T` to `(U,V)`, so

`G=sum_k b_k b_k^T=4 C C^T`,
`sqrt(det G)=4 sqrt(Delta_ij)`.

Whitening only the two-dimensional target plane and applying the completed account02/B11 product-projection theorem gives

`||g_(U,V)||_infinity<=e/[4 sqrt(Delta_ij)]=:M`.

Thus `(U,V)` is absolutely continuous and its coordinate axes are null. Averaging the conditional density bound and applying Lemma 2.1 gives

`||p_Q||_infinity<=E[1/max(|U|,|V|)]<=4sqrt(M)=2sqrt(e)Delta_ij^(-1/4)`.

For almost every `z`, both slopes are nonzero and the conditional output density is a translate of a convolution of two `L^1` functions, hence continuous. It is dominated by the integrable function `1/max(|U|,|V|)`, so dominated convergence gives continuity of the extreme-component output density.

Finally apply the designated partner theorem account04/B13: every arbitrary cap-one product law is an exact mixture of these unit-volume indicator products, and its continuity-transfer lemma averages the component densities. Since every component obeys the same bound, the original arbitrary product law has a continuous density with the identical constant. This is a direct application of the partner result to the target density inequality.

QED.

## 4. Geometric extreme-product form

For arbitrary measurable sets `|E_r|=1` and every interval `I`, Theorem 3.1 is equivalently

`boxed(|{x in E_1 x ... x E_n:x^T A x in I}|<=2sqrt(e)Delta_ij^(-1/4)|I|.)`

The sets may be unbounded and infinitely fragmented. Thus the result sits exactly after the correct extremal reduction and does not revive the refuted single-interval, bounded-diameter, or bounded-fragment shortcuts.

## 5. Why aggregation matters: exact high-cardinality target family

Let `m` be even and define

`u=m^(-1/2)(1,...,1)`,
`v=m^(-1/2)(1,...,1,-1,...,-1)`

with `m/2` plus and `m/2` minus signs. The rows `u,v` are orthonormal. Let `C` have rows `u,v` and put

`A_m=[[0_(2x2),C],[C^T,0_(mxm)]].`

The nonzero eigenvalues of this bipartite block matrix are the signed singular values of `C`, so

`spectrum_nonzero(A_m)={1,1,-1,-1}`.

This is an honest QFORM target family with four eigenvalues of modulus one and arbitrarily many physical coordinates. Here `Delta_12=det(CC^T)=1`, hence

`boxed(||p_(X^T A_m X)||_infinity<=2sqrt(e)=3.297442541400256...)`

for every admissible product law and every even `m`, and the density is continuous.

Every individual cross minor is either zero or has magnitude `2/m`. If one conditions down to a single physical pair before paying reciprocal curvature, the sharp one-minor version below gives only `2/sqrt(2/m)=sqrt(2m)`, which diverges. The aggregate theorem stays constant because it pays

`Delta_12=sum_(k<l) minor_(k,l)^2=1`

before taking a reciprocal. This is an explicit group-before-condition closure of a diffuse high-cardinality full-target family.

## 6. One-minor comparison

If only one pair `k,l` is used and

`d=|A_ik A_jl-A_il A_jk|>0`,

conditioning on every other outside coordinate gives the exact joint slope-density cap `1/(4d)`. Lemma 2.1 then gives

`||p_Q||_infinity<=2 d^(-1/2)`.

This is sharper when a genuinely heavy cross minor exists. The aggregate theorem is complementary: it can remain bounded when every individual minor tends to zero.

## 7. Scope and replacement obligation

This is not an exhaustive structural reduction from the three-large-eigenvalue hypothesis. It requires a physical pair with `A_ii=A_jj=A_ij=0` and a rank-two cross bank. The live corrections already show that a single good local block or minor cannot be assumed universally.

The next B13 implication is a near-zero-pair interpolation that still aggregates the whole cross bank before paying the residual rank-two logarithm. When `A_ij !=0`, the conditional two-coordinate law has a product/log singularity, and a cross-bank determinant alone cannot control it: rank-two collapses such as `(x_1+y_1)(x_2+y_2)` show why a third-curvature payment is necessary. A valid extension must retain the third large direction or an equivalent residual small-ball estimate; it cannot treat the nonzero pair term as a support-uniform perturbation.

Full QFORM remains **OPEN / NOT PROVED**. Full continuity remains **OPEN**, although continuity is proved in Theorem 3.1's arbitrary-ambient scoped branch.
