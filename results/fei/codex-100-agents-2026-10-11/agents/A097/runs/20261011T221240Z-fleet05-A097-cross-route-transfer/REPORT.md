# A097: complete leaf references transferred into physical stopping trees

## exact target, quantifiers, hypotheses and units

For every finite uniform-cube Boolean sign f and every finite deterministic adaptive physical block restriction tree, construct a complete root spectral subprobability reference from arbitrary complete leaf references. A nonempty block A_h is chosen from unqueried coordinates using only the physical history h. Each assignment y has actual conditional probability alpha_h=2^(-|A_h|); no coordinate is queried twice along a path. Different paths may query different blocks. Terminal functions may have arbitrary bias and nonzero entropy. No disjoint selector/data split, orthogonal children, or global order of physical queries is assumed. Entropies, cross-entropies and divergences are in bits; influence uses the ordinary uniform physical flip convention.

At leaf l, fix a nonnegative law Q_l on all subsets of the remaining coordinates, with total mass at most 1, positive on every positive atom of the actual Fourier law P_l. Write c_l=CE(P_l,Q_l)=sum P_l(S) log2(1/Q_l(S)). The generator/dictionary is fixed before sampling a spectral set. These are complete references, including the empty atom; a nonempty-only reference from C020 must first be completed as described below. Let pi_h be the actual physical reach probability.

The new substitution constructs Q_root and proves exactly

    CE(P_root,Q_root) = sum_h pi_h(B_h+J_h-kappa_h) + sum_l pi_l c_l.   (T)

Here B_h is block conditional spectral entropy, J_h the actual physical-child channel information, and kappa_h a specified nonnegative posterior divergence between actual and lifted-reference physical child laws. Consequently

    CE(P_root,Q_root) <= sum_h pi_h(B_h-kappa_h)
                         +(2/ln 2) sum_h pi_h I_A_h(f_h)
                         +sum_l pi_l c_l.                            (P)

This transfers complete references, not just leaf entropy estimates, from C020 into C019/C024. It removes the need to pay a raw physical leaf-label entropy separately. The cumulative erasure term is still unpaid universally. Full FEI remains OPEN. All-dimensional author proof and exact finite checks are supplied; independent acceptance and literature novelty are not claimed.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2, and campaign README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS and the plan. Relevant plan locators: A097 lines 1126-1130, A028 stopping-tree acceptance, A037 common-law ledger, A039 physical projection and C020 complete-reference costs. The board snapshot at stage start was 2026-10-11 22:05 UTC. The supplied claude/B20/STREAM_NOTES.md was absent; no direction was overridden. Other agents' work was read only.

Read supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING; inventoried sources and read ERASURE_REDUCTION.md sections 1-5 and BLOCK_RESTRICTION_IDENTITY_2026-09-18.md in full. The latter supplies the block information estimate and exact influence convention. Earlier B05, B09 and B19 run reports were read; no unreviewed biased B09 theorem or its overstrong endpoint consequence is a proof premise.

Concrete cross-route inputs reconstructed here:

- A011-BOUNDARY-RETAINING-SELECTOR-TRANSCRIPT v1, run 20261011T213831Z-fleet05-A011-representation-existence: REPORT proof and complete reference pushforward. Its raw code costs 2D+sum pi c_l under separate selector/data hypotheses.
- A037-PHYSICAL-SPECTRAL-COMMON-LIFT v1 and A037-CONDITIONAL-CREDIT-CONSERVATION v1, run 20261011T220010Z-fleet05-A037-conditional-credit-ledger: REPORT sections K and P. These give a function-specific common law but explicitly leave reoptimized witness transfer open.
- A061-FAIR-TREE-PROCESS v1, run 20261011T214516Z-fleet05-A061-entropy-process: REPORT sections 1-3, exact physical reach weighting and retained terminal/influence terms.

All these local claims are author-proved and await independent acceptance. Their algebra needed here is reproved below; no accepted status is inferred. Current threshold_paper_38pp.txt was inspected at Sections 5 (complete witness references), 8.3-8.4 (arbitrary-core and activation barriers), Proposition 8.9/Corollary 8.10. Its 29-page earlier version was inspected for introductory scope. Current percolation_spectral_pivotal_entropy_30pp.txt was inspected at Theorems 3.1-3.2; the 31-page other version at its introduction. A local guard gives a lower entropy bound and cannot pay this upper-entropy residual. No threshold/percolation theorem is used as a premise. These inspections are not a full independent paper audit. Source hashes are in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

