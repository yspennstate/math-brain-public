# A fixed number of conditioned-product reference components survives calibration

All laws are finite and normalized, and all logarithms are base two. The references below are probability models; they are not asserted to be squared spectra of Boolean functions. The true law at every physical node is the actual squared Boolean Fourier spectrum. Full FEI remains open.

## 1. The reference family and its boundary

On d frequency bits write 0 for the empty set. A component on the nonempty sets is either

 (i) a product Bernoulli law A_p conditioned on S!=0, with p in [0,1]^d and 1-A_p(0)>0; or
 (ii) an arbitrary probability law supported on the singleton sets {e_1,...,e_d}.

Let K_d be these components. A reference with at most M components is

 Q=r delta_0+(1-r) sum_{j=1}^M w_j B_j,
 r in [0,1], w_j>=0, sum_j w_j=1, B_j in K_d.                 (1)

Zero weights are omitted; r=1 means Q=delta_0 with no components. On d=0 the only law is delta_0. Empty mass is a separate single scalar, not a growing list of witness atoms.

The singleton components are needed for exact boundary closure. If p approaches zero, the product law conditioned on nonemptiness can converge to ANY singleton law, not just to a point mass. Indeed choose p_i=epsilon alpha_i. Put t=sum_i p_i. A union bound over pairs gives probability of at least two occupied coordinates at most t^2/2; Bonferroni gives nonempty probability at least t-t^2/2. For 0<t<=1/2 this denominator is at least t/2, and the conditional multiple-occupancy mass is at most t. The singleton probabilities divided by p_i/t tend to one wherever p_i>0, by the finite product formula. Thus conditional singleton probabilities tend to alpha_i. All sums have fixed finite d.

Conversely K_d is compact. For any convergent subsequence of product parameters p, if its limit is not zero, the nonempty denominator has a positive limit and ordinary continuity gives a component of type(i). If p tends to zero, the same finite expansion shows that every limiting law is supported on the singletons; pass to a subsequence of p/sum p in the compact simplex. Type(ii) is itself compact. Thus mixtures of at most M such components, with a separate vacuum scalar, form a compact class. No spectral-source contraction coefficient is assumed or inherited.

## 2. Every physical marginal keeps at most M components

Project onto ANY remaining coordinate set R, including the empty set. For a component A_p conditioned on nonemptiness, the probability that the remaining set is nonempty is

 a_R=[1-A_{p_R}(0)]/[1-A_p(0)].                              (2)

If a_R>0, its conditional law on remaining nonempty sets is exactly A_{p_R} conditioned on nonemptiness. The rest becomes vacuum. If a_R=0 the whole component becomes vacuum. For a singleton component with weights alpha, a_R=sum_{i in R}alpha_i, and the nonempty residual is the normalized restriction of alpha to R. There is no division when a_R=0.

Multiply each old mixture weight by a_R, move its lost mass into r, and normalize the remaining component weights when their sum is positive. This gives the EXACT complete marginal pi_R Q in the same class with at most M components. In particular its empty mass includes all formerly nonempty atoms whose remaining coordinates vanish. No mass is discarded.

This is the reference update at an actual Boolean query. If parent Fourier amplitudes at paired labels are a_T,b_T, the two child squared masses are (a_T+b_T)^2 and (a_T-b_T)^2, whose mean is a_T^2+b_T^2=pi_i P(T). Each child mass is at most 2 pi_i P(T). Therefore a reference covering P has a marginal covering BOTH physical children. The true signed child laws are recomputed; they are not replaced by the reference marginal.

## 3. Affine moment calibration also keeps at most M

Let P be ANY law covered by Q. Prescribe U(0)=P(0), and any finite collection of affine occupancy moments

 E_U a_l(S)=E_P a_l(S),  a_l(S)=sum_i c_li S_i.              (3)

Examples include total influence |S|, every individual influence, or any chosen linear combinations. The information projection minimizes D(U||Q) subject to (3). Its feasible set is compact and contains P, so a minimizer exists; strict convexity on the supported coordinates gives uniqueness.

