# A uniform normalized entropy budget for the complete matching-gate policy

All entropy is in bits. All Boolean functions are on finite uniform physical cubes.
Let h be negative exactly on binary indices {0,1,2,4,8,16,32,6,17,40}, where a one bit denotes a negative input. For a nonconstant core g, orient its minority output to -1, with probability s=min(P(g=-1),P(g=+1)). Before substitution, use this orientation when s<=7/32 and its complement otherwise. Form h on six disjoint identical copies, then orient the output to its minority again. Repeat the same rule at every level. Write g_d for any finite depth, including d=0.

## Theorem

For every starting nonconstant Boolean core, every dimension, and every finite depth,

    H(g_0)/I(g_0) - 2074/105 <= H(g_d)/I(g_d)
                           <= H(g_0)/I(g_0) + 248/3.

In particular the signed normalized correction is always between -20 and +83. The moderate prefix alone has correction between -314/21 and +200/3. Every exact starting entropy term is retained. This is a bounded COMPOSITION correction, not an absolute FEI bound, a physical restriction-tree payment, or a proof that a hard core can be exposed cheaply. These constants are deliberately coarse.

The proof reconstructs all facts used below. A075's rare-tail proof supplies the source-bound target and prior calculation, but its theorem is not an unreviewed premise. No erasure positivity theorem is needed for the entropy budget.

## 1. Actual composition and bias identities

Let p be the probability of the chosen child output -1, m=1-2p, v=1-m^2, and

    q(p)=2p(1-p)^3(2-p), Q(p)=6q(p).

The minority-negative set of h is a down-set: it consists of the empty set, every singleton, and the three designated matching pairs. A selected input is pivotal with probability q, by counting the configurations of the other five inputs. Pair permutations and pair swaps are transitive on inputs. With the normalized biased outer spectrum b_T^2, each spectral membership marginal is vq, so its expected cardinality is 6vq. The exact disjoint-block entropy and influence identities are

    H(g_next)=Q H(g)+C(p), I(g_next)=Q I(g),
    C(p)=H_p(h)-Q h2(v).                                  (1)

Indeed the occupied outer blocks and their nonempty inner spectral sets are uniquely determined by the physical spectral set. If rho is the core's normalized nonempty Fourier law, H(g)=h2(v)+v H(rho), and H(g_next)=H_p(h)+6vq H(rho). Output complement leaves the entire squared spectrum unchanged. Equation (1) therefore gives the signed, complete telescope

    H(g_d)/I(g_d)-H(g_0)/I(g_0)
                    =sum_(k<d) C(p_k)/(Q(p_k) I(g_k)).     (2)

There is no omission of the terminal core entropy and no identification of substitution levels with physical restriction queries.

Counting the negative set gives alpha(p)=(1-p)^4(1+4p-2p^2). Put

    tau(s)=1-alpha(s)=12s^2-28s^3+27s^4-12s^5+2s^6,
    b(s)=alpha(1-s)=s^4(3-2s^2).

The minority update is tau(s) when s<=7/32 and b(s) when s>7/32. These are the minority branches because tau(7/32)<3/8 and b(1/2)=5/32. Both increase strictly: tau'(s)=Q(s)>0 and b'(s)=Q(1-s)>0 for 0<s<=1/2.

## 2. Analytic entropy envelopes on compact bias bands

For 0<=v,q<=1, the function

    L(v)=q h2(v)+v h2(q)-h2(vq)

vanishes at v=0,1 and has

    L''(v)=q/[ln(2) v] * [1/(1-vq)-1/(1-v)] <=0.

Thus L>=0 by concavity, including endpoints by continuity. Subadditivity of the six spectral membership bits gives H_p(h)<=6 h2(vq), whence

    -Q h2(v) <= C(p) <= 6v h2(q).

Consequently

    -h2(v)/I(g) <= C(p)/(Q I(g))
                           <= [v/I(g)] h2(q)/q.            (3)

The elementary bound h2(q)/q<=log2(e/q) follows from -(1-q)ln(1-q)<=q. Also e<3, from its factorial series, and Poincare gives I(g)>=v (since every nonempty Fourier coefficient has degree at least one).

On the low-moderate band s in [1/16,7/32], chosen p=s. Exact polynomial interval certificates prove

    Q(s)>=19/16, q(s)>=19/96.

Therefore h2(q)/q<4, since e/q<288/19<16. Using v<=1 and h2(v)<=1, each low-moderate correction lies in [-1/I(g),4/I(g)].

On a complemented step s in (7/32,1/2], chosen p=1-s. The compact certificate proves Q(1-s)>=1/9, hence q>=1/54. Thus h2(q)/q<8, since e/q<162<256. Every complemented correction is at most 8, using v/I<=1.

For its lower bound, I>=2s log2(1/s)>=7/8 on [7/32,1/2]. To justify the first inequality without an external premise, induct on dimension for a minority set A. For its two sections of sizes a,b, the edges across the split number at least |a-b|, and inductive section boundaries supply a log2(2^(n-1)/a)+b log2(2^(n-1)/b). The desired difference is (a+b)[1-h2(a/(a+b))]; it is at most |a-b| because h2(z)>=2min(z,1-z). This proves edge isoperimetry and I>=2s log2(1/s). The function 2s log2(1/s) is concave. At s=7/32 it is strictly greater than 7/8 since 32/7>4; at 1/2 it equals 1. On the low-moderate band its endpoint values are at least 1/2, by the same concavity (at 7/32 it exceeds 7/8). Each complemented correction is therefore at least -8/7.

