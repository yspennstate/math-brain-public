# Coherent literal-face certificates for prime56067

Use natural corrected entropy E=(ln2)Hplus, v_i=4p_i(1-p_i), c_S=fhat(S)/sqrt(v_S), h(t)=t^2 ln(1/t^2), h(0)=0, and D=I-Var. Physical inputs are independent. No quotient is assigned at D=0.

## 1. Retain combined coefficients before endpoint normalization

The sign gate positive on A={a=b=z=1}, B={a=0,c=z=1}, C={b=c=0} is mask56067. Write x=1-b, y=1-c. Its exact Boolean polynomial is

    f=-1+2z+2xy-2z[ax+(1-a)y].                         (1)

Let P(a=1)=alpha, P(z=1)=q, P(x=1)=e, P(y=1)=d, with alpha,q fixed in (0,1). Put u=4alpha(1-alpha), w=4q(1-q), v_x=4e(1-e), v_y=4d(1-d). The nonempty normalized coefficients in these reflected coordinates are

    c_a=q(d-e), c_x=d-q alpha, c_y=e-q(1-alpha),
    c_z=1-alpha e-(1-alpha)d,
    c_ax=-q/2, c_ay=q/2, c_az=(d-e)/2, c_xy=1/2,
    c_xz=-alpha/2, c_yz=-(1-alpha)/2,
    c_axz=-1/4, c_ayz=1/4,                              (2)

with all omitted nonempty coefficients zero. These are mixed differences of (1), not separately squared conjunction coefficients. Reflection preserves squared spectra and corrected entropy. The checker compares (2) to direct expectations on the actual reflected truth table.

Define

    L_e=4alpha q(2-alpha-q),
    L_d=4(1-alpha)q(1+alpha-q).

Counting degrees in (2) gives the exact identity

    D=L_e e(1-e)+L_d d(1-d)
       +(u w/4)(d-e)^2+4ed(1-e)(1-d).                 (3)

In particular L_e,L_d>0 and D=L_e e+L_d d+O((e+d)^2).

For completeness the entire natural entropy, before any asymptotic bound, is

    E=u h(q(d-e))+v_x h(d-q alpha)+v_y h(e-q(1-alpha))
      +w h(1-alpha e-(1-alpha)d)
      +u(v_x+v_y)h(q/2)+u w h((d-e)/2)+v_x v_y h(1/2)
      +v_x w h(alpha/2)+v_y w h((1-alpha)/2)
      +u w(v_x+v_y)h(1/4).                             (4)

## 2. Two independent rare rates and the sharp face envelope

Taylor expansion of the nonzero baseline coefficients in (4), writing the zero-baseline h terms explicitly, proves uniformly over all relative rates e,d tending to zero

    E=K_e e+K_d d+O_alpha,q(delta^2 ln(1/delta)),
    delta=max(e,d),                                    (5)

where

    K_e=2w alpha+4h(q alpha)+4u h(q/2)+4w h(alpha/2)
          +(u w/4)ln16,
    K_d=K_e with alpha replaced by 1-alpha.             (6)

The constants are uniform when (alpha,q) ranges over a compact subset of (0,1)^2. To justify the remainder without hidden division by d-e: the first and sixth terms of (4) are bounded by C delta^2 ln(1/delta), including when d=e; the v_x v_y term is O(delta^2). All other h arguments have a nonzero limiting absolute value, except the z coefficient which tends to 1 where h is smooth. Taylor's theorem gives their O(delta^2) errors. Thus (5) is valid without any lower bound on e/d or d/e.

Expanding the logarithms in (6) and using u=4alpha(1-alpha), w=4q(1-q) gives

    R(alpha,q):=K_e/L_e
      =ln4+2[(1-q)+q ln(1/q)+alpha ln(1/alpha)]/(2-alpha-q).
                                                               (7)

Hence, with theta=L_e e/(L_e e+L_d d),

    Hplus/D = [theta R(alpha,q)+(1-theta)R(1-alpha,q)]/ln2
                 +O_alpha,q(delta ln(1/delta)).        (8)

The cluster set for unrestricted relative rates is exactly the closed interval between these two tangent ratios; any theta in [0,1] is attained as a limit by a suitable positive e/d path. For oscillating theta, only the corresponding cluster limits are asserted.

The elementary inequality t ln(1/t)<=1-t proves

    2(2-alpha-q)-[(1-q)+q ln(1/q)+alpha ln(1/alpha)]
      =2(1-alpha)+(1-q)-alpha ln(1/alpha)-q ln(1/q)>0.

