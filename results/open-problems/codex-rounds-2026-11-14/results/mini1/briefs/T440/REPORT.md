VERDICT: PROVED an explicit exponential lower bound for the first-click time when 0<lambda<alpha

For the specified infinite-dimensional diffusion, started at its mutation-selection Poisson profile, put
\[
 V_-=2[\alpha-\lambda+\lambda\log(\lambda/\alpha)],\qquad
 C_-=\frac{\alpha\sqrt\pi}{\sqrt\lambda(\alpha-\lambda)^2}.
\]
For fixed \(0<\lambda<\alpha\), the proved statement is
\[
 \liminf_{\nu\to\infty}
 \frac{\mathbb E\tau_\nu}{C_-\nu^{-1/2}e^{\nu V_-}}\ge1.
\]
In particular \(\liminf\nu^{-1}\log\mathbb E\tau_\nu\ge V_->0\).

The finite-noise bound is the exact positive double integral (1) in PROOF.md, evaluated at \(e^{-\lambda/\alpha}\). It is also the exact mean extinction time of the scalar diffusion with drift \(y[\alpha(1-y)-\lambda]\) and covariance \(y(1-y)/\nu\). The transfer to the full diffusion uses the exact inequality \(m(X)\ge1-X_0\) and stopped Itô's formula. It assumes no autonomous closure for \(X_0\).

The multiplier above belongs to the lower bound. The sharp exponential rate and leading prefactor for the full diffusion remain unresolved. The result is not claimed to be new to the literature.

## Files and verification

- PROOF.md: complete proof, including the degenerate boundary at 1, stopping at the absorbing boundary, and control of all four integration regions.
- CHECKS.md: independent barrier and flux calculations, time-scaling check, and cases where the argument could fail.
- audit.py: numerical cross-check in opposite integration orders; independent barrier integral and prefactor checks.
- audit_data.csv: 20 rows of numerical results.
- audit_output.txt: exact command output.
- LOG.md: search record, chosen scope, derivation checkpoints, command, and output.

Run from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 audit.py > audit_output.txt 2>&1
```

The run exited 0 in 0.411 seconds with peak RSS 72,613,888 bytes, one thread, and inherited niceness 20. The largest relative discrepancy between integration orders was \(1.25\times10^{-10}\). Barrier and multiplier checks agreed to \(1.12\times10^{-16}\). At \(\nu=400\), the exact scalar lifetime divided by its asymptotic was 1.00153424, 1.00527964, and 1.05609327 for \((\alpha,\lambda)=(1,0.25),(1,0.5),(1,0.8)\), respectively. Quadrature is a check, not a certified numerical proof; the analytic proof is independent of these values.

## Literature check

The web search was completed within ten minutes. No later solution of the specified sharp asymptotic problem was found. This is a limited negative search result, not a proof that no such paper exists. Papers actually opened:

- Carola Sophia Heinzel, Peter Pfaffelhuber, Anton Wakolbinger, *A small noise approximation for Muller's Ratchet*, [arXiv:2606.15842](https://arxiv.org/abs/2606.15842), [full text](https://arxiv.org/html/2606.15842v1). Its current arXiv page lists only v1. Its fixed-time expansion does not give the requested sharp first-passage asymptotic.
- Richard A. Neher, Boris I. Shraiman, *Fluctuations of fitness distributions and the rate of Muller's ratchet*, [arXiv:1206.6782](https://arxiv.org/abs/1206.6782), [full text](https://arxiv.org/html/1206.6782v1). The path-integral rate and multiplier involve approximations; they do not supply a proof of this sharp diffusion first-click problem.
- Mauro Mariani, Etienne Pardoux, Aurélien Velleret, *Metastability between the clicks of Muller's ratchet*, [arXiv:2007.14715](https://arxiv.org/abs/2007.14715). The abstract proves quasistationary convergence and moment estimates, rather than the requested small-noise multiplier.
- Jan Lukas Igelbrink, Charline Smadi, Anton Wakolbinger, *The tournament ratchet's clicktime process, and metastability in a Moran model*, [arXiv:2512.24779](https://arxiv.org/abs/2512.24779). The abstract treats tournament selection and a two-type Moran process, which have different structure from the specified diffusion.

No SOLVED_ELSEWHERE.md was created.

## What failed, and what is uncertain

A naive global saddle bound fails when F is negative at the initial mass; the proof replaces it with a four-region estimate. The scalar comparison cannot establish a matching upper bound: mass in mutation classes at least 2 contributes a strictly positive excess drift. No valid equality of full and scalar exponential rates was obtained.

The metastable scalar asymptotic is only for fixed \(0<\lambda<\alpha\); it cannot be continued across \(\lambda=\alpha\) or made uniform at either endpoint by this proof. No rare-click formula for a finite-population genetic model or long-time clicking rate is inferred. It remains uncertain whether this explicit comparison bound strengthens the best existing rigorous bounds.

## Next step

Try a test function depending on \((X_0,X_1)\) to retain part of the omitted drift. The exact inequalities
\[
 m(X)\ge X_1+2(1-X_0-X_1)=2(1-X_0)-X_1,
 \qquad
 m(X)-1\ge1-2X_0-X_1
\]
give joint lower bounds on the two coordinate drifts. A two-variable function increasing in both coordinates and solving a suitable generator inequality could improve the present bound. The sign of each derivative must be proved before substituting these inequalities. In particular, suppressing or deleting the mutation tail without a proved generator inequality would not be justified.

Task: "push this problem forward by one checkable piece" — 14 November 2026, about 22:16 Asia/Tbilisi.
