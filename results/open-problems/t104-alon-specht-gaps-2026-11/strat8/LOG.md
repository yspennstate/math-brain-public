PROVED: Work began 2026-11-13 04:46 +04 on the task “Prove T >= 0 on the residual region of STRAT6.” Read STRAT6/RESULT.md, zero_face.py, face_intervals.py, verify_face_boxes.py and STRAT7/terms.py without modifying them. The STRAT6 face numerator is Cface=45 D^2 Delta T. Its 47 existing boxes are local certificates, not a full cover.

PROVED: Scope is this folder only. The task-specific restriction on all writes supersedes the general instructions to update the external brain, checklist and mesh; those external stores are not being mutated. Startup memory and the compute state were read. Use one low-priority computation process at a time, single-thread BLAS, no network and no language-model workers. Read-only imports of prior scripts use Python -B to avoid writing their __pycache__ directories.

OPEN: Reproduce the polynomial and test the 34 supplied numerical frames, then attempt a rational adaptive cover. Every accepted box must have an exact replay. Full coverage has not yet been established.

PROVED: Copied zero_face.py and face_intervals.py locally; zero_face.py replay passed all symbolic identities and reproduced the 1,254 rational coefficients. Copied the STRAT7 numerical reference as terms_reference.py. The sandbox rejects setpriority, so no claim of an OS priority change is made; computations are single-process and single-threaded, with bounded runs.

NUMERICAL: inspect_frames.py projected all 34 rounded frames (after recentering and QR orthonormalization) to their first zero-weight endpoint. All projected T values are positive; the smallest is approximately 0.0134757681 at r=0.791. The independent terms(W) discrepancy is below 1.8e-15, and the polynomial-versus-trace discrepancy below 7.5e-15. frame_evaluations.json records every coordinate and value. The supplied a_end entries are the spectral ceilings 2/(3-r), not the actual first zero-weight endpoints of these frames. Projection therefore uses the largest edge obstruction, not that field. These are floating tests only.

OPEN: A six-variable raw interval evaluation has severe dependency losses. Next compare centered polynomial bounds and adaptively subdivided Bernstein bounds, retaining exact integer/rational replay. No full face cover exists yet.

OPEN: Began exploring the lower-dimensional face with three zero weights incident to one vertex (a pendant vertex). Substituting v1=v2=-1 into Cface leaves a 49-term polynomial symmetric in the three non-neighbor y-coordinates. explore_pendant.py records the symbolic reduction; no positivity claim follows from it yet.

PROVED: The face numerator has individual degrees (6,6,6,6,6,6), total degree 8, and integer coefficients with common factor 80 (direct coefficient inspection in zero_face.construct()). This permits an exact centered expansion using a common dyadic scale and integers rather than repeated Fraction operations.

NUMERICAL: The pendant-face relaxation obtained by minimizing freely over its centered cubic moment is negative on 4,207 of 10,000 sampled relaxed spectral-domain points. That relaxation is insufficient; it is not a counterexample to the graph inequality and is not used in any certificate.

PROVED: centered_bounds.py implements exact integer Taylor inclusion bounds. If the integer polynomial P has degree d, it expands S^d P((c+y)/S) exactly; each odd-power monomial is bounded symmetrically and each all-even monomial by its sign. discover_boxes.py uses the floating charts only as seeds and exports a box only when the exact lower bound is positive. Initial six-dimensional half-widths are roughly 0.025–0.15 in chart coordinates, substantially larger than what a raw expression interval gives. The final collection and independent replay are still being developed.

PROVED: Adaptive global chart partition: 1000 nodes examined, {'split': 868, 'excluded': 132}; 737 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Adaptive global chart partition: 2000 nodes examined, {'split': 1650, 'excluded': 350}; 1301 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Adaptive global chart partition: 3000 nodes examined, {'split': 2514, 'excluded': 486}; 2029 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Adaptive global chart partition: 4000 nodes examined, {'split': 3423, 'excluded': 577}; 2847 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Adaptive global chart partition: 5000 nodes examined, {'split': 4280, 'excluded': 720}; 3561 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Adaptive global chart partition: 6000 nodes examined, {'split': 5165, 'excluded': 835}; 4331 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Adaptive global chart partition: 7000 nodes examined, {'split': 6052, 'excluded': 948}; 5105 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Adaptive global chart partition: 8000 nodes examined, {'split': 6933, 'excluded': 1067}; 5867 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Completed 34 rational six-dimensional boxes, one seeded by each supplied numerical frame. face_boxes.json records every endpoint and an exact positive lower bound for Cface, obtained with integer centered-polynomial arithmetic. Half-widths range from 1019/262144 to 38902/262144 (approximately 0.00389–0.1484). Seed inclusion is at present a numerical observation; the sign claim on each entire rational box is exact and independent of seed inclusion. Independent replay is next.

