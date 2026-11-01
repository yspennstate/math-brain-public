# fleet01/B09 r18 — cut-rank-one gluing and pair-to-Schur bilinear routing

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Bilinear block mechanism  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW_STRUCTURAL_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  

## 0. Target and source discipline

The full target remains open: for every independent real coordinate vector with one-dimensional densities bounded by one, and every real symmetric matrix A with `s_3(A)>=1`, prove a universal bound on the density of `X^T A X`, or give a genuine counterexample. No rotated-coordinate independence, moments, support regularity, or pointwise van-der-Corput estimate is used below.


The second source applied is fleet03/B20 r16, `QFORM-SCHUR-RIDGE-OR-UNIFORM-NEARRANK1-v1`, canonical source `yspennstate/math-open-problems@241e781422352daf5ca803898f1e2d20f4dfda8e`, whose unpaid survivor satisfies a quantitative all-cut near-rank-one condition and the approximate tetrads recorded below.

---

# 1. Exact classification of the all-cut rank-one geometry

Let `S=(s_ij)` be a real symmetric matrix. Ignore its diagonal and form the support graph

`G_S = { {i,j}: i!=j and s_ij !=0 }`.

Assume

> `rank S[L,R] <=1` for every disjoint coordinate sets `L,R`.

Equivalently, for every four distinct indices `i,j,k,l`,

` s_ik s_jl = s_il s_jk. `                                      (1.1)

By relabeling the same four indices, all three perfect-matching products agree:

` s_ij s_kl = s_ik s_jl = s_il s_jk. `                          (1.2)

## Theorem 1 (`QFORM-EXACT-CUTRANK1-CLASSIFICATION-v1`)

Under (1.1), exactly one of the following descriptions holds for the off-diagonal part.

1. The support graph has matching number at most one. Its unique nontrivial connected component is a **star** or a **triangle**.
2. The support graph contains two disjoint edges. Then there is a set `C`, `|C|>=4`, such that all nonzero off-diagonal entries are exactly the edges of the clique on `C`, all vertices outside `C` are isolated, and there exist nonzero scalars `sigma` and `(u_i)_{i in C}` with

   `s_ij = sigma u_i u_j`,  `i!=j`, `i,j in C`.                (1.3)

Conversely, every star, triangle, or clique factorization (1.3), with arbitrary diagonal entries added, has every disjoint physical cross block of rank at most one.

### Proof

If the support graph has matching number at most one, there cannot be two edge-containing components. A connected graph with matching number one is a star unless it is a triangle: a cycle of length at least four contains two disjoint edges; a tree with matching number one is a star; and a triangle cannot have an extra incident edge because that edge is disjoint from the opposite triangle edge.

Now suppose there are disjoint nonzero edges `ab` and `cd`. Their product is nonzero. By (1.2), the other two perfect-matching products on `{a,b,c,d}` are also nonzero, so **all six edges** on these four vertices are nonzero; they form a `K_4`.

Let `C` be a maximal clique containing this `K_4`. If a vertex `v` outside `C` touches one vertex `a in C`, choose an edge `bc` in `C` disjoint from `a`. The nonzero disjoint edges `va` and `bc`, together with (1.2), force all six edges on `{v,a,b,c}` to be nonzero. Repeating with an edge of `C` avoiding one prescribed vertex shows that `v` touches every vertex of `C`, contradicting maximality. Hence vertices outside `C` do not touch `C`. Two outside vertices also cannot be adjacent, because their edge together with any edge of the `K_4` would force edges back into `C`. Thus all outside vertices are isolated.

It remains to factor the clique weights. Relabel three vertices `1,2,3` and define

`sigma = s_12 s_13 / s_23`, `u_1=1`, `u_j=s_1j/sigma` for `j>=2`.

The formula is exact on edges from vertex 1 and on edge `23`. For any `j>=4`, (1.2) on `{1,2,3,j}` gives

`s_13 s_2j = s_1j s_23`,

