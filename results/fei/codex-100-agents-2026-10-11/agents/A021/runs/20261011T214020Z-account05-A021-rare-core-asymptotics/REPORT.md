# A021 / B05: uniform rare-core asymptotics and control-first debt

## exact target, quantifiers, hypotheses and units

For every balanced Boolean seed b on n independent uniform sign bits, every integer t>=1 and k>=1, put h=H(b), i=I(b), g_t=product of t disjoint copies of b, q=2^{-k}, A_k=indicator of the all-positive control point, and F_{k,t}=1+A_k(g_t-1). Dimension is k+nt. All H, KL, and logarithms are in bits; c=1/ln(2). The two parameters k,t remain independent throughout the identities and remainder estimates. The choice of control point changes Fourier signs only. The validation uses point zero in bit coordinates, equivalently the all-positive point after encoding.

Target: obtain exact entropy/influence/variance and control-first mismatch-KL debt, uniform remainders, and conditional necessary tests for an entropy-dominating influence-bounded global potential. This packet does not attempt a universal potential construction. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

The local campaign snapshot uses protocol revision 2026-10-11-execution-v2. Read EXECUTION_PROTOCOL.json in full, README.md, CURRENT_STATUS.md, claim and obstruction registries, the packet index (especially A021-A025), stream-next-actions, and the plan's A021 contract at lines 640-644. The plan and packet index were scanned for related dependencies. The BOARD snapshot is 2026-10-11 21:38 UTC; A021 had no earlier reported stage. Claude B05/STREAM_NOTES.md was absent at the specified path; no direction was inferred from that absence.

Mathematical source passages inspected:

- threshold_paper_38pp.txt, Section 8.4, Proposition 8.9 and Corollary 8.10 (text lines 2550-2622): exact activation and optimal-constant equivalence. Those are baseline, not new claims of this run. The earlier 29-page version was inspected for definitions/composition and searched for activation; it lacks this section.
- percolation_spectral_pivotal_entropy_30pp.txt, introduction, Theorems 3.1-3.2; the 31-page alternate version's introduction and statement map. Their geometry-specific entropy bounds are not dependencies here. In particular a pivotal-set lower bound is not a spectral entropy payment.
- Supplemental CAMPAIGN.md, CLAIMS.md (C013), COUNTEREXAMPLES.md (X011), SEED_LEMMAS.md (Section 3), NATIVE_MAPPING.md, and sources/ROUTE_MAP_CURATED.md Section 2.1. The latter records the mismatch/KL theorem with magnitude mismatch M, the residual M[log(1/M)-D_2(nu||Q)], and the separately paid 3M/ln2 term. Its unbundled original theorem was not fetched; our exact family identities below are derived directly and do not rely on that original proof.
- Archived B05 REPORT.md at run 20261011T193057Z-account01-B05-rare-restrictions, Sections 1-7, and B19 independent-review REPORT.md at run 20261011T195038Z-account01-B19-independent-review, Sections 2-5. Accepted baseline: the sparse bent surgery defeats fixed-price local variance refunds, not FEI or chosen trees. We do not repackage that no-go as a new result.
- Archived B09 report and registry navigation were inspected for scope; none of its unreviewed lemmas is used.

Source hashes and byte-read inventory are in out/source_inventory.json. Inventory reads are provenance, not a claim of independent full-paper audit or external-source verification.

## complete derivation or exact first unsupported line

### 1. Exact spectrum and all entropy terms

Tensor independence gives H(g_t)=th, I(g_t)=ti, and E g_t=0. For a data set T and control set U, the indicator coefficient is q times a sign epsilon_U. Consequently:

- empty T,U: coefficient 1-q, probability (1-q)^2;
- empty T, nonempty U: coefficient -q epsilon_U, probability q^2, multiplicity 2^k-1, total mass q-q^2;
- nonempty T and arbitrary U: coefficient q epsilon_U ghat_t(T), probability q^2 ghat_t(T)^2, total mass q.

These masses sum to one. No incoherent approximation or Boolean realizability assumption enters. Summing -p log p over the three classes gives

    H(F)=qth+B_k(q),
    B_k(q)=(4q-2q^2)k+b(q),
    b(q)=-2(1-q)^2 log(1-q).

