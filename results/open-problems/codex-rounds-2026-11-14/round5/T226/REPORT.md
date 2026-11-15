VERDICT: PARTIAL almost-sure strictly subcritical endpoints in the larger zero-target rectangle

The round-4 result holds on independent audit. The new result answers its named endpoint question: Gaussian initialization in that rectangle has probability zero of a limiting output eigenvalue at or above 2. Equality is excluded as well as strict instability. This remains a special-case obstruction for the fully trainable multi-input two-layer linear model; it does not solve the general edge-of-stability problem.

For

\[
L_0(a,W)=\tfrac12\|W^Ta\|^2,\quad
A=\sqrt\eta\,a,\quad U=\sqrt\eta\,W,\quad
q=\|A\|^2,\quad C=U^TU,
\]

take $m\geq d+1$. For almost every initial point in

\[
\mathcal R=\{q_0<2,\ \lambda_{\max}(C_0)<2\},
\]

the parameters converge to a full-column-rank global minimizer, with an eventual geometric rate, and

\[
0<\lambda_{\min}(C_\infty+q_\infty I)
\leq\eta\lambda_{\max}(\nabla^2L_0(a_\infty,W_\infty))
=q_\infty+\lambda_{\max}(C_\infty)<2.
\]

“Almost every” is with respect to Lebesgue measure, so this applies to any jointly absolutely continuous initialization law. In particular it applies conditionally on $\mathcal R$ to independent original entries $N(0,\tau^2/\eta)$, for every fixed $\tau>0$ and every $\eta>0$. The rectangle permits $q_0+\lambda_{\max}(C_0)$ arbitrarily close to 4, residual squares above 1, and nonmonotone loss. There is no uniform endpoint gap or convergence rate.

The proof gives a deterministic algebraic obstruction. Set $v_t=U_t^TA_t$ and

\[
D_t=\det[v_t,C_tv_t,\ldots,C_t^{d-1}v_t].
\]

For every start in $\mathcal R$,

\[
q_\infty+\lambda_{\max}(C_\infty)\geq2
\quad\Longrightarrow\quad D_T=0
\text{ at some finite time }T.
\]

Each $D_T$ is a nonzero polynomial of the initial parameters. Thus the exceptional event lies in a countable union of polynomial zero sets. This does not assume that the GD map is a diffeomorphism.

The new ingredient is a multiplicative bound for residual weight in a top spectral cluster. For $B(s)=B-s\alpha vv^T$, if that cluster remains separated from the remaining spectrum by $\delta>0$, its projector satisfies

\[
\|P(1)v\|\geq e^{-\alpha\|v\|^2/\delta}\|P(0)v\|.
\]

This follows by differentiating $v^TP(s)v$, including when eigenvalues inside the cluster are repeated. In the GD recurrence, if the limiting sharpness were at least 2, every subsequent residual multiplier in the top limiting cluster would have magnitude at least $1-\|v_t\|^2$. The earlier summability of $\|v_t\|^2$ makes the product of these lower bounds positive. Residual convergence therefore forces that cluster to be exactly invisible at a finite time. The identity

\[
D_{t+1}=\det((1-q_t)(1-\|v_t\|^2)I-C_{t+1})D_t
\]

establishes the polynomial assertion. PROOF.md writes out the projector lemma, critical-equality argument, exceptional sets, convergence rate, and probability consequences.

The earlier small-nonzero-target argument now applies to almost every point of the entire rectangle. For each fixed target $b$ and each such scaled initialization, sufficiently small $\eta$ gives convergence with a fixed relative endpoint gap below 2. Consequently, for any shrinking relative endpoint window $w(\eta)\to0$,

\[
\limsup_{\eta\downarrow0}\mathbb P\{
\text{convergence to a global minimum with }
|\eta\lambda_{\max}-2|\leq w(\eta)\}
\leq\mathbb P\{q_0\geq2\text{ or }\lambda_{\max}(C_0)\geq2\}.
\]

This improves the region in round 3's probability bound. It supplies no finite-$\eta$ rate for nonzero targets. Any additional edge-residence requirement can only shrink the event.

