# Interleaved selector reserve (bits)

## Scope and prior-source correction
Let a controller on a finite uniform cube choose one of finitely many Boolean cores on pairwise disjoint independent uniform data cubes, or constant signs. Labels selecting the same physical core must be merged. All physical coordinates can be queried adaptively, with arbitrary stopping. Conditional on an actual reached cylinder, unrevealed blocks remain independent and uniform. Selector probabilities q_j and core means m_j, variances V_j=1-m_j^2 are recomputed on that cylinder.

The prior A057 stage3 PROOF sections 1,3,4 pay the exclusive-controller DATA-ONLY cap and its unnormalized coherent concavity gap. A087 independently reconstructed exactly those sections without repair. The prior final paragraph denying arbitrary-controller reserve payment is stale and false scope prose: Section 3 already proves that payment. This run corrects the interpretation, without rewriting the archived run. The remaining inner/terminal debt was not affected. Projected-sector spectral weights are not physical branch weights; branches always have weight 1/2.

## 1. One potential for every physical history
Put r(q)=q log2(1/q), with r(0)=0, and

    R(F_state)=sum_j r(q_j) V_j.

At a data query of core j, q_j stays fixed, its child means are m_j+/-beta, and all other core variances stay fixed. Therefore

    R_parent-E R_child = r(q_j) beta^2.

At a controller query, every core mean and variance stays fixed, and q_j=(q_j,+ + q_j,-)/2. Concavity of r gives the exact nonnegative release

    L_ctrl=sum_j V_j[r(q_j)-(r(q_j,+)+r(q_j,-))/2] >=0.

For q_j>0 its bracket is q_j[1-h2(q_j,+/(2q_j))]. This is the amount released, not a newly assigned reserve in either child. With h2(z)>=2min(z,1-z), the bracket is <=|q_j,+-q_j,-|/2. The difference of slice probabilities is at most the original physical query influence of selector C_j. At a control edge switching distinct cores j,k, independence gives mismatch d_jk=(1-m_j m_k)/2 and V_j+V_k<=4d_jk; constants have variance zero and the identical inequality. Hence

    0<=L_ctrl<= (1/2)sum_j V_j Inf_i(C_j)<=2 Inf_i(F_state).

This last local bound is sharp: one fair bit chooses two disjoint dictators. Both core variances are 1 and both selector probabilities are 1/2, so R_parent=1,R_children=0, while Inf_control=1/2. The two variance charges are counted on one physical edge.

Thus R is a supermartingale on EVERY physical query tree. On any finite stopped tree T,

    R_root-E R_leaf
       =sum_data_nodes w r(q_j) beta^2 +sum_control_nodes w L_ctrl.

No fair weights are replaced by spectral weights. Adaptive branches are actual product cylinders; all releases telescope on those same branches. This identity covers any number of alternating data/control phases, not merely one reset.

## 2. The same cap price under arbitrary interleaving
At each reached data node retain the prior exact split, with C_j the current restricted selector, a=W_j+m_j C_j, c=C_j,

    M(s)=sum_T Phi(ahat(T)^2,s chat(T)^2),
    cap=min{M(V_j),(t/V_j)M(V_j)+q_j t log2(V_j/t)}, t=beta^2.

Zero t or variance gives cap zero. Current q_j=0 also gives zero. The already independently reconstructed local bound is

    M(t)<=cap<=c_data Inf_i(F_state)+r(q_j)t,
    c_data=(1+2/e)/ln2.

It retains t log2(1/t) before maximizing it against physical influence. For completeness, M(V_j)<=h2(q_j V_j), and the cap's two variance logarithms cancel exactly: q_j t log2(1/V_j)+q_j t log2(V_j/t)=q_j t log2(1/t).

Weighting on the interleaved tree and using Section 1 yields the stronger stopped bound

    bank_data <=c_data Pi_I,data +R_root-E R_leaf
                                      -sum_control w L_ctrl.

