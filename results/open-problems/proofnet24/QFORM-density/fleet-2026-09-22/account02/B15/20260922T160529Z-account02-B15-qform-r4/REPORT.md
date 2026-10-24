# account02/B15 — full target-scope C0 regularity and attained-maximum reduction

**Programme:** QFORM-DENSITY-3EIG-20260922, owner revision `2026-09-22.5`  
**Worker:** account02/B15  
**Run:** `20260922T160529Z-account02-B15-qform-r4`  
**Assignment:** Absolute continuity and regularity  
**Method:** complementary constructions and source-valid counterexamples  
**Status:** TARGET-LEVEL REGULARITY THEOREM / FULL UNIVERSAL-CONSTANT QFORM OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Exact target and first unpaid implication

The full live target remains:

> For every dimension n, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric matrix A with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density satisfying `||p_Q||_infinity<=C` for one finite universal constant C independent of n, A and the input laws, or give a valid counterexample.

The first unpaid implication is still the uniform small-ball estimate

`P(X^T A X in I) <= C |I|`

with one matrix- and dimension-independent C. The present run does **not** close that inequality. It proves that all qualitative regularity issues can be removed from that remaining quantitative problem: every individual target instance already has a bounded density in `C_0(R)`, and any failure of the universal constant has witnesses whose density has an **attained pointwise maximum** tending to infinity.

This keeps continuity logically separate from the universal height bound.

## 2. Completed sources actually applied

### Assigned partner account03/B15

I apply the fresh completed assigned-partner report

- repository/commit: `yspennstate/math-open-problems@d73760eb784a86c356c64f05dd92f84655618f02`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260922T153101Z-account03-B15-r12/REPORT.md`.

It proves that if `rank(A)>=3` and at least one original-coordinate diagonal entry is nonzero, then every admissible rough product input gives `X^TAX` a density in `C_0(R)`. Thus its exact remaining rough-input regularity class is `diag(A)=0`.

I use that result as the completed nonzero-diagonal branch and attack the complementary `diag(A)=0` branch below.

### Earlier account02/B15 local theorem

I also use the completed local product-transversality theorem

- repository/commit: `yspennstate/math-open-problems@4b2e6a36bcffeb767998c43d27cee1d8f5eaa07e`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T150242Z-account02-B15-qform-r3/REPORT.md`.

At its exact scope: for `d=3` or `4`, any invertible real symmetric physical-coordinate block B, any affine terms, and independent cap-one coordinate densities, the resulting affine quadratic has a continuous density. The same report retains the earlier height bounds

`||p||_infinity <= C_3/sigma_min(B)`, `C_3=2*pi+3*sqrt(3)` for d=3,

and

`||p||_infinity <= C_4/sigma_min(B)`, `C_4=4*pi+8` for d=4.

That report also uses the previously completed principal-pivot theorem: every real symmetric matrix of rank at least three has an invertible principal physical-coordinate block of order three or four.

### Exact extremal transfer

For the final target reformulation I apply account03/B15

