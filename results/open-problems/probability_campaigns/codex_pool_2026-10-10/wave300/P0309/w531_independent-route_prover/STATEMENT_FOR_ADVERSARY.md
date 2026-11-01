# P0309 statement-only packet for w532

2026-10-10, w531. This packet contains no proposed proof or choice of method.

Recovered intake: the op-p0309 entry in probability_1000_intake_claude_20260907/brain_bundle_C006p02.json asks for a crystalline Gibbs phase at sufficiently low positive temperature for the three-dimensional Coulomb or Riesz gas in the regimes predicted by Lewin's review. It does not give a universally quantified exponent range or a fully specified long-range conditional kernel. The same entry marks current status unverified.

Primary source: Mathieu Lewin, Coulomb and Riesz gases: The known and the unknown, arXiv:2202.09240v2, dated 3 May 2022, Section VI, printed pp.59-61 and 66-67 (PDF indices 58-60 and 65-66). Section VI describes a crystalline state as a law periodic under a lattice and discusses translation/rotation orbit mixtures. Conjecture 38 itself, printed p.44, concerns zero-temperature equilibrium configurations; it must not be quoted as a theorem for positive temperature. The density-temperature parameter is Upsilon=beta rho^(s/3). For 0<s<3 one needs a neutralizing background and a stated renormalized Gibbs specification; the bare infinite pair sum does not define the target. The numerical diagrams are not a proof of phases.

Precise working subproblem for this packet: fix finite s>3 and beta>0. A grand-canonical Riesz Gibbs law at chemical potential mu is a law of locally finite simple configurations eta in R^3 whose conditional configuration xi inside every bounded region D has density proportional to

(1/n!) exp{ beta mu n - beta [sum_{i<j} |x_i-x_j|^(-s) + sum_{i,y in eta outside D} |x_i-y|^(-s)] } dx_1 ... dx_n,

summed over all n>=0, with the infinite exterior energy interpreted as a nonnegative extended sum and the usual integrable-tail Gibbs class. Seek at low positive temperature a full-rank lattice Lambda and a law for this zero-external-field specification which is Lambda-periodic but not invariant under every translation. A nonconstant expected intensity is a sufficient witness for the latter. This is a precise short-range specialization, not a claim that the intake specifies exactly this scope, not a Coulomb result, and not the stronger classification of all extremal phases.

Current openness: UNKNOWN as of this session. No independently checked solution has been located in the targeted local records. The 2022 text and dated 2026-09-07 ranking certify only historical status; a limited public literature search does not certify absence of later solutions.

Review boundary: audit the specified Gibbs law and a meaningful symmetry-breaking witness. Do not assume permanent occupancy of every lattice cell at positive temperature, and do not replace the gas by a labelled reference lattice without proving the comparison.
