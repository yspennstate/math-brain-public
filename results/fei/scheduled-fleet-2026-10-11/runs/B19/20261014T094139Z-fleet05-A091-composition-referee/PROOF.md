# Shared activation with one repeated nonconstant fallback

All cubes are finite and uniform; entropy is in bits. eta(x)=-x log2 x, eta(0)=0; Phi(a,b)=eta(a)+eta(b)-eta(a+b). C_j(z) are mutually exclusive Boolean indicators on an arbitrary physical controller cube, not necessarily a partition. T=sum C_j is an indicator, p_j=E C_j, t=sum p_j. Selected Boolean cores u_j occupy mutually disjoint data cubes independent of z. G is a Boolean fallback on a separate physical cube, disjoint from every prefix core and z. G may itself be an exclusive selector of disjoint independent cores, with probabilities a_l, variances V_l and Z=sum a_l V_l. Its actual mean is n and variance V=1-n^2. A fresh fair physical bit Y in {0,1}, independent of all these blocks, gives

    F=G+Y sum_j C_j(u_j-G).

There is ONE physical G, occurring when Y=0 and when Y=1,T=0. Put m_j=E u_j, h=sum C_j(m_j-n), h0=E h. All biases, constants, empty guards, and full guards are allowed. Arbitrary preceding physical restrictions preserving this decomposition are allowed; in particular actual partial core-data exposure is allowed. Duplicate physical selected-core descriptions must be merged first. Dependence between selected cores is not allowed by this theorem.

## Exact erasure and fine release

Use the original fine selector reserve R=sum eta(q_label) Var(core_label), with prefix masses p_j/2 and fallback masses (1-t/2)a_l. At a reveal of Y its release is

    kappa=R-(R_0+R_1)/2
         =sum_j p_j Var(u_j)/2+k_t Z,
    k_t=eta(1-t/2)-eta(1-t)/2 >=0.                 (1)

Concavity of eta proves the last sign, since eta(1)=0. Factors a_l cancel exactly in the fallback drift. U=sum q_label[H(core)-eta(mean^2)] is harmonic at this controller query. The actual physical query influence is

    d=sum_j p_j(1-m_j n)/2.                      (2)

Independence of the actual selected outputs and G proves (2) on each disjoint activation cell; no child-copy independence is asserted.

For the full Boolean Fourier spectrum, let B_Y=sum_S Phi(fhat(S)^2,fhat(S union {Y})^2). Direct physical-frequency pairing gives

    B_Y-kappa=Var(h)/2+Phi((n+h0/2)^2,(h0/2)^2)
           +[t(1-t)/2+Phi((1-t/2)^2,(t/2)^2)]V
           -k_t Z.                              (3)

Proof with all sectors retained: a nonempty prefix-core frequency gives identical even/odd Y amplitudes, hence total erasure p_j Var(u_j)/2; those sectors cancel their exact part of (1). For each nonempty ACTUAL fallback frequency, the even/odd multipliers are 1-T/2 and -T/2. Nonempty z frequencies have equal squared amplitudes and contribute Var(T)/2; the empty z frequency contributes Phi((1-t/2)^2,(t/2)^2). Summing these actual fallback frequencies gives V, including its nonconstant controller mean-profile. The remaining empty-data profile is n+Y h(z). Its nonempty z frequencies contribute Var(h)/2, and its constant frequency contributes the displayed mean packet. This proves (3), including zeros by continuity. In particular replacing G by independent copies changes this calculation.

## Uniform price

The scalar inequality Phi(a^2,b^2)<=2|ab| holds in bits. Here is an independent full proof. Normalize a^2+b^2 and write their normalized imbalance as tanh v, v>=0. The natural entropy is ln(2 cosh v)-v tanh v, and the normalized right side is sech v. After multiplying by cosh v, the required inequality is F(v)>=0, where F(v)=ln2-cosh(v)ln(2cosh v)+v sinh v. We have F(0)=0 and F'(v)=sinh(v)[v coth v-ln(2cosh v)]. The bracket has derivative (tanh v-v)/sinh^2 v<=0 and limit0 at infinity, so it is nonnegative throughout. Thus F'>=0. Zero amplitudes follow by continuity. Homogeneity gives the stated scalar bound.

Since |m_j-n|<=1-m_j n, |h0|<=sum p_j(1-m_j n)=2d. Also |n+h0/2|=|EF|<=1. Thus the mean packet is at most |h0|<=2d. Exclusivity gives E h^2=sum p_j(m_j-n)^2, hence

    [Var(h)+t(1-t)V]/2
       <=[sum p_j(m_j-n)^2+t V]/2
       =sum p_j(1+m_j^2-2m_j n)/2 <=2d.

The other fallback packet satisfies

    V Phi((1-t/2)^2,(t/2)^2)
       <=t(1-t/2)V <=t V <=4d.

Indeed 1-n^2<=2(1-m_j n) for every |m_j|<=1. Drop only the nonpositive -k_t Z. Therefore

    B_Y-kappa<=8d,
    D_Y H(F)-kappa<=(8+2/ln2)d,                 (4)

where D is the actual entropy decrement and D=B+J with physical child-channel J<=2d/ln2. This bound is valid in every dimension. It asserts no lower bound on B-kappa or D-kappa. At d=0 the actual query is irrelevant and the reserve release and erasure vanish; (3) also shows this directly. The scalar and physical-J bounds are already independently reconstructed in the previous A091/A059 source chain; no new universal controller theorem is being assumed.

## Stopping interface and terminal cases

Equation (4) pays this actual shared activation node in the SAME fine U/R account. For a policy with arbitrary preceding DATA-only exposure, followed by Y, and then arbitrary private-priority queries/data interruptions in each actual child, the accepted A059 v2 theorem applies to the children when C_j form a private point-priority prefix and G a disjoint private-priority suffix. Failed-child G is kept once; the activated child has the original prefix followed by the same G. With K=6+(5+ln10)/ln2<17, which exceeds 8+2/ln2, the resulting finite stopped inequality is

    H_root<=U_root+R_root+(3/ln2)T_data+K Pi_ctrl
                 +E[H_leaf-U_leaf-R_leaf].

This is a conditional graft, not an arbitrary-order theorem for controls before Y. At an actual controller-resolved leaf the exact remaining boundary is eta((Eu_leaf)^2)<=I_leaf/ln2. At unresolved leaves retain literal H-U-R. R_root funding is separate; arbitrary inherited U is unpaid. No reserve is restarted, no terminal copy is issued, and no arbitrary controller is supplied a free certificate.

First unsupported line: a private prefix-controller query BEFORE Y is paid at a fixed rate by the same fine release when the nonconstant fallback still occurs on both inactive and active histories. Equations (1)-(4) close the shared-bit reveal but do not close that other query. Mixed orientations of shared bits, physically overlapping selected core data, and generic inherited entropy/profile payment also remain open.

## Relation to current packets

A059 v2 already settles arbitrary private priority order and common activation with CONSTANT default, by inserting a first point test selecting that constant. Here that insertion would give duplicate descriptions of the SAME NONCONSTANT G at the first and final labels; disjoint-core hypotheses would fail. The new exact identity handles that repeated fallback explicitly. A028's once-carried product bank is conserved but does not claim this local signed payment. A030's harmonic cut reserve leaves its generic coherent correction unproved. The present local lemma supplies one such paid reveal, without asserting their broader correction.
