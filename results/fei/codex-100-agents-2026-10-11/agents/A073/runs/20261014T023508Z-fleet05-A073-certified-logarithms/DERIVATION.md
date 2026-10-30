# Complete references: independent review and a nonzero-erasure extension

All entropy and KL quantities use base two. All functions below are actual Boolean signs on uniform physical coordinates. Write p_S=hat f(S)^2, e_i=sum_(S contains i)p_S, r_i(T)=p_T+p_(T+i), mu_i(T)=p_(T+i)/e_i, and M_i=e_i[log(1/e_i)-D(mu_i||r_i)]. Rows with e_i=0 are omitted. The reference includes every residual atom, including those outside derivative support.

## Independent reconstruction of A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1

Expand f in characters before making the substitution x_i=u_i v_i for i in J. Distinct characters remain distinct, so p is embedded by replacing each selected i by its pair. Entropy is unchanged and the influence sum increases by sum_J e_i. For an unchanged coordinate the residual pairs are the old pairs with an injective relabeling, preserving M_i and D_i. For a duplicated coordinate u, put A_T=p_T and B_T=p_(T+i). Its lower coefficient support has partner occupancy zero, and its upper support has partner occupancy one. Thus r(T,0)=A_T, r(T,1)=B_T, mu(T,0)=0, mu(T,1)=B_T/e_i. These laws sum to one. The likelihood ratio on positive mu is exactly 1/e_i. Hence D_u=log(1/e_i), M_u=0, and its true conditional erasure B_u is zero because no residual pair has two positive masses. This proves the stated H,I,M transport, without assuming invariance under a general linear change of coordinates.

Deleting only the partner bit restores precisely the original complete residual laws A+B and B/e_i. The weighted KL loss is e_i[log(1/e_i)-D_i]=M_i(f). Retaining only the partner gives complete reference (1-e_i,e_i) and derivative (0,1), preserving all KL. Conditional on partner one, both remaining core laws equal B/e_i. An additional common independent spectator multiplies both laws by the same factor and cancels in every likelihood ratio. Summing over all pairs gives total deletion loss 2M(f) and physical influence 2I(f), hence ratio M(f)/I(f) for nonconstant f. The constants are handled by omitting zero rows; no 0/0 ratio is asserted.

For even d>=2, b(y)=(-1)^(y_1 y_2+...+y_(d-1)y_d) is a product of two-bit signs with Fourier coefficients (+1,+1,+1,-1)/2. Consequently hat b(T)=sigma_T t, t=2^(-d/2). Put delta=t^2 and g(s,y)=b(y)-1_(y=0)+s1_(y=0). Its selector row has A_T=(sigma_T t-delta)^2 and B_T=delta^2. Both signs sigma occur, so the reference partner and core after selector duplication are correlated. Since A+B=delta(1-2sigma_T t+2delta)>=delta/2, the direct formula M_s=sum_T B_T log((A+B)/B_T) gives M_s>=delta(d-1). KL nonnegativity gives M_s<=delta d. Each duplicate has influence delta; its loss from dropping the partner is M_s. A single vertex flip in b adds an edge in each core direction, since b(0)=b(e_j)=1. Averaging the two children of g gives each core influence 1/2+delta. Thus I(G)=d/2+(d+2)delta. Character embedding gives H(G)=H(g)<=d+1, so H/I<=3. This reconstructs every clause of the reviewed claim. No repair is required, and no universal payment follows.

## Nonzero-erasure Boolean boundary family

Instead use the actual two-bit gate q(u,v), equal to -1 only at the 0/1 input (1,1), and define

    F_d(u,v,y)=b(y)+1_(y=0)[q(u,v)-1],     even d>=2.

Thus F=b unless y=0, where it equals q. This changes the mechanism from parity duplication: every spectral atom is now positive, so both queried rows have strictly positive true erasure. The gate coefficients are (1,1,1,-1)/2. For each core Fourier set T, the four amplitudes at (u,v) occupancies 00,10,01,11 are

    sigma_T t-delta/2, delta/2, delta/2, -delta/2.

