# A037: conditional posterior credit ledger

Full uniform-cube FEI remains OPEN. This run closes the finite-hierarchy bookkeeping target on an explicitly common probability space. Author proofs and exact validation are supplied; independent review is pending. No novelty claim is made for Shannon/KL chain rules.

## exact target, quantifiers, hypotheses and units

All information is in bits. A tree is finite, with adaptive choices measurable from its history and any declared common random seed. W is one fixed finite witness variable; A is optional finite side information (for example the Fourier set being described). Every node posterior is a conditional law of this SAME W under ONE joint probability measure. Node h has probability p_h, next outcome Y_h, and children hy. Zero-probability nodes are omitted. Leaf L includes the full stopped transcript, so variable depths introduce no extra unrecorded stop symbol. A randomized stop is itself a recorded outcome. Entropy conservation needs no reference law. KL conservation uses finite laws P,Q with P absolutely continuous with respect to Q on all used atoms, and otherwise holds in extended values with no infinity subtraction. The formulas below are stated for finite divergences.

Two distinct resources are retained: initial conditional witness entropy H_P(W|A), and initial divergence D_2(P_W||Q_W). They are not interchangeable, nor are independently optimized child witnesses automatically posteriors of one root witness.

## sources actually read, revisions and theorem locators

The execution protocol was read in full: fei-execution-protocol/2, revision 2026-10-11-execution-v2. Campaign README, CURRENT_STATUS (snapshot 2026-10-11T20:06:24Z), claim/obstruction registries, B08 packet entries, STREAM_NEXT_ACTIONS and plan were inspected. Plan locators: Endpoint J, equations forest/residual; Endpoint R, decrement/block-erasure; A037 acceptance and execution contracts. Supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were inspected, with relevant original BLOCK_RESTRICTION_IDENTITY_2026-09-18.md read in full. Its Section 1 supplies the parent-marginal/child-mixture equality; its Section 4 warns about parity synergy. The other source directory was inventoried; unrelated files are not claimed as read or used.

Earlier B05 rare-restriction and B19 review reports were inspected for the exact local-refund no-go scope; no reproof is claimed. B09's earlier biased-block report was inspected: its physical-child mixture identity is background, not an accepted dependency for the new results. The protocol status correction limits its endpoint conclusions.

Both current paper texts and earlier versions were searched and relevant interfaces inspected. The 38-page threshold paper, Sections 2 (Gibbs/subprobability) and 5.6, Proposition 5.5 (variational finite-run witness bound), provides the fixed-generator context. The 29-page earlier paper has the predecessor queue interface. The 30-page percolation extension, Section 2, Lemma 2.1 and equations (10)-(11), retains terminal contents in its spatial tree chain rule; the 31-page other version has the same tree interface. No percolation arm estimates or threshold FEI bounds are used as premises. The paper inspection is interface-focused, not an independent audit of their entire theorems. Local source hashes are in out/SOURCES_READ.json.

BOARD.md was read at stage start. A036 handles normalized collision payment, A006 handles a concrete posterior forest optimization; this run does neither again. ~\brain_workers\FEI100_20261011\claude\B08\STREAM_NOTES.md did not exist when checked. This access absence does not block A037's explicitly assigned independent work.

## complete derivation or exact first unsupported line

### E. Conditional entropy release, stopping and no reuse

Define the release at h by c_h=I_P(W;Y_h|A,H=h), with the conditioning on A averaged under its law at h. Equivalently,

    c_h = H_P(W|A,H=h) - sum_y P(y|h) H_P(W|A,H=hy).

The entropy in the child term includes the updated distribution of A: this is essential. To verify the formula, expand each entropy into sums over a and use P(a,y|h)=P(y|h)P(a|hy). For each a the conditional mutual information is a weighted KL between P(W|a,hy) and P(W|a,h); Gibbs makes c_h nonnegative. Multiply by p_h. Every internal entropy term cancels its occurrence as a child, yielding

    sum_{h internal} p_h c_h + sum_{l leaf} p_l H_P(W|A,L=l)
      = H_P(W|A).

