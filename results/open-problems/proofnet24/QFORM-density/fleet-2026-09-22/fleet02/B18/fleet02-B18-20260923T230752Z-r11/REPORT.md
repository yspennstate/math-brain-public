SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-23T23:07:52Z.
attacking: a tetrahedral four-bank exact-rank-three family, to compare the newest fleet03/B18 four-source compiler against the pinned e5f Fresnel theorem and quantify the fixed-physical-core loss.

# fleet02/B18 — diffuse four-core versus four-bank aggregation gap

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `fleet02-B18-20260923T230752Z-r11`.
Status: **NEW SUPPORTING CONSTRUCTION / PROOF-CERTIFICATE OBSTRUCTION; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

No literature-wide novelty claim is made. Search misses are not used as novelty evidence.

## First unpaid implication

The newest fleet03/B18 theorem closes a genuine four-source rank-three core with constant `592/s`, and its LPP transfer closes four exact disjoint scalar banks with constant `1184/s`. The first structural debt is therefore not the four-variable analytic receiver itself. It is to produce, from an arbitrary remaining higher-rank/no-pivot matrix, either

1. a product-preserving diffuse rank-three certificate to which the pinned Fresnel theorem applies, or
2. four disjoint original-coordinate banks carrying a rank-three effective matrix at a universal scale while retaining all same-bank/non-diagonal residual curvature.

A fixed set of four physical coordinates cannot supply this bridge in the diffuse regime: the theorem below forces the direct four-coordinate certificate to deteriorate like the reciprocal leverage even though the true density is uniformly bounded by the pinned diffuse theorem. Small operator residuals cannot simply be discarded for arbitrary unbounded inputs.

## Theorem — `QFORM-DIFFUSE-FOURCORE-VS-FOURBANK-GAP-v1`

Let `R` be an `m x 3` real matrix with orthonormal columns, `R^T R=I_3`, let `r_i` denote its rows, and set

`A=R R^T`, `ell=max_i ||r_i||_2^2`.

Assume `ell<=1/2`. For arbitrary independent real inputs with probability densities bounded by one:

### (A) Global diffuse payment

The pinned e5f Theorem F gives

`||p_(X^T A X)||_infinity <= 12`.                                (2.1)

Indeed, `A=sum_{k=1}^3 v_k v_k^T` with the columns `v_k` of `R`, `B=0`, `I={1,...,m}`, and

`G_I=sum_i r_i r_i^T=R^T R=I_3`.

The normalized leverage in Theorem F is exactly `||r_i||^2<=1/2`, while the three spectral coefficients are all one. Thus its formula

`12 (|lambda_1 lambda_2 lambda_3| det G_I)^(-1/3)`

is exactly `12` here. This is a real target inequality for arbitrary cap-one product laws; no moment, support, log-concavity, iid, or post-rotation-independence assumption is added.

### (B) Every fixed four-coordinate use of the newest partner theorem degenerates with diffuse leverage

Let `J` be any four original coordinates and let

`H_J=A[J,J]=R_J R_J^T`.

If `rank(H_J)<3`, the newest fleet03/B18 four-source rank-three theorem is unavailable on this four-coordinate core. If `rank(H_J)=3`, let `s_J` be its smallest nonzero singular value. The nonzero eigenvalues of `H_J` are the three eigenvalues of

`S_J=R_J^T R_J`.

Since `S_J` is positive semidefinite,

`3 s_J <= tr S_J = sum_{i in J} ||r_i||^2 <= 4 ell`,

hence

`boxed: s_J <= 4 ell/3`.                                         (2.2)

The fleet03/B18 theorem, applied directly to these four original variables after conditioning the rest, has displayed right-hand side

`592/s_J`.

Therefore every applicable direct fixed-four-core certificate satisfies the reverse numerical estimate

`boxed: 592/s_J >= 444/ell`.                                     (2.3)

This is a lower bound on the theorem's **certificate value**, not on the true density. Consequently, along diffuse exact-rank-three frames with `ell -> 0`, no strategy that merely selects four physical coordinates and feeds that principal block into `QFORM-FOUR-SOURCE-RANK3-COMPRESSION-v1` can produce a universal constant, although (2.1) already bounds the actual density by `12`.