First suppose the nonempty target moment is in the relative interior of the convex hull of Q-supported nonempty feature vectors. There is then a feasible law positive at every supported atom: the barycenter of all those atoms is relatively interior, and a short extension of the segment from that barycenter through the target expresses the target as a positive mixture of the barycenter and another feasible moment. The minimizer is positive on all those atoms, since mixing any proposed zero with that positive feasible law has a strictly negative epsilon-log-epsilon directional term, which dominates the finite linear terms. Finite-dimensional Lagrange multipliers therefore apply on the positive face and give

 U(0)=P(0), U(S)=C Q(S) product_i t_i^{S_i}, S!=0, t_i>0.   (4)

Redundant features do not affect the law. For type(i), multiplication by product_i t_i^{S_i} changes the product parameters to

 p_i'=p_i t_i/(1-p_i+p_i t_i),                              (5)

and changes its mixture weight by its finite positive nonempty normalizer. Denominators in (5) are positive for t_i>0, including p_i=0 or1. For type(ii), replace alpha_i by alpha_i t_i and normalize. Changing the empty mass affects only r. Thus (4) remains in the family with at most M components.

Boundary target moments do not require new components. On the nonempty support mix the target moment with epsilon times the reference moment. The mixed moment lies in the relative interior of its convex hull. Its projections have the above form and belong to the compact M-component class. As epsilon decreases to zero, their limits give the boundary projection. To check the limit, for any feasible target law V use V_epsilon=(1-epsilon)V+epsilon Q_tail. These laws have the mixed moments, and D(V_epsilon||Q_tail) tends to D(V||Q_tail), by continuity on the finite Q-supported alphabet. Minimality of each interior projection, compactness, and uniqueness prove convergence to the target projection. This uses finite sums and continuity, not an unlicensed infinite interchange.

If P(0)=1 the projection is delta_0. If Q has no nonempty mass, covering forces this same case. If P(0)=0, retain zero vacuum mass. A zero reference vacuum is allowed only when P(0)=0. All conditional normalizations used above have positive mass in their nontrivial cases.

For completeness, the projection identity also holds at the boundary. Let E be the minimal face of the convex hull containing the target nonempty moment. Every feasible law, including P_tail, is supported on the Q-supported feature vectors in E: a supporting linear functional has its extremal expectation only when it is extremal almost surely. On E the target is relatively interior, and the same finite multiplier argument applies there. The projection is positive at all those supported atoms. Hence log(U/Q) is affine in the prescribed features on the support of P, together with a separate vacuum constant. Matching moments gives

 CE(P,U)-CE(P,Q)=-D(U||Q)<=0.                              (6)

For a supplied scalar subprobability sQ, 0<s<=1, use sU. The scalar penalty -log s cancels in (6); it is not refunded or renormalized away. This is a universal compatible calibration interface, not a construction of a cheap initial source.

## 4. The complete stopping-tree account

At a physical query write Pbar=pi_i P and Qbar=pi_i Q. Define

 B_i=H(P)-H(Pbar),
 K_i=D(P||Q)-D(Pbar||Qbar)
    =E_{Pbar} D(P(S_i|S_-i)||Q(S_i|S_-i))>=0.              (7)

All conditional expressions are restricted to positive Pbar; coverage makes their reference denominators positive. Chain rules give

 B_i+mean CE(P_child,Qbar)-CE(P,Q)=-K_i.                   (8)

Calibrate each child reference to U_child by section3, and let R_child=D(U_child||Qbar). From (6)--(8),

 CE(P,Q)=B_i+K_i+mean R_child+mean CE(P_child,U_child).     (9)

Iterating on ANY finite adaptive physical stopping tree proves

 CE(P_root,Q_root)
 =sum_v reach_v(B_v+K_v)
   +sum_calibrations reach_child D(U_child||Qbar_parent)
   +sum_leaves reach_leaf CE(P_leaf,Q_leaf).               (10)

