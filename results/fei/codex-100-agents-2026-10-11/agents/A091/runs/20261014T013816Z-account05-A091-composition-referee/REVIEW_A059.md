# Independent interleaved reserve review

Target A059-INTERLEAVED-BIASED-STOPPING-RESERVE@1, source run 20261013T235852Z. Source statement hash 751c4dfb5c28dc0715e0148810bb712da3d72761db3c29b1f46995ec2d03ab21. Original contributors remain A059 and its named A056/A057 upstream contributors. This reconstruction supplies no substantive repair. Verdict: ACCEPT_AT_STATED_SCOPE after the executed frozen validation record is PASS; no universal controller/terminal price is accepted. The source dependency alias A056-BIASED-ERASURE@2 refers to the interface BIASED_ERASURE_INTERFACE.json exported under A056-DISJOINT-COMPOSITION@2 in the A056 claim file. This is a ledger naming issue, not a mathematical repair. The exact used specialization is reconstructed below; B20 should reconcile that alias before index adoption.

Let exclusive indicators C_j on uniform controller coordinates partition all assignments. Each state chooses a Boolean u_j on its own disjoint data cube. At an actual physical restriction cylinder, independence and uniformity remain because the already observed history fixes coordinates. Means can be biased, selector probabilities may vanish, and constants are allowed. All quantities below are bits; influence means physical sign-flip probability, not indicator Fourier energy without its normalization factor.

Write q_j=E C_j, m_j=E u_j, V_j=1-m_j^2, eta(x)=x log2(1/x), U=sum q_j[H(u_j)-eta(m_j^2)] and R=sum eta(q_j)V_j. A controller query changes q_j to two actual slice probabilities with average q_j. Therefore U has zero expected drift, and the R drift is

    kappa=sum_j V_j[eta(q_j)-E eta(q_j,child)]
          =sum_{q_j>0} q_j V_j D_2(P(X|C_j)||fair)>=0.

The equality follows by inserting P(X=+|C_j)=q_j+/(2q_j); it includes one zero slice and omitted unreachable q_j=0 states. These are physical probabilities, not arbitrary posterior weights.

For a data query in state j, q_j stays fixed and m_child=m+/-beta. Thus V-E V_child=beta^2=t, and R-E R_child=eta(q_j)t. The actual coordinate influence is q_j Inf_i(u_j), with no nominal event duplication.

Put W=sum_{k!=j} C_k u_k, so C_j W=0 and W^2=1-C_j. Expand a=W+mC_j and c=C_j on the other coordinates. Parseval gives sum a_T^2=1-qV and sum c_T^2=q. At nonempty core frequencies the selector factor c_T multiplies the actual core coefficients; only the empty core row combines coherently into a_T. This independently gives

    D_iH(F)=q[D_iH(u)-paird(m,beta)]+M(t)+N,
    M(s)=sum_T Phi(a_T^2,s c_T^2),
    N=sum_T[paird(a_T,beta c_T)-Phi(a_T^2,t c_T^2)],
    paird(a,b)=eta(a^2)+eta(b^2)-E eta((a+/-b)^2).

Homogeneity applies to raw row entropies even when projected child masses differ; N is not silently replaced by a normalized equal-mass JS. The empty core identity paird(m,beta)=eta(m^2)+eta(t)-E eta(m_child^2) shows exactly

    D_iH(F)=U-E U_child+M(t)+N-q eta(t).

The cap bounds M(t) by min{M(V),(t/V)M(V)+qt log2(V/t)}. Entropy concavity bounds M(V)<=h2(qV), since the two grouped masses are 1-qV and qV. Combining h2(x)<=x log2(e/x) with the second cap branch gives

    cap<=eta(q)t+qt/ln2+q eta(t).

The full signed data step cancels q eta(t) against the actual negative empty-core term. The scalar N<=2qt/ln2 bound, independently reconstructed in POINT_CONTROL_PAYMENT.md, then yields

    D_iH(F)<=U+R-E(U_child+R_child)+(3/ln2)qt.

This is the source's 3/ln2 coefficient, not the larger standalone positive cap price. Nonnegative raw N and all q=0,t=0,V=0 cases are defined directly. For the positive cap alone, eta(t)<=2 Inf_i(u)/(e ln2) gives c_data=(1+2/e)/ln2 times the physical data influence, plus the exact R debit.

Finite physical telescoping, with the actual stopping leaves, proves exactly

    R_root=E R_leaf+sum_data w eta(q)t+sum_control w kappa,
    I_root=Pi_data+Pi_control+E I_leaf,
    H_root<=E H_leaf+U_root-E U_leaf+R_root-E R_leaf
                              +(3/ln2)T_data+sum_control w(D-kappa),
    sum_data w cap+E R_leaf+sum_control w kappa
                              <=c_data Pi_data+R_root.

Every allowance uses the same tree; no complete-tree or control-first leaf replaces an actual partial frontier. Adaptivity introduces no separate choice entropy because the policy is determined by recorded history.

Finally indicator edge isoperimetry in pivotal normalization is I(C)>=2q log2(1/q). Slice induction proves it: use the slice inductive bounds, crossing influence >=|q_+-q_-|, and h2(z)>=2min(z,1-z). On each actual controller edge switching states j,k, disjoint data gives mismatch (1-m_jm_k)/2 and V_j+V_k<=2(1-m_jm_k). Summing original edges once yields sum V_j I(C_j)<=4I_ctrl, hence R_root<=2I_ctrl. An edge staying in one state has zero indicator change; it does not compare independent copies of the same core. This prevents an invalid extra mismatch account.

The initial 2I_ctrl funding is not an additional free controller payment. It supplies R once; the residual D-kappa and terminal H-U-R remain in the ledger. With constant cores U=R=kappa=0, an arbitrary Boolean controller remains, so universal pricing of that residual would still require full FEI-strength input. Shared physical data violates the mismatch and separate-core hypotheses and is excluded. The point-controller extension is supplied by A091 in a separate note and is not attributed to the reviewed source claim.

Validation uses an independent direct centered-moment state representation, actual controller slice probabilities and true core tables, independent raw outer rows, prime-log identities and rigorous rational signs. New source-author code is not imported. Own prior exact primitives are transparently reused. The frozen generic-controller and fresh-point jobs verify every reached node and all depth frontiers, plus both exact controller KL and the signed data cancellation. Finite checks corroborate the all-dimensional argument above; they do not establish universal terminal admission.
