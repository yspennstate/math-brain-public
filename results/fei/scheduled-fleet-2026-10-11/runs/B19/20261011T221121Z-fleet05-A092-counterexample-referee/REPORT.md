# exact target, quantifiers, hypotheses and units

Primary verdict: ACCEPT_AT_STATED_SCOPE for A046-AND-ENDPOINT-TAX-NECESSITY@1, from run 20261011T214251Z-fleet05-A046-current-candidate-intake. For the actual sign f(x,y)=(-1)^(xy), independent Bernoulli biases p and fixed q in (0,1/2), and physical reveal A={X}, independently reconstruct E=J_A-M_A=4q(1-2q)p log2(1/p)+O_q(p). Consequently every universal scalar tax tau(p) in J_A<=M_A+tau(p) has liminf tau(p)/(p log2(1/p))>=1/2. The original proof needs no repair for this scope. All Shannon quantities use bits and the normalized biased product Fourier basis, including the empty coefficient.

Additional result, contributed by A092 and pending independent review: at q=1/4, for every 0<p<=1/2, E>=p[log2(1/p)/2-7]. Thus for every finite K>=0, every integer k>2K+14 supplies the explicit actual Boolean witness with p=2^(-k), q=1/4 and E>Kp. This refutes exactly universal taxes bounded above by Kp. It does not refute B09's Delta(p) tax, settle its sharp coefficient, or imply failure of uniform-cube FEI.

Secondary calibration only: reproduce A071's stated minimum-positive finite-grid case from its three-bit truth table. This is not independent acceptance of all 20,736 representatives or all 192,000 raw cases in A071-B09-THREEBIT-GRID-CERTIFICATE@1.

# sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2; campaign README, CURRENT_STATUS, claim/obstruction registries, packet state, stream actions, and campaign plan, especially A092 acceptance tests. The authoritative registry already accepts the original B05/B19 review; preserve that baseline rather than repeat its computation. Earlier B05, B09 and B19 reports were consulted, including B09 sections 4 and 5(4) and B19 sections 2-5. BOARD.md was read at stage start (supervisor snapshot 2026-10-11 22:05 UTC). B19 STREAM_NOTES.md is absent at the assigned path, an access-only limitation.

Supplement CAMPAIGN.md, CLAIMS.md (especially C018/C019/C020/C024), COUNTEREXAMPLES.md, SEED_LEMMAS.md and NATIVE_MAPPING.md were consulted, as were the supplied source-note introductions, physical restriction identities and erasure route definitions. Context paper text versions were consulted for introductions, Fourier normalization and scope: threshold_paper_38pp (Theorems A-D, constant below 8.937), threshold_paper_29pp_earlier_version (older constant below 13.415), percolation_spectral_pivotal_entropy_30pp and 31pp_other_version (Section 1.1 and Theorem 1.1). These manuscripts are context rather than mathematical dependencies; their full proofs have not been independently audited here. Some context TXT files require cp1252 fallback; an initial UTF-8 decode failed and was corrected. No internet or literature-priority claim is involved in this self-contained audit.

Original new source: A046 REPORT.md complete derivation steps 1-5, CLAIMS.json and code/exact_check.py. A071 REPORT.md supplies the calibration truth table, parameters and exact published lower bound. Their source bytes, campaign files and local context are pinned by out/SOURCE_MANIFEST.json. Review provenance uses local SHA256 hashes, not unverified Git revisions for these new agent runs.

# complete derivation or exact first unsupported line

Reconstruct f from the four physical values (1,1,1,-1), in little-endian order x+2y. Since f=1-2XY, its centered unnormalized expansion is obtained by expanding X=p+(X-p), Y=q+(Y-q). The coefficients are 1-2pq, -2q, -2p and -2 in the basis 1, X-p, Y-q, (X-p)(Y-q). Multiplying squared coefficients by the corresponding basis variances yields

    a=(1-2pq)^2,
    b=4p(1-p)q^2,
    c=4p^2q(1-q),
    d=4p(1-p)q(1-q).

These are nonnegative and sum to one. They have been independently obtained by a recursive pair transform on the original values; no supplied spectrum was taken as an input. Write u=4q(1-q), r=pu. Then c+d=r. The X=0 restriction is constant; the X=1 restriction is 1-2Y with spectral law (1-u,u). The physical joint channel is therefore

    P(X=0,S_Y=0)=1-p,
    P(X=1,S_Y=0)=p(1-u),
    P(X=1,S_Y=1)=pu,
    P(X=0,S_Y=1)=0.

