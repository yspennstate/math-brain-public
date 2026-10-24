# Biased reference transfer and common-spine block construction

All entropy, CE and KL are bits. Let g be Boolean, mu=E g, P its squared spectrum, v=1-mu^2. Let R be any normalized reference positive on supp(P). Replace it by its empty-calibrated law R0: R0(empty)=mu^2 and R0(T)=v R(T)/(1-R(empty)) for T nonempty. If v=0, use the point mass at empty. KL chain rule gives CE(P,R0)<=CE(P,R), with the exact removed cost D_Ber(mu^2||R(empty)). No data conditional cost has been removed.

For r fresh controls and p=2^-r set F=1+A_r(g-1). A full normalized reference is

    Q(empty,empty)=[1-p(1-mu)]^2,
    Q(U,empty)=p^2(1-mu)^2 for U nonempty,
    Q(U,T)=p^2 R0(T) for T nonempty and all U.

The corresponding Fourier probabilities are the same expressions with P(T) instead of R0(T). The reference sums to one, using sum_nonempty R0=v. It is fixed before sampling, with explicit sector probabilities. Conditional on the data sector, draw R0 conditioned on nonempty data, then a uniform control subset. The control-only sector draws a uniform nonempty control subset. Vacuum is a separate sector. This generates only finitely many symbols and has a terminating decoder. Its bias and reference parameters are fixed instance data; no arbitrary core spectrum oracle is assumed.

Every required zero-sector convention follows from zero target mass. The exact total debt is

    CE(P_F,Q)-H(F)=p D(P||R0)
                 =p[CE(P,R0)-H(g)].

In particular this holds for biased cores, unlike the balanced-only A086 interface. It preserves the entire conditional data debt, not just a lower bound on it. The coefficient is p, not Var(F).

For one control, actual children are g and the constant 1. Their conditional erasure and JS give H(F)-H(g)/2=B+JS. Put t=(1-|mu|)/2 in [0,1/2]. Data packets contribute v/2=2t(1-t) to B. The remaining packet has masses (1-t)^2,t^2. For E(a,b)=a log2(1+b/a)+b log2(1+a/b), ln(1+x)<=x gives

    B<=2t(1-t)+[2t^2 ln(1/t)+t^2]/ln2.

The JS bound sharp in magnitude mismatch is JS<=(2/ln2)M, where M=sum_T(|ghat(T)|-|1hat(T)|)^2/4=(1-|mu|)/2=t. Here d(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2 obeys d(z)<=1-sqrt(1-z^2): both vanish at zero, and the difference of derivatives z/sqrt(1-z^2)-atanh(z) has nonnegative derivative (1-z^2)^(-3/2)-(1-z^2)^(-1). Evenness and continuity handle negative z and endpoints. For each pair of child coefficients a,b, put m=(a^2+b^2)/2 and z=(a^2-b^2)/(a^2+b^2). Its JS contribution is m d(z)/ln2, at most (|a|-|b|)^2/(2ln2). Summing proves the claimed bound without an unreviewed premise. Thus

    [H(F)-H(g)/2]/t
       <=2+2/ln2+[2t ln(1/t)+(1-2ln2)t]/ln2
       <=2+(2+exp(-1/2))/ln2<6.

The maximum in the last step is attained at t=exp(-1/2)/2 and equals exp(-1/2). The strict rational bound uses ln2>2/3 and e>9/4, so exp(-1/2)<2/3. At t=0 the decrement is zero directly. The physical control influence is d=(1-mu)/2>=t, therefore

    H(F)<=H(g)/2+6d,
    CE(P_F,Q)<=CE(P,R0)/2+6d.

Each added control's reference remains empty-calibrated. Iterating r one-bit activations, with mu_j=1-2^-j(1-mu), gives

    CE(P_F,Q)<=p CE(P,R0)+6rp(1-mu),
    I(F)=p[I(g)+r(1-mu)].

The reference's direct formula above agrees with the iterated reference, coefficient by coefficient.

For disjoint private point-defect signs h_j=1-2 A_(L_j), put a_j=2^-L_j, m_j=1-2a_j, delta_j=1-m_j^2=4a_j(1-a_j). The fixed block reference chooses occupied blocks independently with probabilities delta_j and, for each occupied block, a uniform nonempty subset. It assigns mass

    R_h(S)=product_{j:S_j=empty}m_j^2 product_{j:S_j!=empty}4a_j^2.

Thus R_h=P_h by a direct local Fourier calculation; this is an explicit structural formula, not Q=P for an arbitrary seed. Block identities and standard edge-isoperimetry give

    CE(P_h,R_h)=sum_j[h2(delta_j)+delta_j log2(2^L_j-1)]
                   =sum_j H(h_j)<4 sum_j I(h_j).

Occupied-block cost is <=2 sum I(h_j) (the variance-entropy bound from the level proof); local subset cost is <2 sum I(h_j). Every block identity and the absent-block probabilities are paid exactly once. Local uniform subsets suffice here instead of the Euler rank law; under coordinate selection the binomial predecessor law also pays the local rank uniformly, as in A008. A rank code with a less efficient tail is unnecessary on this family.

Now let q(y) be any terminal Boolean core on fresh variables with a supplied normalized reference R_q and known bias, and set g=q product_j h_j. Empty-calibrate R_q and use its product with the block references. It matches P_g(empty), and CE_g=CE_q_cal+sum H(h_j). For F=1+A_r(g-1),

    CE_F<=p CE_q_cal+4p sum_j I(h_j)+6rp(1-mu_g),
    I(F)=p[I(q)+sum_j I(h_j)+r(1-mu_g)].

If the supplied terminal reference has CE_q<=C I(q), this yields CE_F<=max(C,6) I(F). It does not prove a universal C for arbitrary q. For q=1 the empty/private reference is fully explicit, and all r>=1 and all numbers/unequal sizes of private blocks have CE_F<=6I(F). For r=0 the disjoint product code has CE<4I. With q=1, F is also the XOR/product of point-defect gates each containing the same r common literals and its private block: product_j(1-2 A_r A_(L_j)). This proves a complete reference-cost result with unbounded common read. With q arbitrary it gives exact terminal-inclusive conditional transport rather than claiming the whole class is universally solved.

The first unsupported extension is a complete influence-paid reference when two gates have incompatible shared control events or their private cores share another physical coordinate. Neither product factorization nor the common-spine identity survives that change. The retained p CE_q term prevents declaring arbitrary terminal cores free.
