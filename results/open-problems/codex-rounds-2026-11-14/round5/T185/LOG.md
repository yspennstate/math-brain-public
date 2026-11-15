# T185 continuation log

Task: “take the NEXT checkable step on this problem, building on that work.”
First local clock: 15 November 2026, 08:32:25 Asia/Tbilisi (+04).
Exact receipt time is unavailable.

## Orientation and literature check

Read ~/.claude/brain_startup.md and the compute state: status ok,
owner_away_open, CPU saturated, ample memory. The task-specific rule that
all writes stay here overrides shared brain, checklist and mesh writes.
Those logging commands were not invoked. No git or subagents are used.
The initial read commands omitted nice; subsequent shell programs request
nice 15 and the single-thread environment. The inherited nice priority
will be measured because the wrapper reports a sandbox priority warning.

Read the first session's REPORT.md, LOG.md, PROOF.md and script; round 3's
REPORT.md, LOG.md, PROOF.md and script; and round 4's REPORT.md, LOG.md,
PROOF.md and script. Earlier folders remain read-only.

The literature check used two web calls within five minutes, with queries
including `"alpha-fair" "general file" stability positive recurrence
2024 2025 2026`, `"bandwidth sharing" "general" "positive Harris"
2023 2024 2025 2026`, and Fu/Williams/subcritical/stochastic variants.
Opened Yingjia Fu and Ruth J. Williams, *Asymptotic behavior of a critical
fluid model for bandwidth sharing with general file size distributions*,
Annals of Applied Probability 32 (2022), 1862–1901:
https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf .
This is a critical-fluid result and retains the conditional recurrence
discussion already identified by earlier workers. The 2020 author-PDF
fetch timed out. No later unrestricted stochastic theorem was found;
this brief search cannot certify absence. No SOLVED_ELSEWHERE.md is warranted.

## Independent recheck of round 4

Write q=1-Lambda_0 and Q=integral q. Every occupied local route receives
aggregate q. The exact workload identities give

    -max(w1,w2) <= Delta M-[A0(T)-T+max(A1(T),A2(T))] <= Q.

To check the service-accounting bound, let f_j be the fraction of original
files on each occupied local route. The positive fraction of q not charged
to original service is theta=(1-sum f_j)^+. For each occupied j,
theta <= 1-f_j, so theta*n_j <= new_j. Monotonicity and homogeneity of H
give theta*H(n) <= H(new). If W0(0)>T and residuals are at most one,
n0(t)>=W0(0)-T. Hence

    Q <= w1+w2 + c/[a0*(W0(0)-T)] * integral(A1(t)+A2(t))dt.

The expected area is T^2/2. This recovers round 4's bound and its limiting
d(T)=-3T/10+E|P1(T)-P2(T)|/2. Independently, conditional on the sum of
the two local counts, their difference is a symmetric random walk, whose
variance averaged over that sum is T. Thus d(4)<=-1/5 and the finite-state
constant is -1/5+1/100+8/95=-201/1900. No error found. A copied script
will be rerun here so no output is written into the earlier folder.

## Chosen extension (recorded before proof)

Prove uniform negative fixed-horizon drift of M outside a bounded M-set
in the same deterministic-unit-file two-link network. This is exactly the
next step named in round 4. Include both large local workloads and one
large local workload. If the bound closes, derive recurrence directly by
returning to a bounded-workload set and using a uniform no-arrival emptying
event; do not assume that a workload sublevel is compact in residual state.

Why this piece: local reflection gives an exact upper bound with error
(Q-max(w1,w2))^+. For max(w1,w2)>=T that error is zero. For bounded local
work and large through work, split original local populations at a count
threshold K. The last route to fall below K had at least K original files
throughout the preceding interval, allowing Q on that interval to be
charged to its own initial workload, rather than to the sum of both.
Afterward both original local counts are small and the large through
population controls q. This may remove the remaining bounded-local-work
gap. All claims remain restricted to this topology and unit input files.

## Prior script rerun

