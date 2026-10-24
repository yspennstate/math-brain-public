# A finite adaptive history paid by one incoming source bank

Bits for all CE/entropy/KL; uniform physical influence throughout. This continues A095@4's support-completed point-selector reference. A094's one-query normalizer identity is consumed at its stated scope, not claimed as a new identity or a universal payment theorem.

## 1. Fixed source and allowed history

Let k>=1 and g be ANY Boolean core on k bits with prescribed normalized positive-support finite-cost reference R, raw cost c. Pad by m>=0 dummy bits, n=k+m, flip an arbitrary full vertex a and let M select g and its actual flip by one fresh fair bit. Write delta=2^-n, j for the original incident pivotal degree at a_x. The fixed incoming support-completed Q of A095@4 has

    CE_M <=c+delta[(5/4)2^k c+4n+3],
    I(M)=I(g)+delta(n+1-2j).

Its entire old conditional KL remains; no arbitrary edited-spectrum reference is substituted. Use any finite deterministic adaptive restriction tree T querying ONLY originally unqueried core coordinates. Padding, the selector and an optional independent terminal cube are never queried. Decisions and stopping depend only on queried core values. Apply the exact same physical tree to g as to M. Each node of depth d has reach2^-d; all leaf cubes retain every unqueried coordinate. The policy can leave both children nonconstant; no flatness or balance is required.

Let Pi_g=sum_v reach_v Inf_(i_v)(g_v), the actual original-core queried influence. Let the unique edited-vertex path query t_a coordinates, of which j_a originally pivotal edges at a are queried. These are fixed original edges, not recomputed reserve labels. Put j_rem=j-j_a. No coordinate repeats along a path.

## 2. Inherit the actual reference and keep its normalizers

At a node with actual normalized spectrum P and complete incoming Q, query a fair physical coordinate i. Let child spectra P_0,P_1, their average residual spectrum q=(P_0+P_1)/2, and r(T)=Q(T)+Q(T+i). On q(T)>0 define physical-child posterior pi_b(T)=P_b(T)/(2q(T)); on q=0 choose a fixed normalized posterior, retaining all r mass. Define raw child reference2r*pi_b and normalizer Z_b, then Q_b=2r*pi_b/Z_b. Support positivity ensures Z_b>0; Z_0+Z_1=2. This is a finite normalized reference determined before drawing child spectral output.

Direct row likelihood factorization gives

    D_parent-avg D_child=L_i-avg log2 Z_b >=0,
    CE_parent-avg CE_child=Delta_i+L_i-avg log2 Z_b >=0,  (A)

where L_i is the actual queried-membership conditional KL of P versus Q, and Delta_i=H(parent)-avg H(child)=B_i+JS_i>=0. The normalizer sign uses log concavity and Z_0+Z_1=2. No child is replaced by a fresh floor or independently influence-paid code. For independent supplied terminal R_q tensor Q, use product-compatible posteriors on zero terminal true fibers; Q_b=R_q tensor(core Q_b), so its whole c_q and D_q remain.

Iterating (A) in the finite tree defines the measured nonnegative release

    Gamma_T=sum_v reach_v[Delta_v+L_v-avg log2 Z_vb],
    E CE_leaf=CE_M-Gamma_T.                            (B)

Also D_M-E D_leaf=sum_v reach_v[L_v-avg log2 Z_vb]. Every descendant conditional KL and every actual child normalizer is retained. This uses the one-query identity repeatedly on the incoming model; there is no bank renewal.

## 3. Exact physical edit debit under adaptive queries

Away from the edited-vertex path the functions coincide. At depth d on that path, the remaining point has mass2^d delta. The queried influence of M differs from that of g by2^d delta*(1-2p_i), where p_i indicates whether the ORIGINAL incident edge at a was pivotal. Multiplication by actual reach2^-d cancels the depth. Thus the exact whole-tree queried influence is

    Pi_M=Pi_g+delta(t_a-2j_a),
    E I(M_leaf)=I(g)-Pi_g+delta[n+1-t_a-2j_rem].       (C)

