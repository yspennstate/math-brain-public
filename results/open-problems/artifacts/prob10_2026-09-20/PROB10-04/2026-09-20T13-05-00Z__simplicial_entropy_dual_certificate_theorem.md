# PROB10-04 — simplicial entropy-dual certificate for the global outer annulus

Status: **proved analytic auxiliary theorem; not a 3-SAT threshold endpoint by itself**.

This note continues the outer variational reduction already established on the PROB10-04 route.  It is written after the run's idea-before-code artifact and before the diagnostic code.

## 1. Setting

Let `P` be the feasible copy-mass set in `R^d` (for the Díaz reduction here `d=3` and `y=(u,v,w)`).  Suppose the exponent has the form

\[
\Phi(y)=K(y)+V(y)+C(y)+c_0,
\]

where `K` is convex on an open convex copy-simplex domain `D`, while the two optimized entropy pieces are finite-support maximum-entropy value functions.  Write their log partitions as

\[
A_V(\theta)=\sum_b m_b\log\sum_{s\in S_b}g_{b,s}e^{\theta\cdot s},
\qquad
A_C(\phi)=\sum_r n_r\log\sum_{t\in T_r}h_{r,t}e^{\phi\cdot t}.
\]

After absorbing terms independent of `y` into constants `c_V,c_C`, convex duality gives

\[
V(y)=\inf_{\theta}\{A_V(\theta)-\theta\cdot y\}+c_V,
\qquad
C(y)=\inf_{\phi}\{A_C(\phi)-\phi\cdot y\}+c_C.
\tag{1.1}
\]

For an interior mean the infima are attained at the Gibbs natural parameters satisfying `nabla A_V(theta)=y` and `nabla A_C(phi)=y`.  The inequalities below do **not** require attainment at the point being bounded.

## 2. The simplicial dual certificate

### Theorem 2.1

Let

\[
Q=\operatorname{conv}\{z_0,\ldots,z_d\}\subset D
\]

be any simplex.  Fix arbitrary finite natural-parameter vectors `theta,phi`.  Define, at its vertices,

\[
U_i=K(z_i)+A_V(\theta)-\theta\cdot z_i
             +A_C(\phi)-\phi\cdot z_i+c_0+c_V+c_C.
\tag{2.1}
\]

Then

\[
\boxed{\sup_{y\in Q\cap P}\Phi(y)\le \max_{0\le i\le d}U_i.}
\tag{2.2}
\]

Thus a whole feasible simplex is excluded below any reference value `Phi_*` as soon as all `d+1` quantities `U_i` are strictly below `Phi_*`.

### Proof

Take `y in Q cap P`, with barycentric coordinates `lambda_i>=0`, `sum_i lambda_i=1`, so that `y=sum_i lambda_i z_i`.  Convexity of `K` gives

\[
K(y)\le\sum_i\lambda_iK(z_i).
\tag{2.3}
\]

From the infimum representations (1.1), for the **fixed** trial parameters `theta,phi`,

\[
V(y)\le A_V(\theta)-\theta\cdot y+c_V,
\qquad
C(y)\le A_C(\phi)-\phi\cdot y+c_C.
\tag{2.4}
\]

The right-hand sides of (2.4) are affine in `y`.  Hence

\[
\begin{aligned}
\Phi(y)
&\le \sum_i\lambda_iK(z_i)
 +A_V(\theta)-\theta\cdot\sum_i\lambda_i z_i+c_V\\
&\qquad
 +A_C(\phi)-\phi\cdot\sum_i\lambda_i z_i+c_C+c_0\\
&=\sum_i\lambda_i U_i
\le \max_i U_i.
\end{aligned}
\]

Taking the supremum over `Q cap P` proves (2.2).  No Hessian sign, inverse covariance, local stationarity, or numerical mesh interpolation is used.  QED.

## 3. Why this is different from a blind grid

A grid merely evaluates `Phi` at points.  Theorem 2.1 bounds **every point of an entire continuum simplex**.  It is also valid where `nabla^2 Phi` is indefinite: convexity is used only for the explicit copy term `K`, while the entropy terms are bounded by globally valid dual affine majorants.

If a simplex is known disjoint from `P`, the existing exact support-function separation oracles discard it.  Otherwise Theorem 2.1 supplies an exponent upper bound without solving the Gibbs inverse map anywhere except, optionally, at the point chosen to generate good trial parameters.

## 4. Center-tangent specialization

Suppose `c` is an interior feasible point and choose `theta_c,phi_c` so that

\[
\nabla A_V(\theta_c)=c=\nabla A_C(\phi_c).
\]

Then the two dual affine majorants in (2.4) are the supporting tangent planes of the concave functions `V,C` at `c`.  In particular they are exact at `c`.  For a simplex near `c`, this is the natural certificate because its overpayment is quadratic rather than linear.

## 5. Quantitative refinement / finite-cover termination theorem

The next result turns the preceding qualitative certificate into a rigorous stopping principle.

