# FEIB04 report

Completed the research brief and saved the proofs, searches, witnesses and audits.
The universal Gamma conjecture remains open. No proof or counterexample is claimed.

The brief needs one qualification: constant-sign nonempty derivatives do not make
Gamma zero for a biased function. AND_2 has Gamma=1/4 bit from the empty set.

## Verdict per idea

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

## Main numbers and witnesses

Odd majority gives the rigorous lower bound C>=1/ln(2) =
1.442695040888963, with Gamma approximately
1.151104099072163 sqrt(n) bits. The finite check
at n=1,000,001 gives Gamma/I=1.429197875419796
(theory_checks.json; proof in PROOFS.md Section 5).

The best found Gamma/I through n=20 is 0.8909550348109664, at n=20:
Gamma=4.051516602886615 bits, I=4.547386169433594, symmetric layer string
`++--++---+++++--++++-`. The best balanced Gamma/(I-1) is
1.027939128341704, at n=18: Gamma=5.036126884621722 bits,
I=5.899246215820312, in two blocks of nine variables. See WITNESSES.md for
its layer string and the best-found values and witnesses at every n=6 through 20.
These are lower bounds on global suprema. Exact global maxima beyond n=4 were
not established.

Search coverage was 2,097,088 symmetric output-complement
representatives, 55,084 unrestricted truth-table evaluations through
n=10, 546,840 two-block evaluations through n=20,
20 additional generic low-degree thresholds through n=20, and
10,178 composition candidates. Counts and source
paths are in final_metrics.json and RESULTS.md. The largest dimensions received
structured searches and only two generic PTF samples each; they were not
unrestricted hill-climbed. Symmetric maxima are exhaustive numerical results,
with exact dyadic inputs and 80-digit winner checks, rather than formal interval
certificates of ordering.

## Verification and resources

Every function on n<=4 was used to test the central sign and martingale identities.
The four-variable baseline is Gamma/I=0.375 and balanced Gamma/(I-1)=log2(6)/5.
Independent winner re-evaluation differed by at most
1.77635683940025e-15 bits or influence units; the composition check
differed by at most 4.440892098500626e-16 bits. Exact quadratic
rank, read-once derivative-sign and dictator-lift checks all passed. The majority
constant was re-derived from its exact Fourier masses and independently checked
by numerical quadrature. Generic PTF influences were independently checked at
every dimension, with zero discrepancy; their Gamma values were independently
recomputed through n=14.

All search logs record nice 10 and one thread. Maximum recorded process RSS was
644,235,264 bytes (0.600 GiB), below the 3 GiB cap. At most two
computations ran concurrently. All work stayed in this folder. No model workers,
subagents, pushes, mesh posts, trading processes, email or external writes were
started.

The files to read are [PROOFS.md](PROOFS.md), [RESULTS.md](RESULTS.md), and
[WITNESSES.md](WITNESSES.md). Raw outputs and scripts remain alongside them.
`python3 run_all.py` reproduces the computations sequentially. SHA256SUMS.json
records source and result hashes at finalization.

Brain recall helped with orientation and avoiding prior dead routes. The math
store was unavailable. The fleet's out-of-folder prohibition prevented a shared
brain write; this report is the launcher session's handoff for the proved
composition law, majority constant, exact zero criterion, balanced equivalence,
and the failed-route witnesses.

What is still open is a genuinely aggregate influence charge for cancellation,
a successful superset/coding kernel, and the universal bound itself. Exhaustive
global search beyond four variables is also open.

Task: "Do the brief fully and carefully, saving as you go" —
10 Nov 2026, 01:09:56 +0400 (BRIEF.md launch timestamp).
