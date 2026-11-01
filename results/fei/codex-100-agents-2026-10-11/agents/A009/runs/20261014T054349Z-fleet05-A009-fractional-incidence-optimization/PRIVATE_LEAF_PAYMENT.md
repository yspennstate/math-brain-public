# Complete prime-reference payment for arbitrary cores with private leaves

Let H be ANY finite simple graph on r>=1 named hub vertices, allowing isolated hubs. Attach m_i>=1 degree-one private leaves to hub i, independently for every hub, and retain every core edge. Let G be this augmented graph and f_G the uniform-cube positive edge DNF. All edge conjunctions are exactly its prime implicants. The core may be arbitrary, densely connected and non-read-once; the m_i can vary without bound. Every gate has both endpoint orders fixed, so original size/subset probabilities are t(singleton)=1/4 and t(pair)=1/6. Rarity is pi=1/4.

Fix one GLOBAL weight vector: private edges at hub i have lambda=1/(2m_i); a core edge ij has lambda=1/[2 max(d_H(i),d_H(j))]. Every hub spends 1/2 on private edges and at most 1/2 on core edges; every leaf spends at most 1/2. Thus all coordinate constraints hold. These are weights on the SAME full prime table; the selected witness family uses only private gates, while all core gates remain in D=product_all_edges(1+lambda/4)-1 and have paid absent-root probability. No table is selected as a function of A.

## Actual complete forest numerator

For a nonempty set A, split it into hub/private-leaf blocks. In a block let h indicate whether its hub is selected and t be the number of selected leaves, with m=m_i and ell=1/(2m).

If h=0, every selected leaf owns its unique private gate, which is an isolated root with zero children. The exact numerator is U_0(t)=(ell/32)^t, including U_0(0)=1. If h=1,t=0, choose any private gate to own the hub singleton as one root with zero children. The m distinct root labels sum to U_1(0)=m*ell/32=1/64.

If h=1,t>=1, choose one of the t selected leaves to pair with the hub in its root gate. Every other selected leaf owns its own gate as a child at the hub coordinate of that root. There are (t-1)! distinct chronological label sequences at this repeated attachment. The root is chosen in t ways. For c=t-1 the parent count/multiset probability is 1/[t^2(t+1)]. Thus

    U_1(t)=t! ell^t / [24*8^(t-1)*t^2*(t+1)]     (t>=1).       (1)

The root pays ell*pi*t_pair=ell/24; each singleton child pays ell*t_singleton*Pr(zero children)=ell/8. All root rarity, selected-size, subset, count, attachment and chronological factors appear in (1). Different blocks use disjoint private supports, so their ownership graph has no inter-block arcs, regardless of unused core edges. Each block is an outgoing star or isolated roots; exactly the original source-SCC root restriction holds. Queue traces recover root pair and chronological choices; different traces are distinct. Initial root order is fixed, and earns no extra permutation credit. Consequently

    Q_PL(A)=D^-1 product_i U_(h_i)(t_i)

is an exact nonempty output subprobability, positive on every A. At its actual conditional posterior, complete cost minus witness entropy equals -log2 Q_PL(A). Every failed/infinite queue outcome remains outside this lower mass.

For every block a=h+t,

    U_h(t)>=96^(-a) m^(-t).                              (2)

For h=0 this follows from U_0=(64m)^-t; for h=1,t=0 from 1/64>=1/96. For h=1,t>=1, the elementary count bound t^2(t+1)<=[2*6^(t-1)] and (t-1)!>=1 in the unreduced root/child formula give U_1(t)>=(ell/48)^t=(96m)^-t, which is stronger than (2). The count bound is the standard (c+1)^2(c+2)<=2*6^c, also proved by adjacent ratios. Therefore full nonempty spectral cross-entropy obeys

    C_PL <= v log2 D + (log2 96) I
              +sum_i I_(private leaves of i) log2 m_i.       (3)

No rare-tail approximation is used and no spectral set is excluded.

## Exact physical payment

Write q=Pr(f_G=-1)>0 and a_i=Pr(f_G=-1,x_i=-1), b_i=Pr(f_G=-1,x_i=+1). Then a_i+b_i=q. Conditional on hub i being negative, its degree-one leaves are irrelevant to all other graph edges and remain independent fair bits under the false event. Turning the hub positive requires ALL its leaves negative and all its core neighbors negative. Hence

    b_i<=2^(-m_i) a_i.                                 (4)

Monotonicity gives Inf_(hub i)=2(a_i-b_i)>=a_i and also >=2q/3, since m_i>=1. For each private leaf, its unique pivotal partner state is the false event with positive hub and negative leaves, so Inf_(leaf)=2b_i exactly. Thus

    sum_(leaves at i) Inf_leaf log2 m_i
      =2m_i b_i log2 m_i
      <=2m_i 2^(-m_i) log2 m_i a_i
      <=(9/4) Inf_(hub i).                             (5)

The scalar bound m log2 m /2^m<=9/8 uses log2 m<=m and m^2/2^m<=9/8. The latter holds at m=1,2,3 and decreases from m=3 onward because ((m+1)/m)^2/2<=8/9 for m>=3. These bounds are intentionally coarse but all-dimensional. Summing Inf_hub>=2q/3 gives I>=2rq/3. Since v=4q(1-q)<=4q, rv<=6I.

Total private-edge weight is r/2 and total core-edge weight at most r/4, hence sum_all lambda<=3r/4. Using log D<=sum lambda/(4 ln2) retains the root normalizer even when it is negative and yields

    v log2 D <= [9/(8 ln2)] I.

Combining (3)-(5), with the same physical I used only in this explicit sum, gives

    C_PL <= [log2 96+9/4+9/(8 ln2)] I < 11 I.            (6)

For the strict rational sign, log2 96<33/5 because 3^5<2^8, and ln2>2/3 gives the coefficient <33/5+9/4+27/16=843/80<11. ln2>2/3 follows directly from its positive atanh series at z=1/3 (the first term is 2/3 and the next is positive). An optional empty/nonempty entropy split is paid by the existing h2(v)<=2I baseline; it is not needed for the complete nonempty cost assertion. This is a prime-reference coding result, not a claim that an arbitrary original core's FEI ratio is preserved after attaching leaves.

## First unsupported extension

H can be arbitrary and all m_i may equal one, so this does not depend on uniformly small tails or bounded core degree. However every hub must have at least one genuinely PRIVATE degree-one neighbor. For a leafless vertex or a neighbor shared between hubs, (4)'s conditional independence and the block event disjointness no longer follow. The first unpaid extension is a same-reference replacement for (2) and (4)-(5) on such shared/leafless incidence, retaining the normalizer and the true physical spectrum. Adding private leaves changes the function and cannot transfer this payment back to arbitrary cores for free. No universal PI-J or full FEI result is claimed.
