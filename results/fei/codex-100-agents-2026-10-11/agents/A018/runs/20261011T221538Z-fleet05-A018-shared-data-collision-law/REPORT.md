# A018: shared-data collision law and posterior cancellation

Run: 20261011T221538Z-fleet05-A018-shared-data-collision-law. Stream B04. Packet A018.
Artifact complete locally; elementary proofs and exact author checks complete; independent acceptance pending. Full FEI remains OPEN.

## Exact target, quantifiers, hypotheses and units

Let a,n be arbitrary nonnegative integers, W a fresh physical selector block of a uniform binary coordinates, and y an independent uniform n-bit data vector. For every b in F_2^a, let g_b(y) be an arbitrary Boolean function on the same data cube. No balance, orthogonality, support separation, or data disjointness is assumed. Set F(b,y)=g_b(y), N=2^a, c_T(b)=hat(g_b)(T), and

R_T=N^{-1} sum_b c_T(b)^2.

For R_T>0 define

r_T(b)=c_T(b)^2/(N R_T),
nu_T(A)=(N^{-1} sum_b chi_A(b)c_T(b))^2/R_T.

These are normalized probability laws. Zero-mass T are omitted, including an empty T only when its mass actually vanishes. All entropies are in bits; physical influence uses Pr[F(z) != F(z with one bit flipped)]. Write

B_W=sum_T R_T H(nu_T),
M_W=a-sum_T R_T H(r_T),
Delta_W H=H(F)-N^{-1}sum_b H(g_b),
I_W=sum_{i in W} Inf_i(F).

The packet interface is

**Delta_W H=B_W+M_W, with 0<=M_W<=(2/ln 2) I_W.**

B_W is exactly H(S_W | S_data) for the parent spectral set. M_W is the mutual information of the physical branch label and data Fourier label under the auxiliary law P(b,T)=c_T(b)^2/N. It is not a conditional-label term that can be spent a second time.

The cancellation classification proved here is: M_W=0 iff all branches have identical squared Fourier coefficients at every T; B_W=0 iff every nonzero coefficient row c_T is a scalar multiple of one Walsh character of b. Therefore Delta_W H=0 iff every nonzero row is such a character. Common squared spectra alone are sufficient for complete cancellation when a<=1, but are insufficient when a>=2.

## Sources actually read, revisions and theorem locators

The governing source is EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2; its entire protocol was read. Campaign navigation used README.md, CURRENT_STATUS.md (snapshot 2026-10-11T20:06:24Z), CLAIM_REGISTRY.json, OBSTRUCTION_REGISTRY.json, PACKET_STATUS.json, STREAM_NEXT_ACTIONS.json, and FEI_100_agent_research_plan.tex, particularly B04/A018 acceptance tests and A019/A020's bent-splice guard. The initial BOARD.md is dated 2026-10-11 22:16 UTC. B04/STREAM_NOTES.md was absent when checked; no inferred lead instruction is asserted.

The mathematical baseline is threshold_paper_38pp.txt, Proposition 8.6, equations (75)-(79), and Corollaries 8.7-8.8. This already proves the collision identity and positive-energy closure. The older threshold_paper_29pp_earlier_version.txt supplies the preceding composition/tensorization context and has no Section 8 shared-data extension. The percolation 30-page and alternate 31-page text were consulted for scope and their product-entropy/local-irrelevance interfaces; none of their geometric or percolation theorems is used in this proof. This report does not claim a full independent audit of either paper.

The supplemental CAMPAIGN.md, CLAIMS.md, COUNTEREXAMPLES.md, SEED_LEMMAS.md and NATIVE_MAPPING.md were consulted; decisive controls are C018-C019, C035, X004-X006 and X009. sources/ISOSPECTRAL_SPLICING_CURATED.md Sections 2-5 already gives one-bit zero-cost isospectral splicing and the Hellinger/JS interfaces. Its original source is pinned at fe94de760ee2b47545419a7447b492816bd16045, blob 3421c0cbfd22031554befb962ec92cd0c8bb45b9. sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md is the block-interface context; sources/OVERLAPPING_PRODUCT_NOTE.md prevents an invalid shared-product substitution. The earlier B05 20261011T193057Z report and B19 20261011T195038Z independent reconstruction were consulted for the scope of the rare logarithm obstruction.

