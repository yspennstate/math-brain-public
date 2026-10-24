# T357 extension: Gaussian radii, max-margin stability, and arbitrary-time GD delocalization

B03 — 2026-10-24. New extension only; the accepted `fullproof/` files are unchanged.

**Scope.** Sections 1–3 prove the transfer of spherical-feature max-margin results to the original Gaussian-feature model in every strictly positive-margin phase. Sections 4–7 give a separate, quantitative argument for max-margin and **all-time relative GD delocalization** under a robust training-Gram lower bound. The latter condition is guaranteed in an explicitly sufficiently wide proportional regime, but is stronger than strict separability. No exchange of limits is inferred merely from fixed-dimensional implicit-bias convergence.

## 1. Model and the exact literature assumptions used

Let $n/d\to\alpha>0$, $m/d\to\gamma>0$, $X_i\sim N(0,I_d)$ independently, and
\[
\varepsilon_i=2Y_i-1,\qquad
\mathbb P(Y_i=1\mid X_i)=\sigma(\beta\theta^\top X_i),\quad
\|\theta\|_2=1,\quad 0\le\beta<\infty.
\]
Let $W_j\sim N(0,I_d/d)$ independently. Couple them to independent uniform sphere directions by
\[
W_j=R_jU_j,\qquad U_j\sim\mathrm{Unif}(\mathbb S^{d-1}),
\quad R_j=\|W_j\|_2,
\]
where radii and directions are independent. Define the two feature matrices, on the same inputs and labels,
\[
(H_G)_{ij}=\tanh(R_jU_j^\top X_i),\qquad
(H_S)_{ij}=\tanh(U_j^\top X_i).
\]
Write $S=\operatorname{diag}(\varepsilon_1,\ldots,\varepsilon_n)$.

