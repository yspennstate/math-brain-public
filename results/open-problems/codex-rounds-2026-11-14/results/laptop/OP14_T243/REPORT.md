VERDICT: PROVED sharp depth/width rates in functional W2 and total variation for bias-free ReLU networks on a positive input ray

For h hidden layers of common width n, Gaussian weights of variance 2/fan-in, scalar linear output, and a fixed compact set K on a nonnegative input ray, both distances between the network law and its NNGP law on C(K) have order h/n whenever h/n->0. In particular the fixed-depth rate is n^(-1). The ray must contain a nonzero point.

The proof gives explicit finite-n upper bounds. With V the product of h iid copies of n^(-1) sum 2(G_i^+)^2, put D2=E(V-1)^2 and D4=E(V-1)^4. Their exact formulas are in PROOF.md. For A equal to the limiting standard deviation at the outermost ray point,

    TV <=min(1,6D2),
    W2 <=A[4sqrt(D4)+64D4+sqrt(2)D2].

Uniformly when h/n->0, D2=5h/n+O((h/n)^2) and D4=O((h/n)^2). A bounded smooth cosine test has expectation gap

    [5 exp(-1/2)/8] h/n +o(h/n).

This gives matching lower bounds. All C^4 tests with bounded derivatives satisfy an explicit O(D2) upper bound. Every k-point marginal containing a nonzero ray point has exactly the same TV distance as the scalar coefficient, with no dependence on k.

A separate all-depth bound, valid for n>=100, is

    W2 >= A sqrt(2/pi)[1-exp(-h/(3n))].

Thus functional W2 convergence in this special case holds exactly when h/n->0. The W2 multiplicative constant has not been optimized.

Files: PROOF.md contains the complete proof; AUDIT.md records the adversarial checks; verify.py is the deterministic verification script; verification.json contains its data; verification_output.txt contains its console output; LOG.md records the work and exact commands.

Reproduce in PowerShell from this folder:

```powershell
$p = Get-Process -Id $PID
$p.PriorityClass = 'BelowNormal'
$env:OMP_NUM_THREADS='1'
$env:OPENBLAS_NUM_THREADS='1'
$env:MKL_NUM_THREADS='1'
$env:NUMEXPR_NUM_THREADS='1'
$env:PYTHONDONTWRITEBYTECODE='1'
python -B verify.py
```

The final run exited 0 with all checks passed. Single-factor moments were checked by exact set partitions, product moments by an independent centered recurrence, and the smooth-test coefficient by a closed one-layer Laplace transform. Numerical Gaussian-overlap integration agreed within 9.55e-15. Extinction at width one and the depth lower-bound constants were checked. The script uses the standard library, small fixed workloads, one thread, and BelowNormal priority; it has a two-minute internal work budget. No GPU, training, or large arrays.

No numerical check failed. The naive conditional Gaussian coupling only gives a square-root fluctuation rate; the proof closes this gap by clipping the variance, keeping the clipping-induced mean error, and using an exact density-overlap identity plus a proved one-dimensional entropy/transport inequality. Direct entropy calculations on the original distribution would fail because it has an atom at zero; the proof explicitly avoids that step.

The literature check did not settle the whole problem. [Luis Wiederhold, Nil Ayday, Debarghya Ghoshdastidar, arXiv:2610.18166v1](https://arxiv.org/html/2610.18166v1) give a one-hidden-layer polynomial-activation functional W2 upper bound of order n^(-1/2), and explicitly leave sharpness open. Other opened references and their precise inspected scope are recorded in SOLVED_ELSEWHERE.md. That filename is not a claim that T243 is solved.

Limits and uncertainty: positive-ray inputs make both laws rank one. The theorem does not treat general compact K, non-collinear inputs, biases, general Lipschitz activations, or sharp constants. Prior math-memory work already contained the product representation and the constant 5, as well as related T243 numerical results. The present self-contained explicit functional transport estimate and uniform depth theorem have been checked here, but literature novelty has not been established and there has been no independent referee review.

Next worker: extend the variance-mixture cancellation estimate to matrix-valued conditional covariance on the covariance kernel's actual range, then control its constants under dense input discretization. The main remaining obstacle is an infinite-rank kernel whose small eigenvalues deteriorate with the discretization. A finite set or a rank-one support alone does not resolve that obstacle.

Task: Open problem T243 — optimal rates in the Gaussian-process limit of wide random networks; one checkable piece.