This is precisely an aggregate-before-selection obstruction.

## Exact tetrahedral four-bank family

The preceding certificate gap can be saturated by a target-valid family that also admits a source-valid four-bank compression.

Let `m=4N`, `N>=2`, and partition the original coordinates into four disjoint banks `I_1,...,I_4`, each of cardinality `N`. Define

`eps_1=(1,1,1)`,
`eps_2=(1,-1,-1)`,
`eps_3=(-1,1,-1)`,
`eps_4=(-1,-1,1)`.

Every row of `R` in bank `I_k` is `eps_k/sqrt(m)`. Since

`sum_{k=1}^4 eps_k eps_k^T = 4 I_3`

and `N/m=1/4`,

`R^T R = I_3`.                                                   (3.1)

Thus

`A_m=R R^T`

is an orthogonal rank-three projection with

`boxed: spec_nonzero(A_m)={1,1,1}`.                              (3.2)

It belongs to the exact owner target for every `m`. Its physical row leverage is

`ell=3/m <=3/8<1/2`,

so the pinned result gives

`boxed: ||p_(X^T A_m X)||_infinity <=12`                         (3.3)

for every arbitrary independent cap-one input family. Because the proof provides an integrable characteristic-function majorant, this branch also has the corresponding Fourier-inversion continuous representative; continuity is ancillary and is not used below.

## Source-valid four-bank transfer

Define the normalized original-coordinate bank sums

`S_k=N^(-1/2) sum_{i in I_k} X_i`, `k=1,...,4`.                  (4.1)

The four `S_k` are genuinely independent because their defining coordinate sets are pairwise disjoint **before any rotation**.

The only external anti-concentration theorem needed here is Livshyts--Paouris--Pivovarov, Theorem 1.1. For a genuine product probability density `prod_i f_i`, with bounded one-dimensional factors, and any `k`-dimensional orthogonal marginal, it proves

`||pi_E f||_infinity <= min((n/(n-k))^((n-k)/2), 2^(k/2)) prod_i ||f_i||_infinity^(gamma_i)`,

where `gamma_i in [0,1]` and `sum gamma_i=k`. In particular, for cap-one inputs and a one-dimensional unit projection,

`||p_(<u,X>)||_infinity <= sqrt(2)`.                              (4.2)

No finite moments, bounded support, connected support, log-concavity, smoothness, iid, centering, or symmetry are hypotheses of that theorem. It bounds a marginal density; it does **not** assert independence among projected coordinates. Independence in (4.1) comes solely from the disjoint original supports.

Applying (4.2) separately inside each bank gives

`||p_(S_k)||_infinity <= sqrt(2)`.                               (4.3)

Meanwhile

`R^T X = (1/2) sum_{k=1}^4 eps_k S_k`,

and therefore

`Q=X^T A_m X=S^T K S`,

where

`K=(1/4)(eps_k dot eps_l)_(k,l)
  = I_4-(1/4)11^T`.                                               (4.4)

Hence

`boxed: spec(K)={1,1,1,0}`.                                     (4.5)

Scale `T_k=sqrt(2) S_k`. Then the `T_k` remain independent and now have density caps one; the quadratic matrix becomes `K/2`, whose three nonzero singular values equal `1/2`. The latest completed fleet03/B18 theorem therefore yields the concrete whole-line essential bound

`boxed: ||p_Q||_infinity < 592/(1/2)=1184`.                      (4.6)

Equivalently, this is its stated four-disjoint-bank corollary with original bank scale `s=1`.

The number `1184` is not competitive with the pinned diffuse value `12`; its role is structural. It proves that the four-source receiver is dimension-free **after** exact original-coordinate aggregation, whereas the same receiver necessarily loses on every fixed physical four-core.

## Exact fixed-core loss in the same family

Take any four physical coordinates `J`. Since every row has squared norm `3/m`,

`tr(R_J^T R_J)=12/m`.

If this four-core has rank three, then

`s_J <=4/m`,                                                     (5.1)

and its generic fleet03/B18 certificate has right-hand side

`592/s_J >=148 m`.                                               (5.2)

