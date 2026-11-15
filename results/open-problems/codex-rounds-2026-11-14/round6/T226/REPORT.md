VERDICT: PARTIAL an explicit nonzero-target basin and a finite-step-size Gaussian endpoint bound

The round-5 result holds on independent audit. The new result makes its qualitative small-target persistence quantitative on a smaller spectral region. It gives a finite-eta probability estimate, with an explicit power of eta, instead of only a limsup. It does not solve the original edge-of-stability problem or the round-5 full-rectangle endpoint-gap question.

For the fully trainable multi-input two-layer linear model

\[
L_b(a,W)=\tfrac12\|W^Ta-b\|^2,
\quad A=\sqrt\eta\,a,\quad U=\sqrt\eta\,W,
\quad y=\eta b,
\]

write q=||A||^2, C=U^TU, c=lambda_max(C), G=[A U]^T[A U], and take m>=d+1. Fix 0<delta<=1/4. Suppose

\[
q_0+c_0\leq2-4\delta,\qquad c_0\leq1-2\delta,
\qquad D=\det G_0>0.
\]

Set M=d+2 and chi=exp[-4/(delta(2-delta))]. PROOF.md proves that

\[
\boxed{\quad\eta\|b\|\leq\frac{\delta^2\chi D}{8M^d}\quad}
\]

implies geometric convergence to a full-column-rank global minimizer with

\[
\eta\lambda_{\max}(\nabla^2L_b(a_\infty,W_\infty))
\leq2-7\delta/2.
\]

The residual contracts from the first step by 1-kappa, where kappa=delta chi D/M^d. The proof controls the cumulative target error 2||y|| sum ||r_t||, retains the exact nonzero-target determinant factor (1-||r_t||^2)^2, and closes a simultaneous contraction/determinant bootstrap. It does not shadow an unknown number of zero-target steps.

This region contains the earlier full-rank m=16,d=8 example with initial scaled Hessian Rayleigh quotient 121/50>2. Thus initial sharpness below 2/eta is not required. The theorem does not establish nonmonotone loss or edge residence.

For independent scaled Gaussian entries N(0,tau^2), equivalently original entries N(0,tau^2/eta), the Gram determinant has explicit negative moments. Gram-Schmidt gives a product of independent chi-square variables with degrees m,m-1,...,m-d. Consequently, if F_eta is failure of the convergence and endpoint guarantee above and B_delta is the stated spectral region, then for every 0<p<(m-d)/2,

\[
\mathbb P(F_\eta\cap\mathcal B_\delta)
\leq\mathcal M_p(K_\delta\eta\|b\|)^p,
\]

where

\[
K_\delta=8M^d/(\delta^2\chi),\qquad
\mathcal M_p=(2\tau^2)^{-(d+1)p}
\prod_{j=1}^{d+1}
\frac{\Gamma((m-j+1)/2-p)}{\Gamma((m-j+1)/2)}.
\]

Adding P(B_delta complement) gives an unconditional bound. A sphere-net and chi-square calculation in PROOF.md bounds that complement explicitly.

For m=16,d=8,tau^2=1/288,delta=1/16,p=3, exact rational Taylor enclosures certify

\[
\mathbb P(F_\eta)
\leq\min\{1,\ 9.568\times10^{-25}
+1.127\times10^{120}(\eta\|b\|)^3\}.
\]

In particular, for every fixed target b,

\[
\boxed{\quad\eta\|b\|\leq10^{-48}
\quad\Longrightarrow\quad\mathbb P(F_\eta)<2.1\times10^{-24}.\quad}
\]

The same probability bound excludes convergence to an endpoint in any window |eta lambda_max-2|<=w<7/32. The coefficient is large and the sufficient step-size range is very small. This is a finite-eta guarantee, not an estimate of the observed transition scale. The earlier asymptotic small-probability estimates have smaller constants; this result supplies explicit eta dependence for nonzero targets.

