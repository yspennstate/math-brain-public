Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 — outer covariance compensation and exact projected support oracles

Status: **analytic auxiliary theorem / source OPEN**.  This file does not change the external threshold bracket `[3.52,4.4898]`.

## 1. Setup inherited from the Díaz first-moment count

Freeze the pure-literal core parameters and the truncation `M`.  The three outer copy masses are

\[
y=(u,v,w)=(\ell_{ps},\ell_{ns1},\ell_{ns2}),
\]

with complementary masses `ell_pu=lambda_p-u` and `ell_nu=lambda_n-v-w`.

For every light signed degree `(i,j)` let `delta_ij=widehat delta_{i,j}` and define the three-coordinate copy-count states

\[
S_{ij}=\{(i,0,0)\}\cup\{(0,k,j-k):1\le k\le j\}.
\tag{1.1}
\]

The first state is a true variable; the state `(0,k,j-k)` is a false variable with `k` blocking and `j-k` nonblocking negative occurrences.  Its base multiplicity is `binom(j,k)`.  Heavy positive occurrences contribute the fixed vector `(h_ps,0,0)`.  Heavy negative occurrences split between the two negative copy types.

For a clause type `alpha=(ps,ns,pu,nu)` with `ps+ns>=1`, define

\[
a(\alpha)=(ps,ns1,ns2),
\]

where `ns1=ns,ns2=0` when `ps+ns=1`, and `ns1=0,ns2=ns` otherwise.  Within fixed syntactic positive count `r=ps+pu`, the source base weight is `2/w(alpha)!`.

The copy contribution to `log F` is

\[
K(u,v,w)=u\log u+(\lambda_p-u)\log(\lambda_p-u)
+v\log v+w\log w+(\lambda_n-v-w)\log(\lambda_n-v-w).
\tag{1.2}
\]

Let `V(y)` and `C(y)` be the maximum variable-side and clause-side entropy contributions subject to producing outer copy mean `y`; constants independent of `y` are suppressed.  Then the fully inner-optimized unrescued outer exponent is

\[
\Phi(y)=K(y)+V(y)+C(y)+\mathrm{const}.
\tag{1.3}
\]

The preceding PROB10-04 run pays the additional rescue aggregates `(Q,B,E)` after `y` is fixed, so understanding (1.3) is the remaining outer problem.

## 2. Variable exponential family

Put `theta=(theta_p,theta_1,theta_2)` and

\[
\nu_{ps}=e^{\theta_p},\qquad
\nu_{ns1}=e^{\theta_1},\qquad
\nu_{ns2}=e^{\theta_2}.
\]

For a light block `(i,j)`,

\[
Z_{ij}(\theta)
=e^{i\theta_p}+\sum_{k=1}^j\binom jk e^{k\theta_1+(j-k)\theta_2}
=\nu_{ps}^i+(\nu_{ns1}+\nu_{ns2})^j-\nu_{ns2}^j.
\tag{2.1}
\]

Define

\[
A_V(\theta)=h_{ps}\theta_p
+h_{ns}\log(e^{\theta_1}+e^{\theta_2})
+\sum_{(i,j)\in L}\delta_{ij}\log Z_{ij}(\theta).
\tag{2.2}
\]

If `Y_ij` has the Gibbs law on (1.1), and `Y_H` is `(0,1,0)` or `(0,0,1)` with probabilities proportional to `e^{theta_1},e^{theta_2}`, then

\[
\nabla A_V(\theta)
=(h_{ps},0,0)+h_{ns}\,\mathbb EY_H
+\sum_{ij}\delta_{ij}\,\mathbb EY_{ij},
\tag{2.3}
\]

and

\[
\boxed{\Sigma_V(\theta):=\nabla^2A_V(\theta)
=h_{ns}\operatorname{Cov}(Y_H)+\sum_{ij}\delta_{ij}\operatorname{Cov}(Y_{ij}).}
\tag{2.4}
\]

## 3. Clause exponential family

Put `phi=(phi_p,phi_1,phi_2)` and `mu_s=e^{phi_s}`.  For fixed syntactic class `r`, define

\[
Z_r^C(\phi)=
\sum_{\alpha:p(\alpha)=r}
\frac{2}{w(\alpha)!}
\exp\{\phi\cdot a(\alpha)\}.
\tag{3.1}
\]

and

\[
A_C(\phi)=\sum_{r=0}^3\widehat\gamma_r\log Z_r^C(\phi).
\tag{3.2}
\]

If `Y_r^C` denotes the corresponding Gibbs copy-count vector in class `r`, then

\[
\nabla A_C(\phi)=\sum_r\widehat\gamma_r\mathbb EY_r^C,
\qquad
\boxed{\Sigma_C(\phi):=\nabla^2A_C(\phi)
=\sum_r\widehat\gamma_r\operatorname{Cov}(Y_r^C).}
\tag{3.3}
\]

These covariance identities are exact derivatives of finite log-sum-exp functions.

## 4. Main theorem: inverse-covariance Hessian of the outer exponent

