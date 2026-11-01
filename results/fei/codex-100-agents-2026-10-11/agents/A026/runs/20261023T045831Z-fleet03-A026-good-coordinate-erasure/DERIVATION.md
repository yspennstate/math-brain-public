# Carried nonempty profiles commute with physical DATA queries

Author derivation with exact finite validation; independent human review pending. Bits, uniform Boolean cubes, ordinary physical influence. Full FEI is OPEN. This changes mechanism because A097@stage18 already closes the previous original-source-return NEXT.

## 1. Exact entropy decrement and physical reference transport

Let f have squared Fourier law P. At query j write M_j for deletion of frequency bit j and P_z for the actual child law, z=0,1. Then M_j P=(P_0+P_1)/2 and

    Delta_j H=B_j+JS(P_0,P_1), B_j=H(P)-H(M_j P).

For a normalized reference Q finite on P, use the actual-phase pair channel

    k_z(T)=P_z(T)/(2 M_j P(T)),
    rho_z=sum_T M_j Q(T) k_z(T),
    Q_z(T)=M_j Q(T) k_z(T)/rho_z.

On a zero-true pair prescribe k_0=k_1=1/2. Finite CE implies rho_z>0 because each actual physical outcome has probability1/2. The joint true child law is P_z/2. KL disintegration gives

    CE(P,Q)=Delta_j H + mean_z CE(P_z,Q_z)
             + E_true_fiber KL(P(bit|T)||Q(bit|T))
             + KL((1/2,1/2)||(rho_0,rho_1)).                 (1)

Both last terms are nonnegative. Reset differences reconcile the full terminal CE; they must not be added a second time to a path cost already containing that changed terminal CE. The first pilot detected exactly that checker double count; the corrected checker keeps physical payment and signed reconciliation as separate identities. This is the true entropy-decrement ledger; it does not replace Delta H by B alone. All zero-true reference rows, branch masses and normalizers are retained.

## 2. A general profile-commutation lemma

Keep a Boolean controller a(Y) intact and disjoint from DATA X. Write the Boolean mux f=A(X)+a(Y)D(X), with actual Boolean branches G=A+D and H=A-D. Put V=Var(a)>0 and

    pi(U)=ahat(U)^2/V, U!=empty,
    eta_f=sum_{U!=empty,T} P_f(U,T)=V Pr(G!=H).

Assume pi(U)>0 for every nonempty U in the admitted reference-profile index set. At some history supply a COMPLETE normalized reference of the form

    Q_b(empty,T)=q0(T), Q_b(U,T)=q1(T)b(U) for U!=empty,   (2)

where q0,q1 are nonnegative, sum(q0)+sum(q1)=1, and b is normalized, positive wherever pi is positive. q0 and q1 need not have the true empty/nonempty split or true DATA marginal. This is essential after a physical query.

For U!=empty the two Fourier coefficients at any DATA pair are ahat(U) times the corresponding D coefficients. The actual phase-channel kernel is therefore the SAME for every nonempty U; the zero-D pair uses the fixed fair kernel. Consequently every DATA query carries (2) to the SAME form with b unchanged. Its rho_z and updated q0,q1 are independent of b. This holds recursively for every adaptive DATA-only tree, including source/character queries and constant endpoints.

