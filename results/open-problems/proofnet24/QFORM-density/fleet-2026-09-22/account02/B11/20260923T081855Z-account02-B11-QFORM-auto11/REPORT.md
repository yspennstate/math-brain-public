SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-23T08:18:55Z.
attacking: the balanced two-sheet defect endpoint by classifying zero disjoint defect 2-volume, then paying the factorized-clique exact-rank-three branch without post-rotation independence.

# account02/B11 auto11 — zero-disjoint-defect classification and the factorized-clique compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **ESSENTIAL_STEP_APPLIED / PROVED_STRUCTURAL_ENDPOINT / PROVED_EXACT-RANK3 FACTORIZED-CLIQUE BRANCH / REQUIRED CLAUDE RESULT APPLIED / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN**.

The unrestricted theorem remains OPEN.  This report sharpens the balanced sign-gauged branch left by the previous B11 run.  The new exact statement is: when the designated partner's disjoint defect `2x2` volume is exactly zero, the defect support is not arbitrary.  It is either a literal star or one factorized clique.  In exact rank three the clique can occupy at most five original coordinates; after one product-preserving bank compression the entire form lives on at most six independent cap-one scalars and is universally bounded.  The literal-star branch is the geometry of the partner's mixed-Fresnel receiver and remains open only at its high-leverage endpoint.

No moment, support, log-concavity, identical-law, spectral-coordinate independence, arbitrary-joint coarea estimate, worst conditional density cap, or small-random-perturbation argument is used.

## 1. Source map and the first unpaid implication

Fresh owner control before publication remained revision `2026-09-22.15`, sole programme `QFORM-DENSITY-3EIG-20260922`.

Sources used at equations:

1. **Designated partner account03/B11 r24**, available at
   `yspennstate/math-open-problems@e7fdc2430ce640363582b98adce7771f8797e686`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T061800Z-account03-B11-QFORM-r24/REPORT.md`.
   It proves the balanced defect STAR/CROSS-2VOL dichotomy and the diffuse pure-star mixed-Fresnel receiver.
2. **Required pinned Claude package**
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.
   `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` were read.  Theorem C from `COUNTEREXAMPLE_SEARCH.md` is applied below to an actual one-sheet density inequality.
3. **Finite-dimensional projected-gradient theorem**
   `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`,
   `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Corollary 4.1.
