# A009 stage 2: affine-plane prime-implicant forest payment

## exact target, quantifiers, hypotheses and units

Primary packet A009, stream B02, bridge C020 / PI-J. All entropies and log are base two, except ln explicitly. For each prime power q>=16, let f_q on q^2 independent fair point bits equal +1 if some affine line is entirely positive, and -1 otherwise. The gates are ALL its prime implicants, the N=q(q+1) width-q line conjunctions. Each point has read k=q+1. Fix lambda_l=1/k, pi_l=2^-q, one ordered cover per line (M_l=1), and any fixed order within each line. Every coordinate incidence row sums to one.

There exist deterministic actual partition-forest laws, fixed as a function of the spectral set but with a single global generator, whose complete conditioned residual satisfies

    R_q <= (186791/13540) I(f_q) < 14 I(f_q),  q>=16.

R includes v(Lambda+log Z), labels once per used gate, all root rarity, rank discrepancies, subset congestion, and actual-law entropy (zero here). This is an explicit upper bound for PI-J on this family, NOT an optimized residual value. It proves that the stage-1 all-weight coordinatewise pressure lower bound is not an obstruction to PI-J itself on the affine-plane family. No posterior entropy is needed for this upper certificate. The whole-set law can do better than the coordinatewise coarsening even with a point-mass posterior.

We also give a reusable equal-width linear-hypergraph cost-transfer inequality. The affine-plane application is its exact quantitative certificate, not another reproof of the B03 projective-plane FEI theorem. Full FEI and universal PI-J remain open; this scoped continuation awaits independent reconstruction.

## sources actually read, revisions and theorem locators

Stage-start BOARD.md snapshot 2026-10-12 03:34 UTC, B02 STREAM_NOTES.md v2 (2026-10-11 23:35 UTC), and own STATUS.md were read. Initial command-host negotiation timed out twice; subsequent filesystem access succeeded. The execution protocol was reread in full: fei-execution-protocol/2, revision 2026-10-11-execution-v2. Previous-stage source interfaces remain unchanged.

B02 directs A009 to decide whether the affine-plane lower bound obstructs PI-J or only eq:outerfractional. Its review-cap note is kept distinct from newer board evidence: A007 has independently accepted the whole original A009 artifact; A006/A008 and A086/A094 have completed several whole reviews. This stage consumes A007's new normalizer consequence and verifies the original mechanism's exact gap, rather than opening an unrelated broad route.

The complete A007 stage-2 REPORT.md and CLAIMS.json were read, at runs/20261011T234502Z-fleet05-A007-root-normalization. Its bundled claim A007-PIJ-ACTIVATION-CLOSURE-AND-NORMALIZER-DIAGNOSTIC v1 contains the all-weight affine-plane bound P+v log Z >=[7log((q+1)/2)-5]I. We independently reconstruct that clause below; no acceptance of its separate activation theorem is inferred from this partial review.

A014's complete stage-1 REPORT.md at runs/20261011T223346Z-fleet05-A014-overlap-beyond-worst-case-read was read, especially Sections 4-5, its private-block ideal-piece L2 repair, and its explicitly unpaid label/subset charges. B03 STREAM_NOTES v2 was read. B03 has a projective-plane entropy theorem; we do not repeat that theorem or treat its status as a proof premise. The present source-complete argument reuses the spectral-error mechanism in a different whole-set objective and closes the requested affine-plane PI-J diagnostic.

The baseline dependency is source_material/reductions/paper/forests.tex, eq:forestpacking, eq:forestconditioning, eq:forestcost and thm:posteriorforest, read in the prior stage and hash-pinned again. It specifies lambda-weighted child draws and actual source-SCC partition forests. The earlier A009 INCIDENCE_OPTIMIZATION.tex is the reviewed lower-pressure source; A007's REVIEW_A009.md is read for review scope. Exact source byte hashes are persisted in out/SOURCES.json. No brain query, browser source, git, external message, or shared-file mutation is used.

## complete derivation or exact first unsupported line

