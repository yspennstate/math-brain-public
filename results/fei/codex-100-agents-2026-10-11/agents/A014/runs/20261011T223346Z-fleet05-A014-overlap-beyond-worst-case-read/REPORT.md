# A014 — interference congestion with a paid exceptional mass

## exact target, quantifiers, hypotheses and units

Run: `20261011T223346Z-fleet05-A014-overlap-beyond-worst-case-read`, B03, A014. Full FEI remains OPEN. This stage proves the general interference lemma requested in B03 lead notes v1, supplies a complete queue-cost criterion, checks PP2 and PP3 exactly, and proves an L2 repair paying the PP_q rank/rarity bill for every prime q. Independent review is pending. The complete unbounded-read calibration is addressing, an already established FEI class; no new complete class theorem or priority claim is made.

All cubes are uniform; outputs are +/-1; Fourier coefficients are probability-normalized; entropy and all displayed costs use bits. Let f be an OR of N nonconstant Boolean gates h_l, each a combination of at most M regular functions. Let R_l be its relevant support, p_l=P(h_l=1), pi_l=min(p_l,1/2), b_l=log2(1/pi_l), a=6/5, gamma=120/11. Remove false constant gates; a true constant gate makes f constant and immediate. Set p(A)=fhat(A)^2, v=Var(f), I=sum_A |A|p(A).

For j with alpha_j=Inf_j(f)>0, partition d_j f into disjoint signed {0,+/-1} pieces d_jl by the least gate containing j that is pivotal when f is pivotal. Set alpha_jl=||d_jl||_2^2 and alpha_j=sum_l alpha_jl. Omit zero pieces. Define

    nu_j(T)=dhat_j(T)^2/alpha_j,
    rho_j(T)=sum_l dhat_jl(T)^2/alpha_j.

Both are probability laws. For A=T union {j}, let

    F_lj(A)=min_r ln[r_lr(j)/(|A intersect U_jlr|+1)],
    G_jl(A)=(a/ln 2) F_lj(A)+b_l 1[|A intersect R_l|<b_l/gamma],
    G_j(A)=min_{l:j in R_l} G_jl(A).

These are nonnegative. Let Gmax_j=max_T G_j(T union {j}). For any fixed kappa_j>=1 define the dimensionless exceptional mass

    epsilon_j(kappa_j)=sum_T (nu_j(T)-kappa_j rho_j(T))_+.

Zero denominators contribute zero: rho(T)=0 implies every piece amplitude and their sum vanish. No H(f) or assumed FEI inequality enters these definitions.

**Interference lemma.** For every such union and all choices kappa_j>=1,

    E_nu_j G_j <= E0+(24/5)log2 M+(24/5)log2 kappa_j
                  +epsilon_j(kappa_j) Gmax_j,                       (1)

where E0=(24/5)[log2(sqrt(2e)+2^(3/5))+log2 e]. The worst-event value is max_T nu_j(T)/rho_j(T), in which case epsilon_j=0. A smaller kappa is legal only with its explicit exceptional payment.

**Complete criterion.** Choose a global 0<lambda<=1 and the finite forest witness described below, using an assignment minimizing G_j. Write F(A) for the visited gates, s_l=|A_l|, ell_l=|A intersect R_l|. Let roots(A) be its roots and J_e the attaching coordinate of child edge e. Set

    Lambda_lambda=sum_l log2(1+lambda pi_l),
    S(A)=a sum_{l in F(A)} s_l log2(ell_l/s_l),
    L_lambda(A)=|roots(A)|log2(1/lambda)+sum_edges e log2 k_{J_e},

where k_i counts gates relevant to i. The following fully specified spectral congestion is sufficient:

    Gamma = [h2(v)+v Lambda_lambda+sum_{A!=empty}p(A)(S(A)+L_lambda(A))
              +(24/5)sum_j alpha_j log2 kappa_j
              +sum_j alpha_j epsilon_j(kappa_j)Gmax_j]/I.          (2)

For nonconstant f,

    H(f) <= [K0+E0+(29/5)log2 M+Gamma] I(f),                     (3)
    K0=120/11+3+2log2 3+log2(6e).

In particular the conservative bound K0+E0<218/5 is sufficient. This replaces all three worst-read costs by actual normalized root/label, subset, and interference bills. It does not assert a bound on Gamma for arbitrary unions. Gate/root names, normalization, and rarity are retained.

