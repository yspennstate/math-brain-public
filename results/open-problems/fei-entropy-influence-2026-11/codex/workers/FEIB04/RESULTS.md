# FEIB04 results

The general cancellation conjecture remains open. Full derivations and the exact
failing steps of the proposed proof routes are in [PROOFS.md](PROOFS.md).

There is a correction to the brief's constant-sign observation. With the empty
set included, constant signs for every nonempty derivative do not imply Gamma=0:
AND_2 has Gamma=1/4 bit. A nonconstant zero-Gamma function must be balanced.

## Proof results

(a) Martingale: proved the exact L1 telescope and a first-reveal bound. A
universal bound on each later reveal's charge by its own coordinate influence is
false; an explicit Boolean family has an exponentially growing ratio. Adaptive
ordering and aggregate redistribution remain open.

(b) Superset/Gibbs: the absolute Fourier superset bound and the candidate
nu_t(S)=t^|S| |fhat(S)| abs1(S) both fail on majority, with exact formulas for their
growth. No replacement coding kernel proving the conjecture was found.

(c) Hypercontractivity: a Boolean derivative of outside degree one has cancellation
ratio 2^k-1. Outside degree, boundedness and granularity alone cannot supply the
missing mean comparison. A weighted aggregate argument remains open.

(d) Zero Gamma: proved the exact sign criterion, the necessary balancedness of
nonconstant examples, input/output sign invariance, antichain inclusion, and
closure under balanced composition. Read-once AND/OR/NOT formulas have only the
empty-set contribution. Monotone/unate functions need not have Gamma zero.

Composition: proved Gamma(f(g_1,...,g_m))=Gamma(f)+sum_i I_i(f) Gamma(g_i) for
balanced disjoint inner functions. Products have additive Gamma even for biased
factors. The conjecture is equivalent, with the same optimal constant, to the
balanced strengthening Gamma<=C(I-1).

Majority: proved abs1(S) is the same for every nonempty S, Gamma=H/2+log2(abs1),
and Gamma/I tends to 1/ln(2). Thus any universal constant is at least 1/ln(2).

Counterexample search: found no family with a proved unbounded ratio. Quadratic
bent functions obey Gamma=(1/2) E rank(A_S); their sharp maximum is n/4-1/4,
attained by the complete-graph quadratic. The general Gamma conjecture remains
open, and no global suprema beyond four variables were established.

The asymptotic constants, computed in final_metrics.json, are
Gamma/I -> 1.442695040888963 bits per expected sensitive
coordinate and Gamma/sqrt(n) -> 1.151104099072163
bits. At n=1,000,001, theory_checks.json records Gamma/I =
1.429197875419796. The asymptotic assertion is proved by a
spectral Riemann sum with endpoint bounds, not inferred from that finite value.

## Exhaustive baseline and search results

initial_checks.py / initial_checks.json reproduce the exhaustive n<=4 baseline:
Gamma/I = 0.375 at 0x116, with Gamma=0.75 bit and I=2. The balanced maximum is
log2(6)/5 = 0.5169925001442313 at 0x67b, with
Gamma=log2(6)/4 bits and I=9/4. Bit x set in a hexadecimal witness means f(x)=-1.

These are best-found lower bounds on the unrestricted ambient-n suprema.
Unused-coordinate embeddings are included and explicitly identified in
[WITNESSES.md](WITNESSES.md). They are not global maxima.

| n | best found Gamma/I | best found balanced Gamma/(I-1) |
|---|---:|---:|
| 6 | 0.523731127744 | 0.689548150491 |
| 7 | 0.624076163553 | 0.694742671847 |
| 8 | 0.627219751450 | 0.762762075485 |
| 9 | 0.712432861119 | 0.801046772704 |
| 10 | 0.712432861119 | 0.801046772704 |
| 11 | 0.755555729626 | 0.834333689746 |
| 12 | 0.755555729626 | 0.896994903569 |
| 13 | 0.791524158167 | 0.896994903569 |
| 14 | 0.803067237009 | 0.896994903569 |
| 15 | 0.818794138007 | 0.914596376813 |
| 16 | 0.836833202802 | 0.914596376813 |
| 17 | 0.848406920346 | 0.983146568043 |
| 18 | 0.861912974053 | 1.027939128342 |
| 19 | 0.871821816326 | 1.027939128342 |
| 20 | 0.890955034811 | 1.027939128342 |

The n=20 ordinary witness is symmetric, with Hamming-layer string
`++--++---+++++--++++-`. It has Gamma=4.051516602886615 bits,
I=4.547386169433594, and bias=0.4319057464599609.

