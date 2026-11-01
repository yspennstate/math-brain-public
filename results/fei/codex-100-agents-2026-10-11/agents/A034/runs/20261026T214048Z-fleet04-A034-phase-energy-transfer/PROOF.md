# Arbitrary mass scales and cell-dependent affine carriers

Author proof, independent reconstruction pending. This strengthens the existing phase-row candidate; full FEI remains OPEN. All cubes are independent uniform physical cubes, and entropy is in bits. Write D_i u=(u(y)-u(y+e_i))/2 and E(u)=sum_i ||D_i u||_2^2. Define B(u)=sum_T uhat(T)^2 log2(1/uhat(T)^2), with zero terms omitted. For a ternary row of mass mu, B(u)=mu H(P_u)+mu log2(1/mu).

## 1. Target and constant

For every integer s>=1, every dimension n, and every row u=sum_{t=1}^s 1_{A_t}(-1)^{q_t}, where the nonempty A_t are pairwise disjoint affine physical cells and q_t is quadratic on its cell, set

K_s=2s[log2(s)+(s-1)log2(64s^2)+3+log2(e)].

Then B(u)<=K_s E(u), and therefore mu H(P_u)<=K_s E(u). The union of the cells may be proper and nonaffine. Cell codimensions and mass ratios are unrestricted. For at most four cells one can use K_4=280+8log2(e)<292. This is a loose bound: the sharper previous equal-mass and two-cell bounds remain valid.

## 2. Two previously used facts, reconstructed

For a group v of disjoint quadratic affine cells of minimum mass alpha=2^-k, let a=1_{v!=0} and b=1_{v=-1}. Over F2, deg(a)<=k and deg(b)<=k+2: affine-cell indicators have degree equal to codimension and intrinsic quadratics extend to ambient quadratics; disjointness makes addition of the negative bits exact. A nonzero F2 polynomial of degree r has weight at least 2^-r, by induction using a nonzero coordinate derivative.

Consequently every nonzero p_i=||D_i v||^2 is at least alpha/2. If delta_i a!=0 its degree is at most k-1, and each support-boundary point contributes 1/4 to p_i. If delta_i a=0, then D_i v=-(b(y)-b(y+e_i)) and p_i is exactly the weight of delta_i b, whose degree is at most k+1. The k=0 case uses the second argument. Also p_i<=||v||^2=mu, since D_i is an orthogonal projection in L2.

Entropy subadditivity and h2(z)<=z log2(e/z) give

mu H(P_v)<=sum_i p_i log2(e mu/p_i)<=[log2(mu/alpha)+1+log2(e)]E(v).

The support edge-isoperimetric inequality mu log2(1/mu)<=2 E(a)<=2 E(v) therefore gives

B(v)<=[log2(mu/alpha)+3+log2(e)]E(v).                    (1)

For completeness the support inequality follows by induction on coordinates. Section masses mu0,mu1, with mu=(mu0+mu1)/2 and t=mu0/(mu0+mu1), leave mass-entropy excess mu[1-h2(t)]. The last-coordinate energy of a is at least |mu0-mu1|/4. Concavity h2(t)>=1-|2t-1| pays the excess with twice that energy. Other energies average. Empty sections have zero contribution.

## 3. Cluster the masses, not the Fourier coordinates

Sort the s cell masses in decreasing order and put R=64s^2. Split into consecutive groups whenever the ratio of consecutive masses is greater than R; equality stays in the same group. Let v_1,...,v_q be the grouped rows, q<=s. Within each group max(alpha_t)/min(alpha_t)<=R^(s-1), so mu_g/alpha_g<=s R^(s-1). Equation (1) gives

B(v_g)<=L_s E(v_g),  L_s=log2(s)+(s-1)log2(R)+3+log2(e). (2)

We now prove E(u)>=1/2 sum_g E(v_g), despite arbitrary signed cancellation inside and between groups. Fix coordinate i. If all group derivatives vanish this is immediate. Otherwise let g be the first group with e_g=||D_i v_g||^2>0 and let beta be that group's smallest cell mass. Then e_g>=beta/2. Every cell in later groups has mass <beta/R, so their total mass is at most s beta/R. Earlier derivatives vanish. If T=sum_{h>g} sqrt(e_h), Cauchy--Schwarz and e_h<=mu_h imply

T^2<=s sum_{h>g}e_h<=s^2 beta/R=beta/64<=e_g/32.

Thus T<=sqrt(e_g)/4 (we deliberately weaken 1/sqrt(32) to 1/4). Reverse triangle gives ||D_i u||^2>=(sqrt(e_g)-T)^2>=9e_g/16. Also

sum_h e_h<=e_g+s beta/R<=e_g(1+2s/R)<=33e_g/32.

Hence ||D_i u||^2>= (6/11)sum_h e_h>=1/2 sum_h e_h. Sum over i. This comparison is for the mass GROUPS, not the original cells. Equal-scale cancellation is retained inside each group. In particular a constant complete cover creates one group and does not contradict this argument.

## 4. Keep the entire coherent entropy bill

The group rows have disjoint physical supports. Write mu=sum_g ||v_g||^2=||u||^2<=1. For mu>0 put P(T)=uhat(T)^2/mu and Q(T)=sum_g vhat_g(T)^2/mu. Both are probability laws and P<=q Q by Cauchy--Schwarz. Gibbs' inequality and -log2 Q>=0 imply

