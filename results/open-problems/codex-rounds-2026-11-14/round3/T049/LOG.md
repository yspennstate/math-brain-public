# T049 work log

Task received 15 November 2026, approximately 00:58 Asia/Tbilisi.

## 1. Orientation and bounded literature check (00:58–01:02)

Read the earlier REPORT.md, LOG.md, PROOF.md and verify.py in
`~/codex_op_1114/briefs/T049`; no earlier files were edited.
Read the startup memory and compute state. The governor reports `warn`,
`cpu_saturated`, `owner_away_open`; only small, single-threaded exact arithmetic
will be run, at inherited nice level at least 15. No git or subagents.
The task's folder-only rule precludes mesh/checklist/brain commands that mutate
state elsewhere, so those were not run.

Web searches: `minimal spanning forest Z d connectivity 2025 2026 dimension
open problem`; `minimal spanning forests lattice dimension eight connected
Newman Stein solved`; `"minimal spanning forest" "2026" lattice connected`;
`"minimal spanning forest" "2025" connectivity Z`;
`"minimal spanning forest" "2024" "open"`.

Opened the arXiv pages math/0412263, 1512.09107, 0902.3651, and 2608.10654,
and the full Lyons–Peres–Schramm paper at
https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf . No resolution on full Z^d was
found in the bounded check. Luca Makowiec's *Fixed forests in the minimum
spanning tree and cubic volume growth*, arXiv:2608.10654, concerns complete
graphs. Charles M. Newman, Vincent Tassion and Wei Wu's slab result remains
distinct from full Z^3. T. S. Jackson and N. Read, *Theory of minimum spanning
trees I: Mean-field theory and strongly disordered spin-glass model*,
arXiv:0902.3651, propose critical dimension six on mean-field/scaling grounds,
not a lattice theorem; hence eight should not be presented as a settled
critical-dimension prediction. This older caveat changes no rigorous status.

## 2. Recheck and chosen extension (recorded before implementation)

The earlier deterministic argument holds: deleting an internal edge of a
finite wired MST gives a finite fundamental cut with that edge as its unique
minimum. It therefore belongs to the infinite free MSF. Different simple
paths between the same endpoints cannot both belong to a forest, even if
their interiors overlap. The box argument for P(e in F)=1/d also checks out.

First independently implement the probability calculation, comparing an
edge-subset contraction sum and a cycle-inequality integral with the earlier
reported fractions. Do not import or execute the earlier script, which writes
data in its working directory.

Chosen extension: include every simple five-edge path from 0 to e_1 avoiding
the direct edge, wiring the complement of its six vertices. These certificate
events are incompatible with one another and with all earlier three-edge
certificates. Exact evaluation therefore gives an additive improvement to
the previous bound. Check induced chords rather than assuming every six-cycle
is chordless. This is one local certificate extension, not a component theorem.

## 3. Independent recheck completed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 verify_paths.py --recheck > recheck.txt`.
Exit 0. All 11 earlier probabilities and connectivity bounds for d=2,...,12
agree exactly with both freshly implemented methods. In particular a_4 is
5521/658350 and the d=3 bound is 120767/329175. The earlier result holds.
The code reads the old data only for final comparisons, never imports the old
implementation. Full output: recheck.txt; exact data: recheck.json.
Measured peak RSS 17,530,880 bytes, elapsed 0.0119 seconds, nice 20, OMP=1.
The nice wrapper warns because its relative increment exceeds the inherited
priority ceiling; Python verifies the actual priority is 20.

Next implementation: enumerate all length-five self-avoiding detours, retain
every lattice edge induced by their six vertices, and evaluate each distinct
induced graph with its correct external spoke multiplicities. Independently
count six-cycles using planar rectangles and the unit three-cubes containing
the fixed edge. This specifically audits the chords and path multiplicities.

