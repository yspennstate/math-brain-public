# Exact edge-diversion comparison on the four-site square

## Statement

Let
\[
V=\{(0,0),(1,0),(0,1),(1,1)\}
\]
with vertices numbered 0, 1, 2, 3 in that order. An active particle jumps at rate 1 in a uniformly chosen lattice direction. A particle that is alone falls asleep at rate 1. A jump outside V removes the particle. Arrival at a sleeping particle wakes it.

There are eight directed internal edges, in this order:
\[
(0,1),(0,2),(1,0),(1,3),(2,0),(2,3),(3,1),(3,2).
\]
For a subset M of these edges, redirect each edge in M to the sink. Retain the original jump-direction probabilities: every vertex still has four jump slots, of which at least two go to the sink. In particular, deleting an edge does not renormalize the other probabilities.

Let S_M be the number of sleepers in the stationary law of the chain that adds an active particle at a uniformly chosen vertex and stabilizes. The finite computation establishes
\[
S_M\succeq_{\mathrm{st}} S_{M\cup\{e\}}
\qquad(e\notin M)
\]
for every M and e. There are 256 kernels and 1024 comparisons. Consequently the same ordering holds whenever M is contained in a larger deletion set, by following a sequence of single-edge deletions.

This is a finite statement at sleep rate 1. It makes no assertion about growing boxes or the infinite-volume critical density.

