# T101 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received approximately 04:52 Asia/Tbilisi, 15 November 2026.

## 04:52–04:56 — orientation and literature

Read both earlier folders' REPORT.md, LOG.md, PROOF.md and Python scripts.
Earlier folders remain read-only. Read the startup memory and compute state:
warn, owner_away_open, CPU saturated, 67% free memory. Use tiny single-thread
jobs only. The task's folder-only order overrides shared brain, mesh and
checklist writes; none are run. No git, subagents or external writes.

Web search tool queries: `Lorentz mirror model square lattice all trajectories
finite conjecture 2026 2610.12460` and `Lorentz mirror model periodic orbits
proof 2026 November`. Opened:

- Martin P.W. Zerner, *Infinite light rays and infinite clusters with infinitely
  many pivots*, https://arxiv.org/abs/2610.12460 and
  https://arxiv.org/html/2610.12460v1. The square-lattice problem remains open;
  the infinite examples use other planar graphs.
- Gady Kozma and Vladas Sidoravicius, *Lower bound for the escape probability
  in the Lorentz Mirror Model on the lattice*, https://arxiv.org/abs/1311.7437.
  Its abstract gives the lower bound 1/(2n+1).
- Jian Gu and Qin Hao, *Boundary transmission and excursion geometry in the
  Lorentz mirror model: a numerical study*, https://arxiv.org/abs/2609.14949.
  Its abstract explicitly does not resolve infinite-plane localization.

No later solution found; literature search ends within five minutes.

## Choice before calculation

First independently re-enumerate cell interiors and sum gap weights for the
eight-corner result. Then extend ONE piece: exact ten-corner vertex-simple
orbit contribution, as the round-3 report requests. Five horizontal and five
vertical sides imply at most five corner coordinate levels in each axis;
therefore every rank polygon fits in a four-by-four cell box. Exhaust all
65,535 nonempty subsets. Independently enumerate cyclic coordinate sequences
and compare individual polygons, then test rooted counts using unit walks.
No claim about unrestricted localization is intended.

## First execution and portability correction

Wrote ten_cells.py using Gray-code cell subsets, XOR boundaries, cycle and
rank checks, exact polynomial arithmetic and direct horizontal root weights.
Command: `nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 ten_cells.py --stage recheck`.
The first execution stopped before enumeration: macOS rejected RLIMIT_AS with
`ValueError: current limit exceeds maximum limit`. Removed that unsupported
limit; the data structures are tiny and peak RSS is explicitly checked.
CPU limit remains 180 seconds. The nice warning is inherited priority 20,
as in the prior sessions; the script checks priority >=15.

## Earlier eight-corner result holds

Reran the same recheck command successfully. Independent cell enumeration:
38 shapes; gap groups 8 of (1^5), 18 of (1^6), 8 of (1^5,2), 4 of (1^4,2).
Polynomial numerator [0,0,0,0,0,8,14], denominator (1-r)^6.
Thus F8=2r^5(4+7r)/(1-r)^6, independently recovering the earlier formula.
Direct horizontal-root sums at p=1/10,1/4,1/2,3/4 give respectively
5797575/14301947824, 3303/3294172, 7/3888, 549/312500, exactly as reported.
The small-density coefficient is independently 33/8192, hence the earlier
total is 225/8192. Rooted counts at lengths 10,12,14,16,18,20 are
40,372,1764,5936,16128,37800. Elapsed 0.006 s, peak RSS 16,236,544 bytes,
priority 20. Saved earlier_recheck.json. Proceed with the chosen ten-corner
extension; no discrepancy in the earlier mathematical result.

## Ten-corner cell calculation

Command: `nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 ten_cells.py --stage ten`.
Exhausted 65,535 nonempty subsets. Found 528 distinct rank polygons.
With t=r/(1-r), u=r^2/(1-r^2), the gap groups give
F10=16t^6+32t^5u+80t^7+120t^6u+32t^5u^2+8t^4u^3
    +84t^8+88t^7u+52t^6u^2+16t^5u^3.
Exact polynomial reduction gives
F10=r^6(16+112r+220r^2+176r^3+48r^4)/[(1-r)^8(1+r)^2].
Rooted counts at lengths 12,14,16,18,20: 96,1456,10080,46440,165160.
Direct horizontal-root sums at p=1/10,1/4,1/2,3/4:
6556803748382475/30615271547451923824,
1286614341/2522100437500, 33971/39366000,
31766271/38382812500.
Leading gap singularities give R10/p -> 143/65536.
Elapsed 0.402 s, peak RSS 17,793,024 bytes, priority 20.
Saved ten_data.json, including all 528 individual corner lists and cell rows.
These are provisional until an independent coordinate enumeration and unit
walks agree. Unlike F8, this F10 retains a pole at r=-1.

