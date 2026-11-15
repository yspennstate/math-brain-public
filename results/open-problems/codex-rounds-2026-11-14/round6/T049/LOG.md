# T049 work log

Task: “take the NEXT checkable step on this problem, building on that work”;
received 15 November 2026, approximately 10:03 Asia/Tbilisi.

## Orientation and bounded literature check (10:03–10:06)

Read the startup memory index and compute state. The governor reports `warn`,
`owner_away_open`, with swap paging; calculations will remain small and serial.
The specific order to write only in this folder overrides the global commands
that mutate mesh/checklist/brain stores elsewhere. None of those commands, git,
subagents, or external writes will be used. Read-only orientation used `pwd`,
`rg --files`, `cat`, `date`, `wc`, and `sed`.

Web search tool queries: `"minimal spanning forest" "Z" "2026" connected`
and `"minimal spanning forest" lattice connectivity open problem dimension 8
2025 2026`. Opened the following arXiv pages (abstracts and metadata):

- Russell Lyons, Yuval Peres and Oded Schramm, *Minimal spanning forests*,
  https://arxiv.org/abs/math/0412263 .
- Charles M. Newman, Vincent Tassion and Wei Wu, *Critical Percolation and the
  Minimal Spanning Tree in Slabs*, https://arxiv.org/abs/1512.09107 .
- Shirshendu Chatterjee, Yang Chen and Grigory Terlov, *β-Skewed Maximal
  Spanning Forests*, https://arxiv.org/abs/2609.11845 .
- Luca Makowiec, *Fixed forests in the minimum spanning tree and cubic volume
  growth*, https://arxiv.org/abs/2608.10654 .

No later solution of full-lattice connectivity was found. The recent abstracts
concern weighted forests on nonunimodular graphs and the complete-graph MST;
the older slab result does not resolve full Z^3. This is a bounded search,
completed in less than five minutes, not an exhaustive literature certificate.

Reading all four earlier folders, including their proofs, logs, and scripts.
The latest proof's finite-cut monotonicity and strict-inclusion construction
survive direct mathematical inspection. An independent arithmetic recheck
will precede the extension.

## Independent recheck completed

Read the reports, complete proofs, logs and all Python scripts from all four
earlier folders. No earlier code was imported or executed. Read the startup
scar about relative `nice` stacking; use `os.getpriority`, not `os.nice(0)`.

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 recheck.py > recheck.txt`.
Exit 0. Fresh integration of exponential MST cycle inequalities, using tree
routes and a suffix recurrence, reproduces all 202 square/five-edge/seven-edge
probabilities for d=2,...,12 and all preceding bound sums. A full unreduced
graph calculation additionally reproduces every partial one-end enlargement
for d=2,3 (eight probabilities). In particular the latest d=3 square value
is exactly `7175020914436910477/722017042450235532000`, and inserting it
reproduces `237831533319331629226140743/617324571294951379860000000`.
The earlier main result holds. Runtime 1.6424 seconds; peak RSS 16,351,232
bytes; actual nice 20; one thread; 600-second alarm. The relative-nice
wrapper prints a warning because the inherited priority is already 20.

## One extension selected, before implementation

Add every exterior neighbor of the other endpoint as well. Replace each
one-end enlarged square event by the MST certificate in this larger induced
region, keeping all five-edge and seven-edge terms. Prove nesting and strict
inclusion and evaluate exactly at least d=2,3, subject to the resource bounds.

The full region is the square together with the neighbors of both endpoints
of its excluded direct edge. It has 4d vertices. Unlike the earlier region,
the added vertices are not all pendant: there are 2d-3 edges joining matched
neighbors across the two endpoints, in addition to two unmatched leaves.
Retain these induced edges. A direct partition recursion can compute the
probability without assuming independent effective root edges. An independent
fixed-final-tree cycle integral will audit the resulting probability in d=3.
This choice directly addresses the obstruction named in the latest report.
Only one region is counted per square, so no same-path event is added twice.

## Both-end enlargement computed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 both_ends.py --last 3 > extension.txt`.
Exit 0. The direct full-graph partition recursion gives a strictly larger
square probability in both d=2 and d=3. It independently rechecks the old
one-end probability on the way. The d=3 full graph uses 236,132 states,
below the explicit 300,000-state guard; no higher-dimensional exact
evaluation is attempted with this uncompressed recursion.