Thus R(alpha,q)<4+ln4 for every fixed interior alpha,q. The same holds for R(1-alpha,q). Therefore every such two-rate approach has limsup Hplus/D<2+4/ln2. More quantitatively, fixing alpha,q yields a positive gap in both tangent ratios; (8) then proves the corrected Cstar inequality in a sufficiently small entire (e,d) collar. This collar can be chosen uniformly over compact interior alpha,q domains. No explicit uniform collar radius at the boundary alpha=0,1 or q=0,1 is claimed.

The supremum of the face tangent envelope as alpha,q vary is precisely 4+ln4 in natural units. Indeed, put alpha=1-t^2, q=1-t. In (7) the ratio of the bracket to 2-alpha-q tends to 2. Thus the envelope bound is sharp even though each fixed-interior face tangent is strictly smaller.

## 3. Actual joint endpoint path, without exchanging limits

For the same genuine prime use

    p_a=1-t^2, p_b=1-t^6, p_c=1-t^8, p_z=1-t,
    0<t<1.                                            (9)

This is not justified by substituting into the nonuniform remainder in (5). Instead substitute directly into the exact coefficients (2)-(4). Equation (3) gives

    D=4t^7+O(t^8).

The only entropy terms of order t^7 are the x singleton, the z singleton, and the xz pair. Their leading contributions are respectively 8t^7, 8t^7, and 4ln4 t^7. Every other term is O(t^8 ln(1/t)) or smaller, from its explicit variance and amplitude orders. In detail: u=O(t^2), w=O(t), v_x=O(t^6), v_y=O(t^8); c_a,c_az=O(t^6); c_y=O(t^2); all other nonzero coefficients either approach a nonzero constant or have the orders in (2). For c_x=-1+t+O(t^2), h(c_x)=2t+O(t^2); for c_z=1-t^6+O(t^8), h(c_z)=2t^6+O(t^8). Therefore

    E=(16+8ln2)t^7+O(t^8 ln(1/t)),
    Hplus/D -> 2+4/ln2.                               (10)

This proves a sharp Cstar lower endpoint for this prime, not its all-bias upper bound. At the contracted deterministic corner both entropy and deficit are zero.

## 4. Independent scoped review of A044's obstruction and sharp slice

Source A044-SHARED-GUARD-CANCELLATION-OBSTRUCTION@1, hash 7d78ab7cf325ab80263b94a66f6ac63f38d885de9a60e8fce6bebee46403a120. Reconstruct the original three exclusive events, physical derivatives and combined moments independently. For any pair of exclusive indicators A,B, the deficit cross contribution is

    2 sum_i v_i E[D_i A D_i B] +8P(A)P(B),

where D_i A means the half-difference of the associated sign 2*1_A-1. In A/B only the opposing a derivative overlaps; its product has expectation -p_b p_c q, giving -2u p_b p_c q+8alpha(1-alpha)p_b p_c q^2=-2u p_b p_c q(1-q). For A/C only the opposing b derivative overlaps; its contribution -2v_b alpha q(1-p_c) cancels exactly with 8P(A)P(C). The B/C pair cancels in the same way using c. Thus the all-bias source loss L=2u p_b p_c q(1-q) is correct.

At alpha=q=1/2 and e=d, (2)-(4) give the source's exact spectrum, D=2re(1+2re), L=r^2/2, and

    E=r^2 ln(1/r^2)+8re h(1/4-e)+(3/2)re ln16+4r^2e^2 ln4,
    r=1-e.

For e<=1/2, |1/4-e|<=1/4 and h is increasing on [0,1/4]. The logarithm inequality bounds the first term by 2re; hence E<=(1+ln16)D with sharp endpoint limit 1+ln16. Also E_ge2=(3/2)re ln16+4r^2e^2 ln4<=3ln2 D. For e<=1/4, L/D=r/[4e(1+2re)]>=1/(8e). The universal retained singleton slack is between zero and 4D, so it cannot pay this separately charged L by any constant multiple. These are independently reconstructed complete mathematical portions of the source's narrow claim. All ten proper block row tests and essentiality are checked locally. Verdict HOLDS; no repair supplied. The source's own A043 review record is not independently accepted here.

## 5. Honest frontier

For arbitrary alpha,q,e,d, equations (3)-(4) are exact, but no global constant bound of E by D is proved here. The missing line is a coherent full-spectrum payment at general biases, including joint endpoint regimes outside (9) and interior parameters away from literal-face collars. The separate positive shared-guard debit is ruled out; its failure must not be reintroduced as a fundable singleton-slack cost. The current result supplies the correct two-rate boundary values and sharp test paths for a signed quadratic reference.
