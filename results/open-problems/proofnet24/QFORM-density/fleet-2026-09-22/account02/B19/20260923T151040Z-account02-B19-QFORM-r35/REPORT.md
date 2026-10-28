SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B19, 2026-09-23T15:10:40Z.
attacking: the aligned STAR4 third-spectral-resource routing gate, specifically the fully overlapping in-plane case where the third direction has no source-disjoint bank and no transverse component to either rank-two cross singular plane.

# account02/B19 — fully overlapping third source: structural no-go plus a paid union-bank Fresnel chamber

Programme: `QFORM-DENSITY-3EIG-20260922`

Run: `20260923T151040Z-account02-B19-QFORM-r35`

Status: **ESSENTIAL_STEP_APPLIED + CANDIDATE_STRUCTURAL_IMPLICATION_REFUTED / FULL QFORM OPEN**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval is not claimed as native learned-memory ingestion.

## 1. Source-pinned proof graph entering this run


The current account02/B19 compiler at `math-open-problems@b0628a95c0c4630d063fe8c5649416c804dbceea` reaches, after the paid spectral-window and D5 exits, a literal physical `STAR4` packet. In its quantitative-rank-two branch the physical cross block `N=A[J,K]` has a fixed positive singular product and the hub has nontrivial star energy into each of the disjoint original-coordinate banks `J,K`.

The newest completed designated partner account03/B19 result is `math-open-problems@55fbef3fbe63cb7335851d9772449daac0ed67cf`. It proves that the aligned rank-two packet alone is not an L-infinity receiver: a strict-N3 rank-two core can have an unbounded logarithmic output density. Thus a genuine third spectral resource must be spent. Its first unresolved implication is `QFORM-STAR4-THIRD-SPECTRAL-RESOURCE-ROUTING-v1`.

