# C0049: sharp-boundary adversary

2026-10-10. Author w595. Parent target NOT SOLVED. Current general openness UNKNOWN. Independent derivation was saved before paired-proof access in INDEPENDENT_DERIVATION.md.

The recovered target is Duminil-Copin's Lectures on the Ising and Potts Models on the Hypercubic Lattice, arXiv:1707.00520, Conjecture 3, printed page 93 (PDF page index 92). For fixed q in (0,4] excluding 2, set p=p_c(q) and approximate a simply connected marked domain (Omega,a,b) by square-lattice Dobrushin domains (Omega_delta,a_delta,b_delta). The FK exploration curves should converge weakly to chordal SLE_kappa as delta tends to zero, with kappa=8/(1+sigma)=4*pi/[pi-arccos(sqrt(q)/2)] and sigma=(2/pi)*arcsin(sqrt(q)/2). The source's word 'approximating' is not a complete topology/hypothesis specification inside the conjecture itself; any proof must fix its precise domain and curve convergence conventions. For q<1, do not silently equate p_c with p_sd or import q>=1 RSW/FKG.

The main mathematical contribution is a complete author-derived proof of conditional driver identification using two Laurent coefficients, without an a priori semimartingale assumption. It includes sigma=1/q=4 and pinpoints sigma=0 as the degeneration of this particular observable. It does not prove observable convergence in FK.

The second contribution is an explicit bounded rare-jump martingale sequence converging uniformly almost surely on compact time intervals to exp(-t), which is not a martingale. This is a counterexample to an overstrong martingale-passage bridge, not to FK interface convergence. Uniform integrability is one sufficient repair; an alternative rigorous martingale-passage argument is also admissible.

The single hardest unchecked FK step in the parafermionic route is the correctly normalized observable limit in random evolving slit domains with enough control to establish true stopped martingales in the driver filtration. Once that holds, the conditional identification theorem applies even at q=4. A new discrete relation is a possible approach, not an established necessary condition for all routes.

The primary author preprint Conformal invariance of the planar four-state Potts model and its random-cluster representation, Theorem 1.2, states q=4, p=2/3 free-boundary loop convergence to CLE4 for Caratheodory domain approximations and the stated loop metric. It is a substantial endpoint update. It does not state a Dobrushin chordal SLE4 theorem, so this packet does not mark that precise target solved. Its proof uses the six-vertex/GFF route. No independent verification of that published proof is claimed here.

Source checks H/I attempts and the Lean intake: targeted exact-ID/title search returned no additional C0049 proof in those three named directories. This is a search result, not a proof of absence or current openness.

Scars read: perceptron_proof_open_gaps_fleet_2026_07_12 and audit_finding_pathconv_limit_event_positivity_2026_07_16. A passed computational check or a local theorem cannot certify the parent target; limiting conditioning and limiting martingale assertions need their own hypotheses.

STUCK: team_comm delivery failed first because w595 has no registered team, then because probability300-integration is not a registered team in this environment. Use a named-peer mesh path or an explicit task-local team instead; mathematical work continues.

NEXT: Inspect the paired author's saved original proof, check random-domain/martingale passage, and attach the exact source/hash and independent-review status to the draft bundle.
