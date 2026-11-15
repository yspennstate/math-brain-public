VERDICT: PROVED a positive iid exclusion cap for local minima around a specified stored pattern at every positive load

The round-4 result survives independent checking. The new result in
[PROOF.md](PROOF.md) uses iid disorder rather than another correlated
construction. For alpha>0 and t>0, define

\[
 L_\alpha=8(1+\alpha)\log9-\alpha,\qquad
 R_\alpha(t)=
 \frac{t^2\Phi(-(1+t)/\sqrt\alpha)}{t^2+4L_\alpha^2}.
\]

For every fixed delta<R_alpha(t), with probability tending to one there
is no single-spin local minimum within floor(delta N) errors of a
specified stored pattern. The fraction of patterns having a minimum
that close tends to zero in probability. This does not assert exclusion
around every pattern simultaneously.

At alpha=1/7, t=1/5, the formula gives approximately
1.883692779057533e-8. A separate rational argument proves
R>1/88,202,000>10^{-8}, so error fraction 10^{-8} is a certified exclusion
cap. This is an asymptotic, conservative constant, not a practical
finite-network threshold or an improvement claimed over published bounds.

The proof combines a deterministic inequality for simultaneous spin
stability with the empirical Gaussian law of the signed local fields at
one stored pattern. The latter is proved by explicit fourth moments, a
two-site central limit theorem and a variance calculation. An elementary
matrix-net argument supplies the operator norm bound. It follows that
overlap tending to one at fixed positive extensive load is impossible
for a specified iid pattern, and for all but a fraction tending to zero
of the patterns. The intended fixed-tolerance AGS problem remains open
in this work, as does the replica-symmetric retrieval free energy.

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 recheck_round4.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_iid_cap.py
```

The first script independently verifies the earlier Gram identity, all
shell optima, all neighbors and all minima on instances up to 16 spins
using weighted cuts. The second checks the new moments by complete sign
enumeration and tests the deterministic stability bound at every minimum
of three finite arrays. It independently recomputes the normal tail by a
Decimal power-series integral and checks the rational constant exactly.
Both passed, with peak RSS below 15 MiB and runtimes below one second.
Inherited niceness was 20; the sandbox rejects raising priority to 15,
so actual niceness stayed at 20. Full output is in [LOG.md](LOG.md).

What failed or remains uncertain: no mathematical verification failed.
The two-site argument provides convergence without a rate sufficient
for a union bound over all patterns. The norm constant is loose, and
the resulting cap is far smaller than retrieval errors relevant to the
AGS spinodal. No exclusion above 0.138 at a meaningful fixed tolerance,
capacity certificate, or free-energy formula was obtained. The standard
Lyapunov CLT and Cramer-Wold criterion are used with their hypotheses
checked; they are not reproved. No literature novelty beyond the earlier
sessions is claimed for the restitution-error obstruction.

The five-minute literature update found no newer solution of the stated
problem. Opened sources still list v1: Ayman Ali, Jeanne Boursier,
Hong-Bin Chen, Fu-Hsuan Ho, Victor Issa, Jean-Christophe Mourrat,
*Free energy of the Hopfield model*,
[arXiv:2611.03306v1](https://arxiv.org/html/2611.03306v1); and Yuwen Zhou,
*THE CRITICAL CAPACITY OF THE HOPFIELD MODEL*,
[Hexagon 2611.00105v1](https://hexagonmath.org/pdf/2611.00105v1).
The latter defines capacity through a limiting overlap-profile well.
Their full proofs and numerical certificates remain unaudited here.

Next worker: prove a quantitative empirical-field concentration bound
with failure o(1/N), or exponential, to obtain simultaneous exclusion
around every stored pattern. Retain the distinction between that claim
and the present specified-pattern/vanishing-fraction conclusions.
Sharper matrix estimates can improve the numerical cap; a useful
AGS-scale exclusion will also need substantially better control of
the field corrections caused by an error set.

Task: “take the NEXT checkable step on this problem, building on that work.” Start: 15 November 2026, 09:14 +04.
