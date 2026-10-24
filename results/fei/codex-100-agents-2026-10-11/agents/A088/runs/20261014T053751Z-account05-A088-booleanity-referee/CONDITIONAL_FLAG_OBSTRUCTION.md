# Conditional-flag refund: an exact local payment obstruction

This tests A067 stage5 NEXT (conditional tail-flag prior after one physical core query). It reuses the bent point-attachment mechanism appearing in A066's earlier collision/lost-KL tests, but prices the complete remaining conditional flag entropy, not a discarded quotient KL. This is a new narrow scope diagnostic, not a new FEI counterfamily.

For each integer m>=2, let Y be 2m uniform 0/1 core coordinates, w one further core coordinate, and z a sign control. Define

    b_m(Y)=(-1)^(sum_{j=1}^m Y_(2j-1)Y_(2j)),
    G_m(w,Y,z)=b_m(Y)+1{w=0,Y=0}(z-1).

These are actual Boolean signs. G_m is reachable after one physical core query: start with

    P_m(c,w,Y,z)=(-1)^(c*w+sum_j Y_(2j-1)Y_(2j))
                   +1{c=w=0,Y=0}(z-1),

and restrict c=0. Parent dimension2m+3, child dimension2m+2. Neither arbitrary real phases nor a stochastic posterior is substituted for the physical restriction. G_m is a two-controller four-branch output using complementary indicators p=1{z=+},q=1{z=-}, with two actual accessible cores b_m and b_m-2*1{w=0,Y=0}.

Let T be the core Fourier label and V=1{the control z occurs in the Fourier set}. Put delta=2^(-(2m+1)), A=2^-m. Fourier coefficients in each row are

    u_T=1{w notin T}*sigma_(T_Y)*A-delta,
    v_T=delta,
    q_T=u_T^2+delta^2,

where sigma is the actual quadratic bent Fourier sign. Thus alpha=P(V=1)=delta and I_z(G_m)=delta. The current reference's global flag cost is h2(delta). Replacing its flag prior by the actual conditional law given T refunds exactly I(T;V), leaving

The bent Fourier assertion here is self-contained: the single pair sign (-1)^(Y1*Y2) has Walsh coefficients(1/2,1/2,1/2,-1/2); tensoring m disjoint pairs gives coefficient magnitude2^-m on every Y label. The one-point indicator contributes delta to every core label. No unproved phase realizability premise is used.

    L_cond=H(V|T)=sum_T q_T h2(delta^2/q_T).

This is an exact normalized-law identity; no log term or terminal core law disappears. It is also the entire spectral erasure of singleton control z.

There are2^(2m) rows with w in T. For them u=-delta, q=2delta^2 and the conditional flag is fair. Their total contribution to L_cond is delta.

There are2^(2m) rows with w notin T. For m>=2, delta/A=2^(-(m+1))<=1/8, so

    q_T >=(A-delta)^2 >=(7/8)^2 A^2 > A^2/2
          =delta^2*2^(2m+1).

Since h2(t)>=t log2(1/t), their total contribution is at least

    2^(2m)*delta^2*(2m+1)=delta*(2m+1)/2.

Consequently

    H(V|T)/I_z(G_m) >= m+3/2 -> infinity.

The improvement from a global to a conditional flag prior is real and exactly measurable, but does not give a universal local price K I_z after the first core query. Even the full conditional flag entropy, with its actual informative dummy occupancy retained, still has unbounded query-influence ratio. This does not preclude weighted selection, signed core surplus payment, or a common tree bank.

The function's total influence is

    I(G_m)=m+(2m+2)delta.

Indeed each Y coordinate has original influence1/2. At the edited all-zero core vertex every original Y edge is nonpivotal; editing at z=- adds delta to each of2m influences. The new w and z influences are each delta. The Fourier alphabet has2^(2m+2) labels, so H(G_m)<=2m+2 and

    H(G_m)/I(G_m)<= (2m+2)/m<=3.

Both actual core entropies remain in the physical restriction ledger. Their averaged influence is m+(2m+1)delta; their entropy is not claimed free. Thus this is an honest obstruction to the isolated conditional-flag query price, not an FEI disproof and not a refutation of A067's2I_X access reserve.

The first unsupported stronger step is charging L_cond to unused certified child slack or an exclusively owned remaining core/control bank. Replacing h2(alpha) by H(V|T) without that owner does not solve same-C induction. NEXT must retain this exact post-exposure family as a guard while proving a selected/weighted signed surplus payment.
