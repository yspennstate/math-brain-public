# T336: unconditional GP-prior averaged ERM for Gaussian predictive outputs

This addendum removes bounded-context conditioning from **the sampling and risk** in the finite-class result of `agents/a24.md`. Bounded context labels appear only as a high-probability region on which a constructive predictor is known to approximate the GP posterior. It does not assert a uniform-in-context error guarantee or an optimizer convergence theorem.

## GP setup and the unconditional theorem

For each task let \(1\leq n\leq N\), with fixed query count \(m\geq1\), exogenously selected context/query inputs in the bounded design domain, and a zero-mean GP kernel with \(0\leq k(x,x)\leq k_{\rm diag}\) at every admissible input. Noisy context and query observations have independent \(\mathcal N(0,s)\) noise, \(s>0\). Draw *independent GP tasks* \(D_t=(n_t,X_{c,t},Y_{c,t},X_{q,t})\) from this **unconditioned** GP prior and design distribution, then draw \(Y_t\) from its true posterior predictive law

\[
p_D=\mathcal N(\mu_0(D),\Sigma_0(D)),\qquad
sI_m\preceq\Sigma_0(D)\preceq V_0I_m,\qquad
V_0:=s+mk_{\rm diag}.
\]

Equivalently, each pair \((D_t,Y_t)\) is a jointly sampled GP task with independent noises. The design locations may be random, but must be exogenous to the GP values for the centered Gaussian marginal and posterior-mean moment calculations below. Write \(Y\) for the query-label vector under the unconditioned law and \(V_Y=s+mk_{\rm diag}\) (equal to the displayed admissible \(V_0\)). Conditional on all input locations, *before observing context labels*, \(Y\sim\mathcal N(0,K_{qq}+sI_m)\), with

\[
\|K_{qq}+sI_m\|_{\rm op}\leq V_Y.
\]

Crucially, the candidate prediction may depend arbitrarily on the correlated \(Y_c\); the proof below uses a pathwise loss envelope in \(Y\), not conditional independence between predictor and query labels.

Let a finite, pre-data hypothesis class \(\mathcal F\), cardinality \(J\), output \(q_f(\cdot\mid D)=\mathcal N(\mu_f(D),\Sigma_f(D))\) for *every* context, with global bounds

\[
\|\mu_f(D)\|_2\leq M,\qquad (s/2)I_m\preceq\Sigma_f(D)\preceq VI_m,\qquad V\geq s/2.
\]

Let \(\ell_f=-\log q_f(Y\mid D)\), \(R(f)=\mathbb E\ell_f\), and

\[
\mathcal K(f)=\mathbb E_D\operatorname{KL}(p_D\|q_f(\cdot\mid D)).
\]

The expectation is over the **unconditioned GP prior**, and \(R(f)=\mathbb E_D H(p_D)+\mathcal K(f)\). Define

\[
d_M=\frac m2\log\frac{2V}{s}+\frac{2M^2}{s},\qquad
\Lambda=4\left(d_M+\frac{2mV_Y}{s}\right),\qquad
u=\log\frac{2J}{\delta}.
\]

For the empirical NLL minimizer \(\hat f\in\arg\min_{f\in\mathcal F}T^{-1}\sum_{t=1}^T\ell_f(D_t,Y_t)\), with probability at least \(1-\delta\),

\[
\boxed{\quad
\mathcal K(\hat f)-\inf_{f\in\mathcal F}\mathcal K(f)
\leq 8\sqrt2\,\Lambda\sqrt{\frac uT}
+4\Lambda\frac uT .
\quad} \tag{U1}
\]

For an empirical \(\eta\)-minimizer, add \(\eta\). In particular the class can be a \(P\)-parameter quantized transformer grid with parameters in \([-W,W]\) and grid spacing \(\delta_w\leq W\), \(|\mathcal F|\leq(4W/\delta_w)^P\), in which case \(u\leq P\log(4W/\delta_w)+\log(2/\delta)\). No bound on the *true conditional mean* \(\mu_0(D)\) is used in (U1).

### Proof of unconditional concentration

The NLL is unbounded because \(Y\) is Gaussian. But its candidate-independent lower constant and a pointwise upper envelope are

\[
c_{\rm low}=\frac m2\log(2\pi)+\frac m2\log(s/2),\qquad
0\leq Z_f:=\ell_f-c_{\rm low}
\leq\frac m2\log\frac{2V}{s}+\frac{(\|Y\|_2+M)^2}{s}
\leq d_M+\frac2s\|Y\|_2^2 . \tag{U2}
\]

For \(0\leq t<(2V_Y)^{-1}\), Gaussian diagonalization conditional on the input locations gives

\[
\mathbb E\!\left[e^{t\|Y\|_2^2}\mid X_c,X_q\right]
=\det(I-2t(K_{qq}+sI_m))^{-1/2}
\leq(1-2tV_Y)^{-m/2}. \tag{U3}
\]