- `yspennstate/math-open-problems@40946450aa2bfb06068a2c688d4407be10470c22`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260922T122718Z-account03-B15-qform-r11/REPORT.md`,

which proves that the sharp interval-density supremum over all admissible marginals equals the supremum over product indicators `1_{E_i}` with `|E_i|=1`, and equally over bounded finite unions of intervals, with no universal bound on the fragment count or separation.

I also keep in view account04/B15 `yspennstate/math-open-problems@07672b7beb8f867c7a7b973aa3157a42ae506460`, which independently proves equality of the full sharp constant with the sharp constant over compactly supported smooth cap-one marginals. It is not used to infer rough-output continuity.

## 3. New local tail lemma: every invertible 3/4-coordinate product quadratic is C0

Let `d in {3,4}`. Let Y have independent cap-one probability densities. Let B be invertible symmetric, `sigma=sigma_min(B)>0`, `Lambda=||B||`, and consider

`T(Y)=Y^T B Y + 2 b^T Y + c`.

Completing the square with `x=Y+B^{-1}b` gives

`T = x^T B x + c_0`,

where `c_0=c-b^T B^{-1}b`. The translated coordinates remain independent and their densities remain bounded by one.

The previous B15 report proves that T has a continuous density p and the finite height bound stated above. It remains only to prove vanishing at infinity.

### Lemma 3.1 — far-field interval bound

For every `R>0`, let `mu_R` be the pushforward of the input measure restricted to `|x|>=R` by `x -> x^T B x`. Then

`M(mu_R) := sup_I mu_R(I)/|I| <= d^(3/2)/(sigma R)`.

**Proof.** On `|x|>=R`,

`|Bx| >= sigma R`.

Hence for every such x at least one original coordinate i obeys

`|(Bx)_i| >= sigma R/sqrt(d)`.

Partition the far region among indices i with this property. For fixed values of all coordinates except `x_i`, the derivative of `q(x)=x^TBx` along the original coordinate line is

`dq/dx_i = 2(Bx)_i`.

On the selected part its magnitude is at least `2 sigma R/sqrt(d)`. This derivative is affine in `x_i`, so the selected line set has at most two monotone components. The inverse image of an output interval I of length h therefore has total `x_i`-length at most

`sqrt(d) h/(sigma R)`.

The cap `f_i<=1` gives the same conditional probability bound. Integrating the other product densities and summing over the d possible selected coordinates yields

`mu_R(I) <= d^(3/2) h/(sigma R)`.

This proves the claim. No moments or support assumptions are used. QED.

### Corollary 3.2 — explicit one-block tail envelope

For the centered variable `q(x)=x^TBx`, the contribution of `|x|<=R` is supported in

`[-Lambda R^2, Lambda R^2]`.

Fix `t!=c_0` and take

`R = sqrt(|t-c_0|/(2 Lambda))`.

The bounded-ball contribution vanishes at t, while Lemma 3.1 bounds the far contribution. Since the canonical density p is continuous, the a.e. inequality extends pointwise. Thus

`p(t) <= d^(3/2) sqrt(2 Lambda)/(sigma sqrt(|t-c_0|))`.

In particular

`p(t) -> 0` as `|t|->infinity`.

Therefore every affine nondegenerate 3- or 4-coordinate product quadratic in the previous local theorem has

`p in C_0(R)`.

The tail bound is deliberately instance-dependent; it is a regularity statement, not the missing universal constant.

## 4. The partner's remaining diag(A)=0 branch is closed

Assume now A is real symmetric, `rank(A)>=3`, and `diag(A)=0` in the original independent coordinates. By the completed symmetric principal-pivot theorem, A has an invertible principal physical-coordinate block B of order d=3 or 4.

Let J be its coordinate set and write the remaining coordinates as W. Conditioning on `W=w`, the polynomial in `Y=X_J` is

`T_w(Y)=Y^T B Y + 2 b(w)^T Y + c(w)`.

The coordinates in J retain their original independence and cap-one densities. By Section 3, for every fixed w the conditional output has a density

`p_w in C_0(R)`

and the previous block theorem gives the uniform-in-w height bound

`0 <= p_w(t) <= H_B := C_d/sigma_min(B)`.

There is no need for a nonzero diagonal pivot in B.

For completeness, choose the continuous representative measurably by the Steklov formula

`p_w(t)=lim_{m->infinity} (m/2) P(T_w(Y) in [t-1/m,t+1/m])`.

Each approximant is jointly measurable in `(w,t)`, and continuity of the conditional density identifies the limit. Hence

`p(t)=integral p_w(t) dP_W(w)`

is a density of `X^TAX`.

If `t_n->t`, then `p_w(t_n)->p_w(t)` for every w and `|p_w(t_n)|<=H_B`; dominated convergence gives continuity of p. If `|t|->infinity`, then `p_w(t)->0` for every fixed w, with the same domination; dominated convergence gives

`p(t)->0`.

Thus

`boxed( diag(A)=0, rank(A)>=3 => p_{X^TAX} in C_0(R) )`.

This is exactly the complementary class left open by the fresh assigned-partner theorem.

## 5. Full target-scope regularity theorem

Combining Section 4 with the assigned partner's nonzero-diagonal theorem yields:

### Theorem 5.1 — target product quadratics have bounded C0 densities instance-by-instance

Let `X_1,...,X_n` be independent with probability densities bounded by one, and let A be any real symmetric matrix with `rank(A)>=3`. Then `Q=X^TAX` has a density

`p_Q in C_0(R)`.

Moreover, if B is any invertible principal physical-coordinate block of order d=3 or 4, then

`||p_Q||_infinity <= C_d/sigma_min(B) < infinity`.

In particular every matrix satisfying the owner hypothesis (at least three eigenvalues with modulus at least one) has a bounded continuous density vanishing at infinity.

This proves the implication ledger at the level of **each fixed target instance**:

`target hypotheses => bounded C0 density => continuous density => absolute continuity`.

The first arrow uses a matrix-dependent constant. It does **not** imply the owner theorem, whose content is the supremum of these heights over all dimensions and admissible matrices.

The theorem also shows that the target's essential boundedness and continuity questions should not be conflated:

- essential boundedness is already true instance-by-instance, but the universal bound is open;
- continuity and vanishing at infinity are now qualitative target-level consequences;
- neither conclusion supplies a dimension-free height constant.

Outside the target class the logical implications fail in the usual ways. For example, the earlier rank-two product example `X_1^2+X_2^2` with uniforms on `[0,1]` has a bounded density with a jump at zero, so bounded density does not imply continuity without the rank-three target structure.

## 6. A concrete zero-diagonal control source

The smallest physical matrix in the partner's previously open class is

`B_triangle = [[0,1,1],[1,0,1],[1,1,0]]`.

Its eigenvalues are `2,-1,-1`, so it already satisfies the three-large-eigenvalue target exactly; `sigma_min(B_triangle)=1`, `||B_triangle||=2`, and every physical diagonal entry is zero.

The theorem above gives every independent cap-one input a density in `C_0`, with the retained local height

`||p||_infinity <= 2*pi+3*sqrt(3) = 11.4793377298...`

and the explicit affine-centered tail estimate

`p(t) <= 6 sqrt(3)/sqrt(|t-c_0|)`

away from the completed-square center. This is not a sharp constant claim; it is a source-valid sanity control that the zero-diagonal closure is genuinely nonempty and includes an indefinite exact-target matrix.

## 7. New attained-maximum reformulation of the full open problem

Let `C_*` be the sharp universal target constant, allowing `C_*=+infinity`:

`C_* = sup ||p_{X^TAX}||_infinity`

over all target-admissible dimensions, matrices and independent cap-one marginals.

The completed account03/B15 extremal-transfer theorem identifies this with the supremum over product indicators `1_{E_i}`, where each `E_i` is a bounded finite union of intervals of total measure one.

By Theorem 5.1, every such extreme output has `p_E in C_0(R)`. For a nonnegative continuous function vanishing at infinity, the supremum is attained. Hence

`boxed( C_* = sup_{n,A,E_1,...,E_n} max_{t in R} p_{A,E}(t) )`,

where A ranges over the exact three-large-eigenvalue target and each `E_i` is a bounded finite union of intervals with `|E_i|=1`.

Consequently, if the universal theorem is false, then there is a **genuine source-valid counterexample sequence** with actual maximizers:

there exist target instances `(A_k,E_{k,1},...,E_{k,n_k})` and real numbers `t_k` such that

`p_k(t_k)=max_t p_k(t) -> infinity`.

Thus no failure can hide solely in an essential-supremum representative issue, a discontinuity, or a nonattained tail spike. Any counterexample must create arbitrarily high **continuous attained peaks** while preserving the full product provenance and three-large-eigenvalue condition.

Combining with account04/B15's smooth-envelope theorem, the same sharp constant is also the supremum over compactly supported smooth cap-one inputs; hence a divergent witness sequence may equally be chosen smooth at arbitrarily small loss in peak height.

## 8. What remains unpaid

The universal theorem is still OPEN. The exact remaining implication is quantitative:

`sup_{target instances} max_t p_Q(t) < infinity`.

The current principal-block certificate pays `1/sigma_min(B)` and therefore can deteriorate on delocalized high-dimensional matrices. The live correction inbox already refutes the simple uniformly-good-principal-block OR rank-three-cross-cut dichotomy, while the newer ridge-window theorem controls a substantial low-leverage spectral branch but does not make its window hypothesis automatic.

So the next bridge must aggregate product-coordinate curvature/banks or combine the ridge-certified low-leverage branch with a source-valid high-leverage mechanism. The present run removes regularity and representative pathologies from that bridge; it does not rename them as a solution.

No FEI mathematics, post-rotation independence assumption, generic conditional density cap, pointwise law-uniform oscillatory decay, bounded fragment count, or raw fiber-supremum shortcut is used.
