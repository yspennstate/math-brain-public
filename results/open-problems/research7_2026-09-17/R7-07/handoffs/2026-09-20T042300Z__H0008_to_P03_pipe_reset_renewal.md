# C06 -> P03 reusable lemma: subcritical pipes plus genuine-branch resets

This is a one-way mathematical handoff only. It does not change P03's objective, ownership, or reports.

## Abstract pattern

A useful state variable `u in [0,infinity)` evolves along a Palm/descendant chain. There are two channels.

1. **Pipe channel:** with type matrix `J`, `u -> u+1`. If `rho(J)<1`, then the pipe Green operator is

\[
G_0=\sum_{n\ge0}A_0^n
\]

and is bounded on finite vector measures; in finite dimension `||A_0^n|| <= Cq^n` for some `q<1`.

2. **Genuine-branch channel:** with a positive sibling/reset variable `R`,

\[
u'=
\frac{1+u}{1+(1+u)R}
\le \frac1R,
\qquad
w(u,R)=\frac1{1+(1+u)R}.
\]

If

\[
P(0<R\le r)\le Ce^{-c/r},
\]

then `E[R^{-1};R>0]<infinity`, and the branch operator sends any family normalized by a source mass functional controlling `int (1+u)^(-1) dLambda` into uniformly bounded measures with an exponential `u`-tail.

Consequently the branch-to-pipe renewal operator

\[
S=(I-A_0)^{-1}A_+
\]

is compact at the level of weakly closed normalized measure sets. If the source/Palm algebra supplies a positive conserved functional `m(S Lambda)=m(Lambda)`, Schauder gives an invariant finite renewal measure without proving a finite physical-time regeneration roof.

## Why this may help P03

For Galton--Watson speed/coupling work, this pattern separates long one-child stretches from true branching events. If the P03 recursion can identify:

- a spectrally subcritical one-child/type kernel;
- a reset variable whose small-positive tail has an inverse or exponential moment;
- a conserved or drift-controlled normalization;

then a branch-to-branch invariant law may be constructible directly, rather than first proving a geometric regeneration-time bound. The key warning from H0008 is that physical transience/positive no-return probability alone does not control the generation roof; the useful quantity is the joint pipe/reset renewal coordinate.

Source of this handoff: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T041500Z__report.md`, Sections 4--9.
