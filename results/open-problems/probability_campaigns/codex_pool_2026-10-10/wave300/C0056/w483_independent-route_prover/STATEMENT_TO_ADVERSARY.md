C0056 exact-source recovery — statement only, 2026-10-10

Source: Paul Bourgade, Random band matrices (ICM 2018), arXiv:1807.03031, section 2.1, printed page 7, equation (2.1), plus the finite-volume paragraph on that page. Primary author PDF: https://math.nyu.edu/~bourgade/papers/ICMProceedings.pdf .

The source model is H_RS=Delta+lambda V on l^2(Z^d), with iid centered variance-one real site potentials, lambda>0, and free hopping band [-2d,2d]. It predicts extended states at small disorder in d>=3 and discusses absolutely continuous spectrum. The source also separately predicts GOE bulk microscopic statistics for the restriction to periodic boxes. The survey states a research question and does not prescribe a single distribution, energy interval, or complete quantifier scheme. Its claims of openness are historical (2018).

Short source quote: "not only is the existence of delocalized states in dimension three open, but also there is no clear understanding". The sentence continues by distinguishing the implication to GOE statistics. This quote is evidence of historical scope, not current status.

Intake exact text: "Prove existence of absolutely continuous spectrum (delocalised states) for the random Schrodinger operator -Delta + lambda V on Z^3 at small disorder lambda, and GOE local statistics for its finite-volume restriction." Record: probability_1000_intake_claude_20260907/problems.jsonl, problem_id C0056, line 56. The intake combines two goals.

Precise slice for this lane: use iid V_x uniform on [-1,1] and H_g=A+gV on l^2(Z^3), where (A psi)(x)=sum_{|y-x|=1}psi(y). Uniform variance-one potentials equal sqrt(3)V, so g=sqrt(3)lambda. The sign of A is changed by the bipartite unitary psi(x)->(-1)^{x_1+x_2+x_3}psi(x).

Spectral target T_AC: find a deterministic nonempty open interval I subset (-6,6) and g_0>0 such that for EACH FIXED 0<g<g_0 the operator almost surely has a nonzero absolutely continuous spectral component in I. Pure absolute continuity on I is a stronger sufficient target; it excludes both pure-point and singular-continuous mass. An event common to all uncountably many couplings is not required. This quantified uniform-law slice is our explicit specialization, not a verbatim theorem statement from the survey.

Separate statistical target T_GOE: for periodic cubes of volume n, at a bulk energy E with a positive and well-defined density of states rho_g(E), the unfolded point process sum_j delta_{n rho_g(E)(E_{j,n}-E)} should converge in distribution to the GOE bulk point process as n tends to infinity, at fixed g. Energy averaging, boundary conventions, and the regularity/positivity of rho_g(E) must be specified before a proof claim. This lane does not claim this limit.

Current-status warning: a public OpenAI Math preprint dated September 23, 2026 claims pure absolute continuity for this uniform-law model in dimensions d>=3 on a fixed interval. It states no GOE-statistics theorem in its introduction. Its correctness and relevance to owner solved/retired status are not independently certified here. Current openness: UNKNOWN. No novelty or solved claim.

Request to w484: attack the target and its quantifiers independently first; the independent route is not included in this statement. Any later review of auxiliary lemmas must keep T_AC and T_GOE distinct.
