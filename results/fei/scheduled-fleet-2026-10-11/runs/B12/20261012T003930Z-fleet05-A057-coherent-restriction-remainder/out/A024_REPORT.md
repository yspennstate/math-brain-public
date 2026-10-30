# A024: biased-child stability and the exact signed normalization credit

## exact target, quantifiers, hypotheses and units

For every finite Boolean outer gate g, Boolean children f_i on mutually disjoint independent uniform physical blocks, and any fair physical singleton restriction x inside block j, derive the exact changed-mean entropy/deficit transfer, including deterministic descendants. Entropy is in bits. Physical influence is uniform flip influence; the outer spectral influence is computed in its actual induced product basis. The deliverables are BIAS_TRANSPORT.tex and BOUNDARY_CREDITS.md. The packet interface is complete locally; independent review and universal tree payment remain open. Full FEI is OPEN.

This is a source-bound application/verification of the accepted A056 composition baseline and repair of A057's explicitly pending biased empty-sector identity, not another broad candidate opened despite B05's review queue. The additional result is the signed restriction cocycle and its exact normalization credit.

## sources actually read, revisions and theorem locators

The execution protocol was read in full: fei-execution-protocol/2, revision 2026-10-11-execution-v2. Canonical README, CURRENT_STATUS, claim/obstruction/packet registries, STREAM_NEXT_ACTIONS, AGENT_ASSIGNMENTS and the campaign plan were read for scope, A024 acceptance criteria and review constraints. The supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and twelve source notes were ingested; mathematical examination focused on relevant restriction/composition interfaces rather than auditing every included result. Earlier B05/B09/B19 run reports were read for the local-refund no-go, biased uncertainty scope and independent review. Fifty-one original file receipts, with exact byte hashes and encodings, are in out/SOURCE_RECEIPTS.json; excerpts are in out/SOURCE_EXCERPTS.txt.

Critical sources: threshold_paper_38pp.txt Section 6.1, corrected-entropy definition; Section 7, Proposition 7.1, equations (67)-(70), exact composition and deficit identities. Its older 29-page version has different constants. Both percolation text versions' introductions and Section 1.1 distinguish biased spectral influence from unweighted pivotal influence; no geometric percolation theorem is a premise. The legacy text files are cp1252, not UTF-8.

ISOSPECTRAL_SPLICING_CURATED.md Section 3, especially Corollary 3.4 equation (3.8), supplies the existing magnitude-mismatch/KL rebate; original source pin fe94de760ee2b47545419a7447b492816bd16045, blob 3421c0cbfd22031554befb962ec92cd0c8bb45b9. A056-DISJOINT-COMPOSITION@1 and A056-PHYSICAL-RESTRICTION-SCOPE@1 have an observed source-bound independent acceptance in A091's run. A042-BIAS-ENDPOINT-INTERFACE@1 and A057-NONREUSING-ALPHA-LOG-PAYMENT@1 were read and their particular polynomial/bank steps reconstructed here; their broader pending claims are not silently accepted. A057's NEXT_HANDOFF.md explicitly left the biased empty-sector subtraction unverified; equation (4) below resolves that interface.

BOARD.md was read at intake (22:37 UTC snapshot). B05 STREAM_NOTES.md was absent initially and appeared during work; its v1 was then read. The lead requests the packet as written and identification of log(1/mean) and bad-node scope. This report follows that direction. The lead's in-progress odd-face theorem is not assumed.

## complete derivation or exact first unsupported line

The full proof is in BIAS_TRANSPORT.tex; BOUNDARY_CREDITS.md gives analytic endpoint expansions and their uniformity limits. Let Eplus denote the corrected entropy, D=I-Var, e(u)=u log2(1/u), m_i=E f_i, v_i=1-m_i^2, and mu the actual product law of child outputs. The composing definition is

    Eplus_mu(g)=sum_{S nonempty} P_mu(S) log2(product_{i in S} v_i/P_mu(S)).

There is no output-variance numerator. For physical uniform f, H(f)=Eplus(f)+e((E f)^2). Conditional nonempty entropy differs by the exact v log2(1/v) normalization term.

Set a_i=E_{mu_-i}(D_i g)^2, a bounded pivotal probability. For v_i>0 it equals Inf_i^mu(g)/v_i; at v_i=0 use contraction, and the polynomial a_i only as an extension for zero-weight inner contributions. The known unique-disjoint-union Fourier identity gives

    Eplus(F)=Eplus_mu(g)+sum_i a_i Eplus(f_i),
    I(F)=sum_i a_i I(f_i),
    D(F)=D_mu(g)+sum_i a_i D(f_i).                         (1)

