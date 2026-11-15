# T080 working log

Task: “take the NEXT checkable step on this problem, building on that work”.
First retained clock: 2026-11-15 10:36:07 Asia/Tbilisi (06:36:07 UTC); exact receipt time unavailable.

## 1. Scope and orientation

Read the startup memory and compute state. State was `ok`, mode `owner_away_open`; this task will nevertheless use only short, single-threaded standard-library calculations at nice >= 15. The current instruction to write only inside this folder overrides the older global instructions to update the external brain, checklist, and mesh. No external state will be changed, no git used, and no subagents started. Earlier folders are read-only inputs.

Listed the four predecessor folders and started reading their reports, logs, proofs, and scripts. The latest claim is a universal lower occupation bound for jittered triangular half-plane packings separated by an empty strip. Its proof uses Voronoi-cell erosion.

## 2. Bounded literature check (started 10:36)

Web queries: `hard sphere continuum crystallization phase transition proof 2026 Euclidean`; `hard disk orientational order rigorous phase transition 2026 proof`; `"hard sphere" "phase transition" "2026" rigorous Euclidean proof`; `"hard disks" crystallization theorem 2026 orientational`.
Opened arXiv:2607.23873 and arXiv:2606.28009. The former still describes Euclidean freezing as open and proves a hyperbolic result. A recent hard-disk free-volume paper also appeared in search; its PubMed page did not return substantive content, so it is not evidence used here. Search ended within five minutes. Nothing found changes the problem statement; this is a bounded search, not an exhaustive claim.

Opened primary references:

* Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, https://arxiv.org/abs/2607.23873 . Hyperbolic transition; Euclidean problem explicitly left open.
* Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, https://arxiv.org/abs/2606.28009 . Improved uniqueness and mixing bounds; no hard-sphere freezing theorem.

## 3. Independent re-check of round 5

The main claim holds on analytic re-derivation. A triangular fundamental cell has area sqrt(3)s^2/2 and covering radius R=s/sqrt(3). Every point of an R-eroded rectangle belongs to a nearest-site cell whose site is in that rectangle; hence its lattice count is at least rho_s(w-2R)_+(h-2R)_+. First erode a square by delta to retain centers after jitter, then split it at the strip. The two widths have sum at least ell-2delta-g. The sum of their positive-part erosions is at least (ell-2delta-g-4R)_+. This recovers the stated universal count without sampled phases. Same-side and cross-side separations both exceed 201/200.

The independent scalar calculation will use a rational interval for sqrt(3) with denominator 10^12, rather than the earlier script's field arithmetic or its coarse factor bounds, and independently clear denominators in the expanded expression. The old script will also be copied here and run unchanged, so its output files cannot touch its source folder.

## 4. Choice of one extension, before proof

Prove a local, fixed-orientation defect separator for an arbitrarily filled bounded strip joining jittered triangular lattices of orientations 0 and pi/6. Define good observation windows by (i) a particle within distance one of the anchor, (ii) at least one short bond from every center within distance two, and (iii) all such bonds lying in narrow cones about one of the two six-direction families. Use cutoff 11/10, cone half-angle arcsin(1/100), and observation radius 31/10. Neighboring unit-grid windows cannot carry opposite good labels because they share a particle and one of its bonds. A planar interface-edge parity argument should then force an eight-neighbor defect crossing of every finite-height rectangle, hence an infinite connected defect component in the bounded strip.

Why this piece: it is exactly the fixed-angle geometric test requested in round 5 and permits any admissible filling, with no vacant-seam assumption. The detector will be intrinsic to the observed centers, with dilation, jitter, and observation radius explicit. It intentionally tests two prescribed orientation families: an intermediate rotated crystal can be defective for this detector even if locally perfect. No count deficit, Gibbs probability bound, surface tension, or freezing conclusion is inferred.

## 5. Copied round-5 audit

Commands:

```sh
mkdir -p prior_recheck
cp ~/codex_op_1114r5/briefs/T080/verify.py prior_recheck/verify.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 prior_recheck/verify.py > prior_recheck/VERIFY_OUTPUT.txt 2>&1
```

Exit code 0. Complete output:

