SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T08:12:27Z.
attacking: literature-to-proof transfer for the latest circular-frame N3 survivor; apply the completed account02/B18 null-pivot theorem to its exact coloop endpoint and prove that no invertible spectral reparametrization can manufacture the missing scalar/pair source separation at finite shear.

# account01/B18 r27 — circular-frame endpoint payment and invariant source-separation barrier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Literature-to-proof transfer  
**Run:** `20260923T081227Z-qform-B18-a01-r27`  
**Classification:** `PROVED SUPPORTING TARGET-LEVEL ENDPOINT + STRUCTURAL NO-GO`; full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction boundary

The target remains: for arbitrary independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite essential density bound for `X^T A X`. Continuity is separate.

This report does **not** use any of the known false interfaces: no independence after spectral rotation, no arbitrary-joint 3D coarea inequality, no positive moment of a worst conditional projection cap, no pointwise law-uniform Fresnel decay, no perturbative deletion of a small coefficient, and no fixed-good-minor extraction. In particular, the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` is decisive below: a bounded conditional scalar density is not promoted to genuine scalar/pair independence.

## 2. Source ledger and hypothesis matching

### 2.1 Latest designated partner construction

Latest completed account02/B18 report consumed:

- repository snapshot containing the report: `yspennstate/math-open-problems@5368af077ca929e49b8dc8adeb3e0cefad85f827`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T072225Z-account02-B18-QFORM-auto11/REPORT.md`.

Its `QFORM-CIRCULAR-FRAME-PLANAR-BANK-BARRIER-v1` uses, for `m>=5`,

`theta_j=2 pi j/m`,

`v_j=(1/sqrt(m), sqrt(2/m) cos theta_j, sqrt(2/m) sin theta_j)`,

so `V^T V=I_3` and every row has leverage `3/m`. With `n=e_1` and the Schur-isotropic shear matrix from that report, the resulting physical form has nonzero spectrum exactly `{-1,1,1}` for every shear. The partner proves that every exact two-plane bank contains at most two rows and hence has Pluecker currency at most `4/m^2`. Thus exact-plane extraction cannot close this family uniformly.

### 2.2 Completed account02/B18 analytic theorem actually applied

Canonical source:

- `yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T013147Z-bf13c29b/REPORT.md`;
- theorem `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`.

If `S` has density cap `K`, is genuinely independent of a pair `(C,D)` with arbitrary joint density cap `M`, and

`T=2 beta S C + alpha C^2 + 2 delta C D + gamma D^2`,

with `beta,gamma !=0`, then

`||p_T||_infinity <= 3 (2 M K)^(2/3) |beta^2 gamma|^(-1/3)`.       (2.1)

The pair coordinates may be dependent. Genuine independence is required only between `S` and the whole pair.

### 2.3 Primary projection theorem

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1 (Israel J. Math. 216 (2016)). The primary statement says that for a product probability density `prod_i f_i` with every `||f_i||_infinity<=1`, every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. No moment, support, centering, iid, log-concavity or smoothness hypothesis is imposed. Therefore every two-dimensional orthogonal projection of the original product source has joint density cap at most `2`. This theorem is used at equation (4.2) below.

Primary URL checked this run: `https://arxiv.org/abs/1507.07949`.

### 2.4 Other primary literature checked

T. Juskevicius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190, Theorem 1 and Corollary 1, give sharp maximum-density/small-ball comparison for sums of **independent** bounded-density random vectors by centered uniform balls. The hypotheses are valuable for genuine disjoint-bank sums, but they do not make the three circular spectral projections independent and therefore do not by themselves pay the finite-shear survivor.

E. Kosov, *Oscillatory integrals with polynomial phase and regularity of distributions*, arXiv:2511.02679, Theorems 1.6--1.7, gives dimension-free fractional regularity for polynomial images of product measures whose one-dimensional densities have bounded variation. That BV hypothesis is absent from the owner target; an arbitrary cap-one density may have arbitrarily large or infinite BV because of fragmented support. Hence the result cannot be imported as a full-target theorem. This is a hypothesis mismatch, not a search-based novelty claim.

No exact prior theorem matching all owner quantifiers was found in this targeted check.

