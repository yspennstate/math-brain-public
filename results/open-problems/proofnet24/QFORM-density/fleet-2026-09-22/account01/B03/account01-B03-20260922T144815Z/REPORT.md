# account01/B03 — independent-copy rectangular cross-block theorem

**Run:** `account01-B03-20260922T144815Z`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Decoupled time integral  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and scope

The full owner target remains open: for every dimension, every collection of independent real random variables whose one-dimensional probability densities are bounded by one, and every real symmetric matrix `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has one dimension- and law-independent bounded density, or produce a target-valid counterexample. Continuity is a separate desired conclusion.

This run proves a new supporting theorem for arbitrary **physical rectangular cross blocks**. The proof uses the independent-copy identity for `|phi_Q(t)|^2` but deliberately does **not** condition on a conjugate sum/difference variable. Thus it obeys the completed partner correction `QFORM-UV-CONDITIONAL-CAP-FALSE`: the dependence inside `(X_i+X_i',X_i-X_i')` is never discarded.

The new theorem keeps arbitrary same-side quadratic terms, arbitrary couplings to outside coordinates, arbitrary signs, and arbitrary additional spectrum. It removes every range-leverage condition from the cross-block Fourier step. What remains unpaid for the full conjecture is a structural extraction/aggregation theorem that forces a quantitatively useful cross block or a bank/hyperbolic alternative from only the three-large-eigenvalue hypothesis.

## 2. Dependencies actually used

1. **Product marginal density theorem.** Galyna Livshyts, Grigoris Paouris and Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1: if `Y=(Y_1,...,Y_N)` has product density `prod f_i` with `||f_i||_infinity<=1`, then every `r`-dimensional orthogonal marginal has density bounded by `2^(r/2)`. This exact theorem is also source-read and used in the fleet at `yspennstate/math-open-problems@1f85677029fc5ae27fc69b278620ae89d789efd2`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260922T132134Z-account04-B20-QFORM-r1/REPORT.md`.
2. **Named assignment partner account02/B03.** Canonical report `yspennstate/math-open-problems@24fc7b37c60f77b399936faa7f280296a7ce8c8c`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T131240Z-b03-qform-auto11/REPORT.md`. It proves the exact hard family
   `A_m=[1] direct_sum (J_m/m) direct_sum (-J_m/m)`, whose nonzero spectrum is `(1,1,-1)` and whose every original-coordinate cross cut has rank at most two. Its bank decomposition is applied quantitatively in Section 8 below.
3. **Named partner correction.** `QFORM-UV-CONDITIONAL-CAP-FALSE`, canonical partner report `yspennstate/math-open-problems@0d99f085f5378d267057cc5b9bcbf8e53ca494b5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T124226Z-b03-qform-auto11/REPORT.md`. For iid `Uniform[0,1]`, conditioning on `V=X-X'` yields `||p_{U|V=v}||_infinity=1/[2(1-|v|)]`; hence a proof may not preserve the unit cap after conditioning `U=X+X'` on `V` or conversely.

No pointwise scalar Fresnel bound, post-rotation independence, conditional sum/difference cap, moment assumption, compact support, log-concavity, or connected-support assumption is used.

## 3. Compact conditional end-to-end chain

The full problem would follow from the following structural alternative with universal quantitative constants:

- either a physical cross block of rank `r>=3` has singular-value product bounded below, and the theorem below gives a bounded continuous density directly;
- or after one physical scalar square pivot, the Schur residual has a physical exact-rank-two cross block whose two singular values have product bounded below, and the half-Riesz consequence below gives linear small-ball scaling;
- or the matrix has the localized/overlap geometry requiring the already identified bank/hyperbolic aggregation branch.

The first two analytic implications are proved here without a leverage hypothesis. The first unpaid implication is therefore structural rather than Fourier-analytic.

## 4. Main theorem: independent-copy rectangular cross-block decay

### Theorem `QFORM-COPY-RECTANGULAR-CROSS-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities `f_i` satisfying `0<=f_i<=1`. Let `A` be any real symmetric `n x n` matrix and

`Q=X^T A X`, `phi(t)=E exp(itQ)`.

Choose disjoint sets of **original coordinate indices** `I,J`, and put

`B=A[I,J]`.

Assume `B` has rank `r>=1`, with positive singular values

`sigma_1,...,sigma_r`,

and write

`Delta_r(B)=prod_{j=1}^r sigma_j >0`.

Then for every real `t`,

