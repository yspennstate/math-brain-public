# A086 independent reconstruction of the available joint-code chain

Verdict: accept A006-SUNFLOWER-POSTERIOR-FOREST-PAYMENT v1 and A011-BOUNDARY-RETAINING-SELECTOR-TRANSCRIPT v1 at their stated scopes. Accept A001-FIXED-BOOLEAN-MARGINAL-TENSOR-ADMISSION v1. A001's full 37-interface inventory is only partially reviewed here; no blanket analytic acceptance is given. Full FEI is OPEN. These are local review records, not changes to any shared index.

## 1. The conditioned forest dependency, reconstructed

The exact source is source_material/reductions/paper/forests.tex, labels eq:forestpacking, eq:forestconditioning, eq:forestcost and thm:posteriorforest. The reference uses child probabilities lambda_l; the public threshold queue's uniform-neighbor law is a different generator and cannot be substituted.

For finitely many gates, independent roots have empty-root probability 2^(-Lambda). Every finite successful nonempty-root run picks at least one nonempty subset. Thus its output is nonempty, and the sum of probabilities of such runs is at most Z=1-2^(-Lambda). Failed and infinite histories need no termination theorem: they contribute no output mass. Dividing by Z is legitimate for nonempty output, since Lambda>0. Partition witnesses themselves do terminate: every used gate is queued exactly once, with disjoint owned subsets and a finite spanning forest.

For a given assignment, take source SCC roots and a directed spanning forest. The run specifies the actual root set, subsets, child counts, attachment multiset and ordered occurrence-wise child names. The union decoder forgets latent gates but keeps every selected coordinate. A static function and generator determine one global dictionary. An abstract reordering of edges is not a new run unless some actual occurrence draw changes. This distinction is the only legitimate source of factorial credit.

Re-multiplying all queue choices gives

    -log q_1(r) <= Lambda + K_ref |A| + B_lambda(A;r),
    K_ref = 3 + 2 log2(3) + log2(6e).

The subset weight bound follows by choosing a rank-minimizing order for each owned coordinate: ln^+(rank/s)<=F+ln(kappa/s). The normalizer is <=(6eM)^s; size choices cost <=|A|log2(3); child counts <=|A|(1+log2(3)); multiset choices <=2|A|. Their sum is exactly the displayed K_ref. Gate names occur once per used gate, as either a root or a child. Conditioned q=q_1/Z adds log2 Z to negative log cost, with the stated sign.

For any distinct-run posterior p, set W_A=sum_selected q(r). KL against q/W_A gives E_p[-log q]-H(p)>=-log W_A>=-log Q_*(A). Combining Q_* with the atom 1-v at empty and mass vQ_* on nonempty produces a subprobability. Gibbs yields h2(v)+v(Lambda+log Z)+K_ref I+sum P[A](E B-H(p)). This establishes the dependency used by A006 and the one-way implication audited in A001. There is no assumption that all queues terminate, no free scale choice and no sum over duplicate abstract descriptions.

## 2. A006 sunflower, independent all-m analysis

For m>=1, write b=product_i(1-x_i)/2. The Boolean function is f=x0-(1+x0)b. Thus P(empty)=4^-m, P({0})=(1-2^-m)^2, and each nonempty private T and {0} union T has mass 4^-m. Physical influences are 1-2^-m on x0 and 2^-m on each private coordinate, giving I=1+(m-1)2^-m>=1.

Use supports {0,i}, ordered (0,i), lambda=1/m, pi=1/4, gamma=6/5, a=2^-gamma and D=(1+1/(4m))^m-1. The conditioned root-set probability is (1/(4m))^k/D. In particular Lambda+log2 Z=log2 D; both terms are retained.

Private coordinates have only one possible owner. If 0 is absent there are no graph edges: all t private gates must be roots, giving exactly one run. If 0 is present its owner is the unique source. Every other used gate is a leaf attached through 0. If that owner is private, there are t choices and (t-1)! ordered child names, hence t! runs. If outside the private set, there are m-t choices and t! ordered names, hence (m-t)t! runs. Actual chronological queue keys distinguish these permutations even when attachment occurrences all name the same coordinate. There are no other SCC-root or spanning-forest choices.

Direct residual weights are

    S_B({0})=1/4,
    S_B(T)=(a/(4m))^t,
    S_B({0}+T)=t! a^(t-1)/(4m^t) [1+(1-t/m)a].

The distinct-run variational minimum is -log2 S_B. The logarithmic identity follows from KL; it is not a finite numerical assumption. Singleton-common runs each cost log2 m+2, and their m-fold multiplicity erases log2 m exactly.

