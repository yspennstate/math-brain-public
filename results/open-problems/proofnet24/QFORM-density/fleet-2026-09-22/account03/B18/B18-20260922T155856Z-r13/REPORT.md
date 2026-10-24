# account03/B18 — one-sided cross aggregation from sharp product marginals

**Run:** `B18-20260922T155856Z-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and corrections used

The owner target is the full universal statement: for every dimension, every independent real coordinate family with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a dimension- and law-independent `L^infinity` bound for the density of `X^T A X`, or produce a valid counterexample. Continuity is tracked separately.

This report uses no Gaussianity, log-concavity, moments, compact support, connected support, or independence after an orthogonal rotation. It also preserves the current negative corrections: a generic cross minor by itself does not control uncontrolled quadratic terms on both sides; one uniformly good physical triple or one rank-two Schur minor cannot be extracted universally from the spectral hypothesis; pointwise law-uniform quadratic oscillatory decay is false.

The mechanism below is deliberately different: aggregate a whole original-coordinate cross bank first, while allowing an arbitrary same-side measurable term on ONE side.

## 2. Primary literature audit

### 2.1 Livshyts--Paouris--Pivovarov

Primary source: Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949.

Their Theorem 1.1 states: if `f(x)=prod_i f_i(x_i)`, each `f_i` is a probability density on `R` with `||f_i||_infinity<=1`, and `E` is a `k`-dimensional subspace, then the density of the orthogonal projection onto `E` is at most `2^(k/2)` (with a sometimes sharper first term). In particular, every unit linear form in independent cap-one coordinates has density at most `sqrt(2)`, and every two-dimensional orthogonal projection has density at most `2`. These are exactly the hypotheses available here. No moment or log-concavity condition appears.

The stated theorem assumes `k<n`. When the projection dimension equals the entire ambient dimension, the orthogonal image has the same joint density supremum as the product source, at most one, which is even stronger than the `2^(k/2)` estimate used below.

### 2.2 Banks quadratic-form density theorem: exact scope retained

Primary source: Jesse M. Banks, *Random Matrices and Provable Algorithms for Approximate Diagonalization*, UC Berkeley PhD thesis (2022), Theorem 4.15 and Corollary 4.18.

Banks assumes two arrays/vectors with mutually independent entries having scalar densities bounded by `K`, and controls a genuinely bilinear-plus-linear expression `X^T Z Y + X^T U + V^T Y + W`. In the scalar-output case the corollary replaces a single singular value by a geometric mean of top singular values. The later Gaussian improvement is separate.

That theorem does **not** authorize inserting an arbitrary same-side quadratic term into the same bilinear expression. The theorem below therefore does not silently extend Banks. Instead it uses the sharp product-marginal theorem after conditioning on the side carrying the arbitrary term.

## 3. Reciprocal-radius lemma under only a density cap

Let `Z` be an `R^j`-valued random vector with density bounded by `M`, where `j>=2`, and let `v_j` be the volume of the Euclidean unit ball in `R^j`. Then

`E[1/||Z||] <= [j/(j-1)] (M v_j)^(1/j).`

Indeed, by layer cake,

`E[1/||Z||] = integral_0^infinity P(||Z|| < 1/s) ds`

and

`P(||Z||<1/s) <= min(1, M v_j s^(-j)).`

With `s_0=(M v_j)^(1/j)`, integration gives

`s_0 + M v_j integral_(s_0)^infinity s^(-j) ds = [j/(j-1)]s_0.`

No radiality or regularity of the law is used.

## 4. Main theorem — one-sided cross aggregation

Let

- `U=(U_1,...,U_m)` and `V=(V_1,...,V_k)` be mutually independent families;
- every coordinate have a probability density bounded by one;
- `B` be an `m x k` real matrix of rank at least two;
- `G:R^m -> R` be any measurable function finite almost surely;
- `beta in R^k`.

Define

`T = G(U) + 2 U^T B V + beta^T V.`

Write the singular values of `B` as `sigma_1>=sigma_2>=...`, and let `v_j` be the volume of the unit ball in `R^j`.

### Theorem 4.1 — `QFORM-ONE-SIDED-CROSS-AGGREGATE-v1`

For every `2<=j<=rank(B)`, `T` has a **continuous** density and

`||p_T||_infinity <= [j/(j-1)] [ v_j / prod_{ell=1}^j sigma_ell(B) ]^(1/j).`

Hence

`||p_T||_infinity <= min_(2<=j<=rank B) [j/(j-1)] [v_j / prod_(ell<=j) sigma_ell(B)]^(1/j).`

In particular, for `j=2`,

`||p_T||_infinity <= 2 sqrt(pi) / sqrt(sigma_1(B) sigma_2(B)).`

This result permits an arbitrary same-side term `G(U)`; only the `V`-side self-interaction is absent.

### Proof

Fix `U=u` and set

`c(u)=2B^T u+beta`.

Conditionally on `U=u`, `T` is a translation of the linear form `c(u)^T V`. For `c(u) != 0`, apply the one-dimensional Livshyts--Paouris--Pivovarov marginal bound to the unit direction `c(u)/||c(u)||`. Thus the conditional density satisfies

`||p_(T|U=u)||_infinity <= sqrt(2)/||c(u)||`.  (4.1)

Since `rank(B)>=2`, the affine equation `c(u)=0` has Lebesgue-null solution set (if nonempty), so it has `U`-probability zero.

Now choose the first `j` left and right singular vectors `e_ell` and `v_ell` of `B`, and put

`W=(e_1^T U,...,e_j^T U).`

The coordinates `e_ell` form an orthonormal system. By the `j`-dimensional product-marginal theorem, `W` has density at most `2^(j/2)` when `j<m`; when `j=m`, orthogonal change of variables preserves the full joint density supremum, at most one, so the same weaker cap `2^(j/2)` still holds.

Let `beta_ell=<beta,v_ell>` and define

`Z_ell = 2 sigma_ell W_ell + beta_ell`, `1<=ell<=j`.

Then

`||c(U)||^2 >= sum_(ell=1)^j Z_ell^2 = ||Z||^2`,

and the density of `Z` is bounded by

`M <= 2^(j/2) / [2^j prod_(ell=1)^j sigma_ell] = 2^(-j/2) / prod_(ell=1)^j sigma_ell.`

The reciprocal-radius lemma gives

`E[1/||c(U)||] <= E[1/||Z||]`

`<= [j/(j-1)] 2^(-1/2) [v_j/prod_(ell=1)^j sigma_ell]^(1/j).`

Averaging (4.1) therefore yields

`||p_T||_infinity <= [j/(j-1)] [v_j/prod_(ell=1)^j sigma_ell]^(1/j).`

It remains to justify continuity rather than only essential boundedness. For almost every `u`, the coefficient vector `c(u)` has at least two nonzero coordinates. Indeed, the exceptional set is the finite union over coordinate axes `L_r` of affine preimages `(B^T)^(-1)(L_r-beta/2)`; since the image of `B^T` has dimension at least two, each such preimage has Lebesgue codimension at least one. On the complement, `c(u)^T V` contains a convolution of two scaled `L^1 cap L^infinity` densities, hence has a continuous density (translation continuity in `L^1` gives continuity of the convolution). The pointwise conditional densities are dominated by the integrable majorant `sqrt(2)/||c(U)||`. Dominated convergence in `u` now shows the averaged density `p_T` is continuous. QED.

## 5. Physical quadratic-form corollary

Partition original coordinates into disjoint sets `I,J,O`. Suppose the selected physical principal block satisfies

`A_JJ=0`,

while `A_II` is completely arbitrary. Put `B=A_IJ` and assume `rank(B)>=2`. All couplings of `I union J` to `O`, and the entire `O x O` block, are arbitrary.

Conditioning on `X_O=w` gives

`Q_w = G_w(X_I) + 2 X_I^T B X_J + beta_w^T X_J + c_w`,

with arbitrary measurable (indeed quadratic) `G_w`. Therefore Theorem 4.1 applies uniformly in `w`.

### Corollary 5.1 — `QFORM-ONE-SIDED-PHYSICAL-BLOCK-v1`

The full quadratic form has a **continuous** density satisfying

`||p_Q||_infinity <= min_(2<=j<=rank B) [j/(j-1)] [v_j/prod_(ell<=j) sigma_ell(B)]^(1/j).`

The continuity survives averaging over `X_O` because the conditional densities are continuous and uniformly dominated by the same finite constant.

For `sigma_2(B)>=1`, the simple `j=2` bound is

`||p_Q||_infinity <= 2 sqrt(pi) = 3.544907701811... .`

This strictly weakens the earlier B18 exact-bipartite requirement `A_II=A_JJ=0`: now only one side must have zero self-block.

It also respects `QFORM-CROSSMINOR-ALONE-FALSE`: that correction allows uncontrolled same-side quadratic terms on **both** sides, which this theorem does not.

## 6. Concrete target-valid rotated/indefinite example

Let `I={1,2}`, `J={3,4}`, `B=I_2`, and

`A = [[3,0,1,0],
     [0,0,0,1],
     [1,0,0,0],
     [0,1,0,0]].`

After permuting coordinates into the two coupled pairs, its eigenvalues are

`(3+sqrt(13))/2`, `(3-sqrt(13))/2`, `1`, `-1`.

Thus at least three eigenvalues have absolute value at least one. The `I`-side block is nonzero, so the earlier pure bipartite theorem does not apply. Corollary 5.1 nevertheless gives, for **every** admissible independent cap-one source,

`||p_(X^TAX)||_infinity <= 2 sqrt(pi)`

and the density is continuous.

This is a supporting target subclass, not the full theorem.

## 7. Substantive use of account04/B18 partner theorem

Partner source: account04/B18 scientific commit

`441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Its proved `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` states: if `R` has density at most `M` and, conditionally on `R=r`, a variable `V_r` has density at most one, with no independence assumed, then for `a !=0`,

