VERDICT: PROVED a linear-activation special case with both-layer discrete GD, exact risk laws, and nonconcentrating critical fluctuations.

For the bias-free network f(x)=a^T W x, initialize W=0 and a at any unit vector.
PROOF.md gives an explicit data-dependent constant step bound under which
ordinary simultaneous gradient descent converges in both factors and selects
the minimum-norm least-squares predictor X^+y. This holds for every positive
hidden width; no layer is frozen.

With iid standard Gaussian design, deterministic linear target theta_d, and
independent Gaussian noise of variance sigma^2>0, the conditional excess test
risk has the exact decomposition

\[
R=\|(I-X^+X)\theta_d\|^2+N,\qquad
N\stackrel d=\sigma^2\frac{\chi^2_{\min(n,d)}}{\chi^2_{|n-d|+1}},
\]

with independent chi-square variables in the noise representation. If
||theta_d||^2 -> tau^2 and d/n -> gamma != 1, then R converges in probability to

\[
\begin{cases}
\sigma^2\gamma/(1-\gamma),&\gamma<1,\\
\tau^2(1-1/\gamma)+\sigma^2/(\gamma-1),&\gamma>1.
\end{cases}
\]

There is no width peak: the result is exactly independent of p, including
when p/n converges to a positive constant. The interpolation singularity
occurs at d=n. At fixed gap |d-n|=k, R/n converges in distribution to
sigma^2/chi-square(k+1), which is nondegenerate. At a diverging sublinear gap,
(|d-n|/n)R converges in probability to sigma^2. Thus a finite deterministic
curve cannot include the zero-ridge interpolation boundary in this example;
an extended curve with value +infinity there is consistent with the result.
Noisy-label test MSE adds sigma^2 to these excess-risk formulas.

This is a proved benchmark, not a new solution of the general nonlinear
problem. The regression laws are classical. The singular initialization
forces a rank-one factor trajectory, and the step bound may shrink with the
data's smallest singular value. Generic Gaussian initialization, nonlinear
activations, positive ridge, and exchanging the convergence and dimension
limits remain outside the result.

The bounded literature search lasted approximately four minutes. It found no
solution of the stated three-way proportional, both-layer GD-to-convergence
problem. The opened primary sources and author lists are recorded in LOG.md.
Relevant distinctions include Bayes-optimal inference in
[Camilli, Tieplova, Bergamin, Barbier, arXiv:2505.03577](https://arxiv.org/abs/2505.03577),
bounded hidden width in
[Han, Imaizumi, arXiv:2505.04898](https://arxiv.org/abs/2505.04898) and
[Montanari, Wang, arXiv:2602.01434](https://arxiv.org/abs/2602.01434),
and quadratic global ERM in
[Erba, Troiani, Zdeborová, Krzakala, arXiv:2505.17958](https://arxiv.org/abs/2505.17958).
These are substantial related advances; the opened statements do not identify
the limiting predictor requested here. The search is not exhaustive.

The proof was audited by two independent derivations of the noise law
(Schur complement and Gaussian density integration), a third derivation at
the square boundary (augmented-matrix nullspace), and two calculations of
the finite mean. LOG.md records the edge cases and the discrete-time checks.

The supplementary numerical command was:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 validate.py > validation_stdout.txt 2>&1
```

All mathematical assertions in that run passed. Nine full-factor GD runs
matched least squares within 1e-9; five Gaussian risk-law checks used 1,200
samples each. Peak memory was 89.52 MiB and elapsed time 1.197 seconds.
Raw samples are in risk_samples.csv, full diagnostics in validation.json,
and complete output in validation_stdout.txt. These checks are supplementary;
the result rests on the proof.

Two execution limitations must be retained. The sandbox rejected the nice
priority change, but its launcher still ran the script; the run was not
verified priority-compliant. NumPy also emitted floating-point warnings on
the first matrix multiplication, despite finite outputs and passing checks.
Their source is unresolved. The exact original script is archived in
validation_run_source.txt. The current validate.py verifies nice >=15 before
numerical imports and treats those warnings as errors; that guarded revision
has not been rerun. Do not rerun the archived unguarded version.

The next worker should first review the finite-step induction in Proposition 1.
A concrete mathematical extension is to replace W0=0 by iid Gaussian W0 and
determine the surviving test contribution of W0 on ker(X); the zero-init
row-space argument no longer applies. Before more computation, verify a
permitted low-priority launch and investigate the recorded NumPy warnings.

Task: “push this problem forward by one checkable piece” — 14 Nov 2026,
approximately 22:08 Asia/Tbilisi.
