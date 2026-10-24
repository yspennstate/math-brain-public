# Four affine labels: a hereditary phase-energy terminal

All physical cubes are independent uniform cubes. Entropy is in bits. Identify the data cube with F2^n. For a real row u, E(u)=sum_i ||D_i u||_2^2; for Boolean functions this is total physical influence. The result concerns the FULL entropy and H(S_Y|S_X), with arbitrary spectral correlations.

## The class and result

Let C_t, indexed by t in F2^2, be disjoint affine physical cells partitioning Y; empty cells are allowed. On each nonempty C_t choose a quadratic F2 phase q_t. Let J0,A,B be X-frequency vectors, allowing dependence or zeros. Define

F(x,y)=sum_t chi_(J0+t1 A+t2 B)(x) 1_Ct(y) (-1)^q_t(y).

This is an actual Boolean sign because exactly one term is present at each y. Assume any desired integer X-degree bound d>=1 by requiring every occupied label to have size<=d. There is no constant depending on d, |X| or |Y|.

Every such function, and EVERY physical restriction of it, satisfies

H(S_Y|S_X)<=H(F)<=24 I_Y(F)<=24 I(F).

More precisely, if rank span(A,B) is2, full H<=4I_Y; if rank is1, full H<=24I_Y; if rank is0, full H<=kappa4 I_Y, where kappa4=16 h2(1/16)<11/2. These are complete terminal bounds, not per-query entropy-drop bounds or a reusable stopping budget.

Every fresh Boolean tensor factor of this hereditary class has F2 phase degree<=5. This guard is sharp in degree: the five-bit monomial phase is admitted, and the six-bit monomial phase is excluded. The previous arbitrary TWO-cell class had guard degree<=3; it is not claimed unchanged after this enlargement.

## 1. Restriction preserves the representation

A physical Y restriction intersects each affine cell with a coordinate hyperplane and restricts its quadratic phase, removing empty sections. The sections still partition the remaining Y cube. A physical X restriction projects each frequency vector onto the unqueried coordinates and introduces a sign chi_J(fixed x); since J=J0+t1 A+t2 B this is a constant sign for each cell and is absorbed into q_t's constant coefficient. Thus the same four-cell representation remains valid, although the projected A,B may lose rank.

There is no supposition that spectral coordinates are independent. There is no demand that merged row supports remain affine at rank1.

## 2. Rank2 and rank1 row accounting

Write E0 for sum of component energies in a row. A quadratic signed affine-cell component v of mass alpha=2^-k has uniform normalized Fourier spectrum on an affine coset. The polar-kernel calculation proves this: in the squared Fourier coefficient, differences outside the quadratic polar kernel cancel by a nontrivial character sum; the remaining sum is supported on an affine coset and has constant magnitude. If its dimension is s, entropy is s, and at least s spectral coordinates are fair. Hence alpha H(P_v)<=2E(v). Also alpha k<=2E(v), since at least k physical coordinate directions leave the affine support, each costing alpha/2. A single complete row bill alpha log2(1/alpha)+alpha H(P_v) is therefore<=4E(v).

For two DISJOINT components a,b, alpha=||a||^2, beta=||b||^2, mu=alpha+beta, let Q=(alpha P_a+beta P_b)/mu. Pointwise Cauchy gives P_(a+b)<=2Q. KL positivity and log(1/Q)>=0 imply H(P_(a+b))<=2H(Q). The exact grouping identity gives

mu H(P_(a+b))<=4E0+2mu h2(alpha/mu),
mu h2(alpha/mu)=alpha log2(1/alpha)+beta log2(1/beta)-mu log2(1/mu).

For nonparallel or unequal affine supports, E(a+b)>=E0/3. Indeed on each physical coordinate with a crossing, both components have boundary energy (alpha+beta)/2, and signed overlap is at most gamma=mass of their affine intersection after the shift. If unequal, dyadic masses give gamma<=min(alpha,beta)<=(alpha+beta)/3. If equal with different directions, gamma<=alpha/2. On noncrossing coordinates cross terms vanish. Thus the COMPLETE joint row bill is

mu log2(1/mu)+mu H(P_(a+b))<=8E0<=24E(a+b).

Parallel equal cells are the exception, NOT included in the energy comparison: they unite into one affine cell, with a cubic phase q0(z)+s(q0(z)+q1(z)). Tangent nonzero spectral inclusion probabilities are>=1/4 by the degree-two minimum-weight lemma below, while directions leaving the cell cost1/2. Subadditivity and codimension<=number of leaving directions give complete joint row bill<=4E(a+b). This also covers opposite component signs. Zero-mass components are simply omitted.

If rank(A,B)=2, each occupied label has one cell, so sum the rate4 bound. If rank is1, each fiber of t ->t1 A+t2 B has cardinality2, so every row is a signed sum of at most two cells. Apply the reconstructed two-cell estimate. In both cases the EXACT ledger is

H(F)=sum_J [w_J log2(1/w_J)+w_J H(P_uJ)],
I_Y(F)=sum_J E(u_J), w_J=||u_J||^2.

This proves the rank2 and rank1 bounds, retaining full conditional entropy and all row components on the same physical influence account. It is a reconstruction of A034 stage17, not an assumption of independent acceptance.

