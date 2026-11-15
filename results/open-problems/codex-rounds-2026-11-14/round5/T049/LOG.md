# T049 work log

Task: “take the NEXT checkable step on this problem, building on that work”,
received 15 November 2026, approximately 07:40 Asia/Tbilisi (03:40 UTC).

## Orientation and bounded literature check

Read the reports, logs, proofs and scripts in the original, round 3 and
round 4 folders. Read the startup memory and compute-state file. The latter
reports `warn`, `cpu_saturated`, `owner_away_open`; use only small single-thread
standard-library computations under `env OMP_NUM_THREADS=1 nice -n 15`,
with an actual-priority check, a deadline and measured peak RSS.
The wrapper warns because inherited nice is already 20.

The task-specific prohibition on writes outside this folder takes precedence
over global mesh/checklist/brain commands, which write elsewhere. Those
commands are not run. No git, subagents or outside mutations.

The web check occupied less than five minutes. Queries included
`"minimal spanning forest" "Z" connected 2025 2026`,
`"minimal spanning forests" lattice open problem dimension connected`,
`"minimal spanning forest" lattice 2026 connectivity`, and
`"minimal spanning forest" "Z^d" 2025`.
Opened the following primary sources:

- Russell Lyons, Yuval Peres and Oded Schramm, *Minimal spanning forests*,
  https://arxiv.org/abs/math/0412263 and
  https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf .
- Charles M. Newman, Vincent Tassion and Wei Wu, *Critical Percolation and
  the Minimal Spanning Tree in Slabs*, https://arxiv.org/abs/1512.09107 .
- Shirshendu Chatterjee, Yang Chen and Grigory Terlov, *β-Skewed Maximal
  Spanning Forests*, https://arxiv.org/abs/2609.11845 .
- Luca Makowiec, *Fixed forests in the minimum spanning tree and cubic
  volume growth*, https://arxiv.org/abs/2608.10654 .

The last three were read at abstract level. No later solution on full Z^d
was found. The slab, weighted-forest and complete-graph results do not
announce such a solution. This is a bounded search, not a definitive
bibliographic exclusion. No SOLVED_ELSEWHERE.md is warranted.

## Earlier result: deterministic check and planned independent computation

The finite-cut implication is valid: an internal edge of a finite wired MST
is the unique minimum of its finite fundamental cut. Different simple paths
between the same endpoints are incompatible in a forest even when they
overlap. The boundary-to-volume proof of P(e in F)=1/d holds.

Before extending the result, independently implement the cycle-inequality
integral by a subset recurrence using tree routes, not accepted-component
transitions. Compare every earlier square, six-vertex and eight-vertex
fraction and every final bound for d=2,...,12. Independently rebuild the
seven-edge path counts in d=2,...,5 from lattice coordinates. Earlier JSON
files are comparison data only; no earlier Python code is imported or run.

## Independent earlier-result recheck completed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 recheck.py > recheck.txt`.
Exit 0. The independent tree-route integral recurrence matches all 11 square,
33 six-vertex and 158 active eight-vertex probabilities, and every saved
bound for d=2,...,12. Coordinate enumeration matches all graph multiplicities
in d=2,3,4,5, with 28, 552, 2868, 8272 seven-edge paths respectively.
The earlier result holds, including its d=3 bound
`21272798694838039662654613/56120415572268307260000000`.
Runtime 1.951 seconds, peak RSS 17,367,040 bytes, actual nice 20.
Full output and exact check counts: recheck.txt and recheck.json.

## One extension selected before implementation

Enlarge each square certificate by adding all exterior neighbors of its
initial endpoint 0. There are m=2d-2 added vertices; the induced graph is
the square with m pendant vertices, each with m+1 edges to the wired root.
Keep the earlier five-edge and seven-edge certificates. The enlarged
square events still force the same three-edge paths and hence remain
incompatible with all distinct-path events. Prove wired-region monotonicity
so that the old square event is included in its enlargement; do not add
overlapping probabilities for the same path.

Reason for this choice: it implements the earlier report's alternative of
enlarging wired regions, while a series/parallel reduction makes the exact
calculation small. With exponential labels, an added pendant branch has
effective label max(X,Y), where X has rate 1 and Y has rate m+1. Its survival
function is e^(-t)+e^(-(m+1)t)-e^(-(m+2)t). For k added leaves the effective
root label at 0 has a finite signed exponential expansion. Evaluate the
result as a finite linear combination of weighted five-vertex MST
probabilities. Independently check with a direct Kruskal recursion tracking
counts of leaves attached to 0 or to the root. Aim for an all-dimension
formula and exact comparisons in d=2,...,12, subject to the resource limits.

