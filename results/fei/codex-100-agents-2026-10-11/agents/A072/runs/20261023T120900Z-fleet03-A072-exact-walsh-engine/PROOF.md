# A signed composition correction has a universal influence-paid drift

Entropy is in bits, influences use uniform physical coordinates. Full FEI remains OPEN. The new result proves universal coherence for a signed composition envelope, conditional on its initial bank being supplied. It does not supply a universal initial influence bound.

## 1. Domain, complete functions and definitions

Let h be any Boolean gate of finite arity r and let g_j be arbitrary Boolean functions on disjoint finite uniform physical cubes, allowing constants and dummy coordinates. Write F=h(g_1,...,g_r), q_j for the true pivotal probability of h in input j under the other independent core outputs, and

    C(F;g_1,...,g_r)=H(F)-sum_j q_j H(g_j).

This is the SIGNED correction; no positive part is applied. The original partition and gate remain fixed under arbitrary physical restrictions; cores can become constant. Both children are always the full restricted functions. The standard physical edge identity is I(F)=sum_j q_j I(g_j).

For any physical coordinate i in core j, with d=Inf_i(g_j), the new universal assertion is

    mean C(F|i=b)-C(F) <= (4/ln2) q_j d < 6 q_j d

when q_j d>0; use <=6 q_j d also when it is zero. The constant has no dependence on gate arity, total dimension, biases or Fourier spectrum. The quantity q_j d is exactly Inf_i(F).

## 2. Exact entropy decrement, with its sign derived explicitly

For a Boolean u and coordinate i, pair its normalized real Fourier coefficients as a_L=uhat(L), b_L=uhat(L union{i}), where L omits i. Put

    Phi(A,B)=(A+B)log2(A+B)-A log2 A-B log2 B,
    B_i(u)=sum_L Phi(a_L^2,b_L^2).

Zero terms use0 log0=0. The squared Fourier laws of the two Boolean restrictions are (a_L+b_L)^2 and (a_L-b_L)^2. Each sums to1; their mean law is a_L^2+b_L^2. Let J_i(u) be their Jensen-Shannon divergence. Shannon's chain rule gives the exact identity

    H(u)-mean H(u|i=b)=B_i(u)+J_i(u).

In particular the sign before J is PLUS. This follows directly from H(joint)=H(projected)+conditional entropy and mean H(children)=H(projected)-J. No recalled sign convention is used.

We need two elementary inequalities. For any real x,y,

    Phi(x^2,y^2) <= (2/ln2)|xy|.

Indeed ln(1+t^2)<=t for t>=0: the derivative of t-ln(1+t^2) is (t-1)^2/(1+t^2)>=0. Apply this to the two logarithms in Phi; zero arguments follow by continuity.

Also

    J_i(u) <= (2/ln2) Inf_i(u).

For completeness set s=a^2+b^2 and t=2ab/s. One row contributes s G(t)/ln2, where G(t)=((1+t)ln(1+t)+(1-t)ln(1-t))/2. For |t|<=1,

    G(t)<=1-sqrt(1-t^2).

Both sides are even and vanish at0. Their derivative comparison on[0,1) reduces to atanh(t)<=t/sqrt(1-t^2), which follows by differentiating again: (1-t^2)^(-1)<=(1-t^2)^(-3/2). Endpoints follow by continuity. Thus a row contributes at most2 min(a^2,b^2)/ln2, and summing is at most (2/ln2)sum b_L^2, as asserted.

## 3. The one inner coefficient pair which does not factor

Write the fixed outer gate in input j as h(z)=A(z_-j)+z_j D(z_-j), with A=(h(+1,z_-j)+h(-1,z_-j))/2 and D=(h(+1,z_-j)-h(-1,z_-j))/2. Then

    F=A(g_-j)+g_j D(g_-j),    E D(g_-j)^2=q_j.

If the inner Fourier frequency L is nonempty, the full Fourier coefficient is ghat_j(L) times the corresponding physical Fourier coefficient of D(g_-j). When L is empty it is instead Ahat+mu_j Dhat. Consequently EVERY erasure row with a nonempty remaining inner frequency factors exactly. Let t=ghat_j({i}) and mu_j=E g_j. The exceptional full rows, whose remaining inner frequency is empty, contribute a nonnegative quantity B_special. Parseval for D and homogeneity of Phi prove

    B_i(F)=q_j [B_i(g_j)-Phi(mu_j^2,t^2)]+B_special.

This identity includes zero influences and constant other cores without dividing by their variances. For k!=j the unchanged inner entropy H(g_k) is multiplied by q_k, whose conditional mean is conserved under the physical query: q_k is affine in the sign distribution of g_j. Also q_j itself is unchanged. Therefore

    mean C_child-C_parent
      =q_j [H(g_j)-mean H(g_j|i=b)]
        -[H(F)-mean H(F|i=b)]
      =q_j [Phi(mu_j^2,t^2)+J_i(g_j)]-B_special-J_i(F).