A017/LEARNED.md was read: its quadratic reused-address rank calculation and physical-versus-oblique influence warning are retained. A091/LEARNED.md supplies the terminal-scope guard. No pending claim from another agent is used as an accepted premise. Local source hashes are recorded in out/SOURCE_RECEIPTS.json. Earlier-run source readbacks are distinct from replaying their checkers.

## Complete derivation or exact first unsupported line

### 1. Collision and influence ledger

The exact coefficient is hat(F)(A,T)=N^{-1}sum_b chi_A(b)c_T(b). Parseval on the selector cube gives sum_A hat(F)(A,T)^2=R_T. Thus H(F)=H(R)+sum_T R_T H(nu_T), and I_W=sum_T R_T sum_A |A| nu_T(A).

For P(b,T)=c_T(b)^2/N, the branch marginal is uniform, the data marginal is R, and the posterior branch law is r_T. The chain rule gives

H(R)=a+N^{-1}sum_b H(g_b)-sum_T R_T H(r_T).

Subtract the branch average from the parent entropy to get Delta_W H=B_W+M_W. Also I_data(F)=N^{-1}sum_b I(g_b), by conditioning physical edge differences on b. Consequently total physical influence is I(F)=I_W+average I(g_b).

### 2. Posterior payment, with an elementary proof of the constant

Use natural-log entropy Ent(h)=E[h ln(h/Eh)] on a uniform cube. For real numbers s,t,

Ent_{one bit}((s,t)^2) <= (s-t)^2/2.

To prove it, replacing s,t by their absolute values can only reduce the right side. Normalize (s^2+t^2)/2=1 and interchange them so s^2=1+u, t^2=1-u, 0<=u<=1. The left side is ((1+u)ln(1+u)+(1-u)ln(1-u))/2; the right side is 1-sqrt(1-u^2). Their difference vanishes at zero and has derivative u/sqrt(1-u^2)-artanh(u), which is nonnegative since its own derivative is (1-u^2)^(-3/2)-(1-u^2)^(-1)>=0. Extend to u=1 by continuity, and rescale. If both entries vanish both sides are zero.

For a nonnegative h on a product cube,

Ent(h) <= sum_i E_{outside i} Ent_i(h).

Here is a direct finite proof avoiding an unproved tensorization invocation. Normalize Eh=1 and put P(z)=2^{-a}h(z). Then Ent(h)=ln 2 (a-H(P)). The ith conditional contribution is ln 2 (1-H_P(Z_i|Z_{-i})). The chain rule and conditioning inequality give H(P)>=sum_i H_P(Z_i|Z_{-i}), proving the assertion. Zero conditional masses contribute zero. The general case follows by homogeneity.

For each nonzero T let phi_T(b)=c_T(b)/sqrt(R_T), so E phi_T^2=1. Then

a-H(r_T)=Ent(phi_T^2)/ln 2
<= (2/ln 2) sum_i E[(D_i phi_T)^2]
= (2/ln 2) sum_A |A| nu_T(A),

where D_i phi=(phi(b)-phi(b with bit i flipped))/2. The last equality is Walsh Parseval. Multiply by R_T and sum T. Nonnegativity follows either from H(r_T)<=a or from M_W=I_P(branch;T). This proves the full posterior bound for arbitrary overlapping Boolean branches. The row estimate itself permits real rows, but a universal estimate for B_W does not follow from it.

### 3. Exact cancellation and the role of signs

Because H(r_T)<=a and all positive weights R_T are retained, M_W=0 iff each r_T is uniform. That is iff c_T(b)^2 is independent of b for every T, equivalently all branch squared spectra coincide.

Because entropy vanishes exactly for a point mass, B_W=0 iff each nu_T has exactly one occupied A. Inverse Walsh then gives c_T(b)=alpha_T chi_{A_T}(b), alpha_T!=0. This in turn forces r_T uniform, so B_W=0 implies M_W=0. Since both terms are nonnegative, Delta_W H=0 iff B_W=0 iff all nonzero coefficient rows have this character form. There need not be any affine relation between A_T and T; Boolean realizability of the given branches is still part of the hypotheses.

Identical branches give c_T(b)=hat(g)(T), r_T uniform, nu_T concentrated at A=empty, I_W=0, and H(F)=H(g). For a=1 every sign pattern on two entries is a constant times one of the two Walsh characters, so common squared spectra suffice; this recovers the archived isospectral splice rather than claiming it as new.

