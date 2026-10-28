# The returning rare query has a paid owner

All entropies are in bits. Fix even m>=4, delta=2^-m, activation width t>=0 and p=2^-t. The seed is b(y)=(-1)^(y0*y1+...+y_(m-2)*y_(m-1)). On independent x,z and the original two fair controller bits, take g0=zb, g1=zb flipped only at x=0,y=0, and g2=zb flipped only at x=0,y=e0. Original label probabilities remain (1/2,1/4,1/4). Common activation makes every output +1 off its fresh point event.

Query x, then y0 only at x=0, then y1 in BOTH resulting y0 children. Stop by resolving the two controller bits, leaving actual conditioned cores as terminals. The five data-history leaves have reaches 1/2 and four copies of 1/8. This extension consumes A025's returning rare-query obstruction rather than repeating its already paid second query.

Write D_i=H(f)-[H(f_i=0)+H(f_i=1)]/2 and d_i=Inf_i(f). At a data history define the SAME bank R=2 sum_(j<k) pi_j pi_k I(g_j g_k), including activation. No reference, label law or source bank is changed.

## Independent reconstruction of the inherited facts

For one-bit spectral rows, D=B+JS, B<=h2(d), JS<=2c d with c=log2(e). The erasure bound follows by concavity of binary entropy applied to paired Fourier masses. The Jensen bound is the scalar two-amplitude entropy inequality, summed by Parseval. Since z remains unqueried, every unactivated core and actual node is balanced. Thus balanced activation gives H=p H_unact+A(t), I=p(I_unact+t), A(t)<=p(4t+2c), and scales every data decrement and data pivot mass by p. At t=0, A(0)=0. In particular apply h2 to UNACTIVATED d, rather than introducing a spurious t into its logarithm.

At x, d_unact=delta/2. Since h2(q)<=q log2(e/q), its positive rate10 excess Ux satisfies Ux<=p m delta/2. At y0 in x=0, d_unact=1/2+delta, so D<5d and there is no positive rate10 excess. Direct edge counts give the post-y0 aggregate bank R2=p(3m-3+3t)delta/4. The originally booked pre-y0 bank is Rold=p(3m-1+3t)delta/4. These reproduce the specific inherited A021/A025 clauses used below, not their unrestricted history claims.

For completeness, at a data edge let Pj be the pivotal indicator of original core j and q=sum pi_j Pj. Bank contraction releases 2 E[q(1-q)] in that coordinate: product pivotal indicators are Pj XOR Pk and 2 sum pi_j pi_k(Pj XOR Pk)=2q(1-q). Ordinary influence telescoping on each product proves that no other coordinate capacity is released. At y0 the one exceptional edge has q=1/2, giving conditional release p delta. The x release is 3p delta/4. All bank quantities here and below retain the activation capacity 3pt delta/4.

## The new query and the opposite sibling

At x=0,y0=0, y1 is a dummy of the seed. Only one label, probability1/4, changes at its exceptional edge. Thus d0=p delta, and release0=3p delta/2. Its unactivated decrement has

    D0 <= delta (m+3c),
    Uy := (1/4) max(D0_activated-10p delta,0) <= p m delta/4.

The factor1/4 is its ORIGINAL physical reach. This is an upper bound on the new debit, not a claim of local K-goodness; A025's erasure lower bound B/d>=3/2+m/4 still holds. The logarithm is m because the conditional unactivated pivot mass is delta, even though the remaining edit density itself has increased under restriction.

At x=0,y0=1, the seed depends linearly on y1. The exceptional edited edge removes, rather than creates, pivotality, so d1=p(1-delta). Since delta<=1/16, B<=1 and JS<=2c d give

    D1/d1 <=16/15+2c <5.

This opposite sibling incurs no new rate10 debit. Its exceptional label still has probability1/4, hence release1=3p delta/2. Together these give the exact aggregate remaining bank

    R3 = R2 - (release0+release1)/4
       = p(3m-6+3t)delta/4 >=0.                  (1)

Neither activation direction is released, and neither branch is dropped.

## One owner, three disjoint bookings

Let IT3 and HT3 be influence and entropy of ALL original cores, averaged over ALL five data-history leaves and original labels; S3=8 IT3-HT3. Before activation,

    IT3 = (m+1)/2 + (m-2)delta/2,
    HT3 <= m-1.

