# One further arbitrary core query from an ORIGINAL whole-core owner

All cubes are finite, uniform, and physically disjoint as stated. Entropy and logarithms are in bits. Full FEI remains OPEN. The new conclusion is an expected-resource stopping ledger, with explicit branch innovations; it is not a pathwise subtraction-only cash account.

## 1. A universal one-query bound without FEI

For every Boolean g and coordinate i, put d=Inf_i(g), delta=min(d,1-d), and D=H(g)-(H(g_0)+H(g_1))/2. Then

    I(g) >= d + delta log2(1/delta).                  (1)

To prove this, let A={x:g_0(x) != g_1(x)}, of density d. The sign g_0 g_1 has influence at most I(g_0)+I(g_1)=2(I(g)-d), by the union bound on each physical edge. Cube edge isoperimetry, applied to A or its complement, gives I(g_0 g_1)>=2 delta log2(1/delta), proving (1). Endpoint products are constant and the term at delta=0 is zero.

Here is a proof of the isoperimetric input to fix its normalization. An N-cube set of size a spans at most a log2(a)/2 edges. Induct on N, splitting sizes a0<=a1: cross edges are at most a0, and the induction reduces to h2(a0/(a0+a1))>=2a0/(a0+a1). This is the chord bound for the concave binary entropy on [0,1/2]. Subtracting twice the internal edges from Na gives boundary >=a log2(2^N/a). The influence of the sign is twice this boundary divided by 2^N. No FEI input occurs.

Spectral erasure and the actual child Jensen-Shannon packet obey

    D <= h2(d) + min(1, 2 delta/ln(2)).               (2)

Erasure is at most its binary marginal entropy h2(d), JS<=1 for two equally weighted probability laws, and JS<=2min(d,1-d)/ln(2) follows by summing the amplitude-pair bound proved in A057 PROOF Section2. These inequalities apply to the actual full child spectra.

Let ell=log2(3), and define

    kappa = (3 ell+1)/(ell+1) = 3-2/(1+ell).

Then 2<kappa<9/4: ell>1 and ell<5/3, the latter certified by 3^3<2^5. We claim

    D_i H(g) <= kappa I(g).                          (3)

For d<=1/2, write a(d)=d(1+log2(1/d)). By (1), I>=a(d). Since ln(2)>2/3 (the first two positive atanh(1/3) terms already exceed 2/3), (2) is bounded by h2(d)+min(1,3d). On [0,1/3], kappa a(d)-h2(d)-3d is concave: its second derivative is [1/(1-d)-(kappa-1)/d]/ln(2)<=0 because kappa>2 and d<=1/2. Its continuous endpoint values at 0 and 1/3 are both zero. On [1/3,1/2], kappa a(d)-h2(d)-1 is likewise concave, with endpoint values 0 and kappa-2>0. Both differences are nonnegative by their chords. If d>=1/2, (1) gives I>=d+delta=1, while D<=2. This proves (3), including irrelevant and constant cases.

This constant is sufficient, NOT asserted optimal. AND2 has H=2,I=1 and a first query whose BOTH full child entropies are zero, so every universal one-query whole-core rate must be >=2. Products of r disjoint AND2 factors, one such query in EACH factor, force cost 2r from the sum r of the factor owners. A fixed global additive slack cannot repair a factorwise rate below 2. This statement is about additive one-shot factor owners, not reusing one owner r times.

## 2. Independently reconstructed source profile and original exterior escrow

For F=K+Cg, where K=0 on the indicator C and is a sign off it, t=E C and mu=E g, set eta(x)=-x log2(x). Direct Fourier multiplication yields

 E(K,C;mu)=H(F)-t H(g)
   =sum_s eta((Khat_s+mu Chat_s)^2)
     -t eta(mu^2)+(1-mu^2)sum_s eta(Chat_s^2).        (4)

The core-frequency marginal is (1-t)delta_empty+t ghat^2 because sum_s Khat_s Chat_s=E KC=0. Its entropy lies between tH(g) and tH(g)+h2(t); conditional exterior entropy lies between zero and the remaining exterior dimension r. Consequently

    0<=E(K,C;mu)<=r+h2(t).                           (5)

These arguments independently reconstruct A059's scalar module and preserve ALL nonempty core frequencies. No inaccessible H(g) appears on the right side of (4).

Now use its actual family: m>=4 divisible by4, b=(-1)^(sum_j x_(2j)x_(2j+1)), C=1_(x=1^m), c=2^-m, K=b-C, and F=K+C G chi_J, where J is a nonempty fresh character block and G is ANY actual independent Boolean core. The ORIGINAL physical exterior and core influences are

    I_X(F)=m/2-mc,        I_Y(F)=c I(G).

Freeze exterior B0=4 I_X(F)=2m-4mc. Execute the source's optional specified old core query j before any exterior/tag query, of actual cost d_old=c D_j H(G)<=2c. In both full old children a, retain G_a and the SAME nonempty tag. At this frontier E_start=E(K,C;0) is the same in both children. Put

    L=B0-d_old-E_start >=m/4.                        (6)