For arbitrary a, common squared spectra allow writing c_T(b)=alpha_T h_T(b), with h_T Boolean on the selector cube. In that case

M_W=0, B_W=sum_T alpha_T^2 H(h_T), I_W=sum_T alpha_T^2 I(h_T),
H(F)=H(common squared data spectrum)+B_W.

Thus the posterior label term cancels the entire literal a-bit alphabet cost, but the sign phases may still produce spectral entropy. Relative to the incoherent reference H(R)+a, coherence changes entropy by B_W-a<=0; relative to the branch-average baseline it adds B_W+M_W>=0. Statements about coherence 'adding entropy' must specify which baseline is being compared.

The actual Boolean example a=2, g_b(y)=(-1)^{b_1 b_2}y has identical branch squared spectra, M_W=0, and a single data row whose Walsh spectrum is uniform on all four A. Hence B_W=Delta_W H=2, I_W=1, I_data=1. All branch entropies are zero. For general a and any Boolean h, branches g_b(y)=h(b)y give H(F)=H(h), I_W=I(h), I_data=1. A uniform B_W<=K I_W on all common-spectrum branches would already imply full FEI for arbitrary h. This is the source-credited X005 guard, not a new counterexample to FEI.

### 4. Required bent-splice obstruction

Let m>=2 be even, delta=2^{-m}, and b(y)=(-1)^{y_1y_2+...+y_{m-1}y_m}. Its coefficient c_T has magnitude sqrt(delta); this follows by taking the product of the exact two-bit transform. Set b'(y)=b(y)-2 1_{y=0}. Both are Boolean, and the one-bit selector F between them has I_W=delta.

In every data fiber the two parent coefficients are c_T-delta and delta, so e_T=delta^2 and R_T=(c_T-delta)^2+delta^2. Write u=sqrt(delta)<=1/2. Then

R_T/e_T >= delta^{-1}(1-2u+2u^2) >= 1/(2delta).

Binary entropy obeys R_T h_2(e_T/R_T)>=e_T log_2(R_T/e_T). Summing all 2^m fibers gives

B_W >= delta(m-1), and Delta_W H/I_W >= B_W/I_W >= m-1.

The inference is valid whether or not e_T is the smaller mass. M_W still has the proved constant posterior payment; it cannot remove the nonnegative rare logarithm in B_W. Therefore no finite universal K satisfies either B_W<=K I_W or Delta_W H<=K I_W for all Boolean fresh-selector splices. This is a reconstruction of the archived guard; it does not refute total-influence FEI, good-block selection, or a paid stopping tree.

### 5. Exact open line and the universal interface

For any proper block W, a proposed next step needs to pay B_W=H(S_W|S_{-W}) using a nonreused physical budget or select W so that this payment is possible. The statement 'there exists a usable proper block or physical stopping tree with cumulative B_W cost <=K I(F)' is unproved here. Simply charging each node's B_W to that node's I_W is refuted by Section 4.

For a finite physical stopping tree whose internal nodes query disjoint-from-their-own-ancestor blocks, the entropy chain rule telescopes exactly:

H(root)=sum_internal pi_v(B_{W_v}+M_{W_v})+sum_leaves pi_leaf H(leaf).

Physical influence decomposes exactly as I(root)=sum_internal pi_v I_{W_v}(node)+sum_leaves pi_leaf I(leaf). Thus all posterior terms together cost at most (2/ln 2) times the selector portion of that decomposition. If a separate certificate pays sum_internal pi_v B_{W_v}<=K_B sum_internal pi_v I_{W_v} and all leaves have H<=C_leaf I, then H(root)<=max(K_B+2/ln 2,C_leaf)I(root). That certificate is an additional hypothesis, not a universal result. Overlapping numerical influence banks cannot be used twice. Zero-cost or common-spectrum nodes do not certify arbitrary leaves.

## Executed validation with domain, arithmetic, commands and outputs

The frozen specification is out/FROZEN_SPEC.json, helper A018-collision-v1. It was persisted before search. Command from A018:

`python -X utf8 runs\20261011T221538Z-fleet05-A018-shared-data-collision-law\code\check_collision.py`

