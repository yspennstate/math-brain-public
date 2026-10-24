# account03/B09 — rank-two bilinear direct anti-concentration without decoupling loss

**Run:** `20260922T114536Z-account03-B09-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Bilinear block mechanism`  
**Classification:** `ESSENTIAL_STEP_APPLIED`; full conjecture remains **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.

## 0. Fresh-control correction to the incoming prompt

The incoming invocation still named the superseded FEI programme. Fresh `main` control instead assigns all workers exclusively to the quadratic-form density conjecture. I therefore did no FEI mathematics in this run.

The target is: for independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has a density with universal dimension-free `L^infinity` norm, or give a valid counterexample.

I consumed the live corrections: law-uniform pointwise Fresnel decay is false; naive spectral-fiber supremum integration loses dimension; diagonalizing `A` does not preserve coordinate independence.

The named partner `account04/B09` had no completed QFORM handoff at the fresh reads, so I did not wait or fabricate partner mathematics. I substantively applied two complete other-worker QFORM reports already present in the research archive:

1. `account02/B05`, run `20260922T112240Z-b05-qform-9d86c905`: exact product-preserving pair-kernel identities and the warning that scalar decoupling loses the exponent; it also source-pins the sharp marginal-density theorem of Livshyts--Paouris--Pivovarov.
2. `account02/B06`, run `b06-20260922T113045Z-d47192d10a82`: same-sign spectral-pair Pluecker determinant-mass identity and the delocalized Hadamard obstruction to selecting one uniformly curved physical pair.

The result below turns those two ingredients into a direct, dimension-free bilinear anti-concentration theorem at the **linear interval scale**. It does not square or symmetrize the desired probability.

---

## 1. Marginal-density input

I use the following proved external theorem.

**Product marginal theorem (Livshyts--Paouris--Pivovarov, arXiv:1507.07949 / Israel J. Math. 216 (2016)).** If a random vector `Z in R^d` has independent coordinates with one-dimensional densities bounded by one, then the density of its orthogonal projection onto any `k`-dimensional subspace is bounded by `2^(k/2)`.

Only `k=1,2` are used here. Thus every normalized linear form `<theta,Z>`, `||theta||_2=1`, has density at most `sqrt(2)`, and every two-dimensional orthogonal projection has density at most `2`.

### Lemma 1 — reciprocal-radius budget

If a random vector `Y in R^2` has a density bounded by `H`, then

`E[1/||Y||_2] <= 2 sqrt(pi H)`.

**Proof.** The disk bound gives

`P(||Y||_2 <= r) <= min(1, pi H r^2)`.

By layer cake,

`E[1/||Y||_2] = int_0^infinity P(||Y||_2 < 1/t) dt`.

Set `t_0=sqrt(pi H)`. On `[0,t_0]` use probability at most one; on `[t_0,infinity)` use `pi H/t^2`. Hence

`E[1/||Y||_2] <= t_0 + pi H/t_0 = 2 sqrt(pi H)`. QED.

The integrability is exactly a two-dimensional effect: in one dimension the reciprocal distance has a logarithmic divergence for a density positive at the origin.

---

## 2. Main theorem: direct rank-two bilinear smoothing

### Theorem 2 — `QFORM-RANK2-BILINEAR-DIRECT-v1`

Let

- `U=(U_1,...,U_m)` and `V=(V_1,...,V_k)` be independent random vectors;
- all coordinates within each vector be independent, with probability densities bounded by one;
- `M` be a real `m x k` matrix whose two largest singular values are `s_1 >= s_2 > 0`;
- `H:R^m -> R` be any measurable function.

Then

`Z = H(U) + 2 U^T M V`

has a density satisfying

`||p_Z||_infinity <= 2 sqrt(pi) / sqrt(s_1 s_2)`.                         (2.1)

Consequently, for every interval `I`,

`P(Z in I) <= [2 sqrt(pi)/sqrt(s_1 s_2)] |I|`.                           (2.2)

No moment, centering, support, regularity, or log-concavity assumption is used.

### Proof

Fix `U=u` and put `a=M^T u`. Except on the null set `a=0`, the conditional random variable is a translate of `2<a,V>`. By the one-dimensional product marginal theorem, the normalized linear form `<a/||a||,V>` has density at most `sqrt(2)`. Scaling by `2||a||` therefore gives

`||p_{Z|U=u}||_infinity <= 1/(sqrt(2) ||M^T u||_2)`.                      (2.3)

Let `e_1,e_2` be left singular vectors of `M` for `s_1,s_2` and set

`xi=(<U,e_1>,<U,e_2>)`.

The two-dimensional product marginal theorem says `xi` has density at most `2`. Since

`||M^T U||_2 >= sqrt(s_1^2 xi_1^2+s_2^2 xi_2^2)`,                         (2.4)

define `Y=(s_1 xi_1,s_2 xi_2)`. Its density is at most