## sources actually read, revisions and theorem locators

Execution protocol `fei-execution-protocol/2`, revision `2026-10-11-execution-v2`, read in full. Read README, CURRENT_STATUS, claim and obstruction registries, packet statuses, stream next actions and the plan's A014 contract and relevant joint-cost discussion. Large concatenated initial reads were truncated; source use is confined to the separately displayed relevant passages, not an asserted exhaustive audit of every line of the plan. Read campaign CAMPAIGN/CLAIMS/COUNTEREXAMPLES/NATIVE_MAPPING, the effective-piece seed lemma (SEED_LEMMAS section 1), and curated overlapping-product/log-allocation notes. Reviewed the three earlier B05/B09/B19 run reports for source scope; their theorems are not premises for (1)-(3).

Read BOARD snapshot 2026-10-11 22:26 UTC and B03 STREAM_NOTES v1, 22:30 UTC. The lead directs A014 to interference and PP2/PP3, leaving the full PP family analysis to the lead. **Specific disagreement:** least-pivotal-gate PP pieces are unequal, and the proposed worst-event kappa is unbounded, even though their masses become asymptotically equal. No peer file was modified.

Main mathematical source: `context/threshold_paper_38pp.txt`, Section 5, Theorem 5.1, Lemma 5.3, equations (30)-(37), and its source-exact copy `research_pushes/2026-10-11-full-fei-100-agents/baseline/current-threshold-paper.tex`. The text extraction obscures square-root signs; the TeX establishes B_*=sqrt(2e), not 2e, in the rank tail. Our conservative rounding also remains valid with the larger 2e. Read the earlier 29-page threshold introduction and both percolation introductions/theorem statements for scope; no percolation theorem is used. Source hashes and actual file lengths are recorded in `out/receipts.json`.

The proof uses the manuscript's signed-antichain rank tail and fixed-noise rarity tail, not the mass-only K_eff refinement. The refinement remains a valid baseline but gives no constant when equal piece masses spread over many pieces.

## complete derivation or exact first unsupported line

### 1. Proof of the interference lemma

For a piece d_jl, Section 5.4 gives the rank tail

    nu_jl(F_lj>t) <= M sqrt(2e) exp(-t/2),

and Lemma 5.3 gives

    nu_jl(ell_l<b_l/gamma) <= 2^(3/5) 2^(-5b_l/12).

If G_j>u then G_jl>u. Splitting its two nonnegative summands at u/2, with a=6/5, yields

    nu_jl(G_j>u) <= M (sqrt(2e)+2^(3/5)) 2^(-5u/24).             (4)

For the rarity event to contribute, b_l>u/2, so its probability has precisely the same exponent as the rank term. Weighted averaging with weights alpha_jl/alpha_j gives (4) for rho_j, with no read factor. These weights sum to one because physical supports are disjoint. Piecewise orthogonality alone without the source tail hypotheses would not establish (4).

Let delta_j(T)=(nu_j(T)-kappa_j rho_j(T))_+. Then for every E,

    nu_j(E) <= kappa_j rho_j(E)+delta_j(E).

Layer-cake integration over 0<=u<=Gmax_j gives

    E_nu_j G_j <= integral_0^infty min{1,kappa_j M A0 2^(-beta u)}du
                  +sum_T delta_j(T)G_j(T),

where A0=sqrt(2e)+2^(3/5), beta=5/24. To justify the minimum, nu(E)<=1 and nu(E)<=kappa rho(E)+delta(E) imply nu(E)<=min(1,kappa rho(E))+delta(E). The integral equals beta^(-1)[log2(kappa M A0)+log2 e], since kappa M A0>=1. Bound the last sum by epsilon_j Gmax_j. This proves (1). The sharper sum delta_j(T)G_j(T) can replace epsilon_j Gmax_j throughout.

A spectral-block sufficient condition is also useful. Suppose the fine pieces can be partitioned into groups of at most b pieces, and the sums D_B=sum_{l in B} d_jl have pairwise disjoint Fourier supports. At each T at most one grouped sum is nonzero, so

    dhat_j(T)^2=|Dhat_B(T)|^2 <= b sum_{l in B} dhat_jl(T)^2
                                          <= b sum_l dhat_jl(T)^2.

Thus kappa_j=b, epsilon_j=0 is valid. Fine-piece spectra need not be disjoint; cancellation inside a group is allowed. This criterion is different from merely assuming orthogonality in L2.

