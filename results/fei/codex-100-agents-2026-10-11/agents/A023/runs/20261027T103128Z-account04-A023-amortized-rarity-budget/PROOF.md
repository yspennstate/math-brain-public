# One original influence account for queries and first-mark conversion

The signed terminal conversion and all query influence fit in one original influence account. The stronger bound keeps the unmarked terminal influence as an explicit refund. This concerns influence charges; arbitrary query KL charges and initial source admission remain unpaid.

## Statement

Let f be Boolean on a finite uniform cube. Let T be any finite adaptive physical restriction tree: each internal node queries a coordinate not previously queried on that path, both fair children are retained, and decisions depend only on the revealed history. Leaves may be nonconstant. Write p_v for physical reach, f_v for the actual restriction, J_v=I(f_v), and a_v=Inf_{i(v)}(f_v). A prefix-free set M of nodes declares a persistent mark. No path marks twice. Nodes outside all marked subtrees are unmarked. All logarithms are in bits.

At any marked node with J_v>0 set e_v=min(1/2,J_v/4), q_v=(1-e_v)P_v+e_v u_v, where P_v is the actual squared Fourier law and u_v is uniform on its remaining frequency cube. For J_v=0 set q_v=P_v. Let r_v be any supplied normalized probability reference with positive mass on the support of P_v. Put D_v=KL(P_v||q_v)-KL(P_v||r_v). The second KL is retained in full.

The first mark at v incurs D_v. Each subsequent realized edge in its subtree incurs D_child-D_parent. Let C be the expected total signed conversion charge, with zero charge on unmarked paths. Let Q=sum_internal p_v a_v. Then

    C <= L_M := sum_marked_leaves p_l J_l,
    Q + C <= J_root - L_U,

where L_U=sum_unmarked_leaves p_l J_l. More precisely, if Q_post=sum_internal_marked p_v a_v and B_M=sum_first_marks p_v J_v, then

    B_M=Q_post+L_M,
    J_root=Q_pre+B_M+L_U=Q+L_M+L_U.

These are identities, not independent descendant grants. A mark at an internal node belongs to Q_post. A mark at a leaf requires no query. A mark at the root is allowed. With no marks C=L_M=B_M=0. Constants and zero-influence coordinates are allowed.

## Proof

The physical restriction identity is J_v=a_v+(J_v0+J_v1)/2. It follows directly by partitioning the pivotal edges for every coordinate other than i(v) between the two physical children. Equivalently Fourier Parseval gives a_v=sum_{S containing i(v)} P_v(S), and the residual Fourier squares average to the marginal of P_v.

For any finite subtree rooted at v, induction on its number of internal nodes gives J_v=sum_internal_subtree (p_w/p_v)a_w+sum_leaf_subtree(p_l/p_v)J_l. The induction substitutes the two child identities, multiplying each by 1/2. The root-only case is immediate. Thus the statement includes arbitrary adapted stopping, with no infinite limit or optional-stopping integrability issue.

Apply this identity to each first-mark subtree. They are disjoint because M is prefix-free. Summing gives B_M=Q_post+L_M. Apply the same identity to the pruned tree stopping at first marks and at unmarked leaves: J_root=Q_pre+B_M+L_U. Substitution gives the complete partition. No mark subtree can reuse an ancestor or sibling account.

The smoothing bound is the stage22 lemma, reconstructed here. Since q_v >= (1-e_v)P_v, 0<=KL(P_v||q_v)<=-log2(1-e_v). For 0<J_v<=2, integration of 1/(1-t)<=2 on [0,e_v] gives -log2(1-e_v)<=2e_v/ln2=J_v/(2 ln2)<J_v; ln2>1/2 follows by integrating 1/t>1/2 on [1,2]. For J_v>=2 the bound is <=1<=J_v. At J_v=0 both P_v and q_v are the same point law. Normalization of r_v is used precisely in KL(P_v||r_v)>=0. Therefore D_v<=J_v. Positivity on spectral support is used precisely to make the old KL finite and the signed differences well-defined. Full support away from that support is unnecessary.

