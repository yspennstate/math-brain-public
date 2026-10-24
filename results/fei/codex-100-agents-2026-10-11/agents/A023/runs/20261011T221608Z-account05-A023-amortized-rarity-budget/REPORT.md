# exact target, quantifiers, hypotheses and units

A023 / B05, run 20261011T221608Z-account05-A023-amortized-rarity-budget. All cubes are uniform, all functions are Boolean signs, and entropy/KL/logarithms are in bits. Set c=1/ln(2). For any Boolean core g, r>=1 fresh controls, p=2^-r, and a=1-Eg in [0,2], define F=1+A_r(g-1), where A_r specifies one physical control point. The stopping tree queries these controls in a fixed order, stops that component on the first mismatch, and otherwise stops at g after r matches. It is physical, adaptive through this stopping rule, deterministic, and finite.

Write J_v=mu_v[log2(1/mu_v)-D2(nu_v||Q_v)], with mu_v the MAGNITUDE mismatch (minority fiber) mass, Q_v the average child squared Fourier law, and nu_v its normalized minority law. Zero mismatch means zero cost. The first target is the complete bound

    sum_v w_v J_v <= K rpa,   K=1+c+8c/e < 7,
    sum_v w_v (J_v+3c mu_v) + pH(g) <= 12rpa+pH(g).

The terminal term is retained. The influence partition is exactly I(F)=rpa+pI(g). A second, direct calculation gives H(F)<=pH(g)+8rpa.

The unconditional nontrivial family is every finite disjoint product of these activations whose core is a fair selector between an arbitrary bent function on even k>=4 bits and its flip at an arbitrary one vertex. Widths r, bent dimensions k, chosen vertices, and number of components are all independent and unbounded. For this family control-first J+terminal<=7I, the full sufficient mismatch ledger including 3c mu is <=12I, and H<=8I. Selector-first J+terminal<=8I and its full sufficient ledger is <=13I. This includes the original B05 quadratic witness with r=2k. No assertion of universal tree selection or full FEI is made.

# sources actually read, revisions and theorem locators

Protocol revision 2026-10-11-execution-v2 was read in full. README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS, and the plan were read or inspected at their relevant sections. The plan's A023 acceptance contract is at lines 652-656: both query orders, full KL charge, terminal cost and an unbounded extension. BOARD.md was read at the start (2026-10-11 22:16 UTC snapshot). The supplied claude/B05/STREAM_NOTES.md does not exist. No conflicting lead instruction was inferred.

Original archived B05 report, sections 2-7, source commit 80cc2e5027efa56d79c4ecdf7d4949759ef2068b; B19 independent report, sections 1-5, commit 7955d427222392911dc6af2e4ee3aa8aab67ac8c. Accepted context: a bad selector split defeats fixed-price local refunds, not FEI or a selected tree.

A021 REPORT.md and both version-1 claims were reconstructed independently below, before opening this new family claim. A022 REPORT.md and POINT_SURGERY.tex supplied the signed surgery/normalization warning; their formulas used here are reproved by edge counting and Walsh linearity, rather than assumed accepted.

Supplement CAMPAIGN, CLAIMS (especially C019), COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and the source inventory were inspected. Mathematical passages used: sources/ISOSPECTRAL_SPLICING_CURATED.md sections 2-3 (exact minority/KL and recombination), and sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md equations (4),(10) (complete terminal and influence identity). ISO original blob is 3421c0cbfd22031554befb962ec92cd0c8bb45b9. The supplement protocol source pin is bfb1d10b25cb5cb2e09112357cd24b21b5b1fe5e. No literature novelty claim is made.

Supplied paper passages inspected: threshold_paper_38pp.txt Proposition 8.9 and Corollary 8.10, with Proposition 7.1/8.6 statement map; threshold 29pp earlier Proposition 7.1; percolation 30pp Theorems 3.1-3.2 and the alternate 31pp introduction/statement map. These provide scope checks, not percolation hypotheses for this family. The current paper's balanced-core activation is credited as baseline. File hashes/byte-loading receipts are in out/source_receipts.json; loading a whole text is not a claim of auditing every unrelated theorem.

