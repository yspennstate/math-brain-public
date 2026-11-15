# T185 continuation log

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded clock: 15 November 2026, 11:11:22 Asia/Tbilisi (07:11:22 UTC).
The exact receipt timestamp is unavailable.

## Orientation and short literature check

The task-specific instruction that all writes stay in this folder overrides
shared brain, checklist and mesh logging. Those mutating commands are not
invoked. Startup memory and the compute state were read directly. The
governor reports warn, owner_away_open and CPU saturation; only tiny
single-thread exact checks will run. No git, subagents or external writes.
Initial read commands omitted nice; subsequent programs request nice 15
and single-thread environment variables. The inherited priority will be
measured by the check scripts.

The literature check used web searches and primary-source opens within
five minutes. Queries included alpha-fair/general-file/positive-recurrence
2024–2026, Fu/Williams/stochastic stability, and the older Chiang–Shah–Tang
paper to distinguish its meaning of stability. Opened:

- Yingjia Fu and Ruth J. Williams, *Asymptotic behavior of a critical fluid
  model for bandwidth sharing with general file size distributions*,
  Ann. Appl. Probab. 32 (2022), 1862–1901,
  https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf .
  Page 1863 describes positive recurrence through Lee under suitable
  distributional assumptions; the new theorems concern critical fluid models.
- Mung Chiang, Devavrat Shah, and Ao Tang, *Stochastic Stability Under Fair
  Bandwidth Allocation: General File Size Distribution*, Allerton (2006),
  https://people.ece.cornell.edu/atang/pub/06/allerton06stability.pdf .
  Its introduction specifies rate/fluid stability; its abstract also restricts
  the load/alpha region and assumes bounded support. It does not resolve T185.

The 2020 author PDF request timed out. No later unrestricted recurrence
theorem was found. This brief search establishes neither absence nor
novelty. No SOLVED_ELSEWHERE.md is warranted.

Reading the four earlier REPORT.md, LOG.md, PROOF.md and scripts is in
progress. All earlier paths are read-only. The round-5 proof's main
reflection and threshold estimates have been read in full.

## Earlier result independently checked

Finished reading the four earlier reports, logs, proofs and scripts, plus
the round-5 audit. Copied only round 5's checker into this folder and ran:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /bin/cp ~/codex_op_1114r5/briefs/T185/check_uniform_drift.py ./prior_check_uniform_drift.py
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 prior_check_uniform_drift.py
```

Exit 0, all exact checks passed: 672 paths, 3,733 events, 1,920 threshold
checks, 434 original-cohort departures, 230 paths with Q>m, 72 with positive
empty time. Runtime 0.2348 seconds; peak RSS 15,876,096 bytes; actual nice
20; CPU limit 60 seconds. The priority warning is from attempting to
change the already lower inherited priority. Output: uniform_drift_checks.json.

Independent derivation: use the barrier h=m*(1+L/K), rather than selecting
the last high-count route. If any original local count is >K at time t,
it was >K throughout [0,t]; its original service is at least K*Q(t)/(K+L),
and is at most its initial work <=m. Thus Q(t)<=h. Above h both original
counts are <=K, so Q'<=c*(2K+L)/(a0*R). Integration yields the claimed
threshold bound. The local Skorokhod balance gives the claimed reflection
error (Q-m)^+. For unit input, EL=T and Var(A1-A2)=T, independently
recovering d(4)<=-1/5. At denominator 20480, the final constant is
(-4096+1280+640+5)/20480=-2171/20480. The return-to-set and no-arrival
regeneration argument does not require count compactness. No error found;
round 5's main claim holds under its stated assumptions.

## Chosen extension, before proof

Extend this same two-link recurrence argument to random file sizes and
the entire strictly subcritical load region. Require only that through
files have bounded size; allow both local file-size laws to have arbitrary
finite means, including unbounded support and infinite variance. Arrivals
remain independent marked Poisson processes. This includes the bounded
random-size extension suggested by round 5 and uses the same mechanism.

Why this scope: reflection uses compound input work U_i, while the threshold
lemma uses new local file counts L, whose mean is (nu1+nu2)*T independently
of file-size moments. Only n0>=W0/b0 needs a size cap, and only on route 0.
For arbitrary subcritical loads, choose a sufficiently long fixed horizon:
E max(U1(T),U2(T))/T tends to max(rho1,rho2) with finite means alone.
A truncation of input marks, used solely to bound this expectation, will
be proved directly; it is not a comparison of queueing systems. No claim
is planned for unbounded through sizes or general topologies.

## Proof saved

Saved PROOF.md with the proposed full two-link theorem, including the
finite-mean input estimate, the generalized count threshold, uniform
sampled drift, explicit finite mean regeneration, and extension to
arbitrary finite initial through residuals. Only the incoming through
size law is bounded. The key bound is

    E Delta M <= d(T)+m*lambda*T/K
                   +c*b0*T*(2K+lambda*T)/(a0*(W0(0)-T)),

where d(T)=(rho0-1)*T+E max(U1(T),U2(T)) and lambda=nu1+nu2.
To find a negative horizon with only finite means, cap local input marks
at h and bound the centered capped input by its standard deviation.
The remaining expected work is T*sum nu_j*E(B_j-h)^+, which tends to zero
after division by T as h increases. This proves the needed negative
horizon without a stochastic fluid-limit theorem.

Two exact examples are being checked: bounded nonconstant route sizes
at the original rates, and dyadic unbounded infinite-variance local sizes
with bounded through files. The proposed drift constants are
-3441/10240 at T=8, M>65552, and -17043/1280 at T=192, M>1048960,
respectively (equal weights, alpha=1).

One attempted text-only patch failed to match its context and made no
change; the corrected patch is this entry. No mathematical check has
failed. A new marked-file checker will use route service clocks rather
than the earlier script's residual updates, to independently test the
pathwise estimates with variable sizes.

## New checker run

Command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_marked_drift.py
```

