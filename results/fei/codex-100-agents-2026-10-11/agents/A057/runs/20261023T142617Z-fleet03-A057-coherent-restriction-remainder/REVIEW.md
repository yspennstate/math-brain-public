# A057 independent reconstruction of A060's one-more-query handoff

All entropy is in bits. This is review of A060 stage9, including its pinned A059 version2 prefix. It makes no new complete-core supplier claim. Full FEI is OPEN.

## Universal scalar bound reconstructed

For an arbitrary Boolean g, split coordinate i and let d=Inf_i(g), delta=min(d,1-d). The disagreement indicator has density d. Its sign g_0 g_1 has influence at most I(g_0)+I(g_1)=2(I(g)-d), by an edgewise union bound. Edge isoperimetry on the smaller of the disagreement set and its complement gives influence at least 2 delta log2(1/delta). Therefore I(g)>=d+delta log2(1/delta), including both endpoints by continuity. The normalization is correct: an indicator boundary edge is counted twice in sign influence. The internal-edge induction uses cross edges<=min(a0,a1), reducing exactly to h2(u)>=2u on [0,1/2].

The physical entropy decrement D is erasure plus the actual two-child Jensen-Shannon term. Marginal entropy bounds erasure by h2(d). JS<=min(1,2 delta/ln2), so D<=h2(d)+min(1,3delta), since ln2>2/3 follows from the positive atanh series at 1/3. No FEI input occurs.

Write ell=log2(3), kappa=(3ell+1)/(ell+1)=3-2/(ell+1), and a(d)=d(1+log2(1/d)). For d<=1/2 the needed difference is kappa a(d)-h2(d)-3d below 1/3, and kappa a(d)-h2(d)-1 above 1/3. Both have second derivative [1/(1-d)-(kappa-1)/d]/ln2<0 on their stated intervals, because kappa>2. At d=0 and d=1/3 the first difference is zero. At d=1/3 the second is zero; at d=1/2 it is kappa-2>0. The chord inequalities prove D<=kappa I(g). For d>=1/2, I(g)>=d+delta>=1 and D<=2<kappa I(g). Finally ell<5/3 is exactly 27<32, so 2<kappa<9/4. A060's scalar proof passes unchanged. This is a whole-core bound, not D<=kappa Inf_i(g).

## Original-owner chain reconstructed

For F=K+Cg on disjoint cubes, KC=0, t=EC, and mu=Eg, direct multiplication gives the empty-core coefficients Khat+mu Chat and all nonempty-core coefficients Chat(s)ghat(T). Expanding -ab log2(ab) proves the exact profile

 E=H(F)-tH(g)=sum_s eta((Khat_s+mu Chat_s)^2)-t eta(mu^2)+(1-mu^2)sum_s eta(Chat_s^2).

The core-frequency marginal is (1-t)delta_empty+t ghat^2: the cross term sums to 2mu E(KC)=0. Its entropy lies between tH(g) and tH(g)+h2(t); conditional exterior entropy lies in [0,r]. Hence 0<=E<=r+h2(t), including dead masks and complete exterior exhaustion. This retains the exact coherent logarithmic term. While a tag character remains, take g=G chi_remaining, with H(g)=H(G); after collapse g is the actual signed restricted G. No residual nonempty core frequency is discarded.

For A059@2 the original exterior owner is B0=4I_X=2m-4mc. The old debit cD_j(G)<=2c is paid once. Exact exterior escrow E_start leaves L0=B0-old-E_start>=3m/4-15/32. Each additional admitted core query pays a=tD_i(G)<=2t from L, updating both actual core children and their exact E. Thus m/4 additional queries leave L>=m/8; more are permitted while current L-2t>=m/8. These are expected-resource allocations: E_child-E_childmean is a recorded zero-mean branch innovation. A claim of pathwise subtraction-only cash would be stronger and is not accepted here.

Add the ORIGINAL bank M0=kappa cI(G). At every source-paid core query, including the old one, release kappa t Inf_i(G_current) into unused original cash R, and carry kappa t I(G_child). Conditional influence conservation makes their sum exactly equal to the previous pending bank in expectation. Exterior restrictions make t a martingale; tags preserve core entropy and influence. No cash is renewed. At a reached frontier AFTER source-admission failure, pay ONE additional core query from its current pending bank: replace that bank by t[kappa I(G_current)-D_i(G_current)]>=0 in BOTH children. Keep old R, actual diminished L, and complete E_child. The local full decrement is exactly tD_i(G_current)+E_parent-average E_child, so the original-owner stopping identity holds. The core is then frozen, with arbitrary exterior/tag continuation allowed. The retained floor is m/8 for the admitted-prefix handoff, and m/4 for the narrower old-query-only prefix. These are distinct scopes.

A060's one-more-query conclusion is ACCEPTED at this expected-resource scope. It does not buy a second query from the consumed whole-core bank. The independent reconstruction uses the disagreement-set boundary argument, complete core marginal and influence conservation; no source repair was needed.

## Adversarial boundary and honest first unpaid line

AND2 has H=2,I=1 and a first query with both full children of entropy zero, forcing any universal one-query whole-core rate>=2. A060's rare bent splice has tag influence c_s and tag entropy debit>=c_s(s-1), so refreshing the whole-core account at a local influence price is invalid; tensoring fixed such factors defeats fixed additive slack. The normalized paired bent value at the all-one point is +1 when s is divisible by four, as required.

For the complete-core boundary, a point-defect AND_n has I=2n2^-n and H=eta((1-2^(1-n))^2)+8*2^-n(1-2^-n)(n-1); division gives H/I->4. Tensoring any fixed seed with H>K I defeats a fixed exterior allowance at rate K. More strongly, a universal aggregate assertion cH(G)<=B0+KcI(G), with c>0 and B0 fixed, implies FEI(K) by applying it to r independent copies of ANY fixed Boolean G and dividing by rc before r->infinity. Conversely FEI(K) immediately implies that assertion. Thus A060's complete-core equivalence and rate<4 obstruction also pass. They do not prove rate4 sufficient or FEI false.

The first unpaid line is a necessary further core query AFTER the one-shot original bank has been consumed. Its remaining cash must pay aggregate actual decrements while preserving complete terminal entropy. Reusing kappa I(current core) would assume the false coordinate-price inequality. A universal constant-rate supplier is FEI-scale; another bounded exterior example cannot supply it.
