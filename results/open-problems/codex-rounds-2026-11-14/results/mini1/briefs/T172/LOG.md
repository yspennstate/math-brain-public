# T172 working log

Task received: 14 November 2026, approximately 21:18 Asia/Tbilisi (17:18 UTC).
Ask: “push this problem forward by one checkable piece.”

## Scope and startup

All artifacts stay in this directory. No git, external writes, subagents, or heavy computation.
Read the startup memory index and compute governor state. The governor reported
`warn`, `owner_away_open`, with CPU saturation; any computation here will be small,
single threaded, with `OMP_NUM_THREADS=1` and `nice -n 15`.
The session-specific folder-only rule overrides the global instructions to write to
the shared mesh, checklist, and brain, so those external stores are not modified.

## Literature check, begun 17:18 UTC

Web queries:

- `"input queued switch" "optimal" "2026" queue scaling`
- `"2610.37521"`
- `"optimal scaling" "queue sizes" switch solved`
- `"input-queued" "November" "2026" scaling`
- `"Approaching Optimal Scaling" switch batching k constants`
- `"input-queued switch" batching "lower bound" log`

Opened, rather than citing search snippets:

- Taha Ameen and Weina Wang, *Approaching Optimal Scaling of Queue Size for an
  Input-Queued Switch*, arXiv:2610.37521v1, submitted 27 October 2026.
  https://arxiv.org/abs/2610.37521 and https://arxiv.org/html/2610.37521v1
- Devavrat Shah, John N. Tsitsiklis and Yuan Zhong, *Optimal scaling of average
  queue sizes in an input-queued switch: an open problem* (2011).
  https://www.mit.edu/~jnt/Papers/J132-11-switch-open.pdf
- Jiaming Xu and Yuan Zhong, *Improved queue-size scaling for input-queued
  switches via graph factorization*, arXiv:1903.00398.
  https://arxiv.org/abs/1903.00398

The search found no later full solution. The October 2026 abstract agrees with
the supplied status: a family indexed by a fixed recursion depth approaches
exponent one. Next: inspect its parameter dependence and select a finite,
checkable mathematical target. No claim of exhaustive literature coverage.

## Chosen piece, 17:22 UTC

Quantify the recursion-depth dependence in the Ameen–Wang policy, rather than
substituting a varying depth into a fixed-depth big-O theorem. Target: a proved
uniform bound of the form

`C n log(144 n/epsilon) (1+log(1/epsilon))^9 / epsilon`

for independent Bernoulli arrivals of rate `(1-epsilon)/n`, at least for all
`n >= 2` and sufficiently small explicitly specified `epsilon`. This retains
logarithmic losses and does not settle the exact conjecture.

Why this piece: the opened paper gives explicit block lengths, failure
probabilities, and a final queue bound before it hides constants in `O_k`.
Its Appendix A.3 has an upper-block-size constant `D`; Appendix B uses
`D=(2K)^k`, with `K=144`. If `k` grows as `log_2 log(1/epsilon)`, this is a
power of a logarithm. The actual work is checking every “sufficiently large”
condition and accumulated failure bound uniformly over all levels. Merely
plugging a growing `k` into its stated theorem would not be a proof.

Literature search ended by 17:22 UTC, under four minutes after starting.
No `SOLVED_ELSEWHERE.md` is warranted. The paper's Theorem 1 and Appendix B
were opened, including parameter definitions, factor-test Lemma 11, rounding
rules, maximum-port fluctuation estimates, and the final explicit population
bound. Subsequent web reads, if needed, will only check these source details.

Plan for verification: write the uniform inequalities and the queue argument in
`PROOF.md`, then check rounded parameters, geometric exponents, finite constants,
and possible dependence between arrivals, failures, and queues independently.
Any arithmetic script will use only the Python standard library and run under
the requested resource limits.

## Proof draft saved, 17:26 UTC

Created `PROOF.md` with a full derivation for all `n>=2` and
`0<epsilon<=exp(-128)`. The proposed bound has explicit constant `10^6`.
It uses `k=ceil(log_2(1+log(1/epsilon)))`, retains all ceilings/floors, and
shows `(288)^k <= epsilon^(-1/2)` to make the previous fixed-depth failure
and fluctuation estimates uniform. The final polynomial logarithm is a
rounded upper bound for exponent `log_2(288)<9`.

The proof includes the random graph factor estimate, the nested service
timing, unconditional union bounds for failures, and the scalar Lindley
queue argument. It does not assume independence between a failure and a
port fluctuation. It also constructs a stationary version with random
scheduling phase.

