VERDICT: PROVED TW1 with deterministic finite-size centering for the projected spherical kernel with arbitrary quadratic Hermite coefficient

The round 4 result holds on independent rechecking. This session proves
its proposed next step. Assume independent spherical input columns of
radius sqrt(d), independent standard Gaussian weights, a fixed Lipschitz
activation with a_0=a_1=0 and variance v>0, N/d tending to a positive finite
limit, and b_N=m/N tending to b in (0,infinity), b!=1. For

    K_P=Y(I-ee^T)Y^T/N,    e=(1,...,1)^T/sqrt(N),

the conclusion is

    [b_N^(1/6)/(v(1+sqrt(b_N))^(4/3))] N^(2/3)
       [lambda_max(K_P)-v(1+sqrt(b_N))^2] => TW_1.

Thus lambda_max(K_P) converges in probability to v(1+sqrt(b))^2. There
is no restriction on q=a_2^2. In particular this includes the critical
and supercritical quadratic-spike regimes excluded by round 4. This is
a theorem for an explicitly projected kernel; the full T248 problem
remains open.

The complete proof is in [PROOF.md](PROOF.md). In dimension M=N-1, the
conditional covariance is

    T=(v-q/d)I_M+q Q^T B Q+Q^T R Q,

where Q is any deterministic orthonormal basis of e^perp. The constant
quadratic spike disappears, so ||T-vI||_op=o_p(1) for every q. Projection
loses exact trace cancellation: the trace defect is

    Tr(T-vI)=-q(N-1)/d+o_p(1).

The new deterministic edge lemma retains this bounded trace defect and
the bounded squared Hilbert–Schmidt defect. It gives an O_p(N^-1)
conditional edge displacement, negligible at the TW scale. The proof
handles the singular ambient projection by working on e^perp, verifies
uniform concentration and edge regularity, and removes conditioning.

The universality input remains Corollary 1.4 of Guangchen Chen and Xing
Lyu, *Tracy–Widom law for sample covariance matrices under quadratic form
concentration*, [arXiv:2610.41416v2](https://arxiv.org/html/2610.41416v2).
It is used as stated, not independently reproved. The five-minute web
search found no newer full solution; no SOLVED_ELSEWHERE.md was created.

Commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T248/verify_subcritical.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B verify_projection.py
```

All checks passed. The new [verification script](verify_projection.py)
checks exact rational projection, trace and Frobenius identities;
independently checks the predecessor's circle moments by Fourier
integration; checks a bounded cosine activation's covariance two ways;
and checks the nonzero-trace edge lemma with two independent scalar
solvers. The solvers agree within 1.776e-15. Three normalization formulas
agree within relative error 2.220e-16 for the scale and absolute error
3.553e-15 for the center, in both rectangular orientations. These are
algebra checks, not numerical evidence of a TW limit. The new script
took 0.026 seconds and used 13.8 MiB peak RSS. Full output is in
[LOG.md](LOG.md).

What failed or remains uncertain: replacing the projected trace defect
by zero would be wrong. The general covariance-edge lemma must allow
negative edge corrections; no sign is claimed for the network's correction.
Interlacing cannot transfer this result to lambda_2(YY^T/N); the script
exhibits an order-one gap in a deterministic rank-one example. No sample
outlier law or original-model eigenvalue sticking estimate is proved.
Linear components, random column norms, non-Lipschitz polynomials and
b=1 remain outside the result. Replacing b_N by b in the center still
requires an additional convergence rate. There is no unresolved proof
gap identified within the stated projected model, conditional on the
cited universality theorem.

The launcher printed a priority-adjustment warning. Both numerical runs
passed their effective-priority guards; the new run measured nice value
20. Thus all computations ran at the requested low effective priority.
All writes stayed in this folder. No git, subagents or external writes.

Next worker: in the strictly supercritical regime q alpha sqrt(b)>v,
prove edge sticking between lambda_2(YY^T/N) and lambda_1(K_P), ideally
their difference being o_p(N^-2/3). Start from the exact rank-one identity
K=K_P+aa^T, a=Ye/sqrt(N), and its secular equation. The missing estimate
must control the dependence of a on K_P and the secular denominator near
the bulk edge. A rank-one interlacing argument or population covariance
norm estimate alone is insufficient. Treat a critical spike separately.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first clock reading 08:52:40 +04.
