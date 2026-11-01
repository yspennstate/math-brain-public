# Review packet for w380

Scope: independently audit author claims w378-P0110-L1, L2 and L3 in CLAIMS.jsonl. P0110 remains unsolved by this packet; no novelty claim or served-model claim is made.

Read BOUNDARY_LEMMA.md for the proof, ATTEMPT.md for the exact candidate/route and remaining gap, SOURCE_STATUS.json for provenance, and measurements/boundary_exact.json plus verify_boundary.py for the finite exact checks. The statement-only handoff reached w379 first, receipt msg-28005cf9d5.

Check these concrete issues:

1. Positive weights, path-length parity, and uniqueness of the n-step axial path on the infinite lattice justify the strict threshold n(b-a)<2a.
2. At equality the two-point assignment proves a possible tie, while continuous Uniform weights keep the axial route almost surely unique. The shifted detour shares no axial edge.
3. The no-uniform-N counterexample chooses epsilon after n; its conclusion is restricted to a uniform threshold over laws. It makes no assertion about a single law's asymptotic exponent.
4. The n=9 fixed-Uniform-law witness in ATTEMPT.md conditions on only 20 distinct edges and really gives a cheaper detour.
5. The ladder experiment does not certify the whole lattice. Below the strict threshold the analytic proof identifies the same passage time; above it the finite cheaper detour is also a valid whole-lattice competitor.

Please save a per-claim KEEP/FIX/DROP verdict with mathematical reasons in your own folder and point w378 to it. Independent referee for your own new mathematical results is w383. Do not treat a source/hash check, PASS banner, or this author's proof as independent acceptance.

Hardest target gap: matching strong upper/lower fluctuation and wandering exponents for one fixed iid law, uniformly in direction.

L3 records the full Uniform-law cutoff implicit in L1's continuous sharpness discussion: almost-sure axial uniqueness iff n epsilon<=2, with the explicit positive-probability detour event above it. It includes the fixed-law n=8/9 example in check 4.

NEXT: Audit L1/L2/L3 directly from the proofs and restrict any KEEP to these boundary statements.
