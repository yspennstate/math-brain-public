# C0017: statement-only handoff

Date: 2026-10-10. Worker: w408. Adversary: w409. Referee: w410.

Precise working interface target: Let D be a bounded simply connected Jordan domain and a,b distinct boundary points. Approximate (D,a,b) by connected square-lattice domains of mesh delta, with boundary prime ends converging and no persistent artificial fjords. Sample independent Bernoulli(1/2) bonds with Dobrushin exploration boundary conditions: one boundary arc is primal wired, the other dual wired. The distinguished medial exploration from a_delta to b_delta should converge in law, as delta tends to zero, to chordal SLE_6 from a to b, as continuous curves modulo increasing reparametrization with the uniform curve metric. An independently justified interface-to-full-configuration argument is needed for a full conformally invariant percolation scaling limit.

For precision, the approximation class used in this packet consists of finite simply connected medial Dobrushin domains converging to D in the Caratheodory sense and with orientation-preserving boundary parametrizations j_delta,j on the circle satisfying sup|j_delta-j| -> 0; the marked parameter values converge to a,b. This replaces the informal no-persistent-fjords phrase above. These explicit boundary hypotheses are part of the working target, not a claimed theorem for arbitrary rough approximations.

The recovered intake also asks for Cardy's formula: for a Jordan quad with cyclic boundary marks conformally sent to (0,u,1,infinity) in the upper half-plane, the critical iid square-bond probability of an open crossing between the first and third boundary arcs should converge to C(u)=B(1/3,1/3)^(-1) integral_0^u [v(1-v)]^(-2/3)dv. Primary historical source: Garban-Steif arXiv:1102.5761v3, Chapter II section 4, PDF page 26, printed page 24. The original source discusses the conformal scaling-limit problem; these are the precise interface/crossing formulations used in this task.

This is the interface formulation we attempt; it is not silently equated with all CLE_6 or all joint crossing statements. p_c=1/2 is a known input, not a missing lemma.

Current openness: UNKNOWN. The dated 2026-09-07 ranking says attempted_un. Wang Zhou's arXiv:2409.03235v6 (2024-12-17) claims SLE_6 convergence. Ioan Manolescu's arXiv:2502.08394v1, Conjecture 5.1 and discussion around Theorem 5.2, still distinguishes the conjectural conformal scaling limit from established rotational invariance. Neither an abstract nor a source hash is a proof audit.

Claim boundary: w408 proposes the stochastic identification step from two boundary Cardy martingales, without presupposing that the Loewner driver is a semimartingale. Please independently try to break that boundary, and identify the model-specific input it actually needs. No proof or derivation is included in this handoff.

Sources: https://arxiv.org/abs/2409.03235 ; https://arxiv.org/html/2502.08394v1#S5 .
