# QFORM B15 — exact regularity threshold and a source-valid no-uniform-tail obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet02/B15`  
Run: `20260922T170424Z-fleet02-B15-qform-r5`  
Classification: `SUPPORTING_THEOREM + SOURCE-VALID_COUNTEREXAMPLE / FULL UNIVERSAL HEIGHT OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication

The target is still the dimension- and matrix-independent small-ball/density estimate

`P(X^T A X in I) <= C |I|`

for every independent cap-one product law and every symmetric `A` with at least three eigenvalues of absolute value at least one. The regularity part is not the remaining payment: the completed assigned-partner report `fleet03/B15`, run `20260922T162724Z-fleet03-B15-r13`, canonical source `yspennstate/math-open-problems@4813f09ed4f518a1ee172b77a0f1d315989a84e1`, proves (at worker-result status, with its stated review status) that every fixed symmetric `A` with `rank(A)>=3` gives an individually bounded density in `C_0(R)`. Its constants depend on physical blocks of `A` and therefore do not prove the universal theorem.

This report establishes the exact qualitative threshold around that result and gives a target-valid obstruction to extracting uniform quantitative control merely from the `C_0` conclusion.

## 2. Absolute continuity already starts at rank one

Let `A` be any nonzero real symmetric `n x n` matrix and let `q(x)=x^T A x`. Let `N subset R` have Lebesgue measure zero. The critical set of `q` is

`Crit(q) = {x: A x=0}=ker(A)`,

which has `n`-dimensional Lebesgue measure zero because `rank(A)>=1`.

For every `x notin ker(A)`, choose a coordinate `j` with `(A x)_j !=0`. The map

`F_j(x)=(x_1,...,x_{j-1}, q(x), x_{j+1},...,x_n)`

has Jacobian determinant `2(Ax)_j !=0` at `x`. Hence by the inverse-function theorem it is a `C^1` diffeomorphism on some neighborhood of `x`. On such a neighborhood, `q^{-1}(N)` is carried to a subset of `N x R^{n-1}`, hence has zero `n`-dimensional measure. Second countability gives a countable cover of `R^n\ker(A)` by such neighborhoods. Therefore

`Leb_n(q^{-1}(N))=0`.

Every admissible product law is absolutely continuous with respect to `Leb_n`, so its pushforward under `q` assigns zero mass to `N`. Thus:

> **Lemma 2.1.** For every nonzero symmetric `A` and every admissible independent cap-one product law, `X^T A X` is absolutely continuous.

No boundedness or continuity follows from this argument.

## 3. Rank-one and rank-two controls separate the stronger conclusions

### 3.1 Rank one: absolute continuity without essential boundedness

Take `X~Uniform[0,1]` and `Q=X^2`. Then

`p_Q(t)=1/(2 sqrt(t))`, `0<t<1`,

so `Q` is absolutely continuous but `p_Q notin L^infinity`. This shows that absolute continuity by itself cannot pay the owner's density bound.

### 3.2 Rank two, opposite signs: logarithmic unboundedness

Let `X,Y` be independent `Uniform[-1/2,1/2]` variables and

`Q=X^2-Y^2`.

Set `u=x-y`, `v=x+y`. Then `Q=uv`, `dx dy=(1/2)du dv`, and the transformed square is

`D={(u,v): |u|+|v|<=1}`.

For `0<|t|<1/4`, integrating the delta constraint `uv=t` gives

`p_Q(t)=(1/2) int_{|u|+|t/u|<=1} du/|u|`.

Writing

`r_-(t)=(1-sqrt(1-4|t|))/2`,
`r_+(t)=(1+sqrt(1-4|t|))/2`,

and using the two sign-compatible branches,

`p_Q(t)=log(r_+(t)/r_-(t))`.

Hence `p_Q(t)~log(1/|t|)` as `t->0`, and the density is not essentially bounded.

### 3.3 Rank two, same signs: bounded density can still have no continuous representative

Let `X,Y` be independent `Uniform[0,1]` and `Q=X^2+Y^2`. For `0<t<1`, the sublevel set inside `[0,1]^2` is exactly a quarter disk of radius `sqrt(t)`, so

`P(Q<=t)=pi t/4`,

and therefore

`p_Q(t)=pi/4` for `0<t<1`.

For `t<0`, every density version is zero almost everywhere. Thus no representative can be continuous at zero: continuity would force both the left limit `0` and the right limit `pi/4` to agree. Yet the density is bounded.

So the logical implications are strict below rank three:

`absolute continuity !=> L^infinity`,

and even

`L^infinity !=> existence of a continuous density representative`.

## 4. Exact universal-for-all-rank threshold for qualitative regularity

Apply the completed assigned-partner theorem `fleet03/B15` cited in Section 1: if `rank(A)>=3`, then every admissible product input produces a density `p_Q in C_0(R)` with a finite matrix-dependent `L^infinity` norm.

Combining with Sections 2--3 yields the sharp minimax threshold statement:

> **Theorem 4.1 (regularity threshold).**
> - Rank at least one is sufficient for absolute continuity for every admissible product law, and rank zero is not.
> - Rank at least three is sufficient for an individually bounded `C_0` density for every admissible product law.
> - The threshold three is sharp for these stronger universal-for-all-matrices assertions: at rank two there are admissible opposite-sign examples with unbounded density, and admissible same-sign examples with bounded density but no continuous representative.

Under the owner's hypothesis of three eigenvalues with absolute value at least one, every instance therefore has

`p_Q in C_0(R) cap L^infinity(R)`

instance by instance. The unresolved assertion is solely the uniformity of the `L^infinity` constant across matrices, dimensions and laws.

## 5. New target-valid obstruction: `C_0` does not give a uniform tail envelope

A compactness proof might try to combine target-level continuity/vanishing at infinity with spectral normalization to reduce the universal height problem to a fixed compact output interval. This is false even in a diagonal target family.

Let `T>=17`, let

`A_T=diag(1,1,1,T^{-3})`,

let `X_1,X_2,X_3` be independent `Uniform[0,1]`, and let

`X_4~Uniform[T^2,T^2+1]`,

independent of them. All four input densities are bounded by one, and `A_T` has three eigenvalues exactly equal to one, so this is inside the full owner target.

Put

`S=X_1^2+X_2^2+X_3^2`,
`Y_T=T^{-3} X_4^2`.

For `0<s<1`, the ball of radius `sqrt(s)` lies inside the positive unit cube, hence

`P(S<=s)=pi s^{3/2}/6`,

so

`p_S(s)=pi sqrt(s)/4`.                                           (5.1)

Also

`Y_T in [T, T+delta_T]`,
`delta_T=2/T+1/T^3 <=1/8`                                       (5.2)

for `T>=17`. Evaluate the convolution density of `Q_T=S+Y_T` at

`t_T=T+1/4+delta_T/2`.

For every `y` in the support of `Y_T`,

`t_T-y in [1/4-delta_T/2, 1/4+delta_T/2] subset [3/16,5/16]`.

Using (5.1),

`p_{Q_T}(t_T)=E[p_S(t_T-Y_T)]`
`             >= (pi/4) sqrt(3/16)`
`             = pi sqrt(3)/16`
`             >0.34008`.                                        (5.3)

But `t_T->infinity`. Consequently:

> **Theorem 5.1 (no uniform `C_0` tail modulus).** There is no deterministic function `g(R)->0` such that every target density satisfies `sup_{|t|>=R} p_Q(t)<=g(R)`.

Every individual density in this construction is continuous and vanishes at infinity (indeed the form is diagonal), but the point at which its mass sits can escape to infinity while a fixed positive peak survives. The fourth eigenvalue is deliberately small; arbitrary additional spectral components are allowed by the target.

This is not a counterexample to the universal height conjecture: (5.3) gives a fixed lower bound, not divergent peaks. It does rule out using individual `C_0` regularity as a hidden uniform-tail estimate or as a compact-output reduction.

## 6. Exact implication ledger for proof assembly

The current source-valid ledger is therefore:

1. `A!=0` + admissible product law => absolute continuity. This is qualitative and has no height payment.
2. `rank(A)>=3` + admissible product law => individually bounded `C_0` density, by the completed assigned-partner construction. The bound is matrix dependent.
3. Rank one and rank-two opposite-sign controls prove that neither absolute continuity nor low-rank structure supplies a height bound.
4. Rank-two same-sign control proves that boundedness alone does not force a continuous representative.
5. Even inside the exact three-large-eigenvalue target, `C_0` is not uniform in the tails by Theorem 5.1.
6. Therefore the first unpaid implication remains genuinely quantitative and local-in-height:

`sup_{target instances} sup_t p_Q(t) < infinity`.

Any successful continuation must pay that supremum from product-coordinate curvature/aggregation (for example the current ridge/grouped-coordinate programme), not from absolute continuity, continuity, vanishing at infinity, or a compactness shortcut.

## 7. Source status and nonclaims

Partner premise actually applied: `fleet03/B15`, run `20260922T162724Z-fleet03-B15-r13`, report commit `4813f09ed4f518a1ee172b77a0f1d315989a84e1`. Its source labels the rank>=3 `C_0` theorem a completed worker result with independent review status still to be tracked; I do not manufacture an independent review.

The full QFORM conjecture remains OPEN. No claim is made that Theorem 5.1 obstructs a universal height bound; it only separates pointwise `C_0` regularity from a uniform tail/compactness mechanism.