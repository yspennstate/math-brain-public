# Prime-only high-read diagnostic and independent-set posterior identity

All logs are base two; gamma=6/5. R denotes the foresttarget surrogate residual, not full actual queue cross-entropy. Let f_G be the sign of the positive edge DNF of a simple graph G with no isolated relevant vertices. Its positive prime implicants are exactly its edges: a minimal satisfying positive input contains one edge, while input monotonicity makes negative literals redundant. Fix one full endpoint order per edge, pi=1/4, and positive globally fixed edge weights lambda obeying coordinate packing.

For every nonempty INDEPENDENT selected set A in G, every eligible owned edge contains exactly one coordinate of A. Distinct coordinates must use distinct gates and cannot induce ownership-incidence arcs. All used gates are singleton source SCCs, so every one is a root. Each ownership has a unique zero-child event. Its subset factor is one, and its rank factor at j is r_e(j)^(-gamma), since no other selected coordinate lies in that edge. Summing ALL distinct ownership events gives the exact posterior surrogate mass

    W_A = product_{j in A} [ (1/4) sum_{e incident j} lambda_e r_e(j)^(-gamma) ].

This is an equality at a fixed reference, not a sampled-set-dependent change of table. It remains multiaffine: independence ensures no edge variable appears in two product factors. Selecting one incident gate and paying its individual log(1/lambda) can miss arbitrarily large posterior cancellation. Packing bounds each incident sum by one, but supplies no lower bound. This identity is a general diagnostic tool, not a universal PI-J payment theorem.

Apply it to K_{p,q}, p,q>=2, after relabeling p<=q. The Boolean function is (OR_p) AND (OR_q), while its positive all-prime table has pq gates and reads q,p. Set d=q, lambda_e=1/d, one full order with left endpoint first. This table is fixed and feasible. The one-sided exact masses are W_A=4^(-|A|) on left-only sets and W_A=(p/(4q) * 2^(-gamma))^|A| on right-only sets. The pq labels collectively pay the root choices; the right side retains a real log(q/p) imbalance charge.

For a mixed set, choose any eligible ownership partition. The condensation DAG admits a rooted spanning forest with exactly one root in each source SCC: choose an outward tree in each SCC and incoming edges in the condensation graph. Its used-gate count g and root count c are at most |A|. On width-two gates each subset ratio s/kappa and each strict-predecessor rank ratio are at least 1/2 per selected coordinate. Thus at least one distinct actual event exists and

    W_A >= d^(-g) 4^(-c) 2^(-2 gamma |A|)
          >= (4d)^(-|A|) 2^(-2 gamma |A|).

Additional posterior events can only improve this mass. This crude bound is used only in the mixed Fourier sector. No det-moment surrogate is substituted for an actual probability.

Put u=2^-p, v=2^-q, a=1-u, b=1-v. Physical Fourier coefficients have magnitudes 2bu on left-only sets, 2av on right-only sets, and 2uv on mixed sets. Influences I_L=2pub and I_R=2qva. The degree-weighted sector masses are b I_L, a I_R and v I_L+u I_R; they sum to I=I_L+I_R. Variance V=4ab(1-ab). The one fixed table therefore satisfies

    R <= V log T + 2 b I_L
         + (2+log(q/p)+gamma) a I_R
         + (2+log q+2 gamma)(v I_L+u I_R),
    T=(1+1/(4q))^(pq)-1.

This upper bound already implies an upper bound on the infimum over ALL positive weights, all full orders and both output sides: enlarging the representation menu cannot increase the infimum. It never asserts a sharp optimum or a lower bound on every table.

Here is a dimension-independent bound for every unequal parameter regime. Since log T<=p/(4 ln2), V<=4(u+v), and I>= (3/2)p(u+v), the normalizer costs at most 2I/(3 ln2). The basic degree charge is 2I and the extra one-sided gamma charge is at most (6/5)I. For k=q-p, I_R/I <= (4/3)(q/p)2^-k. Using q/p<=1+k/2, log(q/p)<=k/(2 ln2), and k(k+2)<=2^(k+1), the imbalance charge is at most 2I/(3 ln2). The integer inequality follows at k=1,2 and by induction for k>=2 because (k+1)(k+3)<=2k(k+2).

The mixed gamma charge is at most 2 gamma u I <=(3/5)I. Its log q charge splits as v I_L log q/I <=2^-q log q<=1/4 and u I_R log q/I <=(4/3)(q/p)2^-q log q<=1/2. Use log q<=q-1, (q-1)2^-q<=1/4 and q(q-1)2^-q<=3/4 for integer q>=2. Each integer bound is checked at its initial maximal points and decreases thereafter by adjacent ratios. Consequently

    R/I <= 91/20 + 4/(3 ln2) < 13/2.

The final strict sign is rational: ln2 = 2(1/3 + (1/3)^3/3 + ...) >56/81, and 91/20+(4/3)/(56/81)=907/140<13/2. Interchanging the bipartition before fixing the order handles p>q. Constants and one-vertex-side sunflowers are outside the declared diagnostic, avoiding repeats of A006.

Thus dense unbounded-read COMPLETE BIPARTITE positive prime tables do not produce variational residual growth, including highly imbalanced side sizes. This is a route-candidate elimination, not a new FEI theorem for its already read-once Boolean function. The universal unsupported step is influence payment on non-independent Fourier sectors of arbitrary graphs: the exponentially suppressed mixed-sector degree identity used here does not hold for arbitrary graph spectra.
