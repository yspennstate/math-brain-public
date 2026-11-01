# Projection history review and the local sharpness guard

All entropies are in bits. The all-dimensional projection/profile theorem of A012 survives reconstruction. It does not supply the initial influence-priced reference. The supplementary sharpness statement concerns a LOCAL queried-coordinate payment, not the best global FEI constant or the best coefficient of total root influence.

## 1. Query identity and complete profile fee

Let P be the squared spectrum of an actual Boolean parent and Q a normalized covering reference, with all reference-only atoms retained. For a physical coordinate i let p=pi_i P, q=pi_i Q. If a_T,b_T are the child amplitudes, parent amplitudes are (a_T+b_T)/2 and (a_T-b_T)/2. Thus (P_++P_-)/2=p, including cancellation and zero rows. Both children inherit exactly q. Define L=D(P||Q)-D(p||q)>=0 and J=(D(P_+||p)+D(P_-||p))/2. Directly expanding the finite sums yields

    average D(P_child||q)-D(P||Q)=J-L.

This uses the true child mixture, not either individual child. Cover of P implies cover of both children by q, because a nonzero child amplitude requires some nonzero parent amplitude in that row.

For an arbitrary finite atom partition write p_c,q_c for profile masses and r_c=(1-t)q_c+t p_c. Preserve old conditional reference laws within each cell. For 0<t<1,

    D(P||Q)-D(P||R)-D(R||Q)
      = sum_c (p_c-r_c) log2(r_c/q_c)
      = (1-t)/t [D(r||q)+D(q||r)] >=0.

Cells q_c=0 have p_c=0 and are omitted. At t=0 nothing changes; at t=1 the left side is zero. A zero p_c can delete reference-only mass at t=1; D(R||Q) is still finite, while D(Q||R) need not be. No division by a zero p_c is used. The scalar t is common to the cells; arbitrary unrelated cellwise steps are outside this identity.

For real child amplitudes a,b, e(a,b)=[a^2 ln(2a^2/(a^2+b^2))+b^2 ln(2b^2/(a^2+b^2))]/2 <=(a-b)^2/2. Absolute values can only lower the right side. Write a=u(1+t), b=u(1-t) after that replacement. With j(t)=e(1+t,1-t), j(0)=j'(0)=0 and

    j''(t)=2 ln((1-t^2)/(1+t^2))+4/(1+t^2)<=4.

Integration and continuity at t=+-1 give the assertion, including zero amplitudes. Consequently J<=(2/ln2)Inf_i. The identity I(parent)=Inf_i+average I(children) is the exact physical influence telescope.

## 2. Finite adaptive histories and source ownership

For every finite adaptive tree of the permitted queries and calibrations, multiply each local identity by actual physical reach w_v and add. A reference update does not change the physical function or its reach law. Every interior divergence cancels. If s_v is the nonnegative profile slack above, exactly

    E D_terminal + sum_query w L + sum_update w fee
      = D_root + sum_query w J - sum_update w s.

Also sum_query w Inf_i=I_root-E I_terminal<=I_root. Hence the left side is at most D_root+(2/ln2)I_root. Adding the signed entropy telescope H_root-E H_terminal and a fixed old booking b gives A012's complete bill bound

    bill <= b+CE(P_root,Q_root)+(2/ln2)I_root.

All terminals, all fees, all query contractions and old bookings stay in this equation. Arbitrary finite stopping policies follow by summation or backward induction; there is no descendant source renewal. Infinite histories are not asserted. Positive parts of entropy changes, arbitrary reference resets and required true-kernel inheritance are not covered. For disjoint tensors of supplied normalized references, initial CE and I add; arbitrary interleavings already fall under the all-dimensional theorem. No new gate, label-entropy, or root-normalizer bound follows from this reference statement.

## 3. The local coefficient is sharp for actual Boolean functions