This is a draft claim until the independent audit is complete. Main doubts
to attack: whether final matching batches depend on disjoint original data;
whether promotion timing makes the residual identities valid; whether a
fixed-depth asymptotic is hidden in any remaining step. No claim of the
exact conjecture, or of historical novelty, is made.

## Independent audit started, 17:30 UTC

Created `audit.py` (standard library only). It checks exact rational exponent
identities and constant arithmetic; 44 high-precision rounded-parameter
cases; and an event-by-event small-switch implementation against a separate
offline, original-batch construction. The small simulation tests structural
identities and timing, not the queue bound at the theorem's tiny loads.

Command started:

```sh
env OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > AUDIT_OUTPUT.txt 2>&1
```

The sandbox prints `nice: setpriority: Operation not permitted`. A small
diagnostic using `os.getpriority(os.PRIO_PROCESS,0)` showed that the process
already inherits nice **20**, which is lower priority than requested. The
audit asserts effective nice >=15 before computing. `ps` is denied by the
sandbox, and an attempt to set nice exactly 15 is also denied. No escalation
was attempted. The script has a 90-second CPU limit; its data structures are
small and its actual peak RSS is recorded.

Proof review so far: checked the complementary-cut transformation in the
factor lemma; the complete-packet labeling rather than independent copies
at different levels; integer final service count; and the distinction
between original arrival blocks and the later blocks used to serve them.
The final coefficient was recomputed as `1100*288*3=950400`.

## Audit completed, 17:32 UTC

The command exited successfully. Exact contents of `AUDIT_OUTPUT.txt`:

```text
nice: setpriority: Operation not permitted
PASS exact arithmetic: 276 exponent identities; final coefficient 950400 < 1000000
PASS rounded parameters: 44 cases, n=2..1000000, epsilon=2^-185..2^-1024
PASS pathwise timing: 8904 port identities; 297 online/offline batch comparisons
PASS resources: OMP_NUM_THREADS=1, effective nice=20, peak RSS=17891328 bytes
Wrote AUDIT_DATA.json
```

The arithmetic run was below its 90-second CPU limit and used about 18 MB
peak RSS. It used no numerical or parallel libraries. `AUDIT_DATA.json`
contains each parameter case and each pathwise case, including the seeds.

Independent checks and attempted failure cases:

- Recomputed all balanced exponents as exact rational identities for depths
  2 through 24, not using floating-point simplification.
- Checked `log(129)<5` and `log(288)<6` through rational lower bounds on
  exponential power series. The remaining `log(2)>2/3` follows independently
  from strict convexity of `1/x` integrated on `[1,2]`.
- Computed rounded `L_j,S_j` at 1450-digit precision, then reconstructed
  every `a_j` and every slot-count telescoping identity using exact rational
  arithmetic with `rho=1-2^-r`. Tested both small and large n, several depth
  changes, and the least-heavy case in the tested interval (`r=185`).
- Implemented chronological service on a 2x2 switch with depths 2, 3, 4.
  Used separate offline bottom-up processing of each original batch to
  check that later batches are functions only of their original data.
  All residual port-count identities held, and there were zero packets
  awaiting a lower promotion when a parent service began.
- Checked the event schedule's first unassigned slot explicitly. For the
  depth-4 toy example, it is offset 4, rather than assuming consecutive
  offsets. The audit was corrected before its first run to construct the
  actual slot allocation. The proof uses the allocation rule and makes no
  consecutive-offset assumption.
- Inspected dependence: the cut event need not be independent of the degree
  event or of lower failures; the union bound is unconditional. The variance
  estimate uses `Var(Z+F)<=2 Var(Z)+2 Var(F)`, not independence.
- Checked the n=2 cut boundary: there are no nontrivial protected cuts, and
  the deterministic proof still covers all other cuts through degree bounds.
- Checked irrational rates and rounding: `S_k` is defined by an integer
  count of unassigned slots; its alternative formula need not consist of
  integer summands.

No counterexample to the stated theorem was found. The audit is supporting
verification; the finite samples do not replace the uniform proof.

## Scope and failed routes

A direct substitution of varying k into the published fixed-k theorem is
invalid; the proof instead keeps its dependence explicit throughout.
Taking k to infinity does not remove the losses, because the block-size
constants grow with k. The analysis still contains the factor
`log(144n/epsilon)(1+log(1/epsilon))^9`. No exact `O(n/epsilon)` result,
nonuniform-traffic extension, or arbitrary-process arrival result was obtained.
There is no claim that the displayed corollary is historically new; the short
literature search establishes neither novelty nor absence of all later work.

`REPORT.md` records the proved piece, command, limitations, and a next step.
