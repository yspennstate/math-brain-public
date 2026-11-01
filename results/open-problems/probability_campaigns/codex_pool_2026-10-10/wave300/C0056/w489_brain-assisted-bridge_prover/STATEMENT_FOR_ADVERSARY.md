# C0056 statement-first handoff (2026-10-10)

Native worker: w489. Adversary: w490. Referee: w491.

Recovered intake record: C0056, problems.jsonl line 56, source_id bourgade_band_icm_2018, locator Section 2.1, p. 7. It requests BOTH absolutely continuous spectrum at small disorder on Z^3 and GOE local statistics for finite-volume restrictions. The title alone omits the second requirement. Primary-source verification is pending; do not call the combined target solved.

Precise scoped spectral target: on l2(Z^3), H_lambda,omega=-A+lambda V_omega, where A sums the six nearest neighbours, V_x are iid Uniform[-1,1], and lambda>0 is fixed. Seek lambda_0>0 and a deterministic nonempty bounded open energy interval I such that for every fixed 0<lambda<lambda_0, almost surely chi_I(H)l2(Z^3) is contained in the absolutely continuous spectral subspace and chi_I(H) is nonzero. Probability-one events may depend on lambda. This is the uniform-law spectral specialisation; it does not specify or settle GOE statistics.

Primary literature found: the September 23, 2026 OpenAI preprint claims this spectral conclusion for uniform potentials, including d=3; its proof is not independently verified here. An October 8, 2026 Jaksic--Last primary paper refers to its boundary-to-purity step. Current openness: UNKNOWN; no novelty claim.

Disjoint proposed lane: cavity escape-width moment -> almost-sure spectral absolute continuity. For H^x the compression deleting x and b_x the vector of its six hopping coefficients, define Gamma_x(E,eta)=eta+Im<b_x,(H^x-E-i eta)^(-1)b_x>. Proposed sufficient hypothesis, for some 0<q<1, is sup_{0<eta<1} E integral_I Gamma_x(E,eta)^(-q)dE<infinity for each x at fixed lambda. Please independently test whether this suffices for absolute continuity, and identify any missing quantifier, conditioning or spectral-subspace step. This handoff contains no proof. I will send the proof packet later.

Single hardest gap in this lane: establish this negative moment bound for the actual cyclic lattice at fixed lambda as eta tends to zero. Finite-height and tree estimates cannot simply be substituted.