`R+aV_R^2`

has density at most `2 sqrt(M/|a|)`.

Now choose an original-coordinate scalar pivot `z` with `a=A_zz !=0`, write

`A=[[a,b^T],[b,C]]`, `S=C-bb^T/a`,

and split residual coordinates into disjoint `I,J,O`. Assume only

`S_JJ=0`, `B=S_IJ`, `rank(B)>=2`;

`S_II` and all couplings involving `O` may be arbitrary.

After conditioning on `O`, the Schur residual is of the form paid by Theorem 4.1. Thus, for every `2<=j<=rank(B)`, it has density at most

`M_j = [j/(j-1)] [v_j/prod_(ell<=j) sigma_ell(B)]^(1/j).`

Completing the square in the untouched physical pivot gives

`Q = R + a (X_z + a^(-1)b^T y)^2`.

Conditionally on `R=r`, the shifted pivot is a mixture of translations of the original density of `X_z`, because `X_z` was independent of all residual coordinates before conditioning. Hence its conditional density remains at most one, exactly matching the partner lemma.

### Theorem 7.1 — `QFORM-ONE-SIDED-SCHUR-SMOOTHING-v1`

Under the preceding hypotheses,

`||p_Q||_infinity <= 2 |a|^(-1/2) min_(2<=j<=rank B) sqrt(M_j).`

