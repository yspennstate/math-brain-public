VERDICT: PROVED an exact deterministic reduction for spatially constant additive noise

For nonzero spatially constant additive Gaussian noise on the three-dimensional torus, subtracting the Brownian spatial mean and translating by its time integral converts every pathwise Leray–Hopf martingale solution into an unforced deterministic Leray–Hopf trajectory. The converse construction also holds. PROOF.md gives the argument at weak regularity and proves exact equality of the stochastic and deterministic energy defects.

Two consequences are proved. Uniqueness of the stochastic **velocity law** is equivalent to deterministic Leray–Hopf uniqueness for the centered initial datum. For smooth data, almost-sure global strong solvability is equivalent to deterministic global strong solvability; maximal strong lifetimes agree almost surely. The recovery map uses only the velocity path, so these statements do not confuse joint-law uniqueness with velocity-law uniqueness or assume away extra randomness in martingale solutions.

This is an elementary reduction, with no novelty claim. It does not settle T091. Constant noise is excluded if the phase space and covariance are required to be mean zero. Nonconstant mean-zero noise remains untreated. The solution class here requires a pathwise energy inequality, explicitly written in PROOF.md; a definition using only expected energy inequalities is not silently included.

The bounded literature search found no verified settlement of the stated problem. It did find Felix Brandt and Igor Kukavica, *Regularizing the Navier-Stokes Equations by One Noise Component*, [arXiv:2611.02557](https://arxiv.org/abs/2611.02557), submitted 2 November 2026. Its multiplicative-noise, high-probability results do not settle the additive-noise statement. Further opened references, authors, scope checks, and exact search queries are recorded in LOG.md. No SOLVED_ELSEWHERE.md was created.

Validation:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_reduction.py
```

The successful invocation printed:

```text
nice: setpriority: Operation not permitted
Inherited nice: 20
PASS: 6 exact Fourier drift, translation, and energy-splitting trials
PASS: 5 exact quadratic-increment averages (covariance ranks 0 through 3)
PASS: wrong translation sign and wrong nonzero Ito trace coefficient rejected
Data: audit_results.json
Peak RSS: 16154624 bytes
```

The computation used exact rational arithmetic, one process, under one second of reported wall time, and about 16 MB peak RSS. It checks algebra, not PDE regularity. The inherited nice value was 20; the script refuses to compute below 15. The sandbox rejected the requested priority adjustment. Darwin also rejected memory-cap calls; two initial runs stopped at those calls before any algebra. The successful run recorded those failures and measured actual memory. LOG.md preserves the exact command and all material outputs; audit_results.json contains the data.

AUDIT.md independently re-derives the translation sign, the trace factor, the norm splitting, the covariance ranks, and the finite mode count. It records attempts to break the law argument, the weak chain rule, the energy starting-time convention, and the inference from stochastic to deterministic regularity. No gap was found within the stated scope. Standard local deterministic strong existence is used only in the maximal-lifetime formulation; neither global existence nor deterministic weak uniqueness is assumed.

Next worker: fix a genuinely nonconstant mean-zero covariance before attempting further regularization claims. The mean-subtraction transformation then leaves a spatially varying stochastic term, so the exact cancellation proved here no longer removes the forcing. A useful next piece would be a precise conditional energy or regularity criterion for that remaining term. Separately, check the exact energy-solution definition before extending the law equivalence to energy-supermartingale formulations.

Task: “Open problem T091: Uniqueness and regularity for the three-dimensional stochastic Navier–Stokes equations” — session first clock reading 2026-11-14 20:55:11 +04 (Asia/Tbilisi).