These are literal edge identities, including disappearing original disagreements. They remain valid with branch-dependent query order and stopping because each affected edge is encountered only when its coordinate is queried on a's path. No rare-event mass is reset at a descendant.

## 4. One nonreused source bank pays the surviving terminal average

For K>=4 let S_K=K I(g)-c. Combine the root bound, (B) and (C):

    K E I_leaf-E CE_leaf >= S_K-K Pi_g+Gamma_T
      -delta[(5/4)2^k c+(4-K)n+K(t_a+2j_rem-1)+3].    (D)

This is an independently bounded incoming-reference surcharge with an explicitly measured optional refund, not the identity KI-H renamed as payment. The original source bank is used exactly once: K Pi_g is cumulative spend, and no child receives a renewed copy of S_K. Because j_rem<=k-t_a, the point-path bracket never exceeds

    (5/4)2^k c+(4-K)n+K(2k-1)+3.

Suppose raw c<=K0 I(g), K0>=0, K>=4,K>K0 and g nonconstant. Its total influence is at least2^(1-k). Put beta=Pi_g/I(g) and

    A(k,K0,K)=(5/4)K0+kK+(3-K)/2.

Dropping only Gamma_T>=0 and the favorable(K-4)n term, (D) proves the COMPLETE finite-history admission

    2^-m A(k,K0,K) <= K-K0-K beta
        ==> E CE(inherited leaf)<=K E I(actual leaf). (E)

The same original Q and normalizer transport are used through every query. No separate child certificate or reset is assumed. The right side must be nonnegative; a paid root alone does not imply (E). Constant cores have Q=P_M and inherited references P_leaf, so point-defect entropy pays each surviving leaf at4 independently of this nonconstant-core admission.

For any supplied4I core, K=6 and beta<=1/6 suffice with2^m>=6k+7/2. More sharply, use the actual beta in(E), not a new bank per node. This is uniform over all adaptive trees satisfying the physical influence-spend condition, all growing k and all edit vertices. The remaining terminal average is paid at6 with every source-reference debt preserved. It is a conditional nontrivial class theorem, not a universal existence result for a useful tree or core reference.

## 5. A weak non-flat exposure with two nonconstant children

Take g=h_3 h_2 on five disjoint active bits, h_L=1-2AND_L, and flip the all-zero full point. Its inherited product spectrum reference has c=H(g)<4I(g), I(g)=7/4, and unequal coefficient magnitudes3/8 and1/8. Query one coordinate in the width-three block: original influence1/4, beta=1/7; both original child cores remain nonconstant because the width-two second block survives. All five original incident edges at the point are pivotal, so the edit destroys the queried original edge. The actual first query is1/4-delta, not a strong fresh pivot.

At m=6, A=67/2 and2^-m A=67/128<2-6/7=8/7; (E) pays the whole inherited child average at6. If a second width-three coordinate is queried on the zero first branch, Pi_g=1/2,beta=2/7. At m=7,67/256<2-12/7=2/7, so the SAME bank pays this adaptive two-query history as well. No source slack was regenerated at the intermediate child. Exact terminal CE and physical edge certificates accompany the proof.

An independent arbitrary terminal q never funds the core history: product-compatible transport gives E CE_total=c_q+E CE_core and E I_total=I(q)+E I_core. If c_q<=C I(q), (E) gives max(C,K) at the surviving average. Its complete KL remains additive through the same actual normalizers. No uniform individual-leaf ratio is asserted; A094's incoming-descendant obstruction remains valid.

## 6. First unsupported universal line

The generic one-query reference identity is already known; the new result is its quantitatively paid adaptive source-bank continuation with the exact one-point-path edge debit. Universal closure still needs to pay histories exceeding (E), or construct a universally influence-paid original core reference. To remove the explicit influence-spend/padding admission, the measured Gamma_T and exact signed old log profile must fund the SAME cumulative request K Pi_g, including every terminal KL and normalizer. Neither a root certificate nor a fresh descendant floor proves that. NEXT targets an actual history just beyond (E), using its measured refund and inherited core-reference debt rather than adding another root class.