In detail, the data-class entropy is qth+2kq, pure-control entropy is 2k(q-q^2), and constant-atom entropy is b(q). Every data influence is q times its core influence. A control bit is pivotal if the other k-1 controls match and g_t=-1, probability 2^{-(k-1)}/2=q. Hence

    I(F)=q(ti+k), E F=1-q, Pr(F=-1)=q/2,
    V=Var(F)=2q-q^2.

The spectral empty/nonempty split can also be retained exactly:

    H(F)=h_2(V)+V H(S | S nonempty),
    H(S | S nonempty)=[qth+B_k(q)-h_2(V)]/V.

This prevents losing normalization or the constant atom by replacing full entropy with a conditional spectrum. For any 0<v<1,

    h_2(v)=v log(1/v)+cv-cv^2/2+R_v,
    -cv^3/[6(1-v)] <= R_v <= 0.

Proof: -(1-v)ln(1-v)=v-sum_{j>=2}v^j/[j(j-1)], and the tail coefficients are at most 1/6. Substitution v=V is uniform in t; here V<=3/4.

### 2. Uniform expansion, with no restriction on tensor growth

Expanding the convergent logarithmic series for q<=1/2 gives

    b(q)=2cq-3cq^2+R(q),
    R(q)=-4c sum_{j>=3} q^j/[j(j-1)(j-2)],
    -2cq^3/[3(1-q)] <= R(q) <= 0.

The coefficients follow by multiplying sum q^j/j by 2(1-2q+q^2). All terms in R are negative, and their absolute coefficients are at most 2/3. Therefore, for every t,k,

    H(F)=q[th+4k+2c]-q^2[2k+3c]+R(q),
    I(F)=q(ti+k).

This is an absolute error bound independent of t, h, i, and seed dimension. In particular it does not require qt to be small. Let

    R0=(th+4k+2c)/(ti+k).

Then the exact ratio satisfies

    R0 - q(2k+3c)/(ti+k) - 2cq^2/[3(1-q)(ti+k)]
       <= H(F)/I(F) <= R0 - q(2k+3c)/(ti+k).

Since a balanced Boolean seed has i>=1 (Parseval on nonempty sets), these are uniform also over all balanced seeds. The correction is bounded independently of t by q(2+3c/k)+2cq^2/[3(1-q)k].

For a fixed seed, k->infinity and t/k->lambda in [0,infinity) imply

    H(F)/I(F) -> (lambda h+4)/(lambda i+1).

For t/k->infinity the limit is h/i. For t/k->0 it is 4. No convergence of t/k is needed for the uniform displayed interval. In the core-dominant small-influence regime k=o(t), qt->0, one has I(F)->0, minority probability ->0, and H(F)/I(F)->h/i. Example: t=k^2, q=2^{-k}.

For arbitrary nonconstant, possibly unbalanced f, use g_t=z product_{j=1}^t f_j instead. Then the same proof substitutes H(g_t)=tH(f), I(g_t)=tI(f)+1. Taking t=k^2 preserves H(f)/I(f), while influence and minority probability vanish. This reproves the baseline equivalence along a different explicit sequence; no new restricted endpoint is claimed.

### 3. Exact magnitude-mismatch/KL debt on a control split

At an active node with s>=1 controls remaining, set u=2^{-s}. Its children are constant 1 and an activation with s-1 controls and mask probability p=2u. The balanced core is unchanged. Denote the child Fourier coefficients a_W,b_W, packet law Q_W=(a_W^2+b_W^2)/2, magnitude mismatch m_W=(|a_W|-|b_W|)^2/4, mu=sum m_W, and nu_W=m_W/mu.

The all-empty packet has

    Q0=1-2u+2u^2, m0=u^2.

Every other nonzero packet has a_W=0, so m_W=Q_W/2. Thus mu=u and the remaining mismatch mass is u-u^2. This includes s=1, where the active child is the balanced core and Q0=1/2. Magnitude mismatch coincides with signed mismatch here because the empty child coefficient 1-2u is nonnegative and all other constant-child coefficients vanish. That coincidence is family-specific; magnitude mismatch and disagreement cannot be interchanged for general splits.

The full residual from the source theorem is therefore exactly

    J_s=mu[log(1/mu)-D_2(nu||Q)]
       =sum_W m_W log(Q_W/m_W)
       =u-u^2+u^2 log(Q0/u^2).

