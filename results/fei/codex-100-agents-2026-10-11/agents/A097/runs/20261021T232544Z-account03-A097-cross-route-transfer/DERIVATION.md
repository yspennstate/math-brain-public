# One fresh control exposure from the original active-history bank

All logarithms are base two. This transfers A096-CANONICAL-ACTIVE-RESET-SAME-ANCESTOR@1 into a non-active query. It does not construct a reference for an arbitrary Boolean source. Full FEI remains OPEN.

## 1. Data, references, and the original quota

Let a>=1,b>=0,r>=2 be integers, n=a+b, s=2^-a, t=2^-n, e=2^(1-n-r), mu=1-2s. Let g=1-2A_a on n bits and F=g+2A_(n+r). Indicators A are point events at zero in the indicated physical coordinates. Supply a normalized reference R_raw of finite source cross entropy c_raw<=C0 I(g), C0>=0. Empty-calibrate to R, so R(empty)=mu^2 and c=CE(P_g,R)<=c_raw. Define the complete floor Q by its data marginal

    R_e(T)=(1-e/s)R(T)+(e/s)mu 1_(T=empty)+2et

and the ACTUAL conditional law of the r spectral control coordinates given T. Thus Q(T,U)=R_e(T) P_F(T,U)/M_e(T), with M_e(T)=sum_U P_F(T,U). All M_e are positive here. This is exactly the A097 floor, including every reference-only atom. Its complete cost is at most

    W(a,b,r,R)=c+10e(a+b+r).

The original quota is K I(F), K=2C0+10. Put Ig=2as, E=ea, X=e(b+r). The exact identity is I(F)=Ig+X-E. Since r>=2, E<=Ig/4 and Ig>=4ae. Consequently

    K I(F)-W >= (C0+10)(Ig-2E)+2C0 X
                    >=5Ig>=20ae.                         (1)

This reserve is at the ORIGINAL ancestor. It is neither a price assumption at a child nor a new descendant quota.

## 2. The actual control erasure debit

Query one of the r physical control bits. Pair the parent coefficients (alpha,beta) by absence/presence of this bit. For every remaining control label V, beta=e. For V empty, alpha=g_hat(T)+e; otherwise alpha=e. The nonzero coefficients of g are g_hat(empty)=mu and g_hat(T)=-2s for nonempty T contained in the a active bits.

The elementary inequality ln(1+z^2)<=z for z>=0 follows by integrating 2z/(1+z^2)<=1 from zero. Thus, also by continuity when alpha=0,

    phi(alpha^2,beta^2)<=2|alpha beta|/ln 2.

Directly summing the pairs (all labels, including off-source support) gives

    sum |alpha beta|=e[4-4s+2e-2e/s]<=4e.

The sum formula uses 2^(n+r-1)e=1 and e<=s/2. Since ln2>2/3,

    B_control(F)<=8e/ln2<12e.                             (2)

This is a deliberately coarse erasure bound. It is not a bound on an omitted channel or on a different node's influence.

## 3. Keep the complete off-child reference

The off physical child is g with r-1 dummy controls. Keep Q_old=Q with the queried spectral coordinate marginalized. Its full cost is c_off=CE(P_g tensor delta_empty,Q_old); no atom is reset in this child. For T in the occupied nonempty source spectrum, the actual reference atom on the remaining vacuum controls is

    Q_old(T,empty)=R_e(T) kappa,
    kappa=[(2s-e)^2+e^2]/[4s^2-4se+2te].

Let h=e/s. Here 0<h<=1/2, t<=s, and every denominator is positive. Since

    kappa^-1=1+2e(t-e)/[(2s-e)^2+e^2]<=1+h/2,

we have Q_old(T,empty)>=R(T)(1-h)kappa. At the source vacuum, Q_old(empty,empty)=(mu+e)^2+e^2>=mu^2=R(empty). If a=1 then mu=0, and this atom has zero true source probability; it contributes zero, rather than an undefined logarithm.

The total nonempty source probability is v=1-mu^2=4s(1-s)<=4s. Convexity, using the chord on [0,1/2], gives -log2(1-h)<=2h. Also log2(1+h/2)<=h/(2ln2). Therefore the SIGNED full excess obeys

    c_off-c <=v[-log2(1-h)+log2(kappa^-1)]
             <=(8+2/ln2)e<11e.                           (3)

This bound uses actual likelihoods, not absolute total variation. Extra reference mass outside source support stays present in Q_old and every normalizer remains in the formula.

## 4. Prescribed on-child reset and exact substitution

The on physical child is F_on=1-2A_a+2A_(n+r-1). Reset it to the SAME specified floor built from the SAME current R, with r replaced by r-1 and e replaced by 2e. Its complete envelope is

    W_on=c+20e(a+b+r-1).

