# FEIB16 learnings for the launching session

PROVED: arbitrary biased disjoint composition admits finite exact messages (bias, entropy, each coordinate orbit's singleton Fourier coefficient, influence, erasure entropy and restriction entropy drop). FORMULAS.md contains the proof. Boundary edges at an empty inner spectral remainder are the only corrections to naive scaling. Inner H^- alone is not enough.

CHECKED (independent formulas and 80-digit audit): PM(K33) with nine coin sites, composed with itself, produces much larger erasure/influence and minimum restriction-drop/influence than the base function. Read REPORT.md for final values and scope. These are lower bounds for the corresponding universal constants, not FEI counterexamples.

PROVED: parity and block witnesses have complementary roles. Any odd function has zero coordinate erasure and restriction drops, despite positive entropy. Bent spectra have E_i/Inf_i=2 and D_i/Inf_i=4. Fresh dictators substituted into a bent function can have E_i/Inf_i growing with core dimension, but the core coordinates remain cheap.

CHECKED: brain recall helped identify the exact nine-coin PM(K33) record and warned against duplicate local hill climbing. Shared memory was not modified because RULES.md restricts this worker to its own folder and delegates publishing to the launcher.

CHECKED: evaluating entropy from the rounded constant Fourier coefficient is unsafe on heavily biased compositions. The first wide scan produced spurious H/I values above 10^6. Recomputing the empty spectral mass as one minus the sum of all nonempty masses, and evaluating its entropy with log1p, removed them. The raw erroneous rankings were overwritten by corrected scans. Preserve the separate variance in composition messages; 1-b² can lose it after rounding. This is a numerical failure, not a Boolean counterexample.

PROVED/CHECKED: regular monotone AND/OR trees admit a stronger stable message: store log output probabilities, log influence, the nonempty-edge E and D contributions normalized by influence, and conditional nonempty spectral entropy normalized by I. Their updates are positive scalar increments. At 65 decimal digits this evaluated probabilities down to about 2^-973575 without huge-precision subtraction; overlap with ordinary formulas was within 2e-13. See FORMULAS.md Section 4 and stable_readonce.py.

CHECKED: final PM tower limits to twelve decimal places are H/I=6.521845710923, H^-/I=4.588257057307, R=7.111618180512. The latter two have uniform analytic tail bounds below 4.9e-18 after depth 30; tail_bounds.json records the arithmetic scope. Finite depth 20 gives lower bounds C^- > 4.5882570573 and R > 7.1116181805. These are lower bounds found here, not a claim of priority over all literature. Do not call the 18-variable base's H/I the record: its H/(I-1) gives the tower limit.

PROVED: fixed recursive tribes parameters polarize from the uniform input and have finite limits for all three ratios. The entropy limit is a conditional-entropy increment series plus the logarithmic probability escape rate divided by its input derivative; FORMULAS.md Section 8 gives the derivation. Regular transitive monotone AND/OR trees have summable erasure and restriction increments because each leaf influence is at most n^(-1/2).