Reconstruct the complete probability using size law 1/[s(s+1)], child-count law 1/[(c+1)(c+2)], multiset law 1/binom(s+c-1,c), the singleton weights (1,a)/(1+a), and child probability 1/m. A private singleton leaf contributes a/[4(1+a)]. An inside root has s=2,c=t-1, subset-size probability 1/6, child-count 1/[t(t+1)], multiset 1/t. An outside root has s=1,c=t, singleton probability 1/[2(1+a)], child-count 1/[(t+1)(t+2)], multiset 1. Multiplication and summation over the above chronological runs give

    W({0})=1/[16(1+a)D],
    W(T)=D^-1 [a/(16m(1+a))]^t,
    W_in=t!/[24 D t^2(t+1)m^t] [a/(4(1+a))]^(t-1),
    W_out=(m-t)t!/[8 D m^(t+1)(1+a)(t+1)(t+2)] [a/(4(1+a))]^t.

This agrees with A006 without using its implementation. W is only the selected partition-run mass; additional successful repeat-visit runs can increase Q_* but are not needed. The residual-optimal posterior and complete-probability-optimal posterior are different laws, as A006 correctly states.

The all-m expectation is checked separately from finite enumeration. Binomial aggregation gives

    R_m=v log2 D +2(1-2^-m)^2
      +4^-m sum_t binom(m,t)[2t log2 m+(22/5)t+4/5
                             -log2(t!)-log2(1+(1-t/m)a)].

Here 1/4<=D<1/3, so the first term is nonpositive. Dropping it and the two negative terms yields 2+2^-m[m log2 m+(11/5)m+(4/5)(1-2^-m)]. Use log2 m<=m. P(m)=m^2+(11/5)m+4/5 has initial scaled values 2 and 23/10, and 2P(m)-P(m+1)=m^2+m/5-12/5>=0 for m>=2. Therefore R_m<=43/10<=43I/10. For point-mass posteriors, B>=0 and v log2 D>=-2v give R_det>=(1-2^-m)^2(log2 m+2)-2v, diverging relative to I.

For complete mass, W({0})^-1<32/3<16, using a<1 and D<1/3. Private costs are <=t(m+7), because (1+a)/a<5. Common cost from W_in alone is <=5+3m+t(m+5): bound log2(24D)<=5, 2log2 t+log2(t+1)<=3m, t log2 m<=tm, and (t-1)log2[4(1+a)/a]<=5t, then discard -log2(t!). Sum the two rare spectral sectors. Their expected cost is <=2^-m(m^2+9m+5)<=15/2; the recurrence difference is m^2+7m-5>=0 for m>=1. The dominant cost is <4, so C_m<=23/2<=23I/2.

Each scaled lambda_i=2^-k/m obeys physical packing. The fixed prior w_k=1/[(k+1)(k+2)] telescopes to one. Every component has its own root normalizer and complete law. Using k=0 costs exactly one bit on nonempty spectra, hence v<=I additional expected bits. This gives 53I/10 for residual plus prior and 25I/2 for complete nonempty cost plus prior.

Unit/scope clarification: C_m and the 25I/2 quantity exclude the empty/nonempty binary split. The general Gibbs entropy inference is H<=h2(v)+C_m, or H<=h2(v)+C_m+v for the mixture. Using h2(v)<=2I gives 27I/2 and 29I/2 respectively. A006's claim is an expectation bound, not the stronger assertion H<=C_m or a new FEI class. Its original statement needs no repair.

## 3. A011 coherent transcript, independent reconstruction

At a queried selector j absent from both child subtrees, child coefficients u_T,v_T give parent coefficients (u_T+v_T)/2 at T and (u_T-v_T)/2 at T+{j}. Fair physical child sampling followed by its exact spectral witness produces retained marginal q_T=(u_T^2+v_T^2)/2. Given T, append Z with theta_T=(u_T-v_T)^2/(4q_T). It lies in [0,1] by Cauchy-Schwarz. Zero q is unsampled. The two output probabilities are exactly the parent coefficients squared. This handles u=v, u=-v, one coefficient zero, and arbitrary coherent collisions. The sampled retained vector is not asserted to be a Boolean child after spectral conditioning.

Recursion is finite because the decision tree is finite. Physical choices and original leaf witness distributions retain their marginals: every later innovation sums to one. Thus leaf visitation remains 2^-d and leaf expected cost is unchanged. Coordinates may be repeated across different branches; the no-repeated-query-on-a-path condition ensures a node coordinate is absent from all its descendants.

