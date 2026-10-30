# One original rare-chain source, v8

All cubes are finite and uniform, entropies in bits. Let A,B be arbitrary Boolean functions on the SAME physical data coordinates; there is no disjointness, balance, norm, degree or minority assumption. Put e=AB, delta=Pr(A!=B), and E=I(e). Let k>=1 fresh fair selectors choose A only when all k equal1, otherwise B. Write alpha=2^-k and F_k=B+1_all(A-B). Its complete inherited branch entropy is K_k=alpha H(A)+(1-alpha)H(B). The total coherent overhead is D_k=H(F_k)-K_k.

## Exact posterior and the original source

At a data Fourier row let a=Ahat(T), b=Bhat(T), d=a-b, r=alpha a^2+(1-alpha)b^2. The selector-empty amplitude is b+alpha d; every other selector Fourier coefficient has magnitude alpha |d|. Let v=alpha(1-alpha)d^2/r for a nonzero row. The total mass of that row is r. The conditional selector entropy is h(v)+v log2(2^k-1). Define

    J_alpha(a,b)=alpha a^2 log2(a^2/r)+(1-alpha)b^2 log2(b^2/r).

Then EXACTLY

    D_k=sum_T {r[h(v)+v log2(2^k-1)]+J_alpha(a,b)}.       (1)

Every term is nonnegative: J_alpha is the entropy convexity gap. This is a coherent Fourier posterior, not a disjoint-data chain rule. Parseval gives sum r=1 and V=sum r v=4alpha(1-alpha)delta.

View the OUTERMOST selector as choosing G=F_(k-1) or B (with F_0=A). Its disagreement probability is 2alpha delta. Its disagreement function is GB=1+1_all(k-1)(e-1), whose exact influence is 2alpha E+4alpha(k-1)delta. Consequently the v7 original ticket, supplied at this root, is

    B_k=4 Inf_outer(F_k)+I(GB)
       =2alpha E+4alpha(k+1)delta.                     (2)

This is the existing named source, not a sum of fresh tickets.

## Two elementary analytic estimates

First, delta log2(1/delta)<=E/2. This is entropy tensorization applied to the input indicator of e=-1. For a nonnegative g, Ent(g)=E[g log2(g/Eg)] satisfies Ent(g)<=sum_i E Ent_i(g). One proof decomposes entropy by one coordinate and applies convexity of Ent to the conditional average, inductively; the convexity is the log-sum inequality. With g an indicator, a coordinate contributes0 on a constant fiber and1/2 on a mixed fiber, hence the sum is E/2. No Fourier FEI bound is used.

Second, for 0<alpha<=1/2,

    J_alpha(a,b)<=alpha(log2(1/alpha)+2/ln2)(a-b)^2
                <alpha(k+3)(a-b)^2.                  (3)

For b!=0 scale to t=a/b. In NATURAL logarithms let phi(t)=alpha t^2 ln(t^2/r)+(1-alpha)ln(1/r), r=alpha t^2+1-alpha. Direct differentiation gives

    phi''(t)=2alpha ln(t^2/r)+4alpha(1-alpha)/r
             <=2alpha ln(1/alpha)+4alpha.

Also phi(1)=phi'(1)=0. Taylor's integral formula proves (3), for both signs of t. At t=0 phi is C1 and the logarithmic second-derivative singularity is integrable, so splitting the integral at0 justifies the same bound. The b=0 case follows by continuity. This is a pointwise bound; it is summed additively, never multiplied across dependent rows.

## All-depth payment from THREE times the original ticket

For k>=2, alpha<=1/4. Write beta=4alpha(1-alpha), so V=beta delta. The binary-entropy bound h(x)<=x log2(1/x)+x/ln2, the inequalities beta<=4alpha and log2(1/beta)<=k-3/2, and 1/ln2<3/2 give

    h(V)<=4alpha delta log2(1/delta)+4alpha k delta
         <=2alpha E+4alpha k delta.                  (4)

The logarithm bound follows from 1-alpha>=3/4>1/sqrt2; all factors are nonnegative. The endpoint delta=0 is direct. Concavity applied to (1), followed by (3),(4), yields

    0<=D_k<=h(V)+V log2(2^k-1)+4alpha(k+3)delta
            <=2alpha E+12alpha(k+1)delta
            <=3 B_k.                                (5)

