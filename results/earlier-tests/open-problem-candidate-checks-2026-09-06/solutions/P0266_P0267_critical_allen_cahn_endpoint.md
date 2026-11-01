# P0266 and P0267: critical Allen-Cahn endpoint counterexamples

Scope: counterexamples to two numbered questions in a 2025 survey. The literature search behind them is incomplete; see analyses/.

## Source and exact target

Agresti and Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, NoDEA (2025), Problems 4 and 5, journal page 130 of 150, PDF page 131 (the repository adds a cover page). Primary published PDF: https://repository.tudelft.nl/file/File_783e6459-5d3b-4957-bcd3-64da5b8d9025 . Archived SHA256: a66ffa2c1d88f2b46d563a3e4d3963bbc0f8623492e7e1837b4ae089008ad091. The arXiv version https://arxiv.org/abs/2501.18561 has the questions on PDF page 92. The published page was rendered and visually read in this campaign.

Problem 4 asks for an expected squared maximal-energy bound in the setting of Theorem 6.4. Its explicit model is the Ito equation on the one-dimensional torus

$$du=(\Delta u+u-u^3)\,dt+\gamma u^2\,dW,$$

with one scalar Brownian driver, and it singles out $\gamma^2=2$ as unresolved. Problem 5 asks whether convergence of initial conditions in $L^2(\Omega;H)$ implies convergence of solutions in $L^2(\Omega;L^2(0,T;V)\cap C([0,T];H))$ under the same general assumptions. These are distinct bounds and continuity questions, not parameter copies. Both fail for the same critical equation.

## Scalar reduction and global construction

Normalize the torus volume to one and take the deterministic constant initial condition $u_0(x)=a>0$. A spatially constant solution is $u(t,x)=U_t$, where

$$dU_t=(U_t-U_t^3)\,dt+\sqrt2 U_t^2\,dW_t,\qquad U_0=a.$$

Set $s(t)=(e^{2t}-1)/2$. Let $R_s$ be a four-dimensional Bessel process, starting at $r=1/(\sqrt2 a)$ and satisfying

$$dR_s=dB_s+\frac{3}{2R_s}\,ds.$$

It is the radial part of four-dimensional Brownian motion started at a point of length $r$ and never hits zero. Define

$$U_t=\frac{e^t}{\sqrt2 R_{s(t)}}.$$

Ito's formula for $z(R)=1/(\sqrt2 R)$ gives drift $-z^3$ and diffusion $-\sqrt2 z^2$. Deterministic time change followed by multiplication by $e^t$ yields drift $U-U^3$ and diffusion $-\sqrt2 U^2$; replace the scalar Brownian driver by its negative. This proves the displayed SDE. Positivity and nonexplosion follow from the Bessel construction: a continuous positive Bessel path has a positive minimum on each compact time interval. Local Lipschitz coefficients give pathwise uniqueness; therefore this construction gives the law of the unique global strong solution for any prescribed scalar Brownian driver.

## A finite-time Bessel minimum lemma

For $0<b<r$, define $\tau_b=\inf\{s\ge0:R_s=b\}$. Fix $S>0$. The function $h(x)=|x|^{-2}$ is harmonic away from zero in dimension four. Its stopped process at $\tau_b$ is bounded by $b^{-2}$. Optional stopping at $\tau_b\wedge S$ gives the exact identity

$$\frac{\mathbb P_r(\tau_b\le S)}{b^2}=\frac1{r^2}-\mathbb E_r[R_S^{-2};\tau_b>S].$$

Since the process never hits zero, $\mathbf1_{\{\tau_b>S\}}\to1$ almost surely as $b\downarrow0$. The required integrability and strict loss of harmonic expectation can be computed directly. If $x\in\mathbb R^4$ has length $r$ and $B_S^{(4)}\sim N(0,SI_4)$, then Tonelli's theorem and a Gaussian integral give

$$\begin{aligned}
\mathbb E_r[R_S^{-2}]&=\int_0^\infty(1+2S\lambda)^{-2}\exp\!\left(-\frac{\lambda r^2}{1+2S\lambda}\right)d\lambda\\
&=\frac1{2S}\int_0^1\exp\!\left(-\frac{r^2(1-v)}{2S}\right)dv\\
&=\frac{1-e^{-r^2/(2S)}}{r^2}.
\end{aligned}$$

Dominated convergence in the stopped identity therefore proves

$$\lim_{b\downarrow0}\frac{\mathbb P_r(\tau_b\le S)}{b^2}=\frac{e^{-r^2/(2S)}}{r^2}>0.$$

No infinite-horizon hitting probability has been substituted for a finite-horizon one. The strict positive constant is explicitly derived for every $S>0$.

## Failure of Problem 4