### 1. Actual physical fibers and the new reference generator

At a node suppress h. Let R be the remaining coordinates, A the queried block, C=R\A and m=2^|A|. For U subset A and T subset C put a_U,T=fhat_h(U union T), and let b_y,T be the actual Fourier coefficient of child f_hy at T. Walsh Parseval on A gives

    q(T)=sum_U a_U,T^2 = (1/m) sum_y b_y,T^2.

Write P_y(T)=b_y,T^2. Every P_y is normalized since the child is Boolean. At q(T)>0 define

    theta(U|T)=a_U,T^2/q(T),
    k_P(y|T)=P_y(T)/(m q(T)).

Both are probability kernels. This retains all phases through the actual child coefficients; it is not a universal phase-blind map of parent squared masses. The joint true experiment can be generated bottom-up: choose physical child uniformly, recursively sample its spectral witness with residual set T, then sample U with theta(.|T), independently of y given T. It has parent Fourier law theta(U|T)q(T)=a_U,T^2 and physical child probability 1/m. Inductively it agrees with the common lift of A037.

Given already constructed child references Q_y, put

    r(T)=(1/m) sum_y Q_y(T),
    Q_h(U union T)=theta(U|T) r(T).                       (G)

At q(T)=0, fix any normalized theta(.|T), for example uniform. Such packets have zero true mass, but may carry reference mass: they must not be silently deleted. Formula (G) conserves mass: sum Q_h=(1/m)sum_y sum Q_y <=1. Positivity on actual support follows inductively from leaf support. Thus Q_h is a complete reference on the parent's entire spectral space. References can be chosen differently at different terminal histories; all interior references are determined by (G), rather than reset independently.

### 2. Exact price of the compatible reference transfer

On q(T)>0 define the reference physical-child posterior

    k_Q(y|T)=Q_y(T)/(m r(T)),
    kappa_h=sum_T q(T) D_2(k_P(.|T)||k_Q(.|T)).            (K)

Only positive P_y(T) contribute; support ensures finite logs. Gibbs gives kappa_h>=0 even when Q_y have different total masses. The joint true/reference laws on (y,T) have atoms P_y(T)/m and Q_y(T)/m; the reference can be subnormalized. Expanding their likelihood ratio first by y and then by T gives

    (1/m)sum_y D_2(P_y||Q_y) = D_2(q||r)+kappa_h.         (D)

No reference normalization is discarded. Generalized D(P||Q)=sum P log(P/Q) is used for subprobabilities; it is nonnegative because completing Q with a failure atom reduces to ordinary Gibbs, with P giving that atom zero mass.

Let B_h=H(U|T) under P_h and J_h=H(q)-(1/m)sum_y H(P_y). The restriction identity is H(P_h)=B_h+H(q). The references P_h and Q_h share theta, so D(P_h||Q_h)=D(q||r). Combining with (D) yields

    CE(P_h,Q_h)=B_h+J_h+(1/m)sum_y CE(P_y,Q_y)-kappa_h.

Multiplication by physical reach probabilities and finite telescoping proves (T). The same divergence telescope gives

    D(P_root||Q_root)=sum_l pi_l D(P_l||Q_l)-sum_h pi_h kappa_h.  (S)

In particular sum pi kappa <=sum pi D_leaf. The credit is terminal reference slack that the compatible lift removes; it is not a new source of entropy payment. Choosing every Q_l=P_l makes Q_root=P_root and all kappa_h zero. In that case (T) reduces exactly to the A061 entropy telescope. Arbitrarily replacing an interior Q_h loses (G) and invalidates (T); reference-reset corrections from A037 would then be required.

### 3. Common history and no-reuse certificate

Let L be the complete terminal physical transcript. Define P(S,L) by the bottom-up true generator above, and Q(S,L) by the same physical branch factors 1/m and kernels theta but leaf masses Q_l. Summation over L gives P_root and Q_root. The ratio Q(S,L)/P(S,L), on true support, is exactly Q_l(S_remaining)/P_l(S_remaining): the physical branch and innovation factors cancel. Thus joint divergence is sum pi_l D_leaf. Expanding the joint divergence by S and using (S) proves

    E_{S~P_root} D_2(P(L|S)||Q(L|S)) = sum_h pi_h kappa_h.