The motivation is the edge-diversion question in Section 2.5 of Nicolas Forien, [*A new proof of superadditivity and of the density conjecture for Activated Random Walks on the line*, arXiv:2502.02579v2](https://arxiv.org/html/2502.02579v2).

## Finite states and absorption

A local state is 0 (empty), -1 (one sleeper), or a positive integer (that many active particles). Define the particle count of -1 to be 1. A configuration is stable exactly when every coordinate is 0 or -1. There are sixteen stable configurations, identified by their sets of occupied vertices.

Both computations below use only configurations with at most five particles. Four particles suffice to stabilize the initial configuration (1,1,1,1). Five suffice when adding one particle to any stable configuration, as required for the stationarity check. Thus the state space is finite, without a cutoff on the true dynamics.

Absorption occurs almost surely, for both schedules below. At any transient state there is an active site. In the instruction schedule, the next instruction at the selected active site is a sink jump with probability at least 1/4. In the continuous-time embedded chain, if A is the active population and r is the number of lone active particles, the sink-jump rate is at least A/2, while the total rate of non-null events is A+r, at most 2A. Its next event is therefore a sink jump with probability at least 1/4 as well. Each such event reduces the total population by one. A sequence of at most five sink jumps reaches a stable state. Conditional on any transient history, absorption in the next five events thus has probability at least 4^(-5). Iterating this bound proves absorption and uniqueness of the Dirichlet solution.

## First computation: instruction schedule

At each transient configuration select the lowest-numbered active vertex. Read one instruction there: sleep with probability 1/2, or each of its four jump slots with probability 1/8. A sleep instruction at a site with two or more active particles does nothing. A jump removes one active particle from the selected site; at an occupied sleeping destination it produces two active particles.

For every deletion mask, `exact_square.py` enumerates all transient states reachable from (1,1,1,1). It assigns integer weight 4 to sleep and weight 1 to each jump slot, combining repeated destinations. Let w(s,t) denote these weights and D_s their sum. For k=0,...,4, the probability f_k(s) of absorption with k sleepers satisfies
\[
D_s f_k(s)-\sum_{t\text{ transient}}w(s,t)f_k(t)
=\sum_{t\text{ stable}}w(s,t)\mathbf1\{|t|=k\}.
\]
These are integer-coefficient linear equations AX=B. The script solves them by exact fraction-free elimination, and checks the integer residual AX_num=X_den B. It also checks nonnegativity and normalization of the probability row for every reachable transient state.

The initial row gives the candidate law for each mask. No floating-point arithmetic enters these probabilities.

## Second computation: continuous-time dynamics

The independent audit uses the actual continuous-time generator, without choosing a preferred active site. Multiply all rates by 4. At a site with m active particles, each jump slot has weight m. If m=1, sleep has weight 4. If m>1, no sleep transition is included. These rates are exactly the specified ARW dynamics, with null sleep attempts omitted.

This computation enumerates the transient states reachable from (1,1,1,1) and from each of the 64 configurations obtained by adding a particle at one of four vertices to one of sixteen stable configurations. Its right-hand sides distinguish all sixteen stable absorbing configurations, rather than just their particle counts.

The audit solves these equations with a separately implemented dense Gaussian elimination using only Python `Fraction` arithmetic. It rechecks every equation against the original coefficient matrix. The absorbing law from (1,1,1,1), grouped by particle count, agrees exactly with the first computation for every one of the 256 masks. Thus the result does not require assuming that the preferred-site schedule has the same absorption law as the continuous-time dynamics.

## Identification with the driven stationary law

For a fixed mask, let pi be the full stable-configuration law obtained by the continuous-time audit from (1,1,1,1). For each vertex i, let P_i(a,b) be the absorbing probability of configuration b after adding one active particle at i to stable configuration a. The audit obtains every row of every P_i from the continuous-time Dirichlet equations just described, and checks the sixteen identities
\[
\sum_a\pi(a)P_i(a,b)=\pi(b)
\]
for each i. Hence pi is invariant under uniform driving, and indeed under any mixture of the four single-site addition kernels.

For completeness the uniformly driven chain has a unique stationary law for every deletion mask. From any stable state, choose the successive addition sites to be 0,1,2,3. At each site arrange for the added particle and any sleeper there to jump directly to the sink, without visiting another vertex. Each required event has positive probability, since every vertex has at least two sink slots. This reaches the empty state in four additions with positive probability. Starting from the empty state, a further four additions, one at each vertex, can create any prescribed stable configuration: require immediate sleep at a desired occupied site and an immediate sink jump at a desired empty site. Again the event has positive probability. Therefore the eighth power of the uniformly driven transition matrix has all entries positive. The finite chain has a unique stationary law, which must be pi.

## Exhaustive stochastic-order check

For a deletion mask M let p_M(j)=P(S_M=j). Since the possible values are 0,...,4, stochastic domination is equivalent to the four inequalities
\[
\sum_{j=k}^4p_M(j)-\sum_{j=k}^4p_{M\cup\{e\}}(j)\geq0,
\qquad k=1,2,3,4.
\]

The main program checks these inequalities for every missing bit e of every eight-bit mask M. The count is 8 times 2^7=1024 comparisons and 4096 tail inequalities. All are nonnegative: 1792 are zero and 2304 are positive. The data-only verifier independently enumerates all ordered mask pairs differing by one bit, and recomputes each difference using lower cumulative probabilities instead of upper tails. It also verifies all 2048 combinations of a deletion mask and a dihedral symmetry of the square. Exact laws, full configuration laws from the second computation, and the comparison summaries are in `square_data.json`.

## Hand calculation of a disconnected case

Redirecting the four vertical directed edges corresponds to mask 90. It leaves two independent reciprocal two-site components. In either component a jump goes to the other vertex with probability 1/4 and to the sink with probability 3/4.

Write e_j for unit probability on a final population of j. Let D be the final-population law from one active particle and one empty site; A the law from two active particles on different sites; B the law from two active particles on the same site; and C the law from a sleeper and an active particle on different sites. Symmetry identifies the two possible orientations of each state.

For D, the next event is sleep with probability 1/2, a jump to the other site with probability 1/8, and removal with probability 3/8. Therefore
\[
D=\tfrac12 e_1+\tfrac18D+\tfrac38e_0
=\tfrac37e_0+\tfrac47e_1.
\]
For B no sleep can succeed, and the next jump gives
\[
B=\tfrac14 A+\tfrac34 D.
\]
For C the next event concerns its unique active particle, giving
\[
C=\tfrac12e_2+\tfrac18B+\tfrac38e_1.
\]
Finally, symmetry of the two active sites in A gives
\[
A=\tfrac12C+\tfrac18B+\tfrac38D
=\tfrac14e_2+\tfrac3{16}e_1+\tfrac3{16}B+\tfrac38D.
\]
Substituting B yields
\[
\tfrac{61}{64}A
=\tfrac14e_2+\tfrac3{16}e_1+\tfrac{33}{64}D,
\qquad
A=(99,216,112)/427.
\]
The generating polynomial for two independent components is the square of that for A. Thus
\[
\bigl(p_{90}(0),\ldots,p_{90}(4)\bigr)
=\frac{(9801,42768,68832,48384,12544)}{182329}.
\]
The data-only verifier checks this hand-derived vector against the computed law. When all eight edges are redirected, each vertex separately ends sleeping with probability 1/2. Independence gives Binomial(4,1/2), another checked boundary case.

For reference, the unmodified square has law
\[
\left(
\frac{4101320}{96025977},
\frac{61478038}{288077931},
\frac{109407745}{288077931},
\frac{190576}{665307},
\frac{140}{1803}
\right),
\]
and mean 205775624/96025977. In particular, this square stochastically dominates the independent sum of the stationary populations of its two isolated rows, with all four tail inequalities strict. This last statement is also checked directly in `verify_square_data.py`.

## Reproduction

Run from this folder, using Python 3 with SymPy installed:

```
OMP_NUM_THREADS=1 nice -n 15 python3 exact_square.py --audit-all --output square_data.json
OMP_NUM_THREADS=1 nice -n 15 python3 verify_square_data.py
```

The first command includes both exact solvers and all stationarity checks. The second uses only the standard library and the saved data. Neither program uses random samples.