The owner-required Claude source was read at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`, and its current compatible directory version was checked at master. I use its completed Theorem F below at an actual target-valid inequality.

## 2. New structural correction: source-disjoint or transverse third support is not forced

### Theorem 2.1 — `QFORM-ALIGNED-STAR4-THIRD-INPLANE-FORCING-FALSE-v1`

For every `tau in (0,1]` there is an exact-rank-three target matrix `A` such that

1. `spec_nonzero(A)={sqrt(8),1,-sqrt(8)}`;
2. `A` is strict `N3(tau)`: every `|A_ii|<tau` and every physical principal-pair determinant has magnitude `<tau`;
3. there is a physical hub `h` and disjoint original-coordinate banks `J,K` for which both hub-star energies equal `2`;
4. `N=A[J,K]` has exact rank two and `s_1(N)s_2(N)=7/6`;
5. both hub stars lie exactly in the left/right rank-two singular planes of `N`;
6. the third eigenvector has its `J`-projection in the same left rank-two plane and its `K`-projection in the same right rank-two plane, with no additional original-coordinate bank at all;
7. each one-bank self block `A[J,J]` and `A[K,K]` has range contained in the corresponding two-dimensional cross singular plane.

Hence the full three-large-eigenvalue hypothesis plus arbitrarily strict physical no-pivot geometry and exact two-sided STAR4 alignment does **not** force the third spectral resource to be source-disjoint from the active banks, nor to have a transverse component to either bank's top-two cross singular plane.

### Construction and proof

Fix an even integer `m>4/tau`. On `J` choose flat orthonormal vectors

`p=(1,...,1)/sqrt(m)`,

`r=(1,...,1,-1,...,-1)/sqrt(m)`

with `m/2` plus and `m/2` minus entries in `r`. On the disjoint bank `K` choose analogous flat orthonormal `q,s`. Let `e_h` be the physical hub vector. Set

`alpha=1/sqrt(6)`, `beta=1/sqrt(3)`,

so `alpha^2+beta^2=1/2` and `alpha != beta`. Define

`a=e_h+p+q`,
`b=e_h+r+s`,
`c=alpha(p-q)+beta(r-s)`,

and

`A=a a^T-b b^T+c c^T`.                                      (2.1)

We have

`||a||^2=||b||^2=3`, `a^T b=1`, `||c||=1`, and `c^T a=c^T b=0`.

Therefore `a a^T-b b^T` has nonzero eigenvalues `+sqrt(8),-sqrt(8)`, while `c` is an orthogonal unit eigenvector of eigenvalue `+1`. This proves item 1.

The hub diagonal is zero and

`A[J,h]=p-r`, `A[K,h]=q-s`,

so both star energies are exactly `2`.

In the orthonormal bases `(p,r)` on `J` and `(q,s)` on `K`, the cross block is represented by

`M = diag(1,-1) - [[alpha^2,alpha beta],[alpha beta,beta^2]]`

`  = [[5/6,-1/sqrt(18)],[-1/sqrt(18),-4/3]].`                    (2.2)

Its determinant is

`det M=-(1+beta^2-alpha^2)=-7/6`,                               (2.3)

so `N=A[J,K]` has exact rank two and

`boxed: s_1(N)s_2(N)=7/6.`                                      (2.4)

The hub stars and both pieces of `c` lie in these same two-dimensional planes by construction. Moreover

`A[J,J]=p p^T-r r^T+(alpha p+beta r)(alpha p+beta r)^T`,

and similarly `A[K,K]` has range in `span(q,s)`. Thus there is no one-bank transverse third mode.

For every leaf coordinate, the core diagonal `p_i^2-r_i^2` (or `q_i^2-s_i^2`) is zero, and the remaining diagonal is `c_i^2`. Since

`|c_i| <= (alpha+beta)/sqrt(m) < 1/sqrt(m)`,

we have `|A_ii|<1/m<tau`. Every hub-leaf entry has magnitude at most `2/sqrt(m)`. Every leaf-leaf off-diagonal entry has magnitude at most `3/m`. Consequently

`|A_hh A_jj-A_hj^2| <=4/m<tau`,

while for two leaves

`|A_ii A_jj-A_ij^2| <=1/m^2+9/m^2=10/m^2<tau`

because `m>4/tau` and `tau<=1`. Hence (2.1) lies in strict `N3(tau)`.

Finally, because `alpha!=beta`, each coordinate of `alpha p+beta r` and of `-alpha q-beta s` is nonzero. Thus the third eigenvector is not hidden on a smaller disjoint coordinate packet: it overlaps the active leaf banks coordinatewise.

This is a structural counterexample only. It does not refute QFORM.

## 3. The same fully overlapping family is paid by a union-bank Fresnel receiver

The construction shows the correct replacement for the false source-disjoint/transverse forcing statement.

Let `L=J union K` and put

`d_1=p+q`, `d_2=r+s`.

The leaf principal block is exactly

`A[L,L]=d_1 d_1^T-d_2 d_2^T+c c^T`.                              (3.1)

The three vectors

`v_1=d_1/sqrt(2)`, `v_2=d_2/sqrt(2)`, `v_3=c`

are orthonormal. Hence (3.1) has exact nonzero spectrum

`{2,-2,1}`.                                                       (3.2)

For each physical leaf coordinate `i`, its leverage in this three-frame is

`ell_i=|v_1(i)|^2+|v_2(i)|^2+|v_3(i)|^2`

`    <= 1/(2m)+1/(2m)+(alpha+beta)^2/m < 2/m <=1/2`              (3.3)

for `m>=4`.

Now apply the completed owner-required Theorem F from the Claude source with `I=L`, spectral coefficients `2,-2,1`, and residual matrix equal to `A-(2v_1v_1^T-2v_2v_2^T+v_3v_3^T)`. Its `L x L` residual block is zero, hence diagonal; the hub coupling and every outside block are allowed to remain arbitrary. The frame Gram is `G_L=I_3` and (3.3) verifies the leverage gate. Therefore

`|phi_Q(t)| <= (4 pi)^(3/2) 4^(-1/2) |t|^(-3/2)`

and

`boxed: ||p_Q||_infinity <=12 * 4^(-1/3) = 7.55952629936924... .}` (3.4)

The theorem also gives a continuous `C_0` density on this branch.

This is an equation-level application of a completed result from `math-open-problems@e5f71d79...`; no post-rotation independence is asserted. The orthonormal vectors are used only inside the Fresnel/BL proof, whose factorization remains in the original leaf coordinates.

## 4. General paid chamber extracted from the calculation

The preceding use of Theorem F yields the following direct STAR4-compatible corollary.

### Corollary 4.1 — `QFORM-STAR4-UNIONBANK-RANK3-FRESNEL-EXIT-v1`

Let `L` be any union of original-coordinate banks. Suppose for some orthonormal `v_1,v_2,v_3` supported on `L`, nonzero real `lambda_1,lambda_2,lambda_3`, and a diagonal matrix `D_L`,

`A[L,L]=sum_(k=1)^3 lambda_k v_k v_k^T + D_L`,                   (4.1)

and every physical leverage `sum_k v_k(i)^2 <=1/2`. Then, with **all** coefficients outside `L`, all `L`-outside couplings, and all affine terms arbitrary,

`boxed: ||p_Q||_infinity <=12 |lambda_1 lambda_2 lambda_3|^(-1/3).}` (4.2)

Thus a third source that overlaps both STAR4 banks need not first be separated into a new independent bank. If it closes the *union* leaf block into a diffuse rank-three-plus-diagonal packet, the existing Fresnel-Brascamp-Lieb theorem spends it directly.

This corollary is not claimed for arbitrary extra same-bank curvature beyond (4.1).

## 5. Updated conditional proof graph and first remaining gap

The strongest source-pinned graph now reads:

1. completed physical-pivot synthesis reduces the full theorem to one fixed strict `N3(tau)` statement;
2. at `tau=2^-20`, the spectral-window diffuse branch is paid (`<217.085` in the current compiler);
3. ridge failure produces a literal hub plus two balanced original-coordinate star banks and quantitative leaf cross energy;
4. D5 pays the diffuse fifth-volume branch (`<198.634` in the current compiler);
5. STAR4 splits into a relative-rank-one tube or a quantitative-rank-two branch;
6. selected-volume technology pays one quantitative-rank-two branch and otherwise leaves selected-volume anchors or a two-sided aligned near-rank-two core;
7. account03/B19 r35 proves the aligned local two-channel packet alone is insufficient and that an actual third resource must be spent;
8. **new here:** that third resource cannot be required to live on a source-disjoint bank or to be transverse to either individual cross plane; Theorem 2.1 is a target-valid strict-N3 counterexample to both such forcing statements;
9. **new positive exit:** if the overlapping resource instead creates a diffuse rank-three-plus-diagonal packet on the union leaf bank, Corollary 4.1 pays it directly, with (3.4) giving `<7.560` on the explicit hardest-alignment stress family.

Therefore the first compatible unpaid implication is sharpened to

`QFORM-STAR4-THIRD-RESOURCE-NONFRESNEL-OVERLAP-ROUTING-v1`:

> In the full strict-N3 aligned STAR4 survivor, after excluding source-disjoint packets, transverse selected-volume/rank-three exits, physical-pair/Schur exits, ridge/grouped-square exits, exact-null exits, **and the union-bank rank-three-plus-diagonal Fresnel exit (4.1)**, route the remaining third spectral resource in original product coordinates without deleting arbitrary overlapping tails/self-curvature.

The new family proves that a successful structural lemma must permit a third eigendirection whose projections stay completely inside the two aligned cross planes. What remains difficult is not that geometry by itself; it is the additional uncontrolled same-bank curvature/tail that prevents the union-bank block from having the exact rank-three-plus-diagonal form required by Theorem F.

No full-proof claim is made. Arbitrary-extra-spectrum closure remains contingent on the stated global N3 synthesis, continuity is open in the unrestricted target, and two independent end-to-end reviews do not exist.
