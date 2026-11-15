# T075 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded clock: 2026-11-15 03:57:34 UTC (07:57:34 +04:00).

## Scope and startup

All writes stay in this folder. No git, subagents, external messages, or
shared mesh/checklist/brain writes: the task-specific restriction on writes
elsewhere takes precedence over the global instructions for those writes.
Read the startup MEMORY.md and compute_state.json. The latter reports
warn / owner_away_open and saturated CPU. Only short, single-threaded,
small-memory computations are planned. Shell programs are launched with
OMP_NUM_THREADS=1 and nice -n 15. The inherited priority is already 20;
nice prints “setpriority: Operation not permitted”, as in the prior runs.

## Prior work and bounded literature check

Read REPORT.md and LOG.md in all three prior folders; read both existing
PROOF.md files and both scripts. The original folder has no PROOF.md or
scripts. Prior folders were read only.

Within the first two minutes, used the web search tool for:

- Bernoulli convolutions transcendental absolute continuity 2026 Kittle Kogler
- "2611.17277" Bernoulli
- "Bernoulli convolutions" "transcendental" "November" "2026" absolute continuous
- "Bernoulli convolutions" "absolute continuity" "solved" "2026"

Opened the following actual paper pages:

- Samuel Kittle and Constantin Kogler, *On L^p density of self similar
  measures and Bernoulli Convolutions*, arXiv:2611.17277v1,
  https://arxiv.org/html/2611.17277v1 . Theorem 1.1 assumes absolute
  continuity. Its explicit parameter theorems concern algebraic parameters.
- Samuel Kittle and Constantin Kogler, *The Exact Overlaps Conjecture for
  Self-Similar Measures on the Real Line*, arXiv:2610.10511,
  https://arxiv.org/abs/2610.10511 . Its stated conclusion is dimension.
- Guozheng Cheng, Xiang Fang, Xueqing Ma and Hongli Zhang, *Strict
  Hausdorff-dimension drop for Quartic Salem Bernoulli convolutions*,
  arXiv:2610.12072, https://arxiv.org/abs/2610.12072 .

No subsequent solution of T075 was located. This is a bounded search, not
an exhaustive literature claim. No SOLVED_ELSEWHERE.md is warranted.

## Independent recheck of the earlier result

Re-derived the round-4 recurrence: critical intervals of average ct cover
the high-level set with multiplicity two; their doubled intervals have
average at most ct. The small-set implication bounds the high-level mass
by 2c theta t times their total length. Splitting at height t bounds that
total length by 2F(t)/((c-1)t). Thus the multiplier is
4c theta/(c-1), exactly as reported. The contraction condition is
c>1/(1-4theta), and layer cake requires the strict inequality
[4c theta/(c-1)] [c/epsilon]^(p-1)<1. The earlier claim holds.
The two interval multiplicity factors refer to the original intervals;
there is no assumption of bounded multiplicity for their doubles.

The prefix-to-measure step also holds: weak convergence and pure type
give the qualitative criterion; a compact set of length at most delta/2
has an open neighborhood of length below delta, giving the required
small-set modulus. No finite-depth propagation follows from these steps.

## Choice before extension

Prove an obstruction to a propagation lemma based only on finitely many
small caps. The earlier singular control lambda=1/3 is outside T075's
interval. Instead use reciprocals of multinacci Pisot numbers, which are
singular and approach 1/2 from above. Aim to prove an explicit bound

    A_n(delta) <= min(delta/4,1) + (n+1)(2lambda-1),

by a total-variation telescoping argument, and combine it with an explicit
multinacci root bound. This will show that arbitrarily long initial
segments can pass any fixed cap threshold above delta/4 at singular
parameters in (1/2,1). It does not refute T075, whose parameters are
transcendental, or a propagation lemma using additional information.
Give a self-contained Pisot/Fourier argument and check the constants in
two ways. This is the one extension selected for this session.

## Recheck output and improved bound

Command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T075/check_constants.py > earlier_recheck.txt 2>&1
```

Exit 0. Reproduced 4,943 interval families, 12 exact caps, 18 recurrence
cases and the 1,000-point exponent comparison. The example exponent is
1.130236012180298. Runtime 0.120 s; peak RSS 22,233,088 bytes; priority 20.

The proposed telescoping bound has a sharper and simpler version. Keep
the reference uniform law on the parameter's own support [-R,R]. Its
one-step total variation defect is exactly

    d(lambda) = (2lambda-1)(1-lambda)/lambda.

Markov contraction and telescoping give

    TV(mu_n, uniform[-R,R]) <= n d(lambda),
    A_n(delta) <= min(1, delta(1-lambda)/2 + n d(lambda)).

For 1/2<lambda<1, d(lambda)<2lambda-1, so the simpler consequence is
A_n(delta) <= min(1,delta/4+n(2lambda-1)). No n+1 is needed.
The factor-of-two convention is TV=sup_E|mu(E)-rho(E)|=half the L1
distance for densities. Check it by integrating the positive and negative
parts of the one-step defect separately.

## Proof and computation saved

Wrote PROOF.md. It proves the total variation bound and gives a
self-contained multinacci root estimate, a Rouché argument locating all
other roots inside the unit circle, and the Fourier nondecay proof of
singularity. No numerical root approximation is used in that proof.
The cap condition can hold through every depth up to N at a singular
parameter whenever N*2^(-k)<theta-delta/4.

Wrote check_obstruction.py and ran:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 check_obstruction.py > computation.txt 2>&1
```