Commands (all writes here):

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /bin/cp ~/codex_op_1114r4/briefs/T185/check_sampled_drift.py ./prior_check_sampled_drift.py
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 prior_check_sampled_drift.py
```

Exit 0, `all exact checks passed`: 504 cohort paths, 3,554 events,
d(4) in [-0.428494478548,-0.428494478547], prior constant -201/1900.
Runtime 0.2347 seconds, peak RSS 15,876,096 bytes, actual nice 20,
CPU cap 60 seconds. The copied script writes sampled_drift_checks.json
in this folder. No prior file was modified.

## Candidate bound

For m=max(w1,w2), local reflection gives the pathwise inequality

    Delta M <= A0(T)-T+max(A1(T),A2(T))+(Q(T)-m)^+.

If m>=T the error vanishes. Otherwise assume W0(0)>T and put
R=W0(0)-T. For any integer K>=1, the last original local population to
drop to at most K had more than K original files throughout the preceding
interval. With L=A1(T)+A2(T), its original service fraction was at least
K/(K+L), so Q before that time is at most m*(1+L/K). Subsequently both
original counts are at most K, giving

    Q(T) <= m*(1+L/K) + c*T*(2K+L)/(a0*R).

Thus, for m<T,

    E Delta M <= d(T)+T^2/K+c*T*(2K+T)/(a0*R).

This tends uniformly to d(T) by first taking K large, then R large.
For equal weights, alpha=1, T=4, K=256 and R>=65536, the upper bound is
-1/5+1/16+1/32+1/4096=-2171/20480. Consequently M>65544 should imply
this uniform negative drift. These statements are now being written out
and checked; no recurrence conclusion has yet been certified.

## Complete proof and first verification

Saved PROOF.md. It proves the reflection bound, the count-threshold lemma,
uniform drift for all sufficiently large M, and positive Harris recurrence
for this same unit-file network. The last step does not assume count
compactness: use sampled drift to return to {M<=B}, then try a no-arrival
interval of length D=2B. Total work is at most 2B and aggregate service
is at least one while nonempty. Each trial succeeds with probability
at least exp(-(6/5)D)>0, and expected trial-plus-return duration is bounded.
This gives finite mean emptying time and finite mean regenerative cycles.

New script command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_uniform_drift.py
```

Exit 0, `all exact checks passed`. Output: uniform_drift_checks.json.
672 exact rational cohort paths, 3,733 events, 1,920 threshold-bound
checks, 434 original-cohort departure events, 360 large-local paths.
There are 230 paths with Q(T)>m and 72 with positive empty time. These
last two tests rule out silently assuming Q<=m or that the network never
empties. The paths include no through files, either local alone, both
locals, original counts on both sides of K=256, new counts greater than
K, simultaneous and late arrivals, huge counts with tiny residuals,
and four sets of weights. Exact trajectory checks use alpha=1; the written
proof covers all alpha>0. Runtime 0.2447 seconds, peak RSS 16,465,920 bytes,
actual nice 20, CPU cap 60 seconds, one thread.

Constants: T=4, K=256, R0=65536, B=R0+8=65544, error=385/4096,
drift upper bound=-2171/20480. A separate common-denominator calculation
checks -4096+1280+640+5=-2171 at denominator 20480. The no-arrival
trial probability is retained symbolically to avoid floating underflow.
All assertions passed; no failed numerical run occurred.

## Independent audit and final read-back

Saved AUDIT.md with a second derivation: if an original count is still
above K at time t, monotonicity means its original service fraction was
at least K/(K+L) throughout [0,t]. Therefore Q(t)<=m*(1+L/K).
Whenever Q exceeds that barrier, both original counts are small and q
has the through-population bound. Integrating after the barrier gives
the same estimate as the last-route argument, without selecting a route.

Checked the large-local case again using a single persistent local route.
Checked the stochastic step without a petite-set assumption and without
dividing an unconditional return-cost bound by a failure probability.
The cycle occupation formula was checked directly for invariance, and
the empty holding times establish Harris recurrence with delta_empty.
No mathematical gap was found. The scope remains the specified topology,
unit arriving files and initial residuals at most one; no novelty claim.

Saved REPORT.md with the required PARTIAL first line. Final read-back
commands used nice 15 and the one-thread environment to read PROOF.md,
REPORT.md, AUDIT.md and uniform_drift_checks.json. The saved values agree
with both exact computations. No rerun is needed after documentation-only
changes. Final local clock: 15 November 2026, 08:41:55 Asia/Tbilisi.

Files: LOG.md, PROOF.md, AUDIT.md, REPORT.md, check_uniform_drift.py,
uniform_drift_checks.json, prior_check_sampled_drift.py and
sampled_drift_checks.json. The prior checker is a local unmodified copy;
all output paths resolve here. All new writes stayed in this folder.
