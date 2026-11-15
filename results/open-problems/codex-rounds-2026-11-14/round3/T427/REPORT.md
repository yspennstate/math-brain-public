VERDICT: PROVED an explicit convergent formula and truncation bound for the square spectral finite part h_Q

The earlier report's statement-level deduction from Yunzong Xu's [arXiv:2610.40509v1](https://arxiv.org/abs/2610.40509v1) holds: its theorem implies c_square=beta_sd+h_Q. No later result changing that picture was found in the literature check, completed within three minutes. The full matching proof remains unaudited.

New beyond that report: [PROOF.md](PROOF.md) evaluates the previously unevaluated geometric limit h_Q by an explicit positive, exponentially convergent series H_M. It proves

\[
0\leq h_Q-H_M\leq
\frac{4e^{-\pi(M+1)^2}}
{\pi^2(M+1)^2(1-e^{-\pi})(1-e^{-\pi(2M+3)})}.
\]

Already M=3 gives error below 10^(-21). Independent numerical formulas give

\[
h_Q\approx0.004022236572742278.
\]

The proof derives the formula from the Neumann heat trace, checks the heat-to-zeta finite-part conversion, and independently counts the square–torus boundary correction and omitted lattice shells. A second approximation uses the original quadrant eigenvalue sum with an explicit remainder. This is a new deliverable relative to the earlier folder, not a claim that the underlying spectral calculation is new in the literature.

Reproduce the numerical checks with

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_spectral.py
```

Both runs exited 0. H_3 has analytic tail bound 3.91564898356e-24; H_5 agrees with the independently corrected heat sum within its analytic error bound 1.39401977209e-46. The environment printed a priority-change warning, but the guard verified actual niceness 20 before computation. Measured peak resident memory was 19,562,496 bytes. Complete output is in [LOG.md](LOG.md).

What failed or remains uncertain: no mathematical counterexample was found. Full validation of Xu's subdivision proof and evaluation of beta_sd remain open in this work. Numerical rounding was checked by agreement, not certified by interval arithmetic; the exact series and its proved truncation bound are the rigorous result. No numerical value of c_square is asserted.

Next worker: focus on the equal-mass smoothing constant beta_sd=kappa_equal+log(2)/(4 pi), especially Theorem 4 and Appendix C of Xu's paper. The geometric spectral term now has a reproducible evaluator and need not be estimated again. A numerical estimate of kappa_equal would require a controlled semidiscrete solver and finite-size error analysis; the bipartite or Dirichlet constant cannot be substituted.

Task: “take the NEXT checkable step on this problem, building on that work.” Session clock: 15 November 2026, 03:52:56 Asia/Tbilisi (14 November 2026, 23:52:56 UTC).