### Theorem 4.1

Suppose `y` is an interior outer point for which the variable and clause constrained entropy maximizers are unique and their covariance matrices `Sigma_V,Sigma_C` are positive definite.  Let `theta(y),phi(y)` be their natural parameters.  Then

\[
\boxed{\nabla V(y)=-\theta(y),\qquad
\nabla^2V(y)=-\Sigma_V(y)^{-1},}
\tag{4.1}
\]

\[
\boxed{\nabla C(y)=-\phi(y),\qquad
\nabla^2C(y)=-\Sigma_C(y)^{-1}.}
\tag{4.2}
\]

Consequently

\[
\boxed{
\nabla^2\Phi(y)
=H_{copy}(y)-\Sigma_V(y)^{-1}-\Sigma_C(y)^{-1},
}
\tag{4.3}
\]

where

\[
\boxed{
H_{copy}(y)=
\begin{pmatrix}
 u^{-1}+(\lambda_p-u)^{-1}&0&0\\
 0&v^{-1}+(\lambda_n-v-w)^{-1}&(\lambda_n-v-w)^{-1}\\
 0&(\lambda_n-v-w)^{-1}&w^{-1}+(\lambda_n-v-w)^{-1}
\end{pmatrix}.}
\tag{4.4}
\]

#### Proof

For one finite state block with base weights `g_s`, total mass `d`, and state vectors `a_s`, maximizing

\[
-\sum_s x_s\log(x_s/g_s)
\]

under `sum_s x_s=d` and `sum_s x_s a_s=m` gives, by Lagrange multipliers,

\[
x_s=d\frac{g_s e^{\vartheta\cdot a_s}}
{\sum_tg_te^{\vartheta\cdot a_t}}.
\]

The optimized value, after terms independent of `m` are suppressed, is

\[
d\log Z(\vartheta)-\vartheta\cdot m.
\tag{4.5}
\]

Summing the independent variable blocks yields exactly

\[
V(y)=A_V(\theta)-\theta\cdot y+\mathrm{const},
\qquad \nabla A_V(\theta)=y.
\tag{4.6}
\]

Differentiate (4.6).  The terms containing `d theta` cancel because `nabla A_V(theta)=y`, so `dV=-theta\cdot dy`, proving `nabla V=-theta`.  Differentiating the mean relation gives

\[
dy=\nabla^2A_V(\theta)d\theta=\Sigma_Vd\theta.
\]

Positive definiteness makes this locally invertible, hence

\[
d\theta=\Sigma_V^{-1}dy,
\quad
\nabla^2V=-\Sigma_V^{-1}.
\]

The clause proof is identical with `A_C`.  Direct differentiation of (1.2) gives (4.4), and adding the three Hessians gives (4.3).  QED.

### Corollary 4.2 — local strong concavity criterion

If at an interior stationary point `y_*`

\[
\Sigma_V(y_*)^{-1}+\Sigma_C(y_*)^{-1}-H_{copy}(y_*)\succeq\kappa I
\tag{4.7}
\]

for some `kappa>0`, then by continuity there are `r,c>0` such that

\[
\Phi(y)\le\Phi(y_*)-c\|y-y_*\|_2^2
\tag{4.8}
\]

whenever `y` is feasible and `0<||y-y_*||_2<=r`.

If, in addition, the preceding run's entropy-stabilized rescue penalty has positive minimized value at `y_*`, continuity supplies a possibly smaller neighborhood on which the rescued exponent lies uniformly below the unrescued saddle value.  Thus the local outer obstruction reduces to verifying (4.7); the remaining global obligation is separation outside that neighborhood.

Proof: (4.7) and continuity give `nabla^2 Phi <= -(kappa/2)I` on a small ball; integrate the second derivative along the line segment from `y_*` to `y`.  The rescue statement follows from continuity of the compact inner minimum proved in the preceding run. QED.

## 5. Exact projected support oracles

The outer copy vector produced by the variable allocation belongs to the Minkowski sum

\[
\mathcal P_V=(h_{ps},0,0)
+h_{ns}\operatorname{conv}\{(0,1,0),(0,0,1)\}
+\sum_{(i,j)\in L}\delta_{ij}\operatorname{conv}S_{ij}.
\tag{5.1}
\]

Similarly the clause projection belongs to

\[
\mathcal P_C=\sum_{r=0}^3\widehat\gamma_r
\operatorname{conv}\{a(\alpha):p(\alpha)=r\}.
\tag{5.2}
\]

Every feasible source point must therefore lie in `P_V cap P_C` (together with the obvious copy-simplex bounds).

### Theorem 5.1 — variable support oracle

For `xi=(a,b,c)`,

\[
\boxed{
h_V(\xi)=a h_{ps}+h_{ns}\max\{b,c\}
+\sum_{(i,j)\in L}\delta_{ij}
\max\{ai,m_j(b,c)\},}
\tag{5.3}
\]

where the false-state support has the closed form

\[
\boxed{
m_j(b,c)=
\begin{cases}
bj,&b\ge c,\\
b+(j-1)c,&b<c.
\end{cases}}
\tag{5.4}
\]

