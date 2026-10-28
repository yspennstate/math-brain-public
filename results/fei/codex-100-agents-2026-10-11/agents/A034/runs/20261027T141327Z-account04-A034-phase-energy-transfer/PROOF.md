# Signed scalar entropy and a linear piece-count transfer

Author proof; independent review pending. This strengthens A034-AFFINE-PLANE-HEREDITARY-PHASE@4, not full FEI. Physical X,Y are disjoint independent uniform cubes. Entropies are in bits unless expressly marked natural. A ternary row is u=sum_t 1_At (-1)^qt for disjoint nonempty affine physical cells with intrinsic quadratic phases. Write E(u)=sum_i ||(u(y)-u(y+e_i))/2||_2^2 and B(u)=sum_T uhat(T)^2 log2(1/uhat(T)^2). If mu=||u||^2, B(u)=mu H(P_u)+mu log2(1/mu); no terminal or conditional entropy is dropped.

## 1. Scalar entropy estimate: the new step

Put F(z)=-z ln z on [0,1], with F(0)=0, and phi(t)=sqrt(F(t^2)) for 0<=t<=1. For ANY finite real tuple (a_j) with sum_j |a_j|<=1,

phi(|sum_j a_j|)<=sqrt(2) sum_j phi(|a_j|).                 (S)

If sum_j |a_j|<=1/2 the factor sqrt(2) can be replaced by1. The factor sqrt(2) in (S) cannot be reduced uniformly.

Proof. Set c=exp(-1/2), so phi is increasing on [0,c], decreasing on [c,1], max phi=c, and phi(t)/t=sqrt(-2 ln t) is decreasing for t>0. If every b_j=|a_j|<=c, let L=sum b_j. When L<=c, monotonicity and the decreasing ratio give phi(|sum a_j|)<=phi(L)<=sum phi(b_j). When L>=c, phi(b_j)>=b_j (because -2 ln b_j>=1), hence sum phi(b_j)>=L>=c>=phi(|sum a_j|).

Otherwise exactly one magnitude a exceeds c. Its tail has absolute sum <=1-a; put t=|sum a_j|. If a=1 then all others vanish and both sides are zero. Assume c<a<1. Since c>1/2, t>=2a-1>=0. Thus

t^2 >= (2a-1)^2 >= 2a^2-1,

where the second difference is exactly2(a-1)^2. If t>=a, then t^2>=a^2>1/e and F(t^2)<=F(a^2), since F decreases on [1/e,1]. If t<a, put lambda=(1-a^2)/(1-t^2). Both denominators are positive and 1/2<=lambda<=1. The identity a^2=lambda t^2+(1-lambda)*1 and concavity of F give F(a^2)>=lambda F(t^2), hence F(t^2)<=2 F(a^2). This proves (S), even using only the largest summand on its right.

For L<=1/2<c, the first case gives factor1. For sharpness take a_1=1-epsilon,a_2=-epsilon. As epsilon decreases to0, F((1-2epsilon)^2)~4epsilon, F((1-epsilon)^2)~2epsilon and F(epsilon^2)=o(epsilon). The squared ratio in (S) tends to2. This is a scalar sharpness statement, not a Boolean FEI counterfamily. Taylor remainders can be avoided by -ln(1-z)/z->1, following directly from1<=-ln(1-z)/z<=1/(1-z).

## 2. Consequence for coherent signed physical pieces

Let v_g be disjoint ternary physical rows and u=sum_g v_g. For each Fourier coordinate T,

sum_g |vhat_g(T)|<=sum_g E|v_g|=sum_g ||v_g||^2=mu<=1.

Apply (S) coordinatewise, then the finite Euclidean triangle inequality to the nonnegative vectors phi(|vhat_g(T)|). Dividing out ln2 yields

sqrt(B(u))<=sqrt(2) sum_g sqrt(B(v_g)),
B(u)<=2 (sum_g sqrt(B(v_g)))^2.                           (C)

