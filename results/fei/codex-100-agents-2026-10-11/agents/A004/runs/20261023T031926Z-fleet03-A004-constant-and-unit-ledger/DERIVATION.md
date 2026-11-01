# A proper active query repairs the source-spreading frontier

Full FEI remains open. This result concerns the same specified neutral AND3/Maj3 Boolean source and one unchanged ancestor quota. It does not supply an influence-priced reference for arbitrary Boolean functions. Entropy, cross-entropy and KL include the empty set and use bits.

## Source reference and independent reconstruction

Let b(y)=+1 iff the first three of six binary data bits are zero, c=b except c(0)=-1, and F choose b or c according to a fresh balanced Maj3 encoder on three bits. The original quota is 4(I(b)+I(c))/2=3. Put T0=(H(b)+H(c))/2, S4=3-T0. No descendant 4I-H surplus is added.

Query data y3 (physical bit6). Its two actual functions are f_on and f_off, with laws p_on and p_off. Let B0 be the executed erasure, m the parent spectral marginal and Rold=7m/8+U256/8 the already booked old reference in BOTH children. The old complete liability is C_old=B0+mean CE(p_child,Rold).

Here is a source-only reference prescription for the on-child and its later edited daughter. Let g=1-2A_k on r data bits, with the first k active, s=2^-k, mu=1-2s, t=2^-r, e=t, and Pg its squared spectrum. Let the actual edited Maj3-encoded law be p(S,T), and q(T)=sum_S p(S,T). Define

    V(empty)=mu^2, V(T nonempty)=(1-mu^2)/(2^r-1),
    R_z=(1-z)Pg+zV,
    Rprime_z(T)=(1-e/s)R_z(T)+(e/s)mu*1_empty(T)+2e/2^r,
    Q_z(S,T)=Rprime_z(T)*p(S,T)/q(T).                   (1)

Only (k,r)=(3,5) and (2,4) are used. Formula (1) has no inherited reference as an input. Its controller conditional kernel is known from this particular source geometry. Expanding g+2 psi*1_origin, with psi the negative-Maj3 event of mean1/2, gives

    q(T)=ghat(T)^2+2e*ghat(T)+2e/2^r.

At empty ghat=mu; at a nonempty active set ghat=-2s; elsewhere ghat=0. Substitution gives Rprime_0=q. The coefficients 1-e/s and all constant floors in (1) are positive at both used parameter pairs. Normalization follows from 1-e/s+(e/s)mu+2e=1, since 1-mu=2s. All q(T)>0; hence the displayed division is legitimate. Each Q_z is normalized, affine in z, and positive wherever the actual p is positive. Joint reference-zero atoms are actual-zero, so no invalid logarithm occurs. These are complete references, including every reference-only atom; full support on the whole joint cube is not required.

For the first retained off-child prescribe Qoff_alpha(S,T)=[(1-alpha)Pg(T)+alpha V(T)]1_{S=empty}, using k3,r5. Its alpha0 law is the actual p_off. Thus both endpoint families start at their actual laws.

The complete source-frontier liability is

    C_in(lambda,alpha)=B0+CE(p_on,Q_lambda)/2
                           +CE(p_off,Qoff_alpha)/2.       (2)

It equals C_old plus BOTH signed reference reset prices with reach1/2. The original root debit H(F)-T0 and old mixture reset have not disappeared: their signed changes cancel algebraically when (2) is written in its direct form. The checker reconstructs both expressions. A001's source bound is independently reproduced: C_in<3-42173/10^6 for lambda<=1,alpha<=3/4; on-only reset keeps >201237/10^6; the first-frontier endpoint(1,1) exceeds3 by >153188/10^6. These statements HOLD at their original source scope. This review covers A001's new canonical calculations, not an independent re-review of A004's own earlier reference lemma.

## The active query and its actual refund

Start at the admitted corner lambda=1,alpha=3/4. In the on-child query one of the three active data bits, physical on-child index j=3,4,5. The zero outcome is the edited daughter a with k2,r4; the one outcome is the constant d=-1. The original off-child remains unqueried and nonconstant, with its full reference retained.

Let r be the marginal of the CURRENT Q_1, and m_on the same marginal of p_on. Physical signed amplitudes satisfy a_child(T)=a_parent(T)+epsilon*a_parent(T+j), so mean child squared law=m_on. The actual conditional-KL refund is

    c=D(p_on||Q_1)-D(m_on||r)>=0.                       (3)

The finite KL chain rule proves its sign, including zero packets. It gives the exact local reference identity

    B_j(p_on)+[CE(p_a,r)+CE(p_d,r)]/2
      = CE(p_on,Q_1)-c.                                (4)

