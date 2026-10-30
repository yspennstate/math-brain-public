# exact target, quantifiers, hypotheses and units

A079 / B16 / G-PHASE-COND. For every uniform physical product cube X x Y with Boolean F(x,y)=g_x(y) and bent branches, retain H(S_Y|S_X), the selector conditional entropy B_X=H(S_X|S_Y), and the physical phase energy I_X. Entropy is in bits; Fourier coefficients are normalized; no unbounded H/I Boolean family or universal FEI proof is claimed.

This stage completes the requested correlated-auxiliary diagnostic artifact: explicit actual Boolean realizations, exact joint/conditional spectra, phase-energy ledger, distinct-branch arbitrary-seed guard, and finite signed checks. The universal payment remains OPEN. B16 already had at least two source-complete pending results at the initial board snapshot. This run verifies narrow G-PHASE-COND hypotheses and records the OPEN completion; it does not open another broad completed universal-payment candidate.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision fei-execution-protocol/2, 2026-10-11-execution-v2. Navigation files README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS and the campaign plan were consulted, especially the plan's A079 acceptance contract and shared-data composition section. Initial BOARD.md snapshot: 2026-10-11 22:47 UTC. B16 STREAM_NOTES.md v1, 2026-10-11 22:45Z: A079 direction G-PHASE-COND, distinct bent address branches, conditional remainder and tensor guard. No disagreement with the lead.

The supplementary CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were consulted, including C006/C019 and arbitrary-selector/tensor guards. Curated source inventory was read; relevant source sections inspected: BLOCK_RESTRICTION_IDENTITY sections 1-3, ISOSPECTRAL_SPLICING sections 2-5, ROUTE_MAP product-phase guard, and LOG_ALLOCATION tree context. Earlier B05, B09 and B19 report openings/results/limits were inspected to preserve the local-refund obstruction and avoid presenting this stage as a repeat of it.

Paper context inspected: threshold_paper_38pp.txt Proposition 8.6, equations (75)-(79), Corollaries 8.7-8.8, and Fourier preliminaries/introduction; earlier 29-page version introduction/preliminaries. Percolation 30-page and alternative 31-page text introductions, Theorem 1.1 and conditional spatial-entropy discussion were inspected as scope context only. No percolation geometry or threshold theorem is a premise in the new derivation. The paper text files are cp1252, not UTF-8; the initial UTF-8 reading error was corrected. SHA256 receipts for all consulted files appear in out/SOURCE_MANIFEST.json. These are byte pins, not assertions of full independent source audits.

# complete derivation or exact first unsupported line

The complete self-contained proof is in CONDITIONAL_ENERGY_LEDGER.md sections 1-5; CORRELATED_AUXILIARY_CONSTRUCTION.tex is a concise mathematical companion. Its key formulas are:

For any bent branch on d data bits, sigma_t(x)=2^(d/2) ghat_x(t) is Boolean and P(S_X=v,S_Y=t)=2^(-d) sigmahat_t(v)^2. Hence H(F)=d+E_t H(sigma_t), I_Y=d/2, I_X=E_t I(sigma_t), B_X=E_t H(sigma_t), and H(S_Y|S_X)=d-I(S_X;S_Y)<=2I_Y. Magnitude energy is zero; signed phase energy is exactly I_X.

A fully realizable arbitrary-row family is F(x,a,b)=(-1)^(a dot b)h_b(x) on k+2m bits. Its signed coefficient is 2^(-m)(-1)^(s dot t)hhat_s(v). Thus H(F)=2m+E_s H(h_s), I_Y=m, I_X=E_s I(h_s), and H(S_Y|S_X)=2m-I(V;S). This retains the entire conditional auxiliary remainder.

The linear control h_b(x)=(-1)^(x dot b_[k]) has H=2m, I_X=k/2, I_Y=m, H(S_Y|S_X)=2m-k, and distinct branches with dependent spectral marginals. At k=1 the conditional auxiliary entropy divided by phase energy diverges as 4m-2, although H/I<2. Therefore a selector-phase-only bound on the auxiliary remainder fails.

For an arbitrary k-bit seed g and m>=k+1, add a separate rare B-point tag to each selector assignment: h_b(x)=g(x)(-1)^(1{b=tag(x)}). Every branch is bent, distinct even modulo sign, and the spectral marginals are dependent. With delta=2^(k-m), epsilon=2^(2-m), the exact ledger is B_X=(1-delta)H(g)+2^(-m)sum_u H(g^(u)), p_X=(1-epsilon)p_g+epsilon Uniform, I_X=I(g)+2^(1-m)(k-2I(g)). Entropy continuity has the explicit analytic error bounds |B_X-H(g)|<=delta k and 0<I(V;S)<=h2(epsilon)+(epsilon+delta)k. Thus B_X/I_X tends to H(g)/I(g) for every fixed nonconstant seed.