### Theorem 5.1

Let `R` be a compact subset of the interior of `D cap P`.  Suppose `K,V,C` are twice continuously differentiable on a convex neighborhood of `R` and there are finite constants

\[
\|\nabla^2K(y)\|_{op}\le M_K,
\qquad
\|-\nabla^2(V+C)(y)\|_{op}\le M_E
\tag{5.1}
\]

throughout that neighborhood.  Let `Q=conv{z_0,...,z_d}` lie there, choose any `c in Q`, and use the Gibbs parameters at `c` in Theorem 2.1.  Then for every `y in Q cap P`, the certificate overpayment obeys

\[
\boxed{
U_Q(y)-\Phi(y)
\le {M_K\over2}\operatorname{diam}(Q)^2
   +{M_E\over2}\|y-c\|_2^2,
}
\tag{5.2}
\]

where `U_Q(y)` denotes the barycentric interpolation of the vertex values (2.1).  Consequently, if a compact region `R` satisfies a strict true gap

\[
\sup_{y\in R}\Phi(y)\le \Phi_*-\eta
\qquad(\eta>0),
\tag{5.3}
\]

then every sufficiently fine finite triangulation of `R` is certified below `Phi_*` by Theorem 2.1.

### Proof

First consider the explicit convex term.  For `y=sum_i lambda_i z_i`, Taylor's theorem around `y` and (5.1) give

\[
K(z_i)\le K(y)+\nabla K(y)\cdot(z_i-y)
          +{M_K\over2}\|z_i-y\|^2.
\]

Multiply by `lambda_i` and sum.  The linear term vanishes because `sum_i lambda_i(z_i-y)=0`.  Hence

\[
\sum_i\lambda_iK(z_i)-K(y)
\le {M_K\over2}\sum_i\lambda_i\|z_i-y\|^2
\le {M_K\over2}\operatorname{diam}(Q)^2.
\tag{5.4}
\]

Let `E=V+C`.  Because the Gibbs parameters at `c` give the supporting tangent plane of `E`, its dual affine majorant is

\[
T_cE(y)=E(c)+\nabla E(c)\cdot(y-c).
\]

By integrating the Hessian along the segment from `c` to `y`,

\[
0\le T_cE(y)-E(y)
\le {M_E\over2}\|y-c\|^2.
\tag{5.5}
\]

Adding (5.4) and (5.5) proves (5.2).

For the final assertion, compactness gives a finite triangulation with maximal diameter `delta`.  Choose, for example, `c` inside each simplex.  Since `||y-c||<=delta`, (5.2) is at most `(M_K+M_E)delta^2/2`.  Taking `delta<sqrt(2 eta/(M_K+M_E))` makes the certificate overpayment smaller than `eta`; combining with (5.3) makes every simplex certificate strictly less than `Phi_*`.  Finiteness of the triangulation gives the claim.  QED.

### Scope of Theorem 5.1

This is a **conditional termination theorem**: it says a strict compact-interior gap can, in principle, be converted into a finite rigorous certificate.  It does not itself prove that the Díaz annulus has the required gap, and near entropy-polytope boundaries the uniform Hessian bound can diverge.  Boundary pieces therefore require direct dual choices / exposed-face treatment rather than invoking (5.1) blindly.

## 6. Segment corollary

For a segment `Q=[z_0,z_1]`, choose any fixed `theta,phi`.  Then

\[
\sup_{y\in[z_0,z_1]\cap P}\Phi(y)
\le\max\{U_0,U_1\}.
\tag{6.1}
\]

This is useful for falsifying the idea that loss of negative definiteness of `nabla^2 Phi` prevents rigorous global exclusion: a segment can remain certified far beyond the first Hessian sign change.

## 7. Integration with the exact support oracles

The earlier PROB10-04 support functions `h_V` and `h_C` imply the following safe branch-and-bound logic for a simplex `Q`:

1. if an exact separating direction proves `Q cap P=empty`, discard `Q`;
2. else evaluate a dual certificate (2.2);
3. if the certificate is below the reference value, discard `Q` as exponent-suboptimal;
4. otherwise subdivide, recenter the Gibbs tangent if useful, and repeat.

Theorem 5.1 proves that this procedure cannot get stuck forever on a compact interior region having a genuine strict gap, provided the dual/Gibbs quantities and the vertex arithmetic are outward certified.

## 8. Precise remaining source-level obligation

To turn this theorem into a new 3-SAT upper endpoint one still must, at some `alpha<4.4898`, outward-certify the source reduction parameters and rescue-adjusted exponent, localize every candidate maximizer, and use support separation plus finitely many certificates of the form (2.2) to cover the entire remaining outer feasible set.  Boundary/truncation/configuration-model transfer errors and independent validation remain separate required obligations.

Accordingly this artifact is **auxiliary theorem progress only**.  The parent source remains OPEN/PARTIAL and no threshold endpoint is changed here.
