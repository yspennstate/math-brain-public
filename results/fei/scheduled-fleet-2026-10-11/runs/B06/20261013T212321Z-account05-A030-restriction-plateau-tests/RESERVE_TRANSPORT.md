# Exact plateau transport for the A065 reserve

Fix C>=0. On a prescribed finite fair physical complete tree with constant leaves, use A065's definition Q_C(v)=[D_v-Cd_v+E(Q_C(child)|v)]_+, where D_v is the actual entropy decrement, d_v the actual queried influence. Its minimality follows by backward induction. This stage applies that definition; it does not rename its universal resource estimate as an easier goal.

For a core g with a prescribed complete continuation T, let q=Q_C(g,T). A sign/input-sign translated copy of T has the same node entropies, influences and reserve values. Before this continuation, compress F_L=g(product of L inputs/block) to one input/block, never exhausting a block. Every plateau node has D=0, each query in block i has d=Inf_i(g), and the terminal continuation reserve is q on every leaf. If a node retains ell_i inputs/block, put b_v=sum_i(ell_i-1)Inf_i(g). Then

    Q_C(v)=[q-C b_v]_+.

Proof: b_child=b_v-d on both children, and the induction value is identical on both children. Therefore [ -Cd+[q-C(b_v-d)]_+ ]_+=[q-Cb_v]_+ for C,d>=0. The terminal b=0 value is q. This proof permits every adaptive choice that still completes exactly the same compression partition and uses translated copies of T. It does not require a fixed coordinate order or knowledge of unrevealed assignments. At the root b=(L-1)I(g), so Q_C(F_L)=[q-C(L-1)I(g)]_+. Fresh spectator parity gives the analogous formula [q-Cm]_+ and, after k spectator revelations, [q-C(m-k)]_+. All branch probabilities remain fair; no exponentially rare branch is selected.

For a nonconstant g and C>0, Q_C(g,T)<=H(g) ensures that sufficiently many parity spectators or a sufficiently wide code block give Q_C(root)=0. Thus the predicate 'Q_C<=K I' for any K>=0 at the root does not have a universal multiplicative inheritance rule through zero-entropy compression: the root Q_C/I can be zero while the descendant Q_C/I is positive. This does not contradict a completed root FEI certificate. The prefix has already provided C times its influence as negative debt credit, which may cancel later positive increments. A root reserve bound is inherently a whole-rule initial claim, not a nodewise hereditary certificate.

By contrast A064's terminal-corrected remaining bill P_v=H(g_v)-E(H(final leaf)|v) is invariant through this compression when the continuation is translated consistently: both terms are independent of plateau assignments. If the tree stops at the compressed core, P=0 on the whole plateau and terminal H(g) remains. If the continuation is complete to constants, P=H(g) throughout the plateau. Its exact entropy drift stays zero there; the C-priced minimal reserve can shrink to zero at the root because it includes influence credit. No equality between these two reserves is asserted.

For a general finite zero-entropy plateau subtree with nonnegative terminal reserves q_l and path influence cost b_l, its backward recursion obeys

    [E q_l-C E b_l]_+ <= Q_root <= E [q_l-C b_l]_+.

The lower bound uses complete continuation or stopping immediately. For the upper bound, a stopped-before-terminal path has payoff -C times its spent influence <=0, while a completed path has payoff q_l-Cb_l, hence any adapted strategy is bounded pathwise by the positive part of the completed path payoff. On a plateau the recursion is exactly this optional-abort optimization. The upper bound is an oracle bound; equality need not hold when terminal reserves differ. This is where actual branch heterogeneity, rather than plateau length alone, can become useful in a global stopping argument.

## Whole-block simulation and order sensitivity

There is a second actual tree on the same F_L. Whenever T queries seed coordinate i, query every remaining input in that L-input parity block, then follow the T child specified by its parity. Until the last input, D=0 and d=Inf_i(current seed restriction). At the last input D is exactly the T entropy decrement. All L inputs have the same queried influence, and each parity outcome is fair. Backward induction gives

    Q_C(F_L, block-simulation(T))=Q_(LC)(g,T).

Indeed the last-step positive part is [D-Cd+E q_child]_+; the preceding L-1 negative-credit steps turn it into [D-LCd+E q_child]_+. The identity requires the prescribed translated simulation and cannot be applied to an arbitrary tree on F_L. For the two complete orders,

    [Q_C(g,T)-C(L-1)I(g)]_+ <= Q_(LC)(g,T).

One can prove this from the stopping representation: for any bounded stopping prefix, its expected spent influence is <=I(g), so increasing the price from C to LC loses at most C(L-1)I(g). Take suprema and the nonnegative positive part. Thus compression-first can use all the redundant influence credit before a later positive-cost prefix; interleaved whole-block simulation may expose that prefix before the remaining credit is spent.

Take ordinary addressing A_a, H=2a, I=1+a/2, with data-first complete continuation T. With C=4 and L=2, compression-first has

    Q_4(F_2, compression-first)= [Q_4(A_a,T)-4I(A_a)]_+=0,

because Q_4(A_a,T)<=H(A_a)=2a<4I(A_a)=2a+4. Whole-block simulation has

    Q_4(F_2, block-data-first)=Q_8(A_a,T)>=[a-8]_+.

The last inequality stops T after every data coordinate: expected influence spent is 1, and expected terminal entropy <=a. On F_2 the corresponding data-block prefix spends exactly 2 influence and leaves expected terminal influence a (and entropy <=a), so its unpaid prefix is >=a-8. Both full trees have H_root=2a, I_root=a+2, Pi_H=2a and Pi_I=a+2. Extend all constant leaves with the remaining zero-influence queries; both trees then have exactly the same singleton physical leaf partition. These extensions do not change their reserves.

Hence the minimal nonnegative reserve difference grows at least a-8 with dimension on the same actual Boolean function and the same completed leaf partition. This does not contradict B06 R2: the telescoped total debt is 2a-4(a+2)=-2a-8 in both orders, while the Snell envelope constrains every stopped prefix. Nor does it refute A029's proposed bound on entropy-drop/influence ratio gains. The root H/I here stays below 2; the example is a reserve/order obstruction, not an FEI counterfamily.

## A concrete small exact witness and a heterogeneous plateau

For A_3 and data-first T the frozen integer-Walsh/prime-log recursion gives

    q=Q_4(A_3,T)= (9/32)log2(3)-3/8, with 1/16<q<3/32.

The bounds follow exactly from 3^9>2^14 and 3^3<2^5. A fresh spectator z gives Q_4(z A_3, spectator-first)=0 and Q_4(A_3,T)=q on both children. Thus even a zero root reserve can acquire positive conditional reserve on every probability-1/2 branch.

The heterogeneous upper bound can be strictly loose for actual zero-entropy nodes. For a>=13 take z A_a. Continue one spectator branch with data-first T, reserve q>=a-4>=9, and the other with address-first continuation, reserve zero at C=4. The parent has D=0,d=1, so its actual reserve is q/2-4. The pathwise oracle upper bound is (q-4)/2=q/2-2. The adaptivity gap is exactly 2: the policy cannot see the spectator branch before deciding whether to pay for revealing it. This uses prescribed different future rules on two isospectral children; it makes no claim that the reserve is a function of the child Boolean function alone.