`boxed{
 |phi(t)|^2 <= min{1, (2*pi)^r |t|^(-r) Delta_r(B)^(-1)}
}`                                                               (4.1)

and therefore

`boxed{
 |phi(t)| <= min{1, (2*pi)^(r/2) |t|^(-r/2) Delta_r(B)^(-1/2)}.
}`                                                               (4.2)

The estimate is uniform in the laws of the inputs, the dimensions of `I,J`, every same-side block of `A`, every coupling from `I union J` to the complementary coordinates, every sign pattern, and every additional eigenvalue of `A`.

### Proof

Let `X'` be an independent copy of `X`. The exact collision identity is

`|phi(t)|^2 = E exp(it(Q(X)-Q(X'))).`                              (4.3)

Let `K` be the complement of `I union J`, and condition on `(X_K,X'_K)`. All terms of `Q(X)-Q(X')` other than the `I-J` cross interaction split into one function of `(X_I,X'_I)` and one function of `(X_J,X'_J)`, plus a constant depending only on the conditioned variables. More precisely, after discarding the irrelevant constant phase, the conditional phase has the form

`F_I(X_I,X'_I) + F_J(X_J,X'_J)
 + 2 X_I^T B X_J - 2 X_I'^T B X_J'.`                              (4.4)

The functions `F_I,F_J` can contain arbitrary quadratic terms inside their own coordinate blocks and arbitrary linear terms induced by the conditioned outside coordinates. Their exponentials have modulus one; no structural assumption on them is required.

Take a thin singular-value decomposition

`B=L Sigma R^T`,

where `L^T L=R^T R=I_r` and `Sigma=diag(sigma_1,...,sigma_r)`. Define the original-coordinate orthogonal projections

`P=L^T X_I`, `P'=L^T X'_I`,
`S=R^T X_J`, `S'=R^T X'_J`.                                       (4.5)

By the Livshyts--Paouris--Pivovarov marginal theorem, `P` and `S` have probability densities `p_L,p_R` satisfying

`||p_L||_infinity <= 2^(r/2)`,
`||p_R||_infinity <= 2^(r/2)`.                                     (4.6)

Disintegrate the `I`-copy pair with respect to `(P,P')` and define the complex amplitude

`a_t(p,p')
 =p_L(p)p_L(p') E[exp(it F_I(X_I,X'_I)) | P=p,P'=p']`.             (4.7)

Likewise define `b_t(s,s')` from the `J` pair. Since the conditional phases are unimodular,

`|a_t(p,p')| <= p_L(p)p_L(p')`,
`|b_t(s,s')| <= p_R(s)p_R(s')`.                                    (4.8)

Hence, using `||p||_2^2<=||p||_infinity||p||_1=||p||_infinity`,

`||a_t||_2 <= ||p_L||_2^2 <= 2^(r/2)`,
`||b_t||_2 <= ||p_R||_2^2 <= 2^(r/2)`.                             (4.9)

This is the key place where the two-copy argument pays for arbitrary within-block phases without conditioning any sum on any difference.

Put

`x=(p,p') in R^(2r)`, `y=(s,s') in R^(2r)`,
`M=diag(2 Sigma,-2 Sigma)`.                                        (4.10)

The conditional collision integral is exactly

`I_t = int int a_t(x) b_t(y) exp(it x^T M y) dx dy`.               (4.11)

For completeness, the standard bilinear Plancherel estimate in dimension `d` is

`|int int a(x)b(y)exp(it x^T M y)dxdy|
 <=(2*pi)^(d/2)|t|^(-d/2)|det M|^(-1/2)||a||_2||b||_2`.            (4.12)

Indeed, with the convention `hat a(xi)=int exp(-i xi.x)a(x)dx`, integration in `x`, Cauchy--Schwarz in `y`, the change of variables `xi=-tMy`, and Plancherel prove (4.12) exactly.

Here `d=2r` and

`|det M|^(1/2)=2^r Delta_r(B)`.                                    (4.13)

Combining (4.9), (4.12), and (4.13), the projection-density loss `2^r` cancels the cross-phase determinant factor `2^r`, leaving

`|I_t| <= (2*pi)^r |t|^(-r) Delta_r(B)^(-1)`.                      (4.14)

The bound is independent of the conditioned outside coordinates. Averaging them in (4.3) gives (4.1); `|phi(t)|<=1` and square rooting give (4.2). QED.

### Why the partner correction is respected

