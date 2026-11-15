# T102 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 15 November 2026, 08:21 Asia/Tbilisi (04:21 UTC).

## Orientation and bounded literature check

Read the startup memory, compute governor state, and the REPORT.md, LOG.md,
PROOF.md and Python scripts in rounds 1, 3 and 4. Earlier directories are
read-only. The folder-only order precludes writes to the shared checklist,
mesh or brain; all task records are kept here. No subagents or git used.
The governor reports warn / owner_away_open, CPU saturation, about 43% free
memory. Only small, one-process standard-library calculations are planned.

Web search (within the first five minutes):

- `"2604.14122" resistance exponent`
- `"incipient infinite cluster" "spectral dimension" 2026 resistance exponent`
- `"percolation" "resistance exponent" after:2026-04-16 "spectral"`
- `"Alexander-Orbach" "two-dimensional" after:2026-04-16`

Opened https://arxiv.org/abs/2604.14122 and
https://arxiv.org/html/2604.14122v1 . The arXiv page lists only v1, 15 April
2026. Authors: Irina Đanković, Maarten Markering, Jason Miller, Yizheng Yuan.
Corollaries 1.3–1.4 still express the random-walk exponents in terms of the
unidentified resistance exponent; the Explicit lengths discussion says no
precise estimate is obtained. No later solution found in this bounded check.

## Earlier result: independent derivation

The round-4 circuit bound has the correct signs and constant. With outgoing
minus incoming divergence, the concatenated local optima have divergence
`-delta_i` at each interface. A circuit flow of divergence `delta_i` repairs
it. Every local optimum vanishes on interface edges because their endpoints
have the same wired potential. Repairs on different circuits use disjoint
edges. Hence the repaired energy is exactly `A + sum Q_C(delta)`; minimization
gives `0 <= R-A <= sum Q_C(delta)`. Orthogonality to each wired optimum gives
the lower bound even with disconnected layers.

On a cycle, conservation gives `f_j = c + H_j`; minimizing the quadratic in
`c` gives `Q = sum rho H^2 - (sum rho H)^2 / sum rho`. Independently, the
variance identity gives the pairwise-difference expression. For an antipodal
dipole on a unit cycle of length 2L, the two length-L arcs in parallel give
Q=L/2. Two such cycles and three bridges give A=3 and R=L+3, confirming
the obstruction. An independent executable rational audit will precede the
new computation.

## One extension chosen, before implementation

Implement and run the next experiment proposed by round 4: finite critical
site percolation on the triangular lattice, conditioned only on an open
origin-to-boundary connection. Select enclosing open circuits by a fixed
planar face-walk rule in two separated annuli. In each same realization,
retain every shell component and compute A, full resistance R, exact-form
circuit cost C, lengths, mismatch total variations, and cumulative-current
variances. Record absent circuits rather than silently conditioning them
away. Save configurations and ordered circuits so results can be replayed.

Why: the previous work gives a computable sufficient criterion but contains
no percolation sample. This tests its finite-scale usefulness and whether
circuit length times total variation squared is a poor proxy for the actual
repair energy. It cannot identify an asymptotic exponent or decide AO.
Circuit selection and numerical certification are part of this one
computational extension. No exponent fitting is planned.