Thus total released information equals I_P(W;L|A) and is at most the initial resource. The terminal term is generally positive. The same identity applied below any positive-probability h bounds all future release by H_P(W|A,H=h). A previously revealed bit that is measurable from A,h has zero future release. These are expected conditional statements; individual realized surprisals need not decrease.

For any cut/frontier F separating root from all leaves, the root identity splits into release above F plus the expected remaining conditional entropy at F, and each F-node resource splits again below F. This proves conditioning cannot recharge the root account. If several credits concern coordinates or labels of W, expose them in a single joint order conditioned on earlier exposures. Adding separate marginal informations is invalid when they overlap. Example: W is a fair bit, reveal W twice. Root release is 1 bit; second release is 0. Recharging H(W)=1 at the second step wrongly charges 2 bits.

Side conditioning cannot be dropped: if W,L are independent fair bits and A=W XOR L, then I(W;L)=0 but I(W;L|A)=1. A conditional witness ledger must consistently keep the Fourier set A and all previous reveals.

For the forest residual in the plan, take P(A,r)=P_f(A|A nonempty) P_A(r), with r ranging over distinct actual successful finite runs. If r is finite-valued (or has finite entropy with a justified countable limiting argument), the entropy rebate decomposes exactly as

    H_P(r|A)=I_P(r;L|A)+H_P(r|A,L).

Consequently one may replace the original rebate by released credit PLUS the terminal rebate; one cannot subtract the original rebate and also subtract its released part. The spectral weighting is v=P_f(A nonempty), so the entire identity is multiplied by v in the complete residual. The initial term v(Lambda+log2 Z), gate costs and chosen scale-prior costs remain separate. This result does not bound any of them by influence.

### K. Divergence ledger and the exact corrections

Initially omit A; the same proof holds conditional on each a and averaging. Let p_h(w),q_h(w) be the node posteriors under P,Q. Let k_h^P(y|w), k_h^Q(y|w) be the reveal channels. Put

    K_h = D_2(p_h||q_h),
    d_h = D_2(P(Y_h|h)||Q(Y_h|h)),
    j_h = sum_w p_h(w) D_2(k_h^P(.|w)||k_h^Q(.|w)).

Expanding the joint divergence two ways proves

    K_h+j_h = d_h+sum_y P(y|h)K_hy.

Indeed the likelihood ratio factors first as (p_h/q_h)(k_h^P/k_h^Q), and second as the outcome likelihood ratio times the Bayes-posterior ratio. Sum under the joint P(w,y|h). Multiplying by p_h and telescoping gives

    sum_h p_h d_h + sum_l p_l K_l
      = K_root + sum_h p_h j_h.

All d_h,j_h,K_l are nonnegative. With a single common channel k_h^P=k_h^Q at every node, the injection is zero: total released KL plus terminal KL is exactly the initial divergence. Below a node h, the available KL is K_h, not the original K_root. Replaying an already recorded outcome has d_h=0. Different channels are permitted only with the displayed injection; it is an additional unpaid resource, not free root credit.

This does NOT say posterior KL K_h decreases pathwise. For a common informative channel, the P-expected posterior KL decreases after paying d_h. By contrast D(P(W|h)||P(W)) generally grows as observations accumulate; it is earned posterior information, not a remaining KL reserve. These two directions must not be confused.

To compare freely reset node reference laws r_h, compute the Bayes-predicted child reference q_hy from r_h and the selected Q-channel. Define the signed reset correction

    delta_hy = sum_w p_hy(w) log2(q_hy(w)/r_hy(w)).

Then D(p_hy||r_hy)=D(p_hy||q_hy)+delta_hy, and the local reset ledger is

    D(p_h||r_h)+j_h+sum_y P(y|h)delta_hy
      = d_h+sum_y P(y|h)D(p_hy||r_hy).

The cumulative formula has the same signed reset terms weighted by child visit probabilities. Dropping them invalidates the conserved-resource claim. Infinite/support-changing resets require support checks before subtraction. Common subprobability references should be completed by a failure atom (P gives it zero mass), or normalized with their total mass logged explicitly. Normalizing different node masses silently changes the ledger.

