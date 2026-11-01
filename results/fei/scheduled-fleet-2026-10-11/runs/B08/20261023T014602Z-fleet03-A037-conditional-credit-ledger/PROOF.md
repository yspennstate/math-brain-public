# A second paid reset on the already converted x branch

Full FEI remains open. A second prescribed factor reset costs less than 1/24 bit globally. The original source account, with its first reset and old quarter-bit booking retained, still has more than 17/24 bit. This advances the paid mixed history of A036-PAID-CORRELATED-MIXED-RESET@1 at its x-branch interface.

## Statement and references

All physical bits are independent and fair; all entropy, cross-entropy and KL are in bits. For every m>=1,r>=2 let h be a product of m disjoint width-r point defects, and put delta=2^-r and t=Pr(h=-1). Define

    F_h=(-1)^a on x=0; h on x=b=1; +1 otherwise.

The initial reference is A036/A050's normalized correlated Fourier-sector lift Q0. For each original point factor p_r, put

    q_r^0(empty)=p_r(empty),
    q_r^0(s)=(7/8)p_r(s)+(Var(p_r)/8)1[s=full]   (s!=empty).

Tensor these factor laws. The lift copies the six actual zero-data/control masses and assigns q_core(s)/16 to each of the four control masks 0,x,b,xb when s is nonempty. It is normalized and dominates the actual spectrum. It is a specified INITIAL source. No conversion from an older occupancy reference is included.

Query b first and retain the complete b0 terminal. In b1 take any finite adaptive tree of fresh data queries, keeping x,a unqueried. At any subset of its leaves query x and retain BOTH physical children. Exercise the first reset: use the exact matching character law on x0; on x1 use the tensor reference whose surviving width-w>=2 factors are

    q_w^1(empty)=p_w(empty),
    q_w^1(s)=(5/6)p_w(s)+(Var(p_w)/6)1[s=full].

Width-zero constants and width-one characters use their exact actual spectrum. Fixed leaves are physical subcubes; a surviving factor is a point defect, character or constant. Its sign is irrelevant to its squared spectrum. Record the complete mean first reset sigma1=new KL-old KL. Keep every unselected/complementary terminal inherited.

At any subset of these ALREADY RESET x1 core children, choose one surviving point factor of width w>=2 and query one of its fresh physical coordinates. Retain both outcomes. Exercise the second reset only on that factor: the active remaining width w-1>=2 gets

    q_(w-1)^2(empty)=p_(w-1)(empty),
    q_(w-1)^2(s)=(4/5)p_(w-1)(s)+(Var(p_(w-1))/5)1[s=full].

If the factor becomes constant or a character, match it exactly. Every unqueried factor retains its actual, already paid 5/6 reference, without replacement. Leave all other terminals unchanged. Let sigma2 be the complete physical mean second reset. A prior booking omega in [0,1/4] remains charged to the same original owner.

The conclusion is

    sigma2 <= log2(5/4)/8 < 1/24,
    S-[A0+e+sigma1+sigma2]_+-omega >17/24,

where A0=D(P_F||Q0), S=4 E I_leaf-E H_leaf and e=H(F)-E H_leaf-4(I(F)-E I_leaf). All complete terminal entropies, reference KLs, complementary branches and prior bookings remain present. The theorem is all-m, all-r and all stated adaptive-prefix/selection policies. No arbitrary-core supplier or a-branch continuation is asserted.

## 1. The original source price and first actual reset

This section reconstructs the exact interface from A036 rather than assuming an unreviewed FEI premise. A point factor has p_r(empty)=(1-2delta)^2, p_r(s)=4delta^2 at nonempty s, I_r=2r delta and variance v_r=4delta(1-delta). Its nonempty entropy is 8(r-1)delta(1-delta). Its empty contribution is at most v_r/ln2<3v_r/2, because ln2>2/3. Since q_r^0(s)>=(7/8)p_r(s) and its empty mass matches,

    A_r<=v_r log2(8/7)<v_r/5.

The last inequality follows from 8^5<2*7^5. Therefore

    CE(p_r,q_r^0)<(8r-6/5)delta(1-delta)
                 <4I_r-6delta/5.