## Independent exact audit completed

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck_previous.py`

Exit 0. Fresh rational Gauss–Jordan unit-voltage solves checked all 3,600
square-interface cases: 656 attain the bound and 240 have zero correction.
Grounded prescribed-divergence solves separately checked all 1,222 weighted
cycle demands. The five two-circuit obstruction values are R=5,6,7,11,19
at L=2,3,4,8,16, with A=3 and C=L. Counts agree with the saved round-4 data.
The earlier result holds. Output: previous_audit.json. Internal elapsed
0.8652 seconds; peak RSS 15,990,784 bytes. `nice` reported setpriority denied,
but the process verified inherited nice 20. All computations use the
single-thread environment, standard library, CPU/wall limits 120/180 seconds.

## Experiment design fixed before sampling

Use axial triangular coordinates (a,b), nearest-neighbor directions
(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1), and hexagonal radius
max(|a|,|b|,|a+b|). Sites in the closed ball B_R are independently open with
probability 1/2, with the origin fixed open. Rejection sampling accepts
exactly origin-to-radius-R connections. For each R=12,24,48 accept 40 samples,
without requiring any open circuit. The two circuit search annuli have
integer radii [R/8,R/4] (rounded down, lower endpoint at least 2) and
[R/2,5R/6]. Select the shortest enclosing simple cycle among cycles obtained
by splitting planar face walks of the induced open annulus graph; break ties
by a canonical vertex ordering. Missing circuits are recorded. Selection
uses no electrical data. Save every accepted open configuration and circuit.

Electrical computations will use sparse grounded Laplacians and conjugate
gradients. A voltage gives a resistance lower bound by Cauchy–Schwarz;
route its Kirchhoff residual on a spanning tree to obtain a feasible unit
flow and an upper bound. Both are computed on every whole graph and every
layer. Check circuit repairs by vertex conservation and compare their
energy against A+C. Check cumulative cost separately by pairwise variance.
These are finite numerical calculations, not samples from the infinite IIC.

## Sampling implementation and first run

Created sample_percolation.py, standard library only. Before sampling its
self-tests passed: all 64 first-ring masks (only the complete hexagon
surrounds the origin), full-open B_8 selects circuit lengths 12 and 24,
10 random B_3 resistances agree with independent exact rational solves,
and a signed fractional demand agrees with the exact rational circuit cost.
Layer assignment uses exact midpoint winding tests. Every physical edge is
assigned once, full adjacent-interface vertex intersections are checked,
and isolated interface vertices and other components are retained.

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B sample_percolation.py`

Started successfully. The nice warning is accompanied by a verified inherited
nice 20. CPU/wall limits are 1100/1180 seconds (both under 20 minutes).
Accepted 40 R=12 samples in 47 proposals and 40 R=24 samples in 53 proposals;
first 10 R=48 samples completed at 28.3 seconds. CSV and configuration JSONL
are flushed after each realization. Final output and separate audits follow.

## First experiment failed to obtain circuit data; revised search rule

First run exited 0 after 87.635 seconds, peak RSS 35,848,192 bytes, nice 20.
It found zero circuits in all 240 prescribed annuli across 120 accepted
configurations. Thus its A=R, C=0 observations do not test gluing. It is
not evidence for small mismatch cost. Preserve these outputs with a `thin_`
prefix. A separate BFS of CLOSED sites from the inner to outer edge of
each annulus found such a crossing in every case, agreeing with the
face-walk selector's absence of an enclosing open circuit. Diagnostic command
was a single-thread/nice Python here-document importing ball,norm,DIRS and
select_circuit, reading configurations.jsonl, and flooding the closed annulus
sites from radius low to radius high. At its snapshot it printed counts
(12,False):80, (24,False):80, (48,False):78; the final configuration had not
yet been written. The final audit will repeat this check on all records.

Before the next computation, change ONLY the circuit search to wider,
disjoint annuli [1,R/4] and [R/4+1,R-1]. Replay the SAME 120 accepted
configurations, without redrawing or rejecting any realization. This is an
exploratory design revision, disclosed here; all missing circuits still
remain in the data. The first inner circuit is no longer confined to a
fixed-ratio annulus, which limits asymptotic interpretation further.
Independent closed-crossing checks, geometric flood-fill layer checks and
electrical residual certificates will be used in the replay audit.

