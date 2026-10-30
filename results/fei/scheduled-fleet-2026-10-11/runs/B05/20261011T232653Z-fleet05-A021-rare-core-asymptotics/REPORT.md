# A021 stage 2: corrected remainder and an exact bad-face scheduling obstruction

## exact target, quantifiers, hypotheses and units

Full FEI is OPEN. This stage follows the B05 lead's designated localized odd-face bridge. For a physical coordinate i, let B_i=H(S_i|S_-i), d_i=Inf_i(f), and c_i=I(f_i^+ f_i^-)/2. A node is strictly K-bad when B_i>Kd_i. For a complete physical restriction tree, define Q_bad,K=sum_{bad v} w_v c_v, with actual uniform-cube reach probabilities w_v. All entropies are bits; logarithmic certificates explicitly convert to natural numerators using ln2.

Targets: (1) repair the sign of A021's stage-1 uniform remainder, including affected ratio and decrement bounds; (2) exactly locate bad nodes and measure their odd-face charges on balanced tensor activations in control-first and data-first orders; (3) extract an exact scheduling condition and determine the quantifier of the localized bridge that this family refutes. Parameters t,k remain independent until a limit is specified. All new computations stay at dimension <=13, and the all-parameter conclusions rest on the proofs below.

## sources actually read, revisions and theorem locators

Read BOARD.md (supervisor snapshot 2026-10-11 23:19 UTC), B05/STREAM_NOTES.md v1 (22:4xZ), own STATUS.md and LEARNED.md, and the entire execution protocol, revision 2026-10-11-execution-v2. The B05 notes explicitly require rechecking the remainder sign and classifying bad-node odd-face charges in both orders.

Read the lead's saved in-progress source claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport/_body.md, Lemmas 1-2, Theorem 4, Sections 3 and 6. REPORT.md was initially absent. During final receipt generation the lead replaced _body.md with the completed REPORT.md; that final report was then read and hashed, and its same mathematical passages support the target and correction. Family-specific face and erasure arguments here are reconstructed directly rather than treating a source label as independent acceptance. The provisional source no longer exists at receipt time; the final source is the reproducible pin.

Read A023's REVIEW_A021.md in run 20261011T221608Z-fleet05-A023-amortized-rarity-budget. Its acceptance repeated the same erroneous series sign. Read A087's corresponding report passages in run 20261011T221055Z-fleet05-A087-restriction-referee, especially its A021 reconstruction and remainder assertion. Its sign reconstruction also repeats the error. Their acceptance of exact spectra and KL ledger is unaffected; acceptance of the full v1 asymptotic interval must be narrowed. A087's separate statement-hash criticism does not invalidate our original canonical statement/hypotheses object hashes; this run continues the convention explicitly stated in CLAIM_REGISTRY.json.

Read A025's report in run 20261011T225648Z-fleet05-A025-rare-event-counterfamily. It already refutes threshold K=2 for every complete tree on a point defect and shows why that family fails to obstruct fixed K>2. We do not reprove that result. Our new obstruction addresses every fixed K for the stronger EVERY-tree quantifier, and provides a paid control-first alternative at K=4.

Stage-1 activation baseline remains threshold paper Section 8.4, Proposition 8.9 and Corollary 8.10, already inspected in the preceding stage. No new literature priority claim, unreviewed B09 lemma, or external source is used. Exact local source hashes and scope are saved in out/source_inventory.json. Only A021 files were written.

## complete derivation or exact first unsupported line

### 1. Repair: positive entropy remainder and negative decrement remainder

Put c=1/ln2, q=2^-k. Direct multiplication gives, for j>=3,

    1/j-2/(j-1)+1/(j-2)=2/[j(j-1)(j-2)]>0.

Therefore the correct uniform identity is

    b(q)=-2(1-q)^2 log2(1-q)=2cq-3cq^2+R(q),
    R(q)=+4c sum_{j>=3} q^j/[j(j-1)(j-2)],
    0<R(q)<=2cq^3/[3(1-q)] for 0<q<1.

For balanced seed b, h=H(b), i=I(b), its t-fold disjoint tensor g_t, and F=1+A_k(g_t-1), the exact spectrum from stage 1 still yields

    H(F)=q[th+4k+2c]-q^2(2k+3c)+R(q), I(F)=q(ti+k).

Let Ra=[th+4k+2c-q(2k+3c)]/(ti+k). The corrected interval is

    Ra <= H(F)/I(F) <= Ra+2cq^2/[3(1-q)(ti+k)].