Result: PASS, 31,794 assertions, 7.109 seconds measured by Python. Domain: all Boolean tables in dimension n=0,1,2,3 and all prefix selector block sizes, 1,082 block cases; all 276 signed common-literal phase tables on a=1,2,3; bent splices m=2,4,6,8,10,12. No automatic dimension escalation, GPU, heavy job, or random search. Estimated memory 60 MB; actual process peak memory was not instrumented. The 300 MB preflight threshold did not apply.

Walsh coefficients and influence use integers/Fraction. A separate direct character sum reconstructs FWHT on all n<=3 tables; edge disagreement independently checks physical influences. Entropy equalities are checked as exact rational linear combinations of log2(prime), not by floating subtraction. Inequalities use 36-term rational atanh expansions with positive geometric tail, reduction to [1,2), and sign-aware outward division. The displayed decimal entropies are presentation only. out/CHECK.json contains rational endpoints, domain counts, phase histogram and checker SHA256.

For a=1 all four literal phase tables have zero increment. For a=2, eight have zero increment and eight have positive coherent entropy. For a=3, sixteen have zero increment and 240 have positive coherent entropy. These finite counts supplement the all-a analytic characterization; they do not establish an unbounded class by enumeration. Author cross-checks do not constitute independent agent review.

## Proof dependencies and changed downstream conclusions

Source-bound baseline: threshold Proposition 8.6 / supplemental C035. The report reconstructs its collision identity and supplies a self-contained proof of the exact posterior-payment interface requested by A018. The one-bit cancellation and bent-splice no-go are inherited controls reconstructed here. All mathematical steps are elementary Walsh Parseval, finite entropy chain rule/conditioning, the proved two-point inequality, and the explicit Boolean construction. No pending B09 or A017 theorem is required.

Consumers A019/A020 must pay B_W or impose a substantive structure on the selector sign rows; posterior cancellation alone is insufficient. A026/A027/A037/A057/A058/A061/A063 may replace a raw selector alphabet charge by the exact M_W bound, while retaining B_W and the terminal entropy. A017's physical rank ledger is compatible but not substituted for this arbitrary-branch proof. No new broad class candidate is opened while B04's two already completed baseline packets await review.

## One next mathematical action and independent reviewer

Next: A019 should test a common-spectrum multiplexer with quadratic selector sign rows, paying sum_T R_T H(h_T) by the actual sum_T R_T I(h_T), and then construct a Boolean nonlinear input-translation example with I_W/a tending to zero. This directly addresses the unpaid B_W while excluding the bent-splice via its unequal branch magnitudes. It must keep the physical influence coordinates rather than choosing an oblique basis. A017 already handles a quadratic address phase, so the new application should concern arbitrary shared data spectra rather than repeat its rank census. The proposed next mechanism is not recorded as a proved new class in this stage.

Independent reviewers: A091 and A090. Reconstruct the entropy tensorization from the auxiliary row probability law, check all normalizers including T=empty, and verify the distinction between common magnitude rows and Walsh-character rows. A027 is the next block-interface consumer. No message was sent to other agents; this source-complete artifact is the authorized handoff.

## Actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, COLLISION_BLOCK_INTERFACE.tex, COLLISION_CONTROLS.json, code/check_collision.py, out/FROZEN_SPEC.json, out/CHECK.json, out/SOURCE_RECEIPTS.json and out/PERSISTENCE_RECEIPTS.json are local run artifacts. STATUS.md, WORKLOG.md and LEARNED.md are the local rolling record. Persistence readback and schema receipts are saved in out/PERSISTENCE_RECEIPTS.json. No Git command, shared-index edit, brain write, other-agent mutation, upload or public release occurred. Supervisor copy, mirror verification and independent acceptance remain separate and are not claimed.

## Universal bridge

This stage advances C018's erasure interface and C019's stopping-tree payment by removing the entire posterior component M_W from the unpaid universal budget: it costs at most (2/ln 2)I_W at arbitrary Boolean overlapping branches and telescopes without influence reuse. Exactly B_W and the certified terminal entropy remain. The archived bent splice proves that paying B_W at every chosen node by its own selector influence cannot work universally. The shortest next route is therefore a structural or nonlocal payment of this identified conditional entropy, beginning with common-spectrum quadratic sign rows in A019 and then testing transport through actual restriction trees; another constant-correlation closure would repeat the baseline and would not move the universal gap.
