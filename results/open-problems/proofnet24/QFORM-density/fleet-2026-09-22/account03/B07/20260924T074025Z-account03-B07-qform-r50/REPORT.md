SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B07, 2026-09-24T07:40:25Z.
attacking: the r49 pair-block + rank-24 + small-tail survivor — convert many large pair-block singular directions into one bounded-size physical principal core, otherwise compress the whole matched bank to fixed rank plus a small operator tail.

# account03/B07 r50 — pair-block spectral core compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW SUPPORTING STRUCTURAL LEMMA / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, moment, log-concavity, compact-support, connected-support, iid, post-rotation independence, pointwise quadratic-phase decay, arbitrary-joint coarea, fiber-supremum, or deletion of a nonzero coefficient tail is used. Pairwise orthogonal diagonalizations below are deterministic coefficient algebra only; the random variables are never rotated.

## 1. Fresh sources and exact incoming branch


The incoming worker-owned state is account03/B07 r49:

`yspennstate/math-open-problems@8faa92df02294280a5ed8315598cc4d605d71515`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T064126Z-account03-B07-qform-r49/REPORT.md`.

On r49's unpaid moderate-internal-energy branch there is an actual original-coordinate matched bank `S`, partitioned into literal physical pairs, such that

`A[S,S] = B_pair + R_24 + E_S`,                                  (1.1)

where

* `B_pair` is symmetric and block diagonal on the original physical `2 x 2` matched pairs;
* `rank R_24 <= 24`;
* `||E_S||_F < eps`, with

`eps = 5.43834026762e-4`.                                       (1.2)

The same live state also has an actual physical separator `T | S`,

`M=A[T,S]=L_2+F`,                                                (1.3)

with

`rank L_2<=2`, `||F||_F<2^-16`.                                 (1.4)

The designated partner result actually applied below is account04/B07:

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`.

Its physical-fiber theorem states: if an actual physical principal block `A[I,I]` of size `m` has

`s3(A[I,I]) >= gamma > 0`,                                      (1.5)

then the full ambient quadratic form, retaining all outside coordinates, couplings, signs and additional spectrum, satisfies

`||p_Q||_infinity <= 2 sqrt(6 pi m) / gamma`.                   (1.6)

This partner gate establishes essential boundedness; continuity is not claimed there.

## 2. New block-nullity selection lemma

### Theorem 2.1 — `QFORM-PAIRBLOCK-RANKTAIL-PHYSICAL-CORE-v1`

Let `S` be partitioned into literal physical pairs and suppose

`A[S,S]=B+R+E`,                                                  (2.1)

where `B` is symmetric block diagonal on those physical `2 x 2` pairs, `rank R<=r`, and `||E||_op<=epsilon`. Fix `d>epsilon`.

If `B` has at least `r+3` singular values at least `d`, then there is a union `I` of at most `r+3` physical pairs, hence

`|I| <= 2(r+3)`,                                                 (2.2)

such that

`boxed: s3(A[I,I]) >= d-epsilon.`                               (2.3)

Consequently the account04/B07 physical-fiber theorem gives

`boxed: ||p_Q||_infinity <= 2 sqrt(12 pi (r+3))/(d-epsilon).`   (2.4)

### Proof

Every singular direction of the symmetric pair-block matrix `B` belongs to one literal physical pair. Select physical pairs until they cover `r+3` singular directions of magnitude at least `d`; call their union `I`. Then `m=|I|<=2(r+3)` and the restricted block `B_I=B[I,I]` has a subspace

`U = span{eigenvectors of B_I with |lambda|>=d}`                 (2.5)

with `dim U>=r+3`. On `U`,

`||B_I x||_2 >= d ||x||_2`.                                    (2.6)

The restriction `R_I=R[I,I]` still has rank at most `r`, so

`dim ker R_I >= m-r`.                                           (2.7)

Therefore

`dim(U intersect ker R_I)`
` >= (r+3)+(m-r)-m = 3`.                                       (2.8)

For every `x` in this intersection,

`(B_I+R_I)x=B_I x`,                                             (2.9)

and hence `(2.6)` holds for `B_I+R_I` on a three-dimensional subspace. The max-min characterization of singular values yields

`s3(B_I+R_I)>=d`.                                               (2.10)

Finally `||E[I,I]||_op<=||E||_op<=epsilon`, so Weyl's singular-value perturbation inequality gives `(2.3)`. Equation `(2.4)` is the direct application of the completed account04/B07 theorem `(1.6)`, using `m<=2(r+3)`. QED.

The proof spends a whole bank of pair-block singular directions before selecting the bounded physical set. It never chooses or divides by a tiny coordinate minor.

## 3. Exact application to the r49 survivor

For the live r49 decomposition use

`r=24`,
`epsilon=eps=5.43834026762e-4`,
`d=2 eps=1.087668053524e-3`.                                    (3.1)

If `B_pair` has at least `27` singular values at least `d`, Theorem 2.1 gives an actual principal block on at most

`m<=54`                                                         (3.2)

physical coordinates with

`s3 >= d-eps = eps = 5.43834026762e-4`.                         (3.3)