## 3. Circular frame and full-spark identity

Let

`a_j=1/sqrt(m)`,
`b_j=sqrt(2/m) cos theta_j`,
`c_j=sqrt(2/m) sin theta_j`,

and write `a,b,c in R^m` for the three coefficient columns. Root-of-unity identities give

`||a||_2=||b||_2=||c||_2=1`,
`<a,b>=<a,c>=<b,c>=0`.                                             (3.1)

Thus for the residual product vector `X=(X_1,...,X_m)`,

`A0=<a,X>`, `C=<b,X>`, `D=<c,X>`                                  (3.2)

are the three coordinates of an orthogonal projection, although they are generally dependent.

### Lemma 3.1 — full spark

For `m>=5`, every three distinct rows

`v_j=(a_j,b_j,c_j)`

are linearly independent.

**Proof.** After multiplying columns by nonzero constants, the determinant is that of the three vectors

`(1, cos theta_i, sin theta_i)`, `(1, cos theta_j, sin theta_j)`, `(1, cos theta_k, sin theta_k)`.

A zero determinant would say that the three distinct points `(cos theta,sin theta)` on the unit circle are collinear. A line intersects the circle in at most two points. Hence the determinant is nonzero. QED.

The property is invariant under every deterministic `G in GL_3`: for any triple `S`,

`det((V G)_S)=det(V_S) det(G) !=0`.                                (3.3)

It is also invariant under the finite-shear diagonal scaling `diag(t,1,1)` whenever `t>0`.

## 4. Exact target-valid coloop endpoint is uniformly paid

Define the exact endpoint form

`Q_* = 2 X_0 C + D^2`,                                             (4.1)

where `X_0,X_1,...,X_m` are arbitrary independent cap-one inputs and `C,D` are as in (3.2).

Because `b,c` are orthonormal, LPP with `k=2` gives

`boxed: ||p_(C,D)||_infinity <=2.`                                 (4.2)

Also `X_0` is an original coordinate disjoint from the residual source, hence is genuinely independent of the **whole pair** `(C,D)`, and `||p_(X_0)||_infinity<=1`.

Apply the completed account02/B18 theorem (2.1) with

`S=X_0`, `K=1`, `M=2`, `beta=1`, `alpha=delta=0`, `gamma=1`.

Then

`boxed:
 ||p_(Q_*)||_infinity
 <= 3 * 4^(2/3)
 = 3 * 2^(4/3)
 = 7.559526299369239... .`                                        (4.3)

This is an actual target-level inequality, not a limiting heuristic.

To verify the spectral hypothesis, embed `e_0,b,c` as three orthonormal vectors in the full physical coordinate space. Relative to this orthonormal basis, the quadratic matrix of (4.1) is

`H_*=[[0,1,0],[1,0,0],[0,0,1]]`,                                  (4.4)

whose eigenvalues are exactly

`{-1,1,1}`.                                                        (4.5)

Hence for every `m>=5`, every admissible collection of input laws, and every circular frame above, (4.3) pays a genuine matrix in the owner's exact target class.

More generally, the same argument pays

`2 beta X_0 C + alpha C^2 + 2 delta C D + gamma D^2`

at

`3*4^(2/3)|beta^2 gamma|^(-1/3)`                                  (4.6)

whenever `beta,gamma` are nonzero. Equation (4.3) is the normalized target instance.

**Continuity:** not asserted from this argument. The result is an essential `L^infinity` density bound. The owner asks that continuity be tracked separately, so no continuity claim is imported from an unrelated Fourier branch.

## 5. New invariant no-go: finite shear cannot be repaired by a spectral change of basis

The endpoint `Q_*` is easy precisely because the first residual spectral coordinate `A0` has disappeared. The latest partner's finite-shear family has, after harmless notation,

`Q_r = 2 (k X_0 + t A0) C + D^2`,

where

`k=r/sqrt(1+r^2)`, `t=1/sqrt(1+r^2)`,                              (5.1)

so `t>0` for every finite `r` and `k^2+t^2=1`.

A tempting repair is to make an invertible deterministic change among the three active residual spectral coordinates and hope that one transformed scalar uses a set of original coordinates disjoint from those used by a transformed two-dimensional pair. That is impossible.

