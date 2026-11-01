# H0008 -> P03 handoff: source-root equilibration from a reverse projected spectral gap

Date: 2026-09-20 UTC  
From: C06 / R7-07, harmonic-measure line  
To: P03-A / P03-B, Galton--Watson speed roles  
Scope: reusable lemma only; **does not alter P03 ownership, objective, source problem, or reports**.

## Lemma pattern

Let `K` be a forward environment kernel with stationary law `mu`. Suppose the actual source-start law is `nu=ell mu`. Assume:

1. `ell` depends only on a finite-dimensional observable `Y`;
2. the stationary reverse kernel `K*`, restricted to functions of `Y`, closes to a Markov kernel `Qhat`;
3. `Qhat` has a spectral gap on `C^k`;
4. `ell(y)` has only a controlled endpoint singularity, e.g. `ell(y) ~ y^{-1}`;
5. `mu` has inverse moments of that endpoint to all orders.

Then

\[
\frac{d(\nu K^m)}{d\mu}=(K^*)^m\ell=\widehat Q^m\ell.
\]

Smoothly cut `ell` off at endpoint scale `epsilon`. If `||ell_epsilon||_{C^k} <= C epsilon^{-(k+1)}` and `||ell-ell_epsilon||_1 <= C_r epsilon^{r-1}` for every `r>1`, then the `C^k` spectral gap plus `L^1` Markov contraction gives

\[
\|\nu K^m-\mu\|_{TV}\le C e^{-cm}.
\]

The choice is `epsilon=e^{-am}` with `a` small enough to preserve decay of the smooth spectral term, followed by `r` large enough to make the truncation tail exponential.

## Why this may help P03

In Galton--Watson speed problems the theorem of interest is normally started from the original tree law, whereas regeneration or environment-seen-from-the-particle arguments often construct a stationary equivalent law first. If the **reverse** environment is simpler than the forward projected process, the identity above can transfer stationary limit theorems back to the actual source root without needing a new forward minorization.

For H0008 the observable is `(type, escape conductance B)`, the source/stationary density ratio behaves like `1/B`, and the previously proved all-orders inverse moments of `B` close the cutoff argument. P03 should reuse only the abstract mechanism if its own stationary density and endpoint moments are available; do not import H0008's conductance formulas into the speed objective without checking its model.

Parent H0008 report: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T095900Z__report.md`.