Indeed E_start<=m+1, so L>=m-1-(4m+2)c>=3m/4-9/8>=m/4 for m>=4. In the middle inequality use 4mc<=m/4 and 2c<=1/8. This is an expected-resource ledger. Child profile differences are funded by zero-mean branch innovations, not by a claim that all child allocations equal their parent minus the debit.

## 3. Pay ONE additional core query at ANY exterior/tag stopping frontier

Add precisely ONE ORIGINAL whole-core owner

    M0=kappa c I(G)=kappa I_Y(F).                    (7)

This is priced by original actual influence, never by an assumed entropy bound. Let r_old=kappa c Inf_j(G) if the old query is executed, and zero otherwise; set G_a=G when there is no old query. After the old query, transport pending core capacity kappa t I(G_a), and keep r_old as unused cash. At the old split its conditional mean plus r_old equals M0, since I(G)=Inf_j(G)+E_a I(G_a). This releases original capacity without reversing the actual d_old already booked to B0.

Before any additional core query, allow ANY finite adaptive exterior/tag history and arbitrary stopping. With current surviving point density t and signed current core h=+/-G_a (including any remaining nonempty tag in the wrapper profile), define

    B_v=L+E_v+r_old+kappa t I(G_a).                  (8)

Tag queries leave I(G_a), H(G_a) unchanged. Exterior queries make t a martingale, and change the exact E profile as in (4); physical restrictions of K,C are used even on dead masks. All profile innovations are explicit. The component tH(G_a) remains harmonic.

At ANY chosen reached node, permit ONE additional actual core query i, adaptively selected using all previous physical answers. Its parent/child entropies satisfy EXACTLY

    D_i H(F_v)=t D_i H(G_a)+E_v-E_child E_childprofile. (9)

This holds before or after tag collapse: H(+/-G_a)=H(G_a), and a remaining character changes its mean to zero without changing its entropy. Query i with t=0 is irrelevant and costs zero. Pay tD_i H(G_a) from the pending core owner. By (3), the remaining ORIGINAL cash

    R_v=t[kappa I(G_a)-D_i H(G_a)] >=0              (10)

is nonnegative. In EACH full child retain its exact E_child, r_old, and the SAME R_v; close the pending whole-core owner. Now freeze the child core, but allow arbitrary further adaptive exterior/tag queries and stopping. Carry R_v as constant cash through these queries. If the extra query never occurs on a branch, its original pending owner remains in its terminal. There is at most ONE extra core query on EACH path, not one globally preselected node.

At the extra query, (9) and (10) give the exact expected-resource identity B_parent=D_iH(F_v)+E_child B_child. At exterior/tag queries it follows from harmonicity of tH(current core); at the old query it follows from the original-owner allocation above and its already booked actual cost. Thus every finite allowed tree satisfies

    H(F_root)=B0+M0+E_leaf[H(F_leaf)-B_leaf],
    B_leaf>=L>=m/4.                                 (11)

ALL actual old siblings, stopping leaves, and full terminal functions are retained. No controller/DATA import, no FEI assumption on G, no density reset, and no new source account is used. Individual child owners can exceed the parent; their mean is exactly governed by the local entropy debit. Equation (11) claims no stronger pathwise cash-only subtraction property.

### 3a. Handoff AFTER an actual admitted exterior-cash budget is exhausted

The pinned source is A059-EXACT-EXCESS-ESCROW-AND-CORE-OWNER-OBSTRUCTION@2, not its earlier frozen-core draft. It already pays m/4 additional arbitrary core queries, or longer histories admitted by L_v-2t_v>=m/8, from its original exterior cash. Those already paid queries are NOT new progress here.

Our ORIGINAL core bank can be carried unused through ANY such already paid finite prefix. At every previously paid core query i, update the pending bank to kappa t I(g_child), and add kappa t Inf_i(g_parent) to separate unused original cash R in BOTH children. Conditional influence conservation makes the total core bank harmonic at that split. At exterior queries, t is harmonic and R is constant. At tag queries, neither core influence nor R changes. Thus this transports precisely the SAME M0 from (7), irrespective of how many source-admitted core queries occurred or which coordinates were chosen adaptively. All their actual inherited-core fees a=t D_iH(g) remain debited ONCE to the source's current L; the released influence capacity was never spent, and is not an entropy refund.

At a reached prefix frontier with current source cash L_v>=m/8, including one where the NEXT predictable source admission L_v-2t>=m/8 FAILS, apply (9)-(10) to the CURRENT actual restricted core. Pay a from its current pending original core bank, retain old R, freeze the children, and continue arbitrary exterior/tag histories. The source's L_v stays diminished at its actual value. Formula (11) holds with B_leaf>=m/8 rather than the narrower m/4 bound; no old fee is canceled and no original core account is restarted. This is a genuine continuation beyond A059@2's admitted exterior-cash boundary.

For its stated m/4 guarantee, the source estimate can be independently checked: E_start<=m+h2(c), h2(c)<=11/32 for c<=1/16, and 4mc<=m/4. After old fee<=2c<=1/8, L>=3m/4-15/32. Each further core fee is<=2, so m/4 such queries leave L>=m/4-15/32>=m/8. Predictable admission uses the sharper CURRENT fee upper bound 2t. This reconstruction preserves the source's expected-resource scope.