PROVED: A useful canonical chart reduces the global root domain. For each zero edge choose its endpoint with larger gap-matrix diagonal as vertex 4, reflect so z>=0, and sort vertices 1,2,3 by their first coordinates. Then 1<=t<=4, -1<=v1<=0, -1<=v2<=1/2, -4<=z1,z2<=4, 0<=z<=4. The exact derivation and all additional necessary constraints will be stated in RESULT.md. cover_face.py is constructing a partition of this whole root, retaining every unresolved leaf explicitly.

PROVED: In the pendant subface v1=v2=-1 with y3=0 (equivalently z=-z1-z2), the numerator is 80{K[A(t)+B(t)K+E(t)K^2]+12(t^2-3t+6)J^2}, where K=2(y1^2+y1*y2+y2^2), J=-3*y1*y2(y1+y2). After ordering/sign changes, feasibility reduces to two parameters v,h in [0,1]. The resulting expression is quadratic and concave in h. Exact Bernstein coefficients on t in [3/2,4], v in [0,1] are all nonnegative for the h=0 and h=1 endpoints, and all positive for minus the quadratic coefficient. A complete replay/certificate will replace this exploratory check.

PROVED: Adaptive global chart partition: 9000 nodes examined, {'split': 7658, 'excluded': 1342}; 6317 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Adaptive global chart partition: 10000 nodes examined, {'split': 8519, 'excluded': 1481}; 7039 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Adaptive global chart partition: 11000 nodes examined, {'split': 9310, 'excluded': 1690}; 7621 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Adaptive global chart partition: 12000 nodes examined, {'split': 10181, 'excluded': 1819}; 8363 boxes still OPEN. Exact certificates are being assembled; no full-cover claim.

PROVED: Adaptive refinement examined 8365 boxes; new leaves {'excluded': 1880}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 9001 boxes; new leaves {'excluded': 1903, 'positive': 368}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 10001 boxes; new leaves {'excluded': 2015, 'positive': 835}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 11001 boxes; new leaves {'excluded': 2127, 'positive': 1291}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 12001 boxes; new leaves {'excluded': 2221, 'positive': 1742}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 13001 boxes; new leaves {'excluded': 2334, 'positive': 2178}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 14001 boxes; new leaves {'excluded': 2414, 'positive': 2639}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 15001 boxes; new leaves {'excluded': 2546, 'positive': 3062}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 16001 boxes; new leaves {'excluded': 2666, 'positive': 3488}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 17001 boxes; new leaves {'excluded': 2796, 'positive': 3900}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 18001 boxes; new leaves {'excluded': 2913, 'positive': 4313}. The unsolved frontier remains OPEN.

PROVED: pendant_certificate.py --export passed: it reconstructs the subface identity and verifies all 91 nonnegative rational Bernstein coefficients (including strictly positive controls for A and minus the h-quadratic term). pendant_certificate.json stores the certificate.

PROVED: Rationalizing the supplied frames to integer orthogonal pairs gives 34 exact connected zero-weight endpoints. All 34 fail all applicable saved STRAT6 moment lower bounds and the strengthened nonlinear sufficient condition (when applicable), and no chart lies in any prior face box. Initial attempts to enclose their chart square roots used an absolute precision insufficient for the very large integer frame denominators; the enclosure test rejected them. Increasing to 256-bit integer-square-root enclosures fixes the precision issue without changing any sign certificate. New boxes are being added where rationalization changes the first zero edge.

PROVED: Adaptive sensitivity-based refinement has begun to certify boxes on the whole-root partition. Acceptance still uses integer/rational arithmetic only; floating priorities merely choose which OPEN leaf to split. Thousands of positive leaves have now been found. The remaining leaves will stay explicitly OPEN, with a replay that also proves the tree covers the entire canonical root.

PROVED: Adaptive refinement examined 19001 boxes; new leaves {'excluded': 3025, 'positive': 4734}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 20001 boxes; new leaves {'excluded': 3121, 'positive': 5169}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 21001 boxes; new leaves {'excluded': 3247, 'positive': 5575}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 22001 boxes; new leaves {'excluded': 3326, 'positive': 6017}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 23001 boxes; new leaves {'excluded': 3413, 'positive': 6456}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 24001 boxes; new leaves {'excluded': 3514, 'positive': 6884}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 25001 boxes; new leaves {'excluded': 3632, 'positive': 7285}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 26001 boxes; new leaves {'excluded': 3754, 'positive': 7687}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 27001 boxes; new leaves {'excluded': 3869, 'positive': 8085}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 28001 boxes; new leaves {'excluded': 3987, 'positive': 8491}. The unsolved frontier remains OPEN.

