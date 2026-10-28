SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B13, 2026-09-23T00:05:55Z.
attacking: counterexample normal form for the no-pivot finite-grid extreme-product class using D'/D5 cross-volume certificates and exact low cross-rank completion.

# account02/B13 — finite-grid counterexample normal form and exact cross-rank completion

Run: `20260923T000555Z-account02-B13-productset-r15-482fba`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Extremal product laws  
Status: **PROVED TARGET-LEVEL COUNTEREXAMPLE NORMAL FORM + SUPPORTING LINEAR-ALGEBRA LEMMA / FULL QFORM OPEN / CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Sources and exact scope

The target is unchanged: for every finite `n`, independent real coordinates with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one universal finite `C` with

`P(X^T A X in J) <= C |J|`

for every interval `J`, or give a genuine counterexample. No moments, bounded support, log-concavity, iid assumption, diagonal-basis assumption or post-rotation independence is used below.


The completed inputs actually applied are:

1. **Designated partner account03/B13 r19**, `yspennstate/math-open-problems@d21000e145ff5e4756c0abc8727a7c7aa1a02e4d`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260922T233245Z-account03-B13-qform-r19/REPORT.md`, Theorem 3.1. For rational `tau`, the no-`tau`-pivot slab supremum over arbitrary independent cap-one laws equals the supremum over rational finite-grid product indicators. This theorem uses finite-mixture approximation and does not assume a global bathtub optimizer, bounded diameter or bounded fragment count.
2. Its purification dependency was checked directly at `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`, Lemma 2.1/Corollary 2.2: arbitrary cap-one mass-one laws are `L1` limits of finite convex combinations of unit-measure indicators of bounded finite unions of intervals, and bounded product functionals have the same supremum on these extreme products.
3. **Required Claude-attributed Fourier source**, `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. I use two proved extensions of the decoupled volume theorem: `D'` and `D_5` with their stated constants.
4. **Newest no-pivot synthesis**, `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`, Theorem 5.1. Subject to its supplied one-eigenvalue small-ball dependency, a finite universal no-`tau`-pivot three-eigenvalue density constant implies the full conjecture. I use it only for the contrapositive reduction to the no-pivot class, not as a claim that N3 is solved.

The full theorem remains open. The separate continuity conclusion remains open.

## 2. First unpaid implication

The current B13 gap is no longer purification or countability. It is:

**`QFORM-NOPIVOT-CROSSRANK4-STABILITY-v1`.** Control the finite-grid no-pivot class when every original-coordinate disjoint cross block is uniformly close to rank at most four, and every cross block carrying a non-negligible third singular direction has its volume-sampling third-minor mass simultaneously anchored on one physical row and one physical column. The estimate must be dimension-free and must tolerate arbitrary grid mesh, support radius, translations, gaps and fragment count.

The theorem below shows that any full counterexample can be forced into exactly this asymptotic geometry. Section 4 gives the exact zero-error endpoint: uniformly bounded disjoint cross rank implies diagonal plus bounded rank. What is still missing is a quantitative, product-compatible stability bridge; raw small operator perturbation is not allowed because supports can be unbounded.

## 3. Counterexample normal form from partner purification plus D'/D5

Let

`C3 = 9 sqrt(3e) = 25.701021075349...`,

`C5 = 5 sqrt(2e) = 11.658219907985...`.

### Theorem 3.1 — `QFORM-NOPIVOT-GRID-CROSSRANK-NORMAL-FORM-v1`

Assume the full QFORM essential-density conjecture is false. Then for every integer `m>=2` there exist:

- a finite dimension `n_m`;
- a rational symmetric matrix `A_m` with `s_3(A_m)>1`;
- a rational interval `J_m`;
- a common rational grid and unit-measure product sets `E_{m,i}`, each a finite union of grid cells;

such that, for `P_m=prod_i E_{m,i}`,

`|{x in P_m : x^T A_m x in J_m}| / |J_m| > C3 m`,                 (3.1)

and all the following deterministic matrix properties hold.

**(a) Vanishing physical entries and forced dimension growth.**

`|A_{m,ii}| < m^(-4)`,

`|det A_m[{i,j},{i,j}]| < m^(-4)` for every `i!=j`,                (3.2)

hence

`max_{i,j}|A_{m,ij}| < sqrt(m^(-4)+m^(-8)) <= sqrt(2) m^(-2)`.   (3.3)

Because `s_3(A_m)>1`,

`||A_m||_F^2 > 3`,

and (3.3) implies

`n_m > sqrt(3/2) m^2`.                                             (3.4)

Thus any counterexample sequence in this normal form is necessarily high-dimensional and entrywise diffuse.

**(b) Every original-coordinate disjoint cross block is asymptotically rank at most four.**

For every disjoint `I,J` let `M=A_m[I,J]`. Then

`s_5(M) < (C5/C3) m^(-1) < m^(-1)`.                              (3.5)