### 2. Proof of the complete queue criterion

Use the manuscript queue law, replacing the global root odds pi_l/k by lambda pi_l; retain subset selection, sizes, child counts and multisets. At attaching coordinate i choose uniformly among its k_i gates. The law remains a subprobability, since only successful finite runs contribute.

For each nonzero A, choose tau(j) minimizing G_jl(A), allowing a fixed deterministic tie rule depending on A; A_l={j:tau(j)=l}. Choose the manuscript directed spanning forest. Source components furnish roots. Distinct root supports intersect A in disjoint subsets, by the source-component argument in Section 5.3. The prescribed queue run visits each gate exactly once and outputs A.

Its root bill is Lambda_lambda+sum_roots[b_r+log2(1/lambda)]. Dense-root b_r's sum to at most gamma |A|, because b_r<=gamma ell_r and root intersections are disjoint. Each nondense root owns a variable, and its b_r is paid from the selected variable's G_j. All subset rank terms plus these sparse-root bills are therefore bounded by sum_{j in A}G_j(A), plus the dense-root charge gamma|A|.

The elementary symmetric normalizer obeys Z_s^l<=(6eM)^s. For an assigned variable i, its predecessor count plus one is <=ell_l, whence the subset weight bill is bounded by

    (a/ln2) F_li(A)+a log2(ell_l/s_l).

Summing gives |A|log2(6eM)+the rank bills+S(A). Size choices cost at most |A|log2 3. Child-count choices cost at most |A|(1+log2 3), since |F|<=|A| and sum c_l=|F|-|roots|<=|A|. Multisets cost at most 2|A|. Child gate choices cost exactly the child portion of L_lambda. Thus the probability of this one successful run supplies

    log2(1/Q1(A)) <= Lambda_lambda+(K0+log2 M)|A|
                     +S(A)+L_lambda(A)+sum_{j in A}G_j(A).       (5)

Set Q(empty)=1-v and Q(A)=v Q1(A) for A nonempty. Gibbs' inequality, with the empty atom handled exactly, gives

    H(f)<=h2(v)+sum_{A!=empty}p(A)log2(1/Q1(A)).

Also sum_{A:j in A}p(A)G_j(A)=alpha_j E_nu_j G_j by the derivative/Fourier identity. Average (5) and substitute (1). This proves (2)-(3), including v Lambda_lambda; no root normalizer has been dropped.

For a simple exact conservative constant, e<3, log2 e<3/2 (ln2>=2/3), log2 3<8/5 (3^5<2^8), and 6e<18<2^(9/2) give K0<22. Also A0<8 gives E0<(24/5)(3+3/2)=108/5. Hence K0+E0<218/5. We make no claim of sharp constants.

### 3. Explicit unbounded-read calibration with every charge bounded

For each integer a>=1 let m=2^a and

    f_a(x,y)=y_x,                 x in {0,1}^a, y in {-1,1}^m,
    h_u=1 iff (x=u and y_u=+1).

These m gates are regular oriented conjunctions, M=1, and their OR is f_a. Every selector belongs to m gates, so worst read k=m tends to infinity. Use the same desirability order in each conjunction: selectors in their common physical order, followed by its data coordinate. A Fourier set has exactly one data coordinate y_u and any selector subset T. For each selector j the rank expression is identical across all gates, while ell_u is one larger than ell_v for v!=u, so its rarity charge is no larger. Therefore assigning the entire A to u minimizes all G_j; choose u on ties. This gives a one-gate, one-root witness. Then S(A)=0 and L_1(A)=0 for every nonzero Fourier set. Note that the root's gate identity is paid through its independent root odds, not discarded.

Here pi_u=2^(-a-1), and

    Lambda_1=m log2(1+1/(2m)) <= (1/2)log2 e.

The function is balanced, v=1 and h2(v)=0. Its spectrum has exactly 2^(2a) coefficients of squared magnitude 2^(-2a), namely A=T union {y_u}. Thus H=2a, I=1+a/2; these identities are established controls, reproduced here rather than advertised as new class results.

For a data coordinate, there is one pivotal piece, so kappa=1. For a selector j, group the gates into neighboring address pairs u,v differing only at j. At a pivotal input exactly one of those two gates changes, and the two fine signed pieces are

    d_u = indicator(other address)*indicator(y_u=+1,y_v=-1),
    d_v = -indicator(other address)*indicator(y_u=-1,y_v=+1).

