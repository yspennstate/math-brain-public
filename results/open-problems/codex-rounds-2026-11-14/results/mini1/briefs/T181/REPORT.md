VERDICT: COMPUTED exact Favard lengths for generations 0 through 5

With Fav(E)=(1/pi) integral_0^pi |proj_theta E| dtheta, the certified bounds are:

| n | Strict lower bound | Strict upper bound |
|---:|---:|---:|
| 0 | 1.27323954473516 | 1.27323954473517 |
| 1 | 1.04990339003727 | 1.04990339003728 |
| 2 | 0.92793731495768 | 0.92793731495769 |
| 3 | 0.84365831229531 | 0.84365831229532 |
| 4 | 0.77883017302463 | 0.77883017302464 |
| 5 | 0.72637720829722 | 0.72637720829723 |

`PROOF.md` proves a finite reduction valid for every generation: enumerate
all rational crossings of square projection endpoints, compute the union
length as an integer affine function of slope between crossings, and integrate
exactly. In particular, pi*Fav(K_n) is algebraic for every finite n.

The completed computation saves the entire piecewise affine function and an
exact radical expression at each generation. It includes a hand derivation of
Fav(K_1)=(8+3*sqrt(2)-4*sqrt(5))/pi and an explicit 11-term expression
for 4*pi*Fav(K_2). No claim is made that these small cases or the arrangement
method are new to the literature.

Run from this folder, using Python 3 and its standard library:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 exact_favard.py --max-n 5 > run_output.txt 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_favard.py > audit_output.txt 2>&1
```

The generator finished in 23.504 seconds, with peak RSS 27,852,800 bytes.
The independent audit takes about one second and approximately 22 MB. Both
programs check actual nice >= 15 and OMP_NUM_THREADS=1. The generator reports
actual nice 20. macOS emits a warning when the launcher tries to add another
15 to the inherited low priority; the programs still run at nice 20.

Files:

- `PROOF.md`: complete reduction, integration, certification and small cases.
- `exact_favard.py`: generator and exact arrangement checks.
- `audit_favard.py`: separate interval-merging and integration audit.
- `data/summary.csv`: decimal enclosures and arrangement sizes.
- `data/cells_n0.csv` through `data/cells_n5.csv`: exact slope pieces.
- `data/certificate_n0.json` through `data/certificate_n5.json`: radical
  expressions, rational bounds, cross-checks and resource measurements.
- `run_output.txt`, `audit_output.txt`: successful run outputs.
- `LOG.md`: decisions, commands, failures and verification record.
- `LITERATURE.md`: opened sources and a separately qualified unverified lead.

Every candidate slope cell was tested at two rational samples against an
endpoint-occupancy sweep. Every event slope was checked, including ties.
Endpoint-pair enumeration independently reproduced all events for n<=4.
All generations passed independently generated coordinate sets and exact
horizontal, diagonal and slope-1/2 controls. Direct angular midpoint
quadrature agreed, with maximum observed error 8.39e-7 at n=5; this numerical
quadrature is only a cross-check.

The separate auditor integrates by parts using slope jumps, bounds direct
square roots instead of reciprocals, and bounds pi using a different
arctangent identity. It independently certifies all printed decimal intervals,
with internal enclosure widths below 1e-50. Its printed n=2 closed-form
check also passes.

Two failures were found and fixed. The initial certificate writer exceeded
Python's integer-to-string digit limit because rational denominators grew
unnecessarily; outward rounding onto a common rational grid fixed it. The
first independent integration audit omitted a terminal derivative term;
the n=0 control caught it immediately. Its corrected formula is derived in
PROOF.md. Failed outputs are preserved in `first_run_output.txt` and
`audit_first_run_output.txt`.

The exact asymptotic rate remains unresolved by this work. The literature
search found no complete solution: Dąbrowski's October 2026 survey still
states the problem as open. A repository claims an exponent above 1/4;
its proof and kernel checks were not audited here. These claims do not enter
the computation. Small n cannot distinguish competing asymptotic rates,
and no exponent has been fitted. The certificates rely on the supplied
finite enumeration and Python's exact integer arithmetic, not a formal proof
assistant.

Next worker: use the saved slope arrangements to seek a recursion or an
inequality controlling their integrated contribution across generations.
An extension to n=6 should use a sweep that updates endpoint order across
crossings, rather than repeatedly sorting from scratch. Independently audit
the reported greater-than-1/4 repository bound before treating it as a
literature advance.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 21:19 Asia/Tbilisi.