For r>=2 the new r-1 is at least one, exactly the A096 hypothesis. Equations (2) and (3), retaining the complete off child, give

    B_control(F)+(c_off+W_on)/2
      <c+10e(a+b+r)+(12+11/2-10)e
      <W+8e.                                            (4)

Now first execute ANY A096-allowed active-only prefix, stopping before its final active boundary. Every off-active branch retains its entire inherited reference; every executed erasure stays booked. At the surviving on-active frontier, let physical reach be rho and its current edit amplitude be e_current. Marginalization followed by source empty calibration is exactly the source-reference update in A096. That theorem proves that replacing the frontier cost by its envelope does not exceed the original W, and rho e_current=e_root. Insert (4) at this frontier. On its control-on branch continue with any A096 active-reset policy, including its explicit final point boundary, at its envelope W_on; on its control-off branch retain Q_old. It follows that

    sum_v reach_v B_v + sum_l reach_l CE(P_l,Q_l)
       <= W_root+8e_root
       <= K I(F_root)-12e_root.                          (5)

The stronger (1) leaves at least (20a_root-8)e_root. Existing active-query release only improves this margin; it is not needed. Independent untouched terminal cost c_h is additive on both sides and is never spent. Any no-reset continuation below an allowed terminal is also paid by the exact complete-reference chain rule.

This is one control exposure after any proper active prefix, with active resets thereafter. It does not assert arbitrary repeated control/dummy interleavings, and does not price channels, integer-code roundings or external gate labels. For the exact structural R=P_g, the previous source bound H(g)<=4I(g) supplies C0=4; hence the SAME ORIGINAL rate18 pays (5).

## 5. Independent reconstruction of the imported active theorem

A096 sections1--3 were reconstructed from the explicit coefficient pairs rather than assuming the new statement. Its active erasure comparison needs a>=2: the nonvacuum difference is -2e(1-4s+e)<=0 and the vacuum-pair transfer moves amplitude from the smaller to the larger coordinate. Its complementary likelihood maximizes an affine ratio at v_max=1-mu^2; the exact lower polynomial is 27/52+(13/16)(h-10/13)^2. This yields the signed bound <18e and source-envelope release >=e. At a=1, the erasure comparison is false and the proof correctly switches to the explicit point spectrum; its signed reset is minus an actual KL. The finite checker here reconstructs these local inequalities and retains all off terminals in its mixed histories. Verdict: HOLDS at the precise stated active-reset scope (independent analytic reconstruction with finite exact validation); no universal-source extension is inferred.

## 6. First unpaid line

The same-original-bank result now includes this one genuinely non-active exposure. The next unpaid line is a repeated or interleaved non-active reset whose cumulative weighted excess must be funded after (5), or a signed non-point source reference without the special point-spectrum likelihood bound. A generic initially influence-priced reference remains full-FEI strength. No dimension-independent universal FEI constant has improved.

## 7. Mixed-order strengthening: every remaining eligible control

The one-control calculation also pays repeated eligible controls. At every active on-step, a drops by one and e doubles; at every control on-step, r drops by one and e doubles. Both halve physical reach. Thus rho e_current=e_root throughout EVERY interleaving of these two query types along the still-edited branch. Every complementary branch retains its full inherited reference and either stops or continues without further resets.

At a>=2 the active step releases at least e_current from W; at a=1 the explicit final point-spectrum rule is paid without increasing W and ends the edited branch. Each control step with r_current>=2 costs at most8e_current beyond W by (4). There are at most r_root-1 such control steps before r_current=1. Consequently, for every such mixed policy and every stopping cut,

    complete erasure-plus-terminal ledger
       <=W_root+8(r_root-1)e_root.

The exact original-ancestor lower bound is stronger than (1):

    K I(F_root)-W_root >=5Ig
       =5a_root 2^(b_root+r_root)e_root.

For all integers r>=2,

    5*2^r-8(r-1)>=12.

At r=2 this is equality. Increasing r to r+1 increases its left side by5*2^r-8>0. Since a>=1 and b>=0, the initial reserve therefore pays ALL these control charges and leaves at least12e_root. All old active/control erasures, inherited complementary costs and the current frontier reference are retained. No source price is assumed at a descendant. This strengthens (5) from one control to arbitrary active/control interleavings up to the specified final active boundary or r=1 boundary, at unchanged original rate2C0+10 (18 structurally).

The universal gap and the NEXT in section6 are sharpened accordingly: the new next query is an actual DUMMY-DATA exposure, or a canonical reset inside a previously retained control-off branch, from the SAME remaining original account. Such a query changes the source-reference marginal rather than merely removing a fresh control; it is not covered by the present likelihood substitution. Generic non-point signed sources remain open.