Exit 0. Full output:

```text
priority 20
OMP_NUM_THREADS 1
exact one-step positive/negative TV and explicit-cap cases 39
exact prefix TV checks 72 cap inequalities 288
maximum TV/(n*d) in grid 1
delta 1/64 theta 1/36 margin 55/2304
k 8 lambda approx 0.500994177922889836854084319392 certified depth 6 threshold gap 1/2304
k 12 lambda approx 0.500061132239058190529572138910 certified depth 97 threshold gap 7/36864
k 20 lambda approx 0.500000238420966560446050421230 certified depth 25031 threshold gap 1/9437184
k 40 lambda approx 0.500000000000227373675447471360 certified depth 26247022364 threshold gap 1/2473901162496
rational root brackets versus independent Decimal Newton 39
WARNING: singular parameters here are algebraic; T075 remains open
WARNING: large certified depths use the theorem, not enumeration
elapsed_seconds 0.717
peak_rss_bytes 17022976
```

The script directly enumerates small sign words, integrates the positive
and negative density differences independently, and compares the exact
cap with both bounds. The n=1 cap is also checked against a separate
two-height formula. The 39 root enclosures use exact rational bisection
for sum(lambda^j)=1, checked against 120-digit Decimal Newton iteration
for sum(beta^(-j))=1 followed by inversion. The large depth certificates
are exact applications of the theorem, not enumeration at those depths.
The script uses the Python standard library, one thread, priority 20,
about 17 MB RSS, and less than one second.

## Attempts to break the result

1. TV normalization: the central positive defect and outer negative
   defect each equal d(lambda); their sum is the full L1 distance 2d.
   Integrating either sign therefore independently recovers the TV
   constant. At n=1 the TV bound is an equality in the exact grid.
2. A second derivation of the telescope uses the density recursion:
   ||f_(n+1)-u||_1 <= ||T(f_n-u)||_1+||Tu-u||_1
   <= ||f_n-u||_1+2d. Induction and division by two give n*d.
3. The proof uses the uniform law on the parameter's own support. Using
   uniform[-2,2] instead would introduce an unnecessary initial error.
   At n=0 the present estimate is exact before the simplified bound.
4. Cap sets may be disconnected. The proof bounds every measurable E
   with its TV distance and constant reference density; the computation
   fills all highest-density segments and does not restrict to intervals.
5. Root location is proved for all roots of P_k, so irreducibility is
   unnecessary. The actual minimal polynomial divides P_k; its other
   conjugates inherit the strict unit-disk bound. The root z=1 belongs
   to Q_k only and is excluded from P_k by P_k(1)=1-k.
6. Nondecay requires every cosine factor to be nonzero, not merely
   summable deficits. A rational positive power of beta would be an
   integer and would equal the corresponding conjugate power of modulus
   less than one, a contradiction. This also excludes rational negative
   powers. The zeroth factor is one. Thus no factor vanishes.
7. Fourier nondecay rules out absolute continuity; pure type is proved
   separately before claiming singularity. The limit A_n(delta)->1 uses
   singularity and weak convergence, rather than a Fourier decay rate.
8. The example's margin is 1/36-1/256=55/2304. A second integer check is
   55*4096=225280=9*25031+1. Division by 9*2^20 independently gives the
   gap 1/9437184. All large integers in the output are rational arithmetic;
   Decimal approximations are only displays and independent root checks.
9. The construction gives a different algebraic parameter for each
   prescribed finite horizon. It does not give one parameter passing
   all horizons, and does not provide a singular transcendental parameter.
   Any proposed propagation theorem explicitly using transcendence or
   quantitative arithmetic information is outside this obstruction.
10. The certificates are sufficient and conservative. No first crossing
    time, optimal horizon, or numerical Fourier lower bound is asserted.

What failed to advance: no upper cap bound on an unbounded sequence at a
specified transcendental parameter was found. The obstruction instead
limits a parameter-uniform finite-data approach to that missing bound.
No novelty claim is made for the classical Pisot argument or the Markov
telescoping inequality.

## Final audit and deliverables

Saved REPORT.md with VERDICT: PARTIAL. Ran an inline read-only audit with
`OMP_NUM_THREADS=1 nice -n 15 python3 -` using ast.parse, file existence
and delimiter checks, exact recomputation of both horizon integers, and
separate positive/negative TV integrals expressed in terms of R and the
overlap length. In particular it checked

    N = (margin.numerator*2**k-1)//margin.denominator,
    N/2**k < margin <= (N+1)/2**k

at k=20 and k=40, and independently integrated the one-step defect at
lambda=51/100, 3/5, 3/4, 99/100. Exit 0. Output:

```text
Final audit passed: deliverables, syntax, delimiters, independent TV integrals and both horizon integers.
Actual priority 20
Deliverable bytes 31643
```

The byte count precedes this log append. No tests remain pending.
Final recorded clock: 2026-11-15 04:05:45 UTC (08:05:45 +04:00).