The reference posterior Q(L|S) is normalized for each positive root spectral atom, even though the full Q(S,L) may be subnormalized. This is one global posterior correction, consumed once. It is not a sum of separately recharged root credits. Similarly the true law satisfies

    I_P(S;L)=sum_h pi_h J_h,
    H_P(L|S)=H_P(L)-sum_h pi_h J_h.

These follow directly from the function-specific common lift: given current residual T and history, the next physical outcome is independent of every already erased label. Thus the apparent physical path-label entropy H(L) in an A011-style witness is reduced by its posterior redundancy to sum pi J. The new construction carries complete leaf references through that cancellation, including their support and mass, rather than only the true Fourier laws.

### 4. Explicit dimension-independent channel price

The uniform cube log-Sobolev inequality in the needed natural normalization is

    Ent(g^2) <= (1/2)sum_i E(g(x)-g(x^i))^2, g>=0.

For completeness the two-point assertion is F(t)>=0, where
F(t)=(t^2+1)ln((t^2+1)/2)-2t^2 ln t+(t-1)^2. F(1)=0. For t>=1 its derivative is nonnegative because ln(2t^2/(t^2+1))<=1-1/t; the difference's derivative is (t-1)^2/[t^2(t^2+1)]>=0. Symmetry F(t)=t^2 F(1/t) and continuity handle all endpoints. Entropy tensorization follows by conditioning successively on independent coordinates, giving the stated product inequality.

Apply it to g_y=|b_y,T|/sqrt(q(T)), for each positive fiber T, and sum with weights q(T). The left side is (ln 2)J_h. Replacing magnitude differences by signed differences only increases the right side. Parseval on C gives

    J_h <= (1/(2 ln 2))sum_{i in A} E_y sum_T
                              (b_y,T-b_(y^i),T)^2
        = (2/ln 2) I_A(f_h).

The Boolean signs give squared physical difference 4 on pivotal edges. This proves the constant with the exact physical normalization. Influence conservation is I(f_h)=I_A(f_h)+(1/m)sum_y I(f_hy); hence I(f)=I_removed+I_terminal, where I_removed=sum pi_h I_A(f_h), I_terminal=sum pi_l I(f_l). No influence is spent twice. Substitution gives (P).

### 5. Precisely closed conditional endpoint and exact remaining term

If complete leaf references satisfy c_l<=C_leaf I(f_l) and this actual tree satisfies

    sum_h pi_h(B_h-kappa_h)<=K I_removed,

for finite K,C_leaf>=0, then the constructed root reference satisfies

    H(f)<=CE(P_root,Q_root)<=max(K+2/ln 2,C_leaf) I(f).

This conclusion is all-dimensional under its stated hypotheses. No existence/payment theorem for that tree is claimed. The amount newly paid is the entire channel/history information, at at most (2/ln 2)I_removed; compatible-reference mismatch receives the exact credit sum pi kappa, bounded by leaf slack. The remaining universal line is the displayed erasure-minus-credit inequality together with uniformly certified complete leaf costs. This is not asserted by an analogy or by KL positivity.

For a nonempty subprobability reference R_l from C020 let v_l=P_l(S nonempty). Its complete extension is Q_l(empty)=1-v_l and Q_l(S)=v_l R_l(S) for nonempty S. Then

    CE(P_l,Q_l)=h_2(v_l)+sum_{S nonempty}P_l(S)log2(1/R_l(S)).

For v_l=0 choose Q_l=delta_empty; for v_l=1 set the empty mass to zero. Therefore any complete witness bound from the normalized-prior lemma can be inserted verbatim, retaining its h_2(v), root normalizer, scale prior and all gate/rank costs. Optimizing those terms independently is not permitted. Conversely an entropy-only terminal theorem permits Q_l=P_l for an existence argument, but supplies no computationally cheap dictionary claim.

The accepted B05 all-coordinate local-refund obstruction still applies: B_h/I_A can grow without bound at a chosen rare selector. This transfer does not make every split inexpensive. It provides a compatible construction for prescribed leaf laws and keeps the costly conditional labels explicit.

## executed validation with domain, arithmetic, commands and outputs

Before any computation FROZEN_SPEC.json fixed the helper, actual family, full domain, case count, symmetry, exact arithmetic, memory and 60-second cap. Command from A097: `python -X utf8 runs\20261011T221240Z-fleet05-A097-cross-route-transfer\code\check_transfer.py`.