In particular,

`||p_Q||_infinity <= [2 sqrt(2) pi^(1/4)] / [ |a|^(1/2) (sigma_1(B)sigma_2(B))^(1/4) ].`

If `|a|>=1` and `sigma_2(B)>=1`, this is at most

`2 sqrt(2) pi^(1/4) = 3.765585055106... .`

The wrapper establishes an essentially bounded density. I do **not** claim continuity from the dependent-square lemma alone.

This improves the earlier B18 Schur wrapper in two ways: it no longer requires `S_II=0`, and its `j=2` constant improves from `2 sqrt(2)(e pi)^(1/4)` to `2 sqrt(2) pi^(1/4)`.

## 8. Explicit partner-applied inequality on a fully coupled target matrix

Take the four-coordinate Schur residual

`S = [[4,0,2,0],
     [0,0,0,2],
     [2,0,0,0],
     [0,2,0,0]].`

With `I={1,2}`, `J={3,4}`, we have `S_JJ=0`, arbitrary nonzero `S_II=diag(4,0)`, and `B=2I_2`, so `sigma_1=sigma_2=2`.

Let `a=2`, `b=(1/20)(1,1,1,1)^T`, and define the full five-dimensional matrix

`A=[[2,b^T],[b,S+bb^T/2]].`

Its Schur complement at the first physical coordinate is exactly `S`. The block-diagonal comparison `A_0=diag(2,S)` has spectrum

`{2, 2+2sqrt(2), 2-2sqrt(2), 2, -2}`.

The perturbation `A-A_0` has operator norm at most

`||b|| + ||b||^2/2 = 1/10 + 1/200 = 21/200 < 0.11`.

Therefore Weyl's inequality leaves at least four eigenvalues of `A` with absolute value greater than `2-21/200=379/200>1`; the owner's three-large-eigenvalue hypothesis is rigorously satisfied.

Theorem 7.1 and the partner smoothing lemma give the actual bound

`||p_(X^TAX)||_infinity <= sqrt(2) pi^(1/4) = 1.882792527553...`

for every independent cap-one input law. This example is fully coupled through the pivot (`b !=0`) and the residual is not pure bipartite because `S_II !=0`.

## 9. What this closes and what remains unpaid

This run closes the analytic density step for a substantially larger product-preserving branch:

- a whole physical cross bank may be high-dimensional and diffuse;
- one side may carry an arbitrary quadratic (indeed arbitrary measurable) self-term;
- the payment depends on the geometric product of cross singular values, with no reciprocal fixed physical minor;
- after one physical Schur pivot, the same one-sided branch combines with the completed account04/B18 dependent-square theorem.

This directly addresses the current correction that one good physical triple need not exist. However it does **not** solve the spectral-to-coordinate structural bridge. A general admissible `A` need not admit, before or after one pivot, a substantial cross bank with an exactly zero self-block on one side. The known corrections explicitly forbid promoting a generic cross block with both self-blocks uncontrolled.

The next useful implication is therefore:

> starting only from three eigenvalues `|lambda|>=1`, prove a product-preserving decomposition/conditioning step that either enters the current ridge/diffuse branch, or produces a one-sided low-self-block cross bank to which Theorem 4.1 can be stably extended. The next mathematical attack should quantify a perturbative replacement for the exact condition `A_JJ=0`, rather than returning to fixed-minor extraction.

Full universal QFORM remains **OPEN / NOT PROVED**. No novelty claim is made for the supporting theorem relative to the entire literature.