Up to the sign fixed by the j orientation their sum is

    D_{uv}=indicator(other address)*(y_u-y_v)/2.

Every nonzero Fourier index of D_{uv} contains exactly one of its two private data coordinates, hence different pairs have disjoint Fourier supports. The block criterion gives kappa_j=2, epsilon_j=0 for every selector, uniformly in a. Each selector has influence 1/2, so

    Gamma <= [(1/2)log2 e+(24/5)(a/2)]/(1+a/2)
           < 3/4+24/5.

Equation (3) gives H(f_a)<50 I(f_a) for all a. All label/root/subset/rank and normalizer costs are included. The original worst-read theorem gives 41+7a, which diverges; the new criterion is constant. The known exact H/I=4a/(a+2)<4 is stronger, and remains the preferred bound on addressing. The new information is the explicit bounded interference certificate within the complete queue criterion, not a new addressing theorem.

### 4. Exact PP tests and analytic obstruction to worst-event congestion

For prime q, use normalized nonzero triples over F_q as points and normal vectors; a line consists of triples orthogonal to its normal. There are n=q^2+q+1 points/lines, each line has q+1 points, each point lies on q+1 lines, and distinct lines meet once. PP_q is OR over all line conjunctions. Each line is a monotone minterm: on its own point-set assignment no other line is contained. Every monotone DNF representation therefore contains all lines, so the monotone-DNF minimum read is at least q+1. This assertion is deliberately limited to monotone conjunction covers.

Fix j. There are m=q+1 incident lines. Let A_l mean that all q other points of incident line l are positive; P(A_l)=2^(-q). These q-point sets are disjoint across the incident lines. Let B_r mean a nonincident line is all positive; there are q^2 such lines. The least-gate piece l is exactly A_l, none of the earlier A_t, and none of the B_r. For any t!=l,

    P(A_l intersect A_t)=2^(-2q).

Each nonincident line meets incident line l in one of its q other points, so its conjunction with A_l also has probability 2^(-2q). A union bound proves

    2^(-q)[1-(q^2+q)2^(-q)] <= alpha_jl <= 2^(-q).               (6)

The lower bound can be negative at small q; its asymptotic use is restricted to delta_q=(q^2+q)2^(-q)<1. All pieces are positive indicators. Hence their empty Fourier coefficients are alpha_jl and the sum's empty coefficient is alpha_j=sum_l alpha_jl. At this singleton Fourier event,

    nu_j(empty)/rho_j(empty)=alpha_j^2/sum_l alpha_jl^2
                    >= (q+1)(1-delta_q)^2 -> infinity.          (7)

Thus no uniform bound on the lead's worst-event kappa is possible for PP_q. This is an actual Boolean family refuting that congestion helper, not FEI. The equal-mass premise is false for the exact least-gate partition, but asymptotic equal masses make the obstruction stronger, not weaker.

Exact all-coordinate results:

| Family | I | least-gate masses for each coordinate (ordered) | max kappa |
|---|---|---|---|
| PP2 | 63/32 | 7/64, 3/32, 5/64 | 162/55 |
| PP3 | 5005/2048 | 107/2048, 199/4096, 185/4096, 43/1024 | 3698/925 |

PP2's maximum is realized at the empty residual Fourier index. PP3's empty ratio is 296450/74603, slightly below 3698/925: other events are also nearly maximally coherent. Exact epsilon(1), epsilon(2), rank expectation intervals and tail-event ratios are in `out/check.json`. For q=2,3 every nonempty incident intersection has ell>=1>b_l/gamma, so rarity is identically zero and the listed rank-only intervals are the full G statistic for the canonical sorted line order. This simplification is not extrapolated to large q.

### 5. L2 perturbation repair: PP rank term paid for every prime q

The failed zero-error helper admits a quantitative repair. The following general lemma does not require ideal pieces to have disjoint physical supports. Suppose ideal functions a_l have at most one nonzero Fourier coefficient at each index outside an exceptional index set E. For the actual disjoint physical pieces d_l put e_l=a_l-d_l, e=sum_l e_l, d=sum_l d_l and alpha=||d||_2^2. At T outside E, write a=sum_l a_l. Then

    dhat(T)^2 <= 2 ahat(T)^2+2 ehat(T)^2
              <= 4 sum_l dhat_l(T)^2
                   +4 sum_l ehat_l(T)^2+2 ehat(T)^2.              (8)