hence `s_2j=sigma u_2u_j`. For distinct `i,j>=2`, (1.2) on `{1,2,i,j}` gives

`s_12 s_ij = s_1i s_2j`,

and substituting the preceding identity yields `s_ij=sigma u_i u_j`. This proves (1.3).

The converse is immediate: a clique factorization restricts on any cross cut to an outer product; a star has nonzeros in at most one row or one column of every disjoint cut; and a triangle cannot support a nonzero `2x2` cross minor because four distinct active vertices do not exist. ∎

### Necessary exception to naive gluing

The exact theorem shows that the tempting statement

> “all physical cuts have rank at most one, therefore the whole off-diagonal matrix is rank one”

is false. A four-leaf star has every disjoint cross block of rank at most one, while its symmetric off-diagonal adjacency matrix has rank two. Any robust gluing theorem must therefore retain a star/triangle exceptional branch rather than forcing a single global factor.

---

# 2. Quantitative anchor from the current approximate tetrads

Fleet03/B20 r16 proves on its unpaid Schur survivor that every four distinct residual coordinates satisfy

`|s_ik s_jl - s_il s_jk| < (1/64) sqrt(s_ik^2+s_il^2+s_jk^2+s_jl^2)`.       (2.1)

The following deterministic lemma is the first robust gluing step.

## Theorem 2 (`QFORM-NEARRANK1-HIGHEDGE-ANCHOR-v1`)

Assume (2.1), and put

`M=max_{i!=j}|s_ij|`.

Suppose `M>=1`. Form the high-edge graph

`H = { {i,j}: |s_ij| >= M/2 }`.

Then either

1. `H` has matching number at most one, hence its unique nontrivial component is a star or a triangle; or
2. `H` contains two disjoint edges, and their four endpoints form a complete graph whose **every** edge has magnitude at least

   `M/4 - 1/32 >= 7/32`.                                      (2.2)

Moreover, on those four vertices the six off-diagonal coefficients admit a rank-one clique model `sigma u_i u_j` for which four selected edges are exact and the remaining two have absolute error at most

`M/(8M-1) <= 1/7`.                                             (2.3)

### Proof

If `H` has no two disjoint edges, the graph-theoretic statement follows exactly as in Theorem 1.

Otherwise relabel two disjoint high edges as `13` and `24`. Then

`|s_13 s_24| >= M^2/4`.

Every right side in (2.1) is at most `M/32`, because the square root contains four terms, each at most `M^2`. Applying (2.1) to the relevant relabelings of the four vertices gives

`|s_13 s_24 - s_14 s_23| <= M/32`,
`|s_13 s_24 - s_12 s_34| <= M/32`.

Therefore both other perfect-matching products have magnitude at least

`M^2/4 - M/32 = M(M/4-1/32)`.

Since every individual factor is at most `M`, each of the four crossed edges has magnitude at least `M/4-1/32`. The two original high edges are at least `M/2`, proving (2.2).

For the approximate factorization, define as in Theorem 1

`sigma=s_12 s_13/s_23`, `u_1=1`, `u_j=s_1j/sigma`.

The model is exact on `12,13,14,23`. The two remaining errors satisfy

`|s_24-s_14 s_23/s_13| <= (M/32)/|s_13|`,
`|s_34-s_14 s_23/s_12| <= (M/32)/|s_12|`.

By (2.2), the denominators are at least `M/4-1/32=(8M-1)/32`, so each error is at most `M/(8M-1)<=1/7`. ∎

### Meaning for the B20 survivor

This is a genuine strengthening of “every cut is close to rank one.” At absolute off-diagonal scale `M>=1`, the unresolved geometry cannot be an arbitrary diffuse graph. At the `M/2` level it is either star/triangle-like, or it already contains a constant-scale four-coordinate clique anchor and a quantitative local rank-one factorization. The remaining hard step is to propagate such anchors through lower edges without dimension loss, while routing the star exception into the existing one-strong-cross analytic mechanisms.

