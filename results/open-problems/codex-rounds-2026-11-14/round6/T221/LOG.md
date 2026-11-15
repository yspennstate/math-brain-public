# T221 round 6 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session date: 2026-11-15, Asia/Tbilisi. Exact start time will be recorded from the clock.

First clock reading: 2026-11-15 11:15:52 Asia/Tbilisi (07:15:52 UTC); orientation began shortly before it.

## Scope and startup

All mutations are confined to this folder. The specific task restriction supersedes the global instructions to mutate the shared brain, checklist and agent mesh. Read the startup memory index and compute_state.json without mutation; compute status was ok / owner_away_open. No git, subagents, external messages or account creation. Numerical commands will use nice -n 15, one thread, a time limit, and a memory check below 1 GiB.

## Bounded literature check

Within the first five minutes, searched `"Rokhlin" "Bernoulli" "RBS" 2026` and `"Rokhlin entropy" "Bernoulli shifts" 2025 2026 Seward`. Opened:

- Brandon Seward, *Krieger's finite generator theorem for actions of countable groups II*, arXiv:1501.03367v4, https://arxiv.org/abs/1501.03367v4 and https://arxiv.org/html/1501.03367v4 . The abstract gives the conditional universal RBS theorem.
- Lewis Bowen and Michael Chapman, *Surjunctivity does not characterize cosoficity of invariant random subgroups*, arXiv:2511.06586, https://arxiv.org/abs/2511.06586 . The abstract concerns a non-cosofic IRS with an RBS analogue.
- Zongrui Hu, Leiye Xu, Shuhao Zhang, *Positive Rokhlin Entropy Implies Infinite L^1-Orbit Multiplicity: A Negative Answer to Thouvenot's Question*, arXiv:2607.11549, https://arxiv.org/abs/2607.11549 . The abstract concerns amenable actions and a consequence of positive entropy.

No resolution found; this bounded search is not proof of absence. Continue the finite-table problem.

## Planned independent check and one extension

Read all four predecessor reports, logs, proofs and scripts before mathematical work. Independently reconstruct the fair-AND stationarity certificate rather than trusting a floating optimizer result.

Chosen extension: strengthen the same 103-type relaxation by the ab/ba fixed-point identity, then determine which further conjugacy identities are visible as word-equality events in this window. Certify the rank and a concrete exclusion beyond the predecessor's example, and test whether these identities characterize realizable frequencies. This is one compatibility refinement of the existing table; it supplies no RBS witness on its own.

## First compatibility computation

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 compatibility_audit.py`.

Exit 0; 0.0222 seconds; 16,596,992 bytes peak RSS; effective nice priority 20. The wrapper diagnostic reflects inherited priority 20, as checked in the script. Independent predecessor verification passed: 103 exact costs, 103 certificate slacks, three equalities, rank four and both attainable extrema.

Grouped all 21 two-word equality events by cyclic reduction and conjugacy up to inversion in the free group. They form ten classes, hence eleven representative-difference rows. Exact elimination gives ranks 4 for stationarity, 5 after the ab/ba row, and still 5 after all eleven pair-conjugacy rows. Thus the suggested row supplies the only additional linear constraint of this specified kind. Data saved in compatibility_result.json.

A new obstruction survives: singleton pi=(0,1,2,0,3,4,1) is admissible and stationary and satisfies all pair-conjugacy rows, but asserts a=bb everywhere and ab!=ba everywhere. Globally A=B^2 would imply commutation, so it is impossible. Next derive a robust inequality on the SAME table, using the boundary of E={v:A(v)=B^2(v)} under B. At an E-root, noncommutation is exactly departure from E along B; equal numbers enter and leave E. Entrances are noncommuting roots outside E. This suggests the sharper bound P(E and ab!=ba)<=P(E^c and ab!=ba), and in particular P(ab!=ba)<=2P(a!=bb). Check the proof and sharpness before reporting.

The first expanded audit stopped on a mistyped C3 attainment tuple, before the exhaustive-model loop: (0,1,2,0,0,0,0) is inadmissible. Directly evaluating a=cycle and b=inverse cycle gives the correct tuple (0,1,2,2,0,0,1); corrected that test fixture. No proposed mathematical inequality failed.

## Expanded audit passed; boundary inequality proved

Re-ran the same command after correcting the fixture. Exit 0; 0.218 seconds; 17,088,512 bytes peak RSS; priority 20. All 15,017 permutation pairs on one through five points (74,421 roots) satisfy every stationarity and pair-conjugacy row and the new inequality. The rank-five determinant is exactly one; normalization raises the rank to six.

The new exact inequality is sum x_pi (2 I_{a=bb}-1) I_{ab!=ba} <= 0. Proof: for E={A=B^2}, its noncommuting roots are exactly the exits from E under B. Entrances have equal cardinality and are noncommuting roots outside E. Hence noncommuting E-roots cannot outnumber noncommuting non-E roots. It implies d_H(BA,AB)<=2d_H(A,B^2). Both coefficients are sharp on the four-point model A=(0,3,2,1), B=(1,2,3,0): E={1,3}, noncommutation at all four roots.

The new singleton (0,1,2,0,3,4,1) violates the signed inequality by one and hence has frequency at most 1/2 in every finite model or limit. Its explicit five-point completion is A=(1,0,4,2,3), B=(2,3,1,0,4). Its fair-AND cost is (9/2)log2+(3/4)log3-(5/16)log5-(21/16)log7 = 0.8861651107500812 > log2, so the old entropy inequality does not exclude it. Data saved in compatibility_result.json.

Wrote PROOF.md with the complete pair-conjugacy classification, explicit row identities, determinant-one rank witness, boundary proof, sharpness example, singleton obstruction, and independent five-bit law calculation. The fair-AND extrema and general-p upper cap do not improve because their actual finite-model attainments survive every valid compatibility constraint. Next: independent verifier using different partition construction, inclusion-exclusion probabilities, and a separate direct cycle-boundary count.

## Independent verification and attempts to break the result

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_compatibility.py`.