4. The preceding account02/B11 overlapping-pair theorem at
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T065551Z-account02-B11-QFORM-8cd8bcc4/REPORT.md`, retained as the quantitative physical-indefinite-pair exit and the rank-two logarithmic control.

The first unpaid implication entering this run was the partner's balanced sign-gauged no-good-pair chamber.  After an ORIGINAL-coordinate sign gauge, its hypotheses are

`A_ii>0`, `0<=A_ij<=sqrt(A_ii A_jj)`,

so with

`u_i=sqrt(A_ii)`, `F=uu^T-A`,                                      (1.1)

we have

`F_ii=0`, `F_ij>=0`.                                               (1.2)

The partner proves `s_2(F)>=s_3(A)`.  Writing

`q_i=sum_(j!=i) F_ij^2`,
`V_2=e_2(F^T F)`,
`P=sum_(i<j)F_ij^4`,
`W=sum of squared 2x2 minors with four distinct physical indices`,

its exact identity is

`V_2 = W + sum_i q_i^2 - P`.                                      (1.3)

If the incident contribution dominates, it gives

`max_i q_i >= s_3(A)^2/4`.                                        (1.4)

If not, a random original-coordinate cut gives a disjoint block with fixed second exterior volume.  The previously unclassified exact endpoint is therefore `W=0`, where (1.4) forces a STAR certificate but does not say the defect matrix itself is a literal star.  The next theorem classifies that endpoint.

## 2. Zero disjoint defect volume: support is star or clique

Assume throughout this section that `F` is symmetric, hollow, entrywise nonnegative, and every disjoint `2x2` minor vanishes.  For four distinct indices `i,j,k,l`, one such minor gives

`F_ik F_jl = F_il F_jk`.                                         (2.1)

Permuting the same four indices gives

`boxed(F_ij F_kl = F_ik F_jl = F_il F_jk)`.                      (2.2)

Let `G_F` be the simple support graph with edge `ij` iff `F_ij>0`.

### Theorem 2.1 — `QFORM-ZEROW-STAR-OR-CLIQUE-v1`

`G_F` has at most one nontrivial connected component.  That component is either

1. a star, or
2. a complete graph.

### Proof

If `ij` and `kl` are two vertex-disjoint positive edges, the first product in (2.2) is positive.  Hence both other matching products are positive, so all four cross edges among `{i,j,k,l}` are positive.  Thus the four endpoints induce `K_4`.

This immediately excludes two distinct nontrivial connected components: choose one edge from each and the preceding argument creates cross edges.

Consider the unique nontrivial connected component, if it exists.  If its matching number is at most one, every two edges intersect.  A pairwise-intersecting family of edges in a simple graph is either a star or a triangle: choose intersecting edges `ab,ac`; if not every edge contains `a`, any edge avoiding `a` must meet both and is therefore `bc`, after which every further edge is one of the triangle edges.  A triangle is a clique.

If the matching number is at least two, choose disjoint edges.  Their four endpoints form `K_4`.  Let `x` be a vertex adjacent to a vertex `a` of a complete subgraph of size at least four.  For any other clique vertex `z`, choose an edge `pq` of the clique disjoint from `{x,a}` and with one endpoint arranged so that the four-vertex identity includes `xz`; (2.2) and positivity of `xa` and `pq` force `xz>0`.  Thus `x` is adjacent to every clique vertex.  Induction along a path from the initial `K_4` proves that the whole connected component is complete.  QED.

This classification is scale-free and purely algebraic.  It does not select a uniformly good physical minor.

## 3. The clique weights factor exactly

### Lemma 3.1 — multiplicative weights

If the nontrivial component is a clique `E`, there are positive `c_i`, `i in E`, such that

`F_ij=c_i c_j` for all distinct `i,j in E`,                       (3.1)

and `F_ij=0` when either index lies outside `E`.

### Proof

For `|E|=2` this is trivial.  For a triangle set

`c_1=sqrt(F_12 F_13/F_23)`,
`c_2=F_12/c_1`, `c_3=F_13/c_1`.

For `|E|>=4`, fix vertex `1`.  From the disjoint minor with rows `i,1` and columns `j,k`,

`F_ij F_1k=F_ik F_1j`,                                          (3.2)

so for fixed `i`, the ratio `F_ij/F_1j` is independent of the auxiliary `j`.  Symmetry then shows these row ratios are themselves proportional to `F_1i`; equivalently the off-diagonal clique matrix has multiplicative rank one.  The same normalization as for a triangle yields (3.1).  QED.

Extend `c_i=0` outside `E` and put

`D=diag(c_i^2)`.                                                  (3.3)

Because `F` is hollow,

`F=cc^T-D`, and therefore

`boxed(A=D+uu^T-cc^T)`.                                          (3.4)

Thus the exact zero-disjoint-volume clique endpoint is a **diagonal plus rank-two** matrix, not a mysterious collective star.

## 4. Exact rank three forces the clique onto at most five coordinates

Assume now that `A` has exact rank three, indefinite signature `(+,+,-)` or `(+,-,-)`, and its three nonzero eigenvalues have modulus at least one.

Since `uu^T-cc^T` has rank at most two, (3.4) gives

`rank(D) <= rank(A)+rank(uu^T-cc^T) <= 3+2=5`.                   (4.1)

But `D` is diagonal and positive exactly on the clique support, so

`boxed(|E|<=5)`.                                                  (4.2)

Let `O=E^c`.  The block formula (3.4) shows that all dependence on the outside original coordinates is through the single scalar

`Z_0=<u_O,X_O>/||u_O||`                                          (4.3)

when `u_O!=0`; if `u_O=0`, the outside variables are absent.  The bank `O` is disjoint from the individual coordinates in `E`, so `Z_0` is genuinely independent of `X_E`.  The standard one-dimensional product-marginal theorem gives

`||p_Z0||_infinity <= sqrt(2)`.                                  (4.4)

No rotated spectral coordinate is being declared independent.

Hence `Q=X^TAX` is exactly a quadratic form in at most six independent scalars

`(Z_0,(X_i)_(i in E))`.                                          (4.5)

Let `C` be its coefficient matrix.  Deterministically, an orthogonal basis change **only for matrix analysis** on the coordinate space `O` sends `u_O` to its first axis and puts the original matrix into

`C direct_sum 0`.                                                 (4.6)

Therefore `C` has exactly the same three nonzero eigenvalues as `A`.

Normalize the one aggregate law by `Y_0=sqrt(2)Z_0`.  Every input coordinate now has density cap at most one.  If

`S=diag(1/sqrt(2),1,...,1)`, `C'=SCS`,                            (4.7)