Let m>=4 be even, N=2^m, and c(x)=(-1)^(x_1 x_2+...+x_(m-1)x_m) on bits. Its Walsh coefficients are epsilon_T/sqrt(N), epsilon_T in {+-1}: each two-bit factor has four amplitudes +-1/2, and disjoint products multiply them. Set h=c-2*1_{x=0}. Since c(0)=1, h is again Boolean. Form the actual fresh-selector mux with children c,h. Its parent row amplitudes are

    u_T=epsilon_T/sqrt(N)-1/N,  v_T=1/N,
    d=Inf_selector=sum_T v_T^2=1/N.

Choose Q=P_parent, so the FULL projection contraction L is zero. Stop after querying the selector, with no reference updates. The signed entropy-plus-terminal-CE bill is exactly H_parent+J. Any bound that charges this increase at c*d must therefore have c>=J/d.

For m>=4, the two child amplitudes in each row have the same sign. Set t_T=v_T/u_T. Then |t_T|<=r=1/(sqrt(N)-1)<1 and e(a_T,b_T)=u_T^2 j(t_T). For |t|<=r, put x=r^2. The inequalities ln(1-x)>=-x/(1-x) and ln(1+x)<=x imply

    j''(t)>=4-8x/(1-x).

Integrating twice (j is even) gives

    (2-4/(N-2sqrt(N)))*v_T^2 <= e(a_T,b_T)<=2*v_T^2.

N-2sqrt(N)>0 throughout m>=4. Summing, dividing by d ln2, and sending even m to infinity yields

    J/d -> 2/ln2.

Thus 2/ln2 cannot be reduced in the universal LOCAL per-coordinate inequality, even with actual Boolean parents and Q=P. This does not prove that the total-root-I coefficient in the all-history theorem is globally optimal: the bent family's other-coordinate influence remains large. Improving the local scalar coefficient is not a route to funding the unpaid original source.

## 4. Activation source and support audit

For balanced g and r fresh point controls, p=2^-r, F=1-A+Ag has nonempty-data Fourier sector mass p and conditional law Uniform(control sets) times P_g. Its H=A_r+pH_g and I=p(I_g+r), with A_r=2rp(2-p)-(1-p)^2 log2((1-p)^2). For arbitrary covering Q_F, normalize its data sector and marginalize controls to obtain R_g. Finite KL chain rules give D(P_F||Q_F)>=pD(P_g||R_g), so CE(P_F,Q_F)>=A_r+p CE(P_g,R_g). Arbitrary correlation is retained. Taking g=z times m disjoint copies of arbitrary h and then m->infinity shows that a universal initial influence-priced supplier on this activated family already implies full FEI. This reduction is analytic, not extrapolation from finite tests.

For AND2, parent P is uniform on four atoms. In its constant physical child, projected Q has masses(1/2,1/2), while true-kernel Q is delta_empty. Therefore D(projected Q||true-kernel Q)=infinity. The reverse direction D(true-kernel Q||projected Q)=1 bit is finite: the direction matters. No unrestricted equivalence of these interfaces is asserted.

## 5. Review scope and first unpaid line

A012-UNIVERSAL-PROJECTION-PROFILE-HISTORY@1 reconstructs without a mathematical correction at its stated finite-tree scope. This review concerns the NEW projection/profile theorem. A013's substantive contribution to the older v9 seed precludes independent acceptance of that older full chain and is not counted as such. The local sharpness proof is an auxiliary supporting result, pending disinterested review. Finite checks test identities, boundaries and the actual family; the analytic argument supplies all dimensions and all real calibration parameters. Formal accounting algebra, if admitted, certifies only that algebra.

FIRST UNPAID LINE: provide a useful normalized complete arbitrary-core initial reference with CE(P_f,Q_f)<=C0 I(f), or pay a required compatible-reference conversion from the same unused original influence. Neither local sharpness nor history stability establishes it. Full FEI remains OPEN.