An exact counterexample checks the need for the algebraic exception. With $A_0=e_1$, $U_{0,1}=(e_1+e_2)/4$, $U_{0,2}=(6/5)e_3$, and small independent orthogonal other columns, the residual remains nonzero at every finite step, yet the endpoint has scaled sharpness at least

\[
\frac{14111}{18304}+\frac{36}{25}
=\frac{1011719}{457600}>2.
\]

The spectator direction is invisible to the residual, so $D_0=0$. Thus supercritical exceptional endpoints are not limited to finite-time exact landings. The construction has full augmented rank and embeds in $m=16,d=8$. The round-4 one-step endpoint $256/81$ is also independently verified.

Verification command, run in this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_endpoint.py > verification.audited.stdout.txt 2> verification.audited.stderr.txt
```

Exit 0. Elapsed 1.5901 seconds, effective nice 20, peak RSS 17,661,952 bytes; one process/thread, standard library only, 60-second CPU cap and 90-second wall alarm. The nice utility emitted a permission warning; the process independently verified its already-lower priority before arithmetic.

Thirty-two exact rational cases verify the Gram, residual and new Krylov identities, and both round-4 correction identities. Independent elimination checks the Vandermonde witnesses. Thirty-four projector cases include internal multiplicities, a closed-form 2D comparison, and independent finite differences of the projector derivative; the largest derivative discrepancy is $2.84\times10^{-12}$. Exact coordinates independently recover the spectator constants, and a lifted full-Hessian eigenvector checks $256/81$.

Forty generic finite trajectories all reached residual below $10^{-13}$ with output sharpness below 2; 33 started outside the old sum basin, 14 had loss increases, and 11 had residual square above 1. The largest update count was 2611. These finite probes check the implementation; the infinite-time and probability claims follow from the proof.

The first run failed an auxiliary diagnostic: it reduced a repeated-top-eigenvalue example to two dimensions although its bottom eigenspace had two distinct eigenvalues. That reduction was invalid. It is now used only when both diagonal blocks are scalar, and the distinct-bottom-spectrum case is retained with a direct projector-derivative check. The failed output is preserved. No proved identity failed.

The literature check closed within five minutes. No opened source settled the requested random-entry problem, so no SOLVED_ELSEWHERE.md was created. This was a bounded search, not an exhaustive openness or novelty claim. Sources actually opened:

- Elon Litman, *The Origin of Edge of Stability*, [arXiv:2604.20446](https://arxiv.org/html/2604.20446v1): Theorems 4.1–4.3 give conditional weighted-curvature conclusions, not the network random-entry and endpoint theorem requested here.
- Eric Gan, *A Bifurcation Theory Framework for Gradient Descent on the Edge of Stability*, [arXiv:2606.15551](https://arxiv.org/html/2606.15551v1): Theorem 4.4 assumes initialization in a neighborhood of a specified minimum.
- Eric Regis and Sinho Chewi, *Rod Flow: A Continuous-Time Model for Gradient Descent at the Edge of Stability*, [arXiv:2602.01480](https://arxiv.org/abs/2602.01480): its abstract gives an ODE approximation and quartic-potential self-stabilization results.

What remains uncertain: the complementary initialization region is unclassified, no quantitative law for the endpoint gap is proved, and there is no result for nonlinear activation functions or sustained edge residence. No novelty claim is made against the complete matrix-factorization literature.

Next checkable step: obtain an explicit bound on $\mathbb P\{0<2-S_\infty\leq\varepsilon\mid\mathcal R\}$ under a specified Gaussian law, even with initial margins $q_0,\lambda_{\max}(C_0)\leq2-\delta$. The present result proves only that this probability tends to zero. A rate would turn the qualitative endpoint exclusion into a finite-window estimate.

Artifacts: PROOF.md, LOG.md, verify_endpoint.py, verification.json, and both runs' stdout/stderr files. All writes remained inside this folder; earlier folders were read only.

Task: “Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta” — received 15 November 2026, approximately 08:46 Asia/Tbilisi.
