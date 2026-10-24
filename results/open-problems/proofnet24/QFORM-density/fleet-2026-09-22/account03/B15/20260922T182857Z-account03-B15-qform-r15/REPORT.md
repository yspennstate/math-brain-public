# account03/B15 — coordinatewise L1→output-L∞ stability and rough-input C0 regularity in rank ≥ 5

**Run:** `20260922T182857Z-account03-B15-qform-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh control observed:** `yspennstate/math-research-brain@1dabd8516681f9f2c43318ab858b337d8d6f8cae`, OWNER CONTROL revision `2026-09-22.11`  
**Assignment:** Absolute continuity and regularity  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL-REGULARITY-LEMMA / FULL-TARGET-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval was authenticated, but no authenticated native mathematical-receiver context was consumed.

## 1. Exact target and corrections used

The owner target is unchanged: for independent real coordinates with densities `0<=f_i<=1` and a real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove a dimension- and matrix-independent finite bound on the density of `Q=X^TAX`, or give a valid counterexample. Continuity of the output density is a separate stronger request.

This report does **not** use the false arbitrary-joint rank-three coarea bound or the false conditional positive-moment projection bound. Those claims are explicitly corrected in the live `CURRENT_RESEARCH.md`. No independence after spectral rotation is assumed.

The completed assigned-partner result actually applied is account04/B15:

- repository/commit: `yspennstate/math-open-problems@07672b7beb8f867c7a7b973aa3157a42ae506460`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T152333Z-b15-qform-continuous-envelope-r3/REPORT.md`.

It proves that cap-one compactly supported smooth product inputs have output densities in `C_0(R)`, and more strongly that the optimal universal height constant on the full target equals the optimal constant on this smooth/continuous-output subclass.

The second completed input is the instancewise principal-block theorem:

