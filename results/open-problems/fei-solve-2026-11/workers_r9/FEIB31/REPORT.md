# FEIB31 report

The largest certified monotone value found here is

    G_mon > 4.50640064551556

in bits per unit coordinate influence. An explicit transitive monotone tower
has ratio 4.5064006455155684355071736704529973127... . I also prove the sharp
per-leaf erasure bound pi/ln 2 for read-once AND/OR formulas and an O(w)
best-coordinate bound for width-w DNFs/CNFs. Question M for all monotone
functions remains open. Its boundedness is equivalent to monotone FEI, with
an additive 2/ln 2 between the optimal constants; the remaining obstacle is
choosing a good coordinate when boundaries overlap without a separable path.

The complete proofs are in PROOFS.md. Search results and the current literature
check are in RESULTS.md and LITERATURE.md. Each claim below is marked by its
kind of evidence. No global optimum or new class theorem is claimed.

## The record and its DNF

CHECKED NUMERICALLY WITH INTERVALS: record_certificate.json encloses the largest
value between 4.50640064551556 and 4.50640064551558 using 100-digit outward
interval arithmetic. The function has 112,844,396,298,240 relevant variables.
It is specified by this positive-DNF composition word, bottom to top:

    M,D,D,D,D,M,P,P,P,Q2,dual(PM(K4)),dual(T(4,3)),T(2,6),T(3,5).

Here M is perfect matching on a 3 by 3 bipartite graph, P is perfect matching
on a 4 by 4 bipartite graph, and D is the monotone dual of M. Their positive
DNFs are the OR over permutations of the corresponding matching terms.
D is the OR of the six row/column stars and nine 2 by 2 rectangles.
T(w,s) is the OR of s disjoint width-w terms; Q2=dual(T(2,2)). The dual of
T(w,s) is the OR of the w^s terms obtained by choosing one variable from each
of its s blocks. PM(K4) is the OR of its three pairs of opposite edges.
Exact gate masks are retained in the certificate. PROOFS.md Section 7 gives
the grammar in full, so this specifies a DNF without expanding its enormous
term list.

PROVED: the composition is monotone, and every gate is transitive on its
inputs. The induced action is transitive on all leaves, making the minimum
ratio equal to the ratio certified for one coordinate. The certificate records
means, influences and the singleton identity fhat({i})^2=Inf_i^2 at every level.

A much smaller new witness, M,D,D,D,D,dual(T(2,5)), already gives
4.505850062076900302... on 590,490 variables. Both values are in
record_certificate.json. The deeper floating search had rounding drift of
order 1e-8; its printed final digits are superseded by the intervals.

PROVED and independently recomputed: the brief's previous 4.50504996749762
example is already monotone up to an output complement. A level-uniform word
of M and -M has the same orientation at every leaf. Absorbing signs gives the
monotone word M,D,D,M,M,D,D. tower_certificate.json certifies its value.
Thus calling that old tower non-monotone was an error in the brief.

## Search coverage

CHECKED NUMERICALLY: the following are exact truth-table Fourier calculations
with double-precision logarithms, not sampling estimates. The commands, seeds,
DNFs and outputs are retained in the named scripts and JSON files.

| Search | Coverage | Largest minimum ratio |
|---|---|---:|
| Boundary flips and term insertion/removal | 144 starts, n=8..13, 85,686 objective evaluations | 3.541677755509652 |
| Graph-seeded boundary search | 122 starts, n=8..13, 146,522 evaluations | 3.105857651244001 |
| Cyclic positive DNFs | 180 functions, 20 at each n=12..20 | 3.428002703877404 |
| Direct graph properties | K4, K5, K6, K3,3, K4,4 | 3.3965247927188287 |
| Direct tribes and threshold controls | families.json | 3.6068470020964094 |

The direct graph maximum is PM(K6). The cyclic maximum is the orbit of
{x1,x5,x9} on 20 coordinates. The direct overall maximum is the known OR of
eight disjoint pairs. The hill searches used exact-table objectives with
randomized ascent/annealing; they are not exhaustive optima or certificates
of local optimality. The requested graph properties were included wherever
nontrivial, including Hamiltonicity and connectivity. Mixed-gate beam searches
then used transitive bases and duals; the larger search had 110 gates, a beam
cap of 100 and depth cap of 14. Its winners were independently certified.

## What is proved for classes and selection rules

PROVED, PROOFS.md Section 3: every relevant leaf of a read-once AND/OR formula
satisfies

    E_i/Inf_i < pi/ln 2 = 4.5323601418271938096... .