then the singular-value inequality for invertible left/right multiplication gives

`s_3(C') >= sigma_min(S)^2 s_3(C) >= 1/2`.                        (4.8)

Congruence preserves inertia, so the signature is unchanged.

Apply the completed finite-dimensional projected-gradient theorem, Corollary 4.1 of the source in item 3 above.  With `m<=6`, `sigma=1/2`,

`||p_Q||_infinity`
` <= 2 sqrt(6 pi m)/(1/2)`
` <= 24 sqrt(pi)`
` = 42.5388924217... .                                           (4.9)

### Theorem 4.1 — `QFORM-FACTORIZED-CLIQUE-EXACT-RANK3-v1`

Under the exact-rank-three balanced sign-gauged hypotheses and `W=0`, if the defect support is the clique alternative of Theorem 2.1, then

`boxed(||p_(X^TAX)||_infinity <=24 sqrt(pi)<42.54)`.              (4.10)

This is an essential-density statement.  Continuity is not added here beyond whatever is supplied by the invoked finite-dimensional theorem.

## 5. Required pinned Claude ruled theorem applied at the actual one-sheet inequality

The required source `math-open-problems@e5f71d79.../COUNTEREXAMPLE_SEARCH.md`, Theorem C, proves for exact-rank-three signature `(+,+,-)` with all three eigenvalue magnitudes at least one that on the one-sheet/cone side

`p(s)<=pi sqrt(2)`, `s>=0`.                                       (5.1)

For the cap-one compressed matrix `C'`, (4.8) gives eigenvalue magnitudes at least `1/2`.  Apply Theorem C to `2C'`.  Since scaling the output gives

`p_Q(s)=2 p_(2Q)(2s)`,                                            (5.2)

we obtain the actual branch inequality

`boxed(p_Q(s)<=2 pi sqrt(2)<8.886, s>=0)`                         (5.3)

for signature `(+,+,-)`.  For signature `(+,-,-)`, apply (5.3) to `-Q`; the ruled estimate pays `s<=0`.

Thus the newest-Claude result is used at its exact geometric scope: the ruled theorem pays the majority-sign one-sheet side.  The finite-core estimate (4.9) pays the complementary two-sheet side in the factorized-clique branch.  I do not extend the ruled estimate to the two-sheet side; the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids such a line-marginal shortcut.

## 6. Exactly how the third direction removes the rank-two logarithm here

Keep the mandatory control: for independent centered unit uniforms,

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`,                         (6.1)

so an opposite-sign rank-two saddle has a real logarithmic singularity.

In the clique endpoint,

`A=(uu^T-cc^T)+D`.                                                (6.2)

The bracket has rank at most two and can carry exactly that saddle mechanism.  The third direction is not a claim that the bracket's density became bounded.  Exact rank three forces `D!=0`; moreover (4.1) localizes the entire diagonal correction to at most five ORIGINAL coordinates.  After the product-preserving compression, the finite-dimensional projected-gradient proof uses a three-dimensional substantial eigenspace.  Deleting one original coordinate leaves a two-dimensional product marginal and the singular kernel is

`1/|y-z|`.                                                        (6.3)

The two-dimensional polar integral near the singularity is finite:

`integral_0^r (rho d rho)/rho = r`.                               (6.4)

At rank two the analogous projected-gradient argument leaves only a one-dimensional marginal and the singular kernel `1/|t|`, whose integral is

`integral_0^r dt/t`,                                              (6.5)

the logarithm in (6.1).  This is the geometric reason the third direction removes the singularity in the branch proved here, while retaining the rank-two failure as a genuine endpoint.

## 7. Why the exact-rank-three hypothesis in (4.2) cannot be silently dropped

The bare target assumes **at least** three large eigenvalues and allows arbitrary additional spectrum.  The deduction `|E|<=5` uses `rank(A)=3` essentially.  The following target-valid family makes that explicit.

For arbitrary `n>=3`, let

