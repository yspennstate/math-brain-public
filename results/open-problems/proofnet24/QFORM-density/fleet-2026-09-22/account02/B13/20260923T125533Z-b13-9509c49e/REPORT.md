SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-23T12:55:33Z.
attacking: diffuse Schur-residual extraction from a high-density two-hub witness, then forcing either low residual cross rank or a physical three-volume bi-hub while preserving the extremal product law.

# account02/B13 — diffuse Schur residual and cross-volume bi-hub normal form

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: `Extremal product laws`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING TARGET-LEVEL STRUCTURAL THEOREM; FULL QFORM OPEN; FULL CONTINUITY OPEN**

## 1. Exact target and first unpaid implication

The target remains: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove

`P(X^T A X in J) <= C |J|`

with one universal finite `C` for every interval `J`, or produce a valid counterexample. No moment, bounded-support, connected-support, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumption is allowed. Continuity is separate.

The first unpaid implication after this run is

`QFORM-SCHUR-CROSSCUT-ROBUST-STAR-GLUE-v1`:

> In the high-ratio branch with a genuine invertible physical two-hub block, combine the new strong-but-diffuse Schur cross cut below with either (i) residual cross rank at most four at scale `O(rho^-1)`, or (ii) the forced physical order-three volume bi-hub; simultaneously use the designated partner's slab-scale curvature graph and local principal-triple singularity on the finite-union extreme witness. Close this by a product-preserving grouped-bank/ridge/null-bank estimate, or construct an actual bounded-finite-union product-indicator counterexample. The singular/zero-diagonal hub chambers remain separate and must not be perturbed into this one.

This run does not claim the full conjecture.

## 2. Completed source results actually used

### 2.1 High-ratio two-hub Nystrom rigidity

Source:

`yspennstate/math-open-problems@ac5acc0621d0b45e2942a259747399d983e24c14`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T113036Z-account01-B13-qform-auto22/REPORT.md`.

For an original physical hub pair `H={1,2}` and all remaining coordinates `L`, write

`A = [[H0,B],[B^T,C]]`,
`H0=[[a,h],[h,g]]`,

with `a!=0`, `det H0!=0`, and define the exact Schur/Nystrom remainder

`T = C-B^T H0^{-1}B`.                                             (2.1)

If an interval `J` has slab ratio

`rho=P(X^TAX in J)/|J|`,                                          (2.2)

then the completed theorem gives

`||T||_max <= epsilon`,
`epsilon = C_N/(rho^4 |a det H0|)`,                               (2.3)

where

`C_N=sqrt(128^8+32^8) < 2.685e8`.                                 (2.4)

All remaining curvature and all affine terms are retained in the source theorem. Crucially, (2.3) is **not** permission to delete `T` on arbitrary fragmented/unbounded product supports.

### 2.2 Required pinned Claude/Fourier package

Source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,
`FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Three proved statements are used at equations below.

First, Schur complements keep the remaining large spectrum: if `A` has `k` eigenvalues of modulus at least one and `H0` is an invertible physical `2x2` principal block, then `A/H0` has at least `k-2` eigenvalues of modulus at least one. Therefore the full leaf Schur remainder `T` in (2.1) has an eigenvalue `lambda` with

`|lambda|>=1`.                                                     (2.5)

Second, the unconditional fifth-volume estimate says that for every disjoint original-coordinate cut `I,J`, with `M=A[I,J]`,

`||p_Q||_inf <= C_5 e_5(M^T M)^(-1/10)`,
`C_5=5 sqrt(2e)=11.658219907986...`,                               (2.6)

with no marginal condition. Consequently every slab witness of ratio `rho` obeys

`e_5(M^T M) <= (C_5/rho)^10`.                                     (2.7)

If `e_5=0`, (2.7) is automatic; otherwise it follows directly from (2.6).

Third, the relaxed order-three volume theorem `D'`, at the choice `h=2/3`, gives

`||p_Q||_inf <= C_3 e_3(M^T M)^(-1/6)`,
`C_3=9 sqrt(3e)=25.701021075349...`,                               (2.8)

provided every row marginal of natural order-three volume sampling is at most `2/3`. The same theorem applies to `M^T`, thereby controlling column marginals.

