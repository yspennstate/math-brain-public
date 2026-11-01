# PROB10-04 supplement — continuity of finite-support maximum entropy on the closed mean polytope

Status: **proved auxiliary lemma**. This supplies the boundary-continuity hypothesis used in the finite tangent-bank theorem; it is not a 3-SAT threshold endpoint.

## Lemma

Let `S={s_1,...,s_N}` be a finite subset of `R^d`, let `w_i>0`, and put

\[
P=\operatorname{conv}(S).
\]

For `y in P`, define

\[
I(y)=\min\left\{\sum_{i=1}^N p_i\log{p_i\over w_i}:
 p\in\Delta_N,\ \sum_i p_i s_i=y\right\},
\tag{1}
\]

with `0 log 0:=0`. Then `I` is finite and continuous on the whole compact polytope `P`, in the relative topology of `aff(P)`. Consequently the maximum-entropy value `E(y)=-I(y)` (up to an additive normalization constant) is continuous on `P`, including every boundary face.

The same conclusion holds for a finite positive weighted sum of such blocks after a linear mean projection, because the product probability simplex is again compact and the objective is continuous convex.

## Proof

Write `A:p -> sum_i p_i s_i` for the linear mean map on the simplex `Delta_N`, and

\[
f(p)=\sum_i p_i\log(p_i/w_i).
\]

Because `x log x` extends continuously to `0` with value `0`, `f` is continuous on the compact simplex. Every fiber

\[
F_y=\{p\in\Delta_N:Ap=y\}
\]

is nonempty and compact for `y in P=A(Delta_N)`. Hence the minimum in (1) is attained and finite.

### 1. Convexity

Take `y_0,y_1 in P`, let `p_0,p_1` be minimizers, and let `0<=t<=1`. Then

\[
p_t=(1-t)p_0+t p_1
\]

is feasible for `y_t=(1-t)y_0+t y_1`. Since `f` is convex,

\[
I(y_t)\le f(p_t)
\le (1-t)f(p_0)+t f(p_1)
=(1-t)I(y_0)+t I(y_1).
\]

Thus `I` is convex on `P`.

### 2. Lower semicontinuity

Let `y_n -> y` in `P`. Choose a subsequence, still denoted `y_n`, along which `I(y_n)` tends to the liminf, and choose minimizers `p_n in F_{y_n}`. Compactness of `Delta_N` gives a further subsequence `p_n -> p`. Continuity of the mean map gives `Ap=y`, while continuity of `f` gives

\[
\liminf_n I(y_n)=\lim_n f(p_n)=f(p)\ge I(y).
\]

Hence `I` is lower semicontinuous.

### 3. Upper semicontinuity at an arbitrary boundary or interior point

Fix `y in P`. A finite polytope admits a triangulation in which any prescribed point `y` is a vertex: start with any triangulation and perform stellar subdivisions of the simplices/faces containing `y`. Let `T_1,...,T_m` be the finitely many simplices of this triangulation that contain `y`.

Every simplex of the triangulation not containing `y` has positive distance from `y`. Therefore, for all points `x in P` sufficiently close to `y`, `x` belongs to one of the `T_j` containing `y`.

Write such a simplex as

\[
T_j=\operatorname{conv}\{y,v_{j1},...,v_{jr_j}\}.
\]

For `x in T_j`, let

\[
x=\lambda_0(x)y+\sum_{k=1}^{r_j}\lambda_k(x)v_{jk},
\qquad \lambda_k(x)\ge0,\quad\sum_k\lambda_k(x)=1.
\]

The barycentric coordinates are continuous on the simplex, and as `x->y` within `T_j`, `lambda_0(x)->1` and every `lambda_k(x)->0` for `k>=1`. Convexity of `I` gives

\[
I(x)\le \lambda_0(x)I(y)+\sum_{k=1}^{r_j}\lambda_k(x)I(v_{jk}).
\]

There are only finitely many incident simplices and vertices, so the values `I(v_{jk})` are bounded by one finite constant. Hence uniformly over all incident simplices,

\[
\limsup_{x\to y} I(x)\le I(y).
\]

Together with lower semicontinuity, this proves continuity at `y`. Since `y` was arbitrary, `I` is continuous on all of `P`.

Finally, replacing `I` by `-I` plus any constant proves continuity of the maximum-entropy value. For finitely many weighted blocks with a common linear projected mean, take the product of their compact simplexes and the weighted sum of their continuous convex relative-entropies; the identical argument applies to that compact convex feasible set and its linear image. QED.

## Consequence for the PROB10-04 tangent-bank theorem

The variable-side and clause-side Díaz entropy optimizations are finite-support weighted maximum-entropy programs after the `M=23` truncation used by this lane. Their closed projected mean polytopes therefore satisfy the continuity hypothesis of Theorem 5.1 in

`2026-09-20T14-02-00Z__finite_tangent_arrangement_and_KL_cover_theorem.md`.

Thus the boundary-uniform finite tangent-bank approximation is not merely an interior statement: it applies to the closed finite-support projected feasible region, with no uniform inverse-covariance or Hessian bound.