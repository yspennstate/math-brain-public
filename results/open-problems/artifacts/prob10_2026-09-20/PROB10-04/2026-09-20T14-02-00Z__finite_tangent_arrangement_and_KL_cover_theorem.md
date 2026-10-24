# PROB10-04 — finite entropy-tangent arrangements and a boundary-uniform KL cover

Status: **proved analytic auxiliary theorem; not a random-3-SAT threshold endpoint by itself**.

This note follows the idea-before-code artifact

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T13-47-00Z__tangent_bank_arrangement_three_routes_idea.md`.

It strengthens the preceding one-tangent simplicial certificate in two ways: a finite tangent bank can be treated exactly by a hyperplane arrangement while keeping the convex copy term exact, and the tangent bank can approximate the entropy value uniformly even at mean-polytope boundaries without any Hessian bound.

## 1. Abstract setting

Let `R` be a compact polytope in an affine space of dimension `r`. Let

\[
\Phi(y)=K(y)+E(y)+c_0,
\]

where `K:R->R` is continuous and convex and `E:R->R` is continuous and admits an affine-majorant representation

\[
E(y)=\inf_{\eta\in\mathcal H}L_\eta(y),
\qquad L_\eta(y)=a_\eta+b_\eta\cdot y.
\tag{1.1}
\]

For the Díaz reduction, `r=3`, `K` is the explicit copy term (with `0 log 0:=0` on the closed copy simplex), and `E=V+C` is the sum of two finite-support maximum-entropy value functions.

Fix a finite bank `eta_1,...,eta_J` and abbreviate

\[
L_j=L_{\eta_j},\qquad
\overline E_J(y)=\min_{1\le j\le J}L_j(y).
\tag{1.2}
\]

Then `E<=overline E_J` pointwise.

## 2. Route A: mixture-of-tangents minmax certificate

### Theorem 2.1

Let `Vert(R)` be the vertices of `R`. Then

\[
\boxed{
\sup_{y\in R}\Phi(y)
\le c_0+
\inf_{p\in\Delta_J}
\max_{v\in\operatorname{Vert}(R)}
\left[K(v)+\sum_{j=1}^Jp_jL_j(v)\right].
}
\tag{2.1}
\]

Here `Delta_J={p_j>=0, sum_j p_j=1}`.

### Proof

For every `p in Delta_J`,

\[
E(y)\le \min_jL_j(y)\le\sum_jp_jL_j(y).
\]

Hence

\[
\Phi(y)\le K(y)+\sum_jp_jL_j(y)+c_0.
\]

The right side is a continuous convex function of `y`. A continuous convex function on a compact polytope attains a maximum at an extreme point: if a maximizer is not extreme, express it as a nontrivial convex combination and use convexity to move to one endpoint without decreasing the value; iterate inside the finite-dimensional face lattice. Therefore

\[
\sup_R\Phi
\le c_0+\max_{v\in Vert(R)}
[K(v)+\sum_jp_jL_j(v)].
\]

Taking the infimum over `p` proves (2.1). QED.

This certificate is cheap but can be loose because `min_j L_j` has been replaced by one global convex combination.

## 3. Route B: exact lower-envelope arrangement certificate

For each tangent `j`, define its lower-envelope cell

\[
C_j=R\cap\bigcap_{k=1}^J\{y:L_j(y)\le L_k(y)\}.
\tag{3.1}
\]

Some `C_j` may be empty or lower-dimensional.

### Theorem 3.1 — exact finite arrangement reduction

For every finite tangent bank,

\[
\boxed{
\sup_{y\in R}\bigl[K(y)+\overline E_J(y)\bigr]
=
\max_{1\le j\le J}\ 
\max_{x\in\operatorname{Ext}(C_j)}
\bigl[K(x)+L_j(x)\bigr],
}
\tag{3.2}
\]

where an empty cell contributes `-infinity`. Consequently

\[
\boxed{
\sup_{y\in R}\Phi(y)
\le c_0+
\max_j\max_{x\in Ext(C_j)}[K(x)+L_j(x)].
}
\tag{3.3}
\]

### Proof

The cells cover `R`: at every `y`, at least one finite `L_j(y)` realizes the minimum in (1.2). On `C_j`,

\[
\overline E_J(y)=L_j(y),
\]

so the finite-bank surrogate is `K+L_j`, a continuous convex function. Since `C_j` is a compact polytope in its affine hull, the same extreme-point argument as in Theorem 2.1 gives

\[
\max_{y\in C_j}[K(y)+L_j(y)]
=
\max_{x\in Ext(C_j)}[K(x)+L_j(x)].
\]

Taking the maximum over the finitely many cells yields (3.2). Since `E<=overline E_J`, (3.3) follows. QED.

### Corollary 3.2 — finite candidate generation

Suppose `R` is described in its `r`-dimensional affine hull by finitely many facet inequalities. Every extreme point of `C_j` is obtained by imposing `r` linearly independent active hyperplanes chosen among

1. facet hyperplanes of `R`, and
2. tangent-equality hyperplanes `L_j=L_k`, `k!=j`,

then checking all remaining inequalities. Thus a brute-force exact checker has a finite candidate list. In the Díaz case `r=3`, each candidate is obtained from three active hyperplanes.

### Proof

`C_j` is itself a polytope cut out by the listed finite inequalities. At an extreme point of an `r`-dimensional polytope (or after restricting to the affine hull of a lower-dimensional cell), the active normals span the affine-hull dual space. Select a basis of `r` independent active equations; their unique intersection is the point. QED.

### Comparison with Theorem 2.1

For every `p in Delta_J`, `overline E_J<=sum_jp_jL_j`, so the exact arrangement bound (3.2) is never worse than the corresponding mixture surrogate. It can be strictly better because it allows the active tangent to change with `y` while keeping `K(y)` exact.

## 4. Route C: exact Bregman/KL meaning of entropy-tangent error

Consider first one finite-support log partition

\[
A(\theta)=\log\sum_{s\in S}w_s e^{\theta\cdot s},\qquad w_s>0.
\tag{4.1}
\]

At an interior mean `y=nabla A(theta_y)`, define the concave entropy value

\[
E_A(y)=A(\theta_y)-\theta_y\cdot y.
\tag{4.2}
\]

For another finite parameter `theta_c`, its affine dual majorant is

\[
L_{\theta_c}(y)=A(\theta_c)-\theta_c\cdot y.
\tag{4.3}
\]

### Theorem 4.1 — exact tangent error

\[
\boxed{
L_{\theta_c}(y)-E_A(y)
=D_A(\theta_c,\theta_y)
=\operatorname{KL}(P_{\theta_y}\|P_{\theta_c})\ge0,
}
\tag{4.4}
\]

where

\[
D_A(\alpha,\beta)
=A(\alpha)-A(\beta)-\nabla A(\beta)\cdot(\alpha-\beta)
\]

and `P_theta(s)=w_s exp(theta*s-A(theta))`.

### Proof

Using `nabla A(theta_y)=y`,

\[
\begin{aligned}
L_{\theta_c}(y)-E_A(y)
&=A(\theta_c)-A(\theta_y)
 +(\theta_y-\theta_c)\cdot y\\
&=A(\theta_c)-A(\theta_y)
 -\nabla A(\theta_y)\cdot(\theta_c-\theta_y)\\
&=D_A(\theta_c,\theta_y).
\end{aligned}
\]

Also

\[
\begin{aligned}
KL(P_{\theta_y}\|P_{\theta_c})
&=\sum_sP_{\theta_y}(s)
[(\theta_y-\theta_c)\cdot s-A(\theta_y)+A(\theta_c)]\\
&=(\theta_y-\theta_c)\cdot y-A(\theta_y)+A(\theta_c),
\end{aligned}
\]

which is the same expression. QED.

If `A` is a positive weighted sum of independent finite-block log partitions, (4.4) sums with the same block weights. Therefore in the PROB10-04 decomposition `E=V+C`, an attained tangent-bank error is exactly a sum of variable-side and clause-side block KL divergences. The natural cells `C_j` are therefore KL/Voronoi-type cells for the dual entropy geometry, even though their boundaries are affine because the dual tangents themselves are affine in mean space.

## 5. Boundary-uniform finite tangent bank

The previous run's finite-cover theorem used a uniform entropy Hessian bound and therefore excluded entropy-polytope boundaries. No such differential hypothesis is needed for a finite tangent bank.

### Theorem 5.1 — uniform finite-bank approximation, including boundary points

Assume only that `R` is compact, `E` is continuous on `R`, and (1.1) holds with finite affine functions `L_eta`. Then for every `epsilon>0` there exist finitely many parameters `eta_1,...,eta_J` such that

\[
\boxed{
0\le \min_{1\le j\le J}L_{\eta_j}(y)-E(y)<\epsilon
\quad\text{for every }y\in R.
}
\tag{5.1}
\]

No attainment of the infimum in (1.1), differentiability, Hessian bound, or interior assumption is required.

### Proof

Fix `y in R`. Since `E(y)=inf_eta L_eta(y)`, choose a finite parameter `eta(y)` with

\[
L_{\eta(y)}(y)<E(y)+\epsilon/3.
\]

The function

\[
g_y(x)=L_{\eta(y)}(x)-E(x)
\]

is continuous because `L_eta` is affine and `E` is continuous. Hence there is an open neighborhood `U_y` of `y` in `R` on which `g_y(x)<epsilon`. The collection `{U_y:y in R}` covers the compact set `R`, so choose a finite subcover `U_{y_1},...,U_{y_J}` and retain the corresponding parameters.

For any `x in R`, select `j` with `x in U_{y_j}`. Then

\[
\min_iL_{\eta(y_i)}(x)
\le L_{\eta(y_j)}(x)
<E(x)+\epsilon.
\]

The lower bound in (5.1) is immediate from the infimum representation (1.1). QED.

### Application to finite-support maximum entropy

For a finite support with positive base weights, the primal entropy value is the maximum of the continuous function

\[
-\sum_sp_s\log(p_s/w_s),\qquad 0\log0:=0,
\]

on the compact probability simplex subject to a linear mean constraint. Its value is finite and continuous on the finite-dimensional mean polytope (equivalently, it is the closed finite concave entropy conjugate of the log partition). Weighted finite products/Minkowski sums preserve this property. Thus Theorem 5.1 applies to the Díaz variable- and clause-side entropy values all the way to their projected-polytope boundaries.

## 6. Finite certificate existence without Hessians or geometric triangulation

### Corollary 6.1

Let `R` be a compact polytope and suppose the true exponent has a strict gap

\[
\sup_{y\in R}\Phi(y)\le \Phi_*-\eta,
\qquad \eta>0.
\tag{6.1}
\]

Under the hypotheses above, there exists a finite tangent bank for which the exact arrangement certificate (3.3) is strictly below `Phi_*` on all of `R`.

### Proof

Apply Theorem 5.1 with `epsilon=eta/2`. Then

\[
K(y)+\overline E_J(y)+c_0
\le \Phi(y)+\eta/2
\le \Phi_*-\eta/2
\]

for every `y in R`. Taking the supremum and applying Theorem 3.1 yields a finite arrangement-vertex certificate with strict margin. QED.

This removes the previous conceptual boundary obstruction: **if** a compact Díaz region truly has a strict exponent gap, some finite entropy-tangent arrangement certifies it, including boundary pieces, without any global negative-Hessian theorem and without triangulating the region into tiny simplices.

## 7. What this does and does not prove for random 3-SAT

The theorem changes the remaining proof architecture but does not by itself move the 3-SAT threshold endpoint. To improve the external `4.4898` upper endpoint through the Díaz/rescue lane one still needs, at some `alpha<4.4898`, all of the following:

1. an outward-certified source reduction and rescue-adjusted exponent;
2. a finite bank of outward-certified entropy dual parameters;
3. an exact description/separation of the relevant projected feasible region;
4. exact or outward-certified enumeration of the arrangement candidates in Theorem 3.1;
5. strict negativity of every candidate relative to the reference exponent;
6. configuration-model/proper-clause transfer and all truncation errors;
7. independent validation under repository policy.

The new point is that **boundary entropy and global Hessian sign are no longer separate theoretical blockers**. The remaining obstacle is now finite source-specific certification of the full three-dimensional outer region at an improved density.