```text
nice: setpriority: Operation not permitted
nice_priority=20; thread_environment=1; CPU_limit_seconds=60
exact_rational_count_floor=3317635/1591356=2+134923/1591356; required_count>=3
independent_Qsqrt3_bound=['-4390/303', '1757441/183618']; decimal_for_orientation=2.08932187097; exact_comparison_to_2=PASS
cell_vertices=6; exact_shoelace_area=sqrt(3)*s^2/2; vector_checks=720; PASS
exact_phase_and_square_cases=560; minimum_certified_safe_sites_in_sample=8; witness=[0, 1, '-2', '-7/4']
exact_split_width_cases=35; wide_strip_and_missing_erosion_negative_controls=PASS
conservative_large_box_examples=[{'threshold': '1/8', 'sufficient_integer_side': 6}, {'threshold': '1/2', 'sufficient_integer_side': 9}, {'threshold': '1', 'sufficient_integer_side': 39}, {'threshold': '11/10', 'sufficient_integer_side': 165}]
jitter_trials=3; seed=5080; smallest_sampled_separation=1.00577809998; floating_point_support_only
PASS; elapsed_seconds=1.132; peak_rss_mib=15.359
```

The earlier result holds. The copy is unchanged and all its output is confined to prior_recheck/. Its sampled minimum of eight is not substituted for the analytic universal count of three.

## 6. Proof and new audit

Wrote PROOF.md. Good windows require an occupied central unit ball, a nonempty short-bond neighborhood at every center in the radius-two ball, and all those bonds in one fixed six-cone family. Neighboring good anchors share a particle and a bond, excluding opposite labels. Full jittered crystals pass uniformly: covering distance is below 1217/2000, nearest bond lengths are below 203/200, every other bond exceeds the cutoff by a squared rational comparison, and angular distortion is at most arcsin(1/202), below arcsin(1/100).

The finite separator proof draws edges between A and non-A squares. Interior degrees are even, side endpoints absent, and the number of endpoints on each horizontal boundary is odd. A component with odd top endpoint count must also have odd bottom endpoint count. Its non-A edge neighbors are defective, and successive such cells are eight-neighbors. This gives a crossing with at least one defective anchor per row. For an infinite strip, a row-zero pigeonhole argument produces one defective component unbounded both upwards and downwards.

For the previous example, W=203/400 and observation radius 31/10 give W+R_o=1443/400, so M=4 and all defects lie among columns -3 through 3. Arbitrary admissible additions inside that strip preserve both the forced separator and the earlier occupation lower bound.

Created verify.py. Its first mathematical run passed: independent radical interval and denominator-clearing checks of round 5; exact new constants; all 26,487 assignments on three small rectangles, of which 482 satisfy the hypotheses; independent transfer counts; a separate implementation of the interface graph; and three supporting floating-point jittered interfaces with greedy strip fillings. There were no mathematical failures. This first run took 0.423 seconds and peaked at 15.875 MiB. Before the final run, added an independent cross-product angle inequality and an exact lattice-index cutoff check; neither changes the result.