`2/(s_1 s_2)`.

Lemma 1 now yields

`E[1/||M^T U||_2]
 <= E[1/||Y||_2]
 <= 2 sqrt(2 pi/(s_1 s_2))`.                                               (2.5)

The set `M^T U=0` has probability zero because `(xi_1,xi_2)` is absolutely continuous. Averaging the conditional densities in (2.3), using Tonelli/disintegration and (2.5), gives

`||p_Z||_infinity
 <= (1/sqrt(2)) 2 sqrt(2 pi/(s_1 s_2))
 = 2 sqrt(pi)/sqrt(s_1 s_2)`.

This proves (2.1), and integrating the density over `I` gives (2.2). QED.

### Version without the factor two

For `Z_0=H(U)+U^T M V`, the same proof gives

`||p_{Z_0}||_infinity <= 4 sqrt(pi)/sqrt(s_1 s_2)`.                        (2.6)

The factor-two normalization in (2.1) is the natural one for a symmetric quadratic form split into two coordinate blocks.

---

## 3. Immediate quadratic-form corollary

### Corollary 3 — `QFORM-FREE-LINEAR-BLOCK-v1`

Partition the original independent coordinates as `X=(U,V)` and write

`A = [[B,M],[M^T,0]]`.

If the cross block `M` has `s_2(M)>0`, then

`Q=X^TAX = U^T B U + 2 U^T M V`

has a density with

`||p_Q||_infinity <= 2 sqrt(pi)/sqrt(s_1(M)s_2(M))`.                       (3.1)

Thus this entire non-diagonal, possibly indefinite class has the desired **O(interval length)** anti-concentration, directly and without any square-root/fourth-root decoupling loss.

The same statement holds with the two blocks interchanged. More generally, any additional random term measurable with respect to `U` and variables independent of `V` may be absorbed into `H`.

This is a supporting theorem, not a solution of the full target: for a general split the `V`-block contains `V^T C V`, which shares `V` with the linear cross term and cannot be treated as independent additive noise.

---

## 4. Rank two is the sharp threshold for the pure bilinear mechanism

The rank-two hypothesis is not an artifact of the proof.

Take one-dimensional independent `U,V ~ Uniform[-1/2,1/2]`, whose densities equal one, and let `Z=2UV`. For `0<|z|<1/2`, direct change of variables gives

`p_Z(z)=log(1/(2|z|))`,                                                     (4.1)

which diverges at zero. Thus a rank-one cross block has the same logarithmic obstruction seen elsewhere in indefinite rank-two quadratic forms.

By Theorem 2, two nonzero singular directions immediately make the pure bilinear output bounded. So, for the direct conditional-linear mechanism, the exact threshold is:

`cross rank 1 -> logarithmic singularity can occur; cross rank >=2 -> bounded density`.

---

## 5. Exact bridge to the B06 Pluecker determinant-mass invariant

The B06 report proves that a same-sign spectral pair does not disappear under delocalization; its two-dimensional curvature is distributed over Pluecker weights. The bilinear theorem admits an exact cross-block expression in those weights.

Let `r_1,r_2 in R^n` be orthonormal and

`R=[r_1 r_2]`, `Lambda=diag(lambda_1,lambda_2)`,

with `lambda_1 lambda_2 !=0`. Put `P=R Lambda R^T`. For a coordinate partition `S union T=[n]`, define

`C_S=R_S^T R_S`, `C_T=R_T^T R_T=I_2-C_S`,

and let the cross block of the rank-two spectral component be

`M_{S,T}=P_{S,T}=R_S Lambda R_T^T`.

For the Pluecker weights

`w_ij = det(R_{ {i,j} })^2`, `sum_{i<j}w_ij=1`,

define

`W_S=sum_{i<j, i,j in S}w_ij`, `W_T=sum_{i<j, i,j in T}w_ij`.

### Lemma 4 — `QFORM-PLUECKER-CROSS-SINGULAR-v1`

If `sigma_1>=sigma_2` are the two nonzero singular values of `M_{S,T}` (zeros allowed by continuity), then

`sigma_1 sigma_2 = |lambda_1 lambda_2| sqrt(W_S W_T)`.                     (5.1)

**Proof.** Cauchy--Binet gives

`det C_S=W_S`, `det C_T=W_T`.

For full column rank, the product of the two nonzero squared singular values of `R_S Lambda R_T^T` is

`det(Lambda C_S Lambda) det(C_T)
 = (lambda_1 lambda_2)^2 det(C_S)det(C_T)`.

Taking square roots gives (5.1); rank-deficient cases follow directly or by continuity. QED.

Combining (5.1) with Theorem 2 shows that whenever a quadratic form exposes this spectral-pair cross block as a free linear block,

`||p_Q||_infinity
 <= 2 sqrt(pi) /
    [sqrt(|lambda_1 lambda_2|) (W_S W_T)^(1/4)]`.                          (5.2)