New d=3 square probability:
`106821527499174906671287753163603/8994156750072383564239397632800000`
`= 0.0118767696035890439374...`.
Gain over the latest bound:
`191866255331224667993946415505833/24733931062699054801658343490200000`
`= 0.0077572083000011215234...`.
New bound:
`265115546365736108233965694737821273/674561756255428767317954822460000000`
`= 0.3930189399372764987779...`.

The d=2 bound is `84815746280753023/140256167203152000`
`= 0.6047202627311417414226...`.
Runtime 8.4466 seconds; peak RSS 115,720,192 bytes; actual nice 20;
one thread; 900-second alarm. Exact fractions and full geometry are
checkpointed in extension.json; stdout is extension.txt.

Next: independently enumerate the final spanning trees containing the
specified path, then integrate their cycle inequalities. The 2d-3 matched
neighbor pairs form separate four-terminal-edge branches after contraction
of the desired path. Enumerating their local rooted forests reduces the
tree list; exchangeable branches and reflection may group equal integrals.
This is an arithmetic audit of the chosen extension, not another extension.

## Independent integral audit passed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt`.
Exit 0. The separate tree-route/density integral gives exactly the two
probabilities in extension.json. There are 128 final tree shapes in d=2
and 12,288 in d=3. Branch permutations and endpoint reflection reduce
these to respectively 64 and 1,296 distinct integrals. Their multiplicities
are checked, and each representative is independently verified to be a
spanning tree. Each integral sums all tree-label orderings by a suffix
recurrence; no transition probabilities from the main recursion are used.
The exact final sums, all induced edges and all exterior degrees also pass
independent checks. Runtime 31.6915 seconds; peak RSS 19,611,648 bytes;
actual nice 20; one thread; 900-second alarm.

PROOF.md now gives the complete finite-cut, nesting, strict-inclusion and
disjointness arguments; all-dimension graph and exact recurrence; the
exhaustive final-tree classification; the independent integral derivation;
and the two displayed evaluations. The strict-inclusion event uses the
new unmatched vertex 2e_1, so the matched-neighbor edges do not interfere.

Additional adversarial check launched: enumerate every subset of the
required size in the d=2,3 graphs, without the local-forest classification,
and compare its actual spanning trees against every symmetry multiplicity
in the integral audit. Also build all 132 oriented squares in d=2,...,12,
check original incident-edge counts, verify the strict-inclusion witness
by deterministic Kruskal, and construct a counterexample showing why
deleting a matched-neighbor edge can give a false path certificate.

## Adversarial audit completed; written report and final check

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 adversarial.py > adversarial.txt`.
Exit 0. Unstructured edge-subset enumeration checks 792 candidates in d=2
and 497,420 in d=3. Its full tree-orbit counters agree with every symmetry
multiplicity in the integral calculation, not merely their totals. All
132 oriented lattice geometry checks, strict-inclusion witnesses, and
missing-edge counterexamples pass. Runtime 1.5742 seconds; peak RSS
21,102,592 bytes; actual nice 20; one thread; 600-second alarm.

REPORT.md records the partial result, exact improvements, commands, scope
and next step. No arithmetic or geometry comparison has failed. First
command `env OMP_NUM_THREADS=1 nice -n 15 python3 final_check.py > final_check.txt`
exited 1 because the document check requires every computed fraction to
appear in both proof and report, while the report omitted the d=2 gain
fraction. Added that fraction; no numerical result changed. Rerunning the
document consistency check is required after this correction.

Final command: `env OMP_NUM_THREADS=1 nice -n 15 python3 final_check.py > final_check.txt`.
Exit 0. The check recomputes the weighted sum of every saved final-tree
integral, verifies both new probabilities, gains and bounds, checks all
quoted fractions and decimal prefixes in both documents, validates the
exhaustive tree counts and every saved resource record, and confirms the
required verdict and all deliverables. Full stdout is final_check.txt.
All authored files are in this folder. No earlier files, external stores,
repositories, or external applications were modified.

The completed step is the two-end enlargement and its exact d=2,3
evaluation. The full-lattice component problem is still unresolved here.
For d>=4 only the finite recurrence and strict-improvement proof are
claimed; no higher-dimensional numerical result is reported.
