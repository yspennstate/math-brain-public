# T101 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 01:28 Asia/Tbilisi.

## 01:28–01:30 — orientation and bounded literature check

Read the earlier REPORT.md, LOG.md, PROOF.md, and the complete audit.py in
`~/codex_op_1114/briefs/T101`, without editing them.
Read the startup memory index and compute state. The latter reports `warn`,
`owner_away_open`, 50% free RAM and CPU saturation; use small single-thread runs.
All task artifacts stay here. No git, subagents, posting, or mesh/checklist/brain
writes: the task's folder-only order takes precedence over global write routines.
One initial brain recall was launched before reconciling that scope; it found no
T101 memory. No further brain commands will be run.

Web search tool queries included `Lorentz mirror model square lattice all
trajectories finite conjecture 2026 2610.12460`, `Lorentz mirror model periodic
orbits solved November 2026`, `"Lorentz mirror" "2026" "November" finite`, and
`"Lorentz mirror" "solved" "conjecture" 2026`. Opened:

- Martin P.W. Zerner, *Infinite light rays and infinite clusters with infinitely
  many pivots*, [arXiv:2610.12460v1](https://arxiv.org/html/2610.12460v1).
  Abstract and introduction retain the square-lattice finiteness conjecture;
  the infinite examples use other plane graphs. Its parameter is the probability
  of each mirror orientation, half the total density used here.
- Gady Kozma and Vladas Sidoravicius, *Lower bound for the escape probability in
  the Lorentz Mirror Model on the lattice*,
  [arXiv:1311.7437](https://arxiv.org/abs/1311.7437). Abstract gives the
  `1/(2n+1)` lower bound.
- Jian Gu and Qin Hao, *Boundary transmission and excursion geometry in the
  Lorentz mirror model: a numerical study*,
  [arXiv:2609.14949](https://arxiv.org/abs/2609.14949). Abstract explicitly says
  it does not resolve infinite-plane localization.

No later solution found in this search of less than five minutes. Literature
phase ended; this is not an exhaustive review.

## Choice, before calculation

First independently enumerate compressed coordinate patterns for four- and
six-corner simple polygons, sum arbitrary positive coordinate gaps, and compare
with the earlier formula. Then extend precisely the same finite method to eight
corners, the earlier report's requested next step. Coordinate compression avoids
assuming a visual classification of the two-reflex-corner shapes. Every eight-
corner orthogonal polygon uses at most four distinct x coordinates and four
distinct y coordinates, so the compressed search is small and exhaustive.
An independent rooted unit-walk search will test the resulting perimeter counts,
including the previous audit targets 40, 372, 1764 at perimeters 10, 12, 14.
The general all-orbit conjecture is outside the conclusion of this calculation.

## Earlier result independently rechecked — holds

Command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 eight_corners.py --stage earlier --max-length 16 --output earlier_recheck.json
```

Output (the warning comes from inherited nice 20, confirmed in the script):

```text
nice: setpriority: Operation not permitted
k=4: candidates=4, valid_representations=4, skeletons=1, gap_groups={(1, 1): 1}
root_counts={'4': 2, '6': 6, '8': 12, '10': 20, '12': 30, '14': 42, '16': 56}
k=6: candidates=36, valid_representations=24, skeletons=4, gap_groups={(1, 1, 1, 1): 4}
root_counts={'4': 0, '6': 0, '8': 16, '10': 80, '12': 240, '14': 560, '16': 1120}
priority=20; elapsed_seconds=0.000765; peak_rss_bytes=16629760
```

This is a new enumeration, not a rerun of the earlier audit: alternate horizontal
and vertical corner coordinates, reject repeated boundary vertices, and quotient
only by cyclic starting point and direction of traversal. The unrooted
semiperimeter series are `(r/(1-r))^2` and `4(r/(1-r))^4`. By coordinate
interchange, the rooted series is `r` times the derivative of the unrooted
series. These give exactly the earlier two probabilities, hence its formula for
all p, its coefficient `3/128`, and its value `11/486` at p=1/2. Direct
horizontal-root rational summation also agrees at p=1/10,1/4,1/2,3/4; the full
exact fractions are saved in earlier_recheck.json. No flaw found.

Proceeding with the chosen eight-corner extension. The script has a CPU limit of
180 seconds, checks inherited priority >=15 and peak RSS <1 GB, imports only
the standard library, and runs one thread.

## Eight-corner enumeration completed

Command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 eight_corners.py --stage eight --max-length 16 --output eight_data.json
```

Relevant output:

```text
k=8: candidates=1444, valid_representations=304, skeletons=38
gap_groups={(1, 1, 1, 1, 2): 4, (1, 1, 1, 1, 1): 8,
            (1, 1, 1, 1, 1, 1): 18, (1, 1, 1, 1, 1, 2): 8}
root_counts={'4': 0, '6': 0, '8': 0, '10': 40, '12': 372, '14': 1764, '16': 5936}
exact_probabilities=[{'p': '1/10', 'probability': '5797575/14301947824'},
 {'p': '1/4', 'probability': '3303/3294172'},
 {'p': '1/2', 'probability': '7/3888'},
 {'p': '3/4', 'probability': '549/312500'}]
PASS independent rooted walks through length 16; nodes=83652
priority=20; elapsed_seconds=0.061185; peak_rss_bytes=17399808
```

The previous targets 40,372,1764 all agree. Let `t=r/(1-r)` and
`u=r^2/(1-r^2)`. The unrooted series inferred from the exhaustive rank list is
`F8=8t^5+18t^6+4t^4u+8t^5u`. Algebra simplifies it to
`2r^5(4+7r)/(1-r)^6`; hence `r F8'=4r^5(10+23r)/(1-r)^7`.
This predicts the exact eight-mirror contribution
`R8(p)=p(1-p)^2[10+23(1-p)^2]/[64(2-p)^7]`.
Its small-p coefficient is `33/8192`. Adding the earlier bound predicts
`225/8192` and value `95/3888` at p=1/2. These algebraic consequences will be
audited independently before final reporting. Need a fully explained finite
classification in PROOF.md; the raw 38 skeletons are saved in eight_data.json.

## Independent classification and algebra audit passed

Command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit_cells.py
```

This script shares no enumeration functions with eight_corners.py. It takes
the symmetric difference of the four edges of each cell in all 511 nonempty
subsets of a 3-by-3 cell box; it retains one simple boundary cycle with exactly
eight corners and every coordinate level used by a corner. It found exactly
the same 38 skeletons, including their individual corner lists, not just totals.

```text
PASS: all 511 nonempty subsets of a 3x3 cell box; identical 38 skeletons
width,height,gaps=(2, 3, (1, 1, 1, 1, 1)): count=4
width,height,gaps=(2, 3, (1, 1, 1, 1, 2)): count=2
width,height,gaps=(3, 2, (1, 1, 1, 1, 1)): count=4
width,height,gaps=(3, 2, (1, 1, 1, 1, 2)): count=2
width,height,gaps=(3, 3, (1, 1, 1, 1, 1, 1)): count=18
width,height,gaps=(3, 3, (1, 1, 1, 1, 1, 2)): count=8
PASS: exact rational shape sums and binomial-series tails <1e-30 at five densities
p=1/10: R8=5797575/14301947824, B8=43558175/14301947824
p=1/4: R8=3303/3294172, B8=29567/3294172
p=1/2: R8=7/3888, B8=95/3888
p=3/4: R8=549/312500, B8=16749/312500
p=1: R8=0, B8=1/8
small-p: R8/p -> 33/8192; B8/p -> 225/8192
priority=20; elapsed_seconds=0.02773; peak_rss_bytes=15663104
```

The script also prints every cell mask, now recorded in PROOF.md, and saves
them with exact rational tail bounds in cell_audit.json. The second shape sum
uses total semiperimeter differentiation, whereas eight_corners.py uses direct
horizontal-edge weighting. The independent binomial-series calculation uses
`N8(2m)=40 binom(m+1,6)+92 binom(m,6)`. The two leading six-gap families give
the small-p coefficient separately: `18*6/(256*128)` and
`8*6/(2*256*128)`, totaling `33/8192`. The five-gap families have zero linear
coefficient. Thus the closed formula and its limiting constant agree by two
routes. Extending the unit-walk audit through perimeter 20 next, then final
proof/report audit.

## Unit-walk audit extended through perimeter twenty

Command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 eight_corners.py --stage eight --max-length 20 --output eight_data.json
```

```text
k=8: candidates=1444, valid_representations=304, skeletons=38
root_counts={'4': 0, '6': 0, '8': 0, '10': 40, '12': 372, '14': 1764,
             '16': 5936, '18': 16128, '20': 37800}
PASS independent rooted walks through length 20; nodes=1047620
priority=20; elapsed_seconds=0.64286; peak_rss_bytes=17301504
```

The four/six-corner checks also passed through twenty. Wrote PROOF.md with the
complete cell-mask table, both exhaustive enumeration rules, the rooting
argument, generating-function simplification, probability formula, small-p
constant, and rational-series tail proof. The finite classification is an
explicit reproducible exhaustive calculation, not a claimed classification
of every mirror orbit. Added a perimeter-20 cap to the walk script and an
explicit coefficient-formula comparison to the cell audit. Final runs follow.

## Final verification and result

Reran both final scripts in dependency order, using the commands above.

```text
PASS independent rooted walks through length 20; nodes=1047620
priority=20; elapsed_seconds=0.660607; peak_rss_bytes=17383424; output=eight_data.json
PASS: all 511 nonempty subsets of a 3x3 cell box; identical 38 skeletons
PASS: binomial formula agrees with every stored rooted-walk count
PASS: exact rational shape sums and binomial-series tails <1e-30 at five densities
small-p: R8/p -> 33/8192; B8/p -> 225/8192
priority=20; elapsed_seconds=0.028299; peak_rss_bytes=15171584; output=cell_audit.json
```

The geometric shape sums use four densities with q>0; the fifth density p=1
is checked separately by the absence of eight-corner all-turning polygons.
The binomial-series check includes all five. Recorded that distinction in
REPORT.md. Reviewed the rooting factor (horizontal length, no traversal factor),
coordinate compression (strictly increasing maps preserve intersections),
rank fullness (corner coordinates, not arbitrary unit boundary vertices),
cell-contact/hole exclusions, binomial shifts, tail-ratio indices, endpoint,
and small-density scale. No mathematical failure found.

Artifact inspection found that JavaScript string escaping had stripped inline
TeX delimiters and set braces and converted one rho command into a carriage
return. Restored those delimiters and braces; both documents pass a control-
character scan. A patch failed to match before this correction; it made no
changes. One formatting command had a JavaScript syntax error before running;
the corrected command completed. The numerical scripts and their data were
unaffected. This is an artifact-formatting correction, not a mathematical one.

The result strictly improves the previous restricted-family bound; it is not
a localization proof. Final artifacts: REPORT.md, PROOF.md, this LOG.md,
eight_corners.py, audit_cells.py, earlier_recheck.json, eight_data.json,
cell_audit.json. The next concrete extension is ten corners via a four-by-four
cell box.

Final read-only artifact audit: extracted the binary cell row words from
PROOF.md and compared them as a set with cell_audit.json; all 38 match exactly.
Verified the required first line of REPORT.md and inspected the repaired
inline formulas, finite-classification argument, and tail bound. All eight
result artifacts are present; their total size is under 120 KB.
