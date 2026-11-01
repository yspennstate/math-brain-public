# Sharp binary affinity certificate for an actual ancestor budget

All logarithms are base2 unless ln is displayed. References are complete normalized probability laws and every CE is finite. This is a conditional C024/C019 payment theorem; full FEI remains OPEN.

## 1. Independent reconstruction of A096's geometric compression

Let P be the actual squared Fourier law of a Boolean function, with occupied support Omega. Suppose a finite complete adaptive physical query tree is isospectral at every queried node: for each frequency pair excluding the queried coordinate, at most one of the two Fourier coefficients is nonzero. Then each physical child coefficient is u+v or u-v, its square is u^2+v^2, and deletion maps occupied parent frequencies bijectively to occupied child frequencies with the same probabilities. Every queried erasure is exactly zero. Composing along a leaf l gives a probability-preserving bijection pi_l from Omega to that leaf's actual support. Physical leaf reach w_l=2^(-depth_l); early stopping is allowed and the reaches sum to1.

For each complete terminal target Q_l pull back its probabilities on occupied support: q_l(S)=Q_l(pi_l(S))>0. Its mass m_l=sum_Omega q_l is in(0,1]; the remainder is reference-only mass and MUST be priced. Put G(S)=product_l q_l(S)^(w_l), Z=sum G, Rstar=G/Z. Weighted AM-GM shows0<Z<=1. Direct expansion of CE gives

sum_l w_l CE(P_l,Q_l)=CE(P,Rstar)-log Z.

With arbitrary incoming complete Q0 the signed bill is

Delta=D(P||Rstar)-D(P||Q0)-log Z.                         (1)

Furthermore -log Z=sum_l w_l D((pi_l)_*Rstar||Q_l)>=0, by substituting log Rstar=log G-log Z and summing. Both full terminals, their reference-only masses and every earlier debit remain. If earlier booked costs are W and the ORIGINAL allowance is A, define its actual current unused amount U=A-W-CE(P,Q0). Affordability is exactly Delta<=U. This independently accepts A096's stage20 compression theorem unchanged; neither Rstar nor its influence price is freely supplied.

## 2. Exact binary factorization of the normalizer

Pull ALL references back to the SAME root alphabet Omega. At a leaf set R_l=q_l/m_l and Z_l=m_l. Recursively at a binary internal node v set

a_v=sum_S sqrt(R_left(S) R_right(S)),
R_v(S)=sqrt(R_left(S) R_right(S))/a_v,
Z_v=sqrt(Z_left Z_right)*a_v.                            (2)

All these quantities are positive because finite CE gives full positivity on Omega. Indeed the unnormalized subtree geometric mean is exactly Z_v R_v, by induction from the leaves; fair physical child weights supply the square roots even with unequal stopping depths. Therefore R_root=Rstar, Z_root=Z and

-log Z = sum_leaves w_l*(-log m_l)
         +sum_internal v w_v*(-log a_v).                (3)

Here w_v is actual physical reach, not a freshly normalized allocation. The first sum is the explicit reference-only/ghost penalty. The second is a sum of binary target-disagreement prices, weighted ONCE at their true physical nodes. This decomposition is a refinement of A096's retained normalizer, not its removal. Earlier refunds and original U are not renewed.

## 3. Sharp symbolic one-dimensional certificate

For any two probability laws p,q on a finite common alphabet, set M_i=(p_i+q_i)/2, t_i=(p_i-q_i)/(p_i+q_i) on nonzero denominator atoms, and

V(p,q)=sum_i M_i*t_i^2=(1/2)sum_i (p_i-q_i)^2/(p_i+q_i).

Atoms with p_i=q_i=0 contribute0. Normalization implies sum M_i=1 and sum M_i t_i=0. Their affinity is a=sum sqrt(p_i q_i)=sum M_i sqrt(1-t_i^2).

THEOREM. If t_i^2<=1/2 for every atom, then

V/(2 ln2) <= -log2 a <= V.                              (4)

The upper constant1 is SHARP on this stated domain; the lower constant1/(2 ln2) is sharp in the small-variation limit.

Proof, including the continuum exhaustiveness certificate. Put z=t_i^2 in[0,1/2] and c=2-sqrt2. Concavity of sqrt gives its endpoint chord

sqrt(1-z)>=1-c*z.

One can certify this without approximation by rationalizing: (1-sqrt(1-z))/z=1/(1+sqrt(1-z))<=1/(1+1/sqrt2)=c, with z=0 handled by continuity. Thus a>=1-c V. Since0<=V<=1/2, convexity of u -> -log2(1-c*u), whose endpoint values at0,1/2 are0,1/2, gives its upper chord

-log2(1-c V)<=V.

The endpoint value is EXACT: 1-c/2=1/sqrt2, hence -log2(1-c/2)=1/2. Combining monotonicity proves the upper half of(4). This is a symbolic certificate over the ENTIRE continuum, not a finite-grid inference.

