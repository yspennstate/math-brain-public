# A061: fair adaptive restriction entropy process

## exact target, quantifiers, hypotheses and units

For every n>=0 and Boolean sign f on the uniform cube, construct its entropy process along any finite fair adaptive physical restriction tree. Entropy uses bits, I is ordinary total influence. Prove exact conditional increments and the stopped tree identity, retaining terminal entropy. Identify the sign and a proved sufficient hypothesis for a compensated supermartingale. Full FEI remains OPEN. This is an A061 baseline/interface completion, not a claim of novelty or a universal payment theorem.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full (revision 2026-10-11-execution-v2), README.md, CURRENT_STATUS.md, CLAIM_REGISTRY.json, OBSTRUCTION_REGISTRY.json, PACKET_STATUS.json, STREAM_NEXT_ACTIONS.json, and the campaign plan's B13/A061--A065 and acceptance-contract passages. The board snapshot is 2026-10-11 21:45 UTC; it lists A061--A065 at stage zero. claude/B13/STREAM_NOTES.md was absent at initial read; no direction is inferred from that absence.

Read supplemental CAMPAIGN.md, CLAIMS.md, COUNTEREXAMPLES.md, SEED_LEMMAS.md, NATIVE_MAPPING.md. Mathematical sources used: sources/ERASURE_REDUCTION.md sections 1--2 (exact erasure/JS identity and scalar bound), BLOCK_RESTRICTION_IDENTITY_2026-09-18.md sections 1--3 (channel and influence normalization), and LOG_ALLOCATION_CURATED.md sections 2--5 (rare logarithm and tree transport). Also inspected ISOSPECTRAL_SPLICING_CURATED.md and prior B05/B09/B19 run reports. The B05 original source is run 20261011T193057Z-fleet01-B05-rare-restrictions, sections 2--7, pinned in registry to commit 80cc2e5027efa56d79c4ecdf7d4949759ef2068b. The current paper context and earlier versions were accessed for introductory scope and restriction/composition passages; no threshold or percolation theorem is a premise in the proof below. Relevant paper names are threshold_paper_38pp.txt, threshold_paper_29pp_earlier_version.txt, percolation_spectral_pivotal_entropy_30pp.txt, percolation_spectral_pivotal_entropy_31pp_other_version.txt. Context source hashes and precise inspection record are in out/SOURCE_RECEIPTS.json when the metadata job completes.

## complete derivation or exact first unsupported line

### 1. Probability space and filtration

Sample X uniformly from {-1,1}^n. For randomized policies, also sample an independent policy seed R at time zero. Let F_t contain R, all coordinates queried before t and their physical values. The next coordinate i_t and the decision to stop must be F_t-measurable. Never query a coordinate twice. Conditional on F_t and continuation, X_i_t is a fair sign, and the remaining unqueried coordinates are uniform and independent. This follows inductively because a policy uses only revealed values and its independent seed. Let g_t be the actual Boolean function obtained by restricting f to the observed assignment. Let tau<=n be the stopping time. Freeze g_t and all processes after tau; all increments and charges below are zero there.

Write E_t=H(g_t), V_t=I(g_t), d_t=Inf_i_t(g_t). At a live node suppress t. Let a_T=ghat(T) and b_T=ghat(T union {i}) for T not containing i. Set q_T=a_T^2+b_T^2, theta_T=b_T^2/q_T on q_T>0. The child Fourier coefficients are a_T+sigma b_T, sigma in {+1,-1}. Let p_sigma(T)=(a_T+sigma b_T)^2. Boolean Parseval makes each p_sigma a probability law; their fair average is q. Thus d=sum b_T^2=sum q_T theta_T.

The spectral probabilities q_T and theta_T are not physical branch probabilities. At this one node one may introduce a fresh auxiliary experiment: sample sigma fairly, then Y with law p_sigma. It has marginal q, and J=I(sigma;Y)=H(q)-[H(p_+)+H(p_-)]/2. No global spectral subset is assumed to undergo the physical restriction.

### 2. Exact one-step increments

Let B=sum_T q_T h_2(theta_T), J as above, D=B+J. Splitting the parent spectral law into the removed bit and T gives H(g)=H(q)+B. Therefore

    D = H(g) - (H(g_+)+H(g_-))/2 >= 0.

