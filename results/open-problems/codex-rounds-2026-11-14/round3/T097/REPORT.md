VERDICT: PARTIAL an optimized shell capacity bound and an explicit relative crossover coefficient

The earlier report's Gaussian comparison and its three main consequences
hold under independent verification. No subsequent solution of the lattice
critical-exponent problem was found in the requested brief web check.

The new piece is the exact optimization of its capacity test function over
functions constant on sup-norm shells. For simple-random-walk Green
covariance, PROOF.md proves

    cap(B_R) <= A_R := [sum_{k=R}^infinity (2k+1)^(-2)]^(-1)
                    <= 4R+1/(3R),
    A_R = 4R+1/(3R)+O(R^(-3)).

This improves the earlier explicit bound (28R-1/R)/3 for every R>=1.
The value A_R is optimal within the shell class, not asserted to be the
actual capacity of the cube. Its proof is a finite-annulus quadratic
minimization followed by a positive rational telescoping identity.

For the same relative one-arm radius as in the earlier report,

    L_rel(t) = min{R>=1: p_R(h_*+t)<=p_R(h_*)/2},

the refined comparison and the earlier critical arm bound give

    liminf_{t->0} t^2 log(1/t) L_rel(t) >= (log 2)^2/32.

This replaces an unspecified small constant by an explicit asymptotic
lower coefficient. It uses the existing density theorem of Stephen
Muirhead, [arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), as the
earlier report did. No endpoint density estimate at exponent 4 is assumed.

AUDIT.md independently checks the minimization by Lagrange multipliers,
the coefficients 4 and 1/3 by an integral calculation, the rational
identity by symmetric algebra, and the coefficient 32 by optimized
Holder bounds. It also constructs increasing half-space events on the
same lattice Gaussian marginals for which a probability ratio drops below
1/2 even while t^2 cap(B_R) tends to zero. Thus removing the logarithmic
loss requires information specific to connection events.

Commands and output: no numerical script, simulation or numerical workload
was needed or run. Read-only commands were prefixed with
`OMP_NUM_THREADS=1 nice -n 15`; the sandbox denied the priority change.
Proofs and exact hand calculations are in PROOF.md and AUDIT.md. LOG.md
records the read commands, web queries, findings and final file checks.
All authored files are inside this folder. The earlier folder was read
only; no git, external writes or subagents were used.

What did not follow: the optimized shell profile does not change the power
or logarithmic order of the prior L_rel bound. It gives no connection-event
score improvement and no comparison to a two-point or crossing correlation
length. Exact lattice exponents, their existence, critical nonpercolation,
and agreement with cable exponents remain unresolved. Neither novelty of
these elementary refinements nor optimality of the displayed crossover
coefficient is established.

Next worker: seek a connection-specific bound on

    -d/dh log p_R(h)

near h_* that improves the general Gaussian scale
sqrt(cap(B_R) log(1/p_R(h))). A bound C sqrt(R), uniform for
h in [h_*,h_*+c/sqrt(R)], would remove the logarithmic loss in the lower
bound for this particular relative radius. Alternatively, compare L_rel
to a separately specified conventional correlation length. Further
optimization of deterministic shell functions cannot improve their
leading energy coefficient below 4.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, first recorded local time 01:24:34 +04 (Asia/Tbilisi).