`d=(1/10, 2/5, 3/2, 1/100, ..., 1/100)`,
`u_i=5`, `c_i=5 d_i`,                                             (7.1)

and define the hollow factorized defect

`F_ij=c_i c_j` for `i!=j`, `F_ii=0`,
`A=uu^T-F`.                                                       (7.2)

Then

`A_ii=25`,
`A_ij=25(1-d_i d_j)>=0`,                                         (7.3)

because every pair product `d_i d_j<=1`.  Every physical `2x2` pair is PSD since

`det A[{i,j}] =625[1-(1-d_i d_j)^2]>=0`.                          (7.4)

The defect support is a clique on all `n` vertices and all disjoint tetrads vanish exactly.

The principal block on the first three coordinates is `25 C`, where

`C=[[1,24/25,17/20],
    [24/25,1,2/5],
    [17/20,2/5,1]]`.                                             (7.5)

Its upper-left `2x2` principal block has eigenvalues `49/25` and `1/25`.  Cauchy interlacing therefore gives the two largest eigenvalues of `C` at least `49/25` and `1/25`.  Also

`det C=-1513/10000<0`,                                           (7.6)

so the third eigenvalue is negative, and its characteristic polynomial satisfies

`chi_C(-1/10)=71/100000>0`.                                      (7.7)

Since the middle eigenvalue is positive, (7.7) puts the negative eigenvalue strictly below `-1/10`.  Thus `25C` has two positive eigenvalues at least `49` and `1`, and one negative eigenvalue below `-5/2`.

Interlacing from this principal block to the full `A` gives at least two positive eigenvalues `>=1` and one negative eigenvalue `<=-5/2`.  Hence every matrix (7.2) is a valid member of the **full** QFORM target, while its factorized clique support has arbitrary cardinality `n`.

This is not a QFORM counterexample; here the large physical diagonals already give easy exits.  It is a source-valid counterexample to the invalid extrapolation

`three large eigenvalues + factorized clique => clique supported on O(1) coordinates`. (7.8)

The next full-matrix argument must therefore use the diagonal-plus-rank-two product structure itself, not the exact-rank-three support count.

## 8. Designated partner result: what is now removed and what is still unpaid

The partner r24 theorem is used at the structural inequality (1.4): in the balanced pair-PSD chamber with `s_3(A)>=1`, a `W=0` form is forced into the STAR side with `max q_i>=1/4`.  Theorems 2.1 and 3.1 now show that this exact endpoint has only two actual support geometries:

- **literal star:** the partner's mixed-Fresnel pure-star theorem pays it whenever its augmented frame has leverage at most `1/2` and nonzero transverse area;
- **factorized clique:** Theorem 4.1 above pays the entire exact-rank-three branch, with no leverage hypothesis.

So the zero-disjoint-volume endpoint is no longer an amorphous collective STAR state.

The first unpaid B11 implication is now

**`QFORM-TETRAD-CLIQUE-FULLRANK-v1` (OPEN):** for the full-matrix factorized-clique geometry

`A=D+uu^T-cc^T`, `D=diag(c_i^2)>=0`,                              (8.1)

under only the target assumption of at least three eigenvalues of magnitude at least one and the balanced pair-PSD inequalities, prove a universal density bound by a product-preserving sign-specific Schur / separable-rank-two fractional argument, or force an existing physical-pivot/pair/volume exit.  The family in Section 7 shows that finite support cannot be inferred from the target alone.

After that exact endpoint, the quantitative stability problem `W small but nonzero` and the high-augmented-leverage literal-star endpoint remain.  Arbitrary extra spectrum is never discarded as a small random perturbation.

## 9. Finite regression check and source discipline

`VERIFY.py` exhaustively checks every unweighted support graph through six vertices satisfying the four-vertex tetrad support condition.  Counts are

`2, 8, 28, 82, 214` for `n=2,...,6`,

and every one is classified as empty/star/clique.  It also checks the displayed constants.  The captured output ends

`QFORM_TETRAD_ENDPOINT_CHECK_PASS`.

This finite check is regression only; the proofs are Sections 2-5.

No claim of full QFORM completion is made.  The exact-rank-three clique theorem is a supporting theorem pending independent review; the ruled estimate is used only on the one-sheet side; the full-rank construction is an obstruction to a proof extrapolation, not to the conjecture itself.
