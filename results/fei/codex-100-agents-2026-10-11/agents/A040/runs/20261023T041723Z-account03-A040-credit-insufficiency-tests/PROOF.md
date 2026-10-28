# A fixed spectator survives an arbitrary coherent factor stopping tree

All logarithms are base two. All physical inputs are independent uniform bits. Full FEI is OPEN. This is an analytic local transport lemma, followed by a specified same-source application; neither provides an arbitrary-core initial price.

## 1. Local statement and hypotheses

Let V,U be disjoint variable blocks, v(V),u(U) Boolean signs, epsilon a fixed sign, and G(x,V,U)=epsilon on x=0, v(V)u(U) on x=1. Write p_v,p_u for their squared spectra. Let q_v,q_u be normalized references with the SAME support and empty mass as p_v,p_u respectively. On zero/zero rows assign likelihood one, including the empty row. Write l=q_v/p_v and s=q_u/p_u. The initial complete coherent lift is R=P_G*l*s. Define B=P_G*l. Both are normalized because the V marginal is (delta_empty+p_v)/2 and l(empty)=1; similarly for U. There are no unpriced conversions into these references.

Run ANY finite adaptive physical stopping tree querying only coordinates of V, with no reset inside the tree. At every query, erase the queried frequency, use the actual common physical kernel k_y=P_child_y/(2 P_erased), use fair fallback on zero-source rows, and normalize each reference by its OWN outcome probability. Denote terminal inherited laws by B_h,R_h, with physical reaches pi_h. These references can have different outcome probabilities from the physical fair outcomes. All leaves, including constants, are retained.

At any subset of terminal leaves, replace R_h by the normalized lift N_h=P_h*s*l_h^new, where q_h^new matches the actual restricted v_h's empty mass and support. The spectator law is unchanged. The exact signed local reset cost on those leaves is

    sigma = sum_selected pi_h [D(P_h||N_h)-D(P_h||R_h)]
          = sum_selected pi_h [D(p_vh||q_h^new)/2-D(P_h||B_h)].       (1)

This identity applies to arbitrary v,u under the stated support and factor-separation hypotheses. It does not say that B_h has the physical spectator marginal.

## 2. Spectator sector invariance: proof of (1)

For U-frequency J nonempty, the two x-control copies of the actual spectrum each have mass p_v(T)p_u(J)/4. The coherent query kernel on such rows is independent of J wherever p_u(J)>0. On source-zero rows the same fair extension is independent of J. Therefore, if a reference has nonempty-J rows b(c,T)*p_u(J), transport preserves that form, with a new b independent of J. On J=empty the form can differ because of the constant controller term.

Initially B has precisely this form; R replaces p_u(J) by q_u(J) on nonempty J and agrees with B at J=empty, since s(empty)=1. As sum_nonempty q_u=sum_nonempty p_u, the UNNORMALIZED outcome masses of R and B agree exactly. Dividing by their equal own normalizers preserves

    R_h(c,T,J)=B_h(c,T,J)*s(J)                            (2)

at every history, by finite induction. This argument works when p_u(empty)=0 (forced characters): controller-only atoms still have likelihood one. It also handles constant v restrictions, irrelevant queries and zero coefficient rows. Same-support at entry excludes reference-only spectator sectors from the theorem; no general claim about those sectors is hidden here.

For every actual terminal selector, its U-frequency marginal is (delta_empty+p_u)/2. Thus

    E_P_h[-log s]=D(p_u||q_u)/2,
    D(P_h||R_h)=D(P_h||B_h)+D(p_u||q_u)/2.               (3)

The fresh lift likewise has KL [D(p_vh||q_h^new)+D(p_u||q_u)]/2. Subtracting proves (1). It retains the entire spectator KL in both terms before cancellation; it does not delete a terminal cost. Reference normalizers and their cumulative outcome KL are already present in B_h. In particular their positive corrections cannot be repeatedly charged as if independent: their complete contribution here is the nonnegative terminal D(P_h||B_h).

An initially attempted stronger auxiliary assertion that B_h has the physical spectator marginal is FALSE. Exact pilot witness is retained in out/PILOT.json and out/VALIDATION_REPAIRS.json. Proportionality of its nonempty sector, not equality of marginals, is what proves equal outcome normalizers. Equation (3) averages the spectator log under P_h, not under B_h.

## 3. Point factor: arbitrary stopping costs the same bound as one query

Suppose v is a signed width-w>=2 point defect. At a selected terminal use the matched-empty law q_new=(4/5)p+(Var(v_h)/5)delta_full on the nonempty sector. Constants and width-one characters use their exact law. Hence

    D(p_vh||q_h^new)<=Var(v_h)*log(5/4).

Finite total variance for the physical stopping partition gives sum_h pi_h Var(v_h)<=Var(v). A subset costs no more, since these variances are nonnegative. Equation (1), dropping ONLY the nonnegative inherited B_h KL, gives

    sigma <= (Var(v)/2)*log(5/4)
          <= (3/8)*log(5/4) < 1/8.                     (4)