Equivalently, every physical cross block is within operator norm `<1/m` of a rank-at-most-four matrix (its truncated SVD; this is a deterministic matrix statement only, not a rotation of the random coordinates).

**(c) Any surviving third cross direction is doubly physically anchored.**

Suppose for a disjoint cut `I,J` one has

`s_3(M) >= m^(-1)`.                                                (3.6)

Let

`Z3=e_3(M^T M)=sum_{|S|=|T|=3} det(M[S,T])^2`,

and let

`w_{S,T}=det(M[S,T])^2/Z3`

be the volume-sampling law. Define row and column marginals

`alpha_i=P_w(i in S)`, `beta_j=P_w(j in T)`.

Then there exist a physical row `i in I` and a physical column `j in J` with

`alpha_i > 2/3`, `beta_j > 2/3`.                                  (3.7)

Consequently

`P_w(i in S and j in T) > 1/3`,                                  (3.8)

so more than one third of the entire squared `3x3`-minor mass of this cut is carried by minors containing the same row `i` and the same column `j`. Since the marginals each sum to three, there are at most four rows with `alpha_i>2/3` and at most four columns with `beta_j>2/3`.

No support, moment, connectedness or fragment-count restriction is present in this normal form.

### Proof

Fix `m>=2` and put

`tau_m=m^(-4)`.

By the newest no-pivot synthesis, if the strict no-`tau_m`-pivot three-eigenvalue class had any finite universal density constant, the full QFORM conjecture would have a finite universal constant. Under the assumption that full QFORM is false, its no-pivot slab constant is therefore infinite. The designated partner's exact countable-extreme equivalence then says the rational finite-grid constant is also infinite. Hence choose a grid datum with slab ratio exceeding `C3 m`. This gives (3.1) and the strict no-pivot inequalities (3.2), with `s_3(A_m)>1`.

For `i!=j`,

`det A[{i,j},{i,j}] = A_ii A_jj - A_ij^2`,

so

`|A_ij|^2 <= |A_ii A_jj| + |det A[{i,j},{i,j}]| < tau_m^2+tau_m`.

Together with the diagonal bound this proves (3.3). Since three singular values exceed one, `||A_m||_F^2>3`; on the other hand `||A_m||_F^2 <= n_m^2 max_{ij}|A_ij|^2 < 2 n_m^2 m^(-4)`, proving (3.4).

Now fix any disjoint cut and write `M=A_m[I,J]`.

The proved `D_5` theorem gives, with `Z5=e_5(M^TM)`,

`||p_Q||_infty <= C5 Z5^(-1/10)`                                  (3.9)

whenever `Z5>0`, with no marginal condition; if `Z5=0`, then `s_5(M)=0` already. Since the actual grid witness has a slab ratio greater than `C3 m`, (3.9) forces

`Z5 < (C5/(C3 m))^10`.

But `Z5>=s_1(M)^2...s_5(M)^2>=s_5(M)^10`, so (3.5) follows.

For the third-volume statement, suppose `Z3>0`. The proved `D'` theorem with `h=2/3` gives, whenever `max_i alpha_i<=2/3`,

`||p_Q||_infty <= 6 sqrt(e) (4/3)^(-1/2) (1/3)^(-1) Z3^(-1/6)`

`                 = C3 Z3^(-1/6)`.                               (3.10)

If every row marginal were at most `2/3`, the slab ratio `>C3 m` would force `Z3<m^(-6)` and hence `s_3(M)<1/m`, because `Z3>=s_3(M)^6`. Therefore (3.6) implies a row with `alpha_i>2/3`.

Apply the same theorem to the transposed cut `M^T=A_m[J,I]`. Its volume weights are the same with rows and columns exchanged, so (3.6) also implies a column with `beta_j>2/3`. Under `w`, the union bound gives

`P(i in S and j in T) >= alpha_i+beta_j-1 > 1/3`,

which is (3.8). The count of heavy rows/columns follows from `sum_i alpha_i=sum_j beta_j=3`. This proves the theorem. ∎

### What was actually imported from the required newest source

This is a genuine inequality-level application of `FOURIER_ROUTE_REPORT.md`, not a citation-only mention:

- `D_5` converts a diverging slab ratio directly into the all-cuts bound `s_5(A[I,J])<1/m`;
- `D'` at the explicit threshold `h=2/3` converts every surviving `s_3>=1/m` cross block into a physical row/column double-anchor for its third-minor volume law.

The argument keeps the original physical coordinate cuts and the exact product-grid law throughout.

## 4. Exact endpoint: bounded disjoint cross rank implies diagonal plus bounded rank

The normal form above suggests an algebraic endpoint. The following lemma is exact and independent of probability.

### Theorem 4.1 — `QFORM-DISJOINT-CROSSRANK-COMPLETION-v1`

Let `A` be a finite real symmetric matrix and suppose