Let eta_H=(H(g_+)-H(g_-))/2 and eta_I=(I(g_+)-I(g_-))/2. The exact realized increments, with sigma=X_i, are

    E_{t+1}-E_t = -D_t + sigma eta_H,t,
    V_{t+1}-V_t = -d_t + sigma eta_I,t.

For the influence identity, the average squared child coefficient at T is q_T, so average child influence is sum |T|q_T. Parent influence is that sum plus sum b_T^2. Fairness kills the sigma terms conditionally. In particular E_t and V_t are supermartingales; neither need decrease on every physical branch.

Define A_t=sum_{s<t}D_s and P_t=sum_{s<t}d_s (stopped charges). Then E_t+A_t and V_t+P_t are martingales. Their initial values are H(f) and I(f). They are integrable: 0<=E_t<=n, 0<=V_t<=n, 0<=D_t<=n, 0<=d_t<=1, and tau<=n. Summing finitely many conditional expectations gives

    H(f)=E H(g_tau)+E sum_{t<tau}D_t,
    I(f)=E I(g_tau)+E sum_{t<tau}d_t.

For a deterministic tree with node reach probability pi_v=2^{-depth(v)}, these are exactly H(f)=sum_internal pi_v D_v+sum_leaf pi_l H(g_l) and I(f)=sum_internal pi_v d_v+sum_leaf pi_l I(g_l). A randomized policy averages these identities over its seed. Terminal entropy cannot be dropped unless the leaves have zero entropy or it has a separate bound. Constant leaves have H=I=0; a terminal character can have H=0 and I>0.

### 3. A proved logarithmic compensation

Define the nonnegative predictable one-sided log charge

    lambda_t=sum_{T:b_T^2>0} b_T^2 log_2(q_T/b_T^2).

For theta in [0,1], -(1-theta)ln(1-theta)<=theta, since the derivative of theta+(1-theta)ln(1-theta) is -ln(1-theta)>=0. Consequently B_t<=lambda_t+d_t/ln 2.