References remain positive on actual supports after marginalization. The zero-mass terms contribute zero, and every logarithm used has positive argument. Equation (4) follows also directly by subtracting CE(p_on,Q_1)-CE(m_on,r): the difference is B_j+c. No JS charge is added on top of this identity.

Now prescribe Qnew_beta for a by (1), k2,r4, beta in[0,1]. Prescribe the EXACT constant source law delta_empty for d. This is not silently replacing a constant terminal's incoming CE by zero: book its signed reset

    E_a=CE(p_a,Qnew_beta)-CE(p_a,r),
    E_d=CE(p_d,delta_empty)-CE(p_d,r)=-CE(p_d,r).

The original whole-tree liability is

    C_mid=C_in-c/2+(E_a+E_d)/4
         =B0+B_j/2+CE(p_a,Qnew_beta)/4
                         +CE(p_off,Qoff_(3/4))/2.        (5)

The new constant terminal contributes its complete CE, which is exactly zero only after its explicit reset. All three terminals, with reaches1/4,1/4,1/2, remain in the ledger. Exact certificates show C_mid<3-303343/10^6 for every beta in[0,1].

## Pay the retained sibling's previously excessive spread

On the SAME original off-child change Qoff_(3/4) to Qoff_alpha_new, alpha_new in[3/4,1], charging

    E_far=CE(p_off,Qoff_alpha_new)-CE(p_off,Qoff_(3/4)).

Its reach is1/2. The final bill is

    C_final=C_in-c/2+(E_a+E_d)/4+E_far/2
           =B0+B_j/2+CE(p_a,Qnew_beta)/4
                             +CE(p_off,Qoff_alpha_new)/2. (6)

In particular, beta=alpha_new=1 is paid, with

    3-C_final > 107981/10^6 bits.                        (7)

At the maximum-spread endpoints, the exact margin lies in (107981,107982)/10^6. The larger intermediate margin lies in (303343,303344)/10^6. These are different frontiers from the original failed source(1,1) liability: (6) includes a real active query and a new k2 daughter reference. The earlier failed endpoint remains a correct failure at its own first frontier.

The single-owner form of (7) is

    S4 -(H(F)-T0) -(C_in-H(F))
       +c/2 -E_a/4 -E_d/4 -E_far/2 > 107981/10^6.        (8)

The checker verifies (8) exactly as a prime-log identity. Thus both old source resets, the initial mixture reset, original admission debit and new bookings are all retained. Cross-sibling use of the globally released capacity is allowed; no assertion of a separately nonnegative bank inside every child is made.

## Continuum and all later histories

For fixed actual p, CE(p,Q_z) is convex in z because Q_z is affine and positive on actual support. As Q_0=p, its excess over H(p) is KL, nonnegative and minimized at0. Convexity then implies nondecreasing CE on[0,1]: for0<x<y, convexity gives (D(x)-D(0))/x<=(D(y)-D(0))/y and nonnegative slopes. Thus the upper endpoint beta1 is worst. The far sibling has the same property in alpha. Endpoint certificates prove the entire real rectangle beta in[0,1],alpha_new in[3/4,1], not merely the diagnostic grid. The initial admitted lambda in[0,1],alpha in[0,3/4] may also vary: the final direct bill (6) is independent of initial lambda,alpha once their signed changes are booked, and each initial frontier is paid by A001's verified rectangle. All three active coordinates have identical analytic formulas by data permutation; each is also checked directly.

Below the final frontier allow arbitrary finite adaptive physical stopping trees, with each new reference obtained by marginalization of the current reference in BOTH outcomes, and with no further fresh reset. Iterating (4) subtracts nonnegative conditional KL, so the complete final liability can only decrease. Therefore the SAME remaining margin (7) pays all later such histories, with all complete terminal cross-entropies. Randomized policies follow by averaging fixed random seeds.

In nats, multiply EVERY term in (2)--(8) by ln2. No influence, pivotal probability or sign/indicator normalization is changed. The refunded c is KL in bits, not a Renyi divergence or an additional source influence allowance.

## First unsupported universal line

The reference kernel (1), original quota3 and active AND3-to-AND2 geometry are fixed and explicitly known. Nothing here constructs an influence-priced reference for arbitrary Boolean roots or bounds a fresh canonical reset after arbitrary mixed active/dummy/controller histories. In particular a later query may alter the conditional nonempty shape in a way (1) no longer covers. NEXT is one genuinely mixed data/controller or dummy query in the ALREADY reset daughter, with Qnew_1, the maximally spread retained sibling, all old debits and (7) as the only unused global owner. Its true conditional-KL refund and prescribed next source law must be evaluated rather than renewing S4.
