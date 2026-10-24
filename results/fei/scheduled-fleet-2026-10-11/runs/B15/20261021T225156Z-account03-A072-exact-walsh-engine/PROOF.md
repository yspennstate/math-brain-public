# Mandatory donor payment on an inherited account

Entropy is in bits. Let a parent and its two physical children have full slacks S=K I-H and S_0,S_1. Write e=H-parent minus mean child H minus K times the queried physical influence. Exact influence telescoping gives mean S_c=S+e. Let D be the previously booked debit, R=S-D the unused parent bank, and T=D+e the required outgoing mean debit. These are the original quantities, with no rate change or fresh quota.

Suppose a child is decomposed into a selected raw bank U_c and a signed other-component remainder M_c, so S_c=U_c+M_c. Define W_c=max(M_c,0) and V_c=U_c-max(-M_c,0)=S_c-W_c. Assume V_c>=0 (and hence S_c>=0). Averages below give each physical child weight 1/2.

The exact shortfall identity is

    T-mean V_c = mean W_c-R.

Indeed mean V+mean W=mean S=S+e, and subtracting S-D proves the identity. No sign, small-bias, independence or entropy bound is used in this accounting step. The hypotheses V_c>=0 enter only in the allocation theorem below.

For 0<=T<=mean S_c, choose child debits 0<=d_c<=S_c with mean d_c=T. Among all these choices, the least mean other-owner payment mean max(d_c-V_c,0) is exactly

    max(0,T-mean V_c)=max(0,mean W_c-R).

The lower bound follows pointwise from max(d_c-V_c,0)>=d_c-V_c and from nonnegativity. For attainment, if T<=mean V and mean V>0, set d_c=(T/mean V)V_c. This uses no donor and respects all caps. If mean V=0, this branch forces T=0, and d_c=0 works. If T>mean V, then mean W>0 because T<=mean(V+W). Set theta=(T-mean V)/mean W, which lies in (0,1], and d_c=V_c+theta W_c. This respects all caps and attains the lower bound. In particular the formula never divides by zero in the branch that uses it. If T=0, all bookings can be zero; if W vanishes, the donor branch is unavailable and unnecessary.

If the inherited account is saturated, D=S and R=0. Then T=mean S_c, so every feasible child debit must equal S_c: otherwise one strict deficit and the other nonnegative deficit give a strictly positive mean deficit. Consequently every positive W_c is fully spent, and the least donor payment is mean W_c. Any later argument that counts these same W_c as still unused renews a spent reserve. This is an obstruction to a proposed component ownership rule, not a counterexample to FEI.

For label preservation, let the booked labels sum to D. If T>0, multiply each outgoing child debit by L/T for each original label L and by e/T for the new signed query label. Each original label still has mean L, the new one mean e, and all labels sum to d_c. Negative e is permitted as a signed label; no assertion of nonnegative new credit follows. When T=0, proportional label transport is undefined and needs a separate signed-label convention; the theorem on total debit does not require it. All finite cases in this run certify T>0. The original two-stage prefix labels inside D retain their preexisting split, and all stopped prefix terminals and their reach weights are unchanged.

# How the signed components are obtained without assuming FEI

For a disjoint composition F=h(g_1,...,g_m), let q_j be the pivotal probability of outer coordinate j under the actual core means. If each core has its independently certified slack S(g_j), the exact occupied-block chain rule gives

    H(F)=sum_j q_j H(g_j)+C,
    I(F)=sum_j q_j I(g_j),
    C=H(occupied block mask)-sum_j q_j h2(Var(g_j)).

Thus the selected raw bank is U=q_j S(g_j), the other bank is A=sum_(l!=j)q_l S(g_l), and M=A-C. Every finite value here is reconstructed from core integer Walsh spectra and a rational outer product-measure law. No full FEI hypothesis is used. For a physical query in block j, the other q_l average to their original values, giving mean A_child=A_parent. The symbolic checker verifies this identity and

    e-(mean U_child-U_parent)=C_parent-mean C_child.

This gives a component-level explanation of the shortfall, rather than an unproved appeal to a full-child slack. However, knowing this decomposition does not ensure V_c>=0 for arbitrary cores, nor that a transferable donor has not already been spent. Those remain the unpaid universal hypotheses.

# Checks that can falsify the result

The coefficient checks must fail on a wrong Fourier normalization or a non-Boolean inverse; independent edge counts must fail on a mislabelled restriction; exact profile cancellation must fail if a C term, terminal core or old debit is dropped; the saturated identity must fail if the parent receives a renewed bank. The finite run retains both physical children, verifies all these identities, checks strict signs by outward logarithm intervals, and exercises both donor and zero-donor branches. The zero-denominator branches and T=0 are handled in the proof, not claimed to appear in this particular family. A Lean check of the accounting equality was attempted but compute admission refused to launch a compiler; no Lean certification is claimed.

Both component nonnegativity hypotheses matter for the allocation formula. Dropping W>=0 permits V=(1,0), W=(-1,1), S=(0,1), T=1/2: the unique feasible debit is (0,1), with mean donor1/2, although max(0,T-mean V)=0. Dropping V>=0 permits V=(-1,1), W=(1,0), S=(0,1), T=0: the unique debit is zero, with mean donor1/2, again contradicting the claimed zero formula. These are counterexamples to weakened account lemmas, not Boolean witnesses. Their rational arithmetic is checked in out/HYPOTHESIS_CHECKS.json.

# First unsupported universal line

For every Boolean core and every inherited history there is a physical query whose children have V_c>=0 and enough genuinely unused donor capacity, with the same global K and all full terminal entropy debts retained. Neither the accounting identity nor its optimal allocation proves that line. Full FEI remains OPEN.
