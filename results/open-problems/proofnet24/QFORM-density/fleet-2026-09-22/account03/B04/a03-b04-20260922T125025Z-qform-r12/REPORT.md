# account03/B04 — diffuse rank-two Fourier rearrangement and coupled Schur pivot

Run: `a03-b04-20260922T125025Z-qform-r12`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and corrections

The full target remains the arbitrary-dimensional statement for independent real coordinates with densities `0<=f_i<=1` and a real symmetric matrix having at least three eigenvalues of modulus at least one. No moment, compact-support, log-concavity, identical-law, sign, or eigen-coordinate-independence hypothesis is added.

The known law-uniform one-dimensional pointwise Fresnel-decay claim is false and is not used. The proof below instead uses a **product-space Brascamp--Lieb estimate in two overlapping spectral directions**, integrates its resulting frequency envelope in `L^{3/2}`, and then uses a third coordinate through either Fourier Holder or a dependent square-smoothing lemma. The live corrections `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, and `QFORM-TWOSHEET-XRAY-ONLY-FALSE` were refreshed before publication.

The exact assigned partner `account04/B04` had no completed QFORM report/handoff at the fresh prepublication snapshot; no result is fabricated. Two compatible completed peer results are actually used:

1. `account01/B08`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260922T114116Z-account01-B08-qform-r11/REPORT.md`, available at the fresh math-open-problems master snapshot `cdd32fd16a694a5f8acc7ba758e0db6596a3e4a1`. Its geometric Brascamp--Lieb / Hausdorff--Young calculation is re-run below at rank two; its published theorem stated `k>=3` only because it then integrated the characteristic function in `L^1`.
2. `account01/B11`, source-pinned at `yspennstate/math-open-problems@e06922bfa31bbd225cdce6ee6aea563254e62563`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T121344Z/REPORT.md`. Its proved dependent-square `L^3` smoothing lemma is applied in Section 4 to an actual Schur-pivot equation.

A newly completed same-slot peer result, `account01/B04` at commit `0de99dd6e357f0321caba2fe129d83282c59380d`, proves a determinant-scale density bound for physical triples with two zero diagonal entries. Its first unpaid branch is a near-pure-cross/nonzero-diagonal aggregation problem. The explicit example in Section 5 has **no zero diagonal entries**, so it lies outside that two-zero-diagonal theorem and tests precisely the requested perturbative direction.

## 2. Rank-two diffuse product-Fourier theorem

### Theorem 2.1 — `QFORM-DIFFUSE-RANK2-L3-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities `f_i` satisfying `0<=f_i<=1`. Let `U in R^{n x 2}` have orthonormal columns. Write `u_i^T` for row `i` and

`c_i=||u_i||_2^2`.

Assume

`c_i<=1/2` for every `i`.

Let `Lambda=diag(lambda_1,lambda_2)` with `lambda_1 lambda_2 !=0`, and let `V_i:R->R` be arbitrary measurable functions. Define

`R = sum_i V_i(X_i) + (U^T X)^T Lambda (U^T X)`.

Then `R` has a density `p_R in L^3(R)` and

`boxed( ||p_R||_3 <= (3e)^(2/3) |lambda_1 lambda_2|^(-1/3). )`   (2.1)

This is an overlapping-direction theorem: the two coordinates of `U^T X` need not be independent and may share every original coordinate.

### Proof

For a fixed frequency `t`, set

`a_{i,t}(x)=f_i(x) exp(i t V_i(x))`.

Thus `|a_{i,t}|=f_i`, `||a_{i,t}||_1=1`, and `||a_{i,t}||_p<=1` for every `p>=1`. Let `mu_t` be the pushforward under `x -> U^T x` of the complex product measure with density `prod_i a_{i,t}(x_i)`.

Ignore zero rows. Put `v_i=u_i/sqrt(c_i)`. Then

`sum_i c_i v_i v_i^T=I_2`,  `sum_i c_i=2`.

