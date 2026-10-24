# account01/B15 — joint spectral-split regularity, exact averaged scalar-conditioning gate, and Poisson/Stieltjes reduction

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Worker:** account01/B15  
**Run:** `20260922T180616Z-account01-B15-QFORM-r12`  
**Assignment:** Absolute continuity and regularity  
**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_AVERAGED_SCALAR_CONDITIONING_GATE`  
**Full universal-constant QFORM:** **OPEN**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Fresh target and source state

Fresh owner control advanced during this run to revision `2026-09-22.11`. The sole target remains: for every dimension, every independent cap-one product law, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove

`P(X^T A X in I) <= C |I|`

with one universal finite `C`, or construct a genuine counterexample. Continuity is separate from the central essential-supremum bound.

The current owner message identifies scalar conditioning on the residual quadratic `Q'` as a priority route. This report improves that gate: a **weighted average** of conditional heights is enough; the supremum over residual values is unnecessary. The improvement is exact and comes with a joint absolute-continuity theorem guaranteeing that the scalar-conditioned objects exist as honest densities in the spectral core/rest split.

Assigned partner actually consumed: `account02/B15`, run `20260922T170424Z-account02-B15-qform-r5`, canonical source `yspennstate/math-open-problems@42920d321a16b9393856cfb0ed78d8557170ad38`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T170424Z-account02-B15-qform-r5/REPORT.md`. That report proves scalar absolute continuity for every nonzero quadratic form and, using its assigned partner, records the fixed-matrix rank>=3 `C_0` theorem; it also proves that no target-uniform `C_0` tail envelope exists.

A second dependency from my preceding run is the exact affine closure `C_aff=C_hom`, canonical source `yspennstate/math-open-problems@e4ec163c51bac9e10fd5737e9b1333a410fb7ce7`, same worker root, run `20260922T170451Z-account01-B15-qform-r11`.

## 2. Spectral split

Fix a target matrix `A`. Select any three protected eigenvectors and let

`A = B + C`,

where

`B = U Lambda U^T`,

`U in R^(n x 3)` has orthonormal columns, `Lambda=diag(lambda_1,lambda_2,lambda_3)` with `|lambda_j|>=1`, and `C` is the sum of all remaining spectral components. Thus

`BC=CB=0`, `range(C) subset range(U)^perp`.

Write

`Y = U^T X in R^3`,
`S = Y^T Lambda Y = X^T B X`,
`V = X^T C X`,
`Q = S+V`.

If `C=0`, this is the already isolated exact-rank-three branch. The nontrivial full-rank case is `C!=0`.

## 3. New regularity theorem: `(Y,V)` has a joint density

### Theorem 3.1

Assume `C!=0`. For every input law absolutely continuous with respect to Lebesgue measure (in particular every admissible cap-one product law), the random vector

`(Y,V)=(U^T X, X^T C X) in R^4`

is absolutely continuous with respect to four-dimensional Lebesgue measure.

### Proof

Consider the smooth map

`F:R^n -> R^4`,
`F(x)=(U^T x, x^T C x)`.

The first three rows of `DF(x)` are the fixed orthonormal vectors `u_1^T,u_2^T,u_3^T`. The last row is `(2Cx)^T`. Because `range(C)` is orthogonal to `range(U)`, `Cx` is orthogonal to each `u_j`. Therefore

`rank DF(x)=4` exactly when `Cx!=0`.

Since `C!=0`, `ker(C)` is a proper linear subspace and hence has `n`-dimensional Lebesgue measure zero. On `R^n\ker(C)`, `F` is a submersion. By the constant-rank theorem, every point there has a neighborhood in which smooth coordinates identify `F` with projection onto the first four coordinates. The preimage of a Lebesgue-null subset of `R^4` is therefore null in each such chart. Second countability gives a countable cover. Adding the null critical set `ker(C)` proves

`Leb_n(F^{-1}(N))=0`

for every null `N subset R^4`.

Because the law of `X` is absolutely continuous, its pushforward by `F` is absolutely continuous. QED.

### Corollary 3.2

The pair `(S,V)` also has a joint density `g(s,v)` on `R^2`.

Indeed `(Y,V)` has a joint density `G(y,v)`, and for almost every `v`, the `y`-slice `G(.,v)` is absolutely continuous; the nonzero rank-three quadratic map `y -> y^T Lambda y` sends such a law to an absolutely continuous scalar law. Integrating over `v` gives the joint density of `(S,V)`.

A direct two-dimensional proof is also available: the gradients `2Bx` and `2Cx` are orthogonal, so the map `x -> (x^T Bx,x^T Cx)` has rank two off `ker(B) union ker(C)`, a null set.

This regularity is source-exact and uses no rotated-independence assumption.

## 4. Exact averaged scalar-conditioning inequality

Let `g(s,v)` be the joint density of `(S,V)`, and let

`p_V(v)=int_R g(s,v) ds`.

For almost every `v` with `p_V(v)>0`, define the conditional density

`h_v(s)=g(s,v)/p_V(v)`.

Since `Q=S+V`, Fubini gives the output density

`p_Q(t)=int_R g(t-v,v) dv`

for almost every `t`. Consequently

`p_Q(t) <= int_R sup_s g(s,v) dv`

and therefore

`boxed( ||p_Q||_infinity <= int_R sup_s g(s,v) dv )`.          (4.1)

Equivalently,

`boxed( ||p_Q||_infinity <= E[ ||p_{S|V}||_infinity ] )`.       (4.2)

This is the key new inference. The current owner-state route uses the stronger payment

`sup_v ||p_{S|V=v}||_infinity`.

But (4.2) shows that only the **average conditional height** is needed. Rare residual values with very sharp conditional laws are automatically discounted by their actual `V`-probability. No division by a tiny `p_V(v)` survives in the joint-density form (4.1).

The improvement is not cosmetic: `E Z <= sup Z`, so any proof of the old supremum gate proves (4.2), while (4.2) allows arbitrarily bad exceptional `v` provided their weighted contribution is integrable.

## 5. Insert the rank-three coarea theorem without a residual supremum

Let `G(y,v)` be the joint density of `(Y,V)`. Then

`p_V(v)=int_R3 G(y,v) dy`,

and, for `p_V(v)>0`,

`rho_v(y)=G(y,v)/p_V(v)`

is the conditional density of `Y` given `V=v`.

Use the current source-state rank-three coarea theorem in its exact scale-correct form:

`||p_{Y^T Lambda Y}||_infinity <= K ||rho||_infinity^(2/3)`

for `|lambda_j|>=1`, with one absolute `K`.

Applying it conditionally and then using (4.2) yields

`||p_Q||_infinity
 <= K int p_V(v) ||rho_v||_infinity^(2/3) dv
 =  K int p_V(v)^(1/3) ||G(.,v)||_infinity^(2/3) dv`.          (5.1)

Thus the full conjecture follows from the strictly weaker scalar-conditioned functional bound

`boxed(
 sup_target_splits
 int p_V(v)^(1/3) ||G(.,v)||_infinity^(2/3) dv < infinity.
)`                                                               (5.2)

This replaces the currently advertised

`sup_v ||rho_v||_infinity < infinity`

by a weighted integral. The two statements are not equivalent: (5.2) allows exceptional high conditional peaks on low-probability residual levels.

The exact first unpaid implication after this run is therefore (5.2), not the stronger residual-level supremum.

## 6. Poisson/Stieltjes exact regularization

The preceding conditional statement can be regularized without changing the sharp target constant.

For a probability measure `mu` on `R`, define its interval-density seminorm

`D(mu)=sup_I mu(I)/|I| in [0,infinity]`,

where the supremum is over open intervals. Let

`P_eta(x)=(1/pi) eta/(x^2+eta^2)`

be the Poisson kernel, and

`H_eta(mu)=sup_t (P_eta*mu)(t)`.

### Theorem 6.1 — exact Poisson identity

For every probability measure `mu`,

`boxed( D(mu)=sup_{eta>0} H_eta(mu)=lim_{eta downarrow 0} H_eta(mu) )`.   (6.1)

The limit is monotone increasing as `eta downarrow0`.

### Proof

If `D(mu)=D<infinity`, interval domination implies `mu<=D dx`, hence

`P_eta*mu <= D`

for every `eta`; so `sup_eta H_eta<=D`.

Conversely, suppose `sup_eta H_eta<=M`. The measures

`mu_eta=(P_eta*mu)(t)dt`

converge weakly to `mu` as `eta downarrow0`, since they are the laws of `Z+eta C_0` with `Z~mu` and independent standard Cauchy `C_0`. Every `mu_eta` has density at most `M`. Portmanteau on open intervals gives

`mu(I)<=liminf mu_eta(I)<=M|I|`,

so `D(mu)<=M`. This proves equality.

Finally `P_eta*P_delta=P_(eta+delta)`. Hence

`H_(eta+delta)(mu)<=H_eta(mu)`,

so `H_eta` is nonincreasing in `eta` and (6.1) is a monotone boundary limit. QED.

### Stieltjes form

For

`m_mu(z)=int (x-z)^(-1) dmu(x)`, `Im z>0`,

we have

`Im m_mu(t+i eta)=int eta/((x-t)^2+eta^2) dmu(x)
                 =pi (P_eta*mu)(t)`.

Therefore

`boxed( D(mu)=(1/pi) sup_{z in C_+} Im m_mu(z) )`.              (6.2)

For the QFORM class, the sharp universal constant is exactly the sharp uniform upper bound on this positive resolvent quantity. This avoids the refuted law-uniform pointwise characteristic-function decay and does not require `phi in L1`.

## 7. Exact analytic-subclass reduction using the preceding affine closure

Let `C_0` be standard Cauchy, whose density `1/[pi(1+x^2)]` is <=1, and let it be independent of the target inputs. Then

`Q+eta C_0`

has density `P_eta*mu_Q`, real-analytic in the output variable at every fixed `eta>0`.

As an affine quadratic in the enlarged independent vector `(X,C_0)`, it has Hessian `A direct_sum [0]` and linear coefficient `eta/2` in the new coordinate. The Hessian retains the three protected eigenvalues. My preceding exact affine-closure theorem gives equality of the sharp homogeneous and affine constants. Combining that closure with Theorem 6.1 yields:

> **Corollary 7.1.** The full QFORM sharp constant is exactly the sharp constant on the subclass of Cauchy-output-regularized affine targets `Q+eta C_0`, uniformly over all `eta>0`.

Even a fixed dyadic sequence `eta=2^{-k}` suffices because of monotonicity in Theorem 6.1.

Thus a proof may assume a real-analytic output density at positive scale and then pass monotonically to the original law with **zero constant loss**.

## 8. Assigned-partner theorem applied to an actual inequality

The assigned partner `account02/B15` r5 records, via its completed partner theorem, that every fixed rank>=3 target law has an individually bounded density `p_Q in C_0(R)`. Applying that result to Theorem 6.1 gives, for every fixed owner-target instance,

`boxed( max_t p_Q(t)=lim_{eta downarrow0} ||P_eta*p_Q||_infinity )`.    (8.1)

Because `p_Q in C_0`, Poisson approximation is uniform in `t`; hence the limit in (8.1) is not merely an essential-supremum statement. This is an actual use of the partner regularity result.

The same partner run proves there is no target-uniform tail envelope `g(R)->0`. Equation (8.1) shows why that obstruction does not affect the reduction: no uniform tail localization or uniform convergence rate is needed. Each target is regularized at its own output location, while the **height constant** is the only quantity kept uniform.

## 9. Current end-to-end conditional proof

The surviving proof skeleton is now:

1. Choose three protected eigenvectors and split `A=B+C` spectrally.
2. If `C=0`, use the completed rank-exactly-three theorem.
3. If `C!=0`, Theorem 3.1 gives a genuine joint density `G(y,v)` for `(Y,V)`.
4. Apply rank-three coarea conditionally in `v`.
5. Average, rather than take a supremum, to obtain (5.1).
6. Prove the single remaining target-level estimate (5.2) from original-coordinate product provenance.
7. Then `||p_Q||_infinity<=KC` universally. The partner `C_0` theorem upgrades the resulting essential bound to the canonical continuous representative if its source status survives independent review.

No rotated independence is used, no projection-only shortcut is asserted, no pointwise quadratic Fourier decay is used, and no uniform tail envelope is assumed.

## 10. Exact old/new missing implications

**Old owner-state missing implication:** bound uniformly in `v` the conditional rank-three core density after conditioning on the scalar residual quadratic `V=Q'`.

**New missing implication:** only prove the weighted scalar-level functional

`int p_V(v)^(1/3) ||G(.,v)||_infinity^(2/3) dv <= C_0`           (10.1)

for the joint density `G` of `(Y,V)`, uniformly over all target instances and all choices of three protected eigenvectors.

This is a materially weaker gate and is the first unpaid inference after this run. The next recommended attack is to estimate (10.1) directly by a product-preserving four-dimensional coarea/Brascamp--Lieb argument, **before** normalizing by `p_V(v)`; normalizing first recreates the discarded rare-level supremum.

## 11. Nonclaims

The full QFORM theorem is not proved here. Equation (10.1) remains open. The partner fixed-matrix `C_0` theorem is consumed with its source-reported status and is not upgraded to an independent review by this report. The Poisson/Stieltjes identity is a reduction, not a universal height estimate by itself.