## 4. Extension computed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 verify_paths.py --extend > extension.txt`.
Exit 0, tool wall time 0.719 seconds. All exact probability comparisons and
geometry checks passed for d=2,...,12. Full stdout is extension.txt, rational
data and resource measurements are extension.json; all 44 explicit d=3
paths are in paths_d3.json; grouped cycle-integral factors are in
integral_terms.json.

The exhaustive walk and the independent rectangle/cube count agree:
there are (d-1)(16d-26) five-edge detours. Types C, A, B have multiplicities
4(d-1)(d-2), 2(d-1)(2d-3), 4(d-1)(2d-3), respectively. C has no chord;
A has chord 14 and B has chord 03 when the path is 01,12,23,34,45 and
the excluded direct edge is 05. Reversal identifies chord 25 with type B.
The six-cycle in type A/B has two degree-three vertices with one fewer
external spoke than the other four vertices. Treating these as chordless
would have been wrong; the implementation retains these chords.

An independent abstract-cube enumeration gives four chordless and twelve
chorded six-cycles per cube, with 2,2,4 cycles through a specified cube edge
of types C,A,B. This uses combinations of six edges and degree/connectivity
checks, not the self-avoiding-walk routine.

The exact d=3 probabilities are
`b_C=187806637/902104087500`,
`b_A=44663374963/205507902600000`,
`b_B=14856501533/67257131760000`. The new contribution is
`8829469757/922150845000`; the total bound is
`347146143557/922150845000 = 0.376452665460605...`.
Measured extension usage: peak RSS 18,186,240 bytes, elapsed 0.7501 seconds,
nice 20, one thread, standard library only, 180-second alarm.

## 5. Adversarial audit and written proof

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt`.
Exit 0. A third calculation recursively conditions directly on successful
partitions, without first fixing a final tree. All 33 six-vertex
probabilities agree exactly. Explicitly constructed all 48 paths of lengths
three and five in d=3; every one of the 1128 path pairs has a cycle in its
union, including overlapping paths. Recomputed the d=3 gain and final bound
using integer LCMs/GCDs, independently of the Fraction summation producing
the results. Every probability exceeds the crude sufficient event that the
five path edges are first; every final bound is strictly between the old
bound and one. Full output is audit.txt. Peak RSS 16,334,848 bytes, nice 20.

PROOF.md now contains the finite-cut implication, the edge-density argument,
the complete rectangle/cube classification and multiplicities, explicit
finite-sum probabilities, an independent ordered-simplex integral derivation,
and the exact d=3 result. In particular, it handles zero chordless multiplicity
in d=2, distinct spokes with a common exterior endpoint, extra induced
chords, and paths sharing vertices or edges.

## 6. Final deliverables and audit

REPORT.md starts with the required PARTIAL verdict and records the exact
improvement, reproduction commands, literature qualifications, limitations,
and next steps. A final read-only file audit confirmed all twelve authored
artifacts are present and nonempty (LOG.md, PROOF.md, REPORT.md, two scripts,
three stdout files, and four JSON files). Read the complete proof again;
the count handles two-axis and three-axis cycles separately, and the
finite-cut argument remains independent of the exterior completion.

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 -` with Decimal precision
40, reading extension.json. Independently checked the displayed decimals:
d=3 bound is 0.3764526654606058513..., gain 0.0095748648985947630...;
d=2 bound is 0.5781698982796088305...; d=4 bound is
0.2749666000615474705... . Corrected rounded numbers followed by ellipses
in the prose to actual truncated expansions. The saved stdout tables use
explicitly rounded twelve-place formatting and remain correct.

No tests failed, no simulations were used, no earlier files were edited,
and all new files remain in this folder. The next step is stated in the
report; the full lattice component problem remains open in this work.

Final consistency command checked the saved PASS statuses, required verdict,
and agreement of the proof/report decimal strings with 50-digit Decimal
evaluation. Output: `PASS final report, proof, saved checks, and decimal consistency`.