One can linearly rewrite the two-copy variables as sums and differences, but then each pair is dependent and conditional density caps can blow up. Equations (4.5)--(4.11) instead keep the two independent copies as a single `2r`-dimensional bilinear packet. No conditional density of `X_i+X_i'` given `X_i-X_i'` is ever introduced. Thus the mechanism uses the independent-copy identity while retaining exactly the dependence that the account02/B03 correction says must be retained.

## 5. Direct density consequence for cross rank at least three

For `r>=3`, (4.2) is integrable. Put

`T=2*pi Delta_r(B)^(-1/r)`.

Then the two branches in (4.2) meet at `T`, and

`int_R |phi(t)|dt
 <= 2[T+(2*pi)^(r/2)Delta_r(B)^(-1/2)
       int_T^infinity t^(-r/2)dt]
 =4*pi * r/(r-2) * Delta_r(B)^(-1/r).`                              (5.1)

Fourier inversion therefore yields a bounded continuous density vanishing at infinity, with

`boxed{
 ||p_Q||_infinity <= 2r/(r-2) * Delta_r(B)^(-1/r),   r>=3.
}`                                                                  (5.2)

In particular, a physical rectangular rank-three cross block gives

`boxed{ ||p_Q||_infinity <= 6 Delta_3(B)^(-1/3). }`                 (5.3)

Unlike a local square-minor theorem, (5.3) applies when `I` and `J` are arbitrarily large and `B` has rank exactly three. Unlike the regularized-determinant route, it has no coordinate-range leverage hypothesis. The price is the reciprocal pseudodeterminant `Delta_3(B)^(-1/3)`; the three-large-eigenvalue hypothesis alone does not guarantee this quantity is bounded for one fixed cut.

## 6. Half-Riesz consequence: the rank-two time integral

The assignment specifically asks for an integrated estimate that recovers linear small-ball scaling. For every `r>=2`, (4.2) gives the exact weighted integral

`int_R |phi(t)| |t|^(-1/2) dt
 <= 4r/(r-1) * sqrt(2*pi) * Delta_r(B)^(-1/(2r)).`                   (6.1)

To check the constant, split at the same `T`. On one half-line,

`int_0^T t^(-1/2)dt =2sqrt(T)`,

and the tail equals

`(2*pi)^(r/2)Delta_r(B)^(-1/2)
 int_T^infinity t^(-(r+1)/2)dt
 =2sqrt(T)/(r-1).`

The two half-lines yield (6.1).

The Abel/Riesz identity used in the preceding B03 run says that for any real random variable `R`,

`sup_z E|z-R|^(-1/2)
 <=(2*pi)^(-1/2) int_R |phi_R(t)||t|^(-1/2)dt`,                    (6.2)

whenever the right side is finite. Combining (6.1) and (6.2),

`boxed{
 sup_z E|z-Q|^(-1/2)
 <= 4r/(r-1) Delta_r(B)^(-1/(2r)),   r>=2.
}`                                                                  (6.3)

For rank two this is especially clean:

`boxed{
 sup_z E|z-Q|^(-1/2) <= 8 Delta_2(B)^(-1/4).
}`                                                                  (6.4)

This is a leverage-free, arbitrary-residual rank-two half-Riesz theorem. It is the integrated `|phi|^2` estimate requested by the assignment.

## 7. Linear small-ball scaling after one scalar square pivot

Suppose the original-coordinate quadratic form can be written, after completing a square in one **physical** coordinate `Z`, as

`Q=d(Z+h(W))^2+R(W)`,                                               (7.1)

where `d!=0`, `Z` is independent of `W`, and the density of `Z` is bounded by one. Assume the residual quadratic form `R` has a physical exact-rank-two cross block `B` with singular-value product `Delta_2(B)`.

For every fixed `W`, the density of `d(Z+h(W))^2` is bounded by

`|d|^(-1/2)|y|^(-1/2)`                                             (7.2)

at nonzero `y`; averaging over `W` therefore gives

`p_Q(t) <= |d|^(-1/2) E|t-R|^(-1/2).`                              (7.3)

Apply (6.4):

`boxed{
 ||p_Q||_infinity
 <= 8 |d|^(-1/2) Delta_2(B)^(-1/4).
}`                                                                  (7.4)

Equivalently, every interval `J` satisfies the linear small-ball estimate

`P(Q in J) <= 8 |d|^(-1/2) Delta_2(B)^(-1/4) |J|.`                 (7.5)

