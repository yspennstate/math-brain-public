VERDICT: PROVED exponential risk and W2 convergence for the one-dimensional strict-cone initialization case

For standard Gaussian input in dimension one and every finite bias-free ReLU
teacher, PROOF.md establishes global well-posedness of the self-consistent
characteristic flow, verifies its metric energy dissipation identity, and
proves convergence of both risk and parameter law. The initial probability
law can have unbounded support and needs only finite second moment,
`|a|<|w|` almost surely, and positive mass in each sign of w.

For independent standard normal A,W conditioned on `|A|<|W|`, write the
teacher as `c_+ ReLU(x)+c_- ReLU(-x)` and use
`R=E[(f-y)^2]/2`. Then

    R(rho_t) <= (c_+^2+c_-^2)e^(-t)/4,
    W2(rho_t,rho_infinity) <= C(c_+,c_-)e^(-t/2),
    C^2 = sum_s sqrt(1+4c_s^2) asinh(2c_s)^2 / 4.

The limiting law is an explicit sectorwise hyperbolic pushforward of the
initial law. Its risk is zero. The proof supplies more general constants for
arbitrary admissible initial laws. The convention at the ReLU kink is
`sigma'(0)=0`, but these characteristics never reach the kink.

This does not solve T223 for a full Gaussian or for general input dimension.
Uniqueness is proved for self-consistent characteristic solutions, and the
constructed solution satisfies the W2 metric energy dissipation identity.
No claim of novelty among all previously known one-dimensional cases is made.

Literature check: no post-baseline solution was identified within the bounded
search. A related restricted advance is Lénaïc Chizat, Maria Colombo,
Roberto Colombo, Xavier Fernández-Real,
[Quantitative Convergence of Wasserstein Gradient Flows of Kernel Mean Discrepancies](https://arxiv.org/abs/2603.01977),
arXiv:2603.01977, March 2026. Its Theorem 1.7 gives local polynomial
convergence for an even nonnegative spherical ReLU flow with positive smooth
target density. It does not cover the full signed Gaussian/finite-teacher
question here. Romain Petit, Clarice Poon, Gabriel Peyré,
[On the global convergence of gradient flow for wide shallow models beyond homogeneous nonlinearities](https://arxiv.org/abs/2605.10775),
arXiv:2605.10775, revised August 2026, retains the conditional convergence
conclusion. These arXiv pages and the first paper's HTML were actually opened.
The restricted advance predates the supplied November baseline, so it does
not trigger SOLVED_ELSEWHERE.md.

Reproduce the independent checks from this directory in PowerShell:

```powershell
$env:OMP_NUM_THREADS='1'; $env:PYTHONDONTWRITEBYTECODE='1'; [System.Diagnostics.Process]::GetCurrentProcess().PriorityClass='BelowNormal'; python .\verify.py
```

Output: `PASS: 22 identity/quadrature/adversarial checks.` Full output is
verification_output.txt; the data and per-check errors are in
verification.json. The program uses the Python standard library, one thread,
BelowNormal priority, and no GPU or network training. LOG.md contains the
exact output and recall commands. AUDIT.md records the independent algebra,
quadratures, kink check, and missed-case search.

What failed: the sectorwise moment closure cannot be extended directly to a
full Gaussian. An outside-cone neuron reaches w=0 at a finite clock. A
balanced wrong-sign boundary law can converge to positive risk, so simply
allowing D=0 also fails. Neither is a counterexample to the original full
Gaussian problem.

Uncertainty: no general uniqueness theorem for all nonsmooth metric-flow
conventions or general-dimensional Gaussian convergence is supplied. The
literature search is bounded and is not an exhaustive novelty review.

Next worker: first treat dimension one with a full Gaussian and a precisely
specified metric-compatible kink rule. Track neurons hitting w=0 and derive
the boundary flux correction to the two-moment system before attempting the
same risk or W2 bounds. Do not silently freeze those neurons and reuse the
cone equations.

Scope note: early math-recall calls used defaults later found capable of
appending an incidental external co-use log. Subsequent calls disabled that
logging. All authored deliverables are in this folder; no git, publication,
messages, or accounts were used. See LOG.md for the exact correction.

Task: Open problem T223, one checkable piece.