For k=1 the v7 single-selector proof gives D_1<=B_1, so (5) holds for ALL k>=1. This proves a dimension-independent overhead ledger for arbitrary overlapping A,B with unbounded selector depth. It retains the FULL inherited K_k; it does not prove FEI for arbitrary A or B.

## Same original account, old debit, all stopping histories

For any selector restriction history that has not killed the all1 event, replace k by the number of remaining selectors in the exact D, and keep A,B unchanged. If the event is killed or resolved, the coherent overhead is0 and the actual selected core remains. Every D is nonnegative by (1). At a selector split the full entropy debit equals its inherited-K debit plus D_parent-E D_child. Thus any finite adaptive selector stopping tree has total signed coherent debit

    D_root-sum_live_leaves w_leaf D_leaf <=D_root<=3 B_root.

More generally arbitrary intervening physical DATA queries also telescope in this identity, since (1) remains valid for the reached restricted A,B. After the selector resolves the core debits are wholly inherited. Both actual child branches, true reach weights and complete stopped-terminal entropy remain. Allocate 3 B_root ONCE, subtract each actual signed debit, and retain the reached D reserves and the ORIGINAL slack 3B_root-D_root. No descendant 3B is substituted and no spent influence is restored. If an old original debit c is already booked, the required admission is that the actually remaining original allocation is at least the current aggregate D. The proof does not infer that admission automatically from a fresh descendant formula.

The bound D_root<=3B_root is an all-depth original-source theorem for this rare-switch mechanism. It is not a per-data-query bound, does not allow resetting the source in arbitrary mux trees, and does not add a payment for inherited core entropy. If an arbitrary data tree is stopped after nested selectors, the inherited entropy terms stay SIGNED.

## Exact failure of price1; all-depth lower bound2

Take A=1 and B=x, a single fair shared bit. For k=2, F_2 equals1 when both selectors are1 and otherwise equals x. Its squared Fourier spectrum is one atom9/16 and seven atoms1/16. Therefore

    D_2=4-(9/8)log2(3),     B_2=2,
    D_2-B_2=2-(9/8)log2(3)>0,

certified by 2^16>3^9. The FIRST outer-selector coherent debit is D_2-H(F_1)/2=3-(9/8)log2(3)>0. Its old debit leaves 2-that amount; the subsequently reached inner-selector bill is H(F_1)/2=1. The deficit is exactly D_2-2>0. Both final cores have zero Fourier entropy, so no missing terminal term explains the failure. This refutes price1 after one actual paid nested split.

For arbitrary k>=1 the same family has one Fourier atom (1-alpha)^2 and 2^(k+1)-1 atoms alpha^2. Thus

    D_k=-(1-alpha)^2 log2((1-alpha)^2)+2k(2alpha-alpha^2),
    B_k=2alpha(k+2),
    D_k/B_k ->2.

Indeed the first term is O(alpha), using -ln(1-alpha)<=alpha/(1-alpha), while the second is 4kalpha-2kalpha^2. Hence ANY all-depth original-ticket multiplier must be at least2. Price3 is proved; price2 is NOT proved by this stage. This family has I(F_k)=1+(k-1)alpha, so it is not an FEI counterexample.

## First unpaid universal line

A branch-conditional FEI transfer follows without a factor depending on k. If both complete branches satisfy H<=C I, then I(F_k)=alpha I(A)+(1-alpha)I(B)+2kalpha delta. For k>=2, 3B_k<=6 I_data+9 I_selectors, using E<=I(A)+I(B) and alpha<=1-alpha. For k=1 use the sharper v7 bound 2 I_data+4 I_selectors. Hence H(F_k)<=max(C+6,9)I(F_k) for ALL k>=1. This keeps arbitrary overlapping branch cores as explicit hypotheses; it does not iterate that +6 across a new hierarchy.

The repaired rare-switch ledger pays genuinely noncollinear arbitrary branches from ONE original source at every depth, with multiplier3 and necessary multiplier>=2. The first unsupported universal step is extending its single surviving activation path to an arbitrary branching/mixed mux decomposition while assigning shared physical energy once and retaining the inherited A,B bills. The complete-quadratic obstruction to fresh-ticket renewal from v7 still applies. Do not sum the source again at a descendant. Next: test an actual second surviving branch with ORIGINAL ticket and first debit retained; establish an ownership/refund inequality or give its exact Boolean failure. Full FEI is OPEN.