Let $M_S=\sup_{0\le s\le S}(2R_s^2)^{-1}$. Substituting $b=(2x)^{-1/2}$ in the preceding lemma shows

$$\lim_{x\to\infty}x\,\mathbb P_r(M_S\ge x)=\frac{e^{-r^2/(2S)}}{2r^2}>0.$$

Thus $\mathbb E M_S=\infty$ by integration of the tail. For $S=s(T)$, the scalar construction gives

$$\sup_{0\le t\le T}U_t^2\ \ge\ M_{s(T)},\qquad \mathbb E\sup_{0\le t\le T}U_t^2=\infty\quad(T>0).$$

Consequently, $\mathbb E\sup_{t\le T}\|u(t)\|_{L^2(\mathbb T)}^2=\infty$, although $u_0$ is a smooth bounded deterministic function. The proposed bound fails for each positive finite time, not merely asymptotically.

At each fixed positive time, by contrast,

$$\mathbb E U_t^2=e^{2t}a^2\left(1-\exp\!\left[-\frac1{4a^2s(t)}\right]\right)<\infty.$$

This is consistent with the existing theorem's pointwise second-moment bound. The rare finite-time maxima have a $1/x$ tail for squared amplitude; replacing a localized stochastic integral by a mean-zero integrable martingale would miss exactly this issue.

## Verification of the abstract assumptions

There is already a finite-dimensional counterexample: choose the Gelfand triple $V=H=V^*=\mathbb R$, $A=I$, $B=0$, $F(v)=2v-v^3$, and $G(v)=\sqrt2 v^2$. Then the evolution equation $du+Au\,dt=F(u)\,dt+G(u)\,dW$ is the scalar SDE above. The linear coercivity condition holds with $\theta=1,M=0$. The nonlinear condition is

$$v(Av-F(v))-\tfrac12|G(v)|^2=-v^2\ge |v|^2-2|v|^2-2,$$

so Theorem 6.4's coercivity holds with $\theta'=1,M'=2$. Polynomial local Lipschitz bounds satisfy Assumption 6.1 with $\rho=2$, $\beta=2/3$, since $(2\beta-1)(\rho+1)=1$. All interpolation norms on this one-dimensional triple are equivalent. No compactness or infinite-dimensionality is required in the source assumptions.

For the stated torus model, take $V=H^1(\mathbb T)$, $H=L^2(\mathbb T)$, $A=I-\Delta$, $B=0$, $F(v)=2v-v^3$, and the same one-dimensional noise. Then

$$\langle v,Av-F(v)\rangle-\tfrac12\|G(v)\|_{L^2}^2=\|\nabla v\|_2^2-\|v\|_2^2=\|v\|_{H^1}^2-2\|v\|_2^2.$$

The polynomial Lipschitz condition follows from $(H^{-1},H^1)_{2/3,1}\hookrightarrow H^{1/3}\hookrightarrow L^6$ in one dimension, using Holder for the cubic drift and the resulting $L^4$ embedding for the quadratic diffusion. Thus the same critical indices $\rho=2$, $\beta=2/3$ suffice. The unique solution from Theorem 6.4 agrees with the spatially constant strong solution above.

## Failure of Problem 5

Use a common scalar Brownian driver and initial conditions $u_0^{(n)}(x)=1/n$, with limiting initial condition $u_0=0$. The solutions exist strongly and can be constructed simultaneously for this countable family. Their initial conditions converge deterministically in $L^2$. The limiting solution is identically zero, since both drift and diffusion vanish at zero. For every $n$ and every $T>0$, the preceding calculation applied with $a=1/n$ gives

$$\mathbb E\|u^{(n)}-0\|_{C([0,T];H)}^2=\infty.$$

Therefore convergence in the claimed $L^2(\Omega;L^2(0,T;V)\cap C([0,T];H))$ space cannot hold under the general hypotheses. This does not contradict convergence in probability or the stated $L^p$ convergence for $p<2$. In particular, tiny tail coefficients for small initial conditions do not make an infinite second maximal moment finite.

## Adversarial checks and remaining review

The argument's load-bearing checks are the Ito rather than Stratonovich convention; the scalar spatially constant driver allowed by the published model; the factor $\sqrt2$ and Bessel dimension four; the finite-horizon stopping identity; and the distinction between a fixed-time moment and the expected supremum. All are explicit above. The zero initial condition alone is not a counterexample, and $\gamma^2<2$ is outside this construction's critical claim.

A first later-literature search found the 2026 paper *Fractal dimension of singular times for SPDEs: Energy bounds, criticality, and weak-strong uniqueness*, arXiv:2602.21981. Its abstract concerns singular-time dimensions and does not resolve these two endpoint questions. Its full text was not read. The Bessel and Gaussian facts themselves are classical; what is new here, if anything, is their application to the two precisely sourced questions.
