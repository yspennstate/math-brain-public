# T049 work log

Task received 15 November 2026 at approximately 04:25 Asia/Tbilisi
(00:25 UTC): “take the NEXT checkable step on this problem, building on that work”.

## 1. Orientation and literature check (00:25–00:29 UTC)

Read REPORT.md, LOG.md, PROOF.md and all Python scripts in both earlier
folders, plus the startup memory and brain index. The compute governor
reports `warn`, `cpu_saturated`, `owner_away_open`. Computations will be
small, single-threaded, and run under `env OMP_NUM_THREADS=1 nice -n 15`,
with an actual-priority assertion, runtime alarm and RSS measurement.
The specific folder-only instruction overrides global commands that write
mesh, checklist or brain state elsewhere. Those commands were not run.
No git, subagents, or changes outside this folder.

Read-only shell commands: `rg --files` in both earlier folders; `cat` of
their reports, logs, proofs and scripts; read the startup and governor files.

Bounded web searches (under five minutes):

- `minimal spanning forest Z d connectivity open problem 2025 2026`
- `"minimal spanning forest" "seven" lattice connectivity`
- `"minimal spanning forest" "Z" "connected" "2026"`
- `"minimal spanning forests" "open" "2025"`
- `"minimal spanning tree" "slabs" Tassion Wu Newman`

Opened the arXiv pages math/0412263, 0902.3651, 1512.09107, 2609.11845,
2608.10654 and the full Lyons–Peres–Schramm paper at
https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf . No later solution on full Z^d
was found. The slab theorem and the dimension-six scaling prediction remain
qualifications already identified by earlier workers. The recent weighted
forest and complete-graph papers do not announce the lattice result.
This is a bounded search, not proof that no later paper exists.

## 2. Recheck to perform, and extension selected before implementation

The earlier finite-cut argument rechecks: an internal edge in a wired MST
minimizes its finite fundamental cut and therefore lies in the infinite free
MSF. Two distinct simple paths between fixed endpoints force a cycle, even
when they overlap. The boundary-to-volume proof of P(e in F)=1/d also holds.

First implement a fresh direct recursion for the event that every specified
path edge is accepted, and compare all saved square and six-vertex fractions
in dimensions 2 through 12. Do not import or run the earlier scripts.

Chosen single extension: add every seven-edge simple detour. Retain every
induced chord and calculate each finite wired probability exactly. Classify
by the number of transverse coordinate axes used (at most three), so path
counts in dimensions 2, 3 and 4 determine the all-dimension multiplicities.
Independently enumerate closed eight-step direction multisets to audit the
geometry. Compare probabilities against a separate fixed-tree contraction
calculation and audit the displayed rational sum using integer arithmetic.
This adds one length to the local certificate hierarchy; no global component
claim is intended.

## 3. Independent earlier-result recheck completed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 seven.py recheck > recheck.txt`.
Exit 0. A freshly implemented event-partition recursion reproduces all 11
square probabilities and all 33 six-vertex probabilities in d=2,...,12.
A separate sum over final trees and accepted-edge subsets also agrees with
all 33 six-vertex probabilities. The saved fractions were read only for
comparison; no earlier code was imported or executed. All 11 reported
connectivity bounds agree, including
`347146143557/922150845000` in d=3. The earlier result holds.

The wrapper prints `nice: setpriority: Operation not permitted` because the
inherited nice value is already 20; the program asserts and records actual
nice >=15. Exact output and resource measurements are in recheck.txt and
recheck.json. No arithmetic check failed. Proceeding with the seven-edge
extension chosen above.