# complete derivation or exact first unsupported line

## 1. Node definitions and the complete entropy allowance

For child coefficients x_T,y_T, let Q_T=(x_T^2+y_T^2)/2, e_T=(x_T-y_T)^2/4 and m_T=(|x_T|-|y_T|)^2/4=min(e_T,Q_T-e_T). Put d=sum e_T, mu=sum m_T<=d, L=sum Q_T h2(e_T/Q_T). The exact decrement is Delta H=L+JS(x^2,y^2). The signed logarithmic allocation is J^sgn=sum e_T log2(Q_T/e_T); the required minority allocation is J=sum m_T log2(Q_T/m_T). Each is its own normalized KL expression; they must not be interchanged at a sign-changing endpoint.

Elementary entropy expansion gives J<=L and L<=J^sgn+c d. The first follows because the other half of binary entropy is nonnegative; the second follows from -(1-t)ln(1-t)<=t. Separately L<=J+c mu. The Hellinger inequality JS<=2c mu gives Delta H<=J+3c mu. For completeness: write two probabilities as s(1+t),s(1-t). The nats JS contribution is s[(1+t)ln(1+t)+(1-t)ln(1-t)]/2, at most s(1-sqrt(1-t^2)). The difference starts at zero and has derivative t/sqrt(1-t^2)-artanh(t)>=0, since this derivative's derivative is nonnegative. Summing gives JS_nat<=sum (|x_T|-|y_T|)^2/2=2mu. Thus no unreviewed restriction theorem is needed for this allowance.

## 2. Arbitrary-bias control tree and its retained KL payment

At the unique active node with s remaining controls set u=2^-s and d_s=u a. Its children are 1 and 1+A_(s-1)(g-1). The physical reach probability is w_s=p/u. The empty packet has Q0=1-2d_s+2d_s^2 and signed mismatch e0=d_s^2. In every other packet one child coefficient is zero, so e_T=m_T=Q_T/2, and the total such mismatch is d_s-d_s^2. Hence, for all s including the last one,

    J_s^sgn=d_s-d_s^2+d_s^2 log2(Q0/d_s^2).

If s>=2, the active child's mean 1-2ua is nonnegative; consequently magnitude mismatch agrees with signed mismatch. For s=1 and Eg<0 the empty minority is (1-a/2)^2 rather than a^2/4. We retain the genuine minority cost and only use J_s<=L_s<=J_s^sgn+c d_s. This handles g=-1, g=+1, zero coefficients, and the last-layer sign change. For a=0 the whole tree is constant and all costs are zero.

Since Q0<=1 and 0<d_s<=1,

    J_s^sgn <= d_s+2d_s^2 log2(1/d_s).

Every summand 2^-s(s-log2 a) is nonnegative for a<=2. The infinite sums sum 2^-s=1 and sum s2^-s=2 therefore imply

    sum_s w_s J_s^sgn
      <= p a r + 2p a^2 sum_(s=1)^r 2^-s(s-log2 a)
      <= p a r + 2p a^2(2-log2 a).

Differentiation on 0<a<=2 gives max a(2-log2 a)=4c/e, attained at a=4/e. Combining with J_s<=J_s^sgn+c d_s and sum w_s d_s=rpa proves

    sum_s w_s J_s <= p a[r(1+c)+8c/e] <= K rpa,
    K=1+c+8c/e<7.

Also sum w_s mu_s<=rpa, so the full allowance is at most (K+3c)rpa<12rpa. The remaining expected entropy is exactly pH(g), with expected influence pI(g). Influence is partitioned exactly because each queried control has influence pa and every data influence is p times the core's influence.

These constants require no floating sign calculation. The atanh series gives ln2>2(1/3+1/81)=56/81, and the exponential series gives e>65/24. Thus c<81/56 and c/e< (81/56)(24/65). Substitution proves K<7 and K+3c<12 by rational arithmetic.