#### Proof

The support function of a Minkowski sum is the sum of support functions.  The heavy-positive summand contributes `a h_ps`; the heavy-negative segment contributes `h_ns max(b,c)`.  A light block contributes

\[
\delta_{ij}\max\left\{ai,\max_{1\le k\le j}[bk+c(j-k)]\right\}.
\]

The inner expression is affine in `k`; its maximum on the integer interval `[1,j]` is at `k=j` when `b>=c`, and at `k=1` when `b<c`, which is exactly (5.4). QED.

### Theorem 5.2 — clause support oracle

For the same direction,

\[
\boxed{
h_C(\xi)=\sum_{r=0}^3\widehat\gamma_r
\max_{\alpha:p(\alpha)=r}
\{a\,ps(\alpha)+b\,ns1(\alpha)+c\,ns2(\alpha)\}.}
\tag{5.5}
\]

There are only sixteen admissible extended 3-clause types, so each summand is a maximum of finitely many explicit linear forms.

Proof: apply additivity of support functions to (5.2). QED.

Equations (5.3)--(5.5) replace a generic feasibility LP by exact separation oracles.  In particular, a proposed outer box can be cut by any direction `xi` for which the box violates either support inequality `xi dot y <= h_V(xi)` or `xi dot y <= h_C(xi)`.

## 6. Attack on a global KL shortcut: precise obstruction

A tempting stronger claim would be that the variable KL remainder alone globally dominates the convex copy Bregman cost, which would remove the outer optimization without localization.  This cannot hold with coefficient one in general.

Consider one variable block of mass `d0` with only two states, `0` and `D e_1`, whose Gibbs true-state probability is `p`.  Perturb it to `p+epsilon`.  Its state relative entropy is

\[
d_0 D_{KL}(\mathrm{Ber}(p+\epsilon)\|\mathrm{Ber}(p))
=\frac{d_0\epsilon^2}{2p(1-p)}+O(\epsilon^3).
\tag{6.1}
\]

The induced positive-copy mass moves by `D d_0 epsilon`.  Already the `u log u` part of the copy Bregman divergence, with `u=Dd_0p`, contributes

\[
\frac{(Dd_0\epsilon)^2}{2u}+O(\epsilon^3)
=\frac{D d_0\epsilon^2}{2p}+O(\epsilon^3).
\tag{6.2}
\]

The ratio of (6.2) to (6.1) tends to `D(1-p)`, which exceeds one for many high-degree states.  The complementary `(lambda_p-u)log(lambda_p-u)` term only increases the copy curvature.  Thus a blockwise coefficient-one data-processing inequality is false; coherent high-degree copy motion is exactly why the covariance compensation in (4.3), involving both incidence sides, is needed.

This does **not** prove that no more sophisticated global variable-plus-clause inequality exists.  It refutes only the naive one-side/global-KL shortcut attempted in this run.

## 7. Executed diagnostic after the proof

Only after the idea and theorem were written did I evaluate (4.3) numerically at `alpha=4.4898`, `M=23`.  The six stationarity equations were solved in log multipliers starting from the rounded values printed by Díaz et al.  The solve returned residual infinity norm about `1.8e-15` and

\[
\nu\approx(1.278201778245619,0.3327728049379551,0.9533692701180739),
\]
\[
\mu\approx(1.997279589033755,0.4502935808272316,0.3379403003525446).
\]

At the resulting outer point

\[
y\approx(5.856667999143172,0.5364470108663389,1.153411776660164),
\]

the numerical Hessian eigenvalues are

\[
\boxed{-9.1210550455,\ -1.7705366396,\ -0.07447425718.}
\tag{7.1}
\]

The leading principal minors of `-H_out` are approximately

\[
1.432599418,\quad3.351897667,\quad1.202696855,
\]

so the *computed* saddle has a substantial local negative-definiteness margin, about `0.07447` in Euclidean operator norm.  This is a floating-point diagnostic, **not** interval arithmetic and **not** a threshold endpoint certificate.

The matching checker also performed `34,224` exact integer block comparisons for (5.4), all passing, and enumerated the sixteen source clause types.  Code and stdout are in the matching `outer_covariance_hessian_diagnostic` artifacts.

## 8. Exact remaining obligation

The next source-relevant step is no longer an unconstrained three-dimensional search.  It has two precise pieces:

1. **Local certificate:** interval-Newton certify the six stationarity multipliers and interval-bound (4.3) on an explicit outer neighborhood with `-nabla^2 Phi >= kappa I`; combine this with the preceding run's entropy-stabilized rescue penalty.
2. **Global annulus certificate:** use (5.3)--(5.5) as separation oracles to cover the remaining projected feasible set and prove a uniform negative unrescued gap there, preferably by Taylor/Bernstein upper bounds rather than a blind `100^3` mesh.

Only after those are complete should `alpha` be lowered and the full calculation repeated.  Until then the source bracket remains `[3.52,4.4898]`.