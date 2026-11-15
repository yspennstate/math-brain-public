# T347 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Start: 15 November 2026, 06:32 +04.

## Orientation and bounded update check

Read both earlier REPORT.md and LOG.md files and the round-3 PROOF.md,
audit_landscape.py and audit_blocks.py. The first folder has neither
PROOF.md nor mathematical scripts. Read the startup memory and compute
state: warn/cpu_saturated, owner_away_open. Runs will be small and use one
thread; no agents or git. The explicit instruction to write only here
precludes mesh/checklist/brain commands that log outside this folder.

Web searches: Hopfield critical capacity Zhou 2026; Free energy of the
Hopfield model 2611.03306; Hopfield 0.138 rigorous capacity proof 2026.
Opened https://arxiv.org/abs/2611.03306 and its v1 HTML, and
https://hexagonmath.org/2611.00105v1 and its PDF. Both still show only v1.
The capacity paper defines capacity by a well in a constrained limiting
profile, rather than an iff about individual local minima. No newer
solution of the stated problem was located. Update check ended 06:33 +04,
within five minutes. No SOLVED_ELSEWHERE.md is warranted.

The original report's scope distinction is maintained; the round-3
finite and asymptotic certificates will now be checked independently.

## Independent recheck of the round-3 result

Added and ran `recheck_previous.py`, reading the previous certificate
without modifying it. It computes every shell maximum from the weighted
cut identity Q(s)=Q(1)-4 sum_{i negative,j positive} A_ij, independently
of the earlier projection and quadratic-form enumerations.

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 recheck_previous.py`

Output:
```
base cut enumeration: [192, 236, 256, 284, 288, 300, 304]
fields: [9, 9, 1, 9, 25, 1, 5, 5, 25, 5, 13, 1]
Walsh actual Gram, all 65536 states, all flips near 22 patterns: PASS
minimum energy increase: 8 / 32
priority: 20
elapsed_seconds: 0.243
```

The new Walsh check uses K=2, B=4, N=16 instead of the earlier verifier's
K=4, B=2, N=18. Checked every actual Gram entry and every single-spin
flip of the minima near every pattern. The finite-volume barrier lemma
also holds: a cap minimizer cannot lie on its boundary if an interior
shell has strictly lower minimum energy. The prior asymptotic profile
bounds and positive flip costs follow from its block-diagonal Gram
identity. No error in the earlier result was found.

The nice warning is the sandbox rejecting an increase from inherited
niceness 20 to 15. The actual priority is 20, lower than the requested
priority, throughout.

## ONE selected extension, before the new calculation

Remove the flat-profile limitation of the correlated counterexample.
Construct distinct binary patterns whose limiting shell ground-state
profile is strictly decreasing at every positive overlap with a stored
reference, while that reference is itself a strict single-spin minimum
with a nonvanishing stability margin. The round-3 report explicitly
leaves this strict-decrease case open. This isolates what an iid upper
bound must use beyond monotonicity of the limiting profile.

Candidate: B repeated neurons per block, K Walsh blocks, the constant
Walsh pattern once, and each nonconstant Walsh pattern with both signs.
The actual patterns are distinct, although many are antipodal and they
are highly correlated. Their proposed Gram matrix is
2K times the block-identity matrix minus the all-ones matrix. Its
negative global-magnetization term should produce a strictly decreasing
profile, while within-block coupling should preserve single-spin minima.
All identities, shell optimizers and stability claims will be proved
and independently enumerated before reporting a result. This is one
landscape extension, not an iid capacity theorem.

## Exact construction proved and checked

Wrote PROOF.md. With K=2^q, N=BK, M=2K-1, the Gram identity is
A_{(z,l),(w,t)}=2K*1_{z=w}-1. Thus Q=2K sum_z S_z^2-S^2.
At distance d from the constant stored reference, with r=d mod B,
the exact shell profile is

E_N(d)=1-m_d^2/2-4K*r*(B-r)/N^2.

The error from E(m)=1-m^2/2 is uniformly <=1/K, and E strictly
decreases on [0,1]. At the same time, precisely the 2^K block-uniform
states are local minima, all strict, with every flip costing at least
2(1-M/N). Every stored pattern is one of these minima. The strict
decrease assertion concerns the constant reference; it is not claimed
for all stored references. B>=3 makes the limiting flip margin positive.

Added audit_strict_profile.py, using only Python integers and Fractions.
Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_strict_profile.py`