H(P)<=sum_T P(T)log2(1/Q(T))<=q H(Q).

Mixture entropy, with weights mu_g/mu, then gives

B(u)<=q[mu H(Q)+mu log2(1/mu)]<=q sum_g B(v_g).

All zero coordinates are omitted, and P>0 implies Q>0, so no invalid logarithm occurs. Equations (2) and section3 yield B(u)<=2q L_s E(u)<=K_s E(u). If mu=0 the row vanishes and the inequality is exact. If E(u)=0 the same argument forces B(u)=0. This proves section1 without a bound on absolute codimension or mass disparity.

## 5. Stable enlargement: DIFFERENT affine carriers in different cells

Partition Y into at most M nonempty affine cells C_t. On C_t choose an intrinsic quadratic q_t and an arbitrary affine label map L_t:Y->F2^|X| (an intrinsic affine map also extends). There is NO common-linear-part or equal-rank assumption. Define the actual Boolean sign

F(x,y)=sum_t 1_{C_t}(y)(-1)^{q_t(y)+x dot L_t(y)}.

Optionally require that every occupied X label has Hamming weight at most any chosen integer d>=1; the theorem is uniform in d. For every physical mixed restriction,

H(F)<=K_M I_Y(F),  H(S_Y|S_X)<=K_M I_Y(F).

Indeed the X-frequency row J consists of at most M affine intersections C_t intersect {L_t=J}, with disjoint physical supports and quadratic phases. Their ranks, masses and directions can all differ. Apply section1, then use the exact identities H(F)=sum_J B(u_J), H(S_Y|S_X)=sum_J mu_J H(P_uJ), and I_Y(F)=sum_J E(u_J). These are identities for the SAME original function, not fresh influence credits.

Fixing a physical X coordinate projects each L_t and adds an affine phase to q_t; fixing Y coordinates intersects the phase cells and restricts their affine maps and quadratics. Thus the class is closed under every physical restriction history, with the original M as a valid bound. Correlations between spectral coordinates are unrestricted. Arbitrarily correlated physical input laws are excluded.

The tensor guard remains deg_F2(h)<=M+1 for any fresh Boolean Y-factor h of an admitted function. Fix all old coordinates, including X. The remaining negative bit is a sum of at most M cell indicators times quadratic bits. Any complete dyadic partition into m<=M cells has maximal codimension <=m-1: merge two smallest equal masses, which exist by parity after clearing the largest denominator, and induct. Therefore deg(h)<=M+1. This excludes, for example, the AND_(M+2) phase. It does not exclude every tensor product, nor should it; it excludes arbitrary Boolean factors in each fixed-M class.

This is a strict enlargement of the common-carrier representation at the supplied phase partition: on two halfcubes t=0,1, use L_0=0 and L_1(z)=z in r output coordinates. The zero-frequency row contains masses 1/2 and 2^-(r+1), so its ratio is 2^r, while M=2 stays fixed. This violates the old common-carrier mass-ratio conclusion at k=1; its full row bill is now paid independent of r. No claim of representation-minimality is needed.

The actual three-bit point defect is admitted by two phase cells (fix one bit, with the remaining negative bit quadratic). The normalized non-Boolean psi_N=sum_i y_i/sqrt(N) has H=log2(N), E=1, and fails any fixed K_M for large N. It is not a signed disjoint-cell ternary row. Thus the inequality uses a Booleanity admission and passes the vacuous-embedding guard.

### A useful elementary bound for the complete carrier source

For this COMPLETE source class one can also use H(F)<=2^(M+1) I_Y(F) and H(S_Y|S_X)<=2^M I_Y(F), so the better full coefficient is min(K_M,2^(M+1)). In particular M=4 has full rate32, while the proper FOUR-cell ROW theorem above has rate below292. These are different hypotheses, not competing values of one constant.

Indeed the global phase bit p(x,y) is the F2 sum over cells of 1_Ct(y)[q_t(y)+x dot L_t(y)], hence has degree at most(M-1)+2=M+1. Every essential physical Y coordinate has influence equal to the nonzero weight of delta_i p, at least2^-M. If N is the number of such coordinates, N<=2^M I_Y. For each fixed y the X function is a single signed character. Therefore the X spectral marginal is exactly the law of the deterministic label map L(Y), which depends only on those N essential coordinates; H(S_X)<=H(Y_active)=N. The conditional Y spectral law is supported on subsets of the same N coordinates, hence H(S_Y|S_X)<=N. Sum the two estimates. If N=0, F is a signed X character and both entropies vanish. This is the bounded-phase-degree mechanism credited to A033, applied to a linear-in-X source, rather than another claim about arbitrary proper rows. Its exponential dependence is better for small M; K_M is polynomial in M and eventually better.

## 6. Remaining universal gap

There is no uniform bound here when the number of disjoint quadratic pieces per row grows. Every Boolean function has a singleton-cell representation, with M potentially 2^n, so K_M does not prove FEI. Nor is there a proved influence-priced decomposition of an arbitrary core into bounded-M cell-dependent affine-carrier sources. The next unpaid line is such a decomposition or a cancellation argument whose cost is independent of the row piece count. Independent review of the new grouped-energy and coherent-entropy steps is still required.
