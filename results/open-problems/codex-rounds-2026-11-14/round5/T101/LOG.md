# T101 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received approximately 08:18 Asia/Tbilisi, 15 November 2026.

## 08:18–08:22 — orientation and bounded literature check

Read the three prior REPORT.md files, their PROOF.md, LOG.md, and Python
scripts. Earlier folders are read-only. Read startup memory/index and compute
state: warn, owner_away_open, CPU saturated. Every calculation will use one
thread, nice >=15, small memory, and bounded CPU/wall time. No subagents, git,
background jobs, or external writes. The specific folder-only order overrides
the general shared brain, checklist, and mesh registration orders, since those
commands mutate other folders. Durable results remain here for the coordinator.

Web search queries: `"Lorentz mirror" "2026" conjecture` and
`"Lorentz mirror model" closed orbits proof`. Opened papers:

- Martin P. W. Zerner, *Infinite light rays and infinite clusters with
  infinitely many pivots*, arXiv:2610.12460,
  https://arxiv.org/abs/2610.12460 and https://arxiv.org/html/2610.12460v1.
  Introduction explicitly leaves the square-lattice problem conjectural.
- Gady Kozma and Vladas Sidoravicius, *Lower bound for the escape probability
  in the Lorentz Mirror Model on the lattice*, arXiv:1311.7437,
  https://arxiv.org/abs/1311.7437. Abstract gives 1/(2n+1).
- Jian Gu and Qin Hao, *Boundary transmission and excursion geometry in the
  Lorentz mirror model: a numerical study*, arXiv:2609.14949,
  https://arxiv.org/abs/2609.14949. Abstract leaves infinite-plane localization
  unresolved.
- Kieran Ryan, *The spin-1/2 Heisenberg XXZ chain and the Lorentz mirror model
  with loop weight 2*, arXiv:2608.21306,
  https://arxiv.org/abs/2608.21306. Results concern a different loop weight.
- Raphael Lefevere and Hal Tasaki, *Hierarchical Lorentz Mirror Model: Normal
  Transport and a Universal $2/3$ Mean--Variance Law*, arXiv:2602.07988,
  https://arxiv.org/abs/2602.07988. Results concern a hierarchical model.

Search ended within five minutes; no solution found. This was not an
exhaustive review.

## Next calculation

First independently regenerate ten-corner rank polygons by unit-vertex
self-avoidance from cyclic coordinate words, recompute all strip weights,
and compare the exact gap sums and reduced rational function to round 4.
If this passes, choose ONE extension: the exact twelve-corner vertex-simple
contribution, including arbitrary positive coordinate gaps. At twelve corners
strip half-crossing weights can reach 3, so the new algebra must retain
1-r^3. Use an independent cell-row enumeration to check individual boundaries,
and rooted unit walks to check small perimeter coefficients.

## Independent ten-corner recheck passed

Command: `nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 twelve.py --stage recheck`.
The new implementation tests disjoint half-open sets of unit boundary
vertices, without the earlier cell-interior method or segment-intersection
routine. All 72,900 cyclic coordinate pairs give 5,280 representations and
528 individual boundaries, each identical to round 4, with identical strip
weights. Independently recomputed gap algebra gives F denominator powers
(8,2,0) for (1-r),(1+r),(1+r+r^2), and numerator
r^6(16+112r+220r^2+176r^3+48r^4), as reported.
All rooted counts through perimeter 60, four exact rational probabilities,
and coefficient 143/65536 agree. At p=1/2 the ten-corner probability is
33971/39366000. No discrepancy found: the earlier result holds.
Saved ten_recheck.json. Elapsed 0.0983 s, peak RSS 20,512,768 bytes,
priority 20. The nice warning is macOS rejecting a relative priority change
from inherited nice 20; the script verifies actual nice >=15.

## Choice confirmed before extension

Proceed with exactly the twelve-corner extension described above. Six
horizontal and vertical sides imply at most six coordinate ranks per axis,
so the finite classification and arbitrary-gap summation remain exhaustive.
Use precomputed half-open vertex bitsets for early rejection of intersections;
this avoids blindly scaling the earlier Python cell-subset loop.

## Twelve-corner primary calculation