The bound holds even when \(n\) is random. At \(t=2/(s\Lambda)\), note \(tV_Y\leq1/(4m)\) and \(d_M/\Lambda\leq1/4\). Bernoulli's inequality gives \((1-1/(2m))^{-m/2}\leq\sqrt2\), so (U2)–(U3) imply

\[
\mathbb E e^{Z_f/\Lambda}
\leq e^{1/4}(1-1/(2m))^{-m/2}
\leq e^{1/4}\sqrt2<2. \tag{U4}
\]

The estimate is uniform in \(f\). For every integer \(p\geq1\), \( \mathbb E Z_f^p\leq2p!\Lambda^p\). Writing \(X_f=Z_f-\mathbb E Z_f=\ell_f-\mathbb E\ell_f\), Jensen and \(|a-b|^p\leq2^{p-1}(|a|^p+|b|^p)\) yield \(\mathbb E|X_f|^p\leq2^{p+1}p!\Lambda^p\). Since \(\mathbb E X_f=0\), for \(|\lambda|<(2\Lambda)^{-1}\),

\[
\log\mathbb E e^{\lambda X_f}
\leq\sum_{p=2}^{\infty}2^{p+1}(|\lambda|\Lambda)^p
=\frac{8\lambda^2\Lambda^2}{1-2|\lambda|\Lambda}. \tag{U5}
\]

This is a two-sided sub-gamma MGF with variance proxy \(16\Lambda^2\) and scale \(2\Lambda\). Bernstein and the union bound give, with probability \(1-\delta\), simultaneously for all \(f\in\mathcal F\),

\[
|\widehat R_T(f)-R(f)|
\leq4\sqrt2\,\Lambda\sqrt{u/T}+2\Lambda u/T.
\]

Comparing the empirical minimizer to the population minimizer and canceling the common \(\mathbb E_D H(p_D)\) proves (U1). This argument does **not** condition the \(T\) training tasks on bounded context labels.

## Transfer an approximant from bounded contexts

Let \(E_B=\{\max_{i\leq n}|Y_{c,i}|\leq B\}\) (empty maximum interpreted as zero if \(n=0\)). For a fixed \(B\), suppose \(f_B\in\mathcal F_B\) has the global output bounds above and the constructive bounded-context guarantee

\[
\sup_{D\text{ admissible}:\,E_B}\operatorname{KL}(p_D\|q_{f_B}(\cdot\mid D))
\leq\varepsilon_{\rm app}(B). \tag{U6}
\]

One way to extend a bounded-input constructive predictor globally is to clip each context label to \([-B,B]\) **before** applying its encoder/solver and enforce the global mean and covariance output bounds by construction or clipping. It agrees with the bounded-context predictor on \(E_B\). The chosen grid member must satisfy (U6) *after parameter quantization*; a continuous approximant alone is not sufficient.

The GP context-label marginal and a union bound yield

\[
p_B:=\Pr(E_B^c)
\leq \rho_B:=\min\!\left\{1,\,2N
\exp\!\left[-\frac{B^2}{2(k_{\rm diag}+s)}\right]\right\}. \tag{U7}
\]

The unconditioned posterior mean has a useful fourth moment. Conditional on exogenous input locations,

\[
\mu_0=K_{qc}(K_{cc}+sI_n)^{-1}Y_c
\sim\mathcal N(0,S),\qquad
S=K_{qc}(K_{cc}+sI_n)^{-1}K_{cq}
\preceq K_{qq}.
\]

Since \(\operatorname{tr}S\leq\operatorname{tr}K_{qq}\leq mk_{\rm diag}\),

\[
\mathbb E\|\mu_0\|_2^4
=\mathbb E_X\{(\operatorname{tr}S)^2+2\operatorname{tr}(S^2)\}
\leq3m^2 k_{\rm diag}^2. \tag{U8}
\]

For any candidate with the global output bounds, the exact Gaussian forward-KL formula gives a pointwise upper bound, with \(\log^+x=\max(0,\log x)\),

\[
\operatorname{KL}(p_D\|q_f)
\leq C_{M,V}+\frac2s\|\mu_0(D)\|_2^2,\qquad
C_{M,V}:=\frac{mV_0}{s}+\frac m2\log^+\frac Vs+\frac{2M^2}{s}. \tag{U9}
\]

Indeed, \(\operatorname{tr}(\Sigma_f^{-1}\Sigma_0)/2\leq mV_0/s\), the mean quadratic term is at most \((\|\mu_0\|+M)^2/s\leq2(\|\mu_0\|^2+M^2)/s\), and the remaining \(-m+\log\det\Sigma_f-\log\det\Sigma_0\) is bounded above using \(\Sigma_0\succeq sI\). Cauchy–Schwarz, (U7)–(U9), and (U6) give

\[
\boxed{\quad
\mathcal K(f_B)
\leq \varepsilon_{\rm app}(B)
+C_{M,V}\rho_B
+\frac{2\sqrt3\,m k_{\rm diag}}{s}\sqrt{\rho_B}.
\quad} \tag{U10}
\]

Combine (U1) and (U10) for an unconditional, high-probability pretraining guarantee:

\[
\boxed{\quad
\mathcal K(\hat f_B)
\leq\varepsilon_{\rm app}(B)
+C_{M,V}\rho_B
+\frac{2\sqrt3\,m k_{\rm diag}}s\sqrt{\rho_B}
+8\sqrt2\,\Lambda\sqrt{\frac{\log(2|\mathcal F_B|/\delta)}T}
+4\Lambda\frac{\log(2|\mathcal F_B|/\delta)}T .
\quad} \tag{U11}
\]

This is expected forward KL under the *original, unconditioned GP prior*.

### Link to the explicit encoder grid

The feature-encoder construction of `agents/a28.md` and the fixed one-sided solver core yield a particularly concrete class once only encoder parameters are gridded. Clip input context labels to \([-B,B]\); clip **each** grid encoder output coordinate to \([-2,2]\). With \(p\) feature coordinates, all grid-feature Gram matrices are PSD and \(\|\phi_f(x)\|_2\leq2\sqrt p\). The common solver interval is then \([s,s+4Np]\), so every grid member (including poorly rounded ones) has covariance

\[
sI_m\preceq\Sigma_f(D)\preceq(s+4pm)I_m
\]

and predictive mean norm at most \(4pN\sqrt m\,B/s\), globally in the original context values. These bounds follow from \(0\preceq P_L(A_f)\preceq A_f^{-1}\), \(\|H_f\|_{\rm op}\leq4p\sqrt{Nm}\), \(\|P_L(A_f)\|_{\rm op}\leq1/s\), and \(\|\operatorname{clip}_B(Y_c)\|\leq\sqrt N B\). Thus (U11) applies with

\[
M_B=4pN\sqrt m\,B/s,\qquad V_B=s+4pm.
\]

The separate encoder-grid approximation calculation must provide an actual grid member satisfying (U6). The unnormalized signed-head attention core/solver is fixed and need not be quantized; an ordinary normalized or softmax attention layer is not substituted for that exact matvec realization.

## Consistency and necessary growth conditions

For a sequence of classes indexed by \(j\), (U11) tends to zero if \(\varepsilon_{{\rm app},j}\to0\), \(\rho_{B_j}^{1/2}\to0\), \(C_{M_j,V_j}\rho_{B_j}\to0\), and

\[
\Lambda_j\sqrt{\frac{\log(2J_j/\delta_j)}{T_j}}\to0,\qquad
\Lambda_j\frac{\log(2J_j/\delta_j)}{T_j}\to0 .
\]

For example, grow \(B_j\), choose bounded-context feature/solver accuracy and grid resolution for \(\varepsilon_{{\rm app},j}\downarrow0\), then choose \(T_j\) large enough for the displayed concentration terms. The explicit feature grid has \(M_j=4p_jN\sqrt m B_j/s\); its tail vanishes whenever \(p_j^2 B_j^2\rho_{B_j}\to0\). A concrete diagonal choice for the fixed-dimensional RBF construction of `research/T336_ENCODER_GRID.md` is \(B_j=j\), \(\varepsilon_{{\rm app},j}=1/j\), and \(\delta_j=j^{-2}\), \(j\geq2\). Its displayed choice \(C_*=O(B_j^2+1)\), \(h_j=\min(1,\sqrt{\varepsilon_{{\rm app},j}/C_*})\), \(k_j=O(\log j)\) gives \(p_j=\binom{d+k_j}{k_j}=O((\log j)^d)\). Thus \(M_j=O(j(\log j)^d)\) and \(C_{M_j,V_j}\rho_{B_j}\to0\). After its finite encoder grid is fixed, let \(u_j=\log(2J_j/\delta_j)\) and choose, for instance, \(T_j\geq j^2\Lambda_j^2u_j\) rounded up. Then the concentration terms vanish; since \(\sum_j\delta_j<\infty\), Borel–Cantelli also gives almost-sure convergence of the expected-KL risk of this sequence of exact ERMs.

**A fixed global mean cap \(M\) generally rules out KL consistency.** For any fixed task and candidate mean \(\mu_f\), minimizing the forward KL over *all* positive-definite candidate covariances gives \(\Sigma_f=\Sigma_0+aa^\top\), \(a=\mu_0-\mu_f\), and minimum \(\tfrac12\log(1+a^\top\Sigma_0^{-1}a)\). Thus every globally capped predictor, regardless of its covariance choice, obeys

\[
\mathcal K(f)\geq\frac12\mathbb E_D\log\!\left[
1+\frac{(\|\mu_0(D)\|_2-M)_+^2}{V_0}
\right]. \tag{U12}
\]

If the GP posterior mean has unbounded support (for example, its conditional covariance \(S\) is nonzero on a positive-probability set of designs), the right side is strictly positive for fixed \(M\). Therefore \(M=M_j\) must be allowed to increase for the consistency conclusion. The price is that \(\Lambda_j=O(M_j^2/s+mV_Y/s+m\log(2V_j/s))\) grows too, and \(T_j\) must compensate. The result asserts statistical ERM performance; it does not assert that training dynamics find the empirical minimizer.
