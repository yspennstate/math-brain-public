# T222 work log

Task: "take the NEXT checkable step on this problem, building on that work."
Received 2026-11-15 approximately 05:02 Asia/Tbilisi. All writes stay here.
No git, subagents, shared mesh/checklist writes, or external messages.
The task-specific confinement overrides the global requests to write to
those shared stores. Read the startup memory and memory index directly;
did not run recall, which logs outside this folder.

## Reads and bounded status check, 05:02–05:04

Read REPORT.md, LOG.md, PROOF.md and AUDIT.md in both earlier folders:
`~/codex_op_1114/briefs/T222` and
`~/codex_op_1114r3/briefs/T222`.
`rg --files ... -g '*.py' -g '*.sh'` found no mathematical scripts.
Also read `~/.claude/brain_startup.md`, the startup
memory index, and the compute state. Governor: warn, owner_away_open,
CPU saturated. No numerical computation is planned.

Shell reads after the initial inventory used
`env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '...'`.
The sandbox prints `nice: setpriority: Operation not permitted` and then
runs the short read. Priority adjustment is not verified. The initial
inventory omitted the prefix; it only listed/read files. No heavy program
will be run under this limitation.

Web search tool queries, completed in under five minutes:

- `"Euclidean traveling salesman" "variance" convergence Steele 2025 2026`
- `"Steele" "variance" "conjecture" traveling salesman`
- `"traveling salesman" "variance limit" 2026`
- `"Euclidean" "TSP" "variance convergence"`
- `"Steele" "variance" "limit" travelling salesman`

Opened Sourav Chatterjee, *A general method for lower bounds on
fluctuations of random variables*, arXiv:1706.04290v3,
https://arxiv.org/html/1706.04290v3. Its Section 3, problem (2), still
states the exact variance-limit question (line 732 in the tool rendering).
The TSP discussion recalls Rhee's planar lower fluctuation bound.
No closing theorem found. Search snippets for other papers are not treated
as opened references. No SOLVED_ELSEWHERE.md is warranted; this was a
bounded update check, not an exhaustive review.

## Independent verification before choosing the extension

For a fixed deleted sample S, let d(x;S)=T(S union {x})-T(S).
The Hoeffding residual identity gives
`E_n = sum_j j V[n,j] = n E Var_X(d(X;S) | S)`.
Independently, a replacement pair gives twice this conditional variance,
checking the factor n and the absence of another factor two.
The detour-and-shortcut argument gives `0 <= d <= 2R`.
With Z_n=sqrt(n)R and H_c(z)=max(c^2,(2z-c)^2), conditional centering
gives E_n <= E H_c(Z_n). The square's homothetic area bound supplies
P(Z_n>r | x)<=exp(-r^2/4). Interior disk areas give the limiting tail
exp(-pi r^2). Hence E H_c(Z_n)->F(c).

Recomputed F independently from W=pi Z^2, which is exponential:
E[W 1_(W>a^2)]=(a^2+1)exp(-a^2), and
E[sqrt(W) 1_(W>a^2)]=a exp(-a^2)+(sqrt(pi)/2)erfc(a).
For a=sqrt(pi)c, these give
`F(c)=c^2+(4/pi)exp(-pi c^2)-2c erfc(sqrt(pi)c)`.
The threshold derivative gives F'=2c-4 E[Z 1_(Z>c)] and
F''=2+8pi c^2 exp(-pi c^2)>0. Thus the previous minimizer and
bound limsup E_n<=kappa hold. No error found in either earlier result.

## ONE extension chosen before proof

Prove a strict improvement of the asymptotic interaction-energy bound by
using spatial continuity of the insertion cost. The function x->d(x;S)
is 2-Lipschitz. The scalar extremizer in round 3 jumps from 0 to 2R at
R=c, so it cannot describe this spatial function. Around many isolated
base points, compare two small equal-area disks on opposite sides of
that threshold. Their preferred scalar endpoints are too far apart for
a 2-Lipschitz function. Quantify the integrated squared-error deficit and
average over isolated points. This requires no localization of optimum
tour changes and extends the previous constant rather than claiming any
fixed-order convergence.

Candidate explicit deficit (to be audited):
`eta(c) = (27*pi*c^4/16384) exp(-9*pi*c^2)`.
Target: limsup E_n <= F(c)-eta(c) for each fixed c>0, hence at c=c_*
a strict improvement of kappa. The two disks have radii c/16 and centers
at distances 3c/4 and 5c/4 from an isolated site in scaled coordinates.
Isolation radius 3c makes the nearest site known on both disks and keeps
different sites' disk pairs disjoint. Full details belong in PROOF.md.