An extreme exact control: W=Y is fair under P, but Q makes W,Y independent and fair. Root K=0; release d=0; expected terminal posterior K=1, and channel injection j=1. The missing bit comes entirely from using different channels. With a common reveal Y=W, the posteriors are point masses under both laws, and replaying Y gives zero release. Resetting the reference to uniform before every replay injects a bit each time through delta; there is no conserved root bound after omitting those resets.

### P. A common lift of actual adaptive physical restriction spectra

This provides an explicit joint probability space, not an assumed stochastic map uniform over functions. At a tree node with Boolean restricted function g on R, choose a physical block B determined by the physical history; let C=R\B. Write

    a_U,T = ghat(U union T),
    b_y,T = sum_{U subset B} a_U,T chi_U(y) = (g|_{B=y})hat(T),
    q_T = sum_U a_U,T^2 = 2^(-|B|) sum_y b_y,T^2.

Draw the root spectral set S_0 with law ghat(S)^2. At each node, current S_h is S_0 intersect R. Given its C-part T, choose physical outcome y with

    k_h(y|S_h) = 2^(-|B|) b_y,T^2/q_T

when q_T>0; a zero fiber is unreachable and can be assigned any normalized kernel. Then set S_hy=T. Equivalently at a node the joint atom is

    P(U,T,y|h)=a_U,T^2 * 2^(-|B|) b_y,T^2/q_T.

Parseval gives sum_y k_h=1. Summing U gives P(y,T|h)=2^(-|B|)b_y,T^2; summing T gives P(y|h)=2^(-|B|) because each child is Boolean. Thus the physical branch probabilities are precisely fair, and P(S_hy=T|hy)=b_y,T^2, the actual child spectrum. Inductively the construction supplies one finite common joint space for every finite adaptive physical block tree, with no rerevealed physical coordinates.

At each node it also imposes U independent of Y given T. Hence I(S_h;Y|h)=I(T;Y|h), the local physical-child mixture information. The root-information decomposition is

    I(S_0;Y|h)=I(T;Y|h)+I(S_0\R;Y|T,h).

The second term is zero in this lift: k_h depends only on T,h, so Y is conditionally independent of all the rest of S_0 given T,h. Therefore the cumulative physical mixture information equals I(S_0;L), with terminal remainder H(S_0|L). This proves a common-space conservation law for mixture information on adaptive physical trees. It does not identify the terminal root posterior with the leaf Fourier entropy: when all coordinates are fixed, S_h is empty but S_0 can remain uncertain. The full entropy decrement also includes erased-label conditional entropy, not just mixture information.

More precisely let B_h=H(S_h intersect B|S_h intersect C,H=h) and J_h=I(T;Y|h). Parent entropy is H(T|h)+B_h and the expected child entropy is H(T|Y,h), proving the local decrement B_h+J_h. Telescope this identity and substitute sum_h p_h J_h=I(S_0;L) to obtain the exact residual identification

    H(S_0|L) = sum_h p_h B_h + sum_l p_l H(f_l).

Thus the common-space terminal posterior is precisely cumulative unpaid erasure plus terminal spectral entropy. This is a useful compatibility identity, not an estimate of that residual. The existing block-information bound J_h<=(2/ln 2) I_B(f_h), together with influence conservation, already pays sum p_h J_h by (2/ln 2) I(f); it does not pay the right side above. No new FEI conclusion follows by bounding the mixture information again.

The lift uses Fourier phases through b_y,T. A universal phase-blind channel on parent squared spectra is impossible. On two bits (bits 0,1 represented by signs (-1)^x), take f=[1,1,1,-1] and g=x_1 f, so g=[1,1,-1,1]. Both parent spectra are uniform on the four subsets. Restrict bit 0 to index value 0 (sign +1): f's child is constant and g's child is the bit-1 character. Identical parent squared laws thus give different actual named child laws. The constructed kernel is function-specific; it does not justify applying data processing to a reoptimized convolution reference unless the same kernel or the correction in K is proved.