The pinned counterexample search found no valid counterexample in its tested families. No numerical search result is used as a proof here.

### 2.3 Designated partner account03/B13 r25

Source:

`yspennstate/math-open-problems@7fab009ecf17adff8781fb5f00d94d3cf348e67c`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T113043Z-account03-B13-qform-r25/REPORT.md`.

For any arbitrary cap-one strict bad slab, its completed no-attainment purification gives bounded finite-union unit-measure product indicators `1_{E_i}` with slab ratio arbitrarily close to the original one. No global optimizer, centered interval, support-diameter bound, or fixed fragment count is asserted.

On an actual extreme witness, for a fixed physical hub pair `H`, write `b_j=A[H,{j}]` and `r_j=rad(E_j)`. Put an edge between leaves `u,v` when

`|A_uv| r_u r_v > |J|/12`.                                       (2.9)

If `j,k,l` are pairwise nonadjacent in this slab-scale graph, the partner proves

`|det(b_j,b_k)| ||b_l||_2 <= 216 sqrt(2)/rho_E^3`.                 (2.10)

The same report also records, using its preceding local compiler, that every physical principal triple `S` in a high-ratio extreme witness satisfies

`sigma_min(A[S,S]) <= L_*/rho_E`,
`L_*=128*2^(1/4)<152.219`.                                        (2.11)

Equations (2.10)-(2.11) are applied in Section 6 to the exact obstruction produced here.

## 3. New deterministic random-cut lemma

### Lemma 3.1 — `QFORM-DIFFUSE-EIGENVECTOR-RANDOM-CUT-v1`

Let `T` be a real symmetric `m x m` matrix. Suppose

`Tv=lambda v`, `||v||_2=1`,                                      (3.1)

and

`max_i |T_ii| <= epsilon`.                                        (3.2)

Then there is a partition `[m]=I disjoint-union J` such that

`boxed: s_1(T[I,J]) >= (|lambda|-epsilon)/2.`                     (3.3)

If in addition every entry of `T` has absolute value at most `epsilon`, then necessarily

`boxed: m >= (|lambda|-epsilon)/epsilon.`                         (3.4)

### Proof

Choose a random Bernoulli half-partition: independently put each index in `I` with probability `1/2`, otherwise in `J`. Define

`S(I,J)=v_I^T T[I,J] v_J`.                                       (3.5)

Every ordered off-diagonal pair `(i,j)` occurs in `I x J` with probability `1/4`, hence

`E S = (1/4) sum_{i!=j} v_i T_ij v_j`
`    = (1/4) (lambda - sum_i T_ii v_i^2)`.                        (3.6)

Therefore some partition obeys

`|S(I,J)| >= |E S| >= (|lambda|-epsilon)/4`.                      (3.7)

On the other hand

`|S(I,J)| <= s_1(T[I,J]) ||v_I||_2 ||v_J||_2`
`           <= (1/2) s_1(T[I,J])`,                               (3.8)

because `||v_I||_2^2+||v_J||_2^2=1`. Combining (3.7)-(3.8) gives (3.3).

If every entry has size at most `epsilon`, then

`s_1(T[I,J]) <= ||T[I,J]||_F`
`             <= epsilon sqrt(|I||J|)`
`             <= epsilon m/2`.                                   (3.9)

Combine (3.3) and (3.9) to obtain (3.4). QED.

The randomness is only an existence proof for a deterministic coordinate cut. No random-variable rotation or independence statement is made.

## 4. High-ratio Schur residual must contain a strong diffuse physical cut

Apply Lemma 3.1 to the Schur remainder `T` from (2.1). By (2.3), every entry of `T` has absolute value at most `epsilon`; by (2.5), `T` has a unit eigenpair with `|lambda|>=1`.

If

`rho^4 |a det H0| > 2 C_N`,                                      (4.1)

then `epsilon<1/2`, and Lemma 3.1 produces a partition of the full leaf coordinates `L=I disjoint-union J` satisfying

`boxed: s_1(T[I,J]) >= 1/4`.                                     (4.2)

It simultaneously forces the quantitative dimension lower bound

`boxed:
 |L| >= 1/(2 epsilon)
      = rho^4 |a det H0|/(2 C_N).
