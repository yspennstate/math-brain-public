PROVED: Task received 2026-11-13 at approximately 04:46 +04: “Prove T >= 0 for the 5+1 case at N = 6, beyond a <= 11/25.”

PROVED: Step 1 (04:48 +04). Read STRAT7/RESULT.md, STRAT7/terms.py, STRAT7/scale_certificate.py, STRAT6/RESULT.md and STRAT6/moment_bounds.py read-only. All subsequent writes are restricted to STRAT9; external mesh/checklist/brain writers are omitted under the task's explicit folder-only restriction. No network or helper agents. Computation will use one process and one BLAS thread, with nice >= 10.

OPEN: Derive and audit the padded radial polynomial. The unpadded identity cannot be copied without checking its constant term, because the carrier complete graph plus an isolate need not have T=0 at a=0 for the selected projector.

OPEN: Adapt exact moment certificates and face coordinates; specify any residual domain explicitly.

PROVED: Step 2. Created frame.py, reconstructing T_N from the STRAT7 padding identity with exact SymPy rational arithmetic. The N=6 polynomial has degree two in a with fixed frame and ratio. Its coefficients are being audited before any sign claim.

PROVED: Step 3. Exact expansion gives T6=9/80+a[11(A+rB+(1+r)C)-2(1+r)]/8+a^2 H6. Since A+C,B+C>=1/4, the linear coefficient is at least 3(1+r)/32. Thus the corrected radial decomposition has an additional positive constant term and still reduces sign to the far endpoint. An explicit replay script is in preparation.

OPEN: The shell denied an attempt to increase niceness; check the inherited process priority before further computation. No processes or threads were added by that attempt.

PROVED: Step 4. verify_algebra.py reconstructs T_N independently by exact ordered-pair expansion and checks the corrected radial identity for every N>=6. T_N(0)>0 and the linear coefficient is positive. With t=a/E, T_N(a)=(1-t^2)T_N(0)+a(1-t)L_N+t^2 T_N(E). Thus a nonnegative true far endpoint suffices, with strict positivity at every smaller scale.

NUMERICAL: numerical_check.py compared 1,200 random admissible frames at N=6,7,10 (3,600 comparisons) against STRAT7/terms.py. See numerical_check.json for the seed, discrepancy and sampled minimum. This is an audit of the formula, not a sign proof.

PROVED: Process priority is inherited as zero and attempts to lower it are denied by this sandbox. Work remains short, sequential, single-process and single-threaded; no simulation sweep or large-memory computation is running.

PROVED: Step 4 audit correction. The initial numerical-check invocation failed before sampling because its output file handle shadowed the cubic symbol f. Renamed the handle and reran successfully. The final numerical JSON, rather than the failed invocation, records the completed comparisons.

PROVED: Step 5. Added cells.py with the N=6 cubic blocks [3,1+r;1+r,r^2+4r] and [1+4r,r(1+r);r(1+r),3r^2], four directional weighted-variance bounds, Bessel penalties and exact Bernstein cell verification. Copied the STRAT6 moment-polytope construction and its eight polynomial inequality certificates locally, read-only at source. Their exact replay is required before using the enhanced polytope.

PROVED: Step 6. verify_polya_moments.py replayed all 5,445 exact coefficient matrices and every principal minor. verify_cell_identities.py independently matched the arbitrary-direction weighted first and second moments and the N=6 residual blocks. The enhanced polytope and directional inequalities now have local replay scripts.

OPEN: discover_cells.py is searching ten ratio intervals with one-thread Clarabel; every exported tuple must pass cells.py's exact Fraction verification. No numerical optimum is used as a proof.

PROVED: Step 7. Added and replayed the older exact scalar lower bound A,B>=7/30 and the coefficient-matrix certificate A+C,B+C>=1/4 (verify_moments.py). Added and replayed prior_scale.py locally, proving the inherited a<=11/25 region for all N>=6. The initial directional discovery stopped at an obsolete function argument before exporting any cell; corrected that interface and restarted.

PROVED: Step 8. Ten padded directional cells have now been exported after exact verification, covering all 0<r<=1 up to at least a=66/125. The ceilings in successive width-1/10 ratio intervals are 66/125,71/125,119/200,76/125,76/125,603/1000,119/200,293/500,287/500,14/25. These are rational certificates, not solver optima.

PROVED: Step 9. Adapted the exact zero-face chart locally. zero_face.py constructs C_N=10(N-2)^2 D^2 Delta T_N, quadratic in N-6, and independently checks the N=6 specialization against the original matrix definitions. face_intervals.py encloses all three coefficients with Fraction arithmetic. discover_boxes.py exports only boxes with positive denominators and positive coefficients; verify_boxes.py reconstructs them and their exact rational-frame witnesses. See replay output for counts, including boxes missed by moment cells.

