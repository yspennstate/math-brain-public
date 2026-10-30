# Cheap degree-tilt cross-entropy does not price its own witness entropy

All entropies use base2. This is a source-complete obstruction to a possible supplier for A056 v7, not a refutation of v7 or FEI. The function is an actual balanced Boolean family with every coordinate relevant. No probability distribution lacking Boolean realizability is substituted.

## 1. Boolean family, means and full spectrum

Let x be k guard bits, z one bit and y an independent block of m bits. Put A_k=1 when all guard bits are0, delta=2^-k, and chi_m=product of the y signs. Define

    f_{k,m}=(1-A_k)z+A_k chi_m.                         (1)

The output is a sign on every input. Since z and chi_m are balanced and independent of A_k, Ef=0. All coordinates are relevant for k,m>=1. Expanding the point indicator gives three disjoint spectral sectors:

    {z}:                 amplitude 1-delta;
    {z} union U, U!=0:   amplitude -delta, count 2^k-1;
    Y union U, all U:    amplitude delta, count 2^k.      (2)

Signs use the convention A_k=delta sum_U chi_U; alternative point conventions change only signs. Their degrees are1,1+|U|,m+|U|. Parseval is (1-delta)^2+(2^(k+1)-1)delta^2=1. Literal influences independently give

    Inf_z=1-delta; Inf_(each y)=delta;
    Inf_(each guard)=delta;
    I(f)=1+delta(m+k-1).                                (3)

Take the explicit diagonal m=2^k. Then

    2<=I_k=2+(k-1)2^-k<=9/4.                            (4)

The upper bound follows from(k-1)/2^k<=1/4 for all integers k>=1. Entropy from(2) is exactly

    H(P_k)=-(1-delta)^2 log2((1-delta)^2)
             +2k(2^(k+1)-1)delta^2.                    (5)

The first term is at most1, while the second is at most4k delta<=2. Thus H(P_k)<=3<=(3/2)I_k. Also -p log2 p<=(1-p)/ln2<2(1-p) proves H(P_k)<=4(k+1)delta, so H(P_k) tends to0. This is far from an FEI counterexample.

## 2. Its pure degree-tilted reference has unbounded entropy

The phase is balanced, so v7's target law is S_k(T)=|T|P_k(T)/I_k. It is normalized and has no empty atom. For every one of the 2^k carrier atoms Y union U,

    S_k(T)=(2^k+|U|)delta^2/I_k<=delta,
    sum_(carrier atoms) S_k(T)
                   =(1+k delta/2)/I_k>=1/I_k.           (6)

The first inequality follows from1+k delta<=2+(k-1)delta. Therefore their entropy alone gives

    H(S_k)>=k/I_k,
    H(S_k)/I_k>=16k/81 -> infinity.                     (7)

Despite(7), the cost under the TRUE spectrum is

    CE(P_k,S_k)=H(P_k)+D(P_k||S_k)
               <=H(P_k)+I_k<=(5/2)I_k,                 (8)

using the independently restated v7 scalar identity D(P||S)=log2 I-sum P log2|T|<=I for a balanced law. Thus neither replacing CE(P,S) by H(S), nor inferring H(S)<=C I from a cheap paid reset, is valid. No earlier A056 theorem made that substitution.

The standard pointed spectral law W(i,T)=P(T)/I for i in T has marginal S(T). Hence H(W)>=H(S) and also has unbounded entropy/influence. Its index marginal q_i=Inf_i/I has m carrier labels of mass delta/I, so H(q)>=k/I. This rules out a constant-I bill for this entire influence-normalized pointed witness or its coordinate label. It does not rule out coding the original spectral set, inverse-degree accounting, a different witness, or a once-per-set shared dictionary.

## 3. Paid physical history retains the obstruction and both terminals

Query the first guard bit. With probability1/2 the event is killed and the phase is z; with probability1/2 it is f_{k-1,m}, where m=2^k stays fixed. Both children are nonconstant and balanced, including k=1 (the active child is chi_m). This physical query costs delta influence and

    I_k=delta+(1+I_plus)/2,
    I_plus=3+2(k-2)delta.                               (9)

For k>=2, I_plus<=7/2. The active child has guard probability delta_plus=2delta. Each carrier atom of its degree-tilted law is at most delta_plus and their combined mass is at least2/I_plus. Consequently

    E H(S_child)>= (k-1)/I_plus >=2(k-1)/7,
    E H(S_child)/I_k >=8(k-1)/63 -> infinity.            (10)

