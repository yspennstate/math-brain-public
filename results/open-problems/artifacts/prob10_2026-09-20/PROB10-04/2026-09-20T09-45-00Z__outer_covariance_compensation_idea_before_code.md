Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 idea before code — replace the outer 3-D grid by covariance compensation and exact support oracles

Status: **research idea, source OPEN**. The external explicit bracket stays `[3.52,4.4898]` until a full source-model endpoint proof is certified.

The preceding run proved that, at each fixed copy macrostate
\[
y=(u,v,w)=(\ell_{ps},\ell_{ns1},\ell_{ns2}),
\]
all rescue-aggregate drift in `(Q,B,E)` can be charged by explicit KL/Pinsker penalties. The remaining obstacle was the outer three-dimensional maximization in `y`. This run changes method rather than adding another rescue motif.

## Main new route: use the Hessian of the optimized entropy blocks

Write the logarithm of the unrescued Díaz exponential objective, after maximizing all variable/clause allocations at fixed `y`, as
\[
\Phi(y)=K(y)+V(y)+C(y)+\text{constant},
\]
where `K` is the copy-partition term, while `V` and `C` are respectively the conditional variable and clause maximum-entropy values. The copy term is
\[
K(u,v,w)=u\log u+(\lambda_p-u)\log(\lambda_p-u)+v\log v+w\log w+(\lambda_n-v-w)\log(\lambda_n-v-w).
\]

If `Sigma_V(y)` and `Sigma_C(y)` are the covariance matrices of `(ps,ns1,ns2)` under the variable-side and clause-side Gibbs exponential families that realize `y`, then at every nonsingular interior point the candidate exact identity is
\[
\boxed{\nabla^2\Phi(y)=H_{copy}(y)-\Sigma_V(y)^{-1}-\Sigma_C(y)^{-1}.}
\]
Here
\[
H_{copy}=\begin{pmatrix}
 u^{-1}+(\lambda_p-u)^{-1}&0&0\\
 0&v^{-1}+(\lambda_n-v-w)^{-1}&(\lambda_n-v-w)^{-1}\\
 0&(\lambda_n-v-w)^{-1}&w^{-1}+(\lambda_n-v-w)^{-1}
\end{pmatrix}.
\]

The exact missing lemma for endpoint movement becomes:

> **Outer localization lemma.** Produce an explicit neighborhood `N` of the relevant source saddle on which `Sigma_V^{-1}+Sigma_C^{-1}-H_copy >= kappa I` for some certified `kappa>0`, and prove a certified negative gap for the unrescued objective on the feasible outer set outside `N`. Then insert the already-proved rescue defect on `N` and re-evaluate at some explicit `alpha<4.4898`.

## Three attacks in this run

1. **Global KL domination.** Try to dominate the convex copy Bregman divergence globally by the variable+clause KL remainders. A likely obstruction is that a high-degree variable state moves many copy coordinates coherently: state KL is paid once while copy curvature can scale with degree. Record the precise failure rather than assume it.

2. **Covariance-compensation Hessian.** Prove the inverse-covariance identity by Legendre duality. Only after the proof is written, evaluate it at the rounded Díaz saddle to test whether there is quantitative room.

3. **Exact outer support oracles.** For `theta=(a,b,c)`, prove the variable-side support formula
\[
h_V(\theta)=a h_{ps}+h_{ns}\max\{b,c\}+\sum_{(i,j)\in L}\widehat\delta_{ij}\max\left\{ai,\max_{1\le k\le j}[bk+c(j-k)]\right\},
\]
and the clause-side support formula
\[
h_C(\theta)=\sum_{r=0}^3\widehat\gamma_r\max_{\alpha:p(\alpha)=r}\{a\,ps(\alpha)+b\,ns1(\alpha)+c\,ns2(\alpha)\}.
\]
These yield exact separating hyperplanes for the feasible outer projection.

No code was written for this run before this idea file.