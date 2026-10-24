# account01/B04 — affine star half-Riesz rearrangement and colored curved-bank closure

**Run:** `20260922T174812Z-account01-B04-QFORM-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control at prepublication refresh:** revision `2026-09-22.10`  
**Assignment:** Product Fourier rearrangement  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and conditional end-to-end placement

The full target remains open: for every dimension, every independent real product input with one-dimensional densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal finite essential-supremum bound for the density of the quadratic form, or give a valid counterexample. No moments, support restrictions, log-concavity, post-rotation independence, or diagonal-basis assumptions are available. Continuity is an additional desired conclusion and is tracked separately.

The current proof assembly pays several diffuse/ridge, low-offdiagonal, scalar-square, rank-two Schur and grouped-bank branches. The latest designated partner `account02/B04` pays the pure rank-one star bank by aggregating the entire zero-curvature bank before applying a rank-two Schur estimate. Its first unpaid extension is internal curvature on that same bank.

This report attacks that extension directly. The result is a product-rearrangement half-Riesz estimate which is uniform over **arbitrary affine contamination** of the bank and arbitrary measurable curvature in the center coordinate. It then yields a density theorem whenever, after one physical scalar pivot, the Schur remainder contains a center-to-bank packet whose selected bank principal block is exactly zero. A coloring corollary allows nonzero internal curvature among the full bank: one conditions the other color classes and keeps a zero-principal independent set carrying a quantitative fraction of the cross-bank Euclidean mass.

The first still-unpaid implication after this run is therefore narrower: route the case where the high-cross bank has no quantitatively useful zero-principal independent set—especially nonzero physical bank diagonals or dense internal curvature—into an already paid square/ridge/two-direction mechanism without treating small matrix coefficients as small random perturbations (which is invalid without moment/support assumptions).

## 2. Source-pinned dependencies and corrections

### Designated partner actually used

I read and apply `account02/B04`, theorem `QFORM-ONE-CURVED-LEAF-STAR-BANK-v1`, canonical source

`yspennstate/math-open-problems@2ac6c31f920852005f11947f020bb4642af38d27`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T171934Z-r11/REPORT.md`, blob `849ee45bfc7f7b9e38312e190b7c495cbd6e4a74`.

For

`Q=aX^2+2bXY+lambda Y^2+2X sum c_k Z_k`, `B=||c||_2`,

it proves

`||p_Q||_infinity <= 27.8162566596 / sqrt(|lambda| B)`,

and, when its three nonzero eigenvalues are all target-normalized, it proves `B>=1` and `|lambda|>=1`.

I use the latter target-normalization conclusion below in an actual inequality; the new rearrangement estimate sharpens the partner constant on the same clean star family and survives additional conditioned affine contamination.

### Rank-two affine fractional theorem used for comparison only

I also read the complete proof of `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, canonical source

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`, blob `00681629acaba8f2e04edda6c9f6b5c4f0fdafa4`.

It gives the orientation-free generic bound

`sup_t E |(U^T X)^T Lambda(U^T X)+b^T X-t|^(-1/2) <=128 |det Lambda|^(-1/4)`

for arbitrary affine `b`. The new star lemma below is substantially sharper in the rank-one-cross geometry and is proved independently from scalar product-projection and decreasing rearrangement.

### Corrections respected

The proof uses no law-uniform pointwise quadratic-phase decay, no post-rotation independence, no conditional spectral density cap, no fixed good local minor extraction, no fiber-supremum argument, and no claim that one heavy offdiagonal coefficient can absorb arbitrary same-bank curvature. In particular it is compatible with the live `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` correction: the theorem below requires an exact zero-principal subset after Schur completion, and arbitrary curvature is only conditioned away outside that selected subset.

## 3. Two elementary rearrangement inputs

### Lemma 3.1 — half-Riesz potential of a capped scalar density

If `U` has a probability density `p` with `||p||_infinity<=K`, then

`sup_s E |U-s|^(-1/2) <= 2 sqrt(2K)`.                         (3.1)