Both subtracted quantities are nonnegative. A Boolean derivative gives |t|<=Inf_i(g_j)=d, since t is its signed expectation and d is its absolute expectation. Also |mu_j|<=1. Applying Section2 gives

    mean C_child-C_parent <= (4/ln2) q_j d.

Finally ln2=2 sum_(k>=0)(1/3)^(2k+1)/(2k+1)>2/3, so4/ln2<6. This proves the bound uniformly, without a finite-family inference.

## 4. A coherent signed envelope, retaining the initial-price gap

Take any fixed K>=0, and let rho_j be the full finite stopping hull of (H-KI)_+ for inner core g_j, recomputed on its actual restrictions. Define, with kappa=4/ln2 or with the convenient rational kappa=6,

    A_K(F)=C(F)+kappa I(F)+sum_j q_j rho_j.

This is nonnegative, superharmonic under EVERY physical query, and majorizes (H(F)-K I(F))_+. Indeed C+kappa I is superharmonic by Section3 and the exact physical identity I(parent)-mean I(children)=Inf_i(F). At complete physical revelation it is0, so finite induction proves C+kappa I>=0 everywhere. Separately sum q_j rho_j is superharmonic: the queried core's q_j is unchanged, its rho is superharmonic, and every other q_k has conserved conditional mean while its rho_k is unchanged. Nonnegativity and coherence follow. Finally rho_j>=H(g_j)-K I(g_j), so C+sum q_j rho_j>=H(F)-K I(F); adding the nonnegative influence term proves majorization.

The partition and envelope include all cores from the start. Merely admitting another existing core changes neither their full restricted function nor this envelope. Thus this construction avoids changing local hulls at admission, and the history-transfer shortfall from A072 stage19 is absent. It does not cover changes of the original decomposition without a separate comparison.

If incoming credit a>=A_K(parent) is ALREADY SUPPLIED, allocate

    a_b=A_K(child_b)+a-mean A_K(children).

Both credits are nonnegative and have conditional mean a. Each nonnegative old credit-owner label uses kernel a_b/a (when a=0 both outgoing credits vanish). Full booked debits S_K(child_b)+a_b are nonnegative. If their mean T>0, all old signed debit labels and the new signed query charge e=mean S_K(children)-S_K(parent) use common kernel d_b/T; if T=0 both child debits vanish and kernel1 preserves the signed zero-total labels. All actual reaches and stopped siblings remain intact, with no new outside donor draw. Unused original influence stock kappa I releases exactly kappa Inf_i(F) in conditional mean per query, paying the signed correction's possible increase. This is a potential-headroom identity: actual owner labels follow the conserved-mean allocator, and are not forced to equal each potential component after a query. It is conditional accounting, not a claim that this stock or the rest of the initial bank is newly available after prior spending.

The honest remaining gap is the INITIAL price. With singleton physical-bit cores, every rho_j=0 and C=H(F), hence A_K=H(F)+kappa I(F). A dimension-independent influence bound on this specialization is precisely an FEI bound. We therefore do not treat coherence as proof of initial influence payment. This isolates the unpaid universal line rather than hiding entropy in a claimed influence bank.

## 5. Independent A071 witness review and a paid drift row

A071-POSITIVE-OUTER-CORRECTION-ENVELOPE-FAILS@1 is independently reconstructed without importing its code. For the full AND-of-OR(3,2,2), querying the first bit gives full children AND-of-OR(2,2,2) and AND-of-OR(constant+1,2,2), retaining the two dummy physical bits in the latter. Independent whole-cube characters, inverse signs, Parseval and edge counts precede entropy. They reproduce

    C_parent=57/8-(1431/1024)log2 3-(3087/2048)log2 7,
    C_0=53/8-(1701/512)log2 3-(25/512)log2 5,
    C_1=3-(27/16)log2 3,
    G=mean C_child-C_parent
      =-37/16-(567/512)log2 3-(25/1024)log2 5
        +(3087/2048)log2 7 >0.

All three C values are positive, by the source's independently repeated integer-power inequalities. The queried influence is9/64 and the full parent influence111/64. The inner restriction hulls vanish for every K>=3, proved from the literal g1,g2,g3 spectra and3^9>2^14. Thus the source candidate failure holds unchanged, for all stated K, and its source digest is retained.

The signed repair releases6*(9/64)=27/32 units from the explicitly reserved influence component, against missing drift G between0.107184 and0.107185. Its positive remaining coherence surplus is27/32-G. The source correction fails with no reserve; the new inequality does not manufacture that reserve out of a spent owner. All seven physical parent queries and fixed degenerate/control circuits check the decomposition and rational6 reserve independently of the analytic all-dimensional proof.

The newly read A071-VACUUM-COMPONENT-ENVELOPE statement is background only, not independently accepted or used as a premise here. The present result prices the WHOLE signed composition correction's drift, while leaving its initial nonempty entropy price unpaid. External independent review of this new universal drift/envelope theorem remains pending.