- repository/commit: `yspennstate/math-open-problems@47dc925729bbf269333cc6e1256178a538d2f553`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account01/B15/20260922T120320Z-account01-B15-qform/REPORT.md`.

For every invertible physical principal block `B` of order 3 or 4 and every affine perturbation, conditioning in the original independent coordinates gives a density bound

`C_3/sigma_min(B)` for order 3, `C_3=2*pi+3*sqrt(3)`,

and

`C_4/sigma_min(B)` for order 4, `C_4=4*pi+8`.

It also proves that every symmetric matrix of rank at least 3 has an invertible physical principal block of order 3 or 4.

## 2. A disjoint-block stability lemma

Let `A` be fixed. For a coordinate `j`, assume there is a physical index set

`I_j subset {1,...,n}\{j}`, `|I_j| in {3,4}`,

such that `B_j=A[I_j,I_j]` is invertible. Put

`H_j = C_|I_j| / sigma_min(B_j)`.

### Lemma 2.1 — `QFORM-DISJOINT-BLOCK-L1-LINF-v1`

Fix all marginals except the `j`th. Let `f_j,g_j` be two probability densities with `0<=f_j,g_j<=1`; let every other coordinate density also be bounded by one. Let `p_f,p_g` denote the output densities of `X^TAX` for the two product inputs. Then

`||p_f-p_g||_infinity <= H_j ||f_j-g_j||_1`.    (2.1)

#### Proof

Condition on every coordinate outside `I_j`. In particular `X_j` is among the conditioned coordinates because `j notin I_j`. If the outside value is `w`, the remaining polynomial in the original coordinates `X_{I_j}` is

`X_{I_j}^T B_j X_{I_j} + 2 b(w)^T X_{I_j} + c(w)`.

The coordinates in `I_j` remain independent with unchanged cap-one densities. The completed 3/4-variable affine theorem therefore gives a conditional density kernel `k_w(t)` with

`0<=k_w(t)<=H_j`

for almost every `t`, uniformly in every outside value for which the regular conditional law is defined.

Write the other outside coordinates as `z`, and expose `x_j` separately. The two output densities may be represented as

`p_f(t)=int k_(x_j,z)(t) f_j(x_j) dx_j dtheta(z)`,

`p_g(t)=int k_(x_j,z)(t) g_j(x_j) dx_j dtheta(z)`,

where `theta` is the common product law of the remaining outside coordinates. Hence

`|p_f(t)-p_g(t)|`
`<= int H_j |f_j(x_j)-g_j(x_j)| dx_j dtheta(z)`
`= H_j ||f_j-g_j||_1`.

Taking the essential supremum gives (2.1). No continuity of any marginal is used. `QED`.

### Multi-coordinate form

Suppose every coordinate `j` admits such a disjoint block `I_j`. For two cap-one product inputs `f=(f_1,...,f_n)` and `g=(g_1,...,g_n)`, telescope one coordinate at a time. At every intermediate stage all marginals remain cap-one, so Lemma 2.1 applies unchanged. Therefore

`boxed( ||p_f-p_g||_infinity <= sum_j H_j ||f_j-g_j||_1 ).`    (2.2)

This is a genuine product-law stability estimate: the output density map is Lipschitz from coordinatewise `L1` into `L-infinity`, with constants depending only on fixed physical principal blocks of `A`.

## 3. Rank at least five automatically has the disjoint-block property

### Lemma 3.1

If `rank(A)>=5`, then for every coordinate `j`, the principal deletion `A[j^c,j^c]` has rank at least 3.

#### Proof

Deleting one row can reduce matrix rank by at most one, and deleting the corresponding column can reduce it by at most one more. Hence

`rank(A[j^c,j^c]) >= rank(A)-2 >=3`. `QED`.

Apply the completed principal-block lemma to `A[j^c,j^c]`. It contains an invertible principal block `B_j` of order 3 or 4. Thus every coordinate has a disjoint smoothing block.

## 4. New rough-input continuity theorem

### Theorem 4.1 — `QFORM-RANK5-C0-v1`

Let `A` be any real symmetric matrix with `rank(A)>=5`. Let `X_1,...,X_n` be independent real random variables with arbitrary measurable probability densities satisfying `0<=f_i<=1`. Then

`boxed( X^TAX has a density p_Q in C_0(R). )`

In particular the density is bounded and uniformly continuous for every fixed such instance. No moment, support, log-concavity, sign, or diagonal-coordinate assumption is required.

#### Proof

For every coordinate choose the disjoint invertible block `I_j` obtained in Section 3 and its finite constant `H_j`.

Use the completed cap-preserving approximation underlying the assigned account04/B15 theorem: for each `i`, choose probability densities `g_i^(m) in C_c^infinity(R)` with

`0<=g_i^(m)<=1`, `||g_i^(m)-f_i||_1 ->0`.

Let `p_m` be the density of the quadratic output for the smooth product input `g^(m)`. The account04/B15 theorem gives

`p_m in C_0(R)`.

By (2.2),

`||p_m-p_Q||_infinity <= sum_j H_j ||g_j^(m)-f_j||_1 ->0`.    (4.1)

More explicitly, applying (2.2) to `m` and `ell` also shows that `(p_m)` is uniformly Cauchy in the ordinary sup norm: the difference `p_m-p_ell` is continuous, so its essential supremum equals its pointwise supremum. Since `C_0(R)` is complete in the sup norm, there is a function `p_* in C_0(R)` with `p_m ->p_*` uniformly.

Equation (4.1) identifies `p_*` with the rough output density almost everywhere. Hence `p_*` is a continuous `C_0` representative of `p_Q`. `QED`.

### Quantitative approximation statement

The proof gives the explicit error estimate

`boxed( ||p_Q-p_m||_infinity <= sum_j [C_|I_j|/sigma_min(A[I_j,I_j])] ||f_j-g_j^(m)||_1 ).`    (4.2)

Thus continuity is not obtained by the invalid principle “TV convergence + common height cap preserves continuity”. It follows from the new **target-specific L1-to-L∞ scale-coherence estimate** (2.2), exactly the missing type of ingredient identified by account04/B15.

## 5. Stronger structural version and the remaining continuity obstruction

The rank-five assumption is only a convenient automatic sufficient condition. The same proof works for any fixed symmetric `A` satisfying

`rank(A[j^c,j^c])>=3 for every coordinate j`.    (5.1)

Indeed (5.1) is exactly what provides a disjoint physical 3/4-block for every marginal replacement.

For a general rank-three or rank-four matrix, (5.1) can fail. The obstruction is finite-dimensional and concrete. Choose one invertible physical principal block `I` of order 3 or 4, which exists for every rank-at-least-three symmetric matrix. Every coordinate `j notin I` automatically has a disjoint invertible block, namely `I` itself. Therefore **all marginals outside one 3/4-coordinate core can already be smoothed in output `L-infinity` without changing the rough core**.

Consequently the unresolved rough-input continuity problem reduces to at most four distinguished physical marginals. The remaining task is to establish a comparable stability modulus when changing one of those core marginals, or to construct a genuine rank-three/rank-four product-law discontinuity. This is strictly smaller than the original arbitrary-dimensional regularity problem.

## 6. Relation to the universal-height conjecture

This report does not prove the universal constant. The constants `H_j` may be arbitrarily large along matrices satisfying the owner's three-large-eigenvalue hypothesis. The known flat/diffuse examples show that one cannot replace the aggregate geometry by a single uniformly conditioned principal block.

The main bounded-density conjecture therefore remains OPEN. The new theorem is a regularity result only:

- absolute continuity: already known for every nonzero quadratic polynomial of an absolutely continuous vector;
- instancewise finite `L-infinity`: already known for rank at least 3 with a matrix-dependent block constant;
- rough-input `C_0` continuity: now proved for rank at least 5, and more generally under (5.1);
- arbitrary rank-3/rank-4 rough-input continuity: still open;
- universal dimension/matrix-independent height: still open.

## 7. Sanity checks and correction compatibility

1. The argument conditions only on **original independent coordinates**. No spectral-coordinate independence is used.
2. No law-uniform pointwise oscillatory decay is used.
3. No arbitrary-joint coarea inequality is used.
4. No fiber supremum is integrated over a high-dimensional family.
5. The proof does not claim a universal bound from `sigma_min(B_j)^{-1}`; these constants are used only as fixed-instance stability constants.
6. The theorem is consistent with rank-two discontinuity examples: rank two fails the automatic disjoint rank-3 block hypothesis.

**Status:** supporting target-level regularity theorem proved; full QFORM universal-constant conjecture remains `OPEN / NOT PROVED`.