Because `c_i<=1/2`, the one-dimensional Hausdorff--Young exponent `q_i=1/c_i` is at least two. The same sharp Hausdorff--Young plus geometric rank-one Brascamp--Lieb calculation as in the cited account01/B08 report gives, with Fourier convention `hat a(s)=int exp(-isx)a(x)dx`,

`||hat mu_t||_1 <= (2pi)^2 prod_i (1-c_i)^(-(1-c_i)/2).`

Using `-(1-c)log(1-c)<=c` and `sum_i c_i=2`,

`boxed( ||hat mu_t||_1 <= (2pi)^2 e. )`                         (2.2)

Nothing in this step requires `k>=3`; that restriction in the peer theorem was only used later for `L^1_t` integrability.

The characteristic function of `R` is

`phi_R(t)=int_{R^2} exp(i t z^T Lambda z) g_t(z) dz`,

where `g_t` is the density of `mu_t`. Fresnel inversion, regularized by `exp(-epsilon |z|^2)` and then `epsilon downarrow0`, together with (2.2), yields

`|phi_R(t)| <= pi e |lambda_1 lambda_2|^(-1/2) |t|^(-1)`        (2.3)

for `t!=0`. Trivially `|phi_R(t)|<=1`. Define

`A = pi e |lambda_1 lambda_2|^(-1/2)`.

Then

`|phi_R(t)| <= min(1,A/|t|)`.

This does **not** resurrect the refuted one-dimensional pointwise-decay claim: (2.3) uses the global two-dimensional product-space Brascamp--Lieb hypothesis `max c_i<=1/2` and is not asserted for an arbitrary single bounded density.

Now integrate the envelope at exponent `3/2`:

`int_R |phi_R(t)|^(3/2) dt
 <= 2[ int_0^A 1 dt + int_A^infinity (A/t)^(3/2) dt ]
 = 6A.`                                                        (2.4)

Hence

`||phi_R||_(3/2) <= (6A)^(2/3).`                                (2.5)

Inverse Hausdorff--Young in the convention `p(y)=(2pi)^(-1) int exp(-ity)phi(t)dt` gives

`||p_R||_3 <= (2pi)^(-2/3) ||phi_R||_(3/2).`

Substituting (2.5) and `A=pi e |det Lambda|^(-1/2)` proves (2.1). Standard distributional Fourier inversion for finite measures with characteristic function in `L^{3/2}` identifies this `L^3` function with the law of `R`. QED.

### Mandatory rank-two indefinite control

When `lambda_1 lambda_2<0`, an `L^infinity` bound on `p_R` is neither claimed nor needed. The two-opposite-sign diagonal uniform example has a logarithmic singularity, which is compatible with `L^3`. Thus (2.1) lands at exactly the regularity level that a third square can smooth.

## 3. Product-Fourier closure with an independent third square

The previous B04 run proved the averaged one-square estimate: if `Z` has density at most one and `d!=0`, then for

`F_d(t)=E exp(i t d Z^2)`,

`||F_d||_3 <= 2(2pi)^(1/3)|d|^(-1/3).`                          (3.1)

Let `Z` be independent of the variables in Theorem 2.1 and allow an arbitrary linear term `uZ+v`. Completing the square changes only a translation of `Z` and an output constant, so (3.1) is unchanged. For

`Q=R+dZ^2+uZ+v`,

independence gives `phi_Q=phi_R F_d` up to a unimodular factor. Holder with exponents `(3/2,3)` and (2.5),(3.1) gives `phi_Q in L^1`. Fourier inversion therefore produces a **bounded continuous** density with

`boxed(
 ||p_Q||_infinity
 <= 2(3e)^(2/3)
    |lambda_1 lambda_2 d|^(-1/3).
)`                                                               (3.2)

The same constant follows from `L^3 * L^{3/2} -> L^infinity` in physical space. The point here is that the first two square directions may overlap arbitrarily in the original coordinates; only the final scalar square is separated.

This strictly extends the previous B04 disjoint-three-block theorem, where all three square directions had to be based on disjoint coordinate sets.