Verification command, run here:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_quantitative.py > verification.final.stdout.txt 2> verification.final.stderr.txt
```

Exit 0. Elapsed 2.044715 seconds, effective nice 20, peak RSS 18,202,624 bytes, one process and thread, standard library only. CPU and wall caps were 100 and 150 seconds. The nice utility printed a permission warning; the script verified the already-lower process priority before arithmetic.

Forty exact rational cases verify the perturbed q,C,residual and determinant recurrences, parameter-step norm, Gram-Schmidt volume, and the earlier Krylov identity. A closed-form projector check agrees with its derivative to 1.34e-12. The earlier exceptional endpoint constants 256/81 and 1011719/457600 are recovered. Exact symmetric differences independently recover the 121/50 initial Hessian quotient. A full-rank boundary example at delta=1/4 reaches a nonzero target in one step while q and C both increase; it checks the need for the perturbation terms.

Fourteen 120-digit finite trajectories test targets at one half and at the full proved threshold, with exact rational certificates of their initial spectral margins. All reach residual at most 1e-28 times the nonzero target. The smallest tested target is 1.1013e-42 and the largest update count is 998. These probes test the formulas and implementation; the infinite-time claim follows from the proof.

One auxiliary verification failed: after the rational probability bounds passed, a diagnostic demanded agreement to 1e-70 although the Taylor enclosures had relative widths about 1e-69. The diagnostic now checks containment in the exact intervals; the failed output is retained. No proved inequality failed. All final checks pass.

The literature check closed within five minutes. No opened source settled the requested random-entry theorem; no SOLVED_ELSEWHERE.md was created. Sources actually opened:

- Eric Gan, *A Bifurcation Theory Framework for Gradient Descent on the Edge of Stability*, [arXiv:2606.15551](https://arxiv.org/html/2606.15551v1): Theorem 4.4 assumes a neighborhood of a specified minimum.
- Elon Litman, *The Origin of Edge of Stability*, [arXiv:2604.20446](https://arxiv.org/html/2604.20446v1): conditional trajectory-curvature results, not this random-entry/endpoint theorem.
- Jaerin Lee and Kyoung Mu Lee, *A Journey to the Edge of Stability*, [arXiv:2609.32290](https://arxiv.org/abs/2609.32290): empirical learning-rate and optimizer regimes.
- Geonhui Yoo, Minhak Song and Chulhee Yun, *Understanding Sharpness Dynamics in NN Training with a Minimalist Example: The Effects of Dataset Difficulty, Depth, Stochasticity, and More*, [ICML 2025](https://proceedings.mlr.press/v267/yoo25b.html): a deep linear model with one neuron per layer.
- Rustem Islamov, Michael Crawshaw, Jeremy Cohen and Robert M. Gower, *Non-Euclidean Gradient Descent Operates at the Edge of Stability*, [ICML 2026](https://proceedings.mlr.press/v306/islamov26a.html): generalized sharpness diagnostics and experiments.

This was a bounded search, not an exhaustive openness or novelty claim.

What remains uncertain: the full rectangle's quantitative zero-target endpoint-gap law is still unknown here; the explicit target threshold is conservative; c0<1 is essential to this contraction argument but is not asserted necessary for convergence; nonlinear activations and sustained edge residence remain untreated. No novelty claim is made against the complete matrix-factorization literature.

Next checkable step: remove c0<1 from the quantitative small-target theorem. Start on a compact subset q0+c0<=2-delta with det G0>=D_min>0. The earlier zero-target argument gives summable residual squares and eventual contraction; obtain an explicit uniform time to a contracting region, then an explicit target threshold. This would cover starts with c0>=1. The more difficult separate goal remains a near-critical endpoint-gap rate on the whole round-5 rectangle.

Artifacts: PROOF.md, LOG.md, verify_quantitative.py, verification.json, and first, failed-audited and final stdout/stderr files. All writes remained in this folder. Earlier folders were read only.

Task: “Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta” — received 15 November 2026, approximately 11:27 Asia/Tbilisi.
