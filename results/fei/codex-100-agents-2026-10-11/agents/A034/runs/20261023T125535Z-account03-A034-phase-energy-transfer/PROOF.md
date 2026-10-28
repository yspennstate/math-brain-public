# Mass-relative phase transfer and a common affine label carrier

Author proof, independent review pending. Uniform independent physical cubes X,Y, identified with F2 coordinate bits; all entropies in bits. D_i u=(u(y)-u(y+e_i))/2 and E(u)=sum_i ||D_i u||_2^2. No spectral independence is assumed.

## 1. Local row theorem without an affine completion

Let u=sum_{t=1}^s 1_{C_t}(-1)^{q_t} on a uniform physical Y cube, where C_t are nonempty DISJOINT affine cells, and each q_t is quadratic on its cell. The union may be proper and nonaffine; no affine completion is assumed. Put alpha=min_t P(C_t), mu=||u||_2^2=sum_t P(C_t), and R=mu/alpha. Then

mu H(P_u)<=[log2(R)+1+log2(e)] E(u),
mu log2(1/mu)+mu H(P_u)<=[log2(R)+3+log2(e)] E(u).

Here P_u(S)=uhat(S)^2/mu. In particular s EQUAL-MASS cells have R=s and complete coefficient log2(s)+3+log2(e), INDEPENDENT of their codimensions, dimension, relative directions or affine-completion size. Four equal-mass cells have full coefficient5+log2(e)<13/2 and conditional coefficient3+log2(e)<9/2. For cell mass ratio<=B one may use R<=sB. This closes the equal-mass part of the proper four-cell gap left in stage19.

Proof: write alpha=2^-K. Let a=1_{u!=0}, b=1_{u=-1}; as INTEGER functions u=a-2b. The F2 indicators of the cells have degree<=K. Extend intrinsic quadratic coordinates to the ambient cube; disjointness gives deg_F2(a)<=K and deg_F2(b)<=K+2. A nonzero F2 polynomial of degree r has weight>=2^-r: induct on an essential variable and use the nonzero difference of its sections, of degree<=r-1.

For any coordinate, if delta_i a is nonzero, it has degree<=K-1 and weight>=2^{-(K-1)}. On its support the row difference has squared magnitude1, so p_i=||D_i u||^2>=2^{-(K+1)}=alpha/2. If delta_i a vanishes identically, D_i u=-(b(y)-b(y+e_i)), hence any nonzero p_i equals the weight of delta_i b and is again>=alpha/2. The K=0 case has constant support and uses only the second argument.

Parseval gives the spectral inclusion probabilities p_i/mu. Entropy subadditivity gives mu H(P_u)<=sum_i mu h2(p_i/mu). For each nonzero p_i,

mu h2(p_i/mu)<=p_i log2(e mu/p_i)<=p_i log2(2e mu/alpha).

The first inequality uses -(1-z)ln(1-z)<=z. This proves the conditional statement. For the full bill, the support-indicator edge-isoperimetric inequality mu log2(1/mu)<=2E(a)<=2E(u) gives the extra2. To verify its normalization: sections of masses mu0,mu1 give excess mass entropy mu[1-h2(t)], where mu=(mu0+mu1)/2 and t=mu0/(mu0+mu1). The last-coordinate energy is at least |mu0-mu1|/4=mu|2t-1|/2; concavity h2(t)>=1-|2t-1| pays the excess with twice this energy. The other energies average over sections; zero mass is omitted. Thus every entropy term is paid from the SAME E(u).

The stage19 proof lost log2(mu) by replacing mu with1. Restoring it changes the loss from absolute codimension K to log2(mu/alpha). This is a genuine dimension-free row payment when the component masses are balanced, and a precise residual loss otherwise. No component-energy comparison or cancellation of signed cross terms is used.

## 2. Equal masses alone are not restriction-stable

On physical coordinates (s,u_1,...,u_r,v_1,...,v_r), take A={s=0,u=0} and B={s=1,v=0}, with phases+. They are disjoint and both have mass2^{-(r+1)}. Restricting all u=0 leaves A with mass1/2 and B with mass2^{-(r+1)}, so their mass ratio is2^r and R=2^r+1. The row u=1_A+1_B is realized in the actual Boolean degree-one-address sign F(x,y)=u(y)+chi_{1}(x)(1-u(y)); the completion is not a claim of a bounded phase partition. This is an exact family, not numerical evidence. It does not refute the entropy inequality (the old two-cell theorem still applies); it refutes automatic preservation of the balanced-mass HYPOTHESIS. We do not claim that the equal-mass row criterion alone is hereditary.

## 3. A concrete stable enlargement: common affine carrier

Let C_1,...,C_M be a complete disjoint affine partition of Y, with maximum codimension k, and let q_t be intrinsic quadratic phases. Let L:Y->F2^{|X|} be ANY common affine map and J_t ANY cellwise constant X labels, repetitions allowed. Define the actual Boolean sign