The separate prefix certificate uses m4, a fixed actual core of128 disjoint AND2 factors, and leaves exterior/tag untouched. Query a fresh factor's first bit along its constant-child spine while the source admission allows it; every complementary old sibling stops with its full literal-times-remaining-core function. Each actual fee is2c=1/8. At the first failed admission the current L remains>=1/2. One further fresh-factor query is then paid from the transported ORIGINAL core bank; both of its actual children and all old siblings remain. Only two-bit factor tables and exact product formulas are used, never a 256-core-bit truth table.

## 4. Sharp obstruction to refreshing this owner at the same rate

The pending owner in (8) belongs to the ENTIRE current inherited core, and is consumed once. Replacing (10) by fresh kappa t I(G_a|i=a) accounts, without another original payer, would require D_iH(G_a)<=kappa Inf_i(G_a), which (3) does NOT say.

An actual normalized obstruction is G_s=b_s-C_star+C_star chi_z, s>=4 divisible by4, with paired bent b_s, C_star the all-one point, c_s=2^-s. Its rare tag z has influence c_s and full decrement D_z>=c_s(s-1). Here is the direct lower bound: b_s has amplitudes of magnitude sqrt(c_s), C_star amplitudes of magnitude c_s. At every exterior frequency |Khat|>=sqrt(c_s)-c_s. The erasure at z is sum Phi(Khat^2,Chat^2). Since Phi(a,b)>=b log2(a/b), its erasure/c_s is at least log2(((sqrt(c_s)-c_s)/c_s)^2)>=s-1 for s>=4. JS is nonnegative. At s=4 already s-1>kappa. Both tag terminals b_s and b_s-2C_star are retained.

For any fixed refreshed rate K, choose a fixed s with s-1>K and tensor r independent copies of this ACTUAL core. Query only the rare tag in each factor. Spectra factor, entropy and influence add, and the local refresh deficit grows at least r c_s(s-1-K). No FIXED global additive slack repairs that reset rule. Per-factor slack or new original resources survive tensorization and are not excluded.

## 5. An actual complete-core obstruction, including the fixed exterior allowance

The one-shot rate cannot pay a complete core tree even if ALL of the fixed exterior owner is also available. Let A_n be the AND sign, negative only at one point, p=2^-n. Direct Fourier sums give

    I(A_n)=2np,
    H(A_n)=eta((1-2p)^2)+8p(1-p)(n-1),
    H(A_n)/I(A_n) ->4.                              (12)

For the limit, the second term divided by I tends to4, while 0<=eta((1-2p)^2)<=4p/ln(2), so its ratio is at most2/(n ln(2))->0. These are exact finite formulas, not numerical extrapolation.

Fix the source m=4, so c=1/16 and B0=7, and use the actual core G_N=product of N independent A_4 factors. Its entropy is N H(A_4), its influence is N/2, and querying its complete core while tag/exterior stay untouched costs EXACTLY c N H(A_4). All full core terminals are K+/-C chi_J, of the same entropy E_start; none is discarded. At N=256 the full debit is16 H(A_4), whereas the ENTIRE original proposed two-owner budget is7+8 kappa. Their difference is rigorously positive (see boundary certificate). The first actual core query has positive cost c[H(A_4)-H(A_3)/2], so this includes the old debit without a reversal.

More generally, suppose a complete-core extension uses only B0+K c I(G), with B0 fixed as the exterior family is fixed. For every K<4, choose one fixed n with H(A_n)>K I(A_n), then tensor r A_n factors. The deficit is r c[H(A_n)-K I(A_n)]-B0, tending to infinity. Thus any universal COMPLETE-core rate for this interface must be at least4, even with a fixed global additive exterior/slack allowance. This does not prove rate4 sufficient and does not refute FEI. Per-factor or core-influence-proportional supplementary budgets remain material under tensorization.

Indeed the scalar universal complete-core budget assertion cH(G)<=B0+KcI(G) for ALL Boolean G is EQUIVALENT to FEI(K): substitute the product of r copies of any fixed G and divide by rc, then send r to infinity. Conversely FEI(K) gives that assertion immediately. The fixed exterior owner changes only an additive constant. This equivalence concerns the aggregate complete-core budget; it is not a new constructive all-history source supplier.

## 6. Honest boundary

The one-more-query bridge is closed at the exact expected-resource scope of (11), for arbitrary G, all source dimensions, all exterior/tag histories, and a pathwise stopping choice of the extra coordinate. Section3a includes a handoff AFTER actual A059@2 cash-admission exhaustion, retaining a floor m/8. It uses the original whole-core owner ONCE. Arbitrarily many further core queries would require paying their aggregate debits from the remaining original core cash while retaining full core terminal entropy. The same two-owner extension at rate kappa is FALSE by Section5, not merely unproved. A universal complete-core original source bound needs a rate at least4 and is still FEI-scale. The earlier exterior-only obstruction remains valid. The sufficient ONE-query kappa is not proved optimal; its necessary lower bound is2.
