# account01/B18 r21 — LPP-to-null-ray packet sharpening via designated account02/B18

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T01:56:18Z.

attacking: literature-to-proof transfer for the exact-rank-three null-ray/rank-two-bank packet, applying the latest account02/B18 dependent-pair kernel to an actual target-level inequality.

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed:** revision `2026-09-22.15`  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_TARGET_LEVEL_SHARPENING / DESIGNATED_PARTNER_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and correction boundary

The full owner target remains OPEN: arbitrary finite dimension, independent original-coordinate variables with densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. The present theorem is an exact-rank-three structured branch and is not an exhaustive reduction from the bare spectral hypothesis.

The proof keeps genuine original-coordinate bank independence. It does **not** use independence after spectral rotation, arbitrary-joint rank-three coarea, conditional projection-density caps, positive conditional density moments, pointwise law-uniform Fresnel decay, near-zero-as-zero perturbation, or a fixed-good-minor assertion.

## 2. Primary literature theorem read at its exact hypotheses

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949v2, Theorem 1.1 (later Israel J. Math. 216 (2016)).

Theorem 1.1 assumes a product probability density

`f(x)=prod_(i=1)^n f_i(x_i)`, `||f_i||_1=1`, each `f_i` bounded,

and a `k`-dimensional orthogonal subspace `E`. It gives exponents `gamma_i in [0,1]`, `sum gamma_i=k`, and

`||pi_E f||_infinity
 <= min((n/(n-k))^((n-k)/2), 2^(k/2))
    prod_i ||f_i||_infinity^(gamma_i)`.

Therefore, for the owner's cap-one class:

- every normalized one-dimensional original-product projection has density cap at most `sqrt(2)`;
- every normalized two-dimensional orthogonal original-product projection has joint density cap at most `2`.

No moments, centering, bounded support, connected support, iid assumption, log-concavity, or smoothness enter. This is precisely the source interface needed below.

## 3. Designated partner theorem actually applied

Newest completed designated-partner result read before this proof:

`yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T013147Z-bf13c29b/REPORT.md`.

Its theorem `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1` says:

If `S` has density cap `K`, `(C,D)` is independent of `S` and has an arbitrary joint density cap `M`, and `beta,gamma !=0`, then

`Q=2 beta S C + alpha C^2+2 delta C D+gamma D^2`

obeys

`||p_Q||_infinity
 <= 3 (2 M K)^(2/3) |beta^2 gamma|^(-1/3).`                 (3.1)

Equivalently, if the nonsingular symmetric active matrix has zero scalar pivot, its determinant is `-beta^2 gamma` after an orthogonal change inside the pair, and (3.1) is

`||p_Q||_infinity <=3(2MK)^(2/3)|det H|^(-1/3).`            (3.2)

The pair coordinates need not be independent. Only the scalar-vs-pair independence is required.

Arbitrary affine terms do not create a gap here: because `H` is nonsingular, complete the square by a deterministic translation of the scalar and of the pair. Such separate translations preserve scalar/pair independence and both density caps. An orthogonal rotation inside the pair has Jacobian one, preserves its joint density cap, and aligns the scalar cross-vector with one pair coordinate, exactly giving the partner normal form.

## 4. Existing null-ray packet geometry

Use the exact-rank-three spectral-frame notation

`A=R M R^T`, `R^T R=I_3`, `D=|det M|>0`,

with physical spectral rows `r_j in R^3`.

Let `B,C` be disjoint original-coordinate banks satisfying:

1. all rows in `B` lie in a two-dimensional plane `E`, and

   `H_B=sum_(i in B) r_i r_i^T |_E`, `h=det_E(H_B)>0`;

2. all rows in `C` lie on one unit ray `r`,

   `r_k=alpha_k r`, `m=sum_(k in C) alpha_k^2>0`;

3. `delta=dist(r,E)^2>0`;

4. the ray is spectrally null,

   `r^T M r=0`.

The completed account03/B10 packet identity gives

`T_(B,B;C)
 = sum_(i<j in B,k in C) det(r_i,r_j,r_k)^2
 = m h delta.`                                                (4.1)

Its previous target-level theorem gave the continuous-density estimate

`||p_Q||_infinity <=12 [D T_(B,B;C)]^(-1/3).`                (4.2)

The goal of this run is not to re-prove (4.2), but to sharpen its essential-density constant by transferring the latest account02/B18 kernel at its exact hypotheses.

## 5. Source-valid sharpening

Condition on every original coordinate outside `B union C`. The active variables remain built from disjoint original-coordinate banks; the conditioning introduces only an affine term and a constant.

### 5.1 Rank-one bank

Set

`W=sum_(k in C) alpha_k X_k`.

The coefficient vector has Euclidean norm `sqrt(m)`. Applying the `k=1` Livshyts--Paouris--Pivovarov marginal theorem to `W/sqrt(m)` gives

`K:=||p_W||_infinity <= sqrt(2/m).`                           (5.1)

### 5.2 Rank-two bank