The KL credit is, explicitly,

    D_2(nu||Q)=s-1-u[2s-1+log Q0].

It is independent of t and of the balanced seed. The conditional packet entropy is exactly

    L_s=2(u-u^2)+Q0 h_2(u^2/Q0).

For s>=2, Q0>=1-2u and |log Q0|<=2cu/(1-2u)<=4cu. This yields uniform expansions

    J_s=u+(2s-1)u^2+E_s,       |E_s|<=4cu^3,
    L_s=2u+(2s-2+c)u^2+F_s,   |F_s|<=5cu^3.

For the second bound, write L_s=2(u-u^2)+u^2 log(Q0/u^2)+c u^2 minus a nonnegative tail bounded by c u^4/[2(Q0-u^2)]<=c u^4. Both errors in fact are nonpositive. The s=1 formulas are kept exact: J_1=1/2, L_1=1. They are not forced into a small-u expansion.

The physical entropy decrement is also exact and independent of t:

    Delta_s=B_s(u)-B_{s-1}(2u)/2, with B_0(1)=0.

At s=1 the active leaf's core entropy cancels separately and Delta_1=B_1(1/2)=2. This identity comes directly from Section 1 and needs no imported inequality. The source theorem's additive 3c mu term is a distinct, already linearly paid allowance; it is not part of J_s, and J_s is not the blind scalar mu log(1/mu).

For completeness its uniform small-u expansion, s>=2, is

    Delta_s=4u+(2s-4+3c)u^2+G_s,
    0<=G_s<=8cu^3/[3(1-2u)]<=16cu^3/3.

Indeed G_s=R(u)-R(2u)/2=4c sum_{j>=3}(2^{j-1}-1)u^j/[j(j-1)(j-2)] is nonnegative and at most |R(2u)|/2. Thus the entropy decrement, packet entropy and mismatch debt are each expanded uniformly in both parameters, with the final balanced-core split kept exact.

### 4. Exact control-first tree, nonreuse, and uniform tree asymptotics

Query each control, stopping immediately on the first mismatch. The active node with s controls remaining has physical reach probability w_s=2^{-(k-s)}=q/u. Inactive leaves are constant; the single fully active leaf is g_t and has reach q. The queried influence budget is exactly

    sum_s w_s mu_s=kq.

The unqueried leaf influence is qti, so I(F)=kq+qti: no unit is reused. Entropy telescopes exactly as

    H(F)=sum_s w_s Delta_s+qth=B_k(q)+qth.

Its complete mismatch debt is

    J_tree=sum_s w_s J_s=q[k+A_k],
    A_k=sum_{s=1}^k 2^{-s}[2s-1+log(1-2^{1-s}+2^{1-2s})].

For s=1 the bracket is zero. For s>=2, Q0>=1/2, so 2s-1+log Q0>=2s-2>=0; also log Q0<=0. Thus 0<=A_k<=sum_{s>=1}2^{-s}(2s-1)=3. The increasing sequence has a limit A in [0,3], and its tail obeys

    0<=A-A_k<=sum_{s>k}2^{-s}(2s-1)=(2k+3)2^{-k}.

Hence, uniformly in t,

    q(k+A)-q^2(2k+3) <= J_tree <= q(k+A),
    J_tree <= q(k+3) <= 4kq.

This closes the control-only mismatch payment for this family. If the source inequality Delta<=J+3c mu is used, the full upper ledger includes both J_tree+3ckq AND qth. The linear term is paid from queried control influence; terminal entropy requires a separate core payment from qti.

In contrast, the blind rarity charge sums to

    sum_s w_s mu_s log(1/mu_s)=q k(k+1)/2.

The exact weighted KL credit is the difference between this quantity and J_tree. Dropping it creates a factor of order k even on this ordinary balanced-core activation. This is not the sparse-bent surgery no-go and does not decide what tree is optimal for that different family.

### 5. Necessary potential tests, stated with their quantifiers

For any C and any functional P satisfying H(f)<=P(f)<=C I(f) on all these activations, necessarily

    P(F)/q >= th+4k+2c-q(2k+3c)+R(q)/q,
    C(ti+k) >= th+4k+2c-q(2k+3c)+R(q)/q.