The signed flat coefficients have counts N_+=(2^d+2^(d/2))/2 and N_-=(2^d-2^(d/2))/2, since their sum is b(0)=1. For query u, e=delta/2 and the complete row is

    r(T,0)=delta c_sigma, c_sigma=1-sigma_T t+delta/2,
    r(T,1)=delta^2/2,
    mu(T,0)=mu(T,1)=delta/2.

Indeed sum_T r(T,0)=1-delta/2 and sum_T r(T,1)=delta/2. Retain only partner occupancy v. The binary laws are mu_V=(1/2,1/2), r_V=(1-e,e). Conditional on v=1, both core laws are uniform (mass delta per set). Conditional on v=0, the derivative core is uniform and the reference core has masses delta c_sigma/(1-delta/2). Therefore, exactly,

    D_full = D_binary + D0/2,
    D0 = sum_(sigma=+,-) N_sigma delta log[(1-delta/2)/c_sigma],
    L_u = e[D_full-D_binary] = e D0/2.

The same holds for query v. The reference never loses its unit normalizer, and conditional KL is evaluated separately in both cells. The two different c_sigma values and positive counts imply D0>0 by strict KL nonnegativity.

There is a uniform rational margin for this remainder. For 0<t<=1/2,

    7(1-t+t^2/2)-5(1-t^2/2)
      =2-7t+6t^2=(2-3t)(1-2t)>=0.

Thus every positive conditional likelihood ratio is at most 7/5. Consequently D0<=log(7/5)<1/2, where the last strict sign is the exact integer comparison 49<50. It follows that

    0<L_u/e<=log(7/5)/2<1/4.

The stronger rational margin 1/4-log(7/5)/2>1/256 is separately checked by the fixed N=12 interval certificate and the exact integer comparison 7^128<2^63*5^128. Both pair remainders together are <delta/4 and can be allocated once to their combined physical influence delta with allowance 1/4. If a dedicated core reserve is desired, their total is also <Inf_(y1)/10: Inf_(y1)=(1+delta)/2, and delta/4<=(1+delta)/20 follows from delta<=1/4. This is only a ledger for this remainder; no other cost is charged to the same reserved fraction.

The complete row's retained price is still large:

    M_u/e = 1+(1/2)log[(1-e)/e]-D0/2
           > d/2+3/4,

because (1-e)/e=2^(d+1)-1>=2^d. Thus bounding the lost conditional remainder does not bound the retained row price by the pair's influence. Each core influence equals 1/2+delta/2: at y=0 the gate differs from b only on one quarter of the (u,v) inputs, adding delta/2 influence in each core direction. Hence I(F_d)=d/2+(d/2+1)delta. The generic bound H(F_d)<=d+2 gives H/I<=2+4/d<=4. This family is not an FEI counterexample.

## Certified logarithms and validation limits

The independent checker uses exact integer Walsh transforms, signed inverse checks, Parseval, physical flip counts, complete row and joint P,Q normalizations, and prime-log coefficient identities. The 104 labeled substitution cases consist of all signs in dimensions one and two with every duplication subset, plus majority, parity, point defect and AND in dimension three with every subset. Three bent-selector cases and three new AND-gate cases use d=2,4,6, making 110 cases, maximum physical dimension eight. This finite validation supplements the analytic proofs above, rather than replacing their quantifiers.

For a positive rational logarithm argument, extract its exact integer power of two so the remaining t is in [1,2). Put z=(t-1)/(t+1). The first N terms of 2 sum_(j>=0)z^(2j+1)/(2j+1) are a lower bound for ln t and the positive tail is at most 2z^(2N+1)/[(2N+1)(1-z^2)]. Divide the resulting nonnegative numerator interval by the positive interval for ln2, then add the exact extracted power. Signed linear forms reverse endpoints for negative coefficients. All displayed decimal endpoints are outward rational rounding. N=12 was fixed before execution; signs were determined without refinement.

## First unsupported universal line

For arbitrary Boolean f, no finite universal K is proved for

    sum_i e_i D(mu_i||r_i) >= sum_i e_i log(1/e_i)-K I(f).

Nor is a universal conditional quotient or a globally available nonoverlapping terminal reserve constructed here. The positive remainder bound uses the explicit signed amplitudes of F_d. It is false to transfer it to arbitrary correlated rows merely because the retained alphabet has size two.