Applying the designated account04/B07 physical-fiber result gives the concrete full-ambient inequality

`boxed: ||p_Q||_infinity < 117330.538.`                         (3.4)

This is essential boundedness only; continuity is not claimed on this partner gate.

Therefore every survivor of this payment has **at most 26** singular values of `B_pair` with magnitude at least `d`.

## 4. Global spectral truncation of the entire pair bank

On the unpaid branch, diagonalize each literal `2 x 2` coefficient block of `B_pair` only as deterministic matrix algebra. Define `B_big` by retaining all pair-block eigencomponents with `|lambda|>=d`, and let

`B_small=B_pair-B_big`.                                         (4.1)

Because the paid branch is absent,

`boxed: rank B_big <= 26`,                                      (4.2)

while by construction

`boxed: ||B_small||_op < d.`                                    (4.3)

Hence `(1.1)` becomes the dimension-free operator normal form

`boxed:
 A[S,S] = H_50 + G_S,
 rank H_50 <= 50,
 ||G_S||_op < d+eps = 3 eps
 = 1.631502080286e-3.
}`                                                               (4.4)

Here

`H_50=R_24+B_big`,                                               (4.5)

and

`G_S=B_small+E_S`.                                               (4.6)

Nothing has been deleted: every small pair-block eigencomponent and the entire Frobenius tail remain in `G_S`; they are merely controlled in operator norm. The rank bound is independent of `|S|`.

This is `QFORM-PAIRBLOCK-R50-OPTAIL-NORMALFORM-v1`.

## 5. Combine with the live global separator without losing the physical cut

The same survivor has `(1.3)-(1.4)`. Write the full coefficient matrix in the physical decomposition `T | S` as

`A = diag(A[T,T],0) + P + G`,                                   (5.1)

where

`P = [[0,L_2],[L_2^T,H_50]]`                                    (5.2)

and

`G = [[0,F],[F^T,G_S]]`.                                        (5.3)

The symmetric cross matrix `[[0,L_2],[L_2^T,0]]` has rank at most `4`, so

`boxed: rank P <= 54.`                                          (5.4)

Also

`||[[0,F],[F^T,0]]||_op=||F||_op<=||F||_F<2^-16`,              (5.5)

therefore

`boxed:
 ||G||_op
 < 3 eps + 2^-16
 = 1.6467608693485e-3.
}`                                                               (5.6)

Thus the r49 moderate-energy survivor has been reduced from a dimension-growing pair-block object to:

* arbitrary same-side curvature `A[T,T]`, retained exactly;
* one symmetric perturbation of rank at most `54` coupling into the matched bank;
* one fully retained global operator tail below `0.001647`.

This is a coefficient normal form, not a density theorem by itself. A low-rank perturbation may still carry all three large eigenvalues, so no claim is made that `A[T,T]` inherits three large eigenvalues.

## 6. Why this is stronger than the previous diagonal-pivot count

R49 plus account04/B07 already paid a branch with 27 large *physical diagonal entries*. The new theorem is orientation-free inside each literal physical pair: a pair such as

`[[0,b],[b,0]]`                                                  (6.1)

has zero diagonals but two singular values `|b|`, so it is invisible to a diagonal-pivot count. Theorem 2.1 still counts both directions. If enough such pair directions occur, the physical core is paid; otherwise every remaining unabsorbed pair block has operator norm below the fixed universal threshold `d`.

No independence is assigned to the block eigenvectors. Their only role is to certify deterministic singular values of an **actual original-coordinate principal block**; the analytic receiver is invoked only after that physical block is selected.

## 7. Finite regression checks

`CHECKS.py` and `CHECKS.txt` in this run folder recompute all constants, test 500 random pair-block spectral truncations, and include a saturation-style deterministic core example where a rank-24 perturbation cancels exactly 24 of 27 threshold singular directions. The observed third singular value equals the predicted `d-0.9 eps` to machine precision. The run ends `STATUS=PASS`.

The computation is regression evidence only; the proof is the dimension/intersection and Weyl argument above.

## 8. Remaining obstruction

This does **not** solve full QFORM. The r49 moderate-energy pair-block survivor is now routed as follows:

1. at least 27 pair-block singular directions at scale `2 eps` -> a bounded-size physical principal core -> full ambient essential-density bound `<117330.538`;
2. otherwise the matched bank has the exact normal form `rank<=50 + operator tail <0.001632`, and together with the global separator this becomes `rank<=54 + operator tail <0.001647` relative to the arbitrary `T`-side block.

The separate r49 branch

`E_star=sum_{K good} ||A[K,S\K]||_F^2 > 1`                     (8.1)

remains unpaid. The near-rank-one matched branch and earlier high-degree-hub branch also remain separate.

The next precise debt is:

`QFORM-R54-COUPLER-PLUS-ARBITRARY-TBLOCK-RECEIVER-v1` — exploit the original-coordinate product structure to consume a rank-54 symmetric coupler plus an operator tail below `0.001647` over an arbitrary retained `T`-side quadratic block, or force a paid physical E3/principal core. A complementary next step is to compile the `E_star>1` branch by determinant-weighted random cuts rather than by fiber suprema.

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.**