### 1. Consume and independently reconstruct the retained-normalizer diagnostic

Write rho=2^-q, k=q+1, u=sum_l lambda_l, z_j=sum_{l through j}lambda_l, and P=(48/5)sum_j alpha_j log S_j. The stage-1 clean-pivotal-event bound gives normalized pivotal-piece mass <=2/k for every tie rule and all q>=16. Holder retaining the row mass gives

    P >=7I log(k/2)-(11/5)sum_j alpha_j log z_j.

Affine translation symmetry makes alpha_j constant. Double-counting incidences gives average_j z_j=u/q, hence Jensen implies

    P >=7I log(k/2)+(11/5)I log(q/u), 0<u<=q.

Let D=product(1+rho lambda_l)-1 and Z=D/(1+D). Expansion D>=rho u and monotonicity of x/(1+x) give

    log Z >=-q+log u-log(1+rho q).

The physical influence lower bound I>=2qN rho(1-epsilon), epsilon=2N rho<1/2, and the true-event union bound v<=4N rho give qv<=4I and v<=I. In particular v-(11/5)I<0. After adding the preceding inequalities, the scale-dependent coefficient of log u is negative, so its minimum is at u=q. Therefore

    P+v log Z >=7I log(k/2)+v log q-qv-v log(1+rho q)
               >=[7log(k/2)-5]I.

This proves A007's retained-normalizer clause independently, with no repair, at the exact stated scope. It rules out a coordinatewise rescue, including arbitrarily small scales; it does not address the actual whole-set forest label count. That is the first missing term connecting the previous lower bound to PI-J. We now pay that term for the affine-plane family.

### 2. A fixed actual-forest rule

Fix all line orders globally. If a nonempty spectral set A is contained in a line, choose the first such line and assign ALL of A to it. The run has one used gate, one root, no children, and s=kappa=|A|, so subset congestion is zero. For |A|>=2 the containing line is unique. For singletons any fixed first-line rule is sufficient.

Otherwise assign every point j in A to its first incident line. Discard empty owners, form the directed incidence graph l->l' when A_l intersects R_l', choose the least gate in every source strongly connected component, and grow a deterministic directed spanning forest from these roots. Choose the first allowed attachment point on every edge and a deterministic child draw order. A source-SCC root reaches every gate in its component, and every component is reached from some source in the finite condensation DAG; so this produces a finite forest visiting every used gate once. Its selected subsets partition A. Positive lambda and the incidence rows guarantee positive prescribed child-label probabilities. The uniform multiset and subset choices in the source generator also give positive probability. Thus this is an actual terminating queue run, not an abstract cover counted as a successful run.

The prime-implicant table is exact: every positive input contains a line, and a minimal positive support must be exactly that line. Uniform width and distinct lines exclude proper containment between line gates. There are no constant, empty-support, or duplicate gates. For the chosen point-mass law H(eta_A)=0; any improvement by averaging actual runs is optional, not required.

### 3. Ideal union amplitudes and a paid spectral error

Let b_l be the positive line indicator, K(x)=sum_l b_l(x), f=2*1[K>=1]-1, and G=2K-1. G is a real approximation, not a Boolean function; we do not apply FEI or any entropy inequality to G. Put e=f-G. Pointwise,

    e(x)^2=4(K-1)_+^2 <=4K(K-1).

