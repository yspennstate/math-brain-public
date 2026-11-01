# H0008 -> P03 reusable lemma: zero martingale variance plus branching independence forces deterministic source

Source worker: `C06 / R7-07`, native `6aabe8413f60819197825dd81ca138ae`.  
Source report: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T080600Z__report.md`.  
This is a mathematical handoff only. It does not change P03 ownership, objective, schedule, files, or status.

## Reusable mechanism

Suppose a stationary branching-spine additive functional has a Gordin representation

\[
f=u-Pu
\]

and asymptotic variance

\[
\sigma^2=E[u^2-(Pu)^2].
\]

If `sigma^2=0`, the martingale innovation vanishes, so on a stationary reversed edge `child -> parent`,

\[
f(child)=u(child)-u(parent)
\]

almost surely.

If the forward spine selects every surviving child with strictly positive weight, then the selected-edge identity holds simultaneously for **all** surviving children of almost every parent. Therefore a transformed child variable `Z(child)` is equal across all surviving siblings.

When two prescribed surviving child subtrees can occur independently with positive probability, equality of their `Z` variables forces each `Z` law to be a Dirac mass. Mixed-type sibling events force the constants to agree across types. This can collapse the source recursion itself.

## H0008 realization

For harmonic information,

\[
f=\Phi-d_H,\qquad \Phi=-\log(1-B),
\]

and zero variance gives

\[
u(parent)=u(child)-\Phi(child)+d_H.
\]

Thus `Z=u-Phi` is equal across all surviving siblings. Branching independence makes `Z` one constant for every type; applying the identity to the parent forces `Phi(B)=d_H`, hence `B` is deterministic on survival. The electrical recursion then forces the number `K` of infinite transmitted children to be deterministic `k>=2` on survival. Since

\[
K\mid\nu=n\sim Bin(n,t_i),
\]

any `0<t_i<1` would create `K=1` with positive probability. Therefore `t_i=1`, all transmissions and child survival probabilities equal one, and finally `nu==k` deterministically.

So in H0008 the asymptotic variance is zero **iff** the source is deterministic regular/no-thinning.

## Why P03 may care

For Galton--Watson speed/regeneration work, additive observables often acquire a martingale/Poisson decomposition after a stationary environment or regeneration law is constructed. If a candidate variance or derivative degeneracy is difficult to classify analytically, the same route may be available:

1. convert zero variance to exact edge equality;
2. use positive spine weights to make it simultaneous across siblings;
3. invoke independence of two surviving offspring to force a source variable to be deterministic;
4. feed that determinism back into the offspring/escape recursion.

This avoids continuity, density, or topological-support assumptions on the environment law and can be useful when conductance or regeneration variables are singular.