Command: `nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 twelve.py --stage twelve`.
Output: cyclic surjective word counts on 2,3,4,5,6 ranks are
2,60,480,1080,720; 5,484,964 coordinate pairs; 118,812 valid
representations; 9,901 polygons. Saved every boundary and strip list in
twelve_data.json. All coordinate gaps remain arbitrary positive integers.

The provisional reduced series is
F12=r^6 A(r)/[(1-r)^10(1+r)^4], with
A=(1,36,454,1964,4246,5068,3378,1196,165).
Although some shapes have weight-3 strips, the factor 1+r+r^2 cancels
in the full sum. This cancellation needs independent verification.
The rooted numerator r^6 has coefficients
(6,258,3856,20652,56968,91044,87928,51020,16242,2186),
denominator (1-r)^11(1+r)^5.
At p=1/2 the provisional extra probability is 25440181/56687040000;
the small-p coefficient is 20635/16777216.
Rooted twelve-corner counts at perimeters 12,14,16,18,20,22 are
6,294,5560,51012,304800,1368620.
Elapsed 4.788 s, peak RSS 31,129,600 bytes, actual nice 20.

Important endpoint check: the leading r^6 term means all-turning simple
twelve-step loops exist. Unlike six/eight/ten corners, this family contributes
at p=1. Independently audit this rather than extrapolating the old endpoint.

Next: enumerate cell rows using only local four-cell vertex patterns to prune
diagonal contacts, excess corners, and missing coordinate levels. Check the
remaining boundary for a single cycle, then compare every polygon and strip
weight. This is a different finite construction from cyclic corner words.

## Independent cell, walk, probability, and endpoint audits passed

Command: `nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit_twelve.py`.
The cell-row search visited 129,988 row prefixes, retained 18,525 local
12-corner candidates, and rejected 8,624 disconnected boundaries (including
holes). The remaining 9,901 individual boundaries and both oriented strip
lists agree exactly with the coordinate-word calculation. The row search
prunes only necessary conditions, so it covers the entire five-by-five box
without iterating all 33,554,431 nonempty masks.

Independent rooted unit walks through perimeter 20 visit 3,532,630 nodes
and agree for 4,6,8,10,12 corners at every even perimeter. An independent
signed-binomial convolution agrees with positive gap coefficients through
perimeter 80. Exact total-semiperimeter gap sums agree with the closed
formula at p=1/10,1/4,1/2,3/4. Perimeter partial sums through m=500 agree
at those four densities and p=1 within rigorous exact rational tail bounds
less than 10^-30. Saved twelve_audit.json.

Outputs:
  p=1/10: R12=1372889288868240880383825/11586504797790469247350435328,
          B12=39142335750478941952260625/11586504797790469247350435328
  p=1/4: R12=135696646764249/494331685750000000,
         B12=4824770995100249/494331685750000000
  p=1/2: R12=25440181/56687040000, B12=1459458421/56687040000
  p=3/4: R12=890419205811/1774821250000000,
         B12=97484031148851/1774821250000000
  p=1: R12=3/2048, B12=259/2048.

The maximal ten-gap terms separately give F's leading coefficient 4127/4
at r=1; hence R12/p -> 20635/16777216 and B12/p -> 518043/16777216.
Substitution in the closed numerator independently agrees. The p=1 result
is independently the six all-turning rooted length-12 polygons, each with
probability 2^-12. Elapsed 3.3392 s, peak RSS 92,323,840 bytes, nice 20.
No discrepancy found. Next write out the exact polynomial cancellation and
the full proof, including the cell-row completeness and p=1 exception.

## Exact symbolic cancellation and proof written

Extended audit_twelve.py with an independent expansion of every table row
over denominator (1-r)^10(1+r)^5(1+r+r^2), and an independent expansion
of the differentiated numerator. Reran the audit command above: both exact
identities passed, as did all earlier checks. The common numerator is r^6
times (1,38,528,2945,9118,17942,23970,22334,14381,6100,1526,165),
which equals r^6(1+r)(1+r+r^2)A(r). The rerun used 3.2158 s and
93,192,192 bytes peak RSS, nice 20.