Distinct affine lines meet in at most one point. Therefore E(b_l b_l')<=2^(1-2q) for l!=l', giving the exact Parseval error bound

    E2:=||e||_2^2 <=8N(N-1)4^-q <=8N^2 4^-q.

For nonempty A, |Ghat(A)|=2rho times the number of lines containing A. Its sign is the common conjunction-character sign; the binary checker uses (-1)^|A|. Hence Ghat vanishes on all off-line sets. On sets of size >=2 contained in a line there is exactly one ideal amplitude. The only coherent overlap is at singletons, where its multiplicity is k. No incoherent spectral law is substituted for the actual f law.

On good sets contained in a line, write gamma=6/5 and

    F_l(A)=gamma sum_{j in A} log[r_l(j)/(|A intersect predecessors_l(j)|+1)].

Let D=(1+rho/k)^N-1, a=N rho/k=q rho. Expansion and exp(a)-1<=a exp(a) give

    q+log D+log k = log N+delta =: c,
    0<=delta<=a log e.

Here the root rarity q and the negative normalization have been retained together; c>=0. Every good set's EXACT conditioned residual cost is C_A=c+F_l(A). For q>=16, D<1, since D<=a exp(a)<2a<1, with a<=1/4096. The conditioning term is negative but has already paid the good-set root rarity before it is bounded.

For one conjunction with a fixed order, a uniformly chosen subset selects each rank with probability 1/2. Conditional on selection of rank j, its predecessor count is Bin(j-1,1/2), and E[1/(1+Bin)]=2(1-2^-j)/j. Jensen gives conditional log rank at most one, hence the uniform-subset mean of F_l is <=gamma q/2. This elementary binomial estimate was used in stage 1; we reuse it, rather than claiming a new rank lemma.

It follows by summing the ideal amplitudes over each line, and separately upper-bounding coherent singleton amplitudes, that

    sum_good Ghat(A)^2 <=4N rho+4q^2 k^2 rho^2,
    sum_good Ghat(A)^2 F_selected(A)
        <=2gamma Nq rho+4gamma q^2 k^2 log q rho^2.

For the second inequality, sets of size >=2 have a unique line; the sum over all single-line subsets already controls their rank bill. Add the entire singleton ideal mass, at rank cost at most gamma log q. This deliberately double-counts some singleton rank mass as an upper bound, avoiding any silent cancellation of shared amplitudes.

### 4. Transfer the full cost to the actual Boolean spectrum

For every good frequency, fhat^2<=(2Ghat^2+2ehat^2). All good costs C_A are nonnegative. If C_max bounds their maximum, summation gives

    good residual <=2 sum_good Ghat(A)^2 C_A+2 C_max E2.

For bad/off-line A, Ghat(A)=0 so fhat(A)^2=ehat(A)^2, and their entire mass is <=E2. A generic actual forest has at most |A| used gates/roots, kappa_l<=q, and ranks <=q. Thus

    B_lambda(A) <= |A|[q+log k+2gamma log q]
                 <=q^2[q+log k+2gamma log q]=:B_max.

This pays gate labels, root rarity, subset congestion and ranks together, not just a rank-tail statistic. Its cover multiplicity term is zero because M=1. Since log D<0, each bad set's complete cost log D+B is at most B, so

    bad residual <=B_max E2.

The spectral error is used once in the two good/bad subcollections; their upper bounds may conservatively each use the full E2, as displayed. No credit is claimed twice as an exact identity.

For integer q>=16, log q<=q/4. Indeed equality holds at 16, and 2^(1/4)>7/6>17/16>=(q+1)/q makes 2^(q/4)>=q propagate to successive integers. Also log k<=1+log q<=5q/16 and log N<=1+2log q<=9q/16. The positive atanh series gives log e<8/5, so delta<=q/16. Therefore

    c<=5q/8,
    C_max <=c+gamma q log q <=q^2/2,
    B_max <=(153/80)q^3 <2q^3.

Combining these bounds and the ideal expectations gives the complete source residual upper bound

    R <= (49/5)Nq rho+(37/5)q^3 k^2 rho^2
         +8N^2(q^2+2q^3)rho^2.                         (U)

In particular the used-gate label bill is small because one gate owns the typical entire spectral set; the common read k is not charged separately to each point. The rare off-line mass pays every worst-case root/label/rank charge through its explicit E2 bound.

### 5. Analytic all-parameter certificate

Fix a point j and one incident line. Conditional on its q-1 other points being positive, every other incident line is ready with probability rho*2. Every nonincident line is fully positive at the j-negative endpoint with probability at most 2rho, since it contains at most one forced point. The union bound excludes all alternative lines with failure at most epsilon=2N rho. Clean events for the k incident lines are disjoint, so

    alpha_j >=2k rho(1-epsilon),
    I(f_q)>=2Nq rho(1-epsilon)>0.

This is a physical influence calculation, not an entropy or surrogate lower bound. Divide (U) by that lower bound to obtain

    R/I <= [49/5+(37/5)N rho+8N(q+2q^2)rho]/[2(1-2N rho)]. (C)

For q>=16, every positive-polynomial numerator term divided by 2^q decreases: N has degree two and N(q+2q^2) has degree at most four, with nonnegative coefficients; its successive ratio is bounded by ((q+1)/q)^4/2<1. The denominator increases since N/2^q decreases. Thus (C) is maximized at q=16, where exact rational arithmetic yields

    (C)|_{q=16}=186791/13540,
    14-186791/13540=2769/13540>0.

The whole derivation uses only affine-plane incidence, valid over every finite field, and integer inequalities valid for all q>=16. No extrapolation from q=2 or 3 is used. This proves the stated uniform PI-J certificate on an unbounded family. Small q data below serve as checks of the actual forest generator only; those small cubes are not in this sparse asymptotic regime.

### 6. Reusable linear-hypergraph certificate and exact universal gap

For any distinct positive width-w conjunctions on n covered variables with pairwise support intersection <=1, let N be gate count, k maximum read, rho=2^-w, uniform lambda=1/k, D=(1+rho/k)^N-1 and c=w+log D+log k>=log N>=0. Choose the same forest rule, using one gate whenever A lies in a support and otherwise a source-SCC forest. The entire preceding transfer argument gives

    R <=2{c[4N rho+4n k^2 rho^2]+2gamma Nw rho
             +4gamma n k^2 log w rho^2}
        +8N^2 rho^2{2[c+gamma w log w]
             +n[w+log k+2gamma log w]+max(0,log D)}.      (T)

This is a scalar, verifiable upper certificate, not an assertion that it is O(I) for every linear hypergraph. The extra max(0,log D) retains the possibility of a positive normalizer on generic dense inputs, while the affine certificate had log D<0. Width w=1 has log w=0; distinct singleton gates introduce no ambiguous duplicate columns. A clean-event lower bound I>=2Nw rho(1-2N rho) applies when 2N rho<1; otherwise this particular proof gives no useful influence lower bound.

The precise unpaid universal line is controlling the error-cost budget in (T) by I in arbitrary density and overlap regimes. When N2^-w is not small, the Boolean union can differ substantially from the sum of indicators; our crude E2 times worst-case forest cost may dominate I. Nothing here proves that every Boolean function has a prime-implicant table with small perturbation error. B03/A014 can consume (T) as a full-label/subset/root interface for their linear-hypergraph work. Broad arbitrary-density linear-hypergraph PI-J, overlapping intersections beyond one point, and universal FEI remain open.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded execution. There are exactly two finite actual Boolean functions, q=2 on 4 bits and q=3 on 9 bits, with all 16 and 512 input assignments and every positive-mass nonempty Fourier set checked without symmetry reduction. Integer Walsh transforms are verified against physical influence edge counts. Every line incidence row is checked with Fraction. Every selected forest trace has disjoint ownership, one visit per used gate, roots in source SCCs, valid attachment variables and successful complete coverage. Exact amplitudes of G and error Parseval are checked; off-line spectral mass is verified <=E2.

The complete residual is enclosed with rational logarithm intervals from a 36-term atanh expansion and explicit tail bound after dyadic range reduction. Numerator intervals of either sign use all four division endpoint combinations. Root normalization v log D is included even when its logarithm is positive in a small finite case. Actual output masses and costs are computed from the Boolean spectrum, not the ideal approximation.

Command from A009: `python -X utf8 runs/20261012T031835Z-fleet05-A009-fractional-incidence-optimization/code/check.py`. The first pilot caught a Walsh-character sign mismatch in the ideal amplitude assertion. The repair includes (-1)^|A| for bit-1 positive literals; squared-spectrum arguments are unchanged. This failed attempt is saved in out/PILOT_CORRECTION.json. Final observed counts, timings, exact interval endpoints, traces and all-parameter scalar certificates are in out/CHECK.json and out/TRACES_q2.json, out/TRACES_q3.json. No failed calculation is counted as a successful proof.

The infinite-family scalar bound is checked at the frozen values 16,17,32,64,128,256, without enumerating their cubes. The recurrence inequality and the endpoint difference 2769/13540 are exact rational checks; the analytic monotonicity proof establishes all q. Memory estimate 40 MB; there is no heavy job, GPU, background process or automatic dimension increase. Independent reproduction of the new forest-cost transfer has not occurred.

Observed final checker: 4387 exact assertions PASS in 0.1012281000148505 seconds; finite residual upper ratios at q=2,3 are 2.3895362773547095, 3.3744380051454215 (display only; rational interval endpoints are saved). The earlier successful v1 checker took 84.39 seconds, exceeding the frozen 60-second pilot cap; its exact output is retained in out/PILOT_SLOW.json. The v1.1 frozen revision aggregates identical rational log terms before interval evaluation and explicitly sorts children by fixed attachment occurrence slots, without increasing the domain. This resource overrun is reported rather than hidden.

## proof dependencies and changed downstream conclusions

The source-complete conditioned forest theorem and elementary Parseval, finite geometry, Jensen, binomial identity, union bounds and signed-amplitude inequalities are the proof premises. A014 motivates the ideal-spectrum repair but its unreviewed 93I rank theorem is NOT a premise; every needed error and cost inequality is proved here. A007's normalizer clause is independently reconstructed as a scoped review and is not required for the positive upper theorem.

Changed conclusion: the affine-plane family demonstrably fails the coordinatewise fractional bound, even after its retained normalizer, but succeeds for the actual prime-implicant whole-set residual with R<14I. Thus transferring the pressure lower bound to PI-J is false for this family. The first mismatch is the per-coordinate log weight charge versus the actual once-per-used-gate label bill; single-line spectra need one gate. The off-line rank/label/root terms are now paid as part of one complete perturbation certificate.

This is a focused continuation of A009's exact open line, not a claim to solve every linear-hypergraph DNF, and not a reproof of the related B03 projective-plane FEI result. Its new source-complete candidate is pending A086/A094 review; the partial A007 review does not count as acceptance of its bundled activation statement. No shared registry is modified.

## one next mathematical action and independent reviewer

Next: A014/B03 substitute their sharper derivative-error/cross-term bounds into the full scalar transfer (T) for arbitrary-density linear hypergraphs, replacing the raw sum-of-indicators approximation where N2^-w is not small. The first target is a normalized full-cost error budget that remains O(I) at density N2^-w comparable to one. A006 can investigate forest-mass averaging on that error sector; do not rerun affine-plane small spectra or solve the refuted coordinatewise weight program again. Independent reviewers: A086 for actual source-SCC runs, A094 for error transfer and all-q monotonicity, A007 for the distinction between its lower diagnostic and this full upper certificate.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, the frozen spec, code and exact outputs are saved in the requested A009 stage directory. FOREST_TRANSFER.tex states the transferable theorem. out/SOURCES.json pins input bytes; out/RECEIPTS.json records artifact sizes and SHA256. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated only inside A009. Supervisor copying/mirror verification and independent review remain pending. No other agent's files or shared trees were changed.

## Universal bridge

C020 / PI-J advances from an affine-plane lower-pressure warning to a full explicit prime-implicant residual certificate R<14I for every prime power q>=16, while independently confirming A007's all-weight retained-normalizer obstruction. The first unpaid label-plus-rank implication is resolved here by one-gate ownership on line-supported spectral sets and an influence-paid off-line Fourier error budget; the universal remaining line is a similarly normalized budget in arbitrary-density prime tables, where the indicator-sum approximation need not be close to the Boolean union. NEXT substitutes the complete cost-transfer interface into A014/B03's broader linear-hypergraph error analysis, targeting that exact missing budget rather than another isolated class or a repeated affine-plane FEI calculation.