In particular bank_data<=c_data Pi_I,data+R_root. Indicator edge isoperimetry and the simultaneous edge variance inequality already proved in stage3 give R_root<=2 I_ctrl(root). The physical block-influence telescope gives Pi_I,data=I_data(root)-E I_data(leaf)<=I_data(root), even when controller steps intervene. Controller steps have zero expected decrement of the data-block influence; data steps consume exactly their queried influence. Consequently

    bank_data<=c_data I_data(root)+2 I_ctrl(root)<=c_data I(F_root).

For the unnormalized coherent concavity gap N at data nodes, 0<=N<=2q_j t/ln2<=2 Inf_i(F_state)/ln2. Thus cap+N on arbitrary interleaved trees is at most

    c_rem Pi_I,data +R_root-E R_leaf-sum_control w L_ctrl,
    <=c_rem I_data(root)+2 I_ctrl(root)<=c_rem I(F_root),
    c_rem=(3+2/e)/ln2.

These are prices of DATA-NODE outer banks. They do not include erasure/decrement at controller nodes. The root 2I_ctrl account funds R once; its release is subtracted in the stopped bound and cannot be charged again as an additional positive resource.

## 3. Exact signed ledger with controller steps
Let phi(s)=s log2(1/s), E_ne(u)=H(u)-phi((Eu)^2), and U_state=sum_j q_j E_ne(u_j). At a data query of core j,

    Delta H(F)= q_j[E_ne(u_j)-E E_ne(u_j,child)]
                 -q_j phi(beta^2)+M(t)+N(t).

At a controller query U_parent=E U_child, since core functions stay fixed and selector probabilities average to their parent values. Consequently every stopped interleaved physical tree satisfies exactly

    H(F_root)=E H(F_leaf)+U_root-E U_leaf
               -sum_data w q_j phi(beta^2)
               +sum_data w(M+N)+sum_control w Delta_i H(F_state).

There is no extra inner-entropy reset toll from changing selector probabilities. The actual controller entropy decrement remains, separately and honestly. The data-only specialization is precisely A087-STOPPED-SELECTOR-SIGNED-ENTROPY-LEDGER@1 and is independently accepted here without repair. Its unequal projected-sector mass and different-frontier warning are preserved.

## 4. First unpaid line
One still needs to pay E H(F_leaf)+U_root-E U_leaf-sum_data w q_j phi(beta^2)+sum_control w Delta_i H(F_state), with the same exclusively owned influence. The selector reserve does not pay this expression. An arbitrary Boolean controller selecting constant signs has R=0 and no data bank while its entire H remains in the controller/terminal terms; thus this extension cannot itself imply FEI. Shared physical data between distinct selected cores is excluded: then the mismatch identity requires their actual correlation rather than m_j m_k.

The controller release is not its entropy decrement, even with nonconstant independent cores. In A030's arbitrary-controller two-dictator wrapper take h(x,z1,z2)=(z1+z2+x(z1-z2))/2 and F=(u+v+h(u-v))/2, where u,v are fresh dictators. Both x children have balanced selector probabilities, so R_parent=E R_child=1. F has two Fourier amplitudes 1/2 and eight amplitudes +/-1/4, hence H(F)=3. Each x child is a simple mux with four amplitudes +/-1/2, hence H(child)=2. Thus L_ctrl=0 but Delta_x H(F)=1, B_x=1/2 and Inf_x(F)=1/4. This is the inherited controller entropy term from A030's transfer, not a new FEI counterexample. A fixed exact certificate is in out/RESIDUAL.json. No multiple of release alone can pay this controller decrement.

The next shortest step is to combine this nonresetting R with an actual signed controller-decrement/reference transfer after a nonconstant data exposure. The history and budget compatibility of the outer bank is now settled for arbitrary interleaving; further fresh-event tests would not remove the arbitrary controller/core entropy in the exact remainder.
