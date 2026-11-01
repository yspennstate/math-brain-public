# P0104: sharp boundaries of variance and chaos bridges

The main target is unresolved in this work. The deliverable is an author proof of sharp special cases and counterexamples to stronger auxiliary assertions, with independent review pending. No novelty claim is made.

The canonical read-only store has the P0104 card `claim_32684d2ece2943d218971312722a87f42333b030b9c7a29f034d6c11f31f8f1d`, logical ID `math:probability.core:open-problem-p0104-subdiffusive-and-kpz-passage-time-fluctuation-exponents`. It maps the historical ID to Auffinger, Damron and Hanson, *50 years of first passage percolation*, Questions 13 and 15. The card is secondary, unverified, and not a proof.

The primary v2 manuscript, [arXiv:1511.03262v2](https://arxiv.org/pdf/1511.03262v2), gives both questions on printed page 37 (PDF page index 36): for d>=2, obtain chi<1/2 under suitable F hypotheses, identify chi=1/3 in d=2, and obtain chi>0 in suitable dimensions. Its exact qualifier is "under suitable conditions on F". The model is undirected nearest-neighbour iid nonnegative FPP. Section 3.1 discusses moment and limit-shape restrictions, and does not fix a unique interpretation of its asymptotic scaling notation. The question is therefore a research programme requiring a precise law class and an exponent definition, not a universal quantified assertion over all iid laws.

For a precise planar benchmark, fix one law F=Uniform[1,2] throughout the n limit, and define chi_- and chi_+ as liminf and limsup of log Var_F(T(0,n e1))/(2 log n), respectively. The concrete goal is chi_-=chi_+=1/3. This is a benchmark formulation, not an assertion that every shape hypothesis has already been verified for this F. Suitable-law geometry, when required by a route, must remain an explicit assumption.

The earlier canonical attempt, `claim_9ffe9930e9d9ed5c9d98ff4d61a32155d942cd754628487fc173a2d2c6493b2f`, proves only a logical warning: n/log n has log variance exponent 1, hence chi=1/2. Its independent-sum example is explicitly not an FPP model. It leaves a polynomial power-saving gap and the matching lower bound. I do not re-audit that prior review or duplicate its calculation as a new claim.

Targeted P0104 searches in the named September H/I attempt directories and Lean intake found no relevant P0104 proof. The historical Codex worktree named by the Claude intake README is absent, and the cached control-repository tree does not contain that campaign path. The canonical card and primary paper supply the recovered target. No whole export, test bank, or blind evaluation material was opened.

The owner's directed width-3 Bernoulli FPP time-constant result is a different model and observable (memory `fpp_width3_strip_time_constant_solved_2026_07_12`); it does not settle this exponent target. [Basu, Sidoravicius and Sly, arXiv:2604.01214](https://arxiv.org/abs/2604.01214), submitted 2026-04-01, gives a polynomial variance saving for a rotationally invariant planar Riemannian model. No lattice transfer is established by that abstract. Current openness as of this session remains UNKNOWN; no accepted solution was verified.

The sharp-boundary proof is in LEMMAS.md:

- C1 proves the exact fixed-endpoint moment criterion by four deterministic edge-disjoint routes. Independence is justified by their edge sets, without conditional products.
- C2 gives the Pareto threshold 4 alpha>r and the finite-mean/infinite-variance boundary at alpha=1/2.
- C3 proves the exact straight-path regime n epsilon<=2 for weights in [1,1+epsilon], and its sharpness for continuous uniform weights.
- C4 disproves a variance power bound normalized by edge variance with a prefactor and a starting scale both uniform over these laws.
- C5 gives deterministic geodesic overlap and exact refresh covariance before the detour scale.

These results constrain the following attempted route. First make the variance observable well-defined; C1-C2 show why this is necessary. Then try to gain a polynomial variance saving from independent refreshed environments and geodesic disorder chaos. C3-C5 show that this gain cannot be uniform down to a common finite scale across all bounded nondegenerate laws. A valid route must fix F, allow its crossover scale and prefactor to depend on F, justify its weighted resampling identity, and establish its actual overlap estimates. Simply dividing an axis into straight-path blocks does not repair the problem: a globally optimal route can bypass the fixed block endpoints, and order between random variables does not imply order between their variances.

Single hardest remaining gap: for one fixed suitable planar lattice law, prove control of the optimized geodesic beyond the law-dependent crossover strong enough to obtain matching variance exponents 2/3. In particular, no fixed-law multiscale cancellation estimate or matching power lower bound is supplied here. None of C1-C5 closes that gap.

The perceptron scar `perceptron_proof_open_gaps_fleet_2026_07_12` is used as a process constraint: local verification and a green pipeline do not certify the hardest global proof step. The 3,504 finite exact checks in MEASUREMENTS.json corroborate the boundary cases; they are not a formal proof or evidence of an asymptotic exponent.

NEXT: Independently audit C3-C5's strict/equality boundary and changed-law quantifier, then retain the explicit fixed-law crossover gap when integrating the draft.