F(x,y)=sum_t 1_{C_t}(y) (-1)^{q_t(y)} chi_{L(y)+J_t}(x).

Every physical mixed restriction satisfies

H(S_Y|S_X)<=[k+log2(M)+1+log2(e)] I_Y(F),
H(F)<=[k+log2(M)+3+log2(e)] I_Y(F).

One may use the original bounds M,k after restriction, or tighter current bounds. These constants depend on the phase partition only, NOT on the rank of L, the number of nonempty X-frequency labels, dimension, or an optional occupied-label X-degree cap d>=1. Since k<=M-1, eight phase cells give full coefficient13+log2(e)<29/2. If L=0, stage19's tighter coefficient k+3+log2(e) remains available; the new bound does not replace that sharper subcase.

Proof of row masses: let the current affine map L have rank r. Every nonempty fiber L(y)=z has mass2^-r. A row J is a union, over t, of the affine intersections C_t cap {L=J+J_t}. A nonempty intersection is a fiber restricted by at most k further independent equations, hence has mass>=2^{-(r+k)}. There are at most M pieces, each of mass<=2^-r, so the row's R=mu/alpha is at most M 2^k. Apply section1 to each row, then sum the exact identities

H(F)=sum_J [mu_J log2(1/mu_J)+mu_J H(P_uJ)],
H(S_Y|S_X)=sum_J mu_J H(P_uJ),  I_Y(F)=sum_J E(u_J).

The labels may have unbounded cardinality; none has been discarded or charged a new account. Constant labels at L=0 recover the prior geometry.

## 4. Physical restriction closure and tensor guard

A physical Y restriction intersects C_t with a coordinate slice; nonempty cells still partition the remaining cube and their relative codimension cannot increase. Quadratics and affine maps restrict with the same degrees. A physical X restriction projects L and J_t, and multiplies each cell's phase by chi_{L(y)+J_t}(fixed x). This adds an affine-in-y polynomial to q_t, preserving its quadratic degree. Thus the common-carrier form survives ALL physical restriction histories. Spectral auxiliaries remain freely correlated.

For a fresh Boolean data tensor factor h(Z), fix all old X,Y. What remains is a partition of Z with cell codimension<=k and quadratic phase: the fixed-X carrier contributes only an affine phase. Therefore the negative bit of h has F2 degree<=k+2. For a phase partition of at most M cells, k<=M-1 and deg_F2 h<=M+1. This excludes arbitrary Boolean tensor factors in each fixed-M or fixed-k class, independently of carrier rank. For completeness, prove the partition-size bound by induction on the number m of nonempty dyadic masses summing to1. The sole-cell exponent is0. If the largest denominator exponent K is positive, the number of terms2^-K is even by clearing the denominator, so merge two such terms into2^{-(K-1)}. If any exponent K remains, induction on the new m-1 terms gives K<=m-2; otherwise the merged exponent gives K-1<=m-2. In both cases K<=m-1<=M-1. The nested M-cell partition with a final quadratic phase attains degree M+1, so the guard is sharp. For eight cells degree9 is admitted and degree10 is excluded.

The three-bit point defect is admitted with L=0 and two quadratic cells, so the vacuous-embedding control passes. Normalized non-Boolean psi_N=sum_i y_i/sqrt(N) has H=log2 N and I=1, violating any fixed-M rate for large N; it fails the unit-phase/ternary-row hypothesis. Arbitrary correlated physical input laws are not included.

## 5. Unbounded carrier rank is substantive

On Y=(t,z_1,...,z_r,a,b), X=(x_0,x_1,...,x_r), let

F=(-1)^{x_0 t + sum_{j=1}^r x_j z_j + t a b}.

There are only TWO phase cells t=0 and t=1, with phases0 and ab. The common carrier is L=(0,z_1,...,z_r), with offsets J_t=(t,0,...,0). Nevertheless all2^{r+1} X-frequency rows are nonempty. The new fixed-phase-partition constant is independent of r, and all physical restrictions remain in the class. Thus this is not merely the old at-most-eight-total-cells theorem with renamed cells. Optional d may vary with the family; the theorem is uniform in any degree cap actually satisfied.

## Exact first unsupported line

For arbitrary four disjoint signed quadratic affine cells with unbounded mass disparity and without a common-carrier bounded-phase-partition source, log2(mu/alpha_min) remains unbounded. No argument here replaces it by an absolute constant. The equal-mass condition is not automatically stable, as section2 proves. The common-carrier theorem is a concrete stable restricted result, not a universal source/erasure/history conversion. Removing the mass-disparity loss for those four-cell rows, while preserving full terminal entropy and the SAME physical influence, is the next gap. Full FEI remains OPEN.