**Proof.** The kernel `|u-s|^(-1/2)` is symmetric decreasing about `s`. By the bathtub/decreasing-rearrangement principle, among densities with mass one and cap `K`, the integral is maximized by `K` on the interval of length `1/K` centered at `s`. Hence

`K integral_{-1/(2K)}^{1/(2K)} |u|^(-1/2) du = 2 sqrt(2K)`. QED.

### Lemma 3.2 — a translated inverse-square-root integral under a cap-one input

If `X` has density at most one and `B>0`, then, uniformly in `delta`,

`E |2BX+delta|^(-1/2) <= 2 B^(-1/2)`.                       (3.2)

**Proof.** Again by decreasing rearrangement, the cap-one probability density maximizing the integral occupies a unit interval centered at the singular point. Thus

`E |2BX+delta|^(-1/2)
 <= (2B)^(-1/2) integral_{-1/2}^{1/2}|x|^(-1/2)dx
 =2 B^(-1/2)`. QED.

The only projection fact used below is the standard one-dimensional product projection bound also used in the partner reports: if independent coordinates have densities at most one, then a nonzero linear form `q dot Z` has density at most `sqrt(2)/||q||_2`.

## 4. New theorem — affine star half-Riesz rearrangement

### Theorem 4.1 — `QFORM-AFFINE-STAR-HALF-RIESZ-v1`

Let `X,Z_1,...,Z_m` be independent real random variables with densities bounded by one. Let `c in R^m` be nonzero, put `B=||c||_2`, let `d in R^m` be arbitrary, and let `h:R->R` be any measurable function finite almost surely. Define

`R = h(X) + (2X c + d) dot Z`.                               (4.1)

Then

`boxed: sup_t E |R-t|^(-1/2) <= 2^(11/4) B^(-1/2)`          (4.2)

with

`2^(11/4)=6.7271713220...`.

No moment, support, continuity, sign or compactness hypothesis is imposed on any input density. The function `h` is completely arbitrary.

### Proof

Condition on `X=x`. Except possibly at one value of `x`, the coefficient vector

`q(x)=2xc+d`

is nonzero. The scalar product-projection theorem gives the conditional density cap

`||p_{q(x) dot Z}||_infinity <= sqrt(2)/||q(x)||_2`.          (4.3)

The term `h(x)` is only a translation. Apply Lemma 3.1:

`sup_t E_Z |h(x)+q(x) dot Z-t|^(-1/2)
 <=2^(7/4)||q(x)||_2^(-1/2)`.                               (4.4)

If `q(x)=0` at one `x`, define the right side as infinity there; this is harmless because `X` has an absolutely continuous law.

Let `e=c/B`. Orthogonal projection onto `e` gives

`||2xc+d||_2 >= |2Bx + <d,e>|`.                              (4.5)

Average (4.4) in `x`, use (4.5), then Lemma 3.2:

`sup_t E |R-t|^(-1/2)
 <=2^(7/4) E |2BX+<d,e>|^(-1/2)
 <=2^(7/4)*2 B^(-1/2)
 =2^(11/4)B^(-1/2)`.                                        (4.6)

This proves (4.2). QED.

### Structural significance

The theorem is stronger than a clean aggregate-star estimate in one direction that matters for the full problem: after conditioning arbitrary outside original coordinates, all their cross-couplings into the selected bank become an arbitrary affine vector `d`, and all their cross-couplings into the center become part of the arbitrary function `h`. Both are absorbed at no loss. Thus outside curvature is harmless **provided the selected bank has zero principal quadratic block after the scalar Schur step**.

## 5. Scalar-pivot density theorem with arbitrary outside curvature

### Theorem 5.1 — `QFORM-SCHUR-ZEROBANK-DENSITY-v1`

Let `A` be any real symmetric matrix and let the independent cap-one physical coordinates be partitioned as

`(Y, X, Z_J, W)`.

Assume the physical pivot coefficient `a=A_YY` is nonzero. Write the Schur complement after completing the square in `Y` as

