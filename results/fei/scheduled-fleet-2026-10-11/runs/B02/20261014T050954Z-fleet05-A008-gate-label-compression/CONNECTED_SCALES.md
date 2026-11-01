# Connected graph weights: uniform failure and complete same-prime repair

Let m>=2. On independent uniform signs h,x_1,...,x_m,y,z, let f_m be the sign of the positive edge DNF with edges {h,x_i}, {h,y}, {y,z}. This graph is connected, with adjacent vertices h,y carrying degrees m+1 and 2. These m+2 edges are exactly its positive prime implicants. Fix both endpoint orders per gate, gamma=6/5 and pi=1/4 throughout. No table, order or weight is selected after a Fourier set is sampled. All costs are bits.

Write u=2^-m. Physical pivotal counting gives

    I_h=3/4-u/2, I_y=1/4+u/2, I_z=1/4, I_(x_i)=u/2,
    I(f_m)=5/4+m*u/2 <=3/2.

In particular the singleton spectral probability P({z})=I_z^2=1/16 for every m.

## Failure of one uniform max-read scale, with full posterior

Set all edge weights to 1/(m+1). Packing is feasible. With D=(1+1/[4(m+1)])^(m+2)-1, Bernoulli gives D>1/4. For A={z}, the only eligible owner is gate {y,z}. It is the only root, selects its singleton and has zero children. Its complete mass is Q_part({z})=1/[32(m+1)D]. This is the mass of ALL partition forests at that set, not a selected representative. Thus the full partition-reference cross-entropy C_part satisfies

    C_part >= (1/16)log2[32(m+1)D] > (1/16)log2(m+1),
    C_part/I > (1/24)log2(m+1).

The source-SCC surrogate residual R is also unbounded at the uniform scale. The independently reviewed A010 pointwise comparison is

    Q_part(A) <= W_B(A)/D <= 72^|A| Q_part(A),
    C_part-(log2 72)I <= R <= C_part.

Therefore R/I>(1/24)log2(m+1)-log2 72. For the actual finite Boolean sequence m=2^(24t), t>=1, R/I>t-7 since log2 72<7. No disconnected-component factorization is used. This disproves a uniform-weight payment rule on connected prime graphs, not PI-J or FEI.

## Complete repair with the same primes, orders and physical overlap

Choose lambda_(h,x_i)=1/(2m), lambda_(h,y)=lambda_(y,z)=1/2. Both h and y incidence rows are exactly one; every other row is <=1. The global D is

    D_rep=(1+1/(8m))^m*(9/8)^2-1 <25/56<1.

Indeed the binomial expansion is bounded above by sum_(j>=0)(1/8)^j=8/7. All weights remain positive and fixed. The repaired reference is exactly the original maximal-matching star output family Q_MS on this graph; no alternate Boolean representation is imported.

For every covered nonempty A, the previously independently accepted A006 mass bound gives, for any maximal matching M and unmatched U,

    Q_MS(A) >= D_rep^-1 48^(-(|M|+|U|)) product_(e in M)lambda_e product_(v in U)r_v,
    r_v=sum_(e incident v)lambda_e.

Every edge weight and row sum is >=1/(2m). Since |M|+|U|<=|A|, this implies Q_MS(A)>=(96m)^(-|A|). Consequently the full cost at any nonempty set is <=|A|log2(96m). The signed root normalization is retained in the lower bound and is only dropped using its proved sign D_rep<1.

For a nonempty CORE set A subset {h,y,z}, choose a maximal matching in that induced three-vertex path. Only core matching edges are used, and they have lambda=1/2. Unmatched core vertices have row sums r_h=r_y=1, r_z=1/2. Hence the same bound gives Q_MS(A)>=96^(-|A|), and cost <=|A|log2 96<7|A|.

It remains to pay sets containing leaf coordinates. Let g be the sign of h OR (y AND z), independent of leaves. Pointwise on the actual cube,

    f_m = g - 2*1_(h=+1)*1_(y=-1)*product_(i=1)^m 1_(x_i=-1).

Thus for every Fourier set with a nonempty leaf part S, its coefficient has magnitude u/2 when its remaining coordinates form any subset of {h,y}, and equals zero when it contains z. This is the exact tail law, not a floating-point approximation to an indicator sum. Its degree mass is

    J_tail = sum_(A hits leaves)|A|P(A) = (m/2+1)u-u^2.

Let J_core=I-J_tail. Complete spectral cross-entropy under the one repaired reference is therefore

    C_MS <= (log2 96)J_core + (log2(96m))J_tail
          < 7I + (m+7)(m/2+1)2^-m
          <= 7I+9/2 <= (53/5)I.

Here log2 m<=m and (m+7)(m+2)2^(-m-1)<=9/2 for all m>=2. Equality of this last upper bound is at m=2; its consecutive ratio is (m+8)(m+3)/[2(m+7)(m+2)]<1. Also I>=5/4, so 9/2<=(18/5)I. All entropy-reference factors including singleton1/4, pair1/6, root choices, labels, sizes, children, attachments and output ambiguity are already inside the A006 lower mass. Optional physical prefix rounding is not included.

Since Q_MS<=Q_part and R<=C_part<=C_MS, the same-prime/order all-weight variational infimum is <=53I/5 on every member of this connected family. This settles a quantifier diagnostic at overlapping degree scales; it is not a new FEI class calibration or an all-graph weight optimum. A009's frozen-posterior root-gap interface is compatible with the repaired vector but is not needed as a theorem premise.

## Exact first unsupported line

For arbitrary connected graphs there is no analogue here of the exact tail law J_tail=(m/2+1)u-u^2. The dimension-independent spectral expectation of occupation-weighted matched-label and unmatched-row costs at one globally chosen feasible reference remains unpaid. Connectedness alone does not rescue uniform scaling; conversely uniform-scale growth does not establish growth of the infimum. NEXT must price those occupations across overlapping scales without relying on this special rare-tail identity or changing the posterior between separately charged terms.