For the lower half, sqrt(1-z)<=1-z/2 yields a<=1-V/2. Then -ln a>=1-a>=V/2. Dividing by ln2 proves the result. To verify sharpness, take a two-atom midpoint M=(1/2,1/2) and t=(eta,-eta). Then V=eta^2 and a=sqrt(1-eta^2). At eta=1/sqrt2 the upper ratio is EXACTLY1; as eta->0 the ratio tends1/(2 ln2), by differentiating -ln(1-z) at0. For any larger admissible squared radius z>1/2, the upper bound with constant1 fails on some such pair: -ln(1-z)/z is strictly increasing for z>0, since -ln(1-z)=integral_0^z (1-u)^(-1)du and its average increases. Thus the radius1/sqrt2 is also sharp. Rational negative control eta=3/4 gives cost>9/16; the exact sign is2^23>7^8.

EXHAUSTIVENESS THEOREM FOR THIS FINITE-TO-CONTINUUM BRIDGE. Every normalized finite binary reference pair is represented exactly by the M,t substitution above. When its stated atomwise bound holds, every t_i^2 lies in the FULL interval[0,1/2], covered by the two proved chord inequalities. Summing with probability weights preserves them for EVERY finite alphabet, regardless of dimension or atom count. Applying this theorem at every internal node of ANY finite physical tree proves the next section. Neither a bounded alphabet nor a bounded tree depth is an unstated assumption. The finitely executed fixtures validate the implementation and endpoints; they are not asserted exhaustive of all Boolean functions.

## 4. A dimension-free sufficient test at the SAME original account

For each fork in(2), assume its normalized child targets have relative discrepancy t_i^2<=1/2. Put B=sum_internal w_v V(R_left,R_right), and Gghost=sum_leaves w_l*(-log m_l). Combining(1),(3),(4) yields

D(P||Rstar)-D(P||Q0)+Gghost+B/(2 ln2)
 <= Delta <=
D(P||Rstar)-D(P||Q0)+Gghost+B.                          (5)

Thus the entirely explicit condition

D(P||Rstar)-D(P||Q0)+Gghost+B <= U                      (6)

pays ALL target conversions on the original allowance A, with all earlier W, the current root CE and both complete child/terminal costs retained. This is NOT a pathwise budget that may be reissued at descendants: B uses actual root reach weights and represents one transaction from the original source. Once booked, later work uses the reduced U. If root Rstar=Q0, the KL difference vanishes, but ghost and binary disagreement remain. Under that matching condition, Gghost+B<=U is sufficient, while Gghost+B/(2 ln2)<=U is necessary. Therefore the variance certificate controls the exact normalization bill within factor2 ln2, rather than ignoring it.

The root-KL term, the relative-discrepancy hypothesis and the budget premise are essential. Without a reference floor, arbitrarily small leaf probabilities can create arbitrarily large disagreement charges. No universal source price follows from(6).

## 5. Actual Boolean positive transaction with the old debit retained

Take the three-bit core g=-1 at truth indices0,7 and+1 elsewhere, with P uniform on{empty,12,13,23}. It has H=2,I=3/2. Replace each core bit by a disjoint parity block of length3, producing an actual nine-bit Boolean f. Its spectrum is the same four-atom law on the corresponding block unions and I(f)=9/2. Query the first two physical bits in the first block, retaining the complete depth2 tree. Each query occurs while that block still has at least two free bits; every queried erasure is zero and all four children have spectra related by the occupied-support bijections. The exact incoming reference Q0=P is matched, so query occupancy and calibration refunds are zero.

Label the four occupied root atoms by two signs z0,z1. At leaf outcomes s0,s1 in{-1,1}, prescribe the FULL reference, zero off transported support,

q_s(z0,z1)=(1+s0*eta*z0)(1+s1*eta*z1)/4.

For eta in[0,1), these normalize and stay finite on actual support. The subtree normalized geometric means are product laws; their two fork-level variances both equal eta^2. Hence B=2eta^2, Gghost=0, Rstar=P, Z=1-eta^2, and exact Delta=-log2(1-eta^2).

At rational eta=3/5, the original allowance A=3 and previously booked W=1/4 leave U=3/4 after current CE=2. Both full signed outcomes at EACH of the two physical queries and all four complete terminals are retained. Our certificate B=18/25<3/4 pays the positive conversion with reserve at least3/100. Exact actual Delta=2log2(5/4)<18/25; the variance estimate is conservative. This is a specified positive conversion in a genuine matched isospectral zero-refund history, paid from explicitly declared ORIGINAL unused surplus, not a new query refund. The allowance is SUPPLIED for this fixture; no arbitrary-seed rate is inferred and no intrinsic necessity of this particular target is claimed. The incoming A and booked W are specified account data; no preceding physical prefix realizing that old booking is constructed in this stage. The universal obligation to supply an eligible actual ancestor account is not discharged by this example.

## 6. First unsupported universal line and review scope

The condition(6) is a useful quantitative inherited-reference admission test, not a proof that any FEI invariant's required targets obey it. The missing universal step is an influence-priced initial source for arbitrary cores, OR a genuinely necessary, compatible target construction satisfying the bounded relative discrepancy, root-KL and actual original-budget premises at all histories. A085's arbitrary-depth parity embedding rules out finding fresh positive local query credit by merely searching deeper. This stage keeps that obstruction and A096's normalizer; it replaces no unpaid premise by a finite census or a status field. Independent review of the new certificate/payment corollary remains pending.