Exit 0, all exact checks passed. The new simulator stores cohort completion
levels against per-route service clocks, independently of round 5's
residual-update implementation. It checks exact workload balance,
reflection regulators and their suprema, unit-speed draining of M while
nonempty, the (Q-m)^+ bound, and the count-threshold barrier.

Output: marked_drift_checks.json. Counts: 1,176 marked paths, 7,583 events,
3,780 threshold bounds, 9,667 high-count barrier checks, 1,206 original
cohort departures, 3,020 intervals with mixed original/new local cohorts,
520 paths with Q>m, 180 with positive empty time, and 476 large-local
paths. Marks include through sizes 1/2 and 3/2, very small local files,
local files as large as 10^9, simultaneous arrivals and horizon-end
arrivals. Initial compressed populations reach 10^7 files. Four weight
vectors and horizons 1,8,192 are used. Trajectory calculations are for
alpha=1; the proof covers all fixed alpha>0.

The script also verifies all explicit constants and finite-support
moments by two methods: direct atom sums and survival integrals. Seventeen
dyadic truncation levels verify the infinite-variance example by finite
atom sums with an exact tail and separate survival integrals. The two
drift constants agree with PROOF.md: -3441/10240 and -17043/1280.
Arithmetic time 0.6716 seconds, peak RSS 16,171,008 bytes, actual nice 20,
one thread, CPU limit 60 seconds. No numerical workers or subprocesses.

The main theorem and regeneration step are being audited separately from
these finite deterministic checks. No mathematical check failed.

## Independent audit and report

Saved AUDIT.md. It independently recovers the threshold bound by the last
original local count to fall to K, rather than the proof's barrier argument.
It verifies the negative-horizon limit by truncating iid unit-time input
increments and proving L1 convergence, independently of the mark-level
bound in PROOF.md. It re-derives both sets of explicit constants and checks
the return/trial calculation, cycle invariance and Harris recurrence.

Read PROOF.md back in full, and reread both round-3 and round-5 LOG.md
in untruncated output to complete the source review. The first session,
round 3, round 4 and round 5 reports, proofs, logs and scripts have all
been read. No earlier files were modified. No mathematical gap was found.

The audit specifically checks unbounded local residuals, infinite local
variance, unequal loads, extreme fixed weights, original departures,
empty periods, the distinction between arrival counts and input work,
and arbitrary finite initial through residuals. The latter use a cap
depending on the initial state; only the incoming through size law has
to be bounded. No uniform sampled drift on all uncapped initial states
is claimed. No stationary workload moment follows from this proof.

Saved REPORT.md with the required PARTIAL verdict. The next obstruction
is unbounded incoming through sizes, not unbounded local sizes. The
suggested next step is a residual-tail estimate for through work; the
report explicitly avoids inferring stability from truncation.

## Final read-back

Read REPORT.md and marked_drift_checks.json in full and listed this
folder's files. The report starts with the required verdict; the saved
constants and path counts match the successful run. PROOF.md had already
been read back in full. No code changed after the successful check, so
no additional run was needed. New task artifacts: REPORT.md, PROOF.md,
AUDIT.md, LOG.md, check_marked_drift.py, marked_drift_checks.json,
prior_check_uniform_drift.py and uniform_drift_checks.json. Preexisting
runner files were not edited. Final clock: 15 November 2026, 11:22:13
Asia/Tbilisi (07:22:13 UTC). All new writes stayed inside this folder.