`S=A_{-Y,-Y}-A_{-Y,Y}A_{Y,-Y}/a`.                           (5.1)

Assume that for a nonempty original-coordinate set `J`,

`S[J,J]=0`,                                                   (5.2)

and put

`c=(S[X,j])_{j in J}`, `B=||c||_2>0`.                        (5.3)

There is **no restriction** on `S[W,W]`, `S[{X} union J,W]`, the dimension of `W`, or the signs and sizes of any additional eigenvalues. Then the full quadratic form `Q=X_phys^T A X_phys` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 2^(11/4) / sqrt(|a| B).`         (5.4)

### Proof

Complete the square only in the original physical coordinate `Y`:

`Q = a(Y+a^(-1)A_{Y,-Y}V)^2 + V^T S V`,                    (5.5)

where `V=(X,Z_J,W)`. Conditional on `V`, `Y+a^(-1)A_{Y,-Y}V` is merely a translate of `Y`; therefore the conditional density of the square term is bounded by

`|a|^(-1/2)|u|^(-1/2)` on its half-line.                    (5.6)

Now condition on `W=w`. Because of (5.2), the residual `V^T S V` restricted to the still-random variables `(X,Z_J)` has exactly the form

`h_w(X)+(2Xc+d_w) dot Z_J + const_w`,                        (5.7)

where `h_w` is arbitrary and `d_w` is an arbitrary vector generated by the conditioned cross-couplings. Theorem 4.1 is uniform in both. Mixing the square kernel (5.6) against (5.7) gives

`p_{Q|W=w}(t)
 <= |a|^(-1/2) E_{X,Z_J}|t-R_w|^(-1/2)
 <= 2^(11/4)/sqrt(|a|B)`.                                   (5.8)

Average over `W`. This proves absolute continuity and (5.4). QED.

The theorem does **not** separately prove continuity of the density.

## 6. Internal bank curvature via exact coloring

The previous theorem does not require the *whole* bank to have zero curvature. It only requires one selected zero-principal subset; everything else can be conditioned.

Let `K` be a set of bank coordinates for which `S[j,j]=0`. Form the graph `G` on `K` by joining `j` and `k` whenever `S[j,k]!=0`. Put

`B_0 = (sum_{j in K} S[X,j]^2)^(1/2)`.                       (6.1)

Suppose `G` admits a proper coloring with `chi` colors. Every color class `J` has `S[J,J]=0`. One color class carries at least a `1/chi` fraction of the squared cross mass, so

`||S[X,J]||_2 >= B_0/sqrt(chi)`.                             (6.2)

Applying Theorem 5.1 gives the new curved-bank estimate

`boxed: ||p_Q||_infinity
 <= 2^(11/4) chi^(1/4) / sqrt(|a| B_0).`                    (6.3)

In particular, if the exact nonzero-pattern graph on the zero-diagonal bank has maximum degree `Delta`, greedy coloring gives the explicit replacement `chi<=Delta+1`.

This is a genuine internal-curvature extension: nonzero quadratic couplings may occur throughout the bank, but a product-preserving independent set is selected **before** any spectral rotation, and the other bank coordinates are conditioned rather than declared independent after diagonalization. The price is only `chi^(1/4)`.

The exact-zero requirement is important. Without moments or support control, a small matrix coefficient multiplying `Z_j^2` is not a uniformly small random perturbation, so no norm-small approximation is claimed.

## 7. Actual application of the designated partner result

The partner's clean star theorem proves that for its target-normalized three-nonzero-eigenvalue family,

`B>=1` and `|lambda|>=1`.                                    (7.1)

That family is exactly the `chi=1` case of Theorem 5.1 after pivoting the curved leaf `Y`. Substituting the partner's proved normalization (7.1) into (5.4) gives the actual target-valid inequality

`boxed: ||p_Q||_infinity <= 2^(11/4) < 6.728`.               (7.2)

The partner's previous constant on the same clean family was `27.8162566596`. Thus the new rearrangement both sharpens that bound and explains why arbitrary conditioned affine contamination of the zero-curvature bank does not cost anything. This is a concrete use of a completed partner result, not a scope transfer to arbitrary curved banks.

## 8. Explicit genuinely rotated indefinite example with bank curvature

Order the physical coordinates as `(Y,X,Z_1,Z_2)` and take

`A = [[4, 3/10, 0, 0],
      [3/10, 0, 2sqrt(2), 2sqrt(2)],
      [0, 2sqrt(2), 0, 2/5],
      [0, 2sqrt(2), 2/5, 0]].`                               (8.1)

This is non-diagonal and indefinite. Let `A_0` be obtained by deleting the `3/10` and `2/5` couplings. Then

`spec(A_0)={-4,0,4,4}`.                                     (8.2)

The perturbation `A-A_0` is the direct sum of the offdiagonal `2x2` blocks with coefficients `3/10` and `2/5`, hence

`||A-A_0||_op=2/5`.                                         (8.3)

Weyl therefore gives two positive eigenvalues at least `18/5=3.6` and one negative eigenvalue at most `-18/5`; in particular (8.1) satisfies the exact owner target with room to spare.

Pivot `Y`. Its coefficient is `a=4`; the Schur correction affects only the `X` diagonal, so on the bank `{Z_1,Z_2}` the Schur block is

`[[0,2/5],[2/5,0]]`.                                        (8.4)

Both bank diagonals vanish and the internal-curvature graph is a single edge, hence `chi=2`. The center-to-bank cross vector is `(2sqrt(2),2sqrt(2))`, so `B_0=4`. Formula (6.3) gives exactly

`||p_{X_phys^T A X_phys}||_infinity
 <= 2^(11/4) 2^(1/4) / sqrt(4*4)
 = 2.`                                                       (8.5)

This holds for **every** independent choice of physical-coordinate input laws with densities bounded by one. The example is genuinely rotated/nonseparable and contains nonzero internal bank curvature. The theorem establishes an essentially bounded density here; continuity is not asserted.

## 9. Why this does not solve the full conjecture

The new theorem pays a zero-principal bank subset and, through coloring, bounded-complexity exact internal curvature. It does not show that the bare hypothesis of three eigenvalues of modulus at least one forces such a subset with `|a|B_0/chi^(1/2)` bounded below. A dense bank can have every physical diagonal nonzero, or have a zero-diagonal interaction graph with large chromatic number; arbitrarily tiny nonzero coefficients cannot simply be discarded because the inputs may have arbitrarily remote fragmented support.

Thus the full conjecture remains OPEN.

The first B04 implication now is:

**`QFORM-DENSE-CURVED-BANK-ROUTING-v1`.** In the remaining high-offdiagonal/high-overlap branch, show that failure of a quantitatively useful zero-principal colored bank forces a product-preserving square/ridge/two-direction certificate already paid by the existing square-assisted window or rank-two affine machinery. The proof must use the actual magnitudes/structure of internal curvature, not an exact-support graph alone and not a perturbative moment argument.

A compact conditional end-to-end proof is now: all previously paid diffuse/low-offdiagonal/ridge branches close; a pure or bounded-color zero-principal high-cross bank closes by (6.3); if every such packet fails, prove `QFORM-DENSE-CURVED-BANK-ROUTING-v1` and send its resulting square/ridge certificate to the completed partner/account03 inequalities. This last structural implication is the first unpaid step.

## 10. Integrity and continuity status

- Full QFORM theorem: **not proved**.
- New supporting theorems (4.1, 5.1, 6.3): proved above under their exact scopes.
- Continuous density: **not proved** by these new branches; only existence of an essentially bounded density is proved.
- No Gaussianity, log-concavity, moments, compact support, connected support, or rotated-coordinate independence is used.
- No law-uniform pointwise Fresnel decay or naive fiber supremum is used.
- No numerical histogram is used as evidence. The explicit example's target status follows from the exact reference spectrum and Weyl bound.