The inspected primary source is Montanari–Ruan–Saeed–Sohn, [*Universality of max-margin classifiers*, arXiv:2310.00176v1](https://arxiv.org/html/2310.00176v1). Its RF rows are **uniform on the sphere**, not Gaussian. Its Assumption 1 holds for tanh: nonlinearity, zero Gaussian mean, bounded first/second derivatives, and zero Gaussian mean of the second derivative. The logistic teacher link is Lipschitz and hence pseudo-Lipschitz. Its Lemma 1 supplies the restricted bound used below; Proposition 5 supplies unit max-margin delocalization. Its positive-margin phase is expressed using the source's $(\gamma_1,\gamma_2)=(\gamma,\alpha)$. B01 separately records the explicit phase/margin formulas. We import these spherical statements only, and prove the Gaussian-radius transfer rather than treating the feature distributions as identical.

## 2. Gaussian-radius perturbation is operator-small

**Lemma 1.** In the above coupling,
\[
\|H_G-H_S\|_{\rm op}=O_P(\sqrt{\log d}),\qquad
\frac{\|H_G-H_S\|_{\rm op}}{\sqrt n}\longrightarrow0.
\tag{2.1}
\]

**Proof.** Put $T_{ij}=U_j^\top X_i$, $e_j=R_j-1$, and
\[
\psi(x)=x\tanh'(x)=x\operatorname{sech}^2x.
\]
The function $\psi$ is odd and has bounded derivative. On the event $\min_jR_j\ge1/2$, Taylor expansion in the radius gives
\[
H_G-H_S=\psi(T)\operatorname{diag}(e)+E,
\qquad |E_{ij}|\le C e_j^2.
\tag{2.2}
\]
The uniform remainder bound is justified by
\[
\sup_{r\ge1/2,x\in\mathbb R}x^2|\tanh''(rx)|<\infty.
\]
The event holds with probability tending to one exponentially fast. Gaussian radial concentration gives
\[
\max_j|e_j|=O_P(\sqrt{\log d/d}),\qquad
\mathbb E e_j^4=O(d^{-2}).
\tag{2.3}
\]
For example $|R-1|\le|R^2-1|$, and the centered fourth moment of $\chi_d^2/d$ is $12/d^2+48/d^3$. Therefore
\[
\|E\|_F^2\le Cn\sum_je_j^4=O_P(1). \tag{2.4}
\]

Let $U$ have rows $U_j^\top$. Since $U=\operatorname{diag}(R)^{-1}F$ for the Gaussian feature matrix $F$, its operator norm is $O_P(1)$. Conditional on $U$, the rows of $\psi(XU^\top)$ are independent and centered. Every unit projection of a row is Gaussian-Lipschitz with constant at most $\|\psi'\|_\infty\|U\|_{\rm op}$. The same sphere-net argument as in the accepted proof gives
\[
\|\psi(XU^\top)\|_{\rm op}=O_P(\sqrt d). \tag{2.5}
\]
Combining (2.2)–(2.5) proves (2.1). Notice that the argument does not use a Frobenius bound for the first-order matrix; such a bound would be too weak. ∎

Both $H_S$ and $H_G$ also have operator norm $O_P(\sqrt n)$ at fixed aspect ratios. Multiplying rows by $S$ changes none of these norms.

## 3. Restricted convexity transfers the margin and its direction

For any $n\times m$ signed feature matrix $A$, define
\[
\kappa_A=\min_{u\in\Delta_n}\|A^\top u\|_2,
\qquad \Delta_n=\{u\ge0:\mathbf1^\top u=1\}.
\tag{3.1}
\]
When $\kappa_A>0$, this is the unit-norm maximum margin, and its unique direction is
\[
\vartheta_A=\frac{A^\top u_A}{\kappa_A},
\tag{3.2}
\]
where $u_A$ is any simplex minimizer. The image $A^\top u_A$ is unique because it is the Euclidean projection of zero onto the convex hull of the signed rows. No uniqueness of the dual vector is assumed.

**Lemma 2 (deterministic perturbation).** Suppose
\[
\|A\|_{\rm op}\le C\sqrt n,\qquad
\|A^\top u\|_2\ge c\sqrt n\|u\|_2-C_0\|u\|_1
\quad\text{for every }u\in\mathbb R^n,
\tag{3.3}
\]
and $B=A+D$, with $\|D\|_{\rm op}\le e\sqrt n$, $e<c/2$. Then constants depending only on $(c,C,C_0)$ satisfy
\[
\|u_A\|_2+\|u_B\|_2\le C_1/\sqrt n,
\qquad |\kappa_A-\kappa_B|\le C_1e.
\tag{3.4}
\]
If in addition $\kappa_A\ge\kappa_0>0$ and $e$ is sufficiently small, then
\[
\|\vartheta_A-\vartheta_B\|_2\le C_2\sqrt e.
\tag{3.5}
\]

**Proof.** The perturbation preserves (3.3) with $c$ replaced by $c-e\ge c/2$ and preserves the upper operator bound with $C$ replaced by $C+e$. The uniform simplex vector $u_0=\mathbf1/n$ gives $\kappa_A\le C$ and $\kappa_B\le C+e$. Apply the respective restricted bound to their minimizing vectors, whose $\ell_1$ norm is one, to get the first bound in (3.4). Testing each minimizer in the other problem gives the second bound.

Put $z_A=A^\top u_A$ and $z_B=B^\top u_B$. Projection onto a closed convex set gives
\[
\|A^\top u_B-z_A\|_2^2
\le\|A^\top u_B\|_2^2-\|z_A\|_2^2.
\]
The right side is at most
$(\kappa_B+\|D\|_{\rm op}\|u_B\|_2)^2-\kappa_A^2=O(e)$.
Also $\|D^\top u_B\|_2\le C_1e$. Hence $\|z_A-z_B\|_2=O(\sqrt e)$. The norm of each vector is at least $\kappa_0/2$ for sufficiently small $e$, so normalizing proves (3.5). ∎

Apply this lemma with $A=SH_S$, $B=SH_G$, using the source's Lemma 1 and Lemma 1 above. In every strict phase in which the spherical margin tends to a positive constant,
\[
\kappa_G-\kappa_S\to0,\qquad
\|\vartheta_G-\vartheta_S\|_2\to0
\quad\text{in probability}. \tag{3.6}
\]
The source's spherical delocalization therefore gives the **original Gaussian-row** conclusion
\[
\|\vartheta_G\|_\infty\le\|\vartheta_S\|_\infty+
\|\vartheta_G-\vartheta_S\|_2\longrightarrow0. \tag{3.7}
\]

The rate from the coupling alone is $O_P((\log d/d)^{1/4})$ for the direction difference. The total delocalization rate also includes the rate, if any, of the imported spherical theorem. These conclusions do not include the zero-margin boundary: normalizing by $\kappa_A$ there is not justified.

This completes the independent radius/RSC audit requested by root. It avoids the invalid inference that normalized operator proximity by itself makes a minimum over training margins continuous; the localized simplex dual is the essential intermediate step.
