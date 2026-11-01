# Complete-block obstruction to renewing a rate-4 selected-core owner

## 1. Actual Boolean family and complete accounting

All logarithms are base two; put L=log2(e). For n>=2 let g_n be negative exactly on binary indices {0,1,2} in the n-dimensional uniform cube, and put p=3/2^n. Let h be negative on {0,1,2,4,8,16,32,6,17,40} and J(x)=-h(x xor1). Set F_n=J(g_n^6) on six disjoint physical blocks. Selected block is block0. Every other complete core remains present throughout all physical restrictions of block0.

For independent cores with negative probabilities p_l, let q_l be the actual outer pivot probability and let H_p(J) be the entropy of the normalized biased outer squared spectrum. The exact identities are

    H(F)=sum_l q_l H(g_l)+C(p_vec),
    I(F)=sum_l q_l I(g_l),
    C=H_p(J)-sum_l q_l h2(4p_l(1-p_l)).

Indeed the occupied blocks follow the biased outer spectrum, and conditional on occupancy a block has its original nonempty squared spectrum normalized by its variance. Its entropy contribution is q_l[H(g_l)-h2(var_l)]. Pivotal counting gives the influence identity. Constant cores are included with zero entropy/influence, by the same formula at endpoint bias. No FEI hypothesis enters these identities.

On a physical query of block0, q0 is fixed and the other q_l are affine in its selected bias; averaging both uniform children cancels their complete core entropies. Thus DeltaH(F)=q0 DeltaH(core)+DeltaC, and the physical coordinate influence is q0 times its core influence. This is an actual restriction, not a simultaneous change of all six core biases.

## 2. Complete reveal is independent of query order

Write C=C(p,p,p,p,p,p), C_+=C(0,p,p,p,p,p), C_-=C(1,p,p,p,p,p). A complete block reveal ends with a positive selected constant with probability1-p and a negative selected constant with probability p. Other blocks stay nonconstant. Any physical stopping tree that determines g_n exactly, querying only this block and stopping when the core is constant, has full entropy decrement and queried influence

    DeltaH_block=q0 H(g_n)+D,
    D=C-(1-p)C_+-p C_-,
    I_queried=q0 I(g_n).

For the influence identity, each original core influence equals the reach-weighted influence at its query, by conditioning on earlier independent coordinates. An unqueried coordinate at a constant-core leaf contributes zero. Entropy decrements telescope with the same physical reaches. Equivalently affine transport of the five unqueried pivot weights gives these equations directly. Hence the signed cumulative full rate-4 excess is

    e_n=DeltaH_block-4 I_queried=D-q0 S4(g_n),
    S4(g)=4I(g)-H(g).                              (1)

If a debit account is carried exclusively on queried-core descendants, admits no other-owner transfer, and subtracts the exact full signed rate-4 query excess from its remaining surplus at each query, its final mean remaining selected account is q0 S4(g_n)-D=-e_n. The selected-core surplus itself is zero at every final leaf. Therefore e_n>0 makes a nonnegative complete selected-only ledger impossible, even allowing all negative query excesses as refunds. Charging only positive excesses cannot improve this necessary condition. This is a restriction on the specified rate-4 account, not on all possible stopping-tree methods or constants.

## 3. Exact core formula and analytic parameter bridge

Put N=2^n. The Walsh coefficient at the empty set is1-6/N. For each fixed pattern on the first two spectral coordinates the indicator sum is1+s0+s1: one pattern has absolute value3 and the other three have absolute value1. Consequently the g_n squared spectrum has masses

    (1-6/N)^2 once;
    36/N^2 with multiplicity N/4-1;
    4/N^2 with multiplicity3N/4.

Coordinate influences are2/N on coordinates0,1 and6/N on every other coordinate, so I(g_n)=(6n-8)/N=(2n-8/3)p. With ell(z)=-z log2 z, its exact entropy is

    H(g_n)=ell((1-2p)^2)+(N/4-1)ell(36/N^2)+(3N/4)ell(4/N^2).

Expanding the first term at1 yields

    S4(g_n)=s p+O(n p^2),
    s=6log2 3-8/3-4L=1.0723281741044...>0.          (2)

The pivot polynomial of selected block0 is exactly

    q0=4p-14p^2+18p^3-10p^4+2p^5.

For complete outer corrections, exact rational polynomial calculation gives

    D=(32+16L)p^2+O(p^3(1+|log2 p|)),
    C_-=(64-32L)p^2+O(p^3(1+|log2 p|)),
    sum_(l>0)q_l(1,p,p,p,p,p)=16p-42p^2+36p^3-10p^4.

The exact algebra behind these displays is fully reproducible: if W_U is the integer uniform Walsh transform of J, the raw biased coefficient and squared mass are

    z_T=sum_(U superset T)(W_U/64) product_(j in U\T)m_j,
    P_T=z_T^2 product_(j in T)(1-m_j^2),

where m_j=1-2p for a variable bias, and m0=+1 or-1 at the two endpoints. All192 mass polynomials are stored in ASYMPTOTIC.json, with exact Parseval identities. For a nonzero polynomial P=p^r(a+bp+cp^2+...), a>0, Taylor expansion of -P log2 P gives, through order2:

    r=0: [-a log a, -b(log a+L), -c(log a+L)-b^2 L/(2a)];
    r=1: order1 -a(log a+log p), order2 -b(log a+log p+L);
    r=2: order2 -a(log a+2log p).