Tensor CE and influence add. Direct sector expansion gives A0=A_core/4. Also H(F)=2+H(G)/2, where G selects +1 or h on b. Erasing b and using mixture entropy yields H(G)<=2+H(h)/2. Thus CE(P_F,Q0)<=3+CE_core/4. Direct physical influence counting gives I(F)=1+t/2+I(h)/4. The original inclusive margin M0=4I(F)-CE(P_F,Q0) consequently satisfies

    M0>1+2t+3m delta/10.                                  (1)

At the first x reset the pair mean fresh KL is A_core^1/2, since the character child matches. Each fresh factor has KL at most L1 Var(factor), L1=log2(6/5)<11/40; the integer certificate is 6^40<2^11*5^40. Dropping only nonnegative old KL on the reset terminals bounds sigma1 by the fresh bill. The b1 reach is 1/2, the x1 fraction is 1/2, and conditional variance contracts on the SAME adaptive physical history, factor by factor. Hence

    sigma1 <= (L1/4) sum_original Var(factor)
           = L1 m delta(1-delta)<11m delta/40.              (2)

Subsets of first-reset nodes only reduce this nonnegative upper bound. All inherited reference normalizations and complete first-reset amounts remain in sigma1. Equations (1)-(2) give

    M0-sigma1>1+2t+m delta/40>1.                           (3)

This is the SAME original margin after its first exercised reset, not a new source certificate at the converted core.

## 2. A query changes only one factor's inherited reference

At an x1 child the actual spectral law and the PAID reference are products over its disjoint surviving physical factors. For a query in factor j, write their laws p_j times p_-j and q_j^1 times q_-j^1. Erasing that queried frequency leaves these products. The coherent physical outcome kernel depends only on the queried factor, on every positive source fiber:

    k(y|T_j,T_-j)=p_(j,y)(T_j)/(2 p_(j,erased)(T_j)).

The actual spectator factor cancels in this quotient. Source/reference support matches here: a width>=2 point spectrum is positive on its whole cube, while constants/characters use matching references. Thus source-zero/reference-positive ghost fibers cannot spoil this cancellation; zero/zero rows carry zero mass and retain the declared fair extension.

After the actual outcome, the inherited reference is EXACTLY

    q_(j,y)^predicted times q_-j^1.

The prescribed second reference is q_(j,y)^2 times the SAME q_-j^1. Expanding the KL logarithm now cancels every unqueried factor in the new-minus-old reset:

    sigma_at_node
      = mean_y [D(p_(j,y)||q_(j,y)^2)
                -D(p_(j,y)||q_(j,y)^predicted)].          (4)

It is the full inherited factor KL, not a freshly reissued tensor KL, on the second line. This exact product cancellation is the load-bearing new step.

## 3. Uniform second-reset price

A physical coordinate query in a surviving point factor has one inactive constant child and one active smaller point child, each physically weighted 1/2. For w=2 the active child is a character; both destination KLs vanish. For w>=3 the active destination dominates (4/5)p, preserves the empty mass, and therefore has KL at most L2 Var(active factor), where L2=log2(5/4). The inactive destination has zero KL. From (4), dropping ONLY the queried factor's old nonnegative conditional KL gives

    sigma_at_node <= (L2/2) Var(active factor)<=L2/2.       (5)

There is no factor-count term. The total physical reach of eligible x1 children is at most (b1 reach)*(x1 fraction)=1/4, regardless of the adaptive prefix, the selected nodes or the chosen queried factors. Thus

    sigma2 <= L2/8 <1/24,                                 (6)

where L2<1/3 is the exact integer inequality 5^3<2*4^3. Both outcomes are retained in the 1/2 factor in (5). Replacing that factor by a unit weight would lose the stated constant.

## 4. Terminal certificates and the same diminished owner

All actual point restrictions obey H<=4I. This follows directly from the displayed point spectrum: the nonempty entropy plus empty bound is <4I for width>=2; width0/1 gives a constant/character with zero entropy. Tensor entropy/influence add. No general FEI assumption is used.

