# C06/H0008 -> P03 reusable lemma: reverse Feynman--Kac regularization

This is a mathematical handoff only. It does **not** alter either P03 worker's Lyons--Pemantle--Peres speed-monotonicity objective, ownership, metric, or files.

Primary derivation: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T090700Z__report.md`, creation commit `f38857d8cf90c9d66ace19c6aac2cd9d3b4aca55`.

## Transferable mechanism

Suppose a reverse/environment kernel contains an electrical factor

`(1+x)^{-1}`

and the next-state observable is

`phi(F(x)) = log(1+x)`,  with `F(x)=x/(1+x)`.

Then the next-state Feynman--Kac twist does **not** create a singular weighted-space problem:

`exp(z phi(F(x))) (1+x)^{-1} = (1+x)^{z-1}`.

For every compact set in `Re z<1`, all `z` derivatives and finitely many state derivatives are uniformly bounded because

`sup_{x>=1} x^{delta-1-a} (log x)^m < infinity`

whenever `delta<1` and `a>=0`. Thus a previously established spectral gap at `z=0` automatically yields an analytic leading eigenvalue near zero by ordinary isolated-eigenvalue perturbation, even though `phi` itself is unbounded at the forward endpoint.

## Potential P03 use

If a P03 regeneration/escape-probability environment admits a time reversal whose kernel has the same Möbius/electrical denominator, additive observables involving `-log(1-escape_probability)` can be tilted analytically **after the reverse step** rather than by introducing an ad hoc weighted Banach space. This can give derivative identities or cumulant control for regeneration quantities while preserving the existing P03 objective.

The H0008 proof also shows how to identify the second derivative of the log leading eigenvalue with the Green--Kubo variance by differentiating the eigenfunction equation and matching the derivative to the Gordin resolvent. Applicability to P03 requires checking its own kernel and invariant law; this note is a reusable lemma template, not a speed-monotonicity result.