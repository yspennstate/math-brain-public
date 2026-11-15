VERDICT: PROVED global population-gradient-flow convergence at every finite depth for untied scalar attention step sizes with all other blocks fixed

The round-3 two-layer theorem holds. The extension here covers every
finite L>=1 in the same d=1 architecture. At every finite prompt length
N>=1, gradient flow from any pairwise distinct scalar initialization
converges to the global minimizer with that coordinate ordering.
Independent non-atomic random step-size initialization therefore succeeds
almost surely. Only the L direct scalar Q entries are trained.

The limiting predictor implements L empirical least-squares gradient
steps from zero. Set alpha=N/2. Its residual polynomial is

    r_*(s)=sum_(k=0)^L (-1)^k binom(L,k) alpha^k s^k/(alpha+1)_k.

The learned step sizes are the reciprocals of its L distinct positive
roots, in the initial ordering. The exact prediction risk is

    L!/(alpha+1)_L = 2^L L! / product_(j=1)^L (N+2j).

Thus the excess over the noiseless scalar Bayes risk zero is asymptotic
to 2^L L!/N^L for each fixed L. At depth three it is exactly
48/[(N+2)(N+4)(N+6)]. Depth two recovers the earlier 8/[(N+2)(N+4)].

The new convergence ingredient resolves the earlier report's
repeated-root obstruction. Each pair difference satisfies

    (a_i-a_j)' = (a_i-a_j) 2 E[S^2(1-a_i S)(1-a_j S)R(S)^2],

where S=sum x_i^2/N and R contains the remaining residual factors.
The multiplier is uniformly positive near collisions on a bounded
sublevel set. Every initially nonzero gap therefore stays bounded away
from zero. The coefficient Jacobian remains uniformly invertible along
the trajectory, and strict convexity in polynomial coefficients gives
exponential loss-gap convergence. PROOF.md supplies all steps and a
second quantitative derivation of the collision neighborhood. No general
analytic-flow or stable-manifold theorem is needed.

Every nonglobal stationary point is a strict saddle with a repeated
pair. Repeated initial steps remain equal and cannot attain the global
risk; pairwise distinctness is the exact success condition. Negative
initial values and a single zero value are allowed. No uniform training
time in N, L, or the initial gaps is proved.

Validation commands:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T325/audit_scalar.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_depth.py
```

Both passed. The new standard-library script independently computes
Gaussian moments, solves the coefficient normal equations, verifies the
exact risk, and counts positive simple roots by rational Sturm sequences
for N=1,2,3,5,10,100,1000 and L=1,...,8. It also verifies 105 pair
identities and 315 collision cases, plus Jacobians, loss gaps, and token
updates. Final arithmetic run: 0.710 seconds, peak RSS 15.48 MiB,
inherited nice=20. The nice wrapper prints a priority-setting warning;
the script explicitly checks that the inherited priority is low enough.
The earlier script's optional address-space cap remains unavailable;
no hard RAM cap is claimed. All arithmetic is small and exact.

The initial five-minute literature check found no full solution changing
the task. Sources actually opened and the architectural differences are
recorded in LOG.md. The architecture used here is from Khashayar Gatmiry,
Nikunj Saunshi, Sashank J. Reddi, Stefanie Jegelka, Sanjiv Kumar,
*Can Looped Transformers Learn to Implement Multi-step Gradient Descent
for In-context Learning?*, [arXiv:2410.08292v1](https://arxiv.org/html/2410.08292v1),
Section 3 and Appendix A.1. No exhaustive novelty claim is made.

What failed or remains uncertain: no proof failed within the stated
scalar model; the brief literature check cannot establish priority.
The full T325 problem remains open here. Nothing establishes convergence
with all transformer blocks randomly initialized and trained, d>1,
softmax attention, separately factorized keys/queries, or discrete or
stochastic training. All writes stayed in this folder; no git, external
mutations, subagents, or model training were used.

Next worker: keep the scalar architecture and analyze gradient flow when
each direct step is replaced by a_i=k_i q_i with both factors trained.
Then a_i'=-h_i partial_i F, h_i=k_i^2+q_i^2, and k_i^2-q_i^2 is
conserved. The pair-difference equation above no longer factors, so the
uniform gap argument does not directly apply. Establishing global
convergence for independent continuous factor initialization would close
another concrete restriction. Alternatively, derive a discrete-step
training theorem with an explicit step-size condition.

Task: “take the NEXT checkable step on this problem, building on that work.” — 15 November 2026, approximately 06:31 Asia/Tbilisi.