For a marked root-to-leaf path the realized charges telescope to D_l. Conditional expected increments alone do not telescope pathwise; after multiplying by physical reaches they give the same expected identity. Thus C=sum_marked_leaves p_l D_l<=L_M. Combining with the partition proves both inequalities. Negative D and negative conversion increments remain in the ledger.

## A genuine strengthening and its limits

Stage22 bounds C by J_root as a separate extra original coefficient. The present bound reserves only L_M and proves Q+C<=J_root-L_U. Consequently, if another argument already allocates rate one to Q from this same original account, conversion uses its actual unspent terminal portion. It does not require an additional rate-one copy. This conclusion applies only to that named account: an existing source or other invoice may already consume its remainder. A query invoice larger than a_v is not paid here. In particular query KL, old source cross-entropy, old debits, sibling terminal entropy and the campaign's other reserves cannot be dropped.

For comparison with an old budget lambda*Q+C, lambda>=1, the exact result is lambda*Q+C <= lambda*J_root-(lambda-1)*L_M-lambda*L_U. The displayed rate-one statement is enough for the no-reuse application.

## Nontrivial family and exact stopping rule

Let f_n=1-2*1{x=0} on n>=2 bits. Query x_1. Mark only the x_1=0 child. In that marked branch query x_2 and then stop; in the x_1=1 branch stop immediately. Both terminal laws, including the nonconstant residual point defect, are retained. Then

    J_root=2n*2^-n, Q=4*2^-n,
    L_M=2(n-2)*2^-n, L_U=0.

Thus the actual conversion is <=2(n-2)*2^-n and Q+C<=2n*2^-n for every n>=2. The old bound allows 2n*2^-n even after the actual query cost was paid. For n=2 the leaves are constants and the conversion is nonpositive. This is a complete conversion-plus-query-influence bound on an unbounded Boolean family; it is not a new FEI class theorem. Querying all remaining bits makes L_M=0 and C<=0, which is consistent because the root source still carries the original entropy.

## What remains open

Initial CE(P_v,q_v)=H(f_v)+KL(P_v||q_v) lies in [H(f_v),H(f_v)+J_v]. A universal O(J_v) initial supplier remains equivalent to FEI up to one additive constant. This proof does not construct it. The new ledger is a sharper universal conversion lemma with exact original ownership, not a solution of C000. Independent-person review is pending.

## Adversarial checks of the hypotheses

Persistence and the prefix-free rule matter. On two-bit parity, opening a full grant at the root and again at both children grants 2+1=3 against original influence 2. The subtree identity instead charges the root grant once, leaving only one influence unit after the first query.

Keeping signs matters. For the three-bit point defect, P=(9/16,1/16 repeated seven times), J=3/4 and e=3/16. Thus q=(123/256,19/256 repeated seven times). If the old reference is P itself, the first signed charge is strictly positive: 16*D=log2[(48/41)^9(16/19)^7]>0, as certified by the exact integer inequality 48^9*16^7>41^9*19^7. Querying all bits ends at constants, so the full signed conversion is zero and L_M=0. Discarding its later negative increments would violate C<=L_M.

Normalization of the old reference matters. At a constant, the inadmissible measure r=2P has KL(P||r)=-1, hence D=1>J=0. A subprobability old reference with support coverage would also suffice for the upper bound, but the statement uses a normalized law; a measure of mass greater than one is excluded.

An arbitrary physical-query KL is a different invoice. The two-bit point defect has uniform spectrum on four atoms; both its tuned root reference and its projected one-coordinate marginal are uniform. Its two physical children have point spectra on opposite residual atoms. Their average KL to that marginal is exactly 1, whereas the queried influence is 1/2. Thus a blanket query-KL<=queried-influence substitution is false. The theorem never makes it.
