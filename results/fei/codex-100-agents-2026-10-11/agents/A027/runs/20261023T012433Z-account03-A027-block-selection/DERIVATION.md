# Supporting-line refund through arbitrary point-control interleaving

Rung at creation: analytic derivation awaiting exact validation and independent review. Full FEI remains OPEN. This extends A027's existing partial-core candidate. A028@6 and A029's new general JS ledger retain a separate structural entropy difference; the present theorem prices the FULL point-activation remainder under explicit endpoint conditions.

## Exact statement

Let u be any Boolean sign on m core bits, with negative probability t<=1/16. Let A_r be the indicator that r>=1 fresh independent fair control bits all pass, and F=1+A_r(u-1). Consider ANY finite adaptive physical tree T querying core and control bits in arbitrary order, and stopping immediately when a queried control fails. Condition the ORIGINAL INPUT on all r controls passing and discard deterministic control queries: this yields the actual projected core tree U. Assume every complete U-terminal core has negative probability at most b=1-1/sqrt(2). No pointwise safe-band hypothesis is imposed on intermediate children. All entropies are in bits.

Then, at EVERY partial frontier of T (using the corresponding original-input projected core frontier U),

    Pi_H(F;T) <= 2^-r Pi_H(u;U) + (21/4) Q_control(T).

More precisely the difference is a signed control-tangent bill MINUS one nonnegative frontier refund. The same root tangent is used throughout. If the ACTUAL projected core decrement has an independent price K and every COMPLETE physical terminal has H<=L I, the specified tree gives H(F)<=max(K,21/4,L) I(F). No universally paid K or L is supplied.

## Consumed facts and definitions

Use the previously reconstructed exact activation formula

    H(F_s(v))=p_s H(v)+G_s(d), p_s=2^-s, d=Pr(v=-1),
    G_s(d)=d Hplus(a_s)+R(p_s,d),
    R(p,d)=4d(1-d)eta(p^2)+2d(1-d)V+V E(d)
                         +E(1-2pd)-p E(1-2d), V=4p(1-p).

Here eta(q)=q log2(1/q), E(z)=eta(z^2), and a_s=1-2A_s. Hplus is raw nonempty Fourier entropy. Set G_0=0 (all controls have passed). The prior A027@6 supporting-line theorem gives: for every s>=1, the tangent to G_s at the SAME root t<=1/16 supports G_s on [0,b]. The controller nonempty-entropy term is linear in d and is retained. The needed scalar tangent certificate at1/16,3/10 is reproduced in this stage rather than assumed from a numerical display.

Write T_s(d)=G_s(t)+(d-t)G_s'(t), and U_s(d)=G_s(d)-T_s(d)>=0 on[0,b]. Set T_0=U_0=0. Failed-control states have potential0. This defines one inherited account, with root U_r(t)=0, rather than a new descendant tangent.

For t=0 the core is constant+1 and every actual entropy/influence is zero. For t>0 all derivatives exist. The exact derivative has no residual 1/ln2 term:

    R_d(p,d)=4(1-2d)eta(p^2)+2(1-2d)V
       -4Vd log2(d)+8p(1-2pd)log2(1-2pd)
       -8p(1-2d)log2(1-2d).

The reciprocal-ln2 coefficient cancels as -2Vd+4p(1-2pd)-4p(1-2d)=0. At d=0 take the finite right derivative, with d log d=0.

## New step: the inherited tangent survives each control exposure

A control query with s>=1 controls remaining has actual entropy decrement

    h_s(d)=G_s(d)-(1/2)G_(s-1)(d),

because p_s H(v) cancels against half of p_(s-1)H(v). Its OWN physical queried influence is q_s(d)=2p_s d. Let a_s(d)=T_s(d)-(1/2)T_(s-1)(d), the tangent to h_s at the ORIGINAL t.

An independently useful exact simplification is h_s(d)=A(2p_s d), where A(z)=R(1/2,z)=G_1(z). Indeed the query is a fresh dictator activation of the passing child F_(s-1)(v), whose negative probability is2p_s d; its nonempty dictator-controller entropy is zero. The checker also reconstructs this simplification from the two separate G expressions and full actual Fourier entropies.

We prove a_s(d)<=h_s(d) throughout[0,b]. For s=1 this is exactly the supporting-line theorem for G_1, since G_0=0. For s>=2, 2p_s d<=b/2=d_star and A is convex there, so h_s is convex on the whole required interval. An equivalent check from the old curvature formula gives

    h_s''(d)=16p_s [D(p_s,d)-D(2p_s,d)]/ln2,
    D(p,d)=ln(1-2d)-(1-p)ln(2d)-p ln(1-2pd)+p ln p.