## 4. Seven-edge geometry enumerated

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 seven.py enumerate > enumeration.txt`.
Exit 0. Reachability-pruned DFS finds 28, 552 and 2868 detours in ambient
dimensions 2, 3 and 4. The counts using every transverse axis in each
dimension are 28, 496 and 1296. There are 15 induced graphs up to reversal
of the distinguished path. `graphs.json` records every induced edge,
representative coordinates and the three support coefficients for each.
Memory measured 17,367,040 bytes, time 0.118 seconds, actual nice 20.

An eight-cycle uses at most four axes: each used axis contributes at least
two steps, and axis 1 is used by the closing edge. Consequently the total
seven-edge count is exactly
`28*(d-1) + 496*binom(d-1,2) + 1296*binom(d-1,3)` if the enumerated support
counts pass the independent audit. Probability evaluation is now running:
`env OMP_NUM_THREADS=1 nice -n 15 python3 seven.py extend > extension.txt`.
It checkpoints after each dimension, and does not overwrite earlier files.

## 5. Seven-edge probabilities computed

The extension command exited 0. Every active induced graph probability in
d=2,...,12 agrees exactly between the direct event recursion and the sum
over fixed final trees. The result has 28, 552, 2868 seven-edge detours in
d=2,3,4; all 15 graph types occur in d=3. Every probability strictly exceeds
the crude event that the seven desired edges precede all other incident
edges. All final bounds strictly improve the earlier ones and remain below 1.
Exact data are in extension.json and stdout in extension.txt.

Usage: 23,248,896 bytes peak RSS; 3.375 seconds; nice 20; one thread;
600-second alarm. Only the standard library is used. This is measured RSS,
not an operating-system hard memory limit; the largest exact state space
has at most `(8+1)*2^7 = 1152` partitions, and fixed-tree arrays have 256 entries.

Independent audit command launched:
`env OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt`.
It independently generates closed eight-step direction multisets in d=2,...,5,
checks all 179700 pairs of short d=3 paths, evaluates all 8!*8 cycle-inequality
simplex integrals for each of the 15 d=3 graph types, and repeats the final
rational additions with integer LCM/GCD arithmetic.

## 6. Independent audit passed

The audit exited 0. Full stdout is audit.txt; exact checks and 55-digit
decimals are in audit.json. The independent direction-multiset method
matches every induced graph multiplicity in d=2,3,4,5, including the
prediction 8272 in d=5, outside the dimensions used to derive the table.
The total number of paths of lengths 3,5,7 in d=3 is 600; all 179700
unordered pairs have a cycle in their union, checked with explicit edge
and vertex bit masks.

For all 15 graphs, direct integration of the finite MST cycle inequalities
over 8!*8 = 322560 label-order simplices gives exactly the saved d=3
probability. This method uses tree routes and simplex monomials, not
Kruskal partitions. Integer-only LCM/GCD additions independently reproduce
all 11 gains and bounds. Audit usage: 27,262,976 bytes peak RSS, 3.249 seconds,
actual nice 20. No sampling or finite-box extrapolation.

The new d=3 contribution is
`146118665900743508898613/56120415572268307260000000`
`= 0.002603663290992226709...`.
The final bound is
`21272798694838039662654613/56120415572268307260000000`
`= 0.379056328751598078021...`.
The d=2 and d=4 bounds are respectively
`0.582979463810902852976...` and `0.276251488917593282094...`.

Adversarial checks: G01, G03, G08 and G10 have a degree-four vertex and
therefore a zero-spoke vertex in d=2. Zero multiplicities are allowed and
roots with no spoke are skipped. A strict-positive-spoke assumption from
the earlier implementation would not have applied here. The cube's four
induced chords in G02/G06 are retained. Reversal is the only graph
identification used; no unverified isomorphism merges different path events.
Spokes are separate original edges even when exterior endpoints agree.
Distinct path events remain incompatible across lengths. Counts include
both transverse signs but count each path oriented from 0 to e_1 once.

## 7. Written proof, report and final consistency check

PROOF.md contains the full finite-cut argument, density identity, previous
path count, fifteen-row induced-graph table, proof that support counts
extend to every d, exhaustive-enumeration specifications, exact finite
probability formula and its independent integral derivation. REPORT.md
records the partial verdict, the exact improvement, reproduction commands,
limits and next step. The proof explicitly treats zero-spoke vertices.

A preliminary document audit ran under
`env OMP_NUM_THREADS=1 nice -n 15 python3 -` and checked the proof table
against graphs.json and the d=3 displayed arithmetic. It found a draft
transcription error in the common-denominator multiplier: the correct
integer quotient is `60858172908000`, not the draft's `60858236760000`.
The corrected integer identity gives the already saved numerator
`21272798694838039662654613`. No probability, gain or final bound changed.

Added a persistent final_check.py for this document audit.
Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 final_check.py > final_check.txt`.
Exit 0. Output confirms all 15 proof-table edge sets/coefficient triples,
all 158 new probability comparisons, the total 4838400 audited simplices,
all 11 final sums, the displayed d=3 integer identity and bound decimals,
the required verdict, nonempty artifacts and saved resource records.

Final deliverables: LOG.md, PROOF.md, REPORT.md; seven.py, audit.py,
final_check.py; recheck.txt/recheck.json, enumeration.txt/graphs.json,
extension.txt/extension.json, audit.txt/audit.json, final_check.txt.
All files are in this folder. No outside writes, git, or subagents were used.
The result is one additional local certificate length, not a resolution of
the original component question.
