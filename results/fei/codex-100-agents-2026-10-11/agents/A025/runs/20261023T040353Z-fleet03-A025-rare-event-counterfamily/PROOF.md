# Rare-controller reference overhead contracts under conditioning

Candidate author proof; independent review pending. All entropy units are bits. FEI remains OPEN.

## 1. General scalar lemma

For a Boolean controller a on any finite uniform cube let s=Ea, P_a its squared Fourier spectrum, and 0<delta<=1/8. Define the normalized complete reference

    R_a=(1-delta) point_empty + delta P_a,
    G_delta(s)=H(R_a)-delta H(P_a).

Every true controller atom is supported; zero rows are retained as zero, never divided by. With phi(u)=-u log2(u), continuity at zero gives

    G_delta(s)=phi(1-delta+delta s^2)-delta phi(s^2)
                 +delta(1-s^2) log2(1/delta).                  (1)

In particular this overhead depends ONLY on the actual mean, not on the nonempty profile or controller dimension. For s!=0 put u=(1-delta)/(delta s^2). Differentiation gives

    G'_delta(s)=-2 delta s log2(1+u),
    G''_delta(s)=-(2 delta/ln2)[ln(1+u)-2u/(1+u)].            (2)

Since u>=7, ln(1+u)>=ln8>2>2u/(1+u). Here ln2>2/3 follows from the first positive term of ln2=2 atanh(1/3). The derivative tends to zero at s=0 and is continuous there. Thus G is strictly concave on [-1,1], including across zero. It vanishes at +/-1, is nonnegative, and is at most G(0)=h2(delta). For any physical controller query with child means s0,s1,

    gamma=G(s)-[G(s0)+G(s1)]/2 >=0,  s=(s0+s1)/2.          (3)

For any finite adaptive controller-only tree with actual reaches w_e, the SAME root overhead pays the full history:

    sum_internal w_e gamma_e + sum_leaf w_e G(s_e)=G(s_root). (4)

Nothing is renewed at a child. Delta=1 gives G_1=0, so strict concavity is not asserted there. More relevant failure of nonnegative Jensen gap occurs at delta=1/2 near s=1. It is an actual PARAMETERIZED Boolean family: for every r>=5 let a_r be -1 exactly at the zero vertex of the r-bit cube. Its parent mean is1-2^(1-r), and either physical coordinate has child means1-2^(2-r),1. All these means lie in[7/8,1]. At delta=1/2 on this interval, u=1/s^2 is in[1,64/49], so ln(1+u)<=ln(113/49)<1<=2u/(1+u). The strict logarithm bound follows from113/49<5/2<e, with e>1+1+1/2+1/6=8/3. Hence G''>0 throughout that interval, and the physical Jensen gap is strictly NEGATIVE for EVERY r>=5. This refutes only extending the nonnegative reference-overhead release rule to delta=1/2; it refutes neither an FEI constant nor an all-coordinate entropy/influence rule or universal route.

The counterfamily also has a full physical mux realization: take one fair data bit x, constant seed1 and F_r(x,z)=1-2*1[x=0,z=0^r]. Then delta=1/2 and the actual controller spectral marginal is exactly (1-delta)point_empty+delta P_(a_r). Thus the failed density-free overhead rule is witnessed inside actual Boolean functions, not merely abstract probability vectors. No entropy/influence ratio divergence is asserted.

## 2. Consume the already paid nonflat data prefix

Use exactly A022-ODDFACE-SURGERY-GAP-LEDGER@7 (run20261023T012352Z), PROOF Sections1--6. Thus g is -1 at000 and +1 elsewhere, b=g tensor t, t>=2, delta=8^-t, v any vertex, A=(1-a)/2 any independent physical control indicator, and

    F(x,z)=b(x)(1-2 1[x=v] A(z)), alpha=EA.

Fix a block-first data order and a uniform-depth prefix d<=3 floor(t/2)+2. Retain ALL its physical data children h with weights w_h=2^-d. Let q_h be A022's strictly positive prescribed data reference: original q=(9,1,...,1)/16 on untouched blocks; after the first bit use uniform4 for outcome0 and (13,1,1,1)/16 for outcome1; after the second use (15,1)/16, favored at the unedited seed label; completed blocks contribute1. These references are held fixed during the ensuing controller tree. Original Q on untouched blocks and original delta are never reset.

For any current controller restriction e use the explicitly prescribed target

    R_e=(1-delta) point_empty+delta P_{a_e},  T_he=q_h tensor R_e.