## Geometry simplified before saving the proof

Use disks of radius c/8 with centers 5c/8 and 11c/8 along a fixed
direction from the isolated site. Then their nearest-distance ranges are
[c/2,3c/4] and [5c/4,3c/2], and any two points in opposite disks are
at most c apart. The Lipschitz difference is at most 2c, while the
preferred endpoint separation is at least 5c/2. Both squared-error
deficits have linear coefficient at least c/2. Their sum is therefore
at least c^2/4. Each disk has scaled area pi c^2/64. This improves the
candidate deficit to `eta(c)=(pi*c^4/256) exp(-9*pi*c^2)`.
The isolation radius remains 3c. This is the same chosen extension.

## Proof saved

Saved PROOF.md with the deterministic two-disk deficit, the exact expected
number of admissible sites, the finite-sample bound (19), and its limiting
consequence. The theorem is
`limsup E_n <= F(c) - (pi*c^4/256)exp(-9*pi*c^2)` for fixed c>0.
At the earlier minimizer this is strictly below kappa. Boundary handling
is explicit: use sites at least 3c/sqrt(n) from every side. Their excluded
area vanishes. Different admissible sites' radius-3c/(2sqrt(n)) disks
are disjoint, so there is no counting factor or independence assumption
between the admissibility events.

Next audit: re-derive the local constant by a translation pairing rather
than integrating all pairs; check the isolation count by a binomial/Palm
calculation; check (6) by a different route; try endpoint and boundary
cases, n=2, and artificial Lipschitz fields. No numerical run is needed.

## Independent audit completed

Saved AUDIT.md. A detour-and-shortcut argument independently proves
2-Lipschitz continuity. A translation pairing of the two disks actually
gives a local loss pi c^4/(128n), validating the conservative
pi c^4/(256n) used by the all-pairs proof. No optimality of this constant
is claimed. Kept the all-pairs constant and proof, whose bound holds for
every pair without selecting a correspondence.

Recomputed the expected count by a joint-density integral, and checked
all n factors by measuring the probability an independent query lies in
one of the disjoint disk pairs. The exponent is n-2, not n-1; the count
is n-1, while the energy scale is n. These agree with (18) and (19).
The margin, overlapping-support obstruction, n=2, coincident locations,
and the two endpoint fields all pass. The interval-only discontinuous
scalar extremizer fails the Lipschitz constraint, as required.

Magnitude check: eta(c)/c^2=t exp(-t)/2304<=1/(2304e), t=9pi c^2,
and F(c)>=c^2. The upper bound stays positive. No variance convergence
or variance-limit value follows; this remains the outstanding obstacle.

Read-back command:
`env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c 'cat PROOF.md; cat ~/.claude/compute/compute_state.json; date "+%Y-%m-%d %H:%M:%S %Z"'`
returned exit 0, with the same setpriority denial. Compute state remained
warn, owner_away_open, CPU saturated. Only short file reads were run.

## Final artifact check, 2026-11-15 05:10:04 Asia/Tbilisi

Wrote REPORT.md with the required first line and the exact theorem,
limitations, commands, and next target. Read back AUDIT.md and REPORT.md,
searched the four artifacts for constants, isolation radii and counting
exponents, and checked file lengths. Command:

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
cat AUDIT.md
cat REPORT.md
rg -n "256|n-2|3c/|VERDICT|eta|c_" PROOF.md LOG.md REPORT.md AUDIT.md
wc -l LOG.md PROOF.md AUDIT.md REPORT.md
date "+%Y-%m-%d %H:%M:%S %Z"
'
```

Exit 0; the priority denial persisted. Counts before this append:
LOG.md 140, PROOF.md 331, AUDIT.md 164, REPORT.md 101. The report's
first line is `VERDICT: PARTIAL a strict geometric improvement of the earlier interaction-energy bound`.
The initial candidate 27*pi/16384 appears only in the chronological log
and is explicitly superseded there by pi/256. The proof, audit's stated
theorem constant, and report all use pi/256. The stronger translation
audit is explicitly distinguished from that constant. No correction was
needed. Completed the one chosen extension and its independent audit;
the original variance-limit conjecture remains unresolved here.
