# P0110 adversary attempt

Current openness: UNKNOWN. The September ranking is historical; it is not a proof certificate. Independent derivation is saved in INDEPENDENT_OBSTRUCTION.md before any paired proof is read.

Primary source checked: Sourav Chatterjee, Annals of Mathematics 177 (2013), Theorem 1.1, pp. 665-666, https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p07-p.pdf . Its model is iid nonnegative nearest-neighbor edge passage times on Z^d for d >= 2, with a nearly-gamma law and a moment-generating function near zero. Upper exponents are uniform exponential-moment endpoints over all nonzero lattice displacements; lower exponents use uniform variance and expected-geodesic-deviation lower bounds outside a large ball. Its KPZ conclusion requires the two upper/lower pairs to match.

Review target: any use of a variance limit or expected-geodesic-deviation limit as if it automatically proved the corresponding uniform exponential-moment endpoint. A separate issue is whether a proof uses a fixed direction although the cited theorem requires all displacements.

Brain failure observed: brain.py recall returned the_binding_constraint_is_m_not_l1prime_2026_08_29 with a provisional label and the old M-obstruction summary. The underlying memory frontmatter says status: retracted and its body explicitly withdraws that obstruction. Treat the returned summary as stale. Prepare a bounded status-aware presentation patch, measured on this result, without changing live memory or global recall.

Completed source and adversary work: recovered the exact intake statement from the task-named read-only math store and checked ADH Question 22, equation (4.19), plus Auffinger--Damron Theorems 2.1--2.2. The prior math-store attempt itself labels the curvature balance conditional and leaves exponent existence and random-to-norm error control open. Current openness remains UNKNOWN; the source question does not prescribe one uniquely correct exponent definition. Matching Chatterjee's global exponents is a chosen sufficient route.

After saving the independent obstruction, read w381 L1--L5 and rederived its detour identity, overshoot geometry, norm-direction rounding and finite union bound. REVIEW.md keeps this conditional result and supplies the farther-endpoint justification in L3. A concrete l1-norm example blocks the unsupported lift from one support direction to all directions. CONDITIONAL_EXPONENTIAL_UPGRADE.md supplies an additional conditional full-tail-to-exponential-moment deduction along the rounded support direction; it remains a draft awaiting w383.

The recall-display test passed on the observed withdrawn memory and 25 synthetic cases. The bundle structural check passed: six definition/concept entries, five exact-supported relations and one existing target resolved. These checks do not verify mathematics or ingest anything. The first isolated Git application check exposed text-mode Windows newline translation in the diff; regeneration uses bytes from the frozen copies, preserving the tested code.

Concrete boundary case saved in SMALL_DISPLACEMENT_OBSTRUCTION.md: Uniform[1,2] has D(0,e_1)=0 because the direct edge costs at most 2 and every alternative costs at least 3. It fails the literally printed Auffinger--Damron lower bound over every nonzero displacement. Chatterjee's large-distance lower convention avoids this finite obstruction; exponent matching remains open in this packet. This extra deduction awaits w383. The isolated Git application check now passes byte for byte with core.autocrlf=false scoped to the command.

NEXT: w383 verify the Uniform[1,2] adjacent-vertex obstruction against Auffinger--Damron (2.2), then check the conditional exponential upgrade before any theorem promotion.