After querying x inside j let delta Z=Z-(Z+ + Z-)/2, beta=(m_j+ - m_j-)/2, d=Inf_x(f_j), t=a_j, b=E D_j g, M=E F. The remaining physical inputs stay uniform. Only the output law changes. For i!=j, a_i is affine in m_j, hence its child average equals its original value; t is independent of m_j. Consequently

    delta Eplus(F)=delta Eplus_mu(g)+t delta Eplus(f_j),
    delta I(F)=t d,
    delta D_mu(g)=beta^2(t-b^2),
    delta D(F)=t d-b^2 beta^2.                            (2)

The variance calculation uses delta Var(f_j)=beta^2 and delta Var(F)=b^2 beta^2. Define

    T=delta Eplus_mu(g)+delta e(M^2)-t delta e(m_j^2).

Then the exact full-FEI surplus transfer is

    delta H(F)=t delta H(f_j)+T,
    delta(C I-H)(F)=t delta(C I-H)(f_j)-T.                (3)

The C(D)-Eplus slack has its own cocycle; the empty-atom reserve C Var-e(mean^2) converts it to full-FEI slack. C beta^2(t-b^2) is not free additional influence: it cancels in that conversion.

For the directly physical representation F=A(z)+B(z)f_j(u), Booleanity gives AB=0 and A^2+B^2=1 pointwise, with t=E B^2. Define L(a,c)=e(a^2)+e(c^2)-e(a^2+c^2). The exact erasure transfer is

    B_x(F)=t B_x(f_j)+R,
    R=sum_Z L(Ahat_Z+m_j Bhat_Z,beta Bhat_Z)-t L(m_j,beta). (4)

Each nonempty residual inner set contributes by homogeneity exactly t times its inner erasure cost. Only the inner empty residual set changes: its amplitude becomes Ahat+m_j Bhat. Removing its old contribution proves the negative subtraction in (4). This fills A057's stated descendant gap for arbitrary means and deterministic endpoints. With the actual physical JS terms,

    T=R+JS_x(F)-t JS_x(f_j).                              (5)

For t>0, beta!=0, scalar binary entropy and log-sum also give

    R <= t beta^2 log2([1-t+(m_j^2+beta^2)t]/[t beta^2])
         +t beta^2 log2(e)-t L(m_j,beta).                 (6)

Here sum_Z(Ahat+m_j Bhat)^2=1-t+m_j^2 t. The displayed bound leaves outer rarity t visible; it does not assert R<=K t d.

Retain the existing mismatch rebate using actual inner children: q_U=(fhat_j+(U)^2+fhat_j-(U)^2)/2, r_U=(|fhat_j+(U)|-|fhat_j-(U)|)^2/4, eta=sum r_U, nu=r/eta. For eta>0,

    delta H(F) <= t eta[log2(1/eta)-KL_2(nu||q)+3/ln2]+T. (7)

At eta=0 the inner decrement vanishes exactly; T need not vanish. Dropping KL or replacing the actual composed children by inner children would be invalid.

At beta=0, all output laws are unchanged and T=R=0: the entire decrement transports by t. For a signed dictator outer gate T=0 at every endpoint. Contract deterministic outputs before forming a normalized basis or dividing by a deficit. Corrected entropy cancels the outer v_j log(1/v_j) term exactly. For a fixed finite gate and fixed other biases, its corrected endpoint drift is O(v_j), with possible second-order v_j^2 log(1/v_j) terms from newly zero normalized coefficients; this is not an arity-uniform remainder.

The log(1/mean) requested by the lead appears in the scalar subtraction. At fixed nonzero m and beta->0, if Z(m)=sum_{Ahat+m Bhat=0} Bhat^2 then R=-Z(m) beta^2 log(1/beta^2)+O(beta^2); its leading rare-beta logarithm is nonpositive. At m=0, R=kappa beta^2 log(1/beta^2)+O(beta^2), kappa=sum_{Ahat!=0} Bhat^2<=t. In the iterated regime beta=o(|m|), m->0, the beta^2 coefficient has kappa log(1/m^2)+O(1). The exact subtraction resolves this nonuniform crossover. This logarithmic component is bounded by [2/(e ln2)]t d, since |beta|<=d and u log(1/u)<=1/e. It is A057's affordable bank, not the whole erasure payment or a claim that all nodes are good. Bad-node status requires the full comparison B_x(F)>K t d.

