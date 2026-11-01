# Arbitrary-core correlation survives an isospectral query

All laws are complete normalized finite probability laws, and all logarithms are base two. This is a reference-capacity theorem, not FEI or a claim that product references are necessary.

## 1. Exact diagonal posterior identity

Let p be ANY finite law on bit strings s in {0,1}^n. Let P(s,t)=p(s)1{s=t}. Let Q(s,t)=sum_{j=1}^M w_j A_j(s)B_j(t), where w is a probability law and A_j,B_j are arbitrary probability laws. Thus even correlations within each half are allowed. Assume Q(s,s)>0 whenever p(s)>0. Zero-weight components can be omitted. Define the exact posterior k(j|s)=w_j A_j(s)B_j(s)/Q(s,s), and the joint law L(s,t,j)=p(s)1{s=t}k(j|s). Let v_j=L(J=j) and p_j(s)=L(S=s|J=j) for v_j>0. Expanding logarithms gives the EXACT identity

 D(P||Q)=H_L(S|J)+D(v||w)
                +sum_j v_j[D(p_j||A_j)+D(p_j||B_j)].                 (1)

Indeed lifting P by Q's posterior preserves its KL to Q. Conditional on J, S=T, so the KL to A_j times B_j is H(p_j)+D(p_j||A_j)+D(p_j||B_j). No occupied atom or mixture normalizer is removed. Consequently

 D(P||Q)>=H(p)-H_L(J)>=H(p)-log M.                                (2)

A useful exact nonnegative residual is

 D(P||Q)-H(p)+log M
 =D(v||Uniform_M)+H_L(J|S)+D(v||w)
       +sum_j v_j[D(p_j||A_j)+D(p_j||B_j)].                        (3)

This proves the bound including nonuniform or absent latent components. Infinite CE gives an infinite left side and needs no posterior. For n=0, H(p)=0 and the statement is ordinary KL nonnegativity. More generally, for ANY P(S,T), the posterior lift gives D(P||Q)>=I_P(S;T)-log M: conditional mutual information replaces H_L(S|J), and I_P(S;T)<=I_L(S;T|J)+H_L(J). The diagonal version retains the stronger explicit residual (3).

The coefficient of log M is sharp. For uniform p on all 2^n labels, let M=2^k, 0<=k<=n. Fix the first k bits in both halves to the latent label, and make each of the other 2(n-k) bits independent fair. Then Q is a mixture of M complete coordinate-product laws and Q(s,s)=2^k/2^(2n), so D(P||Q)=n-k. This is an analytic all-n construction; the Boolean realization below supplies such p for even n by bent two-bit blocks.

## 2. Actual Boolean realization and exact phase energy

For ANY Boolean g on n uniform bits, define d_g(x,y)=g(x_1*y_1,...,x_n*y_n). Fourier expansion gives d_g=sum_S ghat(S)x_S*y_S. Its full squared spectrum is exactly the diagonal law above with p=p_g. Thus

 H(d_g)=H(g), I(d_g)=2I(g).

Add three independent physical bits z_1,z_2,z_3 and put h=z_1*z_2*z_3*d_g. Then H(h)=H(g), I(h)=3+2I(g), and h is balanced. Query z_1. BOTH children are nonconstant, have the same complete squared spectrum, and retain the entire diagonal p_g with the mandatory labels z_2,z_3. There is no occupied adjacent pair, no singleton mass and no true spectral erasure.

Use the original four-bit A079 complementary controller a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1), b=1-a^2, beta=E b^2=3/8, and G_sigma=a+sigma*b*h for BOTH sigma in {-1,+1}. At the matched incoming reference P_G, the z_1 query has queried influence beta and EXACTLY zero erasure, child JS, conditional occupancy KL, singleton-ghost credit, coherent calibration refund and nonempty phase-bin energy. These statements hold because the source spectrum always contains the three tag labels and deleting z_1 is injective; all original controller-vacuum atoms remain unchanged. The children still contain z_2,z_3, so tail and vacuum never collide.

At each child prescribe a complete coherent target retaining every actual controller-vacuum atom A_U^2 and replacing ONLY the shifted diagonal core spectrum by ANY normalized q of finite CE. The FULL erasure-plus-average terminal CE increment, including BOTH children, is exactly

 beta D(P_diag||q).                                                (4)

The coherent source is balanced before and after the query, so its vacuum term and every B_U^2 factor cancel literally. If each child may choose a DIFFERENT q that is a mixture of at most M products across the x/y partition, (2) applies separately to each full terminal. Therefore the mean bill is at least

 beta*max(0,H(g)-log M).                                          (5)