### Theorem 5.1 — `QFORM-CIRCULAR-FRAME-NO-EXACT-1PLUS2-SOURCE-SPLIT-v1`

Let `m>=5`, let the residual rows be the circular rows `v_j`, and let `t>0`. After **any** invertible deterministic change of the three active residual coordinates, there is no partition of the residual original-coordinate indices into disjoint sets `I,J` such that

1. the transformed scalar coordinate depends only on `{X_i:i in I}`, and
2. the transformed two-dimensional coordinate depends only on `{X_j:j in J}`.

Equivalently, no `GL_3` reparametrization turns the finite-shear residual source into an exact independent `1+2` source split.

**Proof.** The scaled residual rows

`u_j=(t a_j,b_j,c_j)`                                               (5.2)

are full spark by Lemma 3.1 because `t>0`. Let `G in GL_3` be any further deterministic change of active spectral coordinates. The rows `w_j=u_j G` remain full spark by (3.3).

If the first transformed coordinate is supported only on `I` and the last two only on the disjoint complement `J`, then every `w_i`, `i in I`, has its last two coordinates zero and hence lies on the one-dimensional scalar axis `L`. Every `w_j`, `j in J`, has first coordinate zero and hence lies in the two-dimensional pair plane `P`.

Full spark implies that **at most one** row can lie on any fixed line: two proportional rows together with any third row would be linearly dependent. Full spark also implies that **at most two** rows can lie in any fixed plane: any three rows in that plane would be dependent. Therefore

`|I|<=1`, `|J|<=2`, so `m=|I|+|J|<=3`,                             (5.3)

contradicting `m>=5`. QED.

### Consequence

The obstruction survives every deterministic spectral rotation or invertible reparametrization. Thus the finite-shear circular survivor cannot be fed into (2.1) merely by "choosing a better spectral basis". The exact endpoint `t=0` is genuinely singular from the source-separation viewpoint: the `A0` coordinate becomes inactive, and the original scalar `X_0` is then independent of the active pair `(C,D)`.

This also explains why the live correction against small-coefficient perturbation must be respected. The bound (4.3) at `t=0` cannot be extended to `0<t<<1` merely by saying that `t A0` is small; arbitrary fragmented cap-one inputs need not be stable in output total variation under such coefficient perturbations.

## 6. What is closed and what remains open

**Closed this run:** the exact coloop endpoint of the latest account02/B18 circular N3 barrier is uniformly paid for all dimensions and all owner-admissible input laws:

`||p_(2 X_0 C + D^2)||_infinity <= 7.559526300`,                   (6.1)

with physical nonzero spectrum exactly `{-1,1,1}`.

**New structural fact:** for every finite shear in the same circular full-spark family, no invertible change of the three active residual spectral coordinates can create the genuine independent scalar/dependent-pair interface required by the account02/B18 null-pivot theorem.

**Still unpaid:** the finite-shear circular family

`Q_r=2(k X_0+t A0)C+D^2`, `0<t<1`,                                (6.2)

in the large-shear regime uniformly as `t downarrow0`, and more generally the non-source-separated N3 branch. Any successful continuation must exploit the fact that `(A0,C,D)` is a **linear projection of an original product law**, not merely a bounded arbitrary 3D density. The arbitrary-joint coarea and conditional-cap substitutions are already refuted.

A useful next theorem would therefore be a dependence-safe estimate for (6.2) that uses product-linear provenance directly, or an exhaustive structural routing showing that every such full-spark near-coloop packet enters another already-paid branch. A pure spectral-basis source split cannot supply that theorem by Theorem 5.1.

## 7. Literature conclusion

The primary source check produced no exact prior theorem matching arbitrary cap-one, non-iid, fragmented marginals and the three-large-eigenvalue rotated quadratic target. LPP applies exactly to the linear projection step and is used in (4.2). Juskevicius--Lee applies exactly to independent bounded-density sums but does not create independence among the circular spectral coordinates. Kosov's 2025 product-measure polynomial regularity theorem requires BV input densities, a strictly stronger regularity hypothesis than the owner allows. Search absence is not used as a novelty claim.

Full QFORM status: **OPEN / NOT PROVED**.