## Enlarged square probabilities completed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 enlarge.py --last 12 > extension.txt`.
Exit 0. Every probability for k=0,...,2d-2 added leaves, d=2,...,12,
agrees exactly between the signed effective-edge expansion and an independent
recursion on square partitions plus counts of attached leaves. All 143
probabilities are strictly increasing with k in each dimension. Actual
lattice-neighbor construction confirms every induced edge and spoke
multiplicity. Replacing the earlier square term gives a strict gain in
all eleven dimensions. Results are checkpointed in extension.json;
full fractions and resource records are in extension.txt.

Runtime 2.228 seconds, peak RSS 32,030,720 bytes, actual nice 20, one thread,
900-second alarm. Largest direct-recursion state count is 7732. No sampling.
These are measured RSS limits and bounded finite states, not an OS-enforced
memory cap. The wrapper's priority warning does not affect actual nice 20.

Next audit: calculate the full finite graph without either reduction or
leaf-count aggregation in d=2,3; enumerate its possible final spanning
trees and directly integrate their cycle inequalities. Recheck final sums
by integer LCM/GCD arithmetic. Prove nesting by finite cuts and exhibit
a positive-probability strict-inclusion event, rather than inferring these
facts from numerical monotonicity.

## Independent full-graph audit passed

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt`.
Exit 0. A generic partition recursion on the unreduced graph matches every
k in d=2,3. A fourth probability calculation enumerates all final spanning
trees containing the specified path, with parallel edges collapsed by
their exponential minima, and integrates every cycle-inequality simplex.
For d=2 there are 16 tree shapes and 11,520 simplices; for d=3 there are
80 tree shapes and 3,225,600 simplices. Both exact results agree.
Integer-only LCM/GCD arithmetic confirms all eleven gains and final bounds.
Signed-survival coefficients pass normalization, zero initial density and
an exact rational-point evaluation. No comparison failed.
Runtime 2.505 seconds, peak RSS 20,152,320 bytes, actual nice 20.

The new d=3 square probability is
`7175020914436910477/722017042450235532000`.
Replacing four earlier square certificates adds
`1120101659682220157/180504260612558883000`
`= 0.006205402885677299232...`.
The complete bound becomes
`237831533319331629226140743/617324571294951379860000000`
`= 0.385261731637275377254...`.
The d=2 and d=4 bounds are respectively
`0.592724316686007828922...` and `0.280202821595373250359...`.

The deterministic audit establishes nesting through fundamental cuts. For
strictness, choose a newly added pendant edge and an exterior spoke at a
different square vertex to be lighter than a desired path edge. In the
smaller wired graph those two edges bypass that path edge through the root;
in the larger graph all other edges at the new leaf are heavier, so this
bypass disappears. A precise positive-probability interval event is written
in PROOF.md. The enlargement replaces each earlier square probability;
it is not added as a second overlapping certificate for the same path.

## Written proof, report and final document audit

PROOF.md gives the all-dimension bound, exact finite formula, complete
finite-cut and strict-inclusion arguments, series/parallel reduction,
signed-density derivation and independent full-graph integral calculation.
REPORT.md begins with the required PARTIAL verdict and records the gain,
limits, reproduction commands and next step. This finishes one extension:
replace the square terms by certificates in larger wired regions.

Command: `env OMP_NUM_THREADS=1 nice -n 15 python3 final_check.py > final_check.txt`.
Exit 0. All 202 earlier probabilities, 143 enlarged probabilities, eight
generic full-graph checks, 96 full-graph tree shapes, 3,237,120 explicit
simplex integrals and eleven integer sums have saved passing records.
The final audit independently reconstructs induced edges by pair distances,
checks all spokes and edge counts, multiplies survival polynomials by
literal convolution, and checks every quoted fraction and decimal against
the exact data. The required verdict and all thirteen input artifacts
are present. Runtime 0.007 seconds, peak RSS 17,039,360 bytes, nice 20.

No numerical or geometric comparison failed. The original component problem
is unresolved by this result. All authored files remain inside this folder;
the three earlier folders were read only. No git, outside writes, subagents,
sampling, GPU or external publication was used.