This constant is the sharp supremum for a specified leaf. A family of
alternating independent guards approaches it. This does not establish the
sharp best-coordinate constant. The proof factors the pivotal event into
independent sibling blocks and adapts the potential from the author's existing
FEI19 selector-path proof. FEI19's full entropy-split kernel has sharp constant
pi^2/2 nats; our erasure kernel integrates to pi nats. These are different
quantities. Read-once FEI and the potential method were already known; the
erasure specialization is the result established here. The integral is checked
two ways in class_checks.json.

PROVED, Section 2: every width-w DNF or CNF has a coordinate with

    E_i/Inf_i <= 2+log2(e)+log2(2^(w+1)-1) < w+3+log2(e).

No read bound or monotonicity is needed. This refines FLOW 12(v)'s relative-step
argument and gives a complete answer for this requested class. Its tree
consequence is H<(w+7.328085122666891) I. All monotone functions through five
variables were enumerated as additional controls, including 7,581 at n=5;
the shortest-term influence inequality had smallest factor exactly one.

PROVED, Sections 4--6: maximum influence is not a valid selection rule, even
for monotone functions. Balanced-majority substitution leaves a hidden
coordinate's unbounded ratio unchanged while making it uniquely most
influential. This is an established counterexample from the earlier work,
rederived and checked here. Minimizing the positive-log score changes the
question by at most 1+log2(e), but does not solve it.

PROVED: almost every coordinate can be bad. Put a separate hidden bit at
each point of the lower middle layer of a majority cube. The hidden orbit
has unbounded ratios, while a smaller base orbit has much larger influences.
At k=17, compact exact-spectrum calculations give 24,310 hidden bits with
ratio 14.451731157696454 and 17 base bits with ratio 2.1426634341909123
(hidden_symmetric.json). This is not an all-coordinates counterexample.

PROVED: an inequality sum_i Inf_i^a E_i <= C sum_i Inf_i^(a+1) cannot hold
universally on monotone functions when a<0 or a>1. The layered construction
rules out a<0; the unique-hidden construction with majority substitution
rules out a>1. The interval 0<=a<=1 remains open. Spectral FKG also fails:
x1 OR (x2 AND x3) has P[1,2 in U]=1/8, below (3/4)(1/4).

HEURISTIC, not a no-go theorem: indicator level inequalities and multiplicity
counting alone have not supplied the needed alignment between the spectra
of g and h. No successful weighting in the remaining interval was found.
The suggested low-influence class I<=K sqrt(log n), with dummy variables
allowed, contains every function after padding, so a uniform Question M bound
there is the full problem. The interpretation counting only relevant variables
is left open, and the class is not restriction-closed.

## Validation and limits

CHECKED NUMERICALLY: audit.py compares the transform with direct character sums
and influences with edge counts, both with zero error. Its 20 direct composition
checks have maximum error 2.220446049250313e-16; 100 independent-guard checks
have maximum ratio error 1.3322676295501878e-15. Every saved hill winner was
rebuilt from its DNF and checked monotone; the largest recomputation difference
was 3.4727776210274897e-13. The layered hidden formulas were checked against
full cubes at k=3,5. final_audit.py reconciles counts, constants, intervals,
resource limits and outputs; SHA256SUMS.txt records the numerical artifacts.

The scripts ran one compute process at a time, one thread, inheriting nice 10.
The largest directly enumerated cube has 2^20 entries; one float64 table uses
8,388,608 bytes. Actual audit peak memory and elapsed seconds are recorded by
resource_run.py in audit_resources.json and class_checks_resources.json.
The folder is below 60 MB. No huge tower truth table was allocated. No helper
agents, shared-state publishing, mesh post, push, message or trading process
was used.

The requested primary literature was checked before making any priority claim.
Symmetric and read-once classes are established; monotone/unate min-entropy
follows from KKL and the singleton identity and does not imply Shannon FEI.
The checked current sources leave general monotone FEI open. LITERATURE.md
records exact sources, theorem locations and scope. Startup memory and the
area memories helped: they prevented re-claiming the maximum-influence example,
bounded-width class, and selector potential. No math store or brain data was
modified. Proposed durable results are handed back in these local artifacts.

The brief is complete as an investigation. The full monotone conjecture is
unresolved; no finite universal G_mon has been proved or disproved here.
The most useful next checks are an independent reading of the pi erasure
specialization and an overlap-compatible coordinate selection argument.

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 2026
22:20 ask, as quoted in the FEIB31 brief.
