# First-collision transfer through two independent dictator cores

All entropies are in bits. Let h be any Boolean sign on a uniform finite control cube, b=E h, and

F_h(z,y0,y1)=((1+h(z))/2)y0+((1-h(z))/2)y1.

The data bits are independent fair signs, disjoint from the controls. Fix any finite fresh-coordinate physical restriction tree T for h with constant leaves. Apply its actual controller policy to F, consistently at each history, then query the remaining data bits. Constant-controller leaves are dictators with Fourier entropy zero, so their appended data queries have reserve zero for every C>=0. This statement covers adaptive T, not just fixed permutations.

Write phi(p)=p log2(1/p), phi(0)=0, and

A(b)=phi((1+b)^2/4)+phi((1-b)^2/4)+1-b^2-phi(b^2)/2.

Fourier expansion has the two singleton masses (1+b)^2/4 and (1-b)^2/4, and, for every nonempty control set S, two masses hat h(S)^2/4. Thus, at every actual controller history,

H(F_h)=H(h)/2+A(b),  I(F_h)=1+I(h)/2,

and the influence of a queried control i is d_F=d_h/2. This is a physical coupling identity: on an h-changing edge the selected independent signs disagree with probability 1/2. Retained data influence remains exactly one, including at the constant-controller frontier.

A is even and continuous. For 0<b<1,

A'(b)=[-(1+b)ln(1+b)+(1-b)ln(1-b)+2b ln b]/ln2 <=0.

Consequently 0<=A<=2, A(0)=2, and A(+-1)=0. Moreover

|A'| <= [2ln2+3/e]/ln2 <4.

Here |t ln t|<=1/e for 0<=t<=1; (1+b)ln(1+b)<=2ln2. The strict final comparison follows already from e>8/3 and ln2>2/3. Endpoints follow by continuity, so A is 4-Lipschitz on [-1,1]. No floating calculation is needed.

For any control query, its two means are b+-beta, where beta=hat h({i}). Boolean derivatives belong to {-1,0,1}, hence |beta|<=d_h. The exact entropy decrement satisfies

D_F=D_h/2+A(b)-E A(b_child).

Therefore its scalar correction is at most 4d_h=8d_F. This bound owns the actual control query once; no nominal selector influences are added. The same correction can be negative, so an unsigned telescope must not replace this identity.

Define Q_C(v)=[D_v-Cd_v+E Q_C(child)]_+, zero at specified leaves. Its finite-tree optimal stopping representation is the supremum, over adapted stopping rules sigma, of expected accumulated D-Cd. Optional stopping of the displayed exact decrement gives, for every such controller stopping rule,

payoff_F(C,sigma)=payoff_h(C,sigma)/2+A(b_root)-E A(b_sigma).

The policies have the same histories and probabilities. Appended dictator queries cannot improve a stopped payoff. Taking suprema and using 0<=A<=2 yields the exact universal sandwich for this prescribed tree:

[Q_C(h,T)/2+A(b_root)-2]_+ <= Q_C(F_h,T_control-first) <= Q_C(h,T)/2+A(b_root).

For balanced h this is Q_C(h,T)/2 <= Q_C(F_h,T_control-first) <= Q_C(h,T)/2+2. These are all-dimensional statements, independent of the length of earlier injective support plateaux. The additive two is sharp: h=z, C=0 gives Q_C(h)=0 and Q_C(F_h)=2.

Applying the per-query scalar bound to every stopped payoff also proves

Q_(C+8)(F_h,T_control-first) <= Q_C(h,T)/2.

Equivalently, Q_C(h)/2+A(b) is a nonnegative potential at price C, with zero at the controller frontier, while Q_C(h)/2 alone is a potential at price C+8. The former has at most two units of initial mean correction; the latter spends at most eight times the actual consumed control influence. These are alternative accounts, not additive payments.

The two-state variance-rarity reserve here is S(b)=h2((1+b)/2). Its control release S(b)-E S(b_child) is nonnegative and at most d_h=2d_F. To prove the upper bound, condition additionally on all unqueried control coordinates except i. The mutual information between the selector label and i is at most the probability that the two coupled labels differ, namely d_h; revealing the additional coordinates can only increase that mutual information because they are independent of i. This independently reconstructs A038's release result in this two-dictator scope only.

For an arbitrarily long actual support plateau, take h=product of k fresh control signs, k>=1. The wrapper's four occupied supports are {y0},{y1},K union {y0},K union {y1}. Deleting fewer than k controls leaves four distinct supports of mass1/4, so every such branch has H(F)=2 and S=1, all control decrements and rarity releases zero, and each queried control has influence1/2. At the final control query, the support pairs collide and the leaf becomes a dictator: D_F=2, S release=1. The controller itself has H(h)=Q_C(h)=0 throughout. Direct backward induction gives Q_C at a node with r>=1 surviving controls equal to [2-Cr/2]_+, and zero once the controller is exhausted. Thus at C=1,k>=4 the root reserve is zero while the first collision's parent requires reserve3/2. This isolates the nonlocal stopping debt behind an arbitrarily long separated-support plateau without discarding its previously spent control influence. The total data influence1 is still retained at the frontier. No new census is needed for this four-character identity.

For h=z at its sole control query, D_h=0, D_F=2, S release=1, d_F=1/2. Thus the erasure after removing the intrinsic h decrement and rarity release is still one bit. A038's sharp release bound is not an erasure bound. This does not refute its claim, nor any positive-price universal policy: it identifies the missing signed mean correction at a genuine first Fourier collision. No fresh core reserve or terminal entropy can be silently used to cancel it.

Actual terminal entropy is retained: stopping at any controller prefix leaves H(h_sigma)/2+A(b_sigma), and completing the controller tree leaves a dictator of entropy zero and influence one. The controller reserve Q_C(h,T) is inherited, not proved bounded. In particular, the balanced same-price lower bound preserves arbitrary seed stopping difficulty. Universal payment of that intrinsic controller term, and transport after nonconstant data exposures destroy this simple two-dictator mean formula, remain unsupported.