## 3. Four affine cells covering a cube have relative codimension<=3

For m<=4 nonempty cells, their dyadic masses sum to1. The only mass multisets are

m=1: (1);
m=2: (1/2,1/2);
m=3: (1/2,1/4,1/4);
m=4: (1/4,1/4,1/4,1/4) or (1/2,1/4,1/8,1/8).

For m=3, the largest dyadic mass is at least1/3, hence1/2; normalize the two remaining masses. For m=4, if every mass<=1/4 they must all equal1/4. Otherwise one is1/2; normalize the remaining three and use the preceding case. The m=2 case is immediate. Thus every cell is defined by at most3 independent affine equations. This uses the COMPLETE cover; it is false for a partial four-cell union, where arbitrarily small cells are possible.

## 4. Rank0 gluing has phase degree<=5

If rank(A,B)=0 all four terms share the same X character. Their data sum is a Boolean sign g on the entire data cube. An intrinsic quadratic q_t on C_t extends to an ambient quadratic Q_t: extend affine coordinates on its direction to linear coordinates on the whole cube. If C_t is cut out by r_t<=3 affine equations ell_tj=0, its F2 indicator is a_t=product_j(1+ell_tj), of degree<=r_t. The polynomial

Q=sum_t a_t Q_t over F2

agrees with q_t on each cell, since exactly one indicator is1. Hence g=(-1)^Q and deg Q<=5. All sums are finite; empty cells contribute zero.

For a nonzero F2 polynomial of degree r, uniform weight is>=2^-r. Induct on the last essential variable: the two sections differ by a nonzero degree-at-most-(r-1) polynomial; on every point where this difference is1 at least one section is1, giving the factor1/2. Constants give the base case. Derivatives of Q have degree<=4. Therefore each nonzero influence p_i of g is at least1/16; p_i=1 is allowed. Since h2(p)/p decreases for p>0 (its derivative is log2(1-p)/p^2),

H(g)<=sum_i h2(p_i)<=16 h2(1/16) sum_i p_i=kappa4 I(g).

Zero-influence coordinates contribute zero. The elementary -(1-p)ln(1-p)<=p gives h2(p)/p<=log2(1/p)+1/ln2. The positive atanh series gives ln2>2/3, so kappa4<4+3/2=11/2. No zero denominator is canceled, and the logarithmic arguments lie in(0,1] where used. This bounded F2-degree payment is the A033 baseline, applied here only after the affine complete-cover gluing has established its hypotheses.

With rank0 the X-frequency is deterministic, so H(F)=H(S_Y|S_X)=H(g), and I_Y(F)=I(g). This proves the missing all-four collision, with actual complete terminal costs and no reserve renewed. Combining ranks and restriction stability proves the theorem for every mixed physical restriction history.

## 5. Sharp degree guard, actual collision and controls

On data (t1,t2,t3,a,b), use the affine partition

C00={t1=0}, C01={t1=1,t2=0}, C10={t1=t2=1,t3=0}, C11={t1=t2=t3=1}.

Put phase1 on the first three cells and phase(-1)^(ab) on the last. With the four distinct X labels t in a two-dimensional plane, F is an actual Boolean degree-two-in-X function. Restricting both address characters to+1 merges ALL FOUR original components and gives g=(-1)^(t1 t2 t3 a b), whose unique F2 multilinear degree is5. Every opposite address branch only adds a cellwise constant phase, so all full terminals remain in the theorem. The one-collision guard degree3 therefore MUST be enlarged; it would be false here.

For a fresh Boolean tensor factor h(Z), fix all old X,Y inputs. The representation restricts to at most four affine cells covering Z, each with quadratic sign, so section4 proves deg_F2(h)<=5. The monomial phase on six bits has degree6 and is excluded. Arbitrary tensor factors cannot enter through hidden normalization or old-row signs.

Four NONPARALLEL cells already disprove blindly extending stage17's geometric E>=eta E0 to more components. On F2^3 take the four lines {0,1}, {2,4}, {3,7}, {5,6}. They are disjoint, cover the cube, and have distinct directions1,6,4,3. Give all cells phase+1. Their sum is constant and has energy0, while the sum of component energies is positive. The rank0 phase interpolation handles this cancellation exactly. This is an obstruction to a helper, NOT an FEI counterexample.

The three-bit point defect is covered by splitting its first bit and using two nonempty quadratic cells with rank0 labels; it retains its actual nonproduct spectrum. The generic normalized non-Boolean psi_N has H=log2 N,I=1 and violates24 for N>2^24. It fails the affine-cell unit-phase hypotheses. The entropy inequality is not being inferred from a generic probability law.

## First unsupported line

With a frequency affine space of rank3, a physical projection can leave rank1 and merge FOUR cells in a PROPER union that need not be affine and need not cover Y. The codimension<=3 complete-cover step then fails, and the four-line cancellation example forbids a uniform component-energy comparison without more structure. No rate24 theorem is proved for that proper-four-cell row. No bound on every physical query's entropy drop, prescribed-reference conversion, or universal C018/C019 budget follows from these terminal bounds. The next target is precisely that intermediate four-cell fiber, retaining the full conditional spectrum, signed cross terms and the same physical influence.
