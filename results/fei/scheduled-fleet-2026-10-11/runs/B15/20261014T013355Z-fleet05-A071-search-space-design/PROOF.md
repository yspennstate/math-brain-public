# Exact family and certificate interpretation

The gate h is negative on {0,1,2,4,8,16,32,6,17,40}. Binary zero means sign +1. Its matched pairs are (0,4),(1,2),(3,5). Swapping within any pair and permuting the three pairs preserves the gate and acts transitively on its six inputs. For a sign pattern e, its orbit is determined by the number of pairs containing zero, one, and two complemented blocks. There are ten triples of nonnegative counts summing to three. The code verifies the full group of 48 permutations on all64 truth-table inputs, and explicitly partitions all64 sign patterns. No output-sign or affine symmetry beyond this proved action is assumed.

Let g be any Boolean core whose physical coordinates are transitive, with p=P(g=-1), v=4p(1-p), singleton square t and physical influence d. For F_e=h((-1)^e_j g_j), write p_j=p or1-p according to e_j and m_j=1-2p_j. Let b_T be the normalized Fourier coefficients of h under the independent output laws with these means. Put s_T=b_T^2. For each block j define

    q_j = sum_(T containing j) s_T / v,
    M_j = sum_(T not containing j) Phi(s_T, t s_(T+j)/v),
    R_j = M_j - q_j Phi(m_j^2,t).

Here Phi(a,b)=(a+b)log2(a+b)-a log2 a-b log2 b. Exact conditional-section expansion gives, for EVERY physical coordinate i in block j,

    Inf_(j,i)(F_e)=q_j d,
    B_(j,i)(F_e)=q_j B_i(g)+R_j.                         (1)

Nonempty inner Fourier residuals contribute q_j times their child pairs; the empty residual contributes M_j and replaces exactly one inherited empty pair. Complementing a core changes its singleton sign and mean but leaves its squared spectrum and B_i intact. Consequently

    E(F_e)=min_j [ E(g)+R_j/(q_j d) ].                   (2)

This minimum is taken over all six blocks; mixed signs destroy global coordinate transitivity. Within each block every coordinate remains equivalent. The gate's pivotal event has positive probability at all0<p_j<1, so every relevant physical coordinate stays relevant. Direct weighted gate-edge counting independently checks all six q_j in each case.

The actual core is g0=h, g1=h(g0^6), g2=h((-g1)^6), g3=h(g2^6). At every one of these common-sign steps transitivity is preserved by independent inner automorphisms and the transitive outer gate group. The root singleton absolute value equals its influence. The same holds inductively because each outer signed derivative has one sign, so the new singleton absolute value and influence are multiplied by the same q. Seed Walsh/edge counting checks this directly. Thus the rational p,d,t and interval B,H states reconstructed by the helper specify actual finite Boolean circuits on6,36,216,1296 bits; they are not hypothetical spectral vectors. Every target circuit uses six disjoint copies of g3, hence7776 bits.

For entropy, let H_p(h) be the entropy of the normalized biased outer spectrum and rho the core's nonempty normalized squared spectrum. A physical Fourier set uniquely identifies its occupied blocks and each nonempty inner set. Hence, with Q=sum_j q_j,

    H(F_e)=H_p(h)+v Q H(rho)=Q H(g)+C_e,
    C_e=H_p(h)-Q h2(v),
    I(F_e)=Q I(g).                                      (3)

All outputs retain the complete Q H(g). Neither (1) nor the search pays C_e from a restriction-tree influence ledger. Composition levels must not be substituted for physical queries in such a ledger.

Two independent outer coefficient descriptions are used. The search expands h in products of (x_j-p_j), with c0=(1-p_j)u+p_j v and c1=v-u at each step. Its normalized squared coefficient is c_T^2 product_(j in T) p_j(1-p_j). The verifier first computes the uniform sign Walsh coefficients a_U of the actual64-entry gate and uses

    b_T^2 = v^|T| [ sum_(U containing T) a_U product_(j in U without T) m_j ]^2.

The two descriptions match every squared coefficient exactly, on all ten representatives. The same variance v applies to p_j=p and1-p. This reconstructs the signed coherent rows independently of the search transform. The strict upper certificate for a representative needs only one coordinate's ratio upper bound; the verifier recomputes that witness for each orbit and all six coordinates of the best representative to certify its minimum as well.

# Logarithm enclosure

For n>0 write n=2^k r,1<=r<2. Retain its leading129 binary places to bracket r outward by rationals a/b and (a+1)/b, b a power of two; when no bits were discarded both endpoints coincide. The endpoints lie in[1,2]. For either endpoint let z=(r-1)/(r+1),0<=z<=1/3. Evaluate the first48 positive terms of

    ln r=2 sum_(j>=0) z^(2j+1)/(2j+1)

by flooring each at scale2^160. Their accumulated rounding error is at most48 units; the remaining tail is at most 2 z^97/[97(1-z^2)]. Use its exact ceiling for an upper bound. Enclose ln2 by the same formula. Divide positive interval endpoints outward to enclose log2 r at scale2^96, then add the exact integer k. Enclose log2(a/b) by subtracting the integer-log intervals, reversing endpoints. xlog and Phi use exact rational weights with reversed endpoints for negative coefficients. This argument proves an interval, rather than assuming96-bit floating accuracy. No floating output determines a sign, minimum, orbit maximum, or threshold. Arithmetic stops at this fixed precision.

# One flipped block escapes the common-sign rare region

For any actual core oriented so its negative probability is p, complement exactly one block, say block0. The negative gate vertices have Hamming distances0,1,2,3 from this dominant unit vertex with counts1,2,5,2 respectively. Thus the resulting negative probability is

    A_1(p)=(1-p)^6+2p(1-p)^5+5p^2(1-p)^4+2p^3(1-p)^3.

For0<p<=1/16 the minority probability is

    sigma(p)=1-A_1(p)=4p-10p^2+18p^3-19p^4+10p^5-2p^6.

Indeed sigma/p>=4-10/16-19/16^3-2/16^5>3. Also

    sigma/p<=4+p[-10+18p+10p^3]<4,

since18/16+10/16^3<10. Therefore3p<sigma(p)<4p<=1/4, which also justifies that it is the smaller output probability. Repeating this operation with current minority orientation exits p<=1/16 in finitely many steps; each step remaining in that interval multiplies p by more than3. This proves only a bias-escape statement. A080's absorbing-map theorem was explicitly about common signs and remains valid at that scope.

For the finite actual core g3, the exact certificates yield E(g3)>3.3483. The ten checked orbit minima have largest value between3.34828508 and3.34828510, attained by one flipped block, strictly below3.3483. Thus ALL64 sign choices fail to preserve the threshold K=33483/10000. Nevertheless the one-flip minimum is above669/200 and its minority probability is0.0843323290...>1/16. It rescues A080's old threshold while losing a small amount of E. This distinction rules out monotone independent-sign admission on this core without claiming that every relaxed or paid admission mechanism fails.

The exact remaining universal line is an all-dimensional, once-owned payment for the negative terms R_j/(q_j d) and full terminal C_e along an admission/physical-exposure policy. No such payment is proved here. Neither a finite circuit with high E nor bias escape proves unbounded H/I or full FEI.