To check the influence, after y0 its value is (2m+3)/4+(m-2)delta/2. The next two queries remove (delta+1-delta)/4=1/4. To check entropy, x=1 has weight1/2 and entropy m; every other terminal is z times a sign on m-2 data bits and has entropy at most m-2. Therefore

    S3 >= p[3m+5+4t-2c+4(m-2)delta]
       >= p(3m+2+4t) > p(3m+1+4t).             (2)

Only log2(e)<3/2 is used in the final inequality. The bound covers t=0 as well, with slack. In particular the SAME two old bookings, and one additional disjoint booking, fit this actual NEW terminal partition:

    Rold <= (delta/4) S3,
    Ux   <= (delta/6) S3,
    Uy   <= (delta/12) S3.

Their sum is delta/2<=1/32. The first booking already contains the entire remaining bank R3<=Rold; do not add both banks. The third booking is taken from the previously unbooked part of the SAME owner. No old fraction is reissued and no claim that S3 equals its earlier value is made. Equation (2) verifies the old bookings directly on the new partition.

## Controller continuation, including coincident labels

The x=1 terminal has identical cores and zero two-controller bill. At each of the other four data-history leaves, either all labels coincide or exactly ONE original label of probability1/4 is a point edit of one common seed on n=m-2 bits, balanced by z. The edited terminal may have the opposite overall seed sign; its sign does not affect the following calculation. The other two labels stay present and coincide.

Put eta=2^-n. The edit event in the two fair controller bits has four Fourier coefficients of magnitude1/4. At every one of the 2^n data frequencies the three nonempty controller amplitudes have magnitude eta/2. Thus v_T=3eta^2/4, V=sum v_T=3eta/4, Hplus=(2n+2)V, IC=eta and the unactivated bank R=nV. No seed flatness is assumed for this statement.

Here is the full entropy refund, with zero rows allowed. Let q_T be the mixture of the terminal squared coefficients and a_T the mean coefficient. Then a_T^2=q_T-v_T and sum q_T=1. Concavity of E(s)=s log2(1/s) gives E(q_T-v_T)-E(q_T)<=v_T log2 q_T+c v_T. Since v_T/V=eta and q_T>=v_T>0, weighted Jensen yields sum v_T log2 q_T<=-nV. The mixture entropy J=H(q)-sum pi H(core) obeys J<=2c IC. One can prove this by applying Ent_nat(a^2,b^2)<=(a-b)^2/2 on each physical controller bit, tensorizing, and summing the data rows by Parseval. Consequently the complete controller bill obeys

    Dcontrols <= (n+2+c)V+2c IC
              = R+(2+c)V+2c IC < R+6 IC.

This proof includes every original terminal. Activation scales the bill and IC by p, and adds nonnegative capacity to the ACTUAL R, so R+10 IC is valid for every leaf in the policy. It neither divides by seed coefficients nor assumes distinct edited vertices after restriction.

## Complete telescope and scope

Let Icontrol3 denote total physically reached controller influence, and let Qdata be reached data influence. Then I(F)=Qdata+Icontrol3+IT3 exactly. The data entropy decrements are at most 10 Qdata+Ux+Uy. Summing the complete controller bills gives at most R3+10 Icontrol3. Hence

    10 I(F)-H(F) >= 2 IT3+S3-R3-Ux-Uy
                 >= 2 IT3+(1-delta/2)S3 >=0.       (3)

The stronger known class certificate H<6I is not new. The new conclusion is the explicit same-owner payment of the returned bad partner query and its full opposite sibling, after both old debits were already booked. A fixed-price rule using only query influence and released bank remains false.

All denominators are positive for the stated domain. The smallest m=4 leaves n=2, p>0 for each finite t, and delta<=1/16. There is no exchange of limits and no witness chosen independently of the dimension. The statement does not remove the essential common quadratic seed, point edits, balancing sign or independent fair controllers. The first unsupported universal line is an analogue of (2) for arbitrary nonflat core histories: actual terminal surplus need not remain proportional to m, and the already booked Ux cannot be dropped or renewed. Subsequent queries need either a verified transport of the remaining source surplus or a policy that earns enough new signed query slack from its actual pivots.