Here is a self-contained channel bound. Put z=|2ab|/q in [0,1] for a positive packet. Its JS contribution is q d_nat(z)/ln 2, where d_nat(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2. The inequality d_nat(z)<=1-sqrt(1-z^2) holds: the derivatives are atanh(z) and z/sqrt(1-z^2), and the latter minus the former has derivative (1-z^2)^(-3/2)-(1-z^2)^(-1)>=0 and starts at zero. Integrate twice and extend to z=1 by continuity. Therefore the packet contribution is at most (q-|a^2-b^2|)/ln 2=2min(a^2,b^2)/ln 2. Summation gives J_t<=2d_t/ln 2. Combining,

    0<=D_t<=lambda_t+(3/ln 2)d_t.                 (* proved *)

Thus the explicit compensated quantity

    U_t=(3/ln 2)V_t-E_t-sum_{s<t}lambda_s

is ALWAYS a supermartingale on the stated finite trees: its conditional drift is D_t-(3/ln 2)d_t-lambda_t<=0. It is integrable: every nonzero Fourier coefficient of an actual restriction in at most n coordinates has magnitude at least 2^{-n}, q_T<=1, so every positive theta_T>=2^{-2n} and lambda_t<=2n d_t. The log cost is paid once, through its predictable cumulative sum. At stopping this yields only

    H(f)<= (3/ln 2)I(f) + E sum lambda_t
           + E[H(g_tau)-(3/ln 2)I(g_tau)].

The cumulative log term remains unpaid universally. Its presence is not an FEI proof.

### 4. Hypothesis with a proved finite influence price

Fix epsilon in (0,1]. Suppose at EVERY live node, every T with b_T^2>0 satisfies theta_T>=epsilon. Zero mismatch packets are exempt. Then lambda_t<=log_2(1/epsilon)d_t. This is a directly checkable spectral density hypothesis, not an assumption that the desired entropy drift is already bounded.

With C_epsilon=log_2(1/epsilon)+3/ln 2, the quantity

    Z_t=C_epsilon I(g_t)-H(g_t)

is a supermartingale: E[Z_{t+1}-Z_t|F_t]=D_t-C_epsilon d_t<=0. Equivalently H(g_t)-C_epsilon I(g_t) is a submartingale. Z_0=C_epsilon I(f)-H(f); at constant leaves Z_tau=0. For arbitrary stopping leaves,

    H(f)<=C_epsilon I(f)+E[H(g_tau)-C_epsilon I(g_tau)].

If terminal functions satisfy H<=C_epsilon I, this proves H(f)<=C_epsilon I(f). The conclusion holds in every dimension for any policy/tree satisfying this same fixed epsilon. No assertion is made that every Boolean function admits such a tree. Parities (queried theta=1) show the hypothesis is nonempty in unbounded dimension. As another simple sufficient condition, if every positive d_t>=delta, then B_t<=h_2(d_t)<=d_t[log_2(1/delta)+1/ln 2], and the same conclusion holds with C_delta=log_2(1/delta)+3/ln 2. These are conditional class statements, not new universal FEI results.

For a general F_t-measurable state potential Q_t, C V_t+Q_t-E_t is a supermartingale exactly when D_t<=C d_t+Q_t-E[Q_{t+1}|F_t]. This specifies the sign of the nonlocal debt needed by A064; it does not construct a universally paid Q.

### 5. Obstruction and first unsupported universal line

B05 gives actual Boolean splits with D>=B and B/d >= (1-2^{-k})(k-2) for every even k>=4. Hence no fixed finite C makes CI(g_t)-H(g_t) a supermartingale for ALL fair policies: start by querying that selector. This consumes the source-bound B05 control, rather than rerunning it or misreading it as failure of existential coordinate selection. The first unsupported universal step is: find an adaptive tree paying E sum lambda_t plus its terminal deficit by a dimension-independent multiple of I(f), or find a nonlocal Q whose boundary and conditional drift achieve that payment. The exact telescope alone does not supply it.

## executed validation with domain, arithmetic, commands and outputs

The frozen specification was written before execution in FROZEN_SPEC.json. Command: `python -X utf8 runs\20261011T214516Z-fleet05-A061-entropy-process\code\check_process.py`, from A061. The finite domain comprises all 278 Boolean functions in n=0,1,2,3, every coordinate split, and two deterministic adaptive trees per function (full constant termination and early stop at at most two residual coordinates). The adaptive rule chooses the smallest positive influence, breaking ties by coordinate index. There is no symmetry reduction or randomness. The initial one-bit stopping check had only zero terminal entropy; the frozen specification was corrected before rerunning to include nonzero terminal entropy.

Integer Walsh sums and Fraction arithmetic check exact child coefficients, marginal normalization, selector disagreement and influence decomposition. Entropies are stored as rational coefficient vectors of log_2 primes; factorization of rational probabilities makes the B+J node identity and stopped tree telescopes exact symbolic identities, including nonzero terminal terms. No floating logarithm is used. out/CHECK_RESULTS.json records 24,732 exact assertions passed, 556 adaptive trees, 2,212 split checks including tree rechecks, and 0.823 seconds of checker runtime. This is a finite implementation check of all-dimensional proofs on the page, not a finite-to-infinite bridge or a sign certificate for an unproved inequality.

## proof dependencies and changed downstream conclusions

The process/interface claim is reconstructed directly above using finite probability and Fourier Parseval. Existing source identities are baseline, not credited as a new result. The obstruction's only campaign dependency is B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO v1; it is not needed for the positive derivations. No B09 biased uncertainty statement or unreviewed theorem is used. A062/A063 can reuse this exact filtration and distinguish physical from spectral probabilities. A064 receives the exact drift sign, the unconditional log-cost supermartingale, and the still-unpaid cumulative lambda. A028 receives the retained terminal entropy formula. Independent acceptance remains pending.

## one next mathematical action and independent reviewer

Next action: A064 should construct a state debt Q for the B05 selector-first tree satisfying D<=Cd+Q-EQ_child and verify the boundary charge on the actual control/data descendants, without repeated influence spending. Independent reviewers: A087 and A094; they should reconstruct the scalar JS bound, signs, adaptive fair conditioning, and early-stop terminal term.

## actual persistence receipts or precise save blocker

Artifacts are saved only inside the supplied A061 run directory. REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, FAIR_TREE_ENTROPY_PROCESS.tex, PROCESS_INTERFACE.json, FROZEN_SPEC.json, code/check_process.py and out/CHECK_RESULTS.json form the local handoff. out/PERSISTENCE_RECEIPTS.json records file sizes and SHA256 after completion. Rolling STATUS.md, WORKLOG.md, LEARNED.md are updated locally. Shared ledgers, other agents' folders, git, Brain writes, and uploads were not used. Supervisor copy, mirror verification and independent review are NOT claimed.