A small read-only Python heredoc under the same nice/env prefix inspected
the common numerator and every minimum-perimeter shape. Exactly one
translation class has perimeter 12: the five-cell cross, with strip weights
(1,1,1) on both axes. It independently supplies six rooted boundaries.
The rank-box dimension counts are (2,5):12, (3,3):7, (3,4):126,
(3,5):420, (4,3):126, (4,4):1268, (4,5):2296, (5,2):12,
(5,3):420, (5,4):2296, (5,5):2918. A(-1)=-20, so the -1 pole survives.

Wrote PROOF.md with the full 34-row classification, both exhaustive rules,
the rooting and gap bijections, explicit common numerator and cancellation,
derivative, probability, coefficient formula, tail majorant, two small-p
derivations, half-density value, and endpoint. Wrote REPORT.md with the
required PARTIAL verdict, precise scope, commands, limitations and next step.
Added a separate inclusion-exclusion check of cyclic word counts to the
primary script. The recheck command passed again with this check included:
528 polygons, 0.1011 s, 20,119,552 bytes, nice 20.

Adversarial review: corner coordinate levels, rather than arbitrary boundary
vertices, define ranks; all nonadjacent contacts are excluded; the cell
cycle test removes holes and separate components; rotations remain distinct;
there is no extra root orientation factor. The cell-prefix cutoff of ten
corners is safe because its future top boundary adds at least two corners.
Weight-three terms were included before cancellation. The tail ratio uses
m-9, not the earlier m-7. The p=1 endpoint must include the cross family.
No discrepancy found. Final checks follow after the word-count assertion.

## Final runs and artifact audit

Reran `python3 twelve.py --stage twelve` under the full nice/env prefix:
all results unchanged, 4.2921 s, 30,588,928 bytes before serialization,
nice 20. Reran the full independent audit under the same prefix with
`/usr/bin/time -l python3 audit_twelve.py`. The Python calculation passed
every check again (3.2044 s, 90,750,976 bytes before serialization), but
the time utility then exited 1 because sandboxing denies its
`sysctl kern.clockrate` query. Its resource instrumentation failed; the
mathematical script completed successfully and saved all results.

To measure the full memory peak including JSON serialization without that
unavailable system query, added measure_resources.py, a small standard-library
runpy wrapper. Its child calculation is executed in the same single Python
process, at the same nice level and with CPU/wall guards; final ru_maxrss is
read after the calculation returns. No background processes are launched.

A bounded read-only Python heredoc under the full nice/env prefix checked
Python syntax, all 34 rows of the proof table against twelve_data.json,
both lists' 9,901 entries, the report verdict, exact constants, every tail
bound, preserved TeX delimiters, and document control characters. Output:
`PASS Python syntax, all 34 proof-table rows, full data counts, verdict, constants, tails, TeX and control characters`.
The eight main result artifacts totaled 25,729,262 bytes at this point.

## Full-run resource checks completed; final result

Commands:

    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 measure_resources.py twelve.py --stage twelve
    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 measure_resources.py audit_twelve.py

Both computations passed again with unchanged mathematical output.
The full primary run, including serialization, took 4.3437 s with peak RSS
54,460,416 bytes; the full independent audit took 3.2957 s with peak RSS
137,625,600 bytes. Both priorities were 20. Saved twelve_resources.json
and audit_twelve_resources.json. These measurements include the JSON export
allocation omitted from the scripts' earlier pre-export snapshots; REPORT.md
now states the full-run peak rather than the smaller snapshot.

Finished with a PARTIAL result: exact twelve-mirror vertex-simple probability
and the resulting strict improvement of the explicit periodicity bound.
All 9,901 rank polygons were independently checked. The full conjecture is
unresolved. No prior folder was edited, no git or subagents were used, and
all new artifacts remain in this folder.

Final bounded read-only check, using the same nice/env Python prefix, parsed
all three scripts, checked document control characters and the exact verdict,
and checked both complete-run resource JSON files against nice >=15 and
RSS <1 GB. Output:
`PASS final documents, scripts, verdict, and full-run resource limits`.

Task: “take the NEXT checkable step on this problem, building on that work” —
received approximately 08:18 Asia/Tbilisi, 15 November 2026.