At any node change b to b' but retain the ACTUAL CURRENT q0,q1, the whole empty sector, all reference-only atoms and normalization. The signed full-CE transaction is EXACTLY

    C_v=eta_v [D(pi||b')-D(pi||b)].                       (3)

It is not eta_v D(pi||b') unless the carried profile really was pi. Thus the first debit is retained automatically; signed refunds are not discarded. Since disagreement is a conditional expectation over DATA,

    eta_v=(eta_v0+eta_v1)/2.                             (4)

Equations(3)-(4) telescope through ANY finite adaptive DATA tree and ANY number of such profile transactions:

    sum_reset reach C_v
       =E_final eta_leaf D(pi||b_leaf)-eta_root D(pi||b_root). (5)

The same formula permits nonmonotone choices and multiple transactions at one node; it never sums positive parts. The query refunds in (1) are independent of b: subtract the b=pi CE identity and use (4). If initially b_root=pi and every allowed b satisfies D(pi||b)<=dmax, then

    sum true entropy decrements + E full terminal CE
       <= CE(P_root,Q_pi)+eta_root dmax.                (6)

This is a general carried-profile theorem under a supplied factorized reference. It is neither a universal supplier of such a reference nor an existential good-coordinate theorem. Controller queries are excluded: they can change pi and the profile index set.

## 3. Consume A029's actual non-point family and SAME inherited slack

Use the exact family and original references of A029 stage7: a is negative precisely at three controller points0,1,2 on3 bits; g is negative only at000 on3 shared bits; h is negative when at least two shared bits are1; multiply BOTH g,h by a common character chi_m, m>=1. The SAME source references at the original root are uniform on all2^(m+3) source frequencies. First query shared DATA x0; retain child0 fully. In selected child1, G=chi_m and H=chi_m(-1+2A_2). Here

    V=15/16, gamma=3/4, eta=45/64,
    pi=(3/5,1/15,1/15,1/15,1/15,1/15,1/15).

A029@stage7 equation(6) supplies the inherited source-label slack

    Z_m=(23/32) D_Ber(20/23 || 40M/(55M-36)), M=2^(m+2).

This is the ORIGINAL inherited child Z, never a renewed descendant JS grant. Here is the independently reconstructed scalar proof. For m>=1, M>=8 and 8/11<beta_M<=80/101<20/23, with beta_M decreasing in M. The derivative of D_Ber(p||b) in b is (b-p)/(b(1-b)ln2)<0 on this interval. Thus Z_m>=Z_1. Taylor in the true parameter p, whose curvature is1/[p(1-p)ln2], lower-bounds Z_1 by (23/32)(20/23-80/101)^2/[2(80/101)(21/101)ln2]=135/(10304 ln2). The strict trapezoidal integral bound for1/x on[1,2] gives ln2<3/4. Hence

    Z_m>=135/(10304 ln2)>45/2576>1/64.                   (7)

The general theorem above is independent of this family. Its integrated funding corollary imports precisely (7) and the source admission from A029; finite reconstruction checks the actual source posterior at the selected child.

## 4. Repeated genuine changes up to theta=3/16, not just1/8

Prescribe b_theta=(1-theta)pi+theta Uniform_7, for ANY real theta in[0,3/16]. Its KL d(theta)=D(pi||b_theta) has derivative0 at0 and strictly positive second derivative, so it is increasing. At the maximum

    b_(3/16)=(18/35,17/210,17/210,17/210,17/210,17/210,17/210),
    eta d(3/16)=(9/64) log2(16807/15606)<1/64.           (8)

The last strict sign is the exact INTEGER inequality

    16807^9 < 2*15606^9.

No numerical extrapolation in m or theta occurs. Start with the actual first theta=1/8 transaction proved by A029. Thereafter expose arbitrary DATA coordinates, carry the CURRENT changed reference by (1), and make any number of changes to any theta in[0,3/16]. Equations(5)-(8) pay the TOTAL signed transaction bill, INCLUDING the first one, from the SAME selected child's Z. The child's inherited reserve left is strictly greater than

    45/2576-1/64=19/10304.                              (9)

The initial selected physical reach is1/2, so the original-root remainder is>19/20608. This larger allowed profile interval spends more than A029's single1/8 transaction: its earlier>1/128 child remainder is not asserted for the larger interval. There is no contradiction between these different payment scopes.

One explicitly positive second transaction: after theta=1/8, query shared x1. Its actual child disagreements are1/2 and1. Reset either child, or both, from the carried b_(1/8) to b_(3/16). Every selected second charge is eta_child[d(3/16)-d(1/8)]>0. With m>=1 both mux children and all four source children remain nonconstant. The complementary branch keeps its complete CURRENT reference.

## 5. Original influence quota and universal first unsupported line

Reconstruct A029's exact initial admission: I(F_m)=m+29/16, H_root<=6, W_root<=m+3, SAME U=4I(F_m), unrelated old debit1/8. The common character shifts every squared Fourier coefficient, so H_root equals the6-bit unshifted entropy and is<=6; a complete uniform source law costs m+3 bits, so W_root<=m+3. Every character coordinate is pivotal everywhere and adds1 influence; direct core edge counts give29/16. Thus the original admission reserve is>=3m-15/8. For the initial source refs put Aroot=Wroot-mean Wchild>=0 by the individual source-channel KL contractions in(1), and Df_child=Wchild-Zchild by conditional label KL. Consequently the true root entropy decrement plus BOTH complete prescribed child costs equals Hroot+Wroot-Aroot-mean Zchild. This directly derives the initial funded ledger without assuming an unreviewed universal supplier. All earlier DATA erasures, source contractions, both original terminals and all new phase-query refunds are retained. With (9), every history above has complete payment less than

    U-1/8-[3m-15/8+19/20608].                          (10)

This leaves>9/8+19/20608 for every m>=1. The whole-quota reserve and the selected child's Z are DIFFERENT accounts and are not added twice. The general history lemma uses no C0 reference re-admission. At m=0 the specific child Z is exactly0 while every nonzero theta transaction costs positively, so deleting the inherited-slack eligibility fails; the theorem does not claim otherwise.

The first unsupported universal line is an influence-priced complete source/reference and profile eligibility for arbitrary Boolean sources. A controller query after these DATA transactions also changes the true pi and lies outside (2)-(5). This stage closes repeated DATA/profile transactions under a supplied factorization; it does not pay arbitrary conditional-profile reshaping, controller exposure, or prove full FEI.