The retained b0 character/constant selector has S4=2 at reach1/2, contributing1. Each selected x pair retains a character with S4=4 at half its parent reach. Its data core, before or after the new query, has nonnegative S4. Every unselected selector core has S4>=2, from H=2+H(g)/2 and I=1+I(g)/2. Therefore the COMPLETE final frontier has

    S>=2.                                                 (7)

Let E,O be cumulative erasure and physical-outcome KL through the real history, including the data query after the first reset. If K_final is the complete current terminal reference KL, exact same-channel telescoping with the two exercised resets gives

    A0+sigma1+sigma2=E+O+K_final.                          (8)

The first reset is not omitted or replaced by a delayed diagnostic. For the complete terminal entropy and influence, direct algebra, without an affordability assumption, gives

    S-(A0+e+sigma1+sigma2)=M0-sigma1-sigma2,
    S-[A0+e+sigma1+sigma2]_+
      =min(S,M0-sigma1-sigma2).                           (9)

Combining (3),(6),(7), this minimum is greater than 23/24. Subtract the SAME prior omega<=1/4 ONCE to retain more than 17/24. The earlier 3/4 guarantee and the new 17/24 guarantee concern different frontiers: the difference 1/24 is an allowance for the new actual reset. No universal FEI constant changes.

Both complete H_leaf and K_final remain in (8)-(9). The negative query edges inside e are owned by this account; charging the stronger separated liability A0+[e]_+ would invalidate the stated proof. A positive sigma2 is a real debit, and is not offset by restarting M0, sigma1 or omega.

## 5. Adversarial scope guard

Only the queried factor is reset the second time. If an untouched width-two point factor were ALSO changed from 5/6 to 4/5, its extra KL would be

    c=(1/4)log2(3125/3024)>0.

This follows exactly from its four masses: p is uniform, while the two nonfull nonempty reference masses are beta/4 and the full mass is 3/4-beta/2. The KL difference is (1/2)log2(25/24)+(1/4)log2(20/21)=c.

For a uniform tensor of M=32 width-two point factors and no preliminary data query, query x, exercise the first reset, then query one factor coordinate and reissue 4/5 references on ALL the other factors. The queried factor has only constant/character children, so its own reset cost is zero. The second reset is exactly (31/16)log2(3125/3024)>31/512>1/24 globally. The integer certificate 3125^32>2*3024^32 proves the first strict bound. This is an actual Boolean tensor family, evaluated symbolically, and it refutes extending the NEW constant reset-price bound to resetting all factors. It does not refute FEI or necessarily exhaust the larger tensor's original owner.

## Validation and rung

The frozen main domain is four actual roots (m,r)=(1,3),(2,2),(2,3),(3,2), each with three declared ordered policies. They query b, the first data bit, then x at both reached data leaves, and ACTUALLY exercise the 5/6 reference before the next query. The second query is on the first/last eligible factor at all cores, or the last factor only under the first data outcome0. The latter two (2,3) policies exercise strictly positive second resets; the outcome0 pair has two unequal nonconstant children. Other constant/character boundaries are retained. No whole-cube search at M=32 is run; the scope guard is an exact tensor formula.

An independent implementation uses literal Walsh character sums, Fraction posterior products and exact rational coefficients of prime logarithms. It checks (4) by exact cancellation, not interval overlap, at widths2..5 with untouched spectator widths2,3. Its separate atanh intervals certify positive width-three resets and the local upper bound. The main implementation uses integer FWHT, direct physical-edge influence counts, normalized Fraction references and rigorous outward log intervals. Analytic (1)-(9) establish the all-parameter conclusion; finite checks alone do not.

Rung: analytic proof with exact finite certificates; independent review pending. A core-Lean source formalizes only the scaled 24-unit budget step. Compute admission determines whether it is checked; no entropy/FEI formalization is claimed.

First unsupported universal line: pay the corresponding post-reset query on an a child, where the controller and core remain coherent and the product cancellation (4) need not hold, or supply an eligible arbitrary-core correlated reference and inherited owner. No already owed canonical occupancy source is retired here. Continuing the a-branch interface is the nearest nonseparated test of the same diminished-owner mechanism.
