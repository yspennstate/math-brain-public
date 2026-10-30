# Same owner through the next canonical data query

Use actual F(x,a,b,y)=(-1)^a if x=0, else 2y-1 if b=1, else +1. Frequency masks have physical order x,a,b,y. All entropy/KL is in bits. The root has H=3,I=3/2. Query b. Both children have H=2, with influences 1 and 3/2; hence the certified mean-child surplus at rate four is S=3. Query y next only in the b=1 child. Its query influence is 1/2 and both grandchildren have H=2,I=1. The root-weighted final terminal entropy is 2 and influence 1. Thus the SAME old mean-child surplus obeys the exact conservation identity

    3 = 4*(1/2)*(1/2) + 2 = 1 + S_final.

The first term is the influence consumed by the y query, at root reach 1/2. It is not available terminal surplus. No new bank is admitted.

Let v=15/16, r=(8/15,8/15,4/15,4/15), and c the unique positive solution of 1-c=(1-8c/15)^2(1-4c/15)^2, with 3/4<c<13/16. The complete canonical occupancy reference Q has Q(empty)=1/16 and Q(S)=v product Bernoulli(c r_j)(S_j)/c for nonempty S. Its normalization and uniqueness follow directly as in the source: sum r_j=8/5>1, sum r_j^2=32/45<1, so ln(1-c)-sum ln(1-r_j c) is strictly concave, initially increasing and tends to minus infinity. Rational polynomial signs supply a bracket for its sole positive root.

For any actual query with lower/upper amplitudes A_T,B_T, use physical branch kernel K_±(T)=(A_T±B_T)^2/[2(A_T^2+B_T^2)] on occupied erased rows, and fair fallback otherwise. Erase Q by summing its lower and upper masses; transport this COMPLETE erased reference through the same kernel, then normalize each inherited branch by its actual reference outcome probability. All source-zero/reference-positive atoms are kept.

Write D_b0,D_b1 for complete inherited b-child KL, and D_bar=(D_b0+D_b1)/2. Let C=-(1/2)log2(1-4c/15). The source's initially booked mean-child conditional bill is C, with 1/8<C<3/16. Its mean retained quotient bill is R=D_bar-C>=0. The reference transport explicitly retains this unpaid quotient instead of treating C as payment for the whole reference.

In the b=1 child, four erased residual atoms (x,a masks) are all source-positive, and every y branch kernel is 1/2. Thus both reference outcomes are fair and both inherited y-grandchild laws are the y-erased b=1 reference. Actual grandchildren have uniform spectra on the four x,a masks. On a=0, the incoming reference contains only y=1, matching the source. On a=1, the source has y=0 and the incoming reference has conditional y occupancy tau=4c/15. These a=1 rows have actual weight 1/2. Therefore the y-query source-label erasure KL is EXACTLY C, its outcome KL is zero, and

    D_b1 = C + mean_y D_grandchild.

This follows also from the complete same-kernel KL chain rule, independently checked on every atom. It gives the root-weighted identity

    (1/2)*C + D_final = D_bar,

where D_final=(1/2)D_b0+(1/4)D_grand0+(1/4)D_grand1. Exactly HALF of the earlier booked mean conditional withdrawal moves to the y-query erasure bill; the other half remains in the untouched b=0 terminal. Neither part is charged again. Algebraically D_final=R+C/2. This is a cancellation-safe ownership transfer, not a fresh conditional withdrawal.

The exact checker and its 48-step rational canonical-root interval below certify D_bar<1. The two endpoints of the initial bracket are separate normalized-reference pilot fixtures, not a continuum sign certificate. Thus the same original owner suffices for the full current continuation:

    old S = 1 (consumed influence) + C (already booked)
              + R (newly paid retained quotient) + unused,
    unused = 2-D_bar > 1.

All terminal entropies remain: mean H_final=2 and mean I_final=1. In particular

    mean CE_final + (root-reached y erasure KL)
       = 2 + D_bar < 3 < 4*mean I_final,

where CE_final uses precisely the inherited references, not newly optimized products. The full first-b source-erasure and reference-outcome accounts are not silently included in this local owner: they precede the declared unused mean-child S account and remain separate in a universal history ledger. No earlier A038 a-query bank is spent here.

Independent numerical scope check: a tempting ledger that subtracts only C and then credits a fresh final S=2 would omit the consumed influence or duplicate an existing owner. The checked conservation identity and explicit R eliminate that shortcut. The smallest fixture here has four essential parent coordinates, but no global minimality is claimed.

This closes the requested next y step of the specified A083 canonical fixture, including its previously unpaid retained b-child quotient and the complete current terminal KL. It does not prove a universal policy, an arbitrary non-flat replacement-core bound, or eligibility of the predeclared owner in an earlier history. The first unsupported universal line is the availability and sufficient size of the SAME certified surplus under a general mixed-history non-flat query, together with the preceding source/outcome bills. NEXT must test that inherited complete-reference transaction without creating a new root occupancy bank.

## Compatibility with A050's already booked conservative envelope

A050 stage5 has already continued this same y query with spectator a and retained x. Its exact new conditional cost is C_y=(1/2)log2 V, V=(2-theta)^2/[4(1-theta)], theta=8c/15; its envelope is B_y=2C_y. It books C+C_y from the final2 owner, retaining the earlier C withdrawal in full without recycling any released debt. Its named unpaid continuation is the remaining final quotient.

Our full inherited-reference calculation pays that existing gap with no change to A050's booking: the true unpaid final quotient is J=D_bar-C-C_y/2>0. Keep its conservative booking C+C_y unchanged and add J once. Combined spend is D_bar+C_y/2; the extra C_y/2 is deliberately left as conservative overpayment, never refunded or counted as a new bank. The revised exact canonical interval certifies 2-(D_bar+C_y/2)>173/100. All three full terminal cross-entropies and the earlier reached y-erasure bill remain represented; source-b erasure/outcome precede this owner and are still separate. Thus the stage advances the actual A050 retained-quotient NEXT rather than reopening its already completed conditional pricing. No assumption is made that mean conditional debit equals every individual child's debit.