`                                                                    (4.3)

Thus a high-density witness with a quantitatively nondegenerate physical hub pair cannot hide its Schur-retained third large direction in a bounded collection of leaves once all Schur coefficients have collapsed. It must become a genuinely diffuse, high-dimensional cross interaction.

If (4.1) fails, then instead we already have the quantitative hub degeneracy

`rho^4 |a det H0| <= 2 C_N`.                                      (4.4)

No support information is used in either branch.

## 5. Pinned D5 and D' convert the strong Schur cut into a rank-or-bi-hub dichotomy

Fix the partition `I,J` from Section 4 and write

`M=A[I,J]`,
`R=B_I^T H0^{-1} B_J`.                                            (5.1)

Because `T` is the Schur complement,

`T[I,J]=M-R`,                                                      (5.2)

and `rank R<=2`.

### 5.1 Fifth-volume tail: residual numerical cross rank at most six

From (2.7), Cauchy-Binet/singular values give

`e_5(M^T M)>=s_1(M)^2...s_5(M)^2>=s_5(M)^10`,                    (5.3)

so

`s_5(M)<=C_5/rho`.                                                 (5.4)

For a rank-two perturbation, the singular-value interlacing inequality gives

`s_{k+2}(M-R)<=s_k(M)`.                                            (5.5)

Taking `k=5`,

`boxed: s_7(T[I,J]) <= C_5/rho.`                                 (5.6)

Together with (4.2), the Schur cut has one uniformly strong singular direction while every singular direction from the seventh onward is `O(rho^-1)`.

### 5.2 Third-volume gate: either residual rank four, or a physical bi-hub

Suppose first that the natural order-three volume-sampling row marginals of `M` are all at most `2/3`. By (2.8),

`rho <= C_3 e_3(M^T M)^(-1/6) <= C_3/s_3(M)`,                    (5.7)

hence

`s_3(M)<=C_3/rho`.                                                 (5.8)

Using (5.5) with `k=3`,

`boxed: s_5(T[I,J]) <= C_3/rho.`                                 (5.9)

So the residual cut is numerically rank at most four at scale `C_3/rho`.

Now suppose instead that

`s_5(T[I,J]) > C_3/rho`.                                          (5.10)

Then (5.5) implies `s_3(M)>C_3/rho`, so (5.7) is impossible. Therefore some row `i in I` has order-three volume marginal

`alpha_i>2/3`.                                                     (5.11)

Apply exactly the same pinned theorem to `M^T`. Since its third singular value is the same, its marginal gate must fail too; therefore some column `j in J` has

`beta_j>2/3`.                                                      (5.12)

For the natural volume-sampling law

`w_{S,T}=det(M[S,T])^2/e_3(M^T M)`                                (5.13)

on pairs of `3`-element row/column sets, (5.11)-(5.12) and inclusion-exclusion yield

`boxed:
 P_w(i in S and j in T)
 >= alpha_i+beta_j-1
 >1/3.
`                                                                    (5.14)

Thus the only way the strong Schur cut can retain a fifth singular direction larger than `C_3/rho` is for the **original physical cross block** `A[I,J]` to place more than one third of all its squared `3x3`-minor mass on a single physical row-column joint star.

### Theorem 5.2 — `QFORM-SCHUR-RESIDUAL-CROSSCUT-BIHUB-v1`

Under the target hypotheses, fix any physical hub pair `H` with `H0=A[H,H]`, `a=(H0)_{11}!=0`, and `det H0!=0`. Let `rho` be any slab ratio. Then either

`rho^4 |a det H0| <= 2 C_N`,                                      (5.15)

or there is a partition of all remaining physical coordinates `L=I disjoint-union J` such that

`boxed: s_1((A/H0)[I,J]) >=1/4,`                                 (5.16)

`boxed: s_7((A/H0)[I,J]) <= C_5/rho,`                            (5.17)

and one of the following two alternatives holds:

(A) `s_5((A/H0)[I,J]) <= C_3/rho`;                                (5.18)

(B) the original block `A[I,J]` has row/column order-three volume marginals `alpha_i,beta_j>2/3` for some physical `i,j`, with joint volume mass strictly larger than `1/3` as in (5.14).      (5.19)

In the second branch one also has the forced dimension lower bound (4.3).

Everything in Theorem 5.2 is stated in original coordinate blocks or exact Schur complements of an original physical hub pair. No small matrix is discarded as a small random quadratic error.

## 6. Applying the designated partner to the same obstruction

Let the original arbitrary cap-one law have a strict slab ratio `rho_f`. By the designated account03/B13 purification, for every `eta>0` there is a bounded finite-union product indicator witness `prod_i 1_{E_i}` with

`rho_E >= rho_f-eta`.                                             (6.1)

The matrix `A`, the chosen physical hub pair `H`, its exact Schur complement `T=A/H0`, and the cut produced by Lemma 3.1 are unchanged by this law reduction. Therefore Theorem 5.2 applies with `rho_E` in place of `rho_f` to this actual compact witness.

At the same time, the partner's slab-scale curvature graph (2.9) is valid on those same sets `E_i`. Hence every pairwise nonadjacent triple of leaves around the chosen physical hubs satisfies the concrete inequality

`boxed:
 |det(b_j,b_k)| ||b_l||_2
 <= 216 sqrt(2)/rho_E^3.