Thus for every admitted seed, C>=h/i in the core-dominant regime and C>=4 in the control-dominant regime. A functional vanishing faster than qth when k=o(t) and h>0 cannot dominate entropy, even though I and minority probability vanish. The exact induction slack is

    C I(F)-H(F)
      =q[t(Ci-h)+(C-4)k-2c+q(2k+3c)]-R(q).

For C=h/i<4 and core-dominant t, the ratio still approaches C but the displayed finite-family slack is negative for all sufficiently large k. Limit ratio preservation must not be mistaken for inheritance of an exact finite constant.

For the specific tree potential T=J_tree+terminal_entropy, the terminal term is exactly qth. Its asymptotic coefficient is (lambda h+1)/(lambda i+1) for finite lambda=t/k, not the coefficient 4 of the actual entropy. If a proposed bound T<=K I is asserted for all these cores, it necessarily has K>=max(1,h/i). This is a conditional test of this explicit potential, not an assertion that every imaginable debt has that coefficient. Adding the separately paid 3c control allowance changes the selector coefficient to 1+3c and leaves the hidden-core obstruction unchanged.

Uniform FEI for this fixed-seed activation class follows, without any mismatch theorem, from b(q)<=2cq:

    H(F)/I(F) <= max(h/i,4+2c/k) <= max(h/i,4+2c).

The hidden seed ratio is fully retained. With arbitrary cores this is not an absolute bound, since a uniform h/i bound is exactly the missing FEI obligation.

First unsupported line toward full FEI: a dimension-independent bound on terminal H(g)/I(g) for arbitrary Boolean cores, or a new structural admission rule plus valid terminal payment. No such bound or rule is established here.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec: out/FROZEN_SPEC.json was saved before execution. Helper code/check.py v1 enumerates all 70 balanced 3-bit truth tables, t=1,2 and k=1,2,3: 420 actual Boolean functions, no symmetry reduction, maximum dimension 9. It independently builds truth tables, computes integer Walsh transforms and direct edge influences, and compares entropies as exact rational linear combinations of prime logarithms. The logarithm comparisons are equalities of identical symbolic vectors, not floating signs or presumed logarithm independence.

Command: `python -X utf8 runs/20261011T214020Z-account05-A021-rare-core-asymptotics/code/check.py` from A021. Output: out/validation.json, 3,220 assertions passed, 420 cases, 1.2464 seconds observed Python compute time. No floating-point entropy evaluation, random seed, GPU, heavy job, or automatic dimension increase was used. The all-parameter statements and remainder signs are proved analytically above; finite checks verify implementation and boundary cases only.

## proof dependencies and changed downstream conclusions

The new family results are self-contained consequences of Walsh expansion, tensor independence, Parseval and convergent logarithmic series. Threshold Proposition 8.9/Corollary 8.10 are credited baseline identities; the mismatch source is used to identify the intended debt, not to establish the family's formulas. The accepted B05 no-go supplies context, not a dependency. No B09 theorem or universal restriction claim is used. The global potential remains OPEN.

Changed downstream conclusion: A023/A026/A036/A040/A047/A048 now have an exact uniformly controlled two-parameter test and a complete control-only tree payment. In that test the KL rebate removes a quadratic-in-k rarity ledger, while arbitrary terminal entropy remains. The target is neither a new full-FEI proof nor a disproof.

## one next mathematical action and independent reviewer

Next action: A023 should reconstruct this control-first ledger on the accepted sparse-bent point-surgery family and compare selector-first queries, preserving magnitude mismatch and all terminal entropy. Independent reviewers requested through the saved artifact: A087 and A094, with special attention to the exact tree constant A, uniform remainder signs, and the distinction between signed and magnitude mismatch. No external message was sent.

## actual persistence receipts or precise save blocker

Saved locally in the assigned immutable run folder: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, RARE_CORE_EXPANSIONS.tex, POTENTIAL_NECESSITIES.md, code/check.py, frozen spec, validation and source inventory. Rolling STATUS.md, WORKLOG.md and LEARNED.md are local only. out/artifact_receipt.json records hashes/sizes after saving. Supervisor copying, GitHub/Brain mirrors, independent acceptance and downstream use are not verified by this run.