The slack is q[t(Ci-h)+(C-4)k-2c+q(2k+3c)]-R(q): the remainder lowers slack. For a control entropy decrement at u=2^-s, s>=2,

    Delta_s=4u+(2s-4+3c)u^2+G_s,
    G_s=R(u)-R(2u)/2,
    -8cu^3/[3(1-2u)] <= G_s < 0.

Indeed the series coefficient is 4c(1-2^{j-1}), negative for each j>=3. The s=1 endpoint remains Delta_1=2. Exact spectra, influences, KL debt, tensor-ratio limits and the claim A021-CONTROL-FIRST-KL-LEDGER v1 remain unchanged. The stage-1 finite checker did not test this series sign. Two nominal independent acceptances repeated the same arithmetic error; they do not validate the false interval.

Historical artifacts are preserved. CORRECTION.md identifies affected source passages and consumers; replacement A021-UNIFORM-RARE-CORE-EXPANSION v2 is in this run. Claude B05 contributed the sign repair and cannot independently accept that repaired version. Rational interval certificates at q=2^-s for s=1..12 independently verify positive entropy remainders; s=2..12 certificates verify negative decrement remainders.

The direct bound b(q)<=2cq survives independently: -(1-q)ln(1-q)<=q, then multiply by 2(1-q). No surviving sufficiency bound is justified by discarding a falsely negative remainder.

### 2. Three identities for tracking actual bad nodes

If f is split into children a,b, the queried-coordinate Fourier erasure is

    B_i(f)=sum_W (ahat(W)^2+bhat(W)^2)/2
                     *h2((ahat(W)-bhat(W))^2/[2(ahat(W)^2+bhat(W)^2)]).

Zero packets contribute zero. This formula remains valid with signed child coefficients; h2 is symmetric if opposite signs change the conditional probability to its complement.

First, disjoint multiplication by another sign factor preserves B_i and d_i in the queried factor. Its independent squared spectrum is a tensor factor in the conditional entropy, and its square cancels in the children product.

Second, suppose both core children have mean zero and let F=1+A_k(g-1). Then

    B_i(F)=q B_i(g), d_i(F)=q d_i(g),
    c_i(F)=q c_i(g)+kq d_i(g).

Proof of erasure: every nonempty residual-data coefficient in each child is multiplied by q and repeated across 2^k control sets; packet entropy is homogeneous of degree two, giving q times the core packet sum. Empty data rows have equal coefficients -q for nonempty control sets and 1-q for the empty control set, so contribute zero. Mean-zero children are essential to this cancellation.

Proof of odd-face charge: the actual activated children product is 1+A_k(g_i^+ g_i^- -1). Its data influence is q I(g_i^+g_i^-). Its each control influence is 2q Pr(g_i^+g_i^-=-1)=2q d_i(g), giving the formula after division by two.

Third, all control nodes of a balanced-core activation are K=3-good. At an active node with s controls left, u=2^-s,

    B_control=L_s=2(u-u^2)+Q0 h2(u^2/Q0), Q0=1-2u+2u^2,
    d_control=u.

For s=1, L_s/u=2. For s>=2, the exact binary-entropy expression gives

    L_s/u <= 2+u(2s-2+c) <= 2+(2+c)/4 < 3.

To justify the first bound, use log Q0<=0 and
(Q0-u^2)log2[Q0/(Q0-u^2)]<=c u^2. The sequence 2^-s(2s-2+c) decreases for s>=2, so its maximum is at s=2; c<2 follows from ln2>1/2. A point-defect node on r>=2 bits has exactly the same B/d as this balanced-control node with s=r-1, while r=1 is a character with B=0. Therefore point-defect controls are also 3-good, uniformly in dimension. This direct estimate does not use the incorrectly signed stage-1 expansion.

### 3. A fixed balanced six-bit core and a finite exact leaf certificate

Let b4(x)=(-1)^(x1*x2+x3*x4) on four bits, b4' its value flip at x=0, a(y,x)=b4 for y=0 and b4' for y=1, and b(z,y,x)=z a(y,x), with fresh uniform sign z. This is balanced. Its influence is

    I(b)=1+I(a)=1+2+5/16=53/16.