In (10), each calibration uses its actual immediately incoming reference. For one calibration after a query this is Qbar_parent; for consecutive calibrations it is the preceding calibrated reference. Iterating (6) includes every such release separately, with no extra query or new reserve. An initial root calibration adds its own nonnegative projection release on the right. Every full terminal, query KL contraction, scalar mass and old original-account debit remains. At every node the component count is at most the ORIGINAL M; it is not multiplied by the number of queries or leaves. Local identities prove (10) for arbitrary adaptive policies, including outcome-dependent stopping. Adding an unrelated reserve or replacing Q_root by a cost-free matched law is not allowed.

True child entropy and conditional auxiliary entropy remain those of their actual full spectra. If U,V are any partition of current frequency coordinates, H(V|U)=H(P)-H(P_U) is retained, not replaced by entropy of a component label. Actual physical query influence is sum_T b_T^2 and satisfies I(f)=Inf_i(f)+mean I(f_child); the reference construction neither erases phase energy nor assumes it equals a KL release. Equation (10) prices erasure/reference costs from a SUPPLIED complete root source; no initial influence price follows.

## 5. Representation cost is reduced, not made free

Every type(i) component is an exact mixture of at most d ordinary coordinate-product laws: partition its support by the first occupied coordinate j. The weight is

 eta_j=p_j product_{k<j}(1-p_k)/[1-product_k(1-p_k)],

and the conditional law fixes S_1=...=S_{j-1}=0,S_j=1 while keeping the later Bernoulli coordinates independent. The eta_j sum to one by telescoping; zero terms are omitted. Type(ii) is a mixture of at most d deterministic singleton products. Therefore every Q in (1) is an ordinary product mixture with at most 1+dM components. This representation bound is sharp at d components for the fair product conditioned on nonemptiness: its zero vacuum forces every positive product component to fix some coordinate to1, and no such component can cover two different singletons. Every singleton has positive mass. This is a statement about references, not an assertion that this punctured fair law is a Boolean spectrum.

Consequently the previously independently accepted A079 defect-source bound still gives, for d=3r and these target references,

 D(P_r||Q)>=max(0,r*tau-(3/4)log2(1+3rM)).                 (11)

An exponential number of individual residual atoms is therefore not required by the hereditary format, while a bounded latent format still does not make arbitrary retained entropy free. Equation (11) is applied only to its specified fixed Boolean source, not reissued to arbitrary physical descendants.

For A096's actual even-dimensional product of AND2 signs, P is uniform and q=(P+delta_full)/2. It belongs to this new family with at most TWO nonempty components: the fair product conditioned on nonemptiness, and the deterministic full set. Its separate vacuum is 1/(2*2^d). Vacuum calibration and the exact cardinality projection keep at most those two components, although A096 correctly proves that a positive true-law component plus individual nonnegative atom corrections needs exactly 2^d-d atoms after that projection. These are different representation classes; the new model does not refute its count.

## 6. Source reviews and first unsupported universal line

A096's finite vacuum/influence projection identity is reconstructed in section3, including boundary means, covering and scalar mass. Its individual-atom count remains valid at its stated scope. A032's flat-parent obstruction is also valid: its actual terminal law has m complemented copies of one fair spectral bit and one independent fair bit, giving optimal contraction m and total correlation m-1. Conditioning on the copied bit yields an exact two-product reference. The reference family here includes those laws, but does not give them a renewed fixed-source 7/4 coefficient. The original spent influence(m-1)/2 and both terminal frontiers remain as in that source.

First unsupported universal line: construct a useful ORIGINAL reference in this hereditary family with CE(P_f,Q)<=C I(f), M and its descriptive costs controlled noncircularly for EVERY Boolean f, or justify a productive selected policy with complete terminal costs paid from the same unused original owner. Any finite spectrum can be represented with sufficiently many deterministic components; this tautology does not price its entropy. The new result removes representation growth during inherited marginals/affine calibrations, while leaving the initial arbitrary-core supplier and full FEI open. Independent review of this new interface is pending.
