SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-24T04:25:54Z.
attacking: a zero-loss reduction of the full rough/degenerate target to compactly supported smooth product laws and generic target matrices, followed by same-constant C0 closure.

# account03/B15 — smooth-compact + generic-matrix closure at the exact universal constant

Programme: QFORM-DENSITY-3EIG-20260922  
Run: `20260924T042554Z-account03-B15-qform-auto11`  
Status: `TARGET_LEVEL_CLOSURE_PROVED / BEST_CONSTANT_PRESERVED / PARTNER_APPLIED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Purpose

The owner target allows arbitrary measurable one-dimensional probability densities `0<=f_i<=1` and arbitrary real symmetric target matrices with at least three eigenvalues of absolute value at least one. Several analytic routes are substantially cleaner when the marginals are smooth and compactly supported and when the matrix has no algebraic degeneracies. Those hypotheses cannot be added silently.

This report proves that they may be imposed as a **proof reduction with exactly zero loss in the optimal universal height constant**, provided the estimate proved on the reduced class is uniform in all support locations/sizes and in all genericity parameters. The reduction is measure-level and does not use moments, post-rotation independence, Gaussian smoothing, or pointwise Fourier decay.

It also applies the completed account04/B15 same-constant regularity theorem to show that, after the reduced-class height estimate is transported back, the rough target law has a canonical `C_0` density with the same height constant. Thus a full proof may work on smooth compact product laws and generic matrices and need prove only the interval-height estimate there; roughness, exact matrix degeneracies, and continuity can all be restored afterward without increasing the constant.

## 2. Concentration functional

For a probability measure `mu` on `R`, define

`H(mu) := sup_I mu(I)/|I|`,

where the supremum is over nonempty bounded open intervals. If `H(mu)<infinity`, then `mu<=H(mu) dt`; indeed every open set is a disjoint countable union of open intervals, so `mu(G)<=H(mu)|G|`, and outer regularity gives the same domination for every Borel set. Hence `mu` has a density `p` with `||p||_infinity<=H(mu)`.

Conversely, if `mu=p dt` with `p in L^infinity`, then `H(mu)<=||p||_infinity`, and Lebesgue differentiation gives equality. Thus the owner height problem is exactly the problem of uniformly bounding `H`.

## 3. Cap-preserving compact-smooth approximation in one dimension

### Lemma 3.1

Let `f` be a probability density on `R` with `0<=f<=1`. For every `epsilon>0` there exists `g in C_c^infinity(R)` such that

`0<=g<=1`, `int g=1`, and `||g-f||_1<epsilon`.

### Proof

Choose `R` so that

`d := int_{|x|>R} f(x) dx < epsilon/4`.

Put `f_R=f 1_{[-R,R]}`; its mass is `m=1-d`. Let `rho_delta` be a nonnegative compactly supported standard mollifier of mass one. For sufficiently small `delta`,

`u := f_R * rho_delta`

satisfies

`u in C_c^infinity`, `0<=u<=1`, `int u=m`, and `||u-f_R||_1<epsilon/2`.

Choose once and for all a nonnegative `psi in C_c^infinity` with `int psi=1` and `||psi||_infinity<=1`; such a function is obtained by dilating any standard bump. Translate `psi` far enough that its support is disjoint from `supp u`, and denote the translate by `psi_L`. Define

`g=u+d psi_L`.

Because the supports are disjoint,

`0<=g<=max(1,d)<=1`,

and `int g=m+d=1`. Finally,

`||g-f||_1 <= ||u-f_R||_1 + ||f_R-f||_1 + d||psi_L||_1`

`< epsilon/2 + d+d < epsilon`.

This proves the lemma. Notice that no renormalization of a truncation is used; such a renormalization could violate the cap one condition.

## 4. Product approximation and deterministic pushforward

Let `f_1,...,f_n` be arbitrary cap-one probability densities and choose compact-smooth cap-one probabilities `g_{i,k}` with `||g_{i,k}-f_i||_1 ->0`. Set

`F=prod_i f_i`, `G_k=prod_i g_{i,k}`.

A telescoping expansion gives the exact dimension-finite estimate

`||G_k-F||_1 <= sum_i ||g_{i,k}-f_i||_1 ->0`.  (4.1)

For every measurable map `q:R^n->R` and every Borel set `E`,

`| int 1_{q(x) in E} (G_k-F)(x) dx | <= ||G_k-F||_1`.  (4.2)

Thus, with the matrix fixed, any interval inequality proved uniformly for the compact-smooth product approximants passes directly to the rough product law with the identical constant. This already strengthens ordinary mollification closure by permitting compact support without cap loss.

## 5. Generic symmetric matrices are dense

For fixed `n`, let `G_n` be the set of real symmetric matrices satisfying both:

1. the spectrum is simple;
2. every nonempty principal minor is nonzero.

Then `G_n` is open and dense in the vector space of real symmetric matrices.

Indeed, the discriminant of the characteristic polynomial and every principal determinant are polynomial functions of the matrix entries. Their product is not the zero polynomial: a diagonal matrix with distinct nonzero diagonal entries makes every factor nonzero. Hence the complement of `G_n` is the zero set of a nonzero real polynomial and has empty interior.

In particular, a proof on `G_n` may assume every physical principal block is nonsingular, but **only if its final constant is uniform as those minors approach zero**. The closure below does not rescue a bound containing reciprocal genericity gaps.

## 6. Preserving the three-large-eigenvalue hypothesis while genericizing

Let `A` be symmetric and suppose it has at least three eigenvalues with absolute value at least one. Take `eta_k downarrow0`. Since `G_n` is dense, choose `A_k in G_n` such that

`||A_k-(1+2 eta_k)A||_op < eta_k`.  (6.1)

If `lambda(A)>=1`, then the corresponding eigenvalue of `(1+2 eta_k)A` is at least `1+2 eta_k`; Weyl's inequality and (6.1) leave it at least `1+eta_k` for `A_k`. Likewise every eigenvalue `lambda(A)<=-1` remains at most `-1-eta_k`. Therefore every `A_k` still has at least three eigenvalues of absolute value strictly bigger than one.

Also `A_k->A` in operator norm.

This argument handles all signs and all exact degeneracies. It uses no eigen-coordinate independence.

## 7. Simultaneous law-and-matrix closure

Let `X` have rough product density `F`, let `G_k` be the compact-smooth product approximants from Section 4, and let `A_k` be the generic target matrices from Section 6. Denote by `mu_k` the law under density `G_k` of

`q_k(x)=x^T A_k x`,

and by `mu` the law under density `F` of

`q(x)=x^T A x`.

For every bounded continuous `phi`,

`| int phi(q_k) G_k - int phi(q) F |`

`<= ||phi||_infinity ||G_k-F||_1 + int |phi(q_k(x))-phi(q(x))| F(x) dx`.  (7.1)

The first term tends to zero by (4.1). For every fixed finite `x`, `q_k(x)->q(x)` because `A_k->A`; the second term tends to zero by dominated convergence. No moment bound on `X` is needed. Hence

`mu_k => mu` weakly.  (7.2)

Suppose one constant `C` satisfies

`mu_k(I) <= C |I|`  (7.3)

for every compact-smooth product law, every generic target matrix with at least three eigenvalues of absolute value at least one, and every bounded open interval `I`. Portmanteau applied to the open interval `I` gives

`mu(I) <= liminf_k mu_k(I) <= C |I|`.  (7.4)

By Section 2, the rough/degenerate target law therefore has a density bounded essentially by the same `C`.

## 8. Exact equality of the optimal constants

Let `C_all` be the supremum of `H(Law(X^TAX))` over the full owner target, and let `C_gen-sm` be the same supremum restricted simultaneously to:

- `f_i in C_c^infinity(R)`, `0<=f_i<=1`, `int f_i=1`;
- symmetric `A in G_n` with at least three eigenvalues of absolute value at least one.

Trivially `C_gen-sm <= C_all` because the reduced class is a subclass. Conversely, if `C_gen-sm<infinity`, Section 7 transports the bound `C_gen-sm` to every full target instance, so `C_all<=C_gen-sm`. If `C_gen-sm=infinity`, the subclass inclusion already forces `C_all=infinity`. Therefore

`boxed(C_all = C_gen-sm)`.  (8.1)

This is an exact equality, not an asymptotic comparison.

Consequences:

- A proof of the universal height theorem may assume compactly supported smooth marginals and a generic matrix, with no loss in the final constant.
- A counterexample to existence of any finite universal constant exists in the full class iff no finite universal constant exists on this reduced class.
- Support radii/locations and principal-minor gaps are **not** allowed into the constant; they may diverge or collapse along the approximating sequence.

## 9. Completed partner result applied to the actual inequality

The completed account04/B15 Theorem 6.1, source

`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`,

proves: for every fixed rank-at-least-three target/product instance, any separately established interval inequality

`P{Q in I} <= M |I|`

upgrades to a canonical representative `p_Q in C_0(R)` with the identical pointwise bound `||p_Q||_infinity<=M`.

Every matrix in the owner target has rank at least three. Applying that completed result to the actual transported inequality (7.4) gives, whenever `C_gen-sm<infinity`,

`boxed( p_Q in C_0(R),  ||p_Q||_infinity <= C_gen-sm )`  (9.1)

for **every** rough owner-target instance.

Therefore a proof on the compact-smooth/generic subclass need not separately prove continuity. It only needs the universal interval-height estimate. Account04/B15 then restores the desired continuous representative with zero height loss after Sections 3–8 restore all rough marginals and exact matrix degeneracies.

This application is genuinely target-wide: it does not switch to a diagonal or block-separable subclass.

## 10. Relation to the previous B15 stability theorem

The previous account03/B15 run proved the stronger fixed-matrix quantitative law-stability estimate

`||p_f-p_g||_infinity <= sqrt(2) sum_j K(A,j) ||f_j-g_j||_1^(1/2)`

with a matrix-dependent constant. The present theorem removes that matrix-dependent constant entirely for the purpose of proving the **universal height conjecture**: interval-height bounds pass through total variation/weak closure with zero loss. The previous square-root estimate remains useful when uniform convergence of the actual density representatives is needed, but it is not required merely to reduce the universal height theorem to smooth inputs.

The matrix-genericization step is new in this B15 line and removes exact singular principal blocks from the proof stage as well, again only for estimates whose constant is uniform up to the boundary.

## 11. Absolute continuity and continuity are separate

Independently of the conjectural universal height, every nonzero quadratic form under an absolutely continuous input law is absolutely continuous: the critical set of `q(x)=x^TAx` is `ker A`, a proper linear subspace, hence input-null, and coarea on `R^n\ker A` sends one-dimensional null target sets to zero input mass. This provides no universal height estimate.

The stronger `C_0` conclusion is not a consequence of essential boundedness for arbitrary measures. In the owner target it is supplied, after the interval estimate is paid, by the completed account04/B15 fixed-instance regularity theorem used in Section 9.

## 12. Exact remaining gap

The full universal QFORM theorem remains OPEN. The new result is a closure/reduction theorem, not the missing height estimate.

The remaining task is now cleanly reduced to:

> Prove one dimension-free constant `C` such that `P{x^T A x in I}<=C|I|` for every bounded open interval `I`, assuming only that the independent marginal densities are compactly supported `C_c^infinity`, cap one, and `A` is generic with simple spectrum/all principal minors nonzero and at least three eigenvalues of absolute value at least one; the constant must be independent of support geometry and all principal-minor gaps.

Any such proof automatically yields the full arbitrary-rough, arbitrary-degenerate owner target with the same `C`, and then the partner theorem yields the desired continuous density with that same `C`.

## 13. Source discipline


Partner theorem actually read and applied: account04/B15 r8 at `math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`.

Current correction constraints retained: no pointwise law-uniform quadratic phase decay; no post-rotation independence; no arbitrary-joint coarea height theorem; no dimension-free fiber-sup shortcut; no inference of continuity from boundedness alone.

No numerical histogram, Gaussian/log-concave/moment assumption, compact-support assumption on the original problem, or public release is used.