This makes the connection to B06 quantitative: determinant mass on **both** sides of a split is exactly the resource that produces two bilinear singular directions.

### Random-split identity

If each coordinate is independently placed in `S` or `T` with probability `1/2`, then

`E[W_S W_T]
 = (1/16) sum_{e,f: e cap f = empty} w_e w_f`,                             (5.3)

where the sum is over ordered disjoint coordinate pairs `e,f`. Indeed, a Pluecker edge `e` lies wholly in `S` and a disjoint edge `f` wholly in `T` with probability `1/16`; overlapping edges cannot do both.

Hence a positive amount of **disjoint Pluecker-pair mass** guarantees a split with a quantitatively rank-two spectral cross block. If the disjoint-pair mass vanishes exactly, the support graph of the nonzero `w_ij` is pairwise intersecting, hence is contained in a star or a triangle. That is a clean localized-versus-bipartite structural dichotomy for the same-sign spectral pair. The remaining difficulty is that other spectral components can cancel the cross block or create within-block quadratic terms.

---

## 6. Why standard scalar decoupling cannot finish the full split

Write a general split as

`q(u,v)=u^T B u + 2u^T Mv + v^T C v`.

Let `U,U'` and `V,V'` be independent copies and `I` an interval of length `ell`. Set `h(u,v)=1_{q(u,v) in I}` and `p=E h(U,V)`.

The C4/Sidorenko inequality (two Cauchy--Schwarz applications) gives

`p^4 <= E h(U,V)h(U,V')h(U',V)h(U',V')`.                                  (6.1)

On the four-event intersection, the alternating contrast is in `[-2ell,2ell]`, while the block quadratics cancel exactly:

`q(U,V)+q(U',V')-q(U,V')-q(U',V)
 = 2 (U-U')^T M (V-V')`.                                                   (6.2)

Each coordinate of `U-U'` has density

`g_i(t)=int f_i(x)f_i(x-t)dx <=1`,

and these difference coordinates remain independent; likewise for `V-V'`. Therefore Theorem 2 applies to the scalar contrast in (6.2). If `s_2(M)>0`,

`P(|2(U-U')^T M(V-V')|<=2ell)
 <= 8 sqrt(pi) ell/sqrt(s_1s_2)`.                                          (6.3)

Combining (6.1)--(6.3),

`P(q(U,V) in I)
 <= min(1,[8 sqrt(pi) ell/sqrt(s_1s_2)]^(1/4)).                            (6.4)

So scalar four-cycle decoupling throws away three of the four interval constraints and degrades the desired linear scale to `ell^(1/4)`. This is not a defect in Theorem 2; the scalar alternating contrast itself generally has only an `O(ell)` small-ball probability. A proof that merely decouples to this one scalar cannot recover `O(ell)` for `Q`.

This explicitly identifies the assignment's “square-root decoupling” danger in its stronger C4 form.

---

## 7. First unpaid implication and next mechanism

The direct bilinear step itself is now closed at the correct linear interval scale. The first missing implication for the full target is narrower:

> **`QFORM-BILINEAR-BLOCK-ABSORPTION-v1` (OPEN).** For a coordinate split `A=[[B,M],[M^T,C]]` with two quantitatively nonzero singular directions in `M`, exploit the cross-term smoothing **without** first replacing the two within-block quadratic terms by a scalar alternating difference. The argument must retain enough simultaneous interval constraints to preserve an `O(ell)` bound.

A successful proof can then be paired with the B06 determinant-mass/random-split structure. It must also handle the possibility that other spectral components cancel a same-sign pair's cross block.

A promising next attack is a genuinely vector-valued two-by-two conditioning argument: retain several of the four values `q(U_a,V_b)` simultaneously rather than collapsing them to the single contrast (6.2), and seek a joint density/small-box estimate that spends the third spectral direction. Any such estimate must be checked against the rank-one product logarithm and the rank-two opposite-sign logarithmic control.

## 8. Status

**PROVED / supporting:**
- `QFORM-RANK2-BILINEAR-DIRECT-v1`, with explicit constant `2 sqrt(pi)/sqrt(s_1s_2)` for the symmetric cross normalization;
- `QFORM-FREE-LINEAR-BLOCK-v1`, a non-diagonal quadratic subclass with direct `O(|I|)` anti-concentration;
- rank-one bilinear logarithmic obstruction;
- `QFORM-PLUECKER-CROSS-SINGULAR-v1` and the random-split identity;
- exact C4 scalar-decoupling bound (6.4), exposing the exponent loss.

**OPEN:**
- `QFORM-BILINEAR-BLOCK-ABSORPTION-v1`;
- controlling cancellation of a selected same-sign spectral pair by the remaining spectrum;
- the full quadratic-form bounded-density conjecture and its stronger continuity request.

No full-solution claim is made.