Output:
```
priority 20
OMP_NUM_THREADS 1
K=2 B=3 N=6 M=3: all 64 states, actual Gram, profiles, all neighbors PASS; minima=4; min_flip=1; uniform_error=4/9
K=4 B=3 N=12 M=7: all 4096 states, actual Gram, profiles, all neighbors PASS; minima=16; min_flip=5/6; uniform_error=2/9
K=4 B=4 N=16 M=7: all 65536 states, actual Gram, profiles, all neighbors PASS; minima=16; min_flip=9/8; uniform_error=1/4
K=16 B=14 N=224 M=31: every stored pattern strictly stable by actual projections; all 225 shell optima match separate DP
finite_load 31/224 = 0.13839285714285715
finite_min_flip 193/112 = 1.7232142857142858
limiting_load 1/7 = 0.14285714285714285
limiting_min_flip 12/7
one-block-path_max_excess 25/7 continuous_upper_bound 112/31
boundary B=1 K=4 reference flip cost=-3/2
boundary B=2 K=4 reference flip cost=1/4
elapsed_seconds 0.547
```

The exhaustive checks compare every actual pattern-projection energy
with the block formula, then use actual neighbor energies to count all
local minima. Each shell optimum agrees with both the closed formula
and a separate dynamic program. The larger instance checks actual
projections at every stored pattern and direct energy flips at selected
coordinates. The theorem itself is algebraic, not an extrapolation.

## Attempts to break the result and resource audit

Re-derived the reference flip cost without the Gram-field calculation:
the reference has projections (N,0,...,0), whereas its one-flip neighbor
has first projection N-2 and M-1 projections of absolute value 2.
Their Q difference is 4(N-M), again giving energy cost 2(1-M/N).
The direct enumeration and the local-field proof give the same count
2^K of minima. The exact shell maximum is checked by both exhaustive
projection enumeration and a separate block dynamic program.

Checked the boundary shells d=0,N and the residue r=0 (whole-block
flips), and tried B=1 and B=2. B=1 makes the reference unstable;
B=2 keeps it strictly stable at finite K but its margin tends to zero.
Thus B>=3 is necessary for the asserted positive limiting margin in
this family. K>=2 is used for the strictly lower energy after reversing
a whole block. All patterns are distinct as sign vectors, but nonconstant
patterns occur in antipodal pairs; no independence or exchangeability
is asserted.

Sign/scale audit: E_N=-min H/N. The limiting E decreases as positive
overlap increases, while a single flip from the reference lowers E_N.
Indeed E_N(1)-E_N(0)=-2(N-M)/N^2<0, even though the limiting profile
evaluated at the two overlap grid points has the opposite ordering.
The uniform error O(1/N) is large enough to change adjacent-shell
differences, also of order 1/N. This is the obstruction, not a
normalization change. Reversing an entire block lowers total energy
by 2B(1-1/K) after an initial uphill cost. Equation (7) gives a bounded
energy barrier along this path, consistent with the normalized limit.

For B=14, counting patterns gives (2K-1)/(14K)->1/7 independently of
decimal printing; the margin limit is 2-4/14=12/7. For K=16 this gives
31/224 and 193/112, agreeing with actual projection energies. The
one-block path maximum 25/7 is below its continuous bound 112/31.

Added a peak-RSS print and repeated the audit solely to measure the
resource limit. The same command passed with identical mathematical
output, peak_rss_MiB=14.375 and elapsed_seconds=0.524. The scripts use
the standard library, no worker threads, and 120/180-second alarms.
No verification failed. The nice warning is the only execution warning.

## Final scope and handoff

No iid existence/exclusion estimate or replica-symmetry theorem was
obtained. Only the all-positive stored reference is asserted to have a
strictly decreasing limiting profile; every stored pattern is asserted
to be a strict minimum. The construction is a counterexample to a
deterministic landscape inference, not to T347. The recent variational
and merging results and interval certificates remain unaudited here.

Next: formulate and prove an iid-specific estimate excluding simultaneous
zero-diagonal stability inequalities within a precisely specified error
cap. Uniform monotonicity of the normalized shell profile, without
control of its local errors or of configurations suboptimal on a shell,
cannot be the entire argument. Use the present example as a check on
any proposed deterministic reduction.

Wrote REPORT.md. All deliverables are in this folder; previous folders
were read only. No git, subagents, outside-folder writes or publications.

Final file audit: read REPORT.md's first line and checked the deliverables
for TODO/FIXME markers and stale timing text; none found. Confirmed all
five deliverables exist here. The report's first line has the required
VERDICT format.