## Wider-annulus replay completed

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B sample_percolation.py --replay thin_configurations.jsonl`

Exit 0. Same 120 configurations and proposal counts, no extra conditioning.
Circuit counts (zero, one, two): R=12 (37,3,0); R=24 (32,8,0);
R=48 (29,11,0). Thus 22 nontrivial one-interface measurements, no sampled
two-circuit decomposition. Among configurations with a circuit, median
C/A is 0.1240063, 0.1110963, 0.1207639; maximum C/A is 0.2935476,
0.5660019, 0.6665064. These small selected subsets are descriptive only.
Outputs: configurations.jsonl, samples.csv, circuits.csv, sample_results.json.
Every full/local solve passed its energy and conservation checks; maximum
reported relative primal/dual difference 2.094e-16 and conservation error
4.441e-16. Those floating differences are at roundoff, not rigorous interval
arithmetic error bounds. Independent exact rational checks follow.
Elapsed 94.9393 seconds, peak RSS 41,222,144 bytes, nice 20, one thread.

Created audit_samples.py to reproduce all random proposals, compare every
thin and wide circuit selection with a closed-site radial crossing search,
check all sampled circuit splits by a separate triangular-face dual flood
fill, compare selection to exhaustive simple-cycle DFS on 256 tiny random
annuli, recompute all nontrivial R=12 samples using exact fractions, and
recalculate summary statistics from CSV independently of the main aggregate.

## Independent sampling audit completed

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_samples.py`

The first two attempts stopped in the independent face-dual checker: its
triangulation enumeration omitted a boundary triangle whose anchor was
outside B_R although its three vertices were inside. The missing edge was
((-12,0),(-11,-1)). Enlarged the anchor loop to B_(R+1), retaining only
triangles with all three vertices in B_R. This fixes the checker; the
sampling, circuit selection, winding-based layer partition and measurements
were unaffected. No result was changed to pass the audit.

Corrected run exited 0. Output: sample_audit.json. It reproduced all random
bits, rejected proposals and 120 accepted configurations, and verified the
thin/wide configurations coincide. Closed-site crossing diagnostics agree
in all 480 annulus checks (240 thin, 240 wide). All 22 selected circuits
passed independent face-dual vertex and edge classification. Of 256 tiny
random annuli, 10 contain an enclosing cycle; explicit simple-cycle DFS,
the selector and closed-crossing diagnostic all agree.

Exact rational unit-voltage solves independently recomputed full R, local
profiles, A and C for all three nontrivial R=12 samples: 12-004, 12-017,
12-021. Each satisfies 0<=R-A<=C exactly, and each floating R,A,C differs
from the corresponding rational number by less than 1e-9. Exact fractions
are saved in sample_audit.json. All CSV-based counts and summary extrema
and medians agree with sample_results.json via a separate aggregation.

The coarse circuit bound Nt^2/4 exceeds actual Q by factors 1.80856 to
6.86561, median 2.78776 across the 22 measured circuits. The largest layer
has 207 components, confirming that disconnected shell pieces were retained
in this experiment. Audit elapsed 7.5228 seconds, peak RSS 92,930,048 bytes,
nice 20. One process, single-thread environment, CPU/wall caps 1100/1180 s.

Wrote PROOF.md with the finite model, circuit rule, layer partition,
deterministic energy bound and variational numerical checks. It distinguishes
exact arithmetic statements from floating diagnostic bounds and explicitly
states the lack of any two-circuit percolation sample or exponent inference.

## Final arithmetic and report

A separate small single-thread/nice Python command read the CSVs and printed:

```text
12-004 R=3.24309686604 A=3.10948753655 C=0.258325793986
12-017 R=2.07159909745 A=1.85409026082 C=0.544263769093
12-021 R=2.31941838423 A=2.14459229546 C=0.265942889214
circuit length range 6 73
radius scales checked 120 samples; 22 circuits
AO threshold and dimensions: 91/96 91/32 4/3
peak RSS bytes 14204928
```

The AO values were asserted with exact fractions independently of the
cross-multiplication in PROOF.md. The report table takes values checked by
the independent CSV aggregation. Wrote REPORT.md with COMPUTED verdict,
new finite-configuration result, failed initial design, numerical and
sampling limitations, commands and a next step focused on multiple circuits.
No exponent or asymptotic bound has been obtained. All artifacts are here;
no shared records, git operations, external writes or subagents were used.