If it has rank below three, the theorem is unavailable instead.

The estimate is attained at the certificate scale. If `J` contains exactly one coordinate from each of the four banks, then by the tetrahedral identity

`R_J^T R_J=(4/m) I_3`,                                           (5.3)

so all three nonzero eigenvalues of `A_m[J,J]` equal `4/m`. The direct four-source theorem then reads

`||p_(Q | X_(J^c))||_infinity < 148 m`,                          (5.4)

uniformly in the conditioned outside values. Thus the best displayed fixed-core scale diverges linearly, while the exact same target form has the global bounds (3.3) and (4.6).

Again, (5.2)--(5.4) are statements about the proof certificate, not lower bounds on the true density.

## Why this matters for the live compiler

This family rules out a tempting misuse of the newest partner theorem:

`three large eigenvalues -> choose four original coordinates -> apply 592/s`.

The implication fails quantitatively even for the nicest exact-rank-three PSD projections. The missing operation is aggregation **before** paying reciprocal spectral scale. The tetrahedral bank variables recover a rank-three effective matrix at unit scale even though every fixed four-coordinate core lives at scale `O(1/m)`.

This is compatible with the live fixed-good-minor and cross-rank corrections. It does not assert that every QFORM matrix admits four exact scalar banks. In fact, the general higher-rank problem still contains arbitrary same-bank curvature and non-diagonal residual spectrum; those terms cannot be deleted by small operator norm when the product inputs have arbitrary unbounded supports.

A useful next structural target is therefore:

`QFORM-HIGHERRANK-GROUPED-CARRIER-TO-FOURBANK-v1`:
from the current no-pivot / concentrated-volume survivor, prove a product-preserving reduction that either exposes a Theorem-F-type diffuse three-frame with a permitted residual, or four disjoint original-coordinate low-dimensional banks whose effective rank-three carrier has a universal spectral scale and whose internal residual curvature is handled by an already proved receiver.

Exact scalar collinearity is too strong to assume, and approximate collinearity is not by itself enough because a small matrix coefficient is not a uniformly small random perturbation on arbitrary cap-one laws.

## Pinned e5f result actually applied

The required completed result is Theorem F from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

It is applied literally at (2.1) and (3.3), not merely cited. The same pinned bundle's counterexample search reports no valid QFORM counterexample; that negative search is **not** used as novelty evidence or as proof of the conjecture.

## Latest partner actually applied

Latest compatible completed fleet03/B18 report observed before this write:

`yspennstate/math-open-problems@c11bba404e9782ff3a919e1f7d352f39a7100eaf:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T225405Z-fleet03-B18-QFORM-auto13/REPORT.md`.

Its independent deterministic check artifact is at commit `2a053b6a128ce68f93b524fa3177d227f0990dbb`. The report proves `QFORM-FOUR-SOURCE-RANK3-COMPRESSION-v1` with `592/s` and the LPP-based four-disjoint-bank corollary `1184/s`. Equations (2.3), (4.6), and (5.4) are direct applications to the present construction.

## Correction audit

The argument uses none of the currently refuted interfaces:

- no law-uniform pointwise quadratic-phase decay;
- no arbitrary-joint rank-three coarea bound;
- no worst conditional projection-density moment;
- no conditional cap substituted for genuine independence;
- no post-rotation independence;
- no fixed-good-minor implication from the bare spectral hypothesis;
- no deletion of a small nonzero matrix term;
- no affine-slope rescue of a nonzero translated square;
- no indefinite innovation absorbing an arbitrary same-bank remainder.

All independence assertions above are attached either to the original product coordinates or to functions of pairwise disjoint original coordinate blocks.

## Scope and conclusion

The full universal QFORM theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. This run supplies a quantitative obstruction to direct fixed-four-core use of the latest four-source theorem, a concrete target family saturating that certificate loss, and a source-valid bank aggregation that removes the dimension loss on the same family. The strongest actual density estimate obtained here is the pinned theorem's universal `12` on the entire tetrahedral family. The partner transfer gives `<1184` and identifies the correct structural currency: exact product-preserving aggregation can restore unit rank-three scale that no fixed physical four-core sees.

Primary external source used: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 1.1.
