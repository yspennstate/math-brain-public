# A coherent a-child query after the first paid correlated reset

Full FEI is OPEN. Entropies and divergences are bits. This refines the SAME-source signed history-payment mechanism of A039's previous stage, using the priced source and actual first reset reconstructed from A036. It closes the a-child interface explicitly excluded by A037. No replacement of an older canonical source is claimed.

## 1. Local normalized reference and exact compensated identity

Let v be a width-w>=2 point defect on a block V, let u be a signed product on disjoint spectator blocks, and g=v u. Each spectator is a point defect, character or constant. Fix epsilon=+1 or -1. The actual Boolean function G is epsilon at x=0 and g at x=1. Write p_v,p_u for the squared spectra. A factor reference q_i matches p_i(empty), is normalized and has the same support. A character/constant uses its matching law. On width>=2 factors the current PAID law is

    q_i(empty)=p_i(empty),
    q_i(T)=(5/6)p_i(T)+(Var(v_i)/6)1[T=full], T nonempty.

The outer lift R copies the actual two zero-data control masses (epsilon +/- mean(g))^2/4 and puts q_v(T_v)q_u(U)/4 on each control mask for nonempty combined data. Its total mass is one because q_v(empty)q_u(empty)=p_v(empty)p_u(empty). Its actual KL is D(p_v p_u ||q_v q_u)/2. References are prescribed independently of a sampled frequency.

Define l(T_v)=q_v(T_v)/p_v(T_v) and s(U)=q_u(U)/p_u(U) where defined. Assign both ratios value 1 on zero/zero rows; in particular s(empty)=1 when a forced spectator character gives p_u(empty)=0. This convention is needed on the extra controller-only atoms. The lift has the exact pointwise identity

    R(c,T_v,U)=P_G(c,T_v,U) l(T_v) s(U).             (1)

On nonempty data this follows from the two Fourier copies of g; on zero data both ratios equal one. No reference-positive/source-zero atom occurs in this local family, although all zero rows keep the fair kernel extension.

Query a coordinate j of v. Erase its frequency bit and call the remaining frequency W=(c,T_v\j,U). The common coherent kernel is k_y(W)=P_(G|j=y)(W)/(2 Pbar(W)), with k_y=1/2 on Pbar=0. Define

    B=P_G l,   b(W)=Bbar(W)/Pbar(W) on positive rows.

B is normalized: the marginal of T_v under G is (delta_empty+p_v)/2 and l(empty)=1, so E_P l=1. Erasure of (1) gives Rbar=s Bbar. Let r_y be the ACTUAL reference outcome probability, obtained by applying k_y to Rbar. Then the normalized inherited child reference is

    R_y^old(W)=P_y(W) s(U) b(W)/(2 r_y).             (2)

This equation retains the outcome normalizer, including its dependence on the spectator reference. It makes no product-kernel assumption at the coherent controller row.

Now reset ONLY the queried factor: on the active width-(w-1)>=2 child use

    q_vy^new(empty)=p_vy(empty),
    q_vy^new(T)=(4/5)p_vy(T)+(Var(v_y)/5)1[T=full].

The inactive constant and width-one character children match exactly. Keep every spectator q_u unchanged. Rebuild the outer lift with the ACTUAL child controller masses; its likelihood is

    R_y^new(W)=P_y(W) s(U) l_y^new(T_v\j).         (3)

Both destinations are normalized because their factor-empty masses match. Subtracting the complete normalized KLs in (2)-(3), averaging with the physical weights 1/2, and using mean_y P_y=Pbar, gives the exact identity

    sigma_node := mean_y [D(P_y||R_y^new)-D(P_y||R_y^old)]
       = (1/2) mean_y D(p_vy||q_vy^new)
         - D(Pbar||Bbar) + D((1/2,1/2)||(r_0,r_1)).     (4)

The spectator KL cancels pointwise, not by discarding it. The first term has an extra 1/2 because the outer selector places only half its frequency law on the core. Formula (4) is the compensated projection-under-restriction identity sought in this packet. The negative erasure term and positive outcome term are both essential for equality.

## 2. Uniform price of that coherent correction

Let beta=5/6. Since q_v>=beta p_v, (1) implies R>=beta C where C=P_G s. C is the lift with the queried factor's ACTUAL spectrum and the SAME spectator reference. The common kernel maps C to outcomes of probability EXACTLY 1/2: for U!=empty the spectator likelihood s cancels out of the coherent quotient and is unchanged, while for U=empty it equals one. The resulting child is exactly the normalized lift of p_vy q_u. This remains true for forced characters and zero-bias cores. Therefore

    beta/2 <= r_y <= 1-beta/2,
    D(fair||r)=-log2(4r_0 r_1)/2 <= log2(36/35)/2.      (5)

Only the active point child can have nonzero new factor KL. It is <=log2(5/4) Var(v_active)<=log2(5/4). Drop ONLY the nonnegative erasure term in (4). Thus

    sigma_node <= log2(5/4)/4 + log2(36/35)/2 <1/8.     (6)

The strict rational log certificates are 5^3<2*4^3 and 36^12<2*35^12, giving respectively log2(5/4)<1/3 and log2(36/35)<1/12. This is a signed new-minus-old reset bound, not a claim that each child's KL decreases. No spectator factor is repriced.

## 3. Same original source and first actual reset

For all m>=1,r>=2 let h be a product of m disjoint width-r point defects, delta=2^-r, t=Pr(h=-1), and F_h be chi_a at x=0, h at x=b=1 and +1 otherwise. The ORIGINAL source Q0 is the correlated sector lift of the product factor laws

    q_i^0(empty)=p_i(empty),
    q_i^0(T)=(7/8)p_i(T)+(Var(v_i)/8)1[T=full].

