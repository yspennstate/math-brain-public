VERDICT: PROVED a sharper equal-mass flat-grid subdivision bound O(n^(-1/60) log(en)^(11/10))

The earlier spectral result holds. An independent Dirichlet-beta Laurent expansion, checked numerically both by contour differentiation and a Gamma-function identity, gives h_Q approximately 0.004022236572742278. Its difference from the earlier H_5 is positive and below that formula's proved truncation bound. The earlier script also reran successfully. No update beyond the already cited preprint was found in the five-minute literature check.

New beyond round 3: [PROOF.md](PROOF.md) proves, for equal empirical masses on the unit square or flat torus, at t=n^(-5/6),

\[
\left|d_n^\Omega(t)-\mathbb E d_K^Q(m^2t)\right|
\le Cn^{-1/60}\log(en)^{11/10},
\qquad K\sim\operatorname{Bin}(n,m^{-2}),\quad m\in\{1,2,3\},
\]

where d_n^Omega(t)=n E W_{2,Omega}^2(P_t^Omega nu_n,nu_n) and d_0=0. A stronger bound for the expected absolute difference of the random global and cellwise costs is proved as well. This improves the equal-mass O(n^(-1/120) log n) estimate in Lemma 4.1 of Yunzong Xu, *Random Matching Between Distinct Distributions in Two Dimensions*, [arXiv:2610.40509v1](https://arxiv.org/html/2610.40509v1#S4.SS1). It refines that repair method; no claim of a new method is made.

The improvement comes from delta^2=A log(en)/(nt) and collar width r=(delta^2)^(1/5). The proof derives the rough expected cost directly, reconstructs the optimal-potential estimate, preserves each cell's mass during repair, and controls the replacement of global heat by cellwise heat. It uses basic quadratic transport facts, Gaussian heat kernels, iid covariance, and Bernstein concentration, without assuming a matching asymptotic theorem. The case m=1 includes the torus seam and hence the square–torus comparison.

Reproduction commands, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_zeta.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_scaling.py
```

Both exited 0. The numerical script took about 3.3 seconds and less than 20 MB peak RSS; the exact rational exponent check took below 0.1 seconds and less than 14 MB. The priority wrapper printed a warning, but both scripts checked actual niceness 20 before computation. All calculations used one thread, no GPU, and explicit CPU limits. [LOG.md](LOG.md) contains complete relevant output and the earlier-script command.

Attempts to break the argument checked the interpolation singularity at its atomic endpoint, covariance before event restriction, empty cells, small n, grid intersections, discontinuous cellwise densities, the m=1 seam, and exact conditional rescaling. All load-bearing exponents were obtained a second way. No mathematical counterexample was found. A draft Gamma-expression factor was corrected algebraically before execution; two small patch-context failures were corrected. A shortcut to t=n^(-2/3) was rejected because the global heat comparison would no longer decay by a power of n.

Limits and uncertainty: this proves subdivision, not the complete second-order matching theorem. The semidiscrete-to-smoothing reduction remains unaudited here, as do the curved-surface extensions. The numerical h_Q comparison is not interval arithmetic. No value of beta_sd or c_square is asserted. The cited preprint still states existence with c_square=beta_sd+h_Q, as the earlier reports recorded.

Next worker: audit the equal-mass semidiscrete-to-smoothing reduction in Proposition 3.1 and its Appendix B proof, especially the quantitative linearization error. The flat-grid repair now has a detailed derivation and a sharper bound. Evaluating beta_sd would still require additional analysis or a controlled semidiscrete computation with a finite-size error bound.

Task: “take the NEXT checkable step on this problem, building on that work.” Recorded session clock: 15 November 2026, 06:41:19 Asia/Tbilisi (02:41:19 UTC).
