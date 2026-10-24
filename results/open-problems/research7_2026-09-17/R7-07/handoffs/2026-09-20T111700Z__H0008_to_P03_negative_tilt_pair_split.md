# C06 / H0008 handoff to P03 — negative Feynman–Kac contraction and pair split-time tail

Date: 2026-09-20 UTC  
From: `C06 / R7-07`, native `6aabe8413f60819197825dd81ca138ae`  
To: P03-A / P03-B Galton--Watson speed roles, for reuse only; **no change to P03 ownership or objective**.

Source report: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T111300Z__report.md`.

## Reusable mechanism

Suppose an environment chain has a stationary reversal whose projected transition can be written as a Doob conjugate of

\[
(\mathcal T f)_j(b)
=\sum_i M_{ij}E\left[\frac{f_i(F(b+R_i))}{1+b+R_i}\right],
\qquad F(x)=\frac{x}{1+x},
\]

and the exact one-child/pipe boundary matrix

\[
J_{ij}=M_{ij}P(R_i=0)
\]

satisfies `rho(J)<1`. If the stationary Doob density is `C^k` for arbitrarily large finite `k`, then for every fixed negative Feynman--Kac tilt `t<0`,

\[
(\mathcal T_t f)_j(b)
=\sum_iM_{ij}E[(1+b+R_i)^{t-1}f_i(F(b+R_i))]
\]

has top `k`-th derivative matrix

\[
A_t^{(k)}{}_{ij}=M_{ij}E[(1+R_i)^{t-1-2k}]\to J_{ij}.
\]

Thus for large finite `k`, a Doeblin--Fortet estimate gives quasi-compactness. The tilted Markov conjugate is strictly sub-Markov because `e^{t\phi}<1` for the positive escape-cost observable `phi`; a maximum-principle argument rules out spectral radius one. Therefore every fixed negative tilt contracts exponentially.

This can be useful in speed/regeneration work when a path functional is nonnegative and exact one-child stretches are the only compactification channel. It avoids requiring a uniform one-step split probability.

## Pair-spine consequence worth reusing

In H0008, two independent harmonic rays have common-prefix survival

\[
P_T(\tau>n)=Z_n(2;T).
\]

The global negative-tilt contraction plus all inverse moments of the root conductance gives

\[
E Z_n(2;T)\le Ce^{-cn},
\]

hence, source-a.s., `P_T(tau>n)` is eventually exponentially small and `E_T exp(a tau)<infinity` for a deterministic `a>0`. More generally every fixed `q>1` harmonic Renyi mass decays exponentially.

For P03, the structural lesson is: **subcritical exact pipes plus a reverse negative Feynman--Kac contraction can give exponential pair/regeneration overlap tails even when no uniform local split/minorization bound exists.** This may be useful for coupling histories or derivative covariances. It does not prove any P03 speed-monotonicity statement by itself.

Status: reusable `PROVED PARTIAL` lemma from C06; not independently audited. No P03 file or claim was modified.