If mu<=1/2, use factor1 instead of2 in the squared version. No normalization by a tiny row mass is made, and B already includes mu log2(1/mu). Zero coefficients are treated continuously. The estimate is generic as a scalar tool; the final influence theorem uses the Boolean affine-quadratic derivative gap below. Unlike stage21's q-fold Gibbs bound, (C) has no number-of-groups factor before the square-root sum.

## 3. Reconstruct the derivative and mass-group estimates

For a quadratic affine group v whose smallest cell has mass alpha=2^-k, put a=1_{v!=0} and b=1_{v=-1}. F2 degrees satisfy deg a<=k and deg b<=k+2. This follows by extending intrinsic quadratic coordinates to the ambient cube and summing disjoint cell indicators. The minimum-weight induction says a nonzero F2 polynomial of degree r has weight>=2^-r.

For coordinate i, if delta_i a is nonzero, it has degree<=k-1; boundary points give squared row difference1, so ||D_i v||^2>=alpha/2. If delta_i a is zero, D_i v=-(b(y)-b(y+e_i)), and nonzero energy equals the weight of delta_i b, whose degree<=k+1. The k=0 case uses the second argument. Also ||D_i v||^2<=mu_v. Thus every nonzero coordinate energy is >=alpha/2.

Entropy subadditivity and h2(z)<=z log2(e/z), together with support isoperimetry mu_v log2(1/mu_v)<=2 E(v), give

B(v)<=[log2(mu_v/alpha)+C] E(v), C=3+log2(e).             (R)

The support inequality is normalized as follows. Section masses mu0,mu1 leave excess mu[1-h2(t)] over the average section mass entropy, where mu=(mu0+mu1)/2 and t=mu0/(mu0+mu1). The last-coordinate support energy is at least |mu0-mu1|/4. Concavity h2(t)>=1-|2t-1| pays the excess with twice that energy. Other energies average, giving induction. Empty sections are zero. Since support edges cost no more than signed row edges, the same E(v) pays (R).

Now let s be the number of original pieces, R_s=64s^2. Sort cell masses decreasingly and split whenever adjacent ratio>R_s. The q groups have sizes m_g, sum m_g=s. Their complete bills obey

B(v_g)<=L_g E(v_g), L_g=log2(m_g)+(m_g-1)log2(R_s)+C.    (G)

For each coordinate choose the FIRST group with positive energy e_g, or treat the all-zero case separately. If beta is its minimum cell mass, e_g>=beta/2 and all later cells have mass<beta/R_s. Their total mass is <=s beta/R_s. Cauchy--Schwarz gives (sum_{h>g} sqrt(e_h))^2<=s^2 beta/R_s=beta/64<=e_g/32. In particular the tail norm<=sqrt(e_g)/4, so reverse triangle gives e_total>=9e_g/16. Meanwhile sum_h e_h<=e_g(1+2s/R_s)<=33e_g/32. Therefore

E(u)>=(6/11) sum_g E(v_g).                               (E)

This compares GROUPS, never individual cells; a constant full two-cell cover still refutes ungrouped component-energy domination. Equal-mass cancellation stays inside a group. Earlier zero derivatives contribute nothing. The inequalities before squaring have nonnegative right sides. This reconstructs stage21's stronger6/11 factor instead of discarding it for1/2.

## 4. Linear piece-count theorem

Let s>=2, A_s=1+log2(64s^2), L_s=log2(s)+(s-1)log2(64s^2)+C, and

J_s=(s-2) A_s+2C,
K_s=max{L_s,(11/3)J_s},
K_s^rare=max{L_s,(11/6)J_s}.

Then every row of at most s disjoint affine quadratic pieces satisfies B(u)<=K_s E(u). If its support mass mu<=1/2, B(u)<=K_s^rare E(u). Empty rows are zero. A single piece has the direct bound C E(u). Both full conditional entropy and row-mass entropy are retained. The constants are O(s log s), rather than stage21's O(s^2 log s).