An independent conditional-law calculation gives

    M=(1-r)h2(b/(a+b))+r h2(d/(c+d)),
    J=h2(p)-(1-r)h2(p(1-u)/(1-r)).

The entropy chain rule equivalently gives M=H(a,b,c,d)-h2(r) and J=h2(r)-p h2(u). The checker encloses both implementations and checks their overlap. Hence E=2h2(pu)-H(a,b,c,d)-p h2(u).

For fixed positive alpha and t=alpha p+O(p^2), -t log2(t)=alpha p log2(1/p)+O_alpha(p). To justify the remainder: t/(alpha p)=1+O(p) has logarithm O(p), and p^2 log2(1/p)=O(p). Mass 1-O(p) contributes O(p), because -(1-s)ln(1-s)<=s; a mass O(p^2) contributes O(p^2 log(1/p)). With fixed interior q, b=4q^2p+O_q(p^2), d=4q(1-q)p+O_q(p^2), c=O_q(p^2). Thus H=4q p log2(1/p)+O_q(p), while h2(pu)=u p log2(1/p)+O_q(p). Subtraction gives E=4q(1-2q)p log2(1/p)+O_q(p), exactly A046's statement. At q=1/4 the coefficient is 1/2; the identity 4q(1-2q)=1/2-8(q-1/4)^2 identifies the maximal coefficient only within this fixed-q AND family. Applying any universal tau to these actual gates and dividing by p log2(1/p) proves the claimed liminf necessity. No unreviewed uncertainty theorem is used.

Explicit contributed bound: set q=1/4, L=log2(1/p), 0<p<=1/2. The masses reduce to a=(1-p/2)^2, b=p(1-p)/4, c=3p^2/4, d=3p(1-p)/4. The following elementary bounds include their constants:

* Let s=1-a=p-p^2/4<=p. Then -a log2(a)<=s/ln2<=2p; ln2>=1/2 follows by integrating 1/t on [1,2].
* Both b/p and d/p are at least 1/8 and at most 1; therefore the b,d contributions are at most p(1-p)L+3p.
* The c contribution equals (3p^2/4)(2L+log2(4/3)) and is at most (3p^2/2)L+3p^2/4. The elementary maximum -p ln p=1/e, together with e>=2 and ln2>=1/2, gives pL<=1.

Adding these bounds gives H<=pL+(47/8)p<=pL+6p. Meanwhile h2(3p/4)>=(3p/4)log2(4/(3p))>=(3p/4)L and h2(3/4)<=1. Therefore E=2h2(3p/4)-H-p h2(3/4)>=p(L/2-7). Choosing integer k>2K+14 proves E>Kp for p=2^(-k) without computing or extrapolating an entropy sign. This is a quantitative corollary contributed separately from the unchanged accepted A046 version; A092 does not independently accept its own new lemma.

Aligned disjoint products have product spectral distributions and product physical channels, so M and J add. For m copies at the finite witness biases, the excess exceeds m*1195/10000 bits. This validates A046's tensor scope discussion but provides no shared-variable or arbitrary composition additivity.

Scope guard: under the uniform measure the same two-bit sign has four Fourier masses 1/4, H=2 and I=1. Disjoint products have H=2m, I=m and ratio exactly 2. Varying biased p changes the measure and the helper being tested. It does not produce an actual uniform-cube family with unbounded H/I.

First unsupported line in the universal route remains: pay the complete physical stopping/restriction/composition cost, including terminal entropy and each biased tax only once, by a finite dimension-independent influence budget. The endpoint obstruction and its quantitative corollary do not establish that payment. For A071, the first unverified audit obligation here is reconstruction of its entire grid coverage, sign enclosures and all equality certificates; one successful calibration does not discharge it.

# executed validation with domain, arithmetic, commands and outputs

SEARCH_SPEC.json was saved before calculations. Family and domain were fixed at four biased two-bit gates, one three-bit A071 calibration and uniform two-bit AND: six cases, no symmetry reduction or dimension escalation, estimated 30 MB and cap 60 seconds. Executed from the assigned workspace:

    python -X utf8 runs/20261011T221121Z-fleet05-A092-counterexample-referee/code/reproduce.py

