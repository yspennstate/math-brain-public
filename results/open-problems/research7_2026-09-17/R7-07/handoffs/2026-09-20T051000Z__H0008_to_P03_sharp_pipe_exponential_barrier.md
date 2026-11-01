# C06 -> P03 reusable lemma: exact-pipe spectral barrier for branch-renewal tails

This is a one-way mathematical handoff only. It does not change P03 ownership, objectives, reports, or scheduler configuration.

## Abstract setup

Suppose a positive vector-measure renewal has a pipe operator

\[
(A_0\Lambda)_j=\sum_iJ_{ij}(\tau_1)_*\Lambda_i,
\qquad \tau_1(u)=u+1,
\]

with a nonnegative finite matrix `J` satisfying `rho(J)<1`, and a genuine-reset operator `A_+`. Let

\[
S=(I-A_0)^{-1}A_+,
\qquad \Lambda^*=S\Lambda^*.
\]

Assume the reset coordinate obeys

\[
u'\le R^{-1},\qquad
w(u,R)\le[(1+u)R]^{-1},
\]

and the normalization controls `int (1+u)^(-1)dLambda`. Define

\[
\Gamma_R=
\sup\{\theta>0:E[e^{\theta/R}/R;R>0]<\infty\}.
\]

Then for every

\[
0<\theta<\min\{\Gamma_R,-\log\rho(J)\},
\]

the invariant renewal coordinate has a finite exponential moment. Proof: choose `q` with `rho(J)<q<e^{-theta}` and a positive weight vector `c=(I-J/q)^(-1)1`; then

\[
\|A_0\Lambda\|_{\theta,c}\le qe^\theta\|\Lambda\|_{\theta,c},
\]

while the reset estimate bounds `||A_+ Lambda||_{theta,c}` by the conserved normalization. Summing the pipe resolvent gives the finite bound.

If `J` is irreducible, `rho(J)>0`, and the genuine reset source is nonzero, the pipe threshold is also a genuine obstruction. For a Perron vector `c`,

\[
\|A_0^n\Xi\|_{\theta,c}
=(\rho(J)e^\theta)^n\|\Xi\|_{\theta,c},
\qquad \Xi=A_+\Lambda^*.
\]

Hence

\[
\int e^{\theta u}d\Lambda^*=\infty
\quad\text{for every }\theta\ge-\log\rho(J).
\]

So if the reset reciprocal tail is at least that good, `-log rho(J)` is the exact exponential-moment radius forced by arbitrarily long one-child pipes.

## Why this may help P03

For Galton--Watson speed/regeneration recursions, if a one-child stretch has a finite-type kernel `J`, then `rho(J)` does more than guarantee a finite pipe Green operator: it fixes the best possible exponential tail of any additive pipe-length coordinate after genuine branching resets. This can prevent attempts to prove an impossible stronger regeneration exponential moment and can identify the correct weighted norm before differentiating a speed formula.

The derivation and its H0008 hypotheses are in `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T050500Z__report.md`, Sections 7--8, creation commit `67fb95224a2e83fbe559045171440145716910ae`.
