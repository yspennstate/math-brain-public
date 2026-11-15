# T102 round 6 work log

Task: “take the NEXT checkable step on this problem, building on that work” —
15 November 2026, 10:52 Asia/Tbilisi (06:52 UTC).

## Orientation and literature check

Read the startup memory and brain index, the earlier reports, proofs, logs
and Python scripts. Earlier folders are read-only. The task-specific rule
that all writes stay here overrides shared checklist, mesh and brain writes;
none are run. No subagents or git. Compute governor reported status ok,
owner_away_open. All numerical runs use one standard-library Python process,
thread environment variables set to 1, nice >=15, CPU/wall limits below
20 minutes and an RSS check below 1 GB.

The bounded web check began at 06:52 UTC and finished by 06:56 UTC.
Queries: `"2604.14122" resistance exponent` and
`"incipient infinite cluster" "spectral dimension" 2026 resistance`.
Opened https://arxiv.org/abs/2604.14122 and
https://arxiv.org/html/2604.14122v1. The former lists only v1; Corollaries
1.3–1.4 of the latter leave beta_res unidentified, as does its Explicit
lengths discussion. Authors: Irina Đanković, Maarten Markering, Jason Miller,
Yizheng Yuan. No later solution found; the bounded search cannot prove
absence. No SOLVED_ELSEWHERE.md is warranted.

## Earlier result: independent verification planned

The deterministic bound re-derives directly: each locally wired optimum
vanishes on circuit edges. The concatenated optima have divergence
-delta on each interface. Adding disjoint circuit flows of divergence delta
therefore gives a feasible flow of energy A+C. Restricting any global unit
flow to each layer gives A<=R. Thus 0<=R-A<=C, with disconnected shell
components retained. No error found in this claim.

To check the numerical claim independently, copy the previous audit and
its dependencies/data HERE and run its exact Dirichlet and geometric audits.
Its exact rational solves are independent of the production PCG solves.
Commands and results follow below. Copies preserve previous artifacts.

## Previous computation confirmed

Command (all subsequent Python commands use the same environment):

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_samples.py > previous_samples_audit.stdout
```

Exit 0. The independent audit reproduced all 120 accepted configurations,
all rejected proposals, all 480 thin/wide annulus crossing checks, all 22
face-dual circuit splits, and 256 small brute-force cycle searches. Exact
rational recomputation agrees with R,A,C in every nontrivial R=12 sample
(12-004, 12-017, 12-021), and verifies 0<=R-A<=C exactly. The previous
result holds. Full numerical output: previous_samples_audit.stdout and
sample_audit.json. These files retain run time and RSS; nice was 20.

## One extension chosen, before implementation

Replace the two annular searches by a deterministic outward peeling rule
on all open sites of B_(R-1) except the origin. Extract enclosing simple
cycles by splitting all directed face walks, choose minimum enclosed
coordinate area (canonical lexicographic tie break), keep only vertices
strictly outside that circuit, and repeat until none remain. This gives
vertex-disjoint nested circuits and uses no electrical information. It
need not find a largest possible disjoint family. Record every selected
circuit and its radial range; keep every zero/one-circuit realization.
First replay the SAME 120 configurations. If fewer than 20 realizations
have multiple circuits, extend to a fixed 200 accepted samples per radius
using a separately disclosed seed, still with only origin-to-boundary
conditioning. The threshold governs sample size, not which realizations
are kept; these remain descriptive pilot data.

Why: the earlier report specifically lacks a multi-interface percolation
measurement. Peeling removes the arbitrary division of the disk into two
annuli, and permits later circuits to be exposed after removing an earlier
one. The finite deterministic bound remains the same. Audit geometry by
face-dual floods and audit exact electrical values on small multi-interface
samples. No exponent fitting or IIC-law inference is planned.

## Pilot completed

Created peel_circuits.py. It imports the preserved production electrical
solver and partition code, but implements its own whole-disk candidate
extraction and minimum-area peeling. Fully open disk checks at R=2,...,7
select precisely the hexagonal rings of lengths 6,12,...,6(R-1), with
coordinate doubled areas 6,24,...,6(R-1)^2.

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B peel_circuits.py --replay configurations.jsonl > pilot.stdout`