Choose an orthonormal basis `(e_1,e_2)` of `E` and write

`Z=(Z_1,Z_2)=sum_(i in B) (coordinates of r_i in E) X_i`.

Its coefficient Gram is `H_B`. Whitening gives

`Y=H_B^(-1/2) Z`,

which is an orthogonal two-dimensional projection of the cap-one product block `X_B`. LPP with `k=2` therefore gives `||p_Y||_infinity<=2`. Undoing the linear map yields

`M_2:=||p_Z||_infinity <= 2/sqrt(h).`                         (5.2)

No independence between `Z_1` and `Z_2` is asserted.

Because `B` and `C` are disjoint original-coordinate banks, `W` and the entire pair `Z` are genuinely independent.

### 5.3 Active determinant

Let

`F=[r,e_1,e_2]`.

The active quadratic matrix in `(W,Z_1,Z_2)` is

`H_0=F^T M F`.

Its scalar pivot is zero by `r^T M r=0`, while

`|det H_0|=D |det F|^2=D delta.`                              (5.3)

It is nonsingular because `D,delta>0`.

### 5.4 Apply account02/B18

Insert (5.1)--(5.3) into the designated partner inequality (3.2):

`||p_(Q | outside)||_infinity
 <=3 [ 2 * (2/sqrt(h)) * sqrt(2/m) ]^(2/3)
      (D delta)^(-1/3)`

` =3 * 2^(5/3) (D m h delta)^(-1/3)`

` =3 * 2^(5/3) [D T_(B,B;C)]^(-1/3).`                        (5.4)

The constant is

`3*2^(5/3)=9.524406311809198...`.

The bound is uniform in the outside conditioning value, so averaging gives the full ambient exact-rank-three branch:

### Theorem — `QFORM-RANK2BANK-NULLRAY-PACKET-SHARPENED-v1`

Under the hypotheses in Section 4,

`boxed:
 ||p_Q||_infinity
 <= 3*2^(5/3) [D T_(B,B;C)]^(-1/3)
 < 9.525 [D T_(B,B;C)]^(-1/3).`                                (5.5)

This improves the previous constant `12` by the exact factor

`2^(-1/3)=0.7937005259...`,

i.e. a `20.629947%` reduction.

For the especially clean line-plane Parseval decomposition where the line bank and the orthogonal plane bank exhaust the frame, `m=h=delta=1`, so `T=1`; if the three nonzero eigenvalues all have modulus at least one then `D>=1`, and

`boxed: ||p_Q||_infinity <= 3*2^(5/3)=9.524406311809198... .`   (5.6)

This is an actual application of the designated account02/B18 theorem, not merely a citation.

## 6. Continuity tracked separately

The partner weak-`L^(3/2)` kernel proves essential boundedness but does not by itself state continuity. I therefore do **not** infer continuity from (5.4).

However, the exact same null-ray/rank-two-bank hypotheses were already covered by account03/B10's theorem (4.2), whose proof explicitly supplies a continuous representative via the affine zero-pivot `1+2` theorem and dominated convergence. Hence on this branch we may state separately:

- best essential bound supplied here: `3*2^(5/3)[DT]^(-1/3)`;
- continuity: already established by the prior source-pinned `12[DT]^(-1/3)` theorem.

Thus continuity is retained without pretending the sharper partner kernel proves it.

## 7. Why this does not solve the full target

The bare assumption `s_3(A)>=1` does not force an exact rank-two physical bank plus a transverse spectrally-null rank-one bank, and the correction archive contains counterexamples to several fixed-good-minor / exact-bank extraction shortcuts. Additional eigenvalues and near-null rather than exactly null rays require separate mechanisms.

The remaining structural implication for this branch of the full proof is therefore: obtain a dimension-free lower bound on an aggregate packet `D T_(B,B;C)` in a legitimately disjoint original-coordinate null-ray/rank-two-bank decomposition, or route failure to the already-paid ridge/physical-pivot/capped-basis branches. The analytic payment for such a packet is now `9.524406...` rather than `12`.

No exact prior theorem was located that settles the owner's unrestricted arbitrary-cap-one three-large-eigenvalue target. This report makes no literature-novelty claim; it records a source-valid transfer and quantitative sharpening inside the fleet proof architecture.

## 8. Sources and pins

Primary literature:

- Livshyts--Paouris--Pivovarov, arXiv:1507.07949v2, Theorem 1.1: product marginal density theorem.

Fleet dependencies actually used:

- designated account02/B18: `math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T013147Z-bf13c29b/REPORT.md`;
- null-ray packet geometry and continuity: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260922T231827Z-account03-B10-QFORM-r21/REPORT.md` on master, source blob `d34a92896ab80e510e8807c9fb26b84304ad7d5d` as read this run.


Privacy/write note: this file contains only mathematical and operational source pins. No credentials, private personal material, scheduler identifiers, or unrelated data are included. Repository-native secret scanning was not exposed by the connector; manual changed-file review was used as the limited fallback.