The codebook is fixed for F: physical branch prefix, leaf witness prefix, then d spectral bits in a specified order. A decoder reaches a leaf from the first prefix, parses its prefix dictionary, then reads exactly d bits. The physical queried coordinates identify where to place those membership bits. Codewords remain prefix-free even for empty leaf codes. Include unsampled spectral words when computing Kraft:

    sum_leaves 2^-d Kraft(leaf) sum_z 2^-d <=sum_leaves 2^-d=1.

Distinct witnesses can decode the same spectral set. The code accounts for their probability separately; the output reference sums their Kraft masses. H(S)<=H(W)<=E L and -log Q(S(w))<=L(w) both hold. No normalizer, success conditioning or cancellation credit has been omitted.

Expected length is exactly 2D+sum p_l c_l. Physical conditioning gives I_data=sum p_l I(g_l); admission I_sel>=gamma D bounds the selector part by (2/gamma)I_sel and the leaf part by K I_data. Only disjoint portions of physical influence are charged, yielding max(2/gamma,K)I.

For unsigned character leaves, different characters disagree on half the independent data cube, including when their supports overlap. Thus I_sel=B/2 and c_l=0. A flip outside the coordinates queried on a reached path leaves the selector in its leaf cell, giving B<=D. On the alternating first-positive comb, reach probability at j is 2^-(j-1). The continuation-opposite probabilities obey r_a=1, r_j=1-r_(j+1)/2 in [1/2,1]. Hence D=2(1-2^-a), B=sum reach_j r_j>=D/2 and 2D<=8I_sel. These are valid all-a statements; finite tree checks alone would not prove them.

The first universal unsupported step is replacing the admission condition by a theorem for arbitrary trees or replacing leaf costs by K I for arbitrary Boolean leaves. Neither step is made in the original claim. The code is a different complete reference from the conditioned queue; no inequality between their optimum costs follows from existence of the transcript.

## 4. A001 scope review

Endpoint J is a sufficient condition, not an established equivalence of optimal constants: the source's entropy inequality plus h2(v)<=2I gives FEI(2+K_ref+K) from a universally paid residual. A posterior may depend on A, but representation, lambda and generator are fixed for f. Exact root conditioning remains v log Z. This matches A001's ledger.

For the tensor-admission claim, fix an actual Boolean base F0(X,Y0). Disjoint multiplication F_t=F0 product_{r=1}^t f(Z_r) gives a product Fourier law. Its X marginal and X-degree bound remain unchanged. Let c0=H(S_Y0|S_X). Then H(S_Y0,Z|S_X)=c0+tH(f), I(F_t)=I(F0)+tI(f). Any class-wide constant C therefore yields H(f)<=C I(f) by division by t and passage to the limit. Conversely conditional entropy is at most full entropy, so full FEI(C) gives the bound on every admitted class member. The optimal constants agree as extended-real suprema. The argument covers constant seeds without taking an H/I ratio; divergent suprema are handled seed by seed. Accept this claim independently.

The good-coordinate criterion's direction is consistent: sum_i H(S_i|S_-i)<=H(S) follows from the entropy chain rule and conditioning. Under FEI(C), at least one relevant i has B_i<=C I_i. Induction with the source's physical restriction identity and mismatch bound gives FEI(K+2/ln2) from hereditary availability. This review does not independently accept every remaining analytic entry or manuscript constant in A001's 37-interface inventory.

## 5. Exact validation and unresolved chain

Command from A086: python -X utf8 runs/20261011T214823Z-account05-A086-joint-code-referee/code/audit.py.

Frozen domain: m=1..5, two rational auxiliary theta values; all 1,446 depth-three prunable trees with two unsigned character labels; all 256 full depth-two trees with arbitrary signed Boolean one-bit data leaves. No symmetry reduction. Integer FWHT and Fraction arithmetic only. The checker independently builds assignment graphs, source SCCs, parents, actual chronological queue traces, all legal codewords and a signed recursive sampling law. Actual theta=2^-6/5 is treated analytically; rational theta cases verify the algebraic formulas, not a false rationalization of theta.

Result: 251,206 exact assertions, no failures; 1,750 sunflower run instances, 1,702 trees, 38,958 positive-probability selector witnesses and 20,722 duplicate-output excess witnesses. Runtime 12.670593 seconds. Leaf masses, expected lengths, decoded Fourier laws, physical influences, Kraft sums, prefix-freeness and sum of selected queue probabilities <=1 all pass. No author checker was imported or executed. No floating logarithmic comparison is a proof premise.

The intake inventory contains reports only from A001, A006 and A011 among A001--A015. Missing reports are dependencies to consume in a later stage, not failed proofs. B18 STREAM_NOTES.md is absent. See JOINT_CODE_GAPS.json for the precise next target to A089 and inventory hashes. A094/A085 should review this reconstruction; it supplies one independent review, not the two-review threshold for a major universal candidate.