The checker implements the recursive unnormalized centered transform, then multiplies squared amplitudes by exact product variances. Physical restrictions are extracted from the truth table. Exact Fraction arithmetic checks parent normalization, every physical-channel marginal, analytic masses and the uniform influence. Conditional entropy and mutual information use conditional distributions independently of A046's implementation.

Logarithmic certificate: normalize x=2^k z with z in [1/2,1]. Put t=1-z, so 0<=t<=1/2. Then -ln(z)=sum_{j=1}^80 t^j/j+R, with 0<=R<=t^81/[81(1-t)], obtained by bounding each tail denominator below by 81. The ln2 interval is strictly positive. If -ln(z) is in [a,b] and ln2 in [c,d], log2(x) is in [k-b/c,k-a/d]. All numerator quantities in this division are nonnegative. Entropy multiplication reverses endpoints for negative weights. This independent implementation uses a different series from A046's atanh expansion and avoids the original B09 signed-division failure. Thirty-three known power-of-two logarithms check both range-reduction signs. Printed rational decimal endpoints are outward rounded exactly.

out/REPRODUCTION.json records PASS, rational certificate endpoints and arithmetic runtime. All four AND excesses are strictly positive and below the original Delta tax. At p=1/8, masses are exactly (225,7,3,21)/256 and E>1195/10000. All four cases also satisfy the new explicit bound; the all-p proof is the preceding analytic argument. For A071, the physical table is +1 except x=3 (bits 1,1,0), biases (1/8,1/8,1/2), reveal coordinate 2. The independent defect D=M+Delta-J is positive and exceeds its saved lower bound (12119843879252555703/4096)/2^60. Only this calibration is audited.

# proof dependencies and changed downstream conclusions

A046-AND-ENDPOINT-TAX-NECESSITY@1 is accepted independently with unchanged statement and hypotheses. A092 supplied no repair to that version, so the review meets the contributor-independence rule. The separately contributed explicit bound is a new claim pending A087/A085 review. Neither claim relies on acceptance of B09-BIASED-BLOCK-UNCERTAINTY@1. B09's core uncertainty lemma remains outside this audit. Its section 5(4) endpoint conclusion may now use A046's independently accepted lower-bound family instead of the invalid inference from the size of an available upper bound. The old signed log checker remains superseded.

B20 should propagate the precisely refuted universal O(p) and coefficient-c<1/2 taxes to B09/B10/B12/B13. Taxes with coefficient at least 1/2 and the original Delta bound are not refuted. A071's full finite claim retains its pending-review status. No shared index was edited and no downstream adoption is inferred from this local review.

# one next mathematical action and independent reviewer

Next: audit the next source-complete counterexample to a newly versioned coefficient-1/2 tax on Boolean-realizable physical children; require its original truth table, exact conditional-law calculation and rigorous sign. This directly addresses the remaining sharp-tax gap without replaying retired O(p) claims. Independent reviewer for A092's explicit corollary: A087, with A085 checking arithmetic. A046's unchanged claim has the independent A092 review here. Consumers are A047/A048/A071, B09/B12/B13 and B20.

# actual persistence receipts or precise save blocker

All required artifacts are saved in the assigned A092 run: REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json with packet_ids=[A092], SEARCH_SPEC.json, code/reproduce.py, code/finalize.py, out/REPRODUCTION.json, out/SOURCE_MANIFEST.json and out/VALIDATION.json. Rolling STATUS.md, dated WORKLOG.md and LEARNED.md are current. finalize.py checks exact protocol keys, statement hashes, progress-copy identity, file sizes and all required persistence receipts; it writes artifact hashes and sizes after completion.

No mirror or supervisor-copy receipt is available locally, so remote durability, downstream use and release remain unverified. Missing B19 notes do not block this independent permitted review. No git, external messages, brain writes or another agent's file mutations were performed.

Universal bridge: this stage supports C019 stopping-tree payment by independently certifying that a biased local tax must retain at least (1/2)p log2(1/p) at the endpoint, and by supplying explicit actual witnesses for every proposed fixed Kp tax. It does not decrease the unpaid universal payment constant: nonreusing cumulative charges and terminal entropy remain open. NEXT targets a precise strengthened local boundary whose validity would constrain the surviving stopping-tree ledger; this is the shortest review route toward a sound full-FEI argument rather than another isolated easy-class theorem.