In particular this covers mixtures of coordinate-product laws, with all reference-only mass retained. Any actual unused ancestor allowance U can fund this prescribed class only if U>=beta*max(0,H(g)-log M), at unit reach. At global reach eta the necessary bill is eta times this quantity; disjoint frontiers add and old debits remain untouched. If M<2^H(g), every target in this declared class incurs positive charge, although ordinary inherited continuation still costs zero. Ghost manufacturing can prepay the charge but supplies no additional source budget.

The original full energy is I(G_sigma)=7/4+beta*(3+2I(g))=23/8+(3/4)I(g), and full entropy is 5-(9/16)log 3+beta H(g). Every phase and auxiliary cost has therefore been retained. These formulas do NOT yield an unbounded H/I family: the arbitrary core still carries precisely the unknown FEI ratio. Exact representation of a diagonal law with support size N needs M>=N even with arbitrary within-half components, because its support submatrix is diagonal with rank N. This rank condition concerns the chosen reference class, not Boolean phase realizability.

For a concrete sharp Boolean fixture use g equal to a product of independent two-bit one-point defects (negative only at all-plus). Its spectrum is uniform on all 2^n labels for even n, H(g)=n and I(g)=n/2. The construction above attains (5) exactly at every M=2^k. Its full H/I is bounded; it tests the latent-capacity price, not FEI.

## 3. Independent reconstruction of A032 and A096

A032-ISOSPECTRAL-CORE-BOUNDED-MIXTURE-OBSTRUCTION@1 uses h=z_1*z_2*z_3*g without diagonal duplication. The same literal cancellation proves its exact beta D(p_g||q) bill and its ghost threshold. For its tensor of three-bit point defects, p_0=9/16 and seven masses are 1/16. Direct Walsh and edge counts give H=4-(9/8)log 3, I=3/4 and coordinate-product excess tau=2-(9/8)log 3. The strict bounds 1/8<tau<1/4 follow from 3^3<2^5 and 3^9>2^14. The posterior KL identity gives D(P||q)>=TC(X|J); block independence yields sum_b I(X_b;J)<=I(X;J), hence sum_coordinates I(X_i;J)<=3I(X;J), and D>=r*tau-2log M. Its rank minor K tensor r with K=[[9,1],[1,1]]/16 has determinant (1/32)^(r*2^(r-1)); the mixture (delta_empty+Uniform_3)/2 supplies the matching 2^r upper representation. The stated global rate follows by substitution, including the positive controller reserve. No repair is needed. The coefficient one in (5) is for a DIFFERENT, duplicated-core construction; it does not silently replace A032's coefficient two on its original three-coordinate blocks.

A096's complete-target theorem starts with injective occupied-frequency deletion on any finite isospectral physical tree. Pull complete terminal references back to root occupied labels as q_l(s), with physical reaches w_l. Set G(s)=product_l q_l(s)^w_l, Z=sum_s G(s), R*=G/Z. Weighted AM-GM retains all ghost mass and proves 0<Z<=1. Expanding logs gives mean CE_terminal=CE(P,R*)-log Z and -log Z=sum_l w_l D(R*_l||Q_l). Therefore the signed replacement debit is D(P||R*)-D(P||Q0)-log Z, and at a global subtree reach eta it is eta times that quantity. Old bookings and complementary terminals remain in the SAME allowance. This reconstruction accepts the theorem at supplied-source scope; the effective source is not asserted cheap or algorithmically available.

For the three-bit Boolean law uniform on {empty,12,13,23}, query bit1 and use the two complete transported terminal probabilities (3,3,1,1)/8 and (1,1,3,3)/8. Then R*=P but Z=sqrt(3)/2, so the entire positive bill is (1/2)log(4/3). In particular the geometric normalizer is not optional. Our finite checks additionally use nonuniform actual laws, complete ghost mass, and outcome-dependent tilts with an exactly rational Z^2, independently of A096's implementation.

## 4. Honest universal boundary

The proven capacity bound prices a necessary conversion ONLY AFTER the admissible target class is declared. Neither the duplicated-core construction nor either reviewed theorem proves that FEI intrinsically needs a product-mixture target. No universal source-price assumption is manufactured from a matched spectrum, and A094/A011's numeric original reserve is not transferred to an unidentified model. The first unsupported universal line is an influence-priced arbitrary-core reference family closed under actual inherited marginals, or a useful mandatory compatible target whose entire bill is paid from its ACTUAL unused original allowance. The new result says that a subexponential latent alphabet cannot erase arbitrary retained spectral entropy for free, even in the exact local phase nullspace.