`rank A[I,J] <= r`                                                   (4.1)

for every pair of disjoint coordinate sets `I,J`. Then there exist a diagonal matrix `D` and a symmetric matrix `R` such that

`A=D+R`, `rank R <= 4r`.                                            (4.2)

In particular, if every disjoint cross block has rank at most four, then `A` is diagonal plus a symmetric matrix of rank at most sixteen.

### Proof

The case `r=0` is immediate: every off-diagonal entry vanishes. Assume `r>=1` and replace `r` by the maximum disjoint cross rank if necessary. Choose disjoint coordinate sets `P,Q`, each of size `r`, so that

`B=A[P,Q]`

is invertible. Let `K` be the remaining coordinates and `S=P union Q`.

For distinct `k,l in K`, the `(r+1)x(r+1)` disjoint cross minor with rows `P union {k}` and columns `Q union {l}` has determinant zero. Since `B` is invertible, its Schur complement gives

`A_kl = A[k,Q] B^(-1) A[P,l]`.                                     (4.3)

Swapping `k,l` gives the transpose companion

`A_kl = A[k,P] (B^T)^(-1) A[Q,l]`.                                (4.4)

Define the invertible symmetric `2r x 2r` matrix

`H = [[0, 2B], [2B^T, 0]]`,                                        (4.5)

and put

`C=A[S,K]`.

Define `R1` in the block decomposition `S union K` by

`R1_SS=H`, `R1_SK=C`, `R1_KS=C^T`, `R1_KK=C^T H^(-1) C`.           (4.6)

Its Schur complement relative to `H` is zero, hence

`rank R1 <= 2r`.                                                    (4.7)

For `k,l in K`, direct inversion of (4.5) gives

`(R1)_kl`
` = (1/2)[A[k,P](B^T)^(-1)A[Q,l] + A[k,Q]B^(-1)A[P,l]]`
` = A_kl`                                                           (4.8)

whenever `k!=l`, by (4.3)-(4.4). By construction `R1` also matches every entry of `A` between `S` and `K`.

It remains only to repair off-diagonal entries inside the `2r`-coordinate set `S`. Let `R2` be any symmetric matrix supported on `S x S` whose off-diagonal entries there equal those of `A-R1` and whose diagonal is zero. Then

`rank R2 <= 2r`.                                                    (4.9)

Set `R=R1+R2`. It matches every off-diagonal entry of `A`, and

`rank R <= rank R1+rank R2 <= 4r`.                                (4.10)

Finally set `D=A-R`; since all off-diagonal entries cancel, `D` is diagonal. ∎

### Why this is not yet the full theorem

Theorem 3.1 gives only `s_5(A[I,J])=o(1)` uniformly over cuts, not exact rank four. A quantitative version of Theorem 4.1 with a dimension-free error notion compatible with arbitrary unbounded product supports is not automatic. In particular, small matrix/operator perturbations cannot simply be discarded on unbounded inputs. The current correction history contains explicit warnings against that shortcut.

The exact endpoint does, however, identify the correct structural target: the obstruction is a stability/deshearing problem for a bounded-rank physical bank plus a diagonal bank, not a search for one uniformly good principal minor.

## 5. Deterministic sanity check

A deterministic local checker used random matrices of the form `A=diag(d)+UU^T`, for which every disjoint cross block has rank at most `r`. For `n=7,8,9,10`, `r=1,2,3` when `2r<=n`, and 20 seeded trials per pair, it reconstructed `D,R` exactly by the proof above. Across 240 trials:

- maximum reconstruction error: `7.194e-14`;
- maximum observed `rank(R)/(4r)`: `0.75`;
- `C3=25.701021075349281`;
- `C5=11.658219907985622`;
- `C5/C3=0.453609211626515`.

The checker output terminates with `QFORM_B13_R15_CHECK_PASS`. This finite computation is diagnostic only; Theorems 3.1 and 4.1 are analytic.

## 6. Status and next step

**Target-level movement:** assuming the supplied full-to-no-pivot reduction, any genuine failure of full QFORM has a counterexample sequence inside the partner's finite rational grid class with vanishing physical entries, dimension at least order `m^2`, all physical disjoint cross blocks asymptotically rank at most four, and every non-negligible third cross direction doubly anchored in the exact volume-sampling sense.

**Mechanism-level movement:** the exact zero-error endpoint is proved: cross rank at most `r` on every disjoint cut implies `A=diagonal+R` with `rank R<=4r`.

**Still unpaid:** prove a dimension-free quantitative/product-compatible stability version sufficient to pay the finite-grid slab inequality, or construct a diverging finite-grid sequence satisfying Theorem 3.1. The bound may not use moments, bounded supports, fixed fragment counts, post-rotation independence, arbitrary-joint coarea, or a single-minor reciprocal selection.

Full QFORM essential boundedness is **OPEN**. Continuity is **OPEN**.
