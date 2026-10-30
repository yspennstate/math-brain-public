# Affine-partition collision payment, version 2

Uniform independent physical cubes X,Y; entropy in bits. Write D_i u=(u(y)-u(y+e_i))/2 and E(u)=sum_i ||D_i u||_2^2. All spectral auxiliary coordinates may be correlated.

## Exact theorem

Let C_1,...,C_m be nonempty disjoint affine subsets partitioning F2^n. Their maximum codimension is k. Let q_t be quadratic F2 phases on C_t, and let J_t be ANY X-frequency labels, including repeated labels. Then the actual Boolean function

F(x,y)=sum_t chi_{J_t}(x) 1_{C_t}(y) (-1)^{q_t(y)}

satisfies, at every physical X/Y restriction,

H(S_Y|S_X) <= H(F) <= (k+3+log2(e)) I_Y(F) <= (k+9/2) I_Y(F).

Here k may be the original maximum codimension: restrictions never increase it. Equivalently one may use the current maximum codimension. A complete partition into at most m cells has k<=m-1, so H(F)<=(m+7/2) I_Y(F). In particular EIGHT cells, with completely arbitrary labels, have full entropy <=(23/2) I_Y at every restriction. The actual coefficient is10+log2(e)<23/2. FOUR cells have coefficient6+log2(e)<15/2, improving the former rate24 while retaining its full entropy and all histories. Bounds with the larger rational coefficients are strict only when I_Y>0. No X-degree enters the constant: any optional integer X-degree cap d>=1 on occupied labels is retained.

The proof below is self-contained, including the previous unsupported proper four-cell fiber. It does not compare component energies to collided energy.

## 1. Two polynomial bits encode a collided row

Fix any current label J and write its real row u=sum_{t:J_t=J} 1_{C_t}(-1)^{q_t}. Thus u takes values0,+1,-1. Its support bit is a=1_{u!=0}; its negative bit is b=1_{u=-1}. As INTEGER-valued functions, u=a-2b.

An affine cell of codimension r<=k has F2 indicator A_t equal to a product of r affine equations (with the appropriate constants). Extend the intrinsic quadratic q_t to an ambient quadratic Q_t by extending affine coordinates. Disjointness gives the F2 identities

a=sum_{t:J_t=J} A_t,   b=sum_{t:J_t=J} A_t Q_t.

Consequently deg_F2(a)<=k and deg_F2(b)<=k+2. Outside the row support both bits vanish. This last fact is essential: b is the negative bit, rather than an arbitrary ambient phase.

## 2. Nonzero row influence has an absolute gap

A nonzero F2 polynomial of degree r has uniform weight at least2^-r. Proof: induct on an essential variable. Its two sections differ by a nonzero polynomial of degree<=r-1; above each point of difference at least one section is1. Constants supply the base case. Directional differences lower degree by one.

Fix a physical coordinate i. If delta_i a=a(y)+a(y+e_i) is nonzero, its weight is at least2^{-(k-1)}. At every such point exactly one row value is zero, so (u(y)-u(y+e_i))^2=1. Hence ||D_i u||^2>=2^{-(k+1)}. This case is impossible when k=0.

If delta_i a is identically zero, the integer difference of a vanishes. Then D_i u=-(b(y)-b(y+e_i)); its squared norm equals the weight of delta_i b. Whenever it is nonzero, degree(delta_i b)<=k+1 gives the SAME lower bound2^{-(k+1)}. Therefore every row influence p_i=||D_i u||^2 is either0 or at least epsilon=2^{-(k+1)}. This includes arbitrary signed interference among all components.

## 3. Full conditional spectral entropy payment

Let mu=||u||^2>0 and let P_u(S)=uhat(S)^2/mu. Its coordinate inclusion probabilities are p_i/mu, by Parseval. Shannon entropy subadditivity, without any independence hypothesis, gives

mu H(P_u)<=sum_i mu h2(p_i/mu).

For 0<p<=1, h2(p)<=p log2(e/p), since -(1-p)ln(1-p)<=p. As mu<=1 and nonzero p_i>=epsilon,

mu h2(p_i/mu)<=p_i log2(e mu/p_i)<=(k+1+log2(e)) p_i.

Thus mu H(P_u)<=(k+1+log2(e)) E(u). No entropy term has been dropped or conditioned away.

## 4. The mass entropy is paid on the same account