Proof: if q=1, (G) gives B(u)<=L_s E(u) directly. If q>=2, combine (C), (G), weighted Cauchy--Schwarz and (E):

B(u)<=2 [sum_g L_g][sum_g E(v_g)]<=(11/3)[sum_g L_g]E(u).

No division by L_g or E(v_g) is needed. Because log2(m)<=m-1 for positive integers m,

sum_g L_g <= (s-q) A_s+q C <= (s-2) A_s+2C=J_s.

The last inequality uses A_s>=9>C for s>=2. The rare-row version replaces factor2 by1. At s=4, L_4=35+log2(e)<36.5 and J_4=28+2log2(e)<31. Consequently K_4<341/3<114 and K_4^rare<341/6<57. At most four pieces is covered as the displayed rates are increasing for s>=2; the single-piece bound is smaller. Previous balanced proper-row rate<6.5 and complete four-phase-cell source rate32 remain available on their sharper domains. The new proper-row rate<114 replaces the previous general<292 because the coherent-entropy method has improved, not because of a change of units or dropped terms.

## 5. Stable restricted Boolean consequence and guards

On at most M complete affine physical Y phase cells C_t, take intrinsic quadratic q_t and arbitrary individual affine label maps L_t:Y->F2^|X|. The actual Boolean sign is F(x,y)=sum_t 1_Ct(y)(-1)^{q_t(y)+x dot L_t(y)}. Optional occupied X-label degree<=d is allowed for any integer d>=1; no estimate depends on d. Each X-frequency row has <=M affine quadratic intersections. Sum B(u_J) and E(u_J) to obtain exactly H(F)<=K_M I_Y(F) and H(S_Y|S_X)<=K_M I_Y(F), using the direct single-piece bound if M=1. An individual rare row has the stronger coefficient above. No assumption of spectral-coordinate independence is used.

Physical Y restrictions intersect cells and restrict their maps/phases; X restrictions project each label map and add an affine Y phase. Thus all physical restriction histories retain the same M and full entropy payment. The previous complete-source rate2^(M+1), and conditional rate2^M, remain valid: global phase degree<=M+1 gives each essential Y coordinate influence>=2^-M; label entropy and conditional set entropy are each at most the number of essential Y coordinates. Use the better of that source rate and K_M. The source's M4 rate32 is unchanged, and must not be confused with proper-row114 or rare proper-row57.

Fixing old coordinates shows any fresh Boolean data tensor factor in a fixed-M source has F2 phase degree<=M+1, since any complete dyadic partition into M cells has maximal codimension<=M-1. The latter follows by merging a pair of smallest equal masses and induction; their multiplicity is even after clearing denominators. Therefore AND_(M+2) phase is excluded. For the three-bit point defect use X=(x), Y=(y1,y2), F=(-1)^(x*y1*y2). The cells y1=0,1 have affine label maps0,y2, so M=2,d=1. The row masses are3/4,1/4 and I_Y=1/2. The full squared spectrum is9/16 and seven copies1/16, and the positive conditional entropy is exactly full H minus h2(1/4). This specifies the physical split; no arbitrary one-coordinate conditional-law admission is inferred. NonBoolean psi_N=sum y_i/sqrt(N) has H=log2 N,E=1, violating each fixed rate for large N; it fails signed unit-phase/ternary admission. Arbitrary correlated physical laws remain excluded.

## 6. Exact universal gap

The scalar estimate and the group-energy proof are complete author derivations; independent reconstruction is pending. The first universal unpaid line remains a bound independent of growing row piece count, or an original-influence-priced decomposition of arbitrary Boolean cores into a bounded-piece source. Singleton representations can require exponentially many cells. Thus neither the improved O(s log s) theorem nor a scalar sharpness witness settles full FEI or pays a C018/C019 universal bank.