## 4. Fully coupled third direction by a Schur pivot

The independent-square hypothesis in Section 3 can be removed in an important exact-rank branch.

### Theorem 4.1 — `QFORM-DIFFUSE-SCHUR-PIVOT-v1`

Let `X=(W,Z)` have independent real coordinates, all densities bounded by one. Partition a real symmetric matrix as

`A = [[C,b],[b^T,a]]`,  with `a!=0`,

where `Z` is the last original coordinate. Put

`S=C-bb^T/a`.

Assume `S` has rank exactly two, with nonzero eigenvalues `mu_1,mu_2`, and write

`S=U diag(mu_1,mu_2) U^T`

with `U` having orthonormal columns. If every row of `U` has squared norm at most `1/2`, then `Q=X^TAX` has an essentially bounded density satisfying

`boxed(
 ||p_Q||_infinity
 <= 4 sqrt(3e)
    |a|^(-1/2)|mu_1 mu_2|^(-1/4).
)`                                                               (4.1)

No independence between the completed square and the Schur-complement quadratic is assumed.

### Proof

Complete the square only in the original coordinate `Z`:

`Q = W^T S W + a ( Z + a^(-1)b^T W )^2.`                        (4.2)

Set

`R=W^T S W`,  `V=Z+a^(-1)b^T W`.

By Theorem 2.1 with all `V_i=0`,

`||p_R||_3 <= M := (3e)^(2/3)|mu_1 mu_2|^(-1/3).`               (4.3)

For almost every value `R=r`, the conditional law of `V` is a mixture of translations of the original density of `Z`, because `Z` is independent of `W`. Therefore its conditional density is still bounded by one.

Now apply the completed peer result `QFORM-DEPENDENT-SQUARE-L3-SMOOTHING-v1` from account01/B11 to the **actual equation (4.2)**. That lemma states that whenever a base variable has `L^3` density norm `M` and the conditional density of the translated square variable is at most one,

`||p_{R+aV^2}||_infinity <= 4 |a|^(-1/2) M^(3/4).`

Substituting (4.3) gives exactly (4.1). QED.

This is a genuine overlap/coupling result: the third square may contain a linear form in all of the variables supporting the first two spectral directions. The product structure is used only in original coordinates and survives the conditioning step.

## 5. Explicit fully coupled rotated indefinite target instance

Let

`u_1=(1,1,-1,-1)^T/2`,
`u_2=(1,-1,1,-1)^T/2`,

and

`S=u_1u_1^T-u_2u_2^T
 = [[0,1/2,-1/2,0],
    [1/2,0,0,-1/2],
    [-1/2,0,0,1/2],
    [0,-1/2,1/2,0]].`

The two columns `u_1,u_2` are orthonormal, and every row leverage is exactly `1/2`. Put

`b=(1,1,1,1)^T/10`,

and define the five-dimensional matrix

`A = 2 [[S+bb^T, b],[b^T,1]].`                                  (5.1)

Explicitly,

`A = [[1/50, 51/50,-49/50,  1/50,1/5],
      [51/50,1/50,   1/50,-49/50,1/5],
      [-49/50,1/50,  1/50, 51/50,1/5],
      [1/50,-49/50, 51/50,  1/50,1/5],
      [1/5, 1/5,     1/5,   1/5,   2]].`                         (5.2)

All five diagonal entries are nonzero, so the fresh account01/B04 two-zero-diagonal theorem does not apply directly.

To verify the spectral hypothesis exactly, note that `b` is orthogonal to both `u_1,u_2`. On their span, `A` has eigenvalues `2,-2`. On the orthogonal plane generated by the normalized all-ones vector `e=(1,1,1,1)^T/2` and the fifth coordinate, the unscaled matrix in (5.1) has block

`[[1/25,1/5],[1/5,1]]`,

whose eigenvalues are `0` and `26/25`. A second orthogonal direction in the first four coordinates is also null. Therefore the complete eigenvalue multiset is