## Independent audits passed

Command: `nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit_ten.py --max-length 20`.
This script imports no enumeration or algebra functions from ten_cells.py.
Its first method represents boundaries by ten alternating axis-parallel
segments, rejecting any intersection between nonadjacent segments directly.
There are 0,30,120,120 cyclic surjective coordinate sequences on 2,3,4,5
ranks respectively: 72,900 candidate coordinate pairs, 5,280 valid
representations, exactly 528 polygons. The individual edge sets agree with
every cell-enumerated polygon. Rooted unit walks (2,441,388 search nodes)
independently agree at every even perimeter through 20, for 4,6,8,10 corners.
The ten-corner counts are 96,1456,10080,46440,165160 at 12,14,16,18,20.

Differentiating the exact F10 gives
G10=8r^6(12+110r+312r^2+405r^3+247r^4+58r^5)
       /[(1-r)^9(1+r)^3].
An independent signed-binomial convolution from this expression agrees with
positive gap dynamic programming through perimeter 60. Direct total-length
gap sums agree with the horizontal-root sums and the closed probability at
four rational densities. Independent perimeter partial sums through
semiperimeter 500 agree at those densities and p=1, with rigorous tails
smaller than 10^-30 (exact rational bounds saved).

Outputs:
  p=1/10: R10=6556803748382475/30615271547451923824,
          B10=49899511535164075/15307635773725961912
  p=1/4: R10=1286614341/2522100437500, B10=5980962179/630525109375
  p=1/2: R10=33971/39366000, B10=497923/19683000
  p=3/4: R10=31766271/38382812500, B10=522240549/9595703125
  p=1: R10=0, B10=1/8
Leading eight-gap coefficient is 84+88/2+52/4+16/8=143.
Thus R10/p -> 143/65536, and B10/p -> 1943/65536, checked again by
substitution into the closed numerator. Elapsed 2.524 s, peak RSS 20,267,008
bytes, priority 20. Saved ten_audit.json.

No mathematical discrepancy found. Writing the full proof and checking
edge-root multiplicity, odd cyclic coordinate obstruction on two ranks,
boundary contacts/holes, the tail majorant and p=1 separately.

## Proof and report written

PROOF.md now gives the polygon event argument, exact horizontal-root
multiplicity, rank compression, the complete grouped classification with
an exhaustive rule, the independent sequence counts and segment test,
the full common-denominator expansion, derivative, probability formula,
limiting coefficient, binomial coefficients and rigorous tail proof.
REPORT.md begins with the required PARTIAL verdict and states the exact
scope. The data contain all 528 shapes; no previous folder was edited.

Adversarial review: all nonadjacent segment contacts are rejected, holes
and degree-four cell contacts are rejected, translations are normalized,
rotations are not accidentally quotiented, and the root contributes no
extra traversal factor. The odd five-cycle excludes two-rank coordinate
words, which the independent enumeration confirms. A pole at -1 survives
(A(-1)=-4), so the simpler eight-corner denominator cannot be extrapolated.
For the tail majorant, the composition bound requires m>=16; our omitted
tail starts at 501. The decreasing ratio is q^2(m+1)/(m-7), hence the
chosen rho=q^2(502/494). The endpoint p=1 is treated without q^-10.
No localization conclusion follows from the lower bound.

A document-writing tool call had a JavaScript syntax error before execution
(Markdown fences inside a template literal). It changed no files; the
corrected call wrote the report with indented command blocks.

## Final verification

Reran the three documented commands after the proof/report audit. The earlier
recheck again gave 38 polygons and coefficient 33/8192 (0.0062 s,
17,154,048 bytes RSS); the ten-corner calculation again gave 528 and
143/65536 (0.4113 s, 17,448,960 bytes RSS). The independent audit again
matched all 528 boundaries, all rooted walk counts through twenty, and all
five rational probability/tail checks (2.4223 s, 20,267,008 bytes RSS).
Every run verified priority 20 and OMP_NUM_THREADS=1.

Final read-only artifact inspection used a Python heredoc under the same
`nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3` prefix.
It parsed both scripts with ast, compared every row of the proof's finite
table with ten_data.json, checked the report's exact first line, checked
document control characters, and matched the stated constants and exact
tail fields with ten_audit.json. Output:
`PASS report verdict, proof table against data, Python syntax, document control characters, audit constants`.
The eight result artifacts totaled 485,888 bytes before this final log entry.

Finished with a PARTIAL result: exact ten-mirror contribution and improved
explicit bound, fully audited within its restricted scope. The all-orbit
periodicity conjecture remains open. No git, external writes, shared-state
registration, background processes or subagents were used.