All 278 Boolean truth tables in dimensions 0-3 were tested with three adaptive stopping rules and two reference families, giving 1,668 cases. The policy queries a least-positive-influence coordinate with original-index tie breaking; it stops at residual cutoffs 0,1,2 or constants. References are uniform probabilities or history-dependent tilted subprobabilities. Integer Walsh sums and Fraction arithmetic compute all laws. Every entropy/log-likelihood identity uses rational coefficients of log2 primes, accepted only when every coefficient cancels. Results: 68,136 exact assertions, zero failures, 1,468 cases with nonzero posterior KL and 368 with nonzero terminal entropy; initial runtime 5.698 seconds and final source rerun 9.694 seconds. out/EXACT_RESULTS.json is the final captured machine output; repeat passes are not added to the assertion count.

The separate BLOCK_FROZEN_SPEC.json fixes all functions in dimensions 1-3, every nonempty physical block and both reference families. Its declared count 3,684 was an arithmetic typo: the unchanged domain contains 2[4(1)+16(3)+256(7)]=3,688 cases. SPEC_CORRECTIONS.md preserves that discrepancy; no domain was expanded after freezing. `python -X utf8 runs\20261011T221240Z-fleet05-A097-cross-route-transfer\code\check_blocks.py` checks mass, support-fiber normalization, CE and KL transfer: 20,960 exact assertions, zero failures, 2,080 multicoordinate-block cases, initial runtime 5.053 seconds and final source rerun 3.339 seconds. Final results are captured in out/BLOCK_RESULTS.json. The two distinct jobs total 89,096 exact assertions. No numerical logarithm, random search, automatic dimension escalation or heavy job was used. The proofs above, not finite case extrapolation, supply the universal finite-tree quantifiers. This is author verification, not independent review or Lean certification.

## proof dependencies and changed downstream conclusions

The new theorem reconstructs the needed A011, A037 and A061 source identities and the block log-Sobolev estimate, and needs no unresolved universal FEI helper. Source-bound local author claims remain explicitly unaccepted. This application is distinct from merely proving their common-law baseline again: it constructs the reference law for arbitrary prescribed, individually optimized terminal references, and prices the exact compatibility correction. The independent reviewer should check zero true fibers with positive reference mass, subnormalization, phase dependence, posterior conditionals and no reuse.

A028 may insert complete terminal witness costs directly into a stopping-tree proof. A039 receives an explicit reverse-compatible lift instead of an assumed forward channel on squared parent spectra. A064 receives B_h-kappa_h as the exact remaining state cost; it must pay it on a specified physical tree. A008/A013 can replace raw path-label expense by the paid physical channel term when using this lifted reference. C020 terminal root/scale/rank costs are not removed. No downstream consumer is claimed to have adopted this version, and no shared registry was modified.

## one next mathematical action and independent reviewer

Next: A039/A064 should insert the actual complete leaf laws from the current B05 sparse activated bent-defect control-first tree into (G), then prove or refute an influence payment for sum pi(B-kappa), retaining the seed's terminal witness cost. This fixed compatible reference avoids an extra reoptimization obligation and tests the remaining universal debt directly. Independent reviewers: A090 and A094, with A088 as a KL-focused optional reader. No messages were sent; this is a saved source-bound handoff.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, CROSS_ROUTE_SUBSTITUTION.tex, TRANSFER_HYPOTHESIS_CHECK.json, both frozen specs, code/check_transfer.py, code/check_blocks.py and their exact outputs are saved within the supplied A097 run. out/PERSISTENCE_RECEIPTS.json gives sizes and SHA256, and the metadata writer checks all protocol field sets. STATUS.md, WORKLOG.md and LEARNED.md are current. Source hashes are recorded separately. No write outside A097, git, brain update, background worker, mail or publication was performed. Supervisor copying, mirror verification and independent acceptance remain pending.

Universal bridge: This stage advances C019 stopping-tree payment and C024 history/reference transfer by inserting complete C020 leaf references into a compatible root reference, eliminating separately charged raw physical history entropy and paying the full actual mixture-information term by (2/ln 2) times removed influence. The exact posterior credit is quantified, but cannot exceed terminal reference slack. No universal FEI constant is improved. The erasure-minus-credit expectation and terminal complete costs remain unpaid universally. The shortest NEXT is to evaluate that single explicit residual on the existing sparse-defect tree: another isolated threshold or percolation class estimate would not resolve its cross-route compatibility and payment bottleneck.