Here Var(point_w)=4*2^-w*(1-2^-w)<=3/4 for w>=2, and 5^3<2*4^3 proves log(5/4)<1/3 exactly. Strictness does not depend on a finite search. A zero-length tree is allowed and can have a strictly positive actual reset. For a constant/character chosen initially no new tilted reset is made. Choosing the one surviving point factor separately at each reached entry history is permitted; querying a DIFFERENT spectator afterwards is excluded from this lemma.

## 4. Same original paid source and paired surplus

Use the priority family F_h(x,a,b,z)=chi_a on x=0, h(z) on x=b=1, and +1 otherwise, where h is a tensor of m>=1 disjoint width-r>=2 point signs. Put delta=2^-r and t=Pr(h=-1). Its ORIGINAL source is the A036/A039 seven-eighths correlated lift: each core factor has matched-empty q0=(7/8)p+(Var/8)delta_full on nonempty frequencies, and the complete F reference copies the actual six controller atoms and its four nonempty-data copies have q_h/16. A0=D(P_F||Q0)=D(p_h||q0_h)/4.

For completeness, the root certificate is elementary. Point nonempty entropy is 8(r-1)delta(1-delta), empty entropy is <3 Var/2 since ln2>2/3, and root factor KL<=Var*log(8/7)<Var/5, since 8^5<2*7^5. Thus CE(point,q0)<4I(point)-6delta/5. The sector entropy bound H(F)<=3+H(h)/4 and physical I(F)=1+t/2+I(h)/4 imply

    M0=4I(F)-CE(P_F,Q0)>1+2t+3m delta/10.              (5)

Query b and keep b0. In b1 use any finite adaptive DATA-only prefix. At any selected active leaves expose a, keep BOTH physical outcomes, and ACTUALLY reset both complete coherent child references to the matched-empty five-sixths tensor lifts. Keep all complementary leaves inherited. This is the first paid reset, not a conversion postponed until after the next queries. By finite conditional variance for EACH original factor, its complete signed bill sigma1 is bounded by its new full KL:

    sigma1 <= (log(6/5)/4)*sum_j Var(H_j)
           <11m delta/40,
    M0-sigma1>1+2t+m delta/40>1,                      (6)

using the exact sign 6^40<2^11*5^40. Both the b reach and the coherent half-KL are included. This reconstructs the needed A039 supplier instead of accepting every source clause uninspected.

In any subset of those ACTUALLY RESET a children choose ONE surviving width>=2 point factor. Run an arbitrary finite adaptive stopping tree inside that one factor, preserving all spectator references and making no intermediate reset. At selected terminal leaves make the four-fifths factor-only reset of section 3. Different a children may choose different factors, query orders, depths, stopping choices or subsets. Their entry reaches sum to at most 1/2. Consequently their total complete second bill is

    sigma2<1/16.                                      (7)

This is the SAME 1/16 global upper bound A039 proved for one query. Its scope now includes unbounded factor width and arbitrary finite stopping inside the chosen factor; it is not a larger allowed bank.

All conditional core signs remain tensors of points, constants and characters and obey H<=4I by the explicit point spectrum and tensor additivity. For an a-child G_epsilon(g), H(G)<=2+H(g)/2 and I(G)=Pr(g!=epsilon)+I(g)/2. Thus 4I(G)-H(G)>=-2 epsilon E g+(4I(g)-H(g))/2. In each complete data stopping tree E_h E[g|h]=E g, even when stopping rules differ between the two a children. Their signed bias terms cancel on averaging BOTH a outcomes. Hence their pair has nonnegative mean surplus. Unselected pre-a selectors have surplus>=2, and b0 contributes exactly one globally. Thus the COMPLETE final S=E(4I-H)>=1.

With e=H0-EHleaf-4(I0-EIleaf), exact algebra retains the original signed account:

    S-[A0+e+sigma1+sigma2]_+
      =min(S,M0-sigma1-sigma2).

For any actually supplied old booking 0<=omega<=1/4 against this SAME original account, (5)-(7) give

    S-[A0+e+sigma1+sigma2]_+-omega > 11/16.             (8)

Full original KL, the first reset, second reset, all physical query credits, the old quarter and every terminal entropy/reference remain charged. No allowance or variance is renewed. The theorem is analytic; the finite checks below corroborate its mechanism, not its infinite quantifiers.

## 5. Review scope, obstruction and next unpaid line

The complete A039-COHERENT-A-CHILD-FACTOR-RESET@1 statement is independently reconstructed without a repair to its statement. Its positive outcome term remains correct; section 2 supplies an additional invariant which absorbs it into a nonnegative complete comparison KL across many queries. A039 is not credited with this extension or with checking it independently. A046's prescribed one-shot fresh-tilt theorem is only consulted; it is not a dependency or a source renewed here.

The first unsupported universal line is still a priced useful correlated INITIAL source for an arbitrary Boolean core. The local identity is arbitrary-core, but bounding its terminal queried-block price is not automatic. A completed factor reset restores a full matched-empty product lift, so a new block can then be relabelled as queried block; this observation does NOT pay the sum of repeated reset bills. More critically, querying a spectator block BEFORE the first block's final reset destroys the fixed-spectator hypothesis in section 2. NEXT is to price that actual interposed second-block query and final reset with the SAME diminished owner, both earlier conversions and full paired terminals, or consume an independently supplied arbitrary-core price. This directly tests history composition rather than repeating a tensor H/I estimate. No universal FEI constant improves.