Exit 0. Outputs: pilot_configurations.jsonl, pilot_samples.csv,
pilot_circuits.csv, pilot_results.json. Elapsed 87.7337 s, peak RSS
61,947,904 bytes, verified nice 20. Numerical conservation and feasible-flow
energy checks passed in every sample. The next run follows the sample-size
rule recorded above, if the pilot has fewer than 20 multi-circuit samples.

The pilot has 2 multi-circuit realizations (one at R=24, one at R=48),
so the prespecified extension is triggered: 200 new accepted configurations
per radius R=12,24,48 with seed 202611150652. Pilot circuit counts (0,1,2)
are (34,6,0), (27,12,1), (23,16,1); total 38 circuits. Some newly exposed
interfaces have substantially larger C/A than the earlier annular samples
(maximum 20.4312), so circuit scale distribution and exact audits matter.
These are separate ensembles; no pooled inference is planned.

Before the new ensemble, run the independent pilot audit. The new exact
solver uses sparse rational Schur elimination on the prescribed-current
Laplacian, independent of both PCG and the prior dense unit-voltage solver.
It compares against dense rational solves on ten small graphs. A separate
triangular-face dual flood checks existence at EVERY peeling step, including
termination; selected circuit partitions use the previous independent dual
geometry audit. All rejected proposals are replayed in generated ensembles.

Pilot independent audit exited 0: 120 configurations checked, 158
face-dual existence/termination checks, 38 independent circuit partitions,
256 small brute-force existence comparisons, ten sparse-vs-dense exact
rational solves, and an exact multi-interface measurement at sample 24-005.
The exact R,A,C and each individual repair cost are in pilot_audit.json.
Every reported pilot quantile was recomputed from CSV independently.
Audit elapsed 6.5335 s, peak RSS 100,237,312 bytes, nice 20. No assertion
failed. Pilot geometry is now checked before the new ensemble runs.