It copies all six actual zero-data/control masses and puts q_h(T)/16 on each of four control masks at nonempty data. This initial source is not the canonical occupancy law of A039's preceding biased-core stage. A conversion from that law would require its own debit.

Here is a reconstruction of the exact source certificate, so an unreviewed peer theorem is not silently assumed. A width-r point factor has p(empty)=(1-2delta)^2, p(T)=4delta^2 otherwise, variance 4delta(1-delta), influence 2r delta and nonempty entropy 8(r-1)delta(1-delta). The empty contribution is <=Var/ln2<3Var/2. Since log2(8/7)<1/5 (8^5<2*7^5), its initial cross-entropy is <(8r-6/5)delta(1-delta)<4I_i-6delta/5. Tensor addition and the disjoint control sectors give

    A0=D(P_F||Q0)=D(p_h||q_h^0)/4,
    M0=4I(F)-H(F)-A0>1+2t+3m delta/10.               (7)

Indeed I(F)=1+t/2+I(h)/4 and H(F)<=3+H(h)/4 by erasing b from its constant/core selector and bounding the label entropy by one. These bounds use actual spectra, not general FEI.

Query b, retain b0, and in b1 perform any finite adaptive fresh-data prefix, leaving x,a unqueried. At any selected prefix leaves query a and retain BOTH outcomes. ACTUALLY reset both a-child laws to the lift in section1, using 5/6 factor references (exact laws on characters/constants). Do not pretend this first conversion is delayed until the second query. Let sigma1 be its complete physically weighted new-minus-old KL. Dropping only the old KL at these first-reset nodes, and using conditional variance contraction separately for each original factor along the SAME adaptive data history, gives

    sigma1 <= (log2(6/5)/4) sum_i Var(v_i)
           <11m delta/40,                           (8)
    M0-sigma1>1+2t+m delta/40>1.

The log certificate is 6^40<2^11*5^40. The factors 1/2 for b1 and 1/2 for the complete a-pair fresh lift are both retained. Formula (8) reconstructs A036's first exercised reset with its exact initial source and sharper margin.

## 4. One post-reset data query on the coherent a children

At any subset of those ALREADY RESET a children, choose one surviving width-w>=2 point factor and query one fresh coordinate. Retain both outcomes and exercise the factor-only 4/5 reset of section1, keeping all spectator references at their PAID 5/6 laws. There is at most one such query per reached a child in this theorem. Leave every other terminal/reference untouched. The eligible a-child reaches sum to at most 1/2, independently of the adaptive prefix and subset choices. Equation (6) gives the complete second signed conversion

    sigma2 <1/16                                           (9)

(or sigma2=0 when there is no second query). This pays an actual new factor reference after a physical coherent restriction; it is not a commuting return to the original projected source.

Keep a prior genuine booking 0<=omega<=1/4. Let Hf,If be the COMPLETE final physical means, e=H(F)-Hf-4(I(F)-If), S=4If-Hf. Exact common-kernel telescoping, including both actual reset insertions and both final terminal references, gives

    A0+sigma1+sigma2 = cumulative erasure KL
                       + cumulative outcome KL + final inherited KL.

The signed recovery identity is purely algebraic:

    S-[A0+e+sigma1+sigma2]_+
        =min(S,M0-sigma1-sigma2).                         (10)

This uses each original query allowance only once, through e; no bank, first reset or old booking is renewed.

It remains to certify the actual S, rather than assume affordability. All restrictions of the disjoint point core obey H<=4I, by the elementary point spectrum above and tensor additivity. For an a-child G_epsilon(g), H(G)<=2+H(g)/2 and I(G)=Pr(g!=epsilon)+I(g)/2. Thus S(G)>=-2 epsilon E g + (4I(g)-H(g))/2. Under any complete fresh-data history within that child the mean E g remains its original mean. Averaging BOTH a outcomes cancels the signed bias term, even if their queried coordinates or stopping choices differ. Therefore the complete a-pair contributes nonnegative surplus; unselected pre-a selector leaves have surplus>=2. The untouched b0 terminal contributes exactly1 globally. Hence S>=1 after the second data queries as well. This argument does NOT demand nonnegative surplus of every individual a-child.

Combining (7)-(10) and omega<=1/4 proves

    S-[A0+e+sigma1+sigma2]_+-omega >11/16 bits.            (11)

The old quarter is still charged once after the same signed transaction. The positive reset allowance is at most1/16 globally, while the first reset and every full terminal KL remain charged to the same original owner. The result is all-m, all-r and all stated adaptive-prefix/subset/coordinate policies; finite tests below do not establish these infinite quantifiers.

## 5. Scope, adversarial audit, and first unsupported line

The exact new step is (4), replacing the product-kernel cancellation which is unavailable on coherent a children. Outcome-normalizer omission would incorrectly replace its last term by zero; signs and forced-character spectators are explicit boundary tests. Replacing ALL spectator factors would invalidate (4)'s pointwise cancellation and is outside the theorem (A037 gives an actual many-factor obstruction to a constant second-price bound under that change). Taking an older canonical source as already paid is also excluded.

This is a refinement/validation of the existing signed-source history mechanism, not a new broad FEI candidate. Independent external acceptance is pending. First unsupported universal line: supply a comparably priced correlated INITIAL reference for an arbitrary Boolean core, or iterate descendant reference changes after eligibility/empty calibration is altered without reissuing any original source/query credit. The local identity suggests a next test with a second queried factor or a second change of the already changed factor, retaining its new beta=4/5 and both earlier conversions. No universal FEI constant improves.