## 3. First-revelation ledger and no reuse across descendants

Give this control block one identifier when its first control is queried. Its account holds exactly B_ctrl=rpa, consisting of the distinct physical control-coordinate influences. Its single bill is the complete expected sum of the J_s charges; descendants add subcharges to that bill and cannot open a second account for the same control event. It is closed when the block first becomes known inactive (first mismatch) or known active (r matches). The core account is pI(g), belongs only to the terminal core, and pays pH(g). The two accounts are disjoint; neither is pledged to both a parent and a descendant. This is a first-revelation payment in the sense of the first physical revelation process of a declared event, not an oracle revelation of an unqueried event.

KL credit is generated at the node where its actual (nu_s,Q_s) pair is defined, and consumed once in that node's J_s=mu_s log(1/mu_s)-mu_s D2(nu_s||Q_s). We neither transfer a KL value to another reference law nor claim that the same event earns a fresh credit at every descendant. The paid quantity is the completed block bill, with all these distinct conditional subbills included exactly once. The logarithm is not discarded: the formula in section 2 bounds the post-KL bill explicitly.

On the positive-mean core subfamily (a<=1), mu_s=d_s and the unrebated weighted rarity sum is exactly

    p a [r(r+1)/2+r log2(1/a)].

The weighted KL credit is this expression minus the exact signed J_tree. Thus its quadratic-in-r part is created and consumed within this one control-event account. At a>1 only the last node needs the separate minority endpoint above. This last correction is why simply extending A021's balanced formula by renaming mu would be invalid.

## 4. Direct full-entropy bound for biased activation

Let m=Eg=1-a and use 0log0=0. The empty Fourier coefficient of F is 1-pa; at empty data/nonempty controls it is -pa times the point character; at nonempty data it is p ghat(T) times that character. Summing the actual squared spectrum, with signs retained, gives

    H(F)=pH(g)+2rp a(2-pa)
       +p m^2 log2(m^2)-(p-p^2)a^2 log2(a^2)
       -(1-pa)^2 log2((1-pa)^2).

This is valid for m negative and at all constant endpoints. The m term is nonpositive. The last term is at most 2cpa, by -ln(1-t)<=t/(1-t). For a>=1 the a term is nonpositive; for 0<a<1 its upper bound is 2pa[a log2(1/a)]<=2cpa/e. Therefore

    H(F)<=pH(g)+[4+2c(1+1/e)]rpa < pH(g)+8rpa.

The strict numerical constant follows from c<81/56 and e>65/24: 2c(1+1/e)<7209/1820<4. This improves the conservative mismatch-ledger constant but does not replace the requested J_tree certificate. If H(g)<=C0 I(g), then H(F)<=max(C0,8)I(F); the full sufficient mismatch ledger is <=max(C0,12)I(F). Arbitrary cores still require an actual terminal certificate.

## 5. A complete unbounded family: activated arbitrary bent point-surgery selectors