The second inequality follows because only one ideal amplitude is nonzero; for that index, |ahat_l|^2<=2|dhat_l|^2+2|ehat_l|^2. Consequently,

    epsilon(4) <= nu(E)+[4 sum_l ||e_l||_2^2+2||e||_2^2]/alpha.   (9)

Both the pointwise inequality and the L2 bill are explicit. No comparison of entropies of coherent and incoherent spectra is used.

For PP_q, let a_l=indicator(A_l) from section 4. Each a_l depends on its own q-point block; these blocks partition all points except j. Its Fourier coefficients vanish outside that block. Thus the ideal pieces have disjoint Fourier supports except E={empty}. The actual d_l is a subindicator of a_l. With m=q+1, D=q^2+q and delta=D2^(-q), the same union bound as (6) gives

    ||e_l||_2^2=P(A_l and not piece_l)<=D2^(-2q),
    sum_l ||e_l||_2^2<=mD2^(-2q),
    ||e||_2^2<=m sum_l ||e_l||_2^2<=m^2 D2^(-2q).

The middle pointwise Cauchy-Schwarz inequality holds even though the error supports overlap. Since nu(empty)=alpha, (9) and (6) yield, whenever delta<1,

    epsilon_j(4) <= alpha_j+(4+2m)D2^(-q)/(1-delta).             (10)

All rank orders have ranks at most q+1 and rarity charges at most b_l=q+1, so

    Gmax_j <= q+1+(6/5)log2(q+1).                               (11)

For every integer q>=16, delta<=1/2: at q=16 it is 272/65536, and q(q+1)2^(-q) decreases thereafter. Moreover m<=2q, D<=2q^2, 4+2m<=3q and alpha<=2q2^(-q). Equations (10)-(11) give

    epsilon_j(4)<=14q^3 2^(-q),
    epsilon_j(4)Gmax_j <= (308/5)q^4 2^(-q)<=308/5.              (12)

The last inequality is exact: 16^4/2^16=1 and the successive ratio ((q+1)/q)^4/2<1 for q>=16, since 17^4<2*16^4. For q<16, epsilon_j(4)<=1 and (11) gives Gmax_j<=104/5, so the same bound 308/5 holds. The small-q argument does not use a positive lower bound in (6).

Thus, for every prime q, every coordinate admits the **fixed choice kappa_j=4** and the all-dimensional paid bill

    sum_j alpha_j epsilon_j(4)Gmax_j <= (308/5)I(PP_q).

Substituting in (1), with M=1, gives

    sum_j alpha_j E_nu_j G_j <= [E0+356/5]I(PP_q) < 93 I(PP_q). (13)

The constant is conservative; (12) decays exponentially for large q. This proves a rank/rarity congestion replacement with unbounded actual read q+1 and bounded exceptional bill, even though zero-error worst-event congestion diverges. It uses spectral concentration of the **error of private-block ideal pieces**, not concentration of the masses of the actual pieces. The lead's equal-mass issue is therefore bypassed.

**First unsupported line for the complete PP_q theorem:** one fixed reference and its minimizing assignment have h2(v)+v Lambda_lambda+E[S+L_lambda]=O(I(PP_q)), with a uniform constant. Equation (13) pays the remaining rank term outright. The lead owns those root/label/subset estimates; they are not consumed as proved facts here. In particular, (13) alone is not a complete PP FEI theorem and does not close the universal conjecture.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec precedes search in `FROZEN_SPEC.json`. Pilot q=2: 172 assertions, 0.05137 seconds. Fixed complete test: PP2 on 7 coordinates and 64 residual assignments each; PP3 on 13 coordinates and 4096 residual assignments each; addressing a=1,2,3 on all 3,6,11 coordinates. No coordinate symmetry reduction; no automatic dimension increase. Integer FWHT and rational spectra, physical piece support counts, exact normalizations, derivative influence, and exact pointwise congestion. Full test: **13,023 assertions PASS**, 8.62003 seconds reported inside Python. No heavy job or memory gate was needed; frozen memory estimate <100 MB.

Commands executed in A014:

    python -X utf8 runs/20261011T223346Z-fleet05-A014-overlap-beyond-worst-case-read/code/check.py --pilot --out runs/20261011T223346Z-fleet05-A014-overlap-beyond-worst-case-read/out/pilot.json
    python -X utf8 runs/20261011T223346Z-fleet05-A014-overlap-beyond-worst-case-read/code/check.py --out runs/20261011T223346Z-fleet05-A014-overlap-beyond-worst-case-read/out/check.json