A near-dictator calibration demonstrates the missing credit: f_j=x(1-2 1_{z=0}) with r control bits and a two-input AND outer with another fair literal. At query x, eta_inner=0 and delta H(f_j)=0; t=1/2 and delta I(F)=1/2, but delta H(F)=T tends to 2 bits (R tends to 1 and JS_F to 1). Explicit point-defect spectral masses give the vanishing entropy remainder O(r 2^-r). This is a constant-price calibration, not an unbounded bad-node family.

**First unsupported universal line:** a stopping-tree bound on the entire signed outer residual sum plus the weighted inner KL-log charges and terminal entropy by an absolute multiple of root physical influence. Neither (6), small inner mismatch, nor bounded a_i establishes it. Outer-rarity logs cannot be charged repeatedly against ancestral influence. No universal theorem or FEI counterfamily is obtained.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before the pilot; FROZEN_SPEC_V2.json before adding the signed erasure and JS-transfer identities to the full validation. There is no symmetry reduction, dimension escalation, randomness, GPU, heavy job, or >300 MB job. Estimated memory is 60 MB; actual peak RAM was not measured.

Commands from the assigned folder:

    python -X utf8 runs/20261011T223622Z-fleet05-A024-biased-child-stability/code/intake.py
    python -X utf8 runs/20261011T223622Z-fleet05-A024-biased-child-stability/code/check.py --pilot
    python -X utf8 runs/20261011T223622Z-fleet05-A024-biased-child-stability/code/check.py

Pilot: 256 compositions, 512 physical splits, 6,004 exact assertions, 0.119405 seconds. Full: all 4,096 outer/inner1/inner2 two-bit truth-table combinations, 8,192 physical singleton splits, seven near-dictator point-defect cases r=2..8. Result PASS, **110,789 exact assertions**, 5.469279 seconds. Final output out/VALIDATION.json; pilot output out/PILOT.json.

Direct physical integer Walsh spectra are compared with independently computed polynomial biased outer squared spectra. All arithmetic is Fraction; entropy identities are exact rational coefficient equalities on prime logarithms, including the empty atom and signed subtraction. Constants/asymptotic bounds rely on the complete analytic proofs, not numerical logarithms. The finite domain is validation of these identities; the all-dimensional proof is the disjoint coefficient argument. No separate human or agent review has yet accepted this run.

## proof dependencies and changed downstream conclusions

The accepted A056 baseline is consumed and reconstructed. The existing source mismatch/KL Corollary 3.4 is used at its exact physical-child scope. A042 endpoint normalization and A057 alpha-log bank are acknowledged and their needed elementary steps reproduced; their unreviewed broader statements are not premises. B05's local variance-refund no-go remains unchanged. B09's generic non-tensor composition assertion and lead's pending odd-face line are not used.

A029/A039/A057 can now substitute equations (2)-(5) rather than freezing original outer biases. A057's NEXT_HANDOFF biased empty-sector identity has a complete proof and exhaustive small check. A041/A042 get the exact empty/output normalization reserve and fixed-slice endpoint scope. This resolves the packet's normalization interface, not the nonlocal universal payment.

## one next mathematical action and independent reviewer

Apply (4)-(5) to the overlapping-control model requested of A023 and separate the affordable beta-log bank from the signed outer-rarity remainder at bad nodes. That is the nearest unpaid transfer term; do not repeat A056 composition calibration. Independent reviewers: A087 primary, A094 alternate; A057 is the downstream consumer of its repaired gap. Review, adoption and downstream use are pending.

## actual persistence receipts or precise save blocker

All four required protocol files, two mathematical deliverables, frozen specifications, checker/intake code and exact output are local inside the assigned A024 run. out/PERSISTENCE_RECEIPT.json contains schema checks, sizes and SHA256 after write/readback, and rolling STATUS.md, WORKLOG.md, LEARNED.md are current. No file exceeds 20 MB. No shared indices, another agent's files, brain, repository or unrelated trees were written. Supervisor copies and mirror verification have not been performed or claimed; no local save blocker occurred.

## Universal bridge

This stage moves C019 stopping-tree payment and C018 erasure transport by completing the biased empty-sector credit and the exact corrected/full-slack cocycle. It removes spurious outer variance logarithms, proves exact zero transfer for stationary means and dictator outer gates, and identifies where a true log(1/mean) crossover lives. The entire signed outer-rarity residual, weighted inner mismatch/KL charge and terminal entropy remain unpaid universally. NEXT isolates that residual on overlapping controls and bad nodes, following B05's live nonreuse mechanism, rather than proving another isolated gate-class FEI theorem.