For r>=3 the entire term is O(p^3(1+|log p|)). For r<=2 the remainder follows from analytic Taylor expansion of log(a+bp+...), which has a positive leading argument for sufficiently small positive p. There are finitely many fixed polynomials, so their remainders sum with a finite constant. Zero polynomials are omitted. Multiplication by the exact pivot polynomials and subtraction of h2(4p(1-p)) show that all order0, order1, and p^2 log p terms cancel in D and C_-. `asymptotic.py` performs exactly these rational operations, not a fitted expansion; polynomial evaluations independently match the direct biased-mass engine at three specified rational biases. The logarithmic constants and their signs have outward rational bounds.

Combining with (1)-(2) proves

    e_n/p^2 -> a=128/3-24log2 3+32L
                    =50.7938079578057...>0.          (3)

Thus e_n>0 for every sufficiently large integer n. No explicit all-tail cutoff is claimed. The exact n=6 certificate separately proves e_6=0.09005821863418...>0. These quantified conclusions come from the analytic limit and a finite sign certificate respectively, not from extrapolating the bounded search.

## 4. Negative full terminal and the failed donor repair

At the negative selected endpoint the complete physical function is T_n=J(-1,g_n^5), on5n actual bits, and its full rate-4 surplus is

    M_-=[sum_(l>0)q_l(1,p,...,p)] S4(g_n)-C_-.

Equations above give

    M_-/p^2 -> b=96log2 3-320/3-32L
                    =-0.6765079058825...<0.          (4)

Hence for all sufficiently large n the full terminal has H(T_n)>4I(T_n). At n6 the exact value is M_-=-0.05755653642329... . Every original g_n assignment giving negative output produces this same nonconstant full terminal; its total reach is p. Its selected-core bank is zero, and its complete other-core banks minus the outer bill are negative. A positive *mean* donor surplus therefore cannot justify nonnegative branchwise donor eligibility. Our attempted endpoint donor repair fails at this precise line; the failure is saved separately.

This does not refute A089's scoped two-query certificate, which is independently reconstructed at its selected J0/inner2 then inner0 continuation. The deterministic n6 order [2,0,1,3,4,5], stopping constant-core branches, has27 nodes. The first negative full S4 node occurs at depth6, not in the two accepted initial queries. Complete entropy/influence telescoping and the two-query no-renewal identity are equalities of exact rational logarithmic forms.

Nor is this an FEI disproof. For the endpoint, I(T_n)=(16p+O(p^2))I(g_n)~32n p^2, and (4) implies H(T_n)/I(T_n)->4 from above. For the parent, sum q_l=4+O(p) and C=O(p^2(1+|log p|)): this last cancellation follows from the order0/1 biased masses (four singleton masses4p, empty mass1-16p) and subtracting4h2(4p(1-p)). Thus H(F_n)/I(F_n)->4 as well. A fixed rate K>4 adds (K-4)I to surplus and removes (K-4)q0 I(g_n) from (1); the asymptotic rate-4 obstruction alone does not rule out that repair.

## 5. Independent review of A084 at unchanged scope

The reviewed source is A084-RARE-PHYSICAL-TERMINAL-CURVATURE@1, statement hash8dec94501ef17bd7c176a8425b16b3a4d0cf36332e6b7ae213596f823906e394. Verdict HOLDS at its stated first-query scope; no repair contributed.

Independent reconstruction: with other five laws fixed, expand the two outer sections as A+y_j D, having biased coefficients a_T,d_T and q=sum d_T^2. For selected mean x set U_T=(a_T+x d_T)^2. The non-affine part of the complete correction is

    F(x)=sum ell(U_T)+(1-x^2)sum ell(d_T^2)+q x^2 log2 x^2.

Differentiation gives F''=-2 sum d_T^2 log2[U_T/(x^2 d_T^2)]: the three constant derivative contributions cancel. Coefficient-zero singularities are logarithmic and integrable, and F is continuously differentiable there. The central physical difference equals the integral of this logarithmic density against the nonnegative tent kernel (|beta|-|u|), whose mass is beta^2. Jensen with weights d_T^2/q and Parseval sum U_T=1-(1-x^2)q bound the density by q log2[1+(1-q)/(x^2 q)]. Actual Boolean singleton constraints |beta|<=d and |beta|<=2p give x>=1-4p>=3/4 and beta^2/d<=2p. This proves the source's bias-dependent first-query envelope.

We verify pivot lower bounds by a separate direct table method: for each h direction, four distinct weight-one other-input assignments are pivotal, so q>=4p(1-p)^4>=3p on p<=1/16. For J directions1,2,3,5 the all-zero assignment is pivotal, so q>=(1-p)^5>=1-5p. J direction0 has a weight-one witness, direction4 a weight-two witness, yielding q>=(3/4)p^r. Exact (15/16)^4>3/4 validates both bounds. The envelope is consequently <=2p log(1/p)<=1/2 for h; <2p<=1/8 for the four dominant J directions; and <=2p[r log(1/p)+2], giving3/4 and5/4 for J0,J4. Each scalar envelope is increasing up to1/16. beta=0, irrelevant coordinates and endpoint constant children follow by continuity of the canceled expression. `review.py` independently checks all12 directional witness sets and rational endpoint inequalities.

The accepted theorem pays additive DeltaC only. No inherited-core entropy payment, owner availability, or arbitrary later heterogeneous-history envelope follows. Equations (3)-(4) here are consistent with that limited first-query theorem.

## 6. First unsupported universal line

The universal gap remains a noncircular rate-K selection/payment rule for arbitrary retained rare cores, with unused full terminal surplus transported through heterogeneous histories. At rate4, extending the two-query selected-only owner until the whole queried core is determined is false by (3); assuming both complete endpoint other-owner margins nonnegative is false by (4). Changing K or providing a conserved other-owner transfer must be justified explicitly rather than renewing the original core bank. Independent reviewers should check the polynomial expansion and leaf-account interpretation before downstream adoption.