The original reference is exactly P_k. Carry it by the true physical channel; its children are the exact child spectra. The old entropy debit

    L_old=H(P_k)-[H(P_z)+H(P_plus)]/2

is nonnegative by the erasure+JS identity. Freshly replace each child reference by its prescribed degree tilt. Keep the signed substitutions and the full terminal H+KL. The actual complete ledger is

    L_old+E CE(P_child,S_child)
        =H(P_k)+E D(P_child||S_child)
        <=H(P_k)+E I_child
        <=(5/2)I_k.                                    (11)

Every old physical debit and both full terminal bills are retained. The reset of z costs0; the active reset may cost positively. Equation(10) still makes the entropy of the terminal reference/witness unpayable from ANY constant multiple of the same original I_k. Even a nonnegative old debit cannot repair it. Finite exact checks record both costs separately; no comparison of H(S) with CE(P,S) is silently introduced.

## 4. The physical restriction condition matters: fixing z changes the means

If instead z is physically fixed to tau in{-1,+1}, the child is

    g_tau=tau(1-A_k)+A_k chi_m,
    E g_tau=tau(1-delta), V=2delta-delta^2,
    I(g_tau)=delta(m+k).                               (12)

Its true squared masses are those in(2), with the dominant atom now EMPTY and guard-sector degrees |U|. Its entropy equals H(P_k). The empty-calibrated degree tilt must keep mass(1-delta)^2 at the empty set and put only V on nonempty sets. Since there are at most2^(k+1)-1 nonempty atoms,

    H(S_g)<=h2(V)+V log2(2^(k+1)-1)
            <=1+2delta(k+1)<=3.                        (13)

Thus the divergence in(7),(10) requires keeping the balanced outside literal unqueried. Forgetting the new nonzero means and tilting without empty calibration would manufacture a different law. The literal restriction has entropy drop0 and influence drop1-delta, which is checked directly. This is the precise physical-restriction qualification needed for this composition family.

## 5. Correct witness normalization: select the set before selecting its point

For ANY Boolean squared spectrum P, include a null witness of mass P(empty), and for every nonempty T put

    J_star(i,T)=P(T)/|T| for i in T.                     (14)

Its set marginal is exactly P rather than the size-biased S. Direct entropy expansion gives

    H(J_star)=H(P)+sum_(T nonempty) P(T)log2|T|
             <=H(P)+I-Var(f).                          (15)

The last inequality follows from log2 d<=d-1 for every positive integer d, proved by induction from2^(d-1)>=d. The joint includes the null atom, so constants and biased phases require no omitted label charge. Thus the per-set pointed witness costs at most one additional influence unit beyond the original spectrum. It is FEI-equivalent as an INITIAL supplier: a universal price for J_star implies FEI by marginalization; FEI(C) gives H(J_star)<=(C+1)I. Equation(15) is a normalization correction, not a proof of either universal initial price.

On the explicit balanced family, H(J_star)<=(5/2)I-1, while the influence-normalized W in section2 has unbounded H(W)/I. The difference is the order of sampling and its law, not a failure of the Boolean constraint. This leaves a concrete whole-set interface for the next attempt: preserve the P marginal and pay any shared label once per set, rather than pricing the size-biased law or its influence label entropy.

## 6. Validation, source dependency and first unpaid universal line

FROZEN_SPEC fixes direct truth tables at(k,m)=(1,2),(2,4),(3,8), including both first-guard children and both z children, and exact binomial certificates for k=1..32,64,128,256. Direct Walsh transforms, literal edges, mean/variance, positive reset prices, complete old-debit/full-terminal equalities and biased-child calibration are checked. Compressed certificates verify Parseval, degree moments, every sector count, rational entropy lower coefficients, source upper inequalities and both physical influence telescopes. Larger dimensions are not truth-table enumerated. The all-k theorem is proved by(1)-(13), not inferred from finite certificates. No approximate sign decides a claim.

The negative family and physical means are independent of v5 transport. Equation(8),(11) use the scalar degree-tilt bound, reproved here via KL, degrees>=1 and max_(r>=1) log2(r)/r=1/(e ln2)<1; no universal source-price assumption is used on this explicit family. Equation(14),(15) is checked by explicit joint atoms in all direct cases, with the original spectral marginal and complete overhead retained. General v5-v7 transport remains pending independent reconstruction. First unpaid universal line: build an influence-priced INITIAL source or an original-spectrum whole-set witness without charging its size-biased pointed entropy. Bounds only on set-size bias or influence-normalized coordinate labels cannot supply it. Full FEI remains OPEN.