PROVED: 2026-11-13T05:03:29+04:00. Checkpoint time labels had been entered manually; those estimated labels have been removed. The start time and this automatically read clock time are retained. Subsequent progress records use the system clock.

PROVED: Independent local replay verify_boxes.py passed all 43 rational boxes and matched every center against the separate factored matrix expression exactly. The 34 exact rational witnesses are all enclosed, and all miss the previous moment and face-box certificates and nonlinear test. A full residual-filter check is in progress.

PROVED: Adaptive refinement examined 5694 boxes; new leaves {'positive': 2}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 6000 boxes; new leaves {'positive': 132, 'excluded': 29}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 7000 boxes; new leaves {'positive': 549, 'excluded': 136}. The unsolved frontier remains OPEN.

PROVED: witness_residual.py passed all 34 exact endpoints against every STRAT6 residual-region filter, including the old 19-vertex and enhanced 33-vertex thresholds, all saved scale ceilings, the actual-moment test, every applicable multiplier lower bound, and all old face-box symmetries. Thus these are certified examples from the precisely requested residual set, now covered by the new local boxes.

OPEN: The second global refinement pass is running from the 5,692-leaf OPEN frontier. Its certificates and the whole-chart cover will be replayed before the final count is reported as verified. Closed-box overlaps on subdivision boundaries will be handled explicitly in the residual description.

PROVED: Adaptive refinement examined 8000 boxes; new leaves {'positive': 946, 'excluded': 264}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 9000 boxes; new leaves {'positive': 1320, 'excluded': 408}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 10000 boxes; new leaves {'positive': 1740, 'excluded': 507}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 11000 boxes; new leaves {'positive': 2154, 'excluded': 606}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 12000 boxes; new leaves {'positive': 2544, 'excluded': 733}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 13000 boxes; new leaves {'positive': 2975, 'excluded': 807}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 14000 boxes; new leaves {'positive': 3420, 'excluded': 879}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 15000 boxes; new leaves {'positive': 3842, 'excluded': 979}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 16000 boxes; new leaves {'positive': 4267, 'excluded': 1066}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 17000 boxes; new leaves {'positive': 4676, 'excluded': 1173}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 18000 boxes; new leaves {'positive': 5099, 'excluded': 1264}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 19000 boxes; new leaves {'positive': 5535, 'excluded': 1343}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 20000 boxes; new leaves {'positive': 5927, 'excluded': 1467}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 21000 boxes; new leaves {'positive': 6329, 'excluded': 1582}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 22000 boxes; new leaves {'positive': 6745, 'excluded': 1681}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 23000 boxes; new leaves {'positive': 7129, 'excluded': 1810}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 24000 boxes; new leaves {'positive': 7535, 'excluded': 1912}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 25000 boxes; new leaves {'positive': 7925, 'excluded': 2020}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 26000 boxes; new leaves {'positive': 8344, 'excluded': 2106}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 27000 boxes; new leaves {'positive': 8765, 'excluded': 2193}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 28000 boxes; new leaves {'positive': 9170, 'excluded': 2297}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 29000 boxes; new leaves {'positive': 9559, 'excluded': 2412}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 30000 boxes; new leaves {'positive': 9997, 'excluded': 2479}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 31000 boxes; new leaves {'positive': 10381, 'excluded': 2595}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 32000 boxes; new leaves {'positive': 10778, 'excluded': 2699}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 33000 boxes; new leaves {'positive': 11187, 'excluded': 2791}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 34000 boxes; new leaves {'positive': 11564, 'excluded': 2919}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 35000 boxes; new leaves {'positive': 11936, 'excluded': 3064}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 36000 boxes; new leaves {'positive': 12340, 'excluded': 3163}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 37000 boxes; new leaves {'positive': 12749, 'excluded': 3268}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 38000 boxes; new leaves {'positive': 13137, 'excluded': 3391}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 39000 boxes; new leaves {'positive': 13523, 'excluded': 3509}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 40000 boxes; new leaves {'positive': 13925, 'excluded': 3617}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 41000 boxes; new leaves {'positive': 14262, 'excluded': 3777}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 42000 boxes; new leaves {'positive': 14640, 'excluded': 3907}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 43000 boxes; new leaves {'positive': 14987, 'excluded': 4063}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 44000 boxes; new leaves {'positive': 15352, 'excluded': 4202}. The unsolved frontier remains OPEN.

PROVED: Adaptive refinement examined 45000 boxes; new leaves {'positive': 15764, 'excluded': 4292}. The unsolved frontier remains OPEN.

PROVED: Final witness audit strengthened exclusion from prior boxes to strict interval separation: for every old box and every zero-edge chart, at least one exact coordinate enclosure is disjoint from that closed box. Failed containment alone would not prove non-membership. All 34 witnesses pass the stronger check. Their rational T values were also independently re-derived from the trace formula, matching the moment formula exactly.