`                                                                    (6.2)

And every physical principal triple satisfies

`boxed:
 sigma_min(A[S,S]) <= L_*/rho_E.
`                                                                    (6.3)

Thus a hypothetical counterexample sequence in this invertible-hub chamber with `rho_E -> infinity` is forced simultaneously into the following geometry:

1. unless the physical hub currency `|a det H0|` collapses at the `rho_E^-4` scale, the leaf dimension diverges at least like `rho_E^4 |a det H0|`;
2. the Schur remainder has an original-coordinate cross cut with `s_1>=1/4` but `s_7=O(rho_E^-1)`;
3. either that same residual cut has `s_5=O(rho_E^-1)`, or the corresponding original cross block carries more than one third of its squared third-minor mass on one physical row-column joint star;
4. every slab-scale independent transverse leaf triple around the hub pair obeys the partner's `O(rho_E^-3)` determinant constraint (6.2), while every physical principal triple is `O(rho_E^-1)`-singular by (6.3).

This is the requested equation-level use of the completed partner result: it constrains the same bounded finite-union extreme witness on which the new Schur cross-cut dichotomy is realized. It does not assume that one interval is extremal and it preserves arbitrary fragment separation.

## 7. Extremal-product transfer and scope

The previous account02/B13 finite-mixture purification and the designated partner's no-attainment theorem give the correct interface from arbitrary cap-one marginals to product indicators: approximate each marginal in `L1` by a finite convex mixture of indicators of bounded finite unions of total measure one; expand the product mixture and use the product telescoping estimate. This transfers every strict bounded-slab violation with arbitrarily small loss. It does **not** assert an attained optimizer, a centered interval, a bounded diameter, or a universal fragment count.

No Riesz or other unbounded kernel is passed directly through bare total variation in this run. The new theorem is a slab/singular-value statement and therefore transfers through the bounded slab kernel exactly in the approximation limit.

## 8. What remains

Theorem 5.2 pays neither branch by itself. In alternative (A), one still needs a product-compatible theorem for a cross cut with one strong singular direction but only four potentially significant directions after the exact rank-two Nystrom skeleton is removed. In alternative (B), the `>1/3` physical third-volume joint star must be reconciled with the partner's robust leaf-curvature domination graph and the simultaneous principal-triple near-singularity. Small coefficients cannot simply be deleted on unbounded/fragmented inputs.

The singular-hub and zero-diagonal-hub chambers are not covered by Theorem 5.2; they have separate source-valid compilers in the account01/B13 predecessor and must be joined without perturbing them into the invertible-hub case.

The full arbitrary-density QFORM conjecture therefore remains **OPEN / NOT PROVED / NOT DISPROVED**. Full continuity remains **OPEN**. The new theorem is a supporting target-level structural normal form pending independent review.

## 9. Source integrity

Fresh brain control before publication remained OWNER CONTROL revision `2026-09-22.15`, QFORM only, with no account02/B13 pause or stop. Fresh corrections were re-read before this write. This proof does not use uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, conditional projection-density moments, independence after rotation, a uniformly good physical minor, bounded support/diameter, fixed fragment count, or perturbative deletion of small matrix coefficients.