If s>=3 then 2p_s<=1/4 and D decreases in p on this range for d<=b<1/3: D_p=ln z+z+1<0, z=2pd/(1-2pd)<=1/5. For s=2 the needed comparison is exactly

    D(1/4,d)-D(1/2,d)
       =(1/4)ln((1-d)^2/[d(2-d)])>=0,

because 1-4d+2d^2>=0 for d<=b. Continuity closes d=0. Thus convexity proves the tangent inequality at every remaining-control count, including the last exposure where global convexity would be false but the root supporting line remains valid.

Consequently the control query RELEASES, rather than renews, inherited refund

    ell_s(d)=U_s(d)-(1/2)U_(s-1)(d)
            =h_s(d)-a_s(d)>=0.

The control query can be paid at21/4 by a short self-contained scalar estimate. A''(z)=4log2((1-2z)^2/[4z(1-z)]), so A' has its global maximum on[0,b] at d_star. Moreover A'''<0 on(0,1/2), from differentiating the displayed logarithm. Since 1/8<d_star<1/6,

    max_[0,b] A' = A'(d_star)
      <= A'(1/8)+(1/24)A''(1/8)
       = A'(1/8)+(1/6)log2(9/7) <21/4.

The last strict sign is a new exact rational prime-log certificate, reproduced independently. Integrating from A(0)=0 gives A(z)<=(21/4)z throughout[0,b]. Thus h_s(d)<=(21/4)q_s(d) and a_s(d)<=(21/4)q_s(d). There is no new unpriced point-controller lemma in this constant. The earlier C0<6 estimate remains a separate valid bound, but is unnecessary here.

## One account at every actual frontier

Every active node's core negative probability is<=b. To see this, condition original input on all controls passing: its descendant projected leaves form a partition of its remaining CORE cube, so its bias is their conditional average. This is a physical-input argument and introduces no spectral reference. Active projected reach is v=w p_s/p_root; normalizing raw active weights instead is invalid.

Let B(frontier)=sum_active w_v U_(s_v)(d_v)>=0. At the root B=0. At a CORE query the affine tangent cancels and its full activation correction is U_s(d)-average U_s(children), so the correction is exactly minus the change of B. At a CONTROL query, B drops by w ell_s, and the actual entropy cost w h_s splits as w a_s plus that exact released refund. No controller influence is credited twice.

Finite telescoping yields the EXACT identity

    Pi_H(F;T)-p_root Pi_H(u;U)
       =sum_CONTROL w_v a_(s_v)(d_v)-B(frontier).

The root term is zero because the original tangent touches there. The account may decrease at a positive core correction and at a control release, but never becomes negative. This is stronger than a sum of positive local corrections: clipping negative data corrections would destroy it.

Combining a_s<=(21/4)q_s and B>=0 proves the stated mixed-history bound. The independent original-input projection gives Q_core=p_root Pi_I(u;U). The ACTUAL physical influence partition is

    I(F)=Q_core+Q_control+E_terminal I(F_leaf).

If a control fails the entire physical leaf is constant. At every active terminal the full activated core entropy is retained, even if controls remain. Supplied K,L give max(K,21/4,L); neither a low leaf bias nor the scalar supporting line certifies L.

## Guards and unpaid universal step

The endpoint hypothesis is substantive. With u equal to the four-bit point defect (negative probability1/16), one dictator controller, and the COMPLETE core revealed with no control query, the remaining core leaves have biases0,1. The signed activation correction is R(1/2,1/16)>0 while Q_control=0. Thus dropping the endpoint band falsifies the zero-core-surcharge statement on an actual Boolean function. It does not falsify FEI. Likewise the prior selector with root7/32 and children3/16,1/4 gives a positive correction with no controller query, refuting omission of the root condition even when endpoint biases are in the band.

The theorem covers point controls. For a general controller, physical exposure may reach probabilities in(1/4,1/2), where the earlier curvature comparison fails. No extension through those probabilities is asserted. A028/A029's JS ledger is general, but keeps structural costs; replacing the present FULL remainder by JS alone would remove a different bill.

The first universal unpaid line remains: select an actual proper projected core partition with independently paid decrement and certified complete terminals, while arranging the bias hypotheses or funding their violation from genuinely unused original surplus. This stage closes arbitrary point-control interleaving of the signed account, rather than claiming that source/terminal payment follows from it.
