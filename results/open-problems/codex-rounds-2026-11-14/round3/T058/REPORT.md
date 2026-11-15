VERDICT: PARTIAL proved joint second-moment estimates for the two independent-set counts on fixed interior phase bands

The earlier deterministic phase-density result holds. Its finite counts, density constants and theta calculation were independently reproduced; see LOG.md and earlier_recheck.json.

The new piece is probabilistic. Put k=floor(f(n)), where f is the independence-number approximation in the earlier report, and let X_j count independent j-sets in G(n,1/2), with mean mu_j. Uniformly when delta <= {f(n)} <= 1-delta for any fixed 0<delta<1/2, [PROOF.md](PROOF.md) proves

\[
\operatorname{Var}X_k\sim\mu_k,\qquad
\operatorname{Var}X_{k-1}\sim\mu_{k-1},\qquad
\operatorname{Cov}(X_k,X_{k-1})\sim k\mu_k.
\]

In particular,

\[
\operatorname{Corr}(X_k,X_{k-1})
\sim\sqrt{\frac{k(n-k+1)}{2^{k-1}}}
\sim\frac{2\sqrt2}{e}\,2^{\{f(n)\}/2}
                 \frac{(\log_2n)^{3/2}}{\sqrt n}\longrightarrow0.
\]

The best affine prediction of X_(k-1) from X_k leaves mean-square error asymptotic to mu_(k-1). Contained pairs give the leading covariance; a complete overlap bound makes every other contribution smaller. This extends the earlier report from deterministic phase frequencies to explicit joint moments of the two random counts motivating the Zigzag Conjecture. The band [1/4,3/4] has the positive lower density 1/(1+2^(1/4)) established earlier.

This proves no new concentration bound for chi and makes no literature-novelty claim. Annika Heckel and Oliver Riordan, [*How does the chromatic number of a random graph vary?*, arXiv:2103.14014](https://arxiv.org/html/2103.14014), already discuss approximately Poisson marginal counts; the present piece gives a self-contained joint second-moment estimate on a specified band. The missing relation between these counts and chi is not resolved. Small correlation alone supplies neither independence nor a joint Gaussian law.

Reproduce all checks from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 recheck_earlier.py
OMP_NUM_THREADS=1 nice -n 15 python3 verify_moments.py
OMP_NUM_THREADS=1 nice -n 15 python3 audit_extension.py
```

All final runs passed. The first reproduces the earlier four counts and density constants. The second enumerates all 1024 graphs on five vertices and 32768 on six, and compares exact rational moments with two overlap formulas. The third uses a separate descending recurrence, Decimal inversion, and exact rational checks of the proof's bounds at n approximately 2^320. Runs took 0.051, 3.349 and 20.082 seconds, respectively; peak RSS stayed below 20 MB. The launcher emits a priority diagnostic because nice is already 20; every script verifies actual nice >=15 before computing. Full output is in the three JSON files, with commands and relevant values in LOG.md.

One initial diagnostic failed: a demand for variance relative error below 1e-6 at n approximately 2^160 was unjustified. At phase .75 the actual error is about .0187; at n approximately 2^320 it is 5.108702812850075e-13. The threshold was removed, and no finite uniform cutoff is claimed. [AUDIT.md](AUDIT.md) records hand calculations, endpoint cases and the limitations of the conclusion.

The literature check, under five minutes, found no solution of fixed-p=1/2 concentration. It did find an omission in the earlier summary: Oliver Riordan's Oxford talk, [*Cube-root concentration of the chromatic number of G(n,1/2) – sometimes*, 18 February 2025](https://www.maths.ox.ac.uk/node/70763), announces joint work with Rob Morris giving an O*(n^(1/3)) upper bound for certain n. No paper, arXiv id, precise phase range or proof was located within the search budget; this announcement is not used as a theorem here. Zhifei Yan's opened [*Exponential tails for factors and the chromatic number of random graphs*, arXiv:2609.12700](https://arxiv.org/abs/2609.12700), concerns edge probabilities tending to one. Neither establishes a solution of the present fixed-p problem.

The next worker should obtain the precise statement and proof behind the Morris–Riordan cube-root announcement before attempting a new concentration bound. For the probabilistic route here, the next missing estimate is a conditional relation between chi and the two counts, or their joint law plus a proved sensitivity estimate. The moment calculation alone cannot provide that transfer.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first recorded local clock 01:03:37 +04.