New ensemble command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B peel_circuits.py --samples 200 --seed 202611150652 --prefix ensemble > ensemble.stdout`

Correction to the preceding audit log entry: the exact pilot sample is
24-003, as printed by the audit, not 24-005. The numerical output itself
was correct. Wrote PROOF.md with the exact peeling rule, detection and
nesting arguments, the full layer construction, the finite A+C bound and
the independent sparse rational elimination equations. It makes no claim
of a maximum circuit packing or of separated circuit scales.

## Audit design and interpretation checks

The circuit existence audit is a planar-dual connectivity test with all
remaining open edges as barriers. It checks termination as well as every
positive selection; it does not reuse the face-walk search. Each selected
polygon's vertex/edge partition is also checked with a separate dual flood.
The exact solver is checked against a dense unit-voltage solver on ten
small graphs before it is used on percolation samples. These address missed
circuits, wrong nesting, chord ownership, disconnected pieces, current
signs, and numerical errors separately.

The new measurements keep absent-circuit cases. The pilot already shows
that circuit-only repair can have C/A>20, while the actual correction is
smaller. The rule selects irregular cycles and does not separate annular
scales; counting interfaces alone cannot justify an asymptotic statement.
PROOF.md records these limitations before a final numerical summary.

## Conditional extension for rare multiple circuits, fixed before its run

The 600-sample ensemble is still running; its first 490 accepted samples
contain only three multi-interface cases. To obtain a useful number of
such measurements without solving thousands of zero-interface networks,
add one separate geometry census: exactly 2,000 accepted configurations
at R=48, seed 202611150700. Keep EVERY configuration and its peeling trace
in survey_configurations.jsonl.gz, and every zero/one/multiple count in
survey_census.csv. Electrically measure EVERY case with at least two
selected circuits, and no zero/one cases in this separate census. Do not
stop after a target number of multiple circuits and do not discard any
accepted configuration. The fixed census size is chosen now, before any
of its random bits or electrical values are generated.

This is a disclosed change in allocation of electrical work, not a change
of percolation conditioning. The electrical subset has the explicit extra
condition k>=2. It cannot estimate unconditional electrical moments. The
600-sample ensemble measures all outcomes and remains separate. The survey
only extends the same multiple-interface experiment, not an exponent fit.
New scripts survey_multiple.py and audit_survey.py stream compressed
configurations so their memory does not scale with 2,000 stored graphs.
No survey run has started yet; numerical processes remain sequential.

Saved an interim REPORT.md so a sudden stop preserves the completed pilot
result. The 600-sample run continues. Strengthened audit_peeling.py to
check each circuit CSV row against its saved ordered cycle: length,
minimum/maximum radius, fan-triangle area independent of shoelace area,
Q=N*variance, coarse=N*TV^2/4, and C=sum Q. Exact sample selection now
also includes the largest C/A multi-interface case at any radius. The
survey audit uses the same independent data consistency checks.

PROOF.md now specifies the separate fixed-size geometry census and the
explicit k>=2 electrical subset. Its all-case census and the 600-sample
all-case electrical ensemble have different purposes and are not pooled.
The independent survey audit streams all 2,000 graphs, reproduces rejected
proposals, checks every selection and termination by the triangular-face
dual, and selects exact electrical audits by the first two measured ids,
the maximum C/A and the maximum number of interfaces. This includes an
outlier rather than checking only numerically easy cases.

## All-case ensemble completed; independent audits and census start

The 600-sample production run exited 0. It contains six multi-circuit
realizations. Elapsed 412.3523 s, peak RSS 42,991,616 bytes, nice 20. All
local/full solves and explicit repaired-flow checks passed. Full results
are ensemble_results.json; configurations and CSVs are flushed separately.

Sequential commands (set -e stops the sequence at any failure):

```sh
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 python3 -B audit_peeling.py pilot > pilot_audit.stdout
nice -n 15 python3 -B audit_peeling.py ensemble > ensemble_audit.stdout
nice -n 15 python3 -B survey_multiple.py > survey.stdout
nice -n 15 python3 -B audit_survey.py > survey_audit.stdout
```

The pilot rerun is justified by stronger CSV checks and inclusion of its
largest multi-interface C/A case (at R=48). No numerical processes overlap.
Each individual program has CPU/wall caps of 1100/1180 seconds and checks
its own peak RSS below 1 GB. The census size and seed were recorded above
before this sequence started.

The 600-sample table, before independent audit confirmation:
R=12 counts (0,1,2)=(175,25,0), R=24=(151,47,2),
R=48=(130,66,4). Total 150 circuits. Among circuit-containing samples,
median C/A is 0.718345, 0.696664, 0.812371; maximum C/A is 5.51610,
38.5590, 34.5657. Among the two/four multi-interface samples at R=24/48,
median C/A is 3.66845/1.29369. These numbers are descriptive; some of the
largest costs occur in single-interface samples. Circuit minima are <=2
for 140 of 150 selected circuits. Maximum layer component count is 279.
The all-case ensemble alone still does not supply many multi-interface
realizations, which is why the separate fixed geometry census was specified.

## Strengthened pilot and all-case audits passed

The updated pilot audit exited 0 in 10.6599 s, peak RSS 111,722,496 bytes.
It now includes an exact rational R=48 multi-interface outlier as well as
the R=24 case. The 600-sample ensemble audit exited 0 in 31.9878 s, peak
RSS 199,770,112 bytes. All saved sampling bits/rejections, every circuit
selection/termination, all circuit CSV geometry/energy consistency checks,
all summary quantiles, 256 small brute-force searches, ten sparse-vs-dense
rational solver comparisons and selected exact multi-interface network
calculations passed. Detailed exact fractions are in pilot_audit.json and
ensemble_audit.json. Both verified nice 20. The sequential shell has
advanced to survey_multiple.py; no earlier file was mutated.

## Additional numerical risk identified before final reporting

The all-case table's largest C/A at R=24 is a SINGLE-interface sample,
so the selected multi-interface exact checks do not verify that maximum.
Add audit_outliers.py, which recomputes the largest C/A at each radius in
both pilot and all-case ensembles by exact sparse rational arithmetic.
This checks the reported extrema rather than assuming the largest
multi-interface case is also the largest overall. It streams configurations
and will run after the current sequential census/audit sequence. This
additional check addresses a specific gap; no production rerun is needed.

## Census progress and remaining audit work

At 1,200/2,000 accepted radius-48 configurations the census has 26
multi-interface measurements; all are two-circuit cases so far. Every
zero/one realization remains in the compressed configuration stream and
census CSV. At 1,158 the observed C/A exceeds 39; the survey's exact
outlier rule will include the final maximum. These are provisional values
until the independent streaming audit finishes. The compute governor still
reports ok / owner_away_open, and only one numerical process is running.

A boundary-case review found that D/C is undefined when C=0. The production
summarizer already records None and omits it from D/C quantiles. Before the
survey audit starts, updated its independent aggregation and the final
summary script to follow that definition rather than attempting float('')
on an empty CSV field. This does not alter any measurements or selection.
The exact circuit bound allows C=0, and zero/one outcomes remain retained.

## Fixed census completed

survey_multiple.py exited 0 in 206.2685 s, peak RSS 41,861,120 bytes,
verified nice 20. The fixed 2,000 accepted configurations and all census
rows are saved; no stopping criterion based on circuits was used. The
streaming independent audit has started and has already checked its first
200 configurations. Final counts and extrema are in survey_results.json;
these will be reported only after the replay, geometry and exact outlier
audits finish.

A proof review added the maximum-principle argument for nonnegative local
boundary profiles and TV<=1, and a full derivation of the recorded coarse
bound Q<=N*TV^2/4. This completes the justification of all circuit CSV
quantities, beyond the central A+C bound. No production values changed.

## What did not work, and what this result cannot do

A fully measured 200-per-radius ensemble supplied only six two-interface
realizations; it was too small for the intended multi-interface comparison.
The separate fixed-size geometry census supplied 41 while retaining all
zero/one configurations and making its electrical conditioning explicit.
There are no three-interface realizations in either completed production
ensemble. Thus these data do not test accumulation over a growing number
of interfaces. Peeling guarantees nesting, not annular scale separation or
maximum cardinality. The many circuits with minimum radius 1 or 2 are a
geometric limitation, not evidence about a dyadic IIC decomposition.

No mathematical assertion or executed numerical audit has failed so far.
The earlier low C/A values did not persist uniformly under a different
geometric circuit rule. The full resistor network is unchanged in the
pilot; its selected interfaces and the resulting A and C change. Neither
small nor large finite ratios identify an exponent. The missing estimates
remain an IIC-law bound on C/A and an identified exponent for A.

## Census independent audit passed

The sequential run exited 0. audit_survey.py reproduced all 2,000 accepted
configurations and all 2,643 proposals, checked 2,618 dual selection and
termination states, independently classified every selected circuit,
verified every measured circuit CSV against its ordered polygon, and
recomputed the conditional quantiles. Its exact rational checks include
48-0016, 48-0212 and the maximum-C/A case 48-1290. All pass 0<=R-A<=C
exactly and agree with stored floating R,A,C within 1e-9. Exact fractions
and scale distributions are in survey_audit.json.

Audit elapsed 215.0361 s, peak RSS 55,377,920 bytes, nice 20. Final census
counts (0,1,2)=(1423,536,41), no k>=3. The measured two-interface subset
has C/A range 0.0939863–48.5840, median 2.4148732; R/A median 1.9532239,
maximum 8.9984561; D/C median 0.3089880. All other accepted graphs remain
saved in the compressed census. These conditional data are not pooled
with the separately sampled 600-case all-outcome ensemble.

Final targeted numerical audit and independent report-table command:

```sh
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 python3 -B audit_outliers.py > outlier_audit.stdout
nice -n 15 python3 -B summarize_results.py > summary.stdout
```

## Final exact extrema audit and independent numerical summary

The final sequential commands exited 0. All six per-radius maxima in
pilot/ensemble passed exact sparse rational recomputation, including the
previously unaudited single-interface maxima. outlier_audit.json contains
the fractions. Runtime 7.6940 s, peak RSS 33,931,264 bytes, nice 20.
The summary script independently read CSVs and exact audit fractions;
its complete concise output follows.

```text
pilot samples 120 circuits 38
R 12 counts [34, 6] C/A active median/max 0.609546167700838 5.698603899827415 multi 0 multi median/max None None
R 24 counts [27, 12, 1] C/A active median/max 0.1605630339742448 14.238151493528623 multi 1 multi median/max 14.238151493528623 14.238151493528623
R 48 counts [23, 16, 1] C/A active median/max 0.1701704974625943 20.431165148360748 multi 1 multi median/max 20.431165148360748 20.431165148360748
length range 6 267
min radius <=2 35 / 38 max radius median 5.5
exact 24-003 interfaces 2 R,A,C 3.410430867932591 0.8920951774859155 12.70178628374152 C/A 14.238151493585512 D/C 0.19826626225558397
exact 48-009 interfaces 2 R,A,C 8.038972557337988 1.5585979143078061 31.843971387200863 C/A 20.431165148416863 D/C 0.20350397141842858
resources production 87.73368050000863 61947904 audit 10.659937791991979 111722496
ensemble samples 600 circuits 150
R 12 counts [175, 25] C/A active median/max 0.71834489672232 5.516095196260768 multi 0 multi median/max None None
R 24 counts [151, 47, 2] C/A active median/max 0.6966642218606741 38.558997571922475 multi 2 multi median/max 3.668450722668585 6.631456677223542
R 48 counts [130, 66, 4] C/A active median/max 0.8123712337989992 34.56568395697579 multi 4 multi median/max 1.293694005996644 34.56568395697579
length range 6 374
min radius <=2 140 / 150 max radius median 8.0
exact 24-052 interfaces 2 R,A,C 7.660651372535192 1.9176793601240951 12.717007597473891 C/A 6.631456677226249 D/C 0.4515977495800098
exact 24-085 interfaces 2 R,A,C 3.6347402138009435 2.676667444825546 1.888241044927443 C/A 0.7054447681118304 D/C 0.5073890177046819
exact 48-129 interfaces 2 R,A,C 7.58086548552916 1.0055147594909062 34.75630539063876 C/A 34.565683956977345 D/C 0.1891843984029803
resources production 412.3522994170198 42991616 audit 31.987756374990568 199770112
survey samples 2000 proposals 2643 counts {'0': 1423, '1': 536, '2': 41}
C_over_A 0.09398628643162749 2.4148732344491792 48.583995561095584
R_over_A 1.041864964183494 1.9532238921659195 8.99845614769922
D_over_C 0.11290893032891758 0.30898801180310875 0.5299924231952856
measured circuits 82 length range 6 399
all minradius<=2 542 / 618 minradius range 1 14 maxradius median 12.0 maxradius range 1 47
multiple minradius<=2 62 / 82 minradius range 1 13 maxradius median 12.0 maxradius range 1 47
survey exact 48-0016 interfaces 2 R,A,C 7.462350156258512 2.4036386787612374 22.946352163890268 C/A 9.546506455669169 D/C 0.22045819925390847
survey exact 48-0212 interfaces 2 R,A,C 9.263354865873318 2.509874375331394 26.296015807153065 C/A 10.477024693190488 D/C 0.2568252369510987
survey exact 48-1290 interfaces 2 R,A,C 7.776048338691812 1.047214793178047 50.877878863605915 C/A 48.583995561410745 D/C 0.13225460054167174
resources survey 206.26847766700666 41861120 audit 215.03610612498596 55377920
AO check 91/96 91/32 4/3
```

## Completion

REPORT.md now records the completed 49 two-interface measurements across
three separately described datasets (2 pilot, 6 all-case, 41 census), the
conditional allocation, exact checks, failed initial sample-size choice,
resource use and the remaining IIC estimates. PROOF.md gives the rule,
its detection/nesting justification, full layer construction, every energy
bound used, exact sparse elimination and the limits of interpretation.
No exponent or new bound on beta_res is claimed. All work stayed here;
no subagents, git, posts, external writes or shared-store mutations occurred.