## 3. No uncontrolled repeated moderate excursions

If the initial bias exceeds 7/32, one complemented step sends it to b(s)<=5/32<7/32; it may already be rare. A low-moderate run either stays in its band for as many steps as desired, enters s<1/16, or crosses above 7/32. Its crossing value cannot exceed tau(7/32)<3/8. The next complemented step then sends it to

    b(s)<=b(3/8)=7047/131072<1/16.

Once rare, tau(s)<=12s^2<=3s/4 preserves rarity. Thus the complete stated policy has at most one contiguous low-moderate run and at most two complemented steps. There is no assertion of a uniform length for the low-moderate run. Even a hypothetical exact real fixed-point bias is covered for every finite depth.

If that run starts at index a, I(g_a)>=1/2, and throughout its low steps I(g_(a+k))>=(19/16)^k I(g_a). Hence

    sum_low 1/I(g_k) <= 2 sum_(k>=0)(16/19)^k =38/3.

Combining this with (3), all low corrections sum to an interval contained in [-38/3,152/3]. At most two complemented corrections contribute [-16/7,16]. Every moderate prefix correction therefore lies in

    [-38/3-16/7,152/3+16]=[-314/21,200/3].              (4)

This prices arbitrarily long residence near the irrational fixed bias using a single normalized ledger. It neither waits for a uniform escape time nor invents additional influence.

## 4. Independently reconstructed rare-tail envelope

This section reconstructs the entropy part of A075 PROOF Section5. It is not an independent acceptance of that source's erasure/localization chain, which uses our earlier claim.

For chosen rare p in (0,1/16], 3p<=q<=4p and p_next=tau(p)<=12p^2. Let the raw biased multilinear coefficient of h on a nonempty set T be a_T, so its spectral mass is v^|T| a_T^2. Mixed conditional differences give |a_T|<=1. Each singleton coefficient is -q because the negative set is a down-set. Let ell(x)=x log2(1/x). Expanding the spectral entropy and cancelling all log(v) terms in (1) yields exactly

    C(p)=ell(P_empty)+sum_(T nonempty) v^|T| ell(a_T^2)
                                      -6q ell(1-v),       (5)
    P_empty=(1-2tau(p))^2.

The event h=+1 requires at least one unmatched negative pair; there are twelve, so tau<=12p^2. Consequently 1-P_empty<=48p^2 and ell(P_empty)<72p^2, using ell(x)<(1-x)/ln2 and 1/ln2<3/2.

For the six singleton terms, v<=4p and q<=4p give an upper bound 384p^3[2log2(1/p)-4]<=96p^2. Here ell increases on [0,1/16], and p[2log2(1/p)-4] increases up to the endpoint 1/16, where it equals 1/4; its derivative is positive there and throughout the interval since 1/ln2<3/2.

For |T|>=2, ell(a_T^2)<=1/(e ln2)<9/16. As v<=1/4,

    sum_(k=2)^6 binom(6,k) v^k <=(5385/256) v^2.

Their total is at most (48465/256)p^2. The negative last term in (5) has magnitude at most 6q v/ln2<=144p^2. Hence

    -144p^2 <= C(p) <=360p^2,
    C(p)>=-6q v/ln2.                                  (6)

The numerical inequalities used above follow from ln2>2/3 via its atanh series and e>8/3 via its factorial series, so 1/(e ln2)<9/16; no floating logarithm is used to prove an envelope.

At the beginning of a rare run, r_0=I/p>=4(1-p)>=15/4 by Poincare. Each step satisfies

    r_(k+1)=6q I/tau(p)>=(3/2)r_k.

Dividing (6) by Q I therefore bounds the kth signed correction by

    -(8/5)(2/3)^k <= C/(Q I) <=(16/3)(2/3)^k.

Every finite rare-tail correction lies in [-24/5,16]. This is the full signed telescope with the original tail-core entropy retained, not an absolute terminal entropy claim.

## 5. Complete all-depth theorem and the remaining universal line

Add (4) and the rare-tail interval. For every finite depth,

    -314/21-24/5=-2074/105
       <= H(g_d)/I(g_d)-H(g_0)/I(g_0)
       <=200/3+16=248/3.

If no rare step has yet occurred, (4) already proves these weaker total bounds. If the starting core is rare, Section4 alone suffices. Thus the theorem needs no assumed finite moderate escape time and includes every actual Boolean core.

The exact first unsupported universal line is still an absolute bound on selectable erasure E or H/I for the arbitrary retained rare terminal core. A bounded signed correction preserves its unknown starting ratio; it cannot manufacture an absolute FEI constant. A075's localization now has a bounded full entropy correction including its former unpaid moderate prefix, but the hard rare-core supremum remains unbounded by any proved estimate. Alternating this common-sign policy with A072's DIFFERENT one-flip escape can create new cycles; (4) does not pay an arbitrary repeated one-flip/common-sign strategy. A concrete cancellation or an independently owned terminal slack is required there.

The continuum signs in Sections1-3 are certified by exact rational Bernstein coefficients on fixed compact intervals and by analytic rare endpoint bounds. Finite truth-table and rational entropy checks in code/verify.py validate the signed identities separately; they do not replace the all-dimensional proof.
