# Candidate: priced prefix reserve with a retained controller boundary

Stage 20261013T235917Z. All entropies in bits. Let a finite physical controller on z exclusively select independent, disjoint Boolean cores u_j on x_j, or constant signs. C_j are its disjoint 0/1 indicators, q_j=E C_j. Merge distinct descriptions selecting the same physical core before defining q_j. Data queries are adaptive and interleaved; controls are untouched during this prefix. Every reached history still has independent fair unqueried data bits.

Each core has a prescribed finite fresh-coordinate continuation tree T_j and a nonnegative potential r_j on that tree satisfying D_j<=C d_j+r_j-E r_j(child). The reserve depends only on that core's own history and any independent seed fixed initially. The core can have a stopped terminal, but its terminal entropy is retained separately. For Snell applications r_j is Q_C(u_j,T_j), with zero potential at its specified leaves. Interleaving must respect these continuation trees; the global stopping rule may stop at any data history. Arbitrary core difficulty is inherited in r_j(root), never assumed paid.

Define ell_j=log2(1/q_j), zero q_j terms zero, and

    V_t=sum_j q_j ell_j Var(u_j,t),
    R_t=sum_j q_j r_j(u_j,t)+V_t.

With kappa=(3+2/e)/ln2<11/2 and alpha=C+11/2, the intended theorem is

    D_F,t <= alpha d_F,t + R_t-E[R_next|history],
    R_0 <= sum_j q_j r_j(root)+2 I_ctrl(F).

Proof: the exact A087/A057 split is D_F=q_j[D_j-paird(m,beta)]+M(t)+J, t=beta^2. The crucial scalar paird is nonnegative: paird(m,beta)=Phi(m^2,beta^2)+[phi(m^2+beta^2)-avg phi((m+/-beta)^2)]>=0, by homogeneous binary entropy and concavity of phi. The positive-sector bound yields M+J<=kappa q_j d_j+q_j ell_j beta^2. Use d_F=q_j d_j, the core potential drift and Var(u_j)-E Var(child)=beta^2. No negative corrected-inner entropy or normalized projected-sector shortcut is needed. The edge-owned rarity estimate V_0<=2I_ctrl(F) is reconstructed below; this capacity is reserved once for V and is not renewed at descendants.

For a specified data-only prefix with terminal potential zero, backward induction of the nonnegative Bellman recursion proves Q_alpha(F,prefix)<=R_0, since R at the prefix leaves is nonnegative. This is a nonnegative-prefix reserve theorem, not just an additive whole-tree debt identity. It works under any interleaving respecting T_j, including stopping based on other cores. The prescribed policy and its boundary are part of the statement.

At a partial stopping frontier sigma, R_sigma=sum_j q_j r_j(remaining)+sum_j q_j ell_j Var(remaining). Its expectation is explicit and nonnegative, not generally zero. When every core is exhausted to a constant, R_sigma=0. Actual remaining function F_sigma is then a control function and still has entropy. Zero data-prefix reserve does not erase it.

To include a specified control continuation on each complete-data frontier, let b_sigma be any nonnegative potential for that ACTUAL control tree at the same price alpha (e.g. its least reserve). Add A_t=E[b_sigma|history] to R_t. This is a nonnegative martingale, so the prefix drift is unchanged and at the frontier the total potential equals b_sigma. It grafts to the declared controller continuation without reset. Its initial bound is

    Q_alpha(F,full policy) <= sum_j q_j r_j(root)+2 I_ctrl(F)+E b_sigma.

No second reservation of the same control influence is hidden: the full control account is explicitly 2 I_ctrl plus the boundary debit E b_sigma. If E b_sigma<=K I_ctrl is separately proved, that account has rate 2+K, not max(2,K). This final bound is conditional on that boundary proof and the actual core reserve bounds.

# Independent reconstruction of A087's stopped signed ledger

Put phi(s)=s log2(1/s), E_ne(u)=H(u)-phi((Eu)^2). The exact scalar identity paird(m,beta)=phi(m^2)+phi(beta^2)-E phi(m_child^2) yields

    D_j-paird(m,beta)=E_ne(u_j)-E E_ne(u_j,child)-phi(beta^2).

Finite telescoping along the actual interleaved prefix gives exactly A087-STOPPED-SELECTOR-SIGNED-ENTROPY-LEDGER v1. At a projected empty-core sector with mass M0, child masses M+/-=M0+/-2qm beta have physical weights 1/2, but normalized spectral weights rho+/-=M+/-/(2M0). Homogeneous entropy algebra gives J=M0 JS_rho+M0[1-h2(rho+)]. That second mass term must be retained. The proof is valid with zero masses by continuity. This is the subclaim to review independently, using a separate raw-truth-table Walsh/edge implementation.

# Controller account and boundary obstruction

For an indicator C with measure q, edge isoperimetry in probability-of-change normalization gives I(C)>=2q log2(1/q). One can reconstruct it by splitting the cube into slices and using h2(s)>=2 min(s,1-s). At each original controller edge between states j,k, distinct data independence gives pivotal probability (1-m_j m_k)/2. The charged variance sum satisfies Var(u_j)+Var(u_k)<=2(1-m_j m_k). Constants have zero variance. Summing each original edge once gives sum_j Var(u_j) I(C_j)<=4I_ctrl, hence V_0<=2I_ctrl. Edges staying in the same state have zero selector charge. Shared controller coordinates are never owned independently by nominal events.

The boundary can retain an arbitrary controller seed even when every data core is a dictator with zero core Q_C at every price. Let h(z) be any Boolean sign and F=C0(z)y0+C1(z)y1 with C0=(1+h)/2,C1=(1-h)/2. Query the two independent dictator data bits first. For equal outcomes the actual control leaf is constant; for unequal outcomes it is +/-h. Therefore

    E H(F_sigma)=H(h)/2,
    E I(F_sigma)=I(h)/2=I_ctrl(F),
    E Q_alpha(F_sigma,declared T)=Q_alpha(h,T)/2.

The equality for reserves uses consistently sign-translated copies of one declared tree T and sign invariance. This is a precise remaining-boundary interface, not a new hardness claim for a previously known class. A universal linear entropy payment of this boundary implies FEI, and a uniform bound on its reserve still has to retain the full seed difficulty. Core certification and the positive outer bank alone cannot close it.

First unsupported universal line: there is a physical interleaved/core-controller policy with both inherited core reserve and actual boundary debit bounded dimension-independently by unused exclusive influence. The new potential controls the positive outer prefix but does not prove this universal admission.