Consequently a uniform B_X<=K I_X on this distinct, correlated family implies FEI(K) for arbitrary seeds; conversely FEI(K) applied to each Boolean phase row supplies that bound. The phase completion remains full-FEI difficulty. The full tagged family itself has H/I<3 because m>=k+1: this is a conditional-payment scope guard, not a disproof.

First unsupported line: assert that an absolute finite K bounds E_s H(h_s) by K E_s I(h_s) using only Booleanity, flat data magnitudes, branch distinctness and spectral dependence. Arbitrary seed entropy survives all four hypotheses.

# executed validation with domain, arithmetic, commands and outputs

Frozen before search: out/FROZEN_SPEC.json, helper A079-phase-v1. Command from A079 workspace: python -X utf8 runs\20261011T224806Z-fleet05-A079-correlated-auxiliaries\code\check_phase.py.

Executed 350 actual Boolean truth tables: 272 exhaustive arbitrary phase tables for (k,m)=(1,1),(2,1); 16 deterministic (2,2) tables; 56 rare-tag cases using every k<=2 seed and eight fixed k=3 seeds, m=k+1,k+2; six linear controls for k=1..3, m=k,k+1. No symmetry quotient or dimension escalation. Largest truth table: 8192 signs. Memory estimate under 40 MB, no >300 MB job or GPU.

Result: PASS, 115026 exact assertions, checker runtime 1.8872228000545874 seconds. Integer Walsh coefficients were compared with the closed signed formulas. Fraction probability vectors verify normalization, data flatness, marginal depolarization, both influence blocks and branch bentness. Prime-log entropy expressions verify the joint/conditional ledger as exact symbolic equalities, without floating logs. A physical-edge computation independently checks selector influence in the rare-tag cases. Outputs: out/validation.json. This is an alternate representation self-check, not independent reviewer acceptance. Analytic arguments supply the all-dimensional identities, strict dependence and limiting guards.

# proof dependencies and changed downstream conclusions

The new derivation uses only normalized Walsh expansion, character orthogonality, Parseval, finite entropy chain rules/concavity, and the Bernoulli mixture-label entropy bound. C006/threshold Proposition 8.6 serve as independently re-derived interface checks, not unpaid theorem premises. No new B16 unreviewed theorem is assumed.

Downstream A034 must distinguish the paid data-side conditional entropy from unpaid selector phase entropy; requiring distinct branches or dependent spectral marginals does not remove arbitrary seed FEI. A080 must not call the divergent conditional/phase ratio a disproof: actual H/I is <2 for the linear control and <3 for the tagged family. C019 applications must retain the phase-row terminal entropy rather than spending zero magnitude energy against it.

# one next mathematical action and independent reviewer

Consume A034's next source-complete structural phase hypothesis and test its heredity and exclusions against the rare-tag marginal p_X=(1-epsilon)p_g+epsilon Uniform before attempting a phase-row stopping payment. This directly tests whether the hypothesis removes the arbitrary seed, rather than accumulating more flat-spectrum class controls. Independent reviewers requested by packet: A092 and A088. They should reconstruct the signed partial transform, the sum-of-point-flips depolarization, and the finite-to-limit seed guard. No independent acceptance has occurred.

# actual persistence receipts or precise save blocker

All writes are confined to A079. The run contains REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, mathematical companion files, checker, frozen specification, validation output and source hashes. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/PERSISTENCE_RECEIPT.json records each saved artifact's byte count and SHA256. No shared index, other agent folder or brain was modified. Local durable save is complete; supervisor mirror, GitHub copy, independent review and downstream mathematical adoption are unverified.

**Universal bridge:** This stage moves the lead-named G-PHASE-COND interface by giving an exact conditional auxiliary payment H(S_Y|S_X)<=2I_Y on bent branches while proving that their remaining selector conditional payment retains arbitrary FEI, even with distinct branches and dependent spectral marginals. It does not reduce the universal constant or solve C019. What remains is a restriction-stable phase-family hypothesis with a genuinely paid residual and terminal entropy. Testing A034's next proposed hypothesis against the explicit rare-tag limit is the shortest next route toward full FEI: it detects circular structural assumptions before any new isolated-class calculation.