All logarithm outputs use rational intervals: scale x to [1,2), write z=(x-1)/(x+1), and sum 2 sum_{t=0}^{27} z^(2t+1)/(2t+1). The omitted positive tail is at most 2z^57/[57(1-z^2)]. Scaling and division by ln2 use sign-aware rational endpoint arithmetic. These entropy/rank intervals are rigorous finite data, not the infinite-family proof. The proofs above supply the infinite statements. No floating entropy search is used; the only floating number reported is runtime.

The subsequent analytic L2 repair prompted a separate frozen validation, `L2_FROZEN_SPEC.json`, over the same PP2/PP3 coordinate domain, without dimension escalation. `code/l2_check.py` reconstructs actual and ideal pieces, checks private-block Fourier supports, every nonempty-frequency instance of (8), exact physical L2 error norms, and the scalar integer inequalities in (12)-(13). It passed **117,618 assertions** in **28.81131 seconds**; epsilon(4)=0 for both finite test orders, consistently with their congestion maxima being below 4. It reuses the Walsh helper and is author validation, not independent review. Combined fixed full checks: **130,641 exact assertions PASS**, plus the separate pilot.

    python -X utf8 runs/20261011T223346Z-fleet05-A014-overlap-beyond-worst-case-read/code/l2_check.py

## proof dependencies and changed downstream conclusions

Dependencies: published-source signed antichain and fixed-noise rarity tails; elementary queue subprobability/Gibbs; exact physical/Fourier identities. No unreviewed peer candidate, PP payment claim, percolation theorem, generic coherent entropy subadditivity, or assumption of full FEI is used. The K_eff mass-only lemma is not reproved.

Downstream: A006/A009 can substitute exact L_lambda and S bills; B03 lead can use (13) with all rank costs paid. A086/A094 should reconstruct (4), (5), the address-pair block argument, (6)-(7), and the L2 perturbation chain (8)-(13). Worst-event interference on PP is a rigorously failed route, repaired here with an explicit exceptional bill. General class criterion and all-q rank payment are proved on page but unreviewed; the packet's genuinely new complete unbounded-overlap class remains unfinished until the lead's root/label/subset proof is consumed.

## one next mathematical action and independent reviewer

Next mathematical action: consume the lead's source-complete PP root/label/subset estimates and substitute the unconditional rank payment (13), checking that they use the same minimizing assignment and fixed reference as (5). This is the shortest route to the stream's new complete overlap theorem now that the binding rank term is paid. Independent reviewers: A086 and A094; neither has reviewed this version. If the lead's remaining bills fail, generalize the private-block L2 repair to the exact failing witness, rather than repeating a mass-only estimate.

## actual persistence receipts or precise save blocker

All work is saved only inside A014: this REPORT, CLAIMS, PROGRESS, PACKET_DELTA, FROZEN_SPEC, L2_FROZEN_SPEC, code/check.py, code/l2_check.py, code/finalize.py, out/pilot.json, out/check.json, out/l2_check.json, out/receipts.json, and rolling STATUS/WORKLOG/LEARNED. Receipts list SHA256 and size of source inputs and saved artifacts, with report/source hashes bound in the claim record. Finalization validates protocol field sets and file sizes; the protocol's descriptive field `packet_ids (one primary ID, for compatibility)` is serialized as the specified compatibility key `packet_ids`. Supervisor copy, GitHub upload, Brain ingestion, independent acceptance, downstream use, and public release are **not claimed**. No git, mail, Brain writes, peer-folder writes, deletions or background helpers were used.

**Universal bridge:** This stage moves C020 whole-set witness cost by replacing the rank/read factor with normalized interference plus an explicitly paid exceptional term, while retaining the other two overlap charges and v Lambda. Addressing certifies all charges with unbounded read. PP_q blocks the zero-error helper, but the private-block L2 repair pays its complete rank/rarity term by less than 93I for all prime q. What remains is the lead's source-bound full label/subset/root payment on the same reference and assignment, followed by a broad Boolean representation with controlled ideal-piece errors. The next substitution attacks the only remaining bills in the stream's active family; the L2 certificate offers a reusable mechanism toward universal whole-set payment rather than another isolated known-class result.