This changes the controller reference by a stated conversion. It is NOT declared to be the inherited phase reference. Complete CE and KL for every (h,e) remain, including both children of every query. Define averaged over all h:

    C_d(e)=sum_h w_h CE(P_{F_he},T_he),
    D_d(e)=C_d(e)-sum_h w_h H(F_he),
    B_d(e)=4 I_data,d(e)+delta H(a_e)-C_d(e)-U,
    0<=U<=t/64, fixed original old debit.

The aggregate controller spectral marginal is EXACTLY R_e. Indeed nonempty controller rows of the point-surgery spectrum have mass delta times their controller spectrum, and averaging over all data children is Parseval/forgetting. This includes inactive data cylinders: their reference cost is retained, not discarded. The complete data CE is affine in alpha_e because its data spectral marginal is

    P_b + 4 delta alpha_e [delta - b(v) b_hat(S) chi_S(v)]

before data restrictions, and the same affine dependence holds on every fixed cylinder with its actual conditional point density. Averaging physical data influence is also affine in alpha_e. Consequently there is a fixed data-dependent affine function M_d such that

    B_d(e)=M_d(alpha_e)-G_delta(s_e)-U.                  (5)

For one actual controller query, alpha averages to its parent value and therefore

    [B_d(e0)+B_d(e1)]/2-B_d(e)=gamma_e>=0.              (6)

Along ANY finite adaptive controller tree executed identically on all data siblings,

    sum_leaf w_e B_d(e)=B_d(root)+sum_internal w_e gamma_e
                         >=B_d(root)>=13t/576.          (7)

The last admission is A022@7; Sections1,3 here prove the continuation without assuming that numerical admission. This includes the requested ONE physical controller bit and all later controller-only restrictions. The tree may depend on past control outcomes, but NOT on the data-cylinder label h. No arbitrary unequal-depth mixed data/control theorem is asserted.

## 3. Actual physical inheritance and signed conversion audit

For EACH true parent spectrum P with reference T=q_h tensor R_e and queried control bit, pair true Fourier amplitudes x,y by the omitted frequency label. The actual-phase channel sends either member of a pair of total true mass m=x^2+y^2 to (b,pair) with probability (x+(-1)^b y)^2/(2m); use1/2 when m=0. Propagate ALL reference atoms, including off-support ones. Let rho_b be its reference branch masses and T_b^inh its normalized children. Since T supports P, rho_b>0. KL chain rule gives

    D(P||T)=E+O+[D(P_0||T_0^inh)+D(P_1||T_1^inh)]/2,
    E>=0, O=D(fair||rho)>=0.                            (8)

Define raw signed target conversion kappa=average(D_target-D_inh). Then its exact net cost after the ACTUAL refunds is

    sigma=kappa-E-O=average D_target-D_parent.          (9)

Both child KLs and both branch normalizers remain. Let DeltaH_F be the data-frontier averaged output entropy decrement and DeltaH_a the actual controller entropy decrement. Directly from (1),(5),

    C_parent-average C_target=delta DeltaH_a+gamma,
    sigma=DeltaH_F-delta DeltaH_a-gamma.                (10)

Thus the combined signed controller transaction, using the original supplied controller entropy spend delta DeltaH_a, increases the SAME bank by gamma. It does not separately bound raw positive reset charges. With K the cumulative supplied controller entropy spent, K+delta E_leaf H(a_leaf)=delta H(a_root) exactly. The original full source-controller entropy has not disappeared or been renewed. Old U stays subtracted at every leaf with actual reaches.

Extend A022's signed query account Ehist by delta DeltaH_a-DeltaH_F at controller queries (data queries retain4Inf-DeltaH_F). Then

    E_leaf(B_d+D_d)+Ehist = B_initial+D_initial.        (11)

This conserves the original source entropy earmark and BOTH full terminal debts. No claim replaces delta DeltaH_a by4delta Inf_i(a): such an all-coordinate rule is false in general. The arbitrary controller entropy supplier remains an explicit unpaid universal premise.

## 4. First unsupported line and counterfamily scope

The continuation is proved for a common controller tree AFTER a paid uniform data frontier. The first unsupported mixed-history line is allowing the controller-query/stopping choice to depend on the DATA-cylinder label while charging prescribed target references to the already debited ORIGINAL account. Then aggregate control marginals and affine cancellation need a new conditional ledger; (5) alone does not establish it. Choices between common controller queries based on earlier CONTROLLER outcomes are already covered. Independently, pricing arbitrary delta H(a) by influence is still FEI-strength and is not supplied here.

The inherited A025 finite-price obstruction remains local: no fixed K,lambda pays every coordinate using d and released pair bank, even though that OLD three-core family has H<6I. This is not a bound for the present arbitrary-controller family. This stage refutes no FEI constant, all-coordinate theorem, or universal route. The explicit delta=1/2 scalar witness refutes ONLY extension of the concavity/payment lemma to that activation density.