All residual same-side quadratic terms and all residual extra spectrum are allowed. What is crucial is that the selected physical cross block has **exact rank two**; if it has higher rank, one may instead use the higher-rank consequences above, but it is not legitimate to throw away extra cross directions by changing the phase.

This theorem improves the analytic interface in the localized branch: no `rho<1` leverage condition is needed for an exact-rank-two residual cross block. It does **not** revive the separately refuted claim that every target matrix must have one such scalar-pivot/rank-two extraction.

Continuity is proved in the direct `r>=3` branch because `phi in L1`. Equation (7.4) proves essential boundedness/absolute continuity at its scope; continuity is not proved by this half-Riesz argument alone.

## 8. Required named-partner application: the coloop-bank family

Apply (7.4) to the exact family produced by the assigned partner account02/B03:

`A_m=[1] direct_sum (J_m/m) direct_sum (-J_m/m)`,                   (8.1)

whose nonzero spectrum is `(1,1,-1)`. The partner already proves a sharper bank-specific bound `pi sqrt(2)`; the purpose here is to test and apply the new time-integral theorem on the family that defeats every rank-three cross cut.

Use the hub coordinate as the scalar pivot, so `d=1` and the residual is

`R=P_m^2-R_m^2`,                                                    (8.2)

with one positive and one negative rank-one bank. For `m>=2`, split each bank between the two physical sides of a cross cut with

`p=floor(m/2)`, `q=ceil(m/2)`.

The residual cross block is block diagonal with two nonzero singular values, both equal to

`sqrt(pq)/m`.

Hence its exact rank-two singular product is

`Delta_2 = pq/m^2 >= 2/9`,                                         (8.3)

where the minimum for `m>=2` occurs at `m=3`. Equation (7.4) gives the genuine all-law, all-`m>=2` inequality

`boxed{
 ||p_{Q_m}||_infinity
 <=8 (9/2)^(1/4)
 =11.6518025209... .
}`                                                                  (8.4)

This is weaker numerically than the partner's special-purpose `pi sqrt(2)=4.44288...`, but it is structurally different: it follows directly from the independent-copy cross-block time integral, uses no bank convolution theorem, and remains valid with arbitrary same-side residual phases covered by Theorem 4.1. It therefore satisfies the assignment requirement to consume the named partner result in an actual inequality.

The family also confirms why the theorem is stated for rank two as well as rank three: every cross cut has rank at most two, yet a balanced rank-two cut has stable singular product and is enough after the hub square is consumed.

## 9. Exact checks

A deterministic checker bundled with this report verifies:

- `|det diag(2Sigma,-2Sigma)|^(1/2)=2^r prod sigma_j` for random positive singular values and `2<=r<=6`;
- the weighted-integral constant in (6.1) against numerical quadrature for `r=2,3,4,5`;
- the partner-family balanced-cut inequality `Delta_2>=2/9` for `2<=m<=100` and the displayed worst-case constant.

The checker is regression evidence only; the proof above establishes the all-dimensional statements.

## 10. Status and first unpaid implication

**Proved in this report:**

- `QFORM-COPY-RECTANGULAR-CROSS-v1`, equations (4.1)--(4.2), for every physical cross block of any rank and arbitrary residual couplings;
- bounded continuous density (5.2) for cross rank `r>=3`;
- the leverage-free half-Riesz trace (6.3), in particular (6.4) for exact cross rank two;
- the scalar-pivot linear-small-ball estimate (7.4);
- actual application (8.4) to the completed account02/B03 hard family.

**Not proved:** the full three-large-eigenvalue conjecture. The owner hypothesis does not by itself guarantee a fixed rank-three cross cut, and `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` forbids claiming a universal one-pivot exact-rank-two extraction.

The first unpaid implication is now a **product-preserving structural alternative**: from the sole assumption of at least three eigenvalues of modulus at least one, prove that one of the following has universal quantitative mass:

1. a physical rank-`r>=3` cross block with controlled `Delta_r`;
2. a physical scalar pivot plus post-Schur exact-rank-two cross block with controlled `|d|^2 Delta_2`;
3. a disjoint-bank/hyperbolic-square aggregate certificate of the type required by the known overlap/coloop families.

The new theorem closes the Fourier/Riesz payment once branch (1) or the exact-rank-two version of branch (2) is structurally produced. It does not close branch (3), nor does it make additional eigenvalues disappear.

**Full target status:** `OPEN`.