Exit 0; 0.0421 seconds; 16,203,776 bytes peak RSS; priority 20. It reconstructs partitions by block insertion rather than restricted-growth strings, tests partial bijections rather than pairwise equivalences, computes the joint laws by inclusion-exclusion rather than class-bit assignments, and expands entropy in prime-log forms rather than a product of rational powers. It independently matches all 103 exact costs, all 103 nonnegative predecessor slacks (three zero), all eleven explicit row identities, and the rank-five minor by elimination rather than the Leibniz expansion.

The new singleton's law was derived separately by conditioning on its bit U: nonzero (R,N) counts out of 32 are 14,2 for R=0 and 10,2,1,1,1,1 for R=1. Inclusion-exclusion gives exactly the same law and the same cost. The sign above log2 is independently the integer comparison 2^56*3^12 > 5^5*7^21. These computations remove any reliance on rounded entropy values.

The second verifier checks the boundary inequality directly from actual permutations and sets for all 15,017 pairs on one through five points, without any type table or matrix calculation. It independently reproduces 74,421 roots from sum n(n!)^2. It finds 384 models with nonzero equality on both sides. The reported four-point model attains both coefficients. The weaker distance constant two was also re-derived from the triangle inequality and bi-invariance by inserting B^3 between BA and AB.

Cases challenged: E empty or full; fixed points of either generator; ab=ba at some or every root; one-point and two-point actions; collisions that occur at one root but not globally; equality of inverse-word fixed-point fractions versus pointwise equality; ordinary right/left composition order; exact zero slacks; and limits of frequency vectors. All constraints are finite linear equations or inequalities on the same 103 coordinates and therefore pass to limits. The new singleton passes the old AND entropy inequality, so its exclusion does not merely repeat that inequality. Its frequency bound 1/2 is a proved bound, with no claim that this particular type attains it. No sufficiency theorem is asserted for the strengthened relaxation.

No new RBS case, positive-gap group/code, or non-sofic candidate has been established. All checks after the corrected C3 test fixture passed. The actual finite-model extrema prevent an AND cap improvement, so the extension's result is the compatibility constraint and its explicit exclusion.

## Final report and artifact audit

Wrote REPORT.md with the required PARTIAL verdict, the rank-five classification, sharp joint-event inequality, new singleton and its exact cost, commands, failures, limitations and the next concrete extension. PROOF.md defines normalized Hamming distance explicitly and gives every boundary-count step.

Ran a final read-only Python audit under the same one-thread environment and nice -n 15, with a 60-second alarm. Exit 0. It parsed both scripts, verified the report verdict, all 18 consecutive equation tags and balanced mathematical delimiters, ten classes containing all 21 events, eleven conjugacy rows, all 103 signed-inequality columns, and agreement of rank/model/root counts between the independently generated JSON files. Output: `Artifact audit passed: verdict, 18 equation tags, balanced math delimiters, script syntax, 21 events in 10 classes, 11 rows, 103 inequality columns, matching rank/model/root counts.`

All deliverables are in this folder: REPORT.md, PROOF.md, LOG.md, compatibility_audit.py, verify_compatibility.py, compatibility_result.json, independent_verification.json. No predecessor artifacts, shared brain/mesh/checklist state, git state, or external systems were mutated. No subagents or additional language-model workers were started.

## Independent predecessor check passed

Read all four predecessor reports, logs, proofs and scripts. Recomputed fair class-label laws and expanded rational entropy powers without importing a predecessor script. All 103 exact costs, all stationarity columns, all 103 nonnegative dual slacks and the three equality cases match. Rational elimination gives stationarity rank four. The attained costs log 2 and (3/2)log 2 are exact. The earlier main result holds. The direct conditional bound C <= H(R)+H(E|R) independently proves the upper bound.