PROVED: Step 10. All 47 face boxes replayed successfully for every N>=6, because all three coefficients of C_N in N-6 are strictly positive throughout each box. Thirty-five box witnesses have a negative lower bound from every current N=6 directional cell, so these boxes certify regions beyond those moment tests. This is a finite collection of open neighborhoods, not a global cover.

OPEN: padding.py applies the same moment lower bounds to every coefficient of (N-2)^2 T_N in N-6. verify_cells.py checks whether the ten existing N=6 cells extend under this stronger certificate.

PROVED: Step 11. verify_algebra.py also matches the all-N moment coefficients and the discarded cubic remainder (N-6)(N-2)a^2 E, where E=d^2+(1+2r)e^2+(2r+r^2)f^2+r^2h^2>=0. Three full N=6 cells already extend unchanged to all N>=6. extend_cells.py is finding exact truncated ceilings for the other seven.

OPEN: Step 12. Added a small-ratio strip attempt. small_ratio_polynomial.py constructs three Bernstein controls of a homogeneous ordered-cone quartic lower bound, retaining the padded radial constant. quartic_sos.py uses one-thread Clarabel only for Gram discovery, then exact coefficient repair and rational PSD acceptance. Only a complete certificate and independent replay will support a theorem; partial output is explicitly OPEN.

PROVED: Step 13. A complete small-ratio SOS certificate at rho=3/25 was discovered, using three Bernstein controls and 858 rational 6-by-6 Gram matrices. verify_small_ratio.py reconstructs its polynomial directly from frame.py and the padded radial formula before checking every coefficient and rational PSD test. A stronger rho=1/5 candidate is now being attempted; it is not a theorem until full exact acceptance and replay.

OPEN: Step 14. The rho=1/5 small-ratio attempt left thirteen unresolved quartic coefficient forms. This is a failure of this lower-bound/SOS construction, not a counterexample. The complete rho=3/25 certificate was preserved. A rho=3/20 attempt is running.

PROVED: The ten truncated all-N cells have ceilings 66/125,71/125,119/200,299/500,59/100,23/40,559/1000,543/1000,263/500,127/250, in successive width-1/10 ratio intervals. Thus these certificates alone improve the all-N uniform scale ceiling from 11/25 to 127/250.

OPEN: Directly optimizing all three padding coefficients may improve those all-N ceilings; any accepted record is rechecked with Fraction arithmetic.

PROVED: Step 15. The complete N=6 ratio strip now reaches r<=3/20, with three exact Bernstein controls and 858 rational Gram matrices. The rho=1/5 attempt remains incomplete and is not used. Combining r<=3/20 with the ten moment cells proves the N=6 uniform scale region a<=14/25; the minimum cell ceiling outside the full strip is 14/25.

OPEN: The analogous three padding-coefficient strip is being checked with the same exact SOS acceptance rule. This would extend the full small-ratio strip to all N>=6, if all nine controls succeed.

PROVED: Step 16. Direct all-N optimization exported ten fully exact cells with ceilings 66/125,71/125,119/200,3/5,74/125,289/500,563/1000,547/1000,53/100,64/125. The all-N uniform bound is now a<=64/125. verify_allN_cells.py replays both the truncated and optimized banks.

OPEN: The all-N rho=3/20 strip attempt failed at two coefficient forms of the linear padding coefficient. No all-N ratio theorem is inferred. A rho=1/10 attempt is running.

PROVED: Step 17. Added exact elementary constant checks and a residual-certificate-gap witness search. An initial elementary assertion compared an expanded expression with an unexpanded factorization; changed it to test that their expanded difference is zero. No mathematical bound changed. residual_witness.py checks all valid zero-edge chart permutations and both column orientations against every saved box, and every saved moment multiplier at the witness. Its exact positive T is a finite certificate of that point, not a neighborhood theorem or counterexample.

PROVED: Step 18. The all-N small-ratio strip succeeded at rho=1/10, with nine Bernstein controls and 2,574 rational Gram matrices. Its independent exact replay is pending before inclusion in the final theorem. The next rho=3/25 attempt preserves that complete certificate unless a full stronger certificate succeeds.