`{ 2, -2, 52/25, 0, 0 }.`                                      (5.3)

Thus this is a genuinely rotated, fully coupled, indefinite exact target instance with three eigenvalues of modulus at least one.

For the fifth-coordinate pivot, `a=2` and the Schur complement is `2S`, whose nonzero eigenvalues are `2,-2` and whose row leverage remains `1/2`. Theorem 4.1 gives, uniformly over **all** independent input laws with densities bounded by one,

`boxed( ||p_{X^TAX}||_infinity <= 2 sqrt(3e) < 5.712. )`        (5.4)

This is a new nonzero-diagonal near-pure-cross example obtained without a small-pivot loss.

## 6. Relation to the newly completed product-rearrangement peer result

The account01/B04 theorem gives, for an invertible physical triple

`B=[[d,a,b],[a,0,c],[b,c,0]],`

`||p||_infinity <= 12 e^(-2/3)|det B|^(-1/3)`.

Theorem 4.1 supplies a complementary mechanism when the physical diagonal entries do **not** vanish but one scalar pivot leaves a diffuse rank-two Schur complement. In particular, (5.2) has no zero diagonal at all and so is beyond that codimension-two local theorem.

Together the two results remove two different failure modes of naive scalar-pivot estimates:

- the peer theorem is uniform as an isolated diagonal pivot tends to zero on a two-zero-diagonal physical triple;
- the present theorem is uniform in the detailed pivot couplings whenever the rank-two Schur remainder is diffuse, because only `a` and the two Schur eigenvalues enter (4.1).

Neither statement supplies the still-missing dimension-free global aggregation from the sole three-large-eigenvalue hypothesis.

## 7. First unpaid implication

The next B04 implication is now the **localized/diffuse coupling bridge**, compatible with the Pluecker flag isolated by account02/B07:

`QFORM-RANK2-DIFFUSE-COUPLED-PIVOT-v1`:

> Starting from three large spectral directions, in the `q=1` heavy/light flag branch, choose a localized original coordinate and prove that either its scalar pivot plus rank-two Schur complement satisfies a dimension-free version of Theorem 4.1, or another already-paid branch (two-zero-diagonal/pure-cross, definite/indefinite physical triple, or fully diffuse rank three) fires. The argument must tolerate cancellation in the scalar pivot and arbitrary small spectral-complement eigenvalues, and must not select one potentially tiny principal minor.

Equivalently, the remaining quantitative obstruction is no longer the overlap of **two** diffuse directions: Theorem 2.1 pays that overlap at the exact `L^3` exponent. The debt is to aggregate that `L^3` currency with a third localized direction without losing a factor through pivot cancellation or a dimension-dependent coordinate selection.

A promising next mechanism is to average (4.1) over candidate heavy pivots using the exact exterior-power row identity

`sum_{j<k; j,k!=i} det[u_i,u_j,u_k]^2 = ||u_i||_2^2`

rather than choosing one minor, while routing the near-zero pivots to the account01/B04 rearrangement bound.

## 8. Status and integrity

Proved in this run:

- `QFORM-DIFFUSE-RANK2-L3-v1`, explicit constant `(3e)^(2/3)`;
- overlapping-rank-two plus independent third-square density bound (3.2), continuous;
- `QFORM-DIFFUSE-SCHUR-PIVOT-v1`, fully coupled dependent-square bound (4.1);
- the explicit five-variable indefinite target instance (5.2) with exact eigenvalues (5.3) and universal density bound (5.4).

Not proved:

- the full arbitrary-matrix conjecture;
- a universal global extraction/aggregation theorem from three large eigenvalues alone;
- continuity in the dependent-square theorem (only an essentially bounded density is claimed there).

Privacy/write review: this report contains only mathematical statements and repository provenance. No credentials, scheduler identifiers, machine paths, unrelated personal/private data, email/Drive/public release, paid model/API/Codex call, remote workflow, permission expansion, or scheduler mutation is involved.
