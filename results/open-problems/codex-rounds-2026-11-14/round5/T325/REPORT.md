VERDICT: PROVED almost-sure global population-gradient-flow convergence at every finite depth for scalar attention with both key/query factors trained and all other blocks fixed

The round-4 direct-step theorem holds. The new result removes its
restriction against separately training the two scalar factors of each
step. Set a_i=k_i q_i and train all 2L scalars k_i,q_i by Euclidean
population gradient flow, for every finite depth L>=1 and prompt length
N>=1. For every initialization the factor trajectory is bounded and
converges to a critical point. Every nonglobal critical point is a strict
saddle. Outside a Lebesgue-null set of initial factors the limit is
globally optimal. This includes independent Gaussian initialization of
the 2L factors, with no size or sign restriction. It requires a joint
law with a density, not merely an atomless law.

The limiting predictor implements L empirical least-squares gradient
steps from zero. The products a_i are a permutation of the reciprocals
of the distinct positive roots of

    r_*(s)=sum_(j=0)^L (-1)^j binom(L,j) (N/2)^j s^j/(N/2+1)_j.

Its exact squared prediction risk is unchanged from the direct-step
optimum:

    L!/(N/2+1)_L = 2^L L!/product_(j=1)^L(N+2j).

It approaches the noiseless scalar Bayes risk zero as N tends to
infinity, with fixed-depth leading term 2^L L!/N^L. Each finite-N flow
is trained to its limit before this asymptotic limit is taken.

The new argument uses the conserved imbalance D_i=k_i^2-q_i^2 and
(k_i^2+q_i^2)^2=D_i^2+4a_i^2 to bound individual factors. At a critical
point with no double-zero pair, the product map has full row rank and
lifts the earlier negative splitting curvature. At a double-zero pair,
the product derivative need not vanish, but is strictly negative; the
factor Hessian has block [[0,F_i],[F_i,0]] and hence a negative direction.
Analytic gradient convergence and local center-stable manifolds then
give actual convergence and a null attraction set for all nonglobal
critical points. PROOF.md states the imported local theorems, cites
opened sources, and gives the localization and countable-cover steps.
No countability of the critical set or global Hessian bound is assumed.

The earlier deterministic pair-order proof does not transfer: equal
products can separate when factor imbalances differ. At N=2,L=2,
(k_1,q_1)=(1,1), (k_2,q_2)=(2,1/2) gives (a_1-a_2)'=99/2.
There are genuine exceptional initializations. Already at one layer,
k=-q stays anti-balanced and converges to the zero-product saddle,
whose risk is 1. Thus convergence from every initialization is false.

Validation commands:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T325/audit_depth.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_factors.py
```

Both passed. The earlier audit independently rechecks moments, the
coefficient optimum, risks, roots and collision identities. The new
standard-library script imports none of the earlier scripts. It checks
24 coefficient/risk cases, 126 flow and boundedness identities, 36
factor-path Hessians and token updates, 63 double-zero Hessians, 45
lifted splitting directions, and 18 actual critical-point cases. It
also checks the anti-balanced obstruction and factor-limit formulas.
Its bivariate polynomial expansion is independent of its Hessian
chain-rule computation. Runtime 0.348 seconds, peak RSS 15.12 MiB,
inherited nice=20. The nice wrapper prints a priority-setting warning;
the script verifies the already lower inherited priority. CPU and wall
limits are 120 seconds. No hard memory cap is claimed; measured usage
and fixed small arithmetic sizes are far below 1 GiB.

The initial literature check found no full solution changing the task.
Opened sources and the proof-tool references are recorded in LOG.md
and PROOF.md. No exhaustive search or literature-priority claim is made.

What failed or remains uncertain: initial product ordering is not an
invariant and cannot replace strict-saddle avoidance. Nothing here
trains the fixed zero entries or value maps, treats d>1 or softmax, or
handles discrete or stochastic training. No uniform training-time bound
is established. The unrestricted T325 problem remains unresolved here.
All writes stayed in this folder; no git, subagents, external writes,
or numerical model training were used.

Next worker: prove a discrete population-gradient-descent version for
these same 2L factors, first with initialization supported in a fixed
bounded set and a uniform sufficiently small step size eta. The exact
one-step identities are

    D_i,new=D_i(1-eta^2 F_i^2),
    a_i,new=a_i-eta(k_i^2+q_i^2)F_i+eta^2 a_i F_i^2.

If eta|F_i|<=1 then |D_i| cannot increase. Combine this with loss descent
and the product-space compact sublevels to construct an invariant
bounded factor region. A Hessian bound on a slightly larger region
can supply a uniform step size, local invertibility, and saddle
avoidance; verify all those conditions rather than importing the
continuous-time invariants unchanged.

Task: “take the NEXT checkable step on this problem, building on that work.” — 15 November 2026, 09:12 Asia/Tbilisi.