PROVED: The explicit remaining-certificate-gap witness has U=(10,0,0,0,-10), W=(-100,80,60,60,-100), r=41/50 and a=525/866. It is connected, has a zero edge, fails every saved moment lower bound and avoids all 47 face boxes in all 24 valid charts. Its exact T6 is positive: 2219640933/6719605760. This demonstrates that the current covering arguments leave a genuine gap; it is not a counterexample.

OPEN: A final N=6 rho=4/25 strip attempt is running. The complete rho=3/20 certificate remains valid unless replaced by a completely verified stronger one.

PROVED: Step 19. Added a sequential replay_all.py driver that runs every proof certificate locally, writes individual replay transcripts, records peak resident memory, and appends each completed check to LOG.md. It launches no subprocesses or workers and enforces a 1 GiB replay RSS guard. verify_coverage.py derives the headline scale regions from the exact ratio intervals and saved rational cell ceilings.

PROVED: Step 20. The all-N full ratio strip succeeded at rho=3/25, with nine exact Bernstein controls and 2,574 rational Gram matrices. The final N=6 rho=4/25 attempt left two unresolved coefficient forms, so its theorem remains rho=3/20. Those failures are not counterexamples. Both complete certificate files are preserved and will be replayed in the final audit.

PROVED: verify_elementary.py PASS; NUMERICAL: 0.34 seconds; peak RSS 55.3 MiB

PROVED: prior_four.py PASS; NUMERICAL: 0.67 seconds; peak RSS 58.5 MiB

PROVED: prior_triangles.py PASS; NUMERICAL: 0.19 seconds; peak RSS 59.0 MiB

PROVED: verify_moments.py PASS; NUMERICAL: 0.01 seconds; peak RSS 59.6 MiB

PROVED: verify_polya_moments.py PASS; NUMERICAL: 0.81 seconds; peak RSS 64.3 MiB

PROVED: prior_scale.py PASS; NUMERICAL: 0.53 seconds; peak RSS 64.3 MiB

PROVED: verify_algebra.py PASS; NUMERICAL: 0.96 seconds; peak RSS 66.1 MiB

PROVED: verify_cell_identities.py PASS; NUMERICAL: 0.03 seconds; peak RSS 66.2 MiB

PROVED: verify_small_ratio.py PASS; NUMERICAL: 5.07 seconds; peak RSS 81.1 MiB

PROVED: verify_cells.py PASS; NUMERICAL: 9.12 seconds; peak RSS 81.1 MiB

PROVED: verify_allN_cells.py PASS; NUMERICAL: 21.50 seconds; peak RSS 81.1 MiB

PROVED: verify_allN_ratio.py PASS; NUMERICAL: 13.93 seconds; peak RSS 88.2 MiB

PROVED: zero_face.py PASS; NUMERICAL: 0.24 seconds; peak RSS 88.2 MiB

PROVED: verify_boxes.py PASS; NUMERICAL: 0.39 seconds; peak RSS 88.8 MiB

PROVED: residual_witness.py PASS; NUMERICAL: 0.01 seconds; peak RSS 88.8 MiB

PROVED: verify_coverage.py PASS; NUMERICAL: 0.04 seconds; peak RSS 99.1 MiB

PROVED: Step 21. Wrote RESULT.md with the exact N=6 formula, corrected radial identity, rational moment/SOS/box certificates, all-N extensions and the explicit residual intersection. The full theorem is labelled OPEN. The final audit is replaying all proof scripts sequentially; numerical discovery and partial certificates are excluded.

PROVED: Step 22. All exact certificates passed final replay, including 858 N=6 ratio-strip Gram matrices, 2,574 all-N ratio-strip matrices, both all-N cell banks and all 47 face boxes. NUMERICAL: The main sequential replay peaked at 99.125 MiB RSS. Individual transcripts and replay_summary.json record the checks.

PROVED: Boundary audit correction. At a=lambda, r=1 gives rank two rather than rank three. Corrected the endpoint classification in RESULT.md and extended verify_boundary.py to check both rank-two equality graphs exactly for every padding size. That added certificate passed; all seventeen proof scripts are recorded in replay_summary.json. This correction changes no scale or ratio bound.

PROVED: Step 23. Final reporting audit separated resource measurements from exact mathematical certificates. RESULT.md and LOG.md are current; replay_all.py includes all seventeen proof scripts, all of which passed. No proof conclusion uses the floating discovery runs or numerical reference samples.

OPEN: The full inequality on the explicitly specified residual region (11) remains unresolved. The delivered result is the proved enlarged regions and their replayable certificates.

PROVED: Task: “Prove T >= 0 for the 5+1 case at N = 6, beyond a <= 11/25.” Received 2026-11-13 at approximately 04:46 +04.