The best balanced ratio was found at n=18 in two blocks of sizes 9 and 9:
Gamma=5.036126884621722 bits and I=5.899246215820312, giving
Gamma/(I-1)=1.027939128341704. Its full layer string and all other
witnesses are in WITNESSES.md and search_audit.json. The same function supplies
the n=19 and n=20 balanced lower bounds by ignoring the extra inputs.

## Search coverage

search.cpp / symmetric_search.jsonl enumerate every symmetric function at n=6
through n=20 up to output complementation: 2,097,088 representatives.
The signed finite differences, Fourier coefficients and L1 numerators are exact
integers/dyadics; Gamma uses floating-point logarithms. All winning symmetric
values were independently recalculated at 80 decimal digits. This is an
exhaustive numerical census, not an interval-arithmetic certificate of ordering.

truth_search.jsonl records 55,084 exact derivative evaluations at
n=6 through n=10, including random, majority-like, bent-like initial states,
balanced and unrestricted annealed single-bit/swap searches, and
500 generic quadratic-threshold samples.

block_search.jsonl records 546,840 exact derivative evaluations
over two permutation-invariant blocks at every n=6 through n=20. These searches
use random, majority-like, quadratic-bent-like, and low-degree threshold starts,
including a balanced self-dual arm. Repeated evaluations are included in the count.
Only the block sizes in the saved records were searched; no completeness claim
is made for two-block functions.

ptf_search.jsonl adds 20 generic weighted linear/quadratic thresholds on
n=11 through n=20, evaluated by full derivative traversal with no Monte Carlo
estimation. These are one sample of each degree per dimension, not a wide search
at the largest dimensions. Their coefficients and bit-packed truth tables are
saved. The 20-variable linear and quadratic ratios are
0.331856617772 and 0.516895322828, respectively.

search_audit.json records 10,178 balanced-inner
single-variable replacement candidates, evaluated from the proved law. The
quadratic-bent benchmarks at each dimension use the proved rank formula and the
independently checked symmetric/product evaluators.

## Independent checks and resource use

initial_checks.out checks Walsh coefficients against direct derivatives, all
symmetric functions through seven variables, and 696 compositions. The largest
composition error was 4.440892098500626e-16 bits.

theory_checks.out checks the zero characterization and martingale telescope on
all functions through four variables, plus random larger functions and explicit
obstructions. The telescope discrepancy was
3.33066907387547e-16 bits. At k=10 the local
martingale-charge witness gives charge/I_i=
11.19524368004344; formula (4) in
PROOFS.md proves its divergence. At n=51, the proposed sub-probability ansatz with
t=1/2 has log2(total mass)=3.223014287845826>0.

search_audit.out independently checks all 70 original search winners, 84 random
two-block functions against full truth tables, and the small composition winners.
Maximum winner discrepancy: 1.77635683940025e-15 bits or influence
units. All generic PTF truth tables were independently reconstructed and their
Fourier influences checked through n=20; Gamma was independently recomputed in
Python through n=14, with maximum discrepancy
1.332267629550188e-15 bits. Beyond that their Gamma values rely on
the C++ traversal already cross-checked at smaller dimensions.

proof_audit.out checks all 452 quadratic bent
functions up to output sign on n=2 and n=4, 36 random
larger quadratic bent functions, every essential labeled read-once AND/OR/NOT
function through four variables, every dictator-product lift through four
variables, and an independent smaller symmetric census. All assertions passed.

Runs inherited nice 10, as recorded in each search log, and used one thread each.
No more than two computations were active together. The maximum recorded resident
set was 644,235,264 bytes (0.600 GiB), below the 3 GiB per-process
limit. The generic 20-variable traversal's process peaked at 93,110,272 bytes
(ptf_search.log). All arrays fit the planned truth-table/depth-first allocation;
no full 3^20 table was allocated. No subagents or model workers were started.

## Reproduction and memory handoff

Run `python3 run_all.py` in this folder. It sets numerical libraries to one thread,
retains or lowers priority to nice 10, compiles search.cpp with clang++ -O3, runs
the searches and independent checks sequentially, and rebuilds the reports.
Dependencies are Python 3, NumPy, SciPy, mpmath, and clang++.

Brain recall supplied the startup context and prior FEI warnings; it did not
supply the proofs above. The math recall tool returned "math store not found".
The fleet rules forbid out-of-folder writes and mesh posts, so no shared memory,
checklist, mesh, deployment, repository or external service was modified. This
report is the launcher's durable-learning handoff.

Task: "Do the brief fully and carefully, saving as you go" —
10 Nov 2026, 01:09:56 +0400 (BRIEF.md launch timestamp).