PROVED: axis_bernstein.py adds an exact one-coordinate Bernstein conversion followed by signed monomial bounds in the other five coordinates. All 28 monomial conversion identities through degree six have replayed symbolically. This will be applied to the remaining OPEN boxes without further subdivision, with each accepted control lower bound saved for replay.

PROVED: One-axis Bernstein pass tested 500 OPEN boxes; 0 exact new positive leaves.

PROVED: One-axis Bernstein pass tested 1000 OPEN boxes; 1 exact new positive leaves.

PROVED: One-axis Bernstein pass tested 1500 OPEN boxes; 1 exact new positive leaves.

PROVED: One-axis Bernstein pass tested 2000 OPEN boxes; 8 exact new positive leaves.

PROVED: One-axis Bernstein pass tested 2500 OPEN boxes; 11 exact new positive leaves.

PROVED: The draft RESULT.md now includes the exhaustive Gram-chart construction, proofs of every canonical coordinate bound, exact centered and one-coordinate Bernstein certificate rules, the pendant proof, and a fully specified inherited residual R6. At an endpoint a=a_end, the prior current-scale and endpoint filters coincide; the positive connectedness clearance makes its minimum-weight filter automatic.

PROVED: One-axis Bernstein pass tested 3000 OPEN boxes; 11 exact new positive leaves.

PROVED: One-axis Bernstein pass tested 3500 OPEN boxes; 11 exact new positive leaves.

PROVED: One-axis Bernstein pass tested 4000 OPEN boxes; 15 exact new positive leaves.

PROVED: One-axis Bernstein pass tested 4500 OPEN boxes; 15 exact new positive leaves.

PROVED: One-axis Bernstein pass tested 5000 OPEN boxes; 16 exact new positive leaves.

PROVED: Final exact replay has checked 20000 tree nodes; verified counts so far {'split': 10005, 'excluded': 2559, 'open': 1236, 'positive': 6200}. Full replay is still running.

PROVED: Final exact replay has checked 35000 tree nodes; verified counts so far {'split': 17506, 'excluded': 4942, 'open': 2146, 'positive': 10406}. Full replay is still running.

PROVED: Final exact replay has checked 45000 tree nodes; verified counts so far {'split': 22506, 'excluded': 5880, 'open': 2570, 'positive': 14044}. Full replay is still running.

PROVED: Final exact replay has checked 50000 tree nodes; verified counts so far {'split': 25006, 'excluded': 6481, 'open': 2761, 'positive': 15752}. Full replay is still running.

PROVED: Final exact replay has checked 55000 tree nodes; verified counts so far {'split': 27503, 'excluded': 7181, 'open': 3209, 'positive': 17107}. Full replay is still running.

PROVED: Final exact replay has checked 60000 tree nodes; verified counts so far {'split': 30004, 'excluded': 8025, 'open': 3629, 'positive': 18342}. Full replay is still running.

PROVED: Final exact replay has checked 75000 tree nodes; verified counts so far {'split': 37502, 'excluded': 9647, 'open': 4636, 'positive': 23215}. Full replay is still running.

PROVED: Final exact replay has checked 80000 tree nodes; verified counts so far {'split': 40003, 'excluded': 10078, 'open': 5217, 'positive': 24702}. Full replay is still running.

PROVED: 2026-11-13T05:17:09+04:00. Full exact replay passed: 43 local boxes; global counts {'split': 40181, 'excluded': 10208, 'open': 5272, 'positive': 24702}; 34 residual witnesses and the pendant subface theorem. Peak RSS 151764992 bytes. verification.json records hashes and results. The residual OPEN leaves are not certified.

PROVED: 2026-11-13T05:20:36+04:00. Final audit passed: all 27 hashes in verification.json match their proof artifacts; explicit leaf files contain exactly 24,702 positive and 5,272 OPEN boxes. RESULT.md gives the canonical-domain proof, local and global certificate rules, the 91-control pendant theorem, and exact residual set (R), including all chart symmetries and closed-boundary exclusions. All 34 exact enlargement witnesses satisfy every inherited residual filter.

NUMERICAL: Complete exact replay runtime approximately 211.57 seconds; measured peak resident memory 151,764,992 bytes (144.734375 MiB). No worker pools, no network, no language-model workers. No task computation is left running.

OPEN: The universal residual inequality remains unproved on set (R). This is the requested partial-cover fallback, with every unresolved box retained, rather than a claim that a finite positive bank settles the continuum.

PROVED: Task: “Prove T >= 0 on the residual region of STRAT6” — received 2026-11-13, approximately 04:46 +04.