## 7. Final mathematical audit

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
```

Exit code 0. Complete output:

```text
nice: setpriority: Operation not permitted
nice_priority=20; thread_environment=1; CPU_limit_seconds=90
prior_independent_radical_interval_lower=2.08932187097>2; cleared_integer_comparison=PASS
exact_detector_constants=PASS; cutoff=11/10; angular_sine=1/100; observation_radius=31/10; M=4; band_columns=7
exhaustive_grid=1x5; assignments=243; legal=1; eight_neighbor_crossings=ALL; four_neighbor_failures=0; independent_transfer_count=PASS
exhaustive_grid=2x4; assignments=6561; legal=81; eight_neighbor_crossings=ALL; four_neighbor_failures=40; independent_transfer_count=PASS
exhaustive_grid=3x3; assignments=19683; legal=400; eight_neighbor_crossings=ALL; four_neighbor_failures=148; independent_transfer_count=PASS
negative_controls=PASS: face_adjacency, missing_A_B_exclusion, empty_window, isolated_particle
floating_packing_trial=0; inserted=11; minimum_distance=1.00504322032; defect_crossing_vertices=11; supporting_only
floating_packing_trial=1; inserted=11; minimum_distance=1.00555920681; defect_crossing_vertices=11; supporting_only
floating_packing_trial=2; inserted=14; minimum_distance=1.00007865484; defect_crossing_vertices=11; supporting_only
PASS; elapsed_seconds=0.378; peak_rss_mib=15.422
```

The exact enumeration concerns abstract labels satisfying the lemma's hypotheses; it does not assert every labeling is realizable by disks. The geometric lemma proving those hypotheses is analytic. The floating-point trials check three realizable interfaces with added strip centers, including distinct phases and jitters; they are supporting examples, not exhaustive phase or displacement certificates. Machine-readable results are in verification.json. The finite patch's lattice-index cutoff is checked by the inverse-basis norm, and every observation ball fits strictly inside that patch. The analytical theorem has no finite-patch restriction.

## 8. Attempts to break the result and second derivations

1. **Angular distortion, independent route.** If w=v+e, |v|=s and |e|<2delta, then v dot w >= s(s-2delta)>0. Its angle is acute and sin(angle)=|v cross e|/(s|w|) < 2delta/(s-2delta)=1/201<1/100. This recovers cone membership without the tangent construction, whose sharper ratio is 1/202. The rational comparisons are in the script.
2. **Covering and shells.** Equilateral triangles give covering radius s/sqrt(3), independently of the predecessor's Voronoi-hexagon derivation. Squaring 5/3<sqrt(3) gives the strict covering bound 1217/2000<1. The integer norm formula enumerates the six shortest vectors; all remaining squared norms are at least two. Independently, (sqrt(2)s-2delta)>t is the exact integer comparison 81608>48841 after multiplying by 40000. Nearest distances are below 203/200<220/200. Thus cutoff ambiguity at equality does not affect the construction.
3. **Observation radius and shared bond.** Radius 2+t is sufficient even for a bond of length exactly t, since its first endpoint has distance strictly below two from the anchor. A witness within the unit ball belongs to the neighboring radius-two ball when the anchors are a unit apart. Both observations then test precisely the same bond. Checking only one preferred bond without controlling the others would not supply this argument. Occupancy and neighbor existence cannot be dropped: an empty window or an isolated particle would otherwise pass both directional predicates vacuously.
4. **Planar parity, independent check.** The drawn-edge graph was independently built for all 482 legal labelings. Every interior degree is two or four, boundary endpoint counts are odd, and a component reaches both horizontal boundaries. A direct eight-neighbor BFS independently finds all the defect crossings. A row transfer recurrence counts legal labelings without iterating full rectangles and gives the same totals 1,81,400.
5. **Face adjacency fails.** A diagonal chain D at (1,0),(2,1),(3,2), A to its left and B to its right, satisfies every label hypothesis and has no face-connected D crossing. Exhaustive enumeration finds 40 such failures among the 81 legal 2-by-4 interiors and 148 among the 400 legal 3-by-3 interiors. The theorem explicitly uses eight-neighbor adjacency. No round-4 face-component estimate is silently transferred.
6. **Strip width, independent check.** At x=-4 the furthest observed x-coordinate is less than -4+31/10=-9/10<-203/400; the whole window is in the left pure region. At x=4 it is greater than 9/10>203/400. Thus the seven intervening columns suffice independently of the floor computation. Adding arbitrary admissible centers only within the strip preserves this and cannot decrease square occupation counts.
7. **Infinite crossing quantifier.** Crossings need not be nested. A fixed row has finitely many available defect anchors; one lies on crossings of unbounded heights. Its component, rather than an arbitrarily chosen sequence of paths, is unbounded above and below. No false inference from different finite components to one infinite component is needed.
8. **Fixed-family limitation.** Intermediate perfect crystals can be labeled defective. The separator is a geometric classification result and supplies no uniform suppression estimate for its defects. There is no estimate of conditional Gibbs probabilities or displacement-volume loss. This is the unresolved step, not a reason to apply the occupation bound to a different event.

All mathematical audits passed. The conjectured stronger face-connected conclusion is false; the counterexample is retained as a negative control. The nice wrapper warning reflects inherited priority 20 and does not mean normal-priority computation occurred. Every run is far below the 1 GiB and twenty-minute limits.

## 9. Report and final artifact audit

Wrote REPORT.md with the required PARTIAL verdict, the new arbitrary-filling separator, explicit observation parameters and strip width, reproduction commands, the failed stronger adjacency claim, fixed-family limitations, opened references, and the next Gibbs comparison test. Wrote audit_artifacts.py as a read-only consistency check.

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_artifacts.py > ARTIFACT_AUDIT.txt 2>&1
```

Exit code 0. Complete output:

```text
nice: setpriority: Operation not permitted
PASS: unchanged prior sources; complete logged outputs; exact constants; exhaustive counts; resource records; eight-neighbor and Gibbs scope consistent.
```

The audit also confirms the nested predecessor script copies equal the earlier source scripts, all required artifacts are nonempty, both complete mathematical outputs occur in this log, and the report preserves the distinction between a geometric separator and a Gibbs estimate. Only this folder was written. No git, subagents, background processes, external messages, accounts, GPU work, or numerical libraries were used. Completed the selected extension; T080 remains open.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15 10:36:07 Asia/Tbilisi, first retained clock.