---

# 3. Partner theorem converted into a diagonal-or-strong-cross routing lemma

Now return to the **full target matrix** `A`, with `s_3(A)>=1`, and suppose an original-coordinate pair gives an invertible indefinite physical block `E`. Partition

`A = [[E,B],[B^T,C]]`,

and let

`S = C - B^T E^{-1} B`                                      (3.1)

be its exact Schur complement. Put

`D=|det E|`, `kappa=sigma_min(E)`.

## Theorem 3 (`QFORM-PAIRLOG-DIAGONAL-OR-CROSS-v1`)

For every `0<eta<1`, one of the following holds.

### (A) Schur-center payment

There is a residual physical coordinate `k` with `|S_kk|>=eta`, and then the newest fleet02/B09 r9 theorem gives directly

`||p_{X^TAX}||_infinity <= 8 sqrt(2)/(sqrt(kappa eta)) + 2/sqrt(D)`.          (3.2)

Hence every interval `I` satisfies the same coefficient times `|I|`.

### (B) Strong physical bilinear cut

Every residual diagonal obeys `|S_kk|<eta`, and there exists a physical cut `L | L^c` of the residual coordinates with

`||S[L,L^c]||_op >= (1-eta)/2`.                             (3.3)

In particular, with `eta=1/4`, either the density is bounded by

`8 sqrt(2)/sqrt(kappa/4) + 2/sqrt(D)`,                       (3.4)

or some residual physical cross block has first singular value at least `3/8`.

### Proof

First, `||S||_op>=s_3(A)>=1`. Indeed

`R = [[E,B],[B^T,B^T E^{-1} B]]`

has rank at most two, while

`A-R = diag(0,S)`.

By the operator-norm Eckart-Young characterization of `s_3(A)`, every rank-two approximation has error at least `s_3(A)`, so `||S||_op>=1`.

If some `|S_kk|>=eta`, let `G` be the physical `3x3` principal block consisting of the endpoint pair and coordinate `k`. The block determinant identity gives

`|det G| = |det E| |S_kk| = D |S_kk|`.

Fleet02/B09 r9 (`QFORM-PAIRLOG-SCHUR-CENTER-v1`) applies with `Delta=D|S_kk|` and yields

`8 sqrt(2) sqrt(D/(kappa Delta)) + 2/sqrt(D)`
`= 8 sqrt(2)/(sqrt(kappa |S_kk|)) + 2/sqrt(D)`,

which is bounded by (3.2). This is an actual application of the designated partner result, with all outside coefficients and couplings retained in its stated scope.

Otherwise all residual diagonals have magnitude below `eta`. Let `T=S-diag(S)`. Then

`||T||_op >= ||S||_op-||diag(S)||_op >= 1-eta`.              (3.5)

We use an elementary cut lemma for every hollow symmetric matrix `T`: there exists a coordinate cut `L|L^c` such that

`||T[L,L^c]||_op >= ||T||_op/2`.                             (3.6)

To prove it, choose a unit vector `x` with `|x^T T x|=||T||_op`. Put each coordinate independently into `L` with probability one half and set

`Z=x_L^T T[L,L^c] x_{L^c}`.

Because `T` is hollow, `E Z=(1/4)x^T T x`; hence some cut has `|Z|>=||T||_op/4`. But `||x_L|| ||x_{L^c}||<=1/2`, so `|Z|<= (1/2)||T[L,L^c]||_op`, proving (3.6). Since removing the diagonal does not change a cross block, (3.3) follows from (3.5). ∎

## Quantitative overlap with the current near-rank-one survivor

If a branch already supplies an indefinite endpoint pair with, for example,

`kappa>=3/32`, `D>=33/1024`,

then at `eta=1/4` the partner-paid branch gives

`||p_Q||_infinity < 85.05`.

If that payment does not fire, Theorem 3 forces a residual physical cross block with `s_1>=3/8`. On a branch where fleet03/B20's cutwise conclusion also gives `s_2<1/64`, this cross block has

