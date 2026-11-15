# FEIB06 status

Started 2026-11-10 01:29 +04. Read fleet rules, brief, and FEI NOTES.md.
Scope: census of every E/D node and coordinate; potential fits with explicit root/leaf conditions; counterexamples and proofs.

The fleet's specific rule forbids mesh/checklist/brain mutations and all writes outside this folder; those global routines are therefore not run. Recall was consulted read-only. The default math-store lookup reports no store.

Important correction to the brief: with the displayed sign in (*), +B is tautological, whereas -B doubles J. Both B gauges and the entropy gauge will be identified and excluded from candidate results.

DONE: final census, fits, independent audits, proofs, tables and REPORT.md are saved. No working potential was found; FEI remains open.

Census: exhaustive Boolean roots through n=4; 9,668 five-variable and 11,783 six-variable truth tables, each with every E/D order represented. Source counts: census_summary.json. Saved compressed data: 131,322,091 bytes.

All 200 saved finite LP/MILP fits passed independent node-potential verification. The 24 enlarged-box best-coordinate fits agree to within 1.606e-9 in total objective. Numerical checks and tolerances are in fit_verification.json and summary.json. Maximum recorded RSS: 1,178,091,520 bytes; numerical processes ran at nice 10 and one thread each, at most two together.

PROOFS.md classifies the unweighted entropy family and rules out finite polynomial level-mass, quadratic level-weighted B, and level-profile/marginal-entropy families under a universal root budget. proof_checks.json supplies killing examples for every n=6 total-objective fit outside the excluded B diagnostics. RESULTS.md contains both local-C and C+Cprime tables; DATA.md has the schema and replay commands. REPORT.md is the final handoff.

NEXT: no brief work remains. The launching session can read REPORT.md and decide what to publish or store in shared memory; arbitrary potentials outside the obstructed families remain open.