An arbitrary root witness r can be appended via its chosen conditional law given S_0 and then propagated using this lift. Its descendants are well-defined posteriors. They need not equal independently selected witness laws for the restricted functions. A transfer correction or compatible construction is still needed. This is the exact first unsupported line in any proposed universal FEI application: the claim that child reoptimization/reference replacement costs and the remaining erased-label/witness cost admit one dimension-independent influence payment.

## executed validation with domain, arithmetic, commands and outputs

The frozen specification predates execution in out/FROZEN_SPEC.md. Command from A037's folder:

    python -X utf8 runs\20261011T220010Z-account05-A037-conditional-credit-ledger\code\ledger_check.py

The checker uses Fraction for every probability and prime exponent maps for rational logarithms. An entropy identity is accepted only when every rational coefficient of log2(prime) cancels exactly; there is no floating-point sign certificate. It checks 81 strictly positive rational chain/channel/reference-reset cases, all 256 three-bit Boolean functions under the specified adaptive depth-two physical tree, all 16 two-bit Boolean spectra and child normalizations, an exact phase control, and elementary repeated/side-conditioned information controls. Finite checks validate algebra and implementation; all-tree quantifiers are supplied by the proofs above. Output is out/VALIDATION.json, including executed assertion count and observed runtime. No heavy job or dimension escalation was used.

The initial execution caught a checker zero-fiber error: zero-mass states created by accumulation were retained and later divided by a zero fiber. Filtering those states implements the proof's unreachable-fiber convention. The corrected pass and the additional exact erased-label/terminal identity checks are retained; this was an implementation correction, not a failed mathematical mechanism.

Final validation: 18,945 exact assertions PASS, 81 rational cases, 256 physical lifts and 16 two-bit Boolean controls; observed checker runtime 0.689 seconds. Persistence schema validation uses the wire key packet_ids: the protocol progress_fields entry appends the explanatory phrase '(one primary ID, for compatibility)', while its compatibility section explicitly prescribes packet_ids=[primary packet_id]. No other fields are added or omitted.

## proof dependencies and changed downstream conclusions

The two new claims are source-complete self-contained author proofs using finite probability algebra, Gibbs inequality (proved by -ln t >=1-t) and Walsh Parseval (character orthogonality). No unaccepted campaign theorem is a logical dependency. External inputs orient the target and terminology only. A023/A029/A063/A064 can use a precise retained-resource identity. A039/A057 must either use one shared reveal kernel or pay the channel/reset correction; child spectra alone do not establish it. A097 can use the physical lift to place adaptive node posterior credits on one space, while keeping child witness transport open.

## one next mathematical action and independent reviewer

Next: A039/A064 should compute the exact channel injection and reference-reset correction for the chosen parent/child witness generator on the sparse activated bent-defect tree, and test whether their weighted sum is bounded by physically removed influence. This is one concrete compatibility/payment obligation, not another unconstrained KL positivity lemma. Independent reviewers assigned by the packet: A088 and A094; no independent acceptance is claimed.

## actual persistence receipts or precise save blocker

The run contains REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, POSTERIOR_CREDIT_CHAIN.tex, NO_REUSE_CERTIFICATE.md, code/ledger_check.py, out/FROZEN_SPEC.md, out/VALIDATION.json and out/SOURCES_READ.json. out/ARTIFACT_SHA256.json records local file hashes after validation. Rolling STATUS.md, WORKLOG.md and LEARNED.md were saved in A037 only. Shared registries, other agents, brain databases, repositories and publication were not modified. Supervisor copying, mirrors and downstream use remain unverified.

Universal bridge: This stage advances C024 history transfer and the bookkeeping interface of C019 stopping-tree payment by proving exact conditional entropy/KL conservation, retaining terminal balances and pricing incompatible channels/references explicitly; it also supplies a function-specific common lift for adaptive physical spectra. It gives no new universal constant and does not close C018 or C020. The remaining obligation is an influence bound for the entire transported witness/erased-label cost, including reset and channel terms. The shortest next route is measuring and paying those terms on the current physical witness hierarchy: without compatibility, apparent repeated credit cannot support any universal stopping-tree argument, regardless of further class estimates.