Let b be any bent function on even k>=4 bits, v any vertex, delta=2^-k, s=b(v), b'=b-2s1_{x=v}, and let t choose b or b' fairly. Define g(x,t) as this selector core, and F=1+A_r(g-1), with arbitrary r>=1. Bent flatness gives I(b)=k/2. Flipping v changes influence in coordinate i by 2delta b(v)b(v^i), since precisely one undirected edge changes status. Consequently

    I(g)=delta+(I(b)+I(b'))/2 >= k/2-(k-1)delta >=7k/16.

Every distribution on the core's 2^(k+1) Fourier labels has H(g)<=k+1<=5k/4. Thus H(g)/I(g)<=20/7<3, a direct terminal certificate. Each child's H is at most k; no threshold or read-once membership is assumed. The exact mean is Eg=Eb-delta s, with |Eb|=sqrt(delta); hence 11/16<=a<=21/16.

The control-first tree therefore has

    J_tree+pH(g) <=7rpa+3pI(g)<=7I(F),
    J_tree+3c sum w_s mu_s+pH(g)<=12I(F),
    H(F)<=8I(F).

The rare point-surgery selector is not queried on inactive paths. On the active leaf its entire entropy, including the surviving kdelta selector logarithm, is paid once by the core account pI(g). That account is not also used for a separate selector bill. In particular r=2k and the quadratic b at v=0 is exactly the accepted B05 sparse-bent obstruction, with its local bad ratio fully absorbed in this complete tree.

## 6. Selector-first complete tree and comparison

Query t at the root, then query controls in each child, stopping on their first mismatch, with terminals b or b'. Let a_*=(1-Eb+1-Eb')/2=a and Ibar=(I(b)+I(b'))/2. Root disagreement is d=pdelta. Because the root children differ at exactly one point of the (r+k)-cube, every Fourier ratio is an even integer: an integer Walsh sum of 2^(r+k) signs is even. Thus the signed mismatch e=d^2 is the minority in every packet, mu=d. Its exact bill is sum_T e log(Q/e), and its KL representation implies

    J_root<=d log2(1/d)=pdelta(r+k).

The two child control-tree bills average to at most 7rpa. Their expected terminal entropy is p[H(b)+H(b')]/2<=pk. Since a>=11/16>=delta, the r part of J_root is <=rpa. Since Ibar>=k/2-kdelta>=7k/16, its k part is <=(16delta/7)pIbar, and terminal entropy is <=(16/7)pIbar. Therefore, for k>=4,

    J_selector-first+terminal <=8rpa+(17/7)pIbar<=8I(F),
    I(F)=rpa+pIbar+pdelta.

The full 3c mu allowance is <=3c(rpa+pdelta), so full sufficient ledger<=13I(F). Influence accounts here are distinct: root selector pdelta; queried controls rpa; terminal data pIbar. The selector bill uses additional control/data allowances once; the stated constants include these extra debits. No assertion that selector-first is optimal is made. Both actual complete trees are linearly paid although the isolated selector is not paid by its own influence with a universal constant.

For the original positive quadratic b at zero, Ibar=k/2+kdelta, Eg=sqrt(delta)-delta, and I(g)=k/2+(k+1)delta. These identities are checked exactly. Terminal-entropy placement differs: control-first leaves the full selector core; selector-first retains the root selector bill and leaves its two children. The entropy difference is exactly the core's own restriction decrement, multiplied by p, so neither tree silently omits it.

## 7. Multiple events and descendants: disjoint product extension

For any finite number M of independent components of section 5, let f=product_(j=1)^M F_j. Process components in fixed order, querying a component's controls until it fails or activates, leaving its certified core unqueried; continue until every component is resolved. The tree has depth at most sum r_j. Its leaves are products of the active cores and constant signs. A core is activated with probability p_j. Entropy and influence of disjoint products add by tensor Fourier factorization.

At a node querying component j, child Fourier coefficients are x_T b_R,y_T b_R. Their Q and m are multiplied by b_R^2; the ratio Q/m is unchanged, and sum_R b_R^2=1. Thus J, mu and queried influence are precisely the component's quantities, even with earlier terminal cores and later unresolved components present. Averaging over earlier histories restores the original reach weights for component j. Hence total J and expected terminal entropy are the sums of the component bills, and all bounds in sections 5-6 add. The simultaneous rarity events never share an account or a physical coordinate. This proves the stated unbounded-dimensional, unbounded-component family, rather than merely finitely checking a quadratic example.

First unsupported universal line: every arbitrary Boolean f admits such a controlled-event decomposition, or another physical stopping rule with the same complete linear bill and uniformly certified terminal cores. Neither is proved. Allowing arbitrary g in section 2 without its terminal certificate leaves pH(g) unpaid; the threshold paper's Corollary 8.10 explains why this cannot be treated as a negligible remainder.

# executed validation with domain, arithmetic, commands and outputs

Frozen before execution: out/FROZEN_SPEC.json, helper A023-v1. All 276 Boolean cores in dimensions n=1,2,3, each activated at r=1,2,3: 828 cases, no symmetry reduction. Additional 9 comparisons use quadratic bent k=2,4,6 and r=1,2,3, with 18 auxiliary child activation checks. Dimension k=2 is an endpoint test outside the stated k>=4 family theorem. Max actual truth-table dimension is 10. Runtime estimate 60 seconds, memory estimate 20 MB; no heavy job, randomness, GPU or dimension escalation.

Command from A023: `python -X utf8 runs\20261011T221608Z-account05-A023-amortized-rarity-budget\code\check.py`.

Result: 837 primary cases, 44,452 exact assertions PASS; observed Python runtime 3.929812300018966 seconds. Integer FWHT and Fraction edge counting check each coefficient, all influences, exact activation entropy, signed/magnitude endpoint distinction, fair-tree entropy telescoping and surgery core influence. Entropies and J equalities are rational combinations of prime logarithms; equality is certified by identical vectors, without assuming prime-log linear independence. out/validation.json saves both query orders' exact J vectors for the surgery grid. Universal signs and constants come from the analytic proofs, not decimal evaluations.

The independent A021 review is recorded in REVIEW_A021.md. It reconstructs both version-1 statements using this separately implemented raw-truth-table checker and analytic series/tail arguments. Review is local and source-bound; it does not modify another agent's files or the shared registry.

# proof dependencies and changed downstream conclusions

The new claim is self-contained: Boolean Walsh expansion, Parseval, exact minority/KL definition, the scalar Hellinger/JS proof in section 1, elementary logarithm bounds and exact influence edge counting. A021 and A022 are context/interface inputs, not unreviewed mathematical premises of the new theorem. Baseline balanced activation is credited to threshold Proposition 8.9. No percolation result or B09 theorem is used.

A021's two claims are locally independently accepted without repair in the separate review record. This satisfies the protocol's instruction to prioritize independent review when the stream has two source-complete pending candidates; A023 opens one consolidated family claim after that reconstruction. Shared-index adoption and the ultimate stream queue remain B20's responsibility.

Changed downstream conclusions: A029/A028/A064/A065 now have a complete first-revelation control account valid for biased cores, a guarded negative-mean endpoint, and both complete sparse-surgery tree orders, including terminal cost. The elementary terminal bound is not claimed as a new hard FEI theorem; the contribution is the explicit nonreusing KL tree payment and its extension to multiple rare events with independently varying dimensions/rarities.

# one next mathematical action and independent reviewer

Next: A029/A064 should test an overlapping pair of rare controls sharing one data core, keeping the existing terminal account and deriving the exact correction for assigning a physical coordinate to more than one event. Use two explicit control subcubes first; do not extrapolate disjoint tensor additivity. Independent reviewers: A087 for first-revelation/magnitude conventions and A094 for all endpoint inequalities and the product-tree factorization. No messages were sent externally.

# actual persistence receipts or precise save blocker

Local artifacts: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, REVIEW_A021.md, FIRST_REVELATION_LEDGER.md, code/check.py, code/save_metadata.py, frozen spec, exact validation, source receipts, schema check and SHA256 persistence receipts. STATUS.md, WORKLOG.md and LEARNED.md are current in A023. Every write is inside the assigned A023 workspace. Supervisor copying, GitHub/Brain mirrors, external review of the new claim and actual downstream use are not verified here.

**Universal bridge:** This stage moves C019 stopping-tree payment from balanced single-core activation to arbitrary-bias control paths with a complete minority/KL bill below 7 times their exclusive queried influence, including the last-node sign correction, and closes the full sparse-bent-surgery and disjoint multi-event family with terminal cost. Control-first and selector-first sufficient ledgers are respectively <=12I and <=13I; a direct entropy calculation gives H<=8I. What remains is a universal structural admission/stopping theorem, particularly payment when events share physical coordinates or terminal cores. The shortest next route is an exact overlapping-event account correction, because disjoint rarity and all terminal costs are now paid and only physical-budget sharing obstructs transfer; another isolated rare-family computation would not address that universal gap.