For any indicator a of mass mu on a uniform cube, the edge-isoperimetric entropy inequality is mu log2(1/mu)<=2E(a). Here is an induction to fix all factors. With last-coordinate sections of masses mu0,mu1, put mu=(mu0+mu1)/2 and t=mu0/(mu0+mu1). The mass-entropy excess above the average section mass-entropies is mu[1-h2(t)]. The last-coordinate energy is at least |mu0-mu1|/4=mu|2t-1|/2. Concavity gives h2(t)>=1-|2t-1|. Twice that energy therefore pays the excess; the other energies average over sections. Zero mass and dimension zero have zero bills.

For the support a of u, E(a)<=E(u) pointwise in squared differences. Thus the COMPLETE row bill satisfies

mu log2(1/mu)+mu H(P_u)<=(k+3+log2(e)) E(u).

Summing rows uses EXACT identities

H(F)=sum_J [mu_J log2(1/mu_J)+mu_J H(P_uJ)],
H(S_Y|S_X)=sum_J mu_J H(P_uJ),   I_Y(F)=sum_J E(u_J).

This proves the theorem. The conditional bound alone has the stronger coefficient k+1+log2(e). The full bound consumes each row's original physical energy once, with coefficient k+3+log2(e). It is a complete terminal inequality, NOT a renewable per-query reserve or an erasure inequality. Finally ln2>2/3 by the positive atanh series, so log2(e)<3/2.

## 5. Partition size, restriction stability, and tensor guard

The cell masses are dyadic powers summing to1. In any list of m such masses the largest denominator exponent K is at most m-1. Induct on m: if K>0 at least two masses2^-K occur, since the denominator-cleared sum is even. Merge two of them into2^{-(K-1)}. If another exponent K remains, induction yields K<=m-2; otherwise induction yields K-1<=m-2. The sole-cell case has exponent0.

A physical Y restriction intersects cells with a coordinate slice, retaining disjointness and complete cover. Relative codimension cannot increase: restriction of r affine equations still has rank<=r. Quadratic phases restrict to quadratics. A physical X restriction projects labels and adds cellwise constant signs, absorbed in q_t. Consequently every subsequent collided row still has the two polynomial bits of section1, with the SAME k bound. There is no restriction on how many labels collide.

For any fresh Boolean tensor factor h(Z) admitted to a fixed-k class, fix all old X,Y. The remaining cell partition on Z has codimension<=k, and its negative bit has degree<=k+2 by section1. Hence deg_F2(h)<=k+2. Arbitrary Boolean tensor factors are excluded for fixed k. For at most m cells the bound is m+1, and is sharp: take a nested partition with m-1 successive tests; put phase+ on the first m-1 cells and quadratic phase(-1)^(ab) on the last. After all X signs are fixed+, the phase is the monomial on m+1 bits. Thus for eight cells degree9 is admitted but degree10 is excluded; the former FOUR-cell degree5 guard remains valid in that smaller class.

The three-bit point defect is admitted by a two-cell quadratic partition, so its nonproduct spectrum is included. Normalized non-Boolean psi_N=sum_i y_i/sqrt(N) has H=log2 N and I=1, violating every fixed-k rate when N is large. It fails the unit-phase/disjoint-cell hypothesis. No correlated physical input law is used.

## 6. A genuinely unpaid four-cell geometry now covered

On t1,...,t7 take C_j={t1=...=tj=1,t_(j+1)=0} for0<=j<=6, and C_7={t1=...=t7=1}; add free a,b. Assign X labels J_j=j in F2^3. Put q_7=ab and all other q_j=0. Fix the upper two X coordinates+, retaining the low bit. One row is C0 union C2 union C4 union C6, of mass85/128; the other has mass43/128. Both masses have binary popcount4. A DISJOINT union of at most two affine cells has mass equal to a sum of at most two dyadic powers and therefore binary popcount<=2. Neither row can coarsen into two disjoint signed affine components; their supports are proper and nonaffine. The old complete-cover gluing and two-cell proof cannot pay these rows directly. Sections1-4 now pay BOTH full terminal rows from their actual I_Y, at coefficient<23/2. All signs, conditional spectral entropy, and signed physical cross terms are retained.

## Exact first unsupported line

The fixed-k (or fixed-m) theorem does not provide a dimension-independent constant for partitions of unbounded codimension and unbounded size. An arbitrary Boolean data sign has an affine singleton partition, with k=n, so removing k-dependence from this statement would itself imply full FEI. No cancellation-sensitive replacement for the absolute derivative gap epsilon=2^{-(k+1)} is proved. Nor is a same-account history/reference conversion proved merely by terminal bounds. Full FEI remains OPEN.