`s_2/s_1 < 1/24`.

Thus after an actually useful indefinite physical pair is found, the remaining unpaid geometry is not amorphous: it is forced into a very strong one-direction bilinear cut, exactly the regime where the star/near-rank-one gluing classification matters.

The caveat is important: the B20 near-rank-one statement is currently for a scalar-pivot Schur residual, whereas Theorem 3 is stated for a full matrix after removing an indefinite pair. One must verify the spectral resource at the same level before chaining them; the displayed overlap is a routing template, not an assertion that every B20 survivor already contains such a pair.

---

# 4. Target-valid partner stress test on the clique-factor branch

The exact classification has a genuine clique-factor branch, not only stars. The following four-coordinate target instance lies in that geometry:

`G = [[ 2, 1, 1, 1],
      [ 1,-2, 1, 1],
      [ 1, 1, 2, 1],
      [ 1, 1, 1, 0]].`

Its off-diagonal coefficients are exactly a rank-one clique (`u=(1,1,1,1)`, `sigma=1`). Its characteristic polynomial is

`(lambda-1)(lambda^3-lambda^2-11lambda-5)`.

The cubic has one root in `(-3,-2)`, one in `(-1,0)`, and one in `(4,5)`, so together with the eigenvalue `1`, the matrix has at least three eigenvalues of modulus at least one. It is therefore an honest target instance.

Use coordinates 1 and 2 as the endpoint pair and coordinate 3 as the Schur-center coordinate. Then

`E=[[2,1],[1,-2]]`, `D=5`, `kappa=sqrt(5)`, and `|det G[{1,2,3}]|=8`.

Fleet02/B09 r9 therefore gives, after conditioning coordinate 4 and retaining its arbitrary induced affine terms,

`||p_{X^T G X}||_infinity`
`<= 8 sqrt(2) sqrt(5/(8 sqrt(5))) + 2/sqrt(5)`
`= 4*5^(1/4) + 2/sqrt(5)`
`< 6.876`.                                                     (4.1)

This is a direct `O(|I|)` target-level estimate for every product input law with one-dimensional density caps one. It proves essential boundedness for this stress instance; continuity is not asserted by the partner endpoint.

---

# 5. What changed and what remains unpaid

The run changes the structural picture in three ways.

* The exact all-cut-rank-one limit is now **classified**, and a global rank-one conclusion is proved false unless star/triangle exceptions are retained.
* The current B20 approximate tetrads now yield a concrete high-edge dichotomy: either the `M/2` graph is star/triangle-like, or there is a constant-scale `K_4` anchor with a local rank-one approximation.
* The newest fleet02/B09 pair-log theorem is converted into an exact **Schur diagonal versus strong physical cross cut** routing lemma. It pays every nontrivial Schur-center diagonal and forces a `3/8` cross direction when all such diagonals are small.

The first unpaid implication is therefore

`QFORM-ROBUST-STAR-OR-CLIQUE-GLUING-v1`:

> Starting from the current cutwise `s_2<1/64` / low-ridge survivor, propagate the local `K_4` rank-one anchors through the physical coordinates with dimension-independent error, or prove that the high-edge graph is quantitatively star/triangle-like; then pay the resulting star or diagonal-plus-rank-one model while preserving the original-coordinate product law and the outer scalar-pivot dependence.

The exact theorem identifies the only limiting geometries that a correct robust statement should converge to. A proof that simply glues every near-rank-one cut to one global rank-one matrix is structurally false because of the star example.

## Status

* Full QFORM theorem: **OPEN**.
* Counterexample to the full QFORM theorem: **none produced**.
* New theorems above: deterministic/supporting and proved at their stated scopes.
* New target-level density payment: equation (4.1), via the designated partner theorem.
* Continuity: **not established** by the new partner-paid endpoints; only essential boundedness / linear interval anti-concentration is claimed there.