Indeed I(b4)=2; the zero flip toggles one edge in each of four coordinates, so I(b4')=2+8/16; the selector influence is d=1/16. Averaging the data influences and adding d gives I(a)=37/16.

At the selector, the 16 bent Walsh coefficients are +/-1/4, with 10 positive and 6 negative. The flip subtracts 1/8 from every coefficient. Child packet masses are 5/128 (ten packets) and 13/128 (six packets); each mismatch mass is 1/256. Thus

    B_y=(10[10 log2 10-9 log2 9]+6[26 log2 26-25 log2 25])/256,
    256 ln2 (B_y-4/16)=192 ln2-180 ln3-200 ln5+156 ln13>0.

The last strict sign has a rational atanh certificate in out/validation.json. Balancing by z changes no selector erasure or influence. The actual children product is b4*b4', a point defect on four bits, so its odd-face charge is 4/16.

Every coordinate of every physical restriction of b4 or b4' has B_i<=4d_i. This is a finite proof obligation, closed by 216 split certificates: each of the two functions has 4*3^3=108 pairs (partial assignment, live coordinate). Output out/seed_split_certificates.json records every partial assignment, queried original coordinate, integer-Walsh denominator, exact influence, prime-log vector and rational sign enclosure. All 216 natural numerators of B_i-4d_i are nonpositive. No larger census or numerical extrapolation is used.

### 4. Exact complete-tree classifications for every t,k

Take t disjoint copies of b above, g_t=product b_j, and k fresh point controls, F=1+A_k(g_t-1). We use two fully specified complete orders:

    CF: controls; all t selectors; all 4t bent-data bits; all t balancing signs.
    DF: all t selectors; all 4t bent-data bits; all t balancing signs; controls.

On either order, K=4-bad nodes are exactly the selector stages, with branches stopped whenever the function is already constant.

For CF, the control nodes are good by Section 2. They leave one live core branch of probability q. At each selector stage the disjoint-factor identity leaves B_y and d unchanged, so every selector node is bad. After selectors have been queried, each factor is z_j times either bent child. During the bent-data queries the four-bit restriction certificate makes every node good, with disjoint factors affecting neither B nor d. The remaining signs form a character and have B=0. Hence

    Q_bad,4(CF)=qt/4.

For DF, unqueried balancing signs make both children mean zero throughout the selector and bent-data stages. Thus B and d scale by q exactly. Every selector stage stays bad, and its node odd-face charge is q(4+k)/16. Each stage's physical reach probabilities sum to one, so the total selector charge is qt(k+4)/16. All bent-data nodes remain good by exact scaling and the finite certificate. With at least two balancing signs left, each queried sign has B=0; the last sign produces a point defect on k+1 bits, whose B/d is less than 3 by Section 2. After the signs, the function is either constant or a point defect on the controls, again good. Consequently no hidden bad stages remain and

    Q_bad,4(DF)=qt(k+4)/16.

Together with I(F)=q(53t/16+k),

    Q_bad,4(CF)/I(F)=4t/(53t+16k)<=4/53,
    Q_bad,4(DF)/I(F)=t(k+4)/(53t+16k).

Taking t=k^2 gives the DF ratio asymptotic to k/53, despite I(F)->0 and Pr(F=-1)=q/2->0. CF remains paid. This is an obstruction to an arbitrary-order claim, not to the existence of a paid order.

### 5. Exact adaptive interleaving condition

The fixed six-bit witness also permits a policy-level identity. During a prefix, query only controls and previously unqueried selector bits, stopping on an inactive control. After every selector has been queried, finish by querying the bent-data bits, balancing signs, and any remaining controls. Let r_j be the number of controls still unrevealed just before the j-th selector query on the hypothetical branch where all controls are active; the rule may depend on earlier selector outcomes, so r_j is a random variable under uniform selector histories. Selector labels may also be chosen adaptively, provided each copy's selector is used once.

All nonselector nodes of this policy are good by the preceding proof. The exact localized charge is

    Q_bad,4(policy)=q/16 [4t+sum_{j=1}^t E r_j].

For a selector history with j-1 earlier selectors and k-r controls fixed active, its physical weight is 2^{-(j-1)}2^{-(k-r)}. Multiplying by its activation factor 2^-r leaves q 2^{-(j-1)}. Its unactivated charge is (4+r)/16. Summing over fair histories gives the formula, without charging inactive branches or assuming spectral independence of physical histories.

For any claimed constant K', the exact necessary and sufficient condition within this policy class is

    sum_j E r_j <= 16 K'(53t/16+k)-4t.

Thus when t>>k, a uniformly paid policy must keep the average number of unrevealed controls at bad selector queries bounded independently of k. CF has r_j=0; DF has r_j=k. This specifies the missing scheduling work instead of replacing it by another scalar rarity bound. An adaptive finite certificate (t=2,k=1) queries the control before the second selector only on the first-selector zero branch: sum E r_j=3/2 and Q_bad=19/64. All twelve deterministic prefix orders in the two three-coordinate cases were checked exactly as well.

### 6. EVERY-tree localized payment fails at every fixed threshold

The fixed K=4 example extends to any finite K>=0 without a new dimensional search. Choose an even m>=4 such that m-2>K; let bent_m be the product of m/2 quadratic two-bit bent factors, flip its value at zero, splice with a selector y, and balance with z. Put delta=2^-m. Each Walsh coefficient c_T of the bent function is +/-sqrt(delta); the flipped coefficient is c_T-2delta. Thus each mismatch packet has mass delta^2 and

    Q_T=(c_T^2+(c_T-2delta)^2)/2>=delta/4,
    B_y >= sum_T delta^2 log2(Q_T/delta^2)
        >= delta(m-2)>K delta.

The core selector is genuinely bad, with influence delta, core child-product charge m delta, and seed influence i_m=1+m/2+(m+1)delta. The fresh balancing sign keeps both children mean zero at every selector-first stage of the activated t-fold tensor, even after earlier selectors have been fixed. Therefore, for the designated complete DF tree,

    Q_bad,K(DF) >= qt delta(m+k),
    Q_bad,K(DF)/I(F) >= t delta(m+k)/(t i_m+k).

Set t=k^2 and let k grow, holding this m fixed. The lower bound diverges linearly in k. Hence for every fixed finite K,K' there are actual Boolean balanced-core activations and complete physical trees with Q_bad,K>K'I. This rules out a payment quantified over EVERY complete tree for any fixed threshold, not merely K=2 or K=4.

For K>=3 these examples have a paid alternative: CF has good control nodes, and the remaining localized charge is at most q Q(g_t)=qt Q(seed), with Q(seed) finite since m is fixed. The equality Q(g_t)=tQ(seed) follows because mixed two-faces between disjoint factors have corner product +1. This prevents promoting the bad DF ledger into an existential-tree refutation or an FEI counterexample.

The face normalization itself is directly checked: Q(f)=2^(1-n) times the odd-two-face count, and Q(f)=I(f_i^+f_i^-)/2+(Q(f_i^+)+Q(f_i^-))/2. A two-face involving i corresponds to an edge cut by the children product; other two-faces stay in one child. The frozen full-tree checks verify that both orders spend the same total Q while locating different fractions at bad nodes. Tree independence of TOTAL face mass does not imply tree independence of its BAD-node part.

First unsupported universal line: construct, for every Boolean f, a realizable policy whose bad-node odd-face mass is <=K'I(f) at an absolute sufficiently large K, together with a nonreusing terminal entropy payment if the policy stops early. Our adaptive formula settles that condition only on the explicit fresh-control witness; overlapping controls and arbitrary cores remain unpaid.

## executed validation with domain, arithmetic, commands and outputs

Three frozen specifications were saved before their corresponding jobs. Memory estimates were at most 80 MB; resident memory was not instrumented. No job was expected to exceed 300 MB, and no GPU, process spawning, window, or automatic dimension increase occurred. Every compute job had a 60-second frozen cap, and all measured runtimes were below one second.

- out/FROZEN_SPEC.json: one-case pilot, then four functions at (t,k)=(1,1),(1,2),(1,3),(2,1), dimensions 7,8,9,13, both full orders. Exact Walsh/edge checks confirm I, Q_bad and the total face telescope. Full validation additionally checks all 216 seed restriction splits, twelve positive remainder intervals, and the selector's strict badness certificate. The pilot took 0.0041 seconds; validation took 0.1419 seconds of measured Python time.
- out/CERTIFICATE_SPEC.json: code/certificates.py persists all 216 sign leaves and eleven negative decrement-error intervals. Measured runtime 0.0319 seconds. Domain unchanged; this adds the previously untested sign obligation and explicit leaf receipts.
- out/INTERLEAVING_SPEC.json: twelve deterministic prefix schedules and one adaptive schedule on the same dimension-bound pairs, exact rational charges. Runtime 0.3218 seconds. Output out/interleaving_certificates.json, thirteen cases PASS.

Commands, from A021:

    python -X utf8 runs/20261011T232653Z-fleet05-A021-rare-core-asymptotics/code/check.py --pilot
    python -X utf8 runs/20261011T232653Z-fleet05-A021-rare-core-asymptotics/code/check.py
    python -X utf8 runs/20261011T232653Z-fleet05-A021-rare-core-asymptotics/code/certificates.py
    python -X utf8 runs/20261011T232653Z-fleet05-A021-rare-core-asymptotics/code/interleaving.py

Certificates use integer Walsh sums and Fraction arithmetic. If the full-cube Walsh coefficients adjacent along a queried coordinate are integers a,b, the natural numerator of B_i-Kd_i is

    sum_pairs [(a^2+b^2)ln(a^2+b^2)-a^2 ln(a^2)-b^2 ln(b^2)]
       -K sum_pairs b^2 ln2,

divided by the squared cube size. Zero terms are omitted. Logs are factored into a rational prime-log vector, and signs are enclosed with atanh series, not inferred from floating values or from unproved logarithm independence. Normalize an argument to 2^e r, 1<=r<2, and use ln r=2 sum y^{2j+1}/(2j+1), y=(r-1)/(r+1)<=1/3. The omitted positive tail is bounded by 2y^{2N+1}/[(2N+1)(1-y^2)]. Negative coefficients reverse interval endpoints. Reciprocal logs and all signed interval arithmetic preserve ordering. Empty vectors prove exact equality. The analytic large-parameter bridge is Sections 4-6; the finite jobs do not extrapolate signs into larger dimensions.

## proof dependencies and changed downstream conclusions

The repaired v2 expansion is self-contained, with Claude B05 as a repair contributor. Its exact activation identities are unchanged baseline from stage 1 and threshold Proposition 8.9. The odd-face order obstruction and interleaving identity are derived directly from actual children, tensor independence, exact seed split certificates and Walsh homogeneity; they do not rely on any false v1 remainder or an unaccepted external theorem. The localized isoperimetric reduction in the lead's Theorem 4 identifies the C019 target; the obstruction here does not need the isoperimetric theorem itself.

Changed source conclusions: A021-UNIFORM-RARE-CORE-EXPANSION v1 is refuted in its remainder interval and superseded by v2. A023/A087's acceptance of that interval must be withdrawn or narrowed; their separate exact KL and spectrum reconstructions survive. B20 is the shared-registry owner; this run saves the original source-bound correction and affected consumer list without editing their files or claiming adoption. Since B05's pending queue already exceeds the protocol cap, the new work is repair and a narrow attack on the lead's specified live bridge, not another broad positive candidate.

Changed mathematical conclusion: localized odd-face payment can never be an arbitrary-complete-tree theorem at any fixed threshold. At K=4 the explicit fresh-control witness admits a paid CF tree, while its DF tree fails without bound; the adaptive formula isolates the unrevealed-control exposure that an existential policy must pay or avoid. Full FEI and the existential C019 bridge remain OPEN.

## one next mathematical action and independent reviewer

Next: derive the counterpart of sum E r_j for two overlapping activation events sharing one core, and determine whether an adaptive rule can bound that exposure without spending the same control boundary twice or discarding terminal core entropy. A023 owns the overlapping-control packet; A021's continuation should derive the policy criterion and hand off that scalar exposure, rather than duplicate its exhaustive cases. Independent reviewers requested through saved artifacts: A094 for the repaired sign and propagation scope, and A087 for the strict bad-node classifications, uniform schedule identity and EVERY-versus-EXISTS quantifier. Claude B05 is a contributor to the repair and not an independent reviewer of v2.

## actual persistence receipts or precise save blocker

Saved locally: the four protocol files, CORRECTION.md, BAD_NODE_LEDGER.md, executable checks, all three frozen specs, rational log certificates, finite tree results, source inventory and final artifact receipt. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current only in A021. out/artifact_receipt.json binds local hashes and sizes; all files are below 20 MB. Independent review of this run, registry adoption, supervisor copies, GitHub/Brain mirrors and downstream substitution have not been verified. No message was sent to another person or agent.

## Universal bridge

This stage moves C019 through the B05 localized odd-face target: it repairs a wrong asymptotic sign, proves exact paid control-first versus divergent data-first bad-node ledgers, refutes EVERY-complete-tree payment at every fixed threshold, and replaces vague scheduling with the exact exposure sum_j E r_j for adaptive interleavings. The universal EXISTS-policy payment, overlap ownership and arbitrary terminal entropy remain open. The shortest next route is to transport this exposure criterion to overlapping controls, where querying one rare event can alter another event's residual bill: that directly tests the missing nonreusing policy needed by C019, rather than claiming another isolated class as progress toward full FEI.
