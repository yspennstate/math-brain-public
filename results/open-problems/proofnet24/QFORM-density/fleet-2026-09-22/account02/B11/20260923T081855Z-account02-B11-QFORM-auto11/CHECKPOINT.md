# account02/B11 auto11 — early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.  Full target remains OPEN.  Execution is `WITHOUT_VERIFIED_BRAIN`.

First unpaid implication attacked: sharpen the designated partner's balanced sign-gauged defect endpoint.  In the partner notation, after a deterministic sign gauge on ORIGINAL coordinates,

- `A_ii>0`,
- `0<=A_ij<=sqrt(A_ii A_jj)`,
- `u_i=sqrt(A_ii)`, and
- `F=uu^T-A` is symmetric, hollow, and entrywise nonnegative.

The completed designated-partner result account03/B11 r24 (`math-open-problems@879d132f1c4b5f5b45ab890c4121744e6e2573d5`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T061800Z-account03-B11-QFORM-r24/REPORT.md`) proves a defect-STAR versus disjoint defect-2-volume dichotomy and pays the diffuse pure-star endpoint by mixed Fresnel.  Its first remaining branch is the high-leverage / grouped endpoint.  I isolate the exact zero-disjoint-volume geometry.

## 1. New zero-disjoint-volume support classification

Assume every disjoint `2x2` defect minor vanishes.  Equivalently, for every four distinct indices `i,j,k,l`,

`F_ik F_jl = F_il F_jk`.

Permuting the same four indices gives the stronger symmetric tetrad identity

`F_ij F_kl = F_ik F_jl = F_il F_jk`.                              (1)

Let `G` be the support graph with edge `ij` iff `F_ij>0`.

**Lemma (support classification).**  There is at most one nontrivial connected component of `G`, and that component is either a star or a clique.

Proof.  If two vertex-disjoint positive edges `ij` and `kl` exist, then (1) forces all four cross edges positive, so the four endpoints induce `K4`.  Hence two distinct nontrivial connected components are impossible.  In the unique nontrivial component, if the matching number is one, all edges intersect pairwise; a simple pairwise-intersecting edge family is either a star or a triangle, and a triangle is a clique.  If the matching number is at least two, choose two disjoint edges; their endpoints form `K4`.  Any vertex adjacent to one vertex of this clique is, by applying (1) to its incident edge and an edge of the clique disjoint from it, adjacent to every clique vertex.  Induction along a path shows the whole connected component is complete.  QED.

**Lemma (weights on the clique).**  If the nontrivial component is a clique `E`, there are positive numbers `c_i`, `i in E`, such that

`F_ij=c_i c_j` for every distinct `i,j in E`,

and `F_ij=0` if either index lies outside `E`.

For `|E|=2,3` this is immediate (for a triangle take `c_1=sqrt(F_12 F_13/F_23)` and cyclically).  For `|E|>=4`, fix vertex 1.  The tetrads imply that `F_ij/F_1j` is independent of the auxiliary `j`, hence the off-diagonal matrix has multiplicative rank one; the same triangle normalization gives the displayed factorization.

Thus the partner's exact zero-disjoint-volume endpoint has only two graph geometries: a literal defect star, or a factorized defect clique.  The former is exactly the geometry for which r24's mixed-Fresnel pure-star receiver was designed.  The latter is different and is closed below in exact rank three.

## 2. Exact-rank-three factorized clique compresses to at most six independent variables

Assume now the target matrix has exact rank three and indefinite signature `(+,+,-)` or `(+,-,-)`, with its three nonzero eigenvalues of modulus at least one.  In the factorized-clique branch extend `c_i=0` off `E` and put `D=diag(c_i^2)`.  Since `F` is hollow,

`F = c c^T-D`,

so

`A = uu^T-c c^T+D`.                                                (2)

The first two terms have rank at most two.  Therefore

`rank D <= rank A + rank(uu^T-c c^T) <= 3+2=5`.                    (3)

But `rank D=|E|`, hence

`|E|<=5`.                                                          (4)

Let `O=E^c`.  Formula (2) shows that every dependence of the quadratic form on `X_O` is through the single ORIGINAL-bank linear form

`Z_0=<u_O,X_O>/||u_O||`                                           (5)

when `u_O!=0`; if `u_O=0` the outside coordinates are absent.  `Z_0` is independent of the individual coordinates `X_i`, `i in E`, because the banks are disjoint, and the standard one-dimensional product-marginal theorem gives `||p_{Z_0}||_infinity<=sqrt(2)`.

Consequently `Q=X^TAX` is exactly a quadratic form in at most `|E|+1<=6` independent scalar variables `(Z_0,X_E)`.  This is an algebraic compression before any reciprocal local-minor payment; no spectral rotation is declared independent.

The compressed matrix `C` has exactly the same three nonzero eigenvalues as `A`: deterministically, an orthogonal basis change on the `O` coordinate space sends `u_O` to its first axis and puts `A` into `C direct_sum 0`.  This is only a matrix statement and is not used to rotate the product law.

Scale only the aggregate variable: `Y_0=sqrt(2)Z_0`, so every scalar input now has density cap at most one.  The new coefficient matrix is `C'=SCS`, `S=diag(1/sqrt(2),1,...,1)`.  Hence

`s_3(C') >= sigma_min(S)^2 s_3(C) >= 1/2`,                       (6)

and Sylvester inertia preserves the indefinite signature.

Now apply the completed finite-dimensional projected-gradient theorem at `math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Corollary 4.1.  With `m<=6` and `sigma=1/2`,

`||p_Q||_infinity <= 2 sqrt(6 pi m)/(1/2) <= 24 sqrt(pi) < 42.54`. (7)

This proves a universal essential-density bound for the entire exact-rank-three factorized-clique endpoint.

## 3. Required newest-Claude result applied on an actual side of the same branch

Use the required pinned package `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, Theorem C.  It gives the ruled one-sheet bound `pi sqrt(2)` for exact-rank-three `(+,+,-)` forms with all three magnitudes at least one.

For the cap-one compressed matrix `C'`, (6) gives magnitudes at least `1/2`.  Apply Theorem C to `2C'`.  Since `p_Q(s)=2 p_{2Q}(2s)`, on the majority-sign one-sheet side

`p_Q(s) <= 2 pi sqrt(2)`.                                         (8)

Thus (8) pays the ruled one-sheet side directly from the required `e5f71...` source; the finite-core bound (7) pays the remaining two-sheet side in this branch.  Negating the form exchanges `(+,+,-)` and `(+,-,-)` and reverses the level side.

## 4. Where the third direction kills the rank-two logarithm

The mandatory control remains `2XY` for independent centered unit uniforms, whose density is logarithmically unbounded at zero.  Algebraically, the factorized clique decomposes as

`A=(uu^T-c c^T)+D`.

The bracket has rank at most two and is exactly the kind of opposite-sign saddle capable of the logarithmic singularity.  Exact rank three forces `D!=0`; more strongly, (3) localizes the whole diagonal correction to at most five original coordinates.  After the product-preserving compression, the completed projected-gradient proof uses a three-dimensional substantial eigenspace.  Removing one original coordinate leaves a **two-dimensional** product marginal, and the singular kernel is `1/|y-z|`, whose polar integral is finite.  At rank two the analogous removal leaves a one-dimensional marginal and the kernel `1/|t|`, giving the logarithm.  This identifies the third direction geometrically rather than asserting that the rank-two density itself became bounded.

## 5. Remaining implication after this checkpoint

The factorized-clique exact endpoint is paid.  The unpaid balanced-defect work is now narrower:

`QFORM-BALANCED-DEFECT-W-STABILITY-v1`: obtain a quantitative stability version when the disjoint defect-minor mass is small but nonzero, or close the high-augmented-leverage literal-star branch by a product-preserving grouped/pair/ridge receiver.  Arbitrary additional spectrum remains a separate debt; the rank argument `|E|<=5` used exact rank three and is not silently extended to the full matrix problem.
