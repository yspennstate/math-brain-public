# A GU-valid hereditary class still cannot fund all product stops

All logarithms in entropy formulas are base2. Physical cubes are uniform; all stopping trees are finite with predictable coordinate choice and fair outcomes. Full FEI remains OPEN. The result below refutes an auxiliary necessity bridge, not GU or FEI.

## 1. Exact GU certificate for every point dimension

Let f_m(x)=1-2*1[x=0], m>=1. Put d=2^(1-m). The squared spectrum is p(empty)=(1-d)^2 and p(S)=d^2 for every nonempty S. Every physical influence is d, so I_m=md. For nonempty S, pi(S)=2^(m-|S|)d^2; pi(empty)=1. Therefore, with A(t)=-2(1-t)^2 log2(1-t), A(1)=0,

    U_m=A(d)+m d-m d^2.                              (1)

This follows by summing m-|S| over nonempty subsets: m*2^(m-1)-m. No support or empty-set term is omitted. U_1=0. A physical query has one constant child and one f_(m-1) child. Define U_0=0 for constants. Thus every coordinate has identical drift and

    G_m=m(U_m-U_(m-1)/2),
    G_m/I_m=1+(m-2)d+[A(d)-A(2d)/2]/d, m>=2.         (2)

Write c=log2(e). On 0<=t<1,

    A''(t)=(-4 ln(1-t)-6)/ln2.

Consequently A(t)+3c t^2 is convex, including its continuous limit at1. Its midpoint inequality at0,d,2d gives

    A(d)-A(2d)/2 <=3c d^2, 0<=d<=1/2.               (3)

For m>=3, (m-2+3c)2^(1-m) decreases with m, since m-3+3c>0. Also ln2>2/3 from the positive atanh series at1/3, so c<3/2. Equations(2),(3) yield

    G_m/I_m <=1+(1+3c)/4 <19/8, m>=3.

For m2, U_2=I_2=1 and G_2=2, giving ratio2. For m1, G=U=0. Constants have I=U=G=0 and require no division. Hence for ALL m>=0,

    G(f_m)<=19 I(f_m)/8.                             (4)

This is an analytic all-dimensional certificate, not extrapolation from a finite search. It is not claimed to be the optimal constant.

## 2. Disjoint products, bent factors, and every physical descendant

For functions on disjoint physical coordinate blocks, p_(fg)(S,T)=p_f(S)p_g(T) and pi_(fg)(S,T)=pi_f(S)pi_g(T). Direct substitution gives U(fg)=U(f)+U(g); influences and G are also additive because each physical restriction acts on one factor. The assertion includes arbitrary adaptive histories: a reached history fixes a cylinder, so the remaining disjoint factorization is literal.

The bent pair beta(u,v)=(-1)^(uv) has uniform four-atom spectrum, I=1,U=1,G=2: fixing either physical bit leaves a constant or a character, each with U=0. Characters and constants have U=G=0. Restricting a point function gives either a smaller point function or a constant. Therefore the class C of ALL finite disjoint products of arbitrary-dimensional point functions, bent pairs, characters and constants is restriction closed and satisfies the ONE fixed GU pair

    (a,b)=(19/8,0)                                  (5)

at EVERY physical descendant. There is no dependence on factor count, dimension, history, stopping depth or rare reach probability. This certificate is used to test a funding bridge, not presented as closure of universal GU.

## 2a. An explicit nonnegative physical supermartingale, with paid U boundary

Let a=19/8. Within a point factor every remaining coordinate has the SAME drift ratio (2); in a bent factor it has ratio2; in a character it has ratio0. Thus in C the stronger guard Delta_i U<=a Inf_i holds at EVERY remaining physical coordinate. A rule may query any remaining relevant coordinate, using any predictable history-dependent choice, and stop when desired. The usual physical edge identity is I_parent=Inf_i+mean I_child. Induction on remaining dimension, ending with U=I=0 at constants, proves U<=aI throughout C. Consequently

    V_t=a I(f_t)-U(f_t)>=0,
    V_t-E[V_(t+1)|F_t]=a Inf_(i_t)(f_t)-Delta_(i_t)U(f_t)>=0.

This is an explicitly influence-priced NONNEGATIVE supermartingale on the revealed-bit filtration, for every such rule and bounded stopping time. The process V_t+sum_(s<t)(a Inf_(i_s)-Delta_(i_s)U) is an exact martingale. Equivalently, for every stopping cut tau,

    U(f_0) <= a E sum_(s<tau) Inf_(i_s)(f_s)+E U(f_tau)
            <= a I(f_0).

The last inequality uses the SAME already certified class bound on actual terminal U and the exact influence telescope; no terminal U is erased or renewed. All-terminal boundary price and correction are bounded by the original aI. Constant/parity endpoints are handled without dividing by zero. This process is a scoped sufficient U-drift formulation, not a universal assertion for arbitrary Boolean cores. The reset-capital obstruction below therefore persists even in a class with a fully paid physical U-process. It cannot be dismissed as an unpaid U boundary of that class.

## 3. Any-reference capital obstruction inside that GU-valid class

For m>=3, take N=1/d=2^(m-1) disjoint copies of f_m and let g_m be their product. Add one fresh bent pair F_m(u,v,Y)=(-1)^(uv)g_m(Y). This is a member of C. All quantities below concern actual Boolean truth tables, not a relaxed law.

Let M(f)=sum_j h2(Inf_j f), TC=M-H. For f_m,

    M(f_m)>=m d log2(1/d)=m d(m-1).

Its nonempty spectral mass epsilon=2d-d^2 lies in[d,2d], spread uniformly over2^m-1 atoms. The elementary bound h2(epsilon)<=epsilon log2(1/epsilon)+epsilon log2(e), together with log2(e)<2, gives

    H(f_m)<=2d(2m+1),
    TC(f_m)>=d(m^2-5m-2).                            (6)

Tensor additivity yields

    I(g_m)=m, TC(g_m)>=m^2-5m-2,
    I(F_m)=m+1, H(F_m)<=4m+4=4I(F_m).               (7)

Start F_m at ANY normalized supporting reference Q, with any account that pays actual terminal KL plus accumulated actual outcome KL, and admits querying v, resetting BOTH children to their actual marginal products, then stopping. The children are g_m and (-1)^u g_m; multiplication by this character only makes the surviving u spectral bit deterministic. Their FULL terminal entropies are H(g_m); their actual product KL is TC(g_m). Actual reference predictions r_v are positive, and their outcome KL O_v>=0. Consequently the admitted stopping cut FORCES

    Account >=TC(g_m)+O_v >=TC(g_m),
    Account/I(F_m)>=(m^2-5m-2)/(m+1) ->infinity.     (8)

This argument does not require a sector form, Q=p, product Q, zero erasure, or a special fair-zero kernel. It is a necessary nonnegative terminal bill, independent of how the account is implemented. If an account also pays terminal H or U, those nonnegative terms only strengthen the obstruction. In particular retaining the FULL H+KL does not rescue the proposed cheap account; that full terminal bill is M(g_m).

Thus even the hereditary valid GU certificate(5) does NOT imply influence-scale initial capital for ALL actual product stopping cuts of the same class. A064's obstruction is not a consequence of failure of GU on its hard family. Conversely, this says nothing against a selected policy that excludes such unnecessary resets, or against a suitable nonproduct terminal/reference class. It does not disprove FEI; (7) explicitly controls H/I.

## 4. Independent reconstruction of A064's sector eligibility and drift

Let F(u,v,y)=g(y) if v0 and (-1)^u h(y) if v1. Its actual squared law is P(b,c,T)=p_b(T)/4. Start with the FULL normalized reference Q(b,c,T)=w_b R_b(T)/2, w_b>0, sum w=1; every R_b supports p_b. This full reference hypothesis persists under ALL ordinary y queries, including zero-source rows. The actual sector predictions t_b(e)>0 update w'_b=w_b t_b(e)/sum_j w_j t_j(e), and R'_b is the actual normalized conditional transport. Nothing claims R'_b stays product.

At a reached node write a_b=R_b(supp p_b), D_b=KL(p_b||R_b), T_b=TC(p_b), L_b=D_b-T_b. Erasing spectral v combines two equal source probabilities and equal reference probabilities in each (b,T) pair, so E_v=0. On positive source rows the coherent physical v outcome is deterministically b; on source-zero rows it is fair. Thus

    r_0=1/2+(w_0 a_0-w_1 a_1)/2,
    K_b=D_b+log2(r_b/w_b),
    J_b=T_b-K_b=log2(w_b/r_b)-L_b,
    B=( [J_0]_+ + [J_1]_+ )/2.                     (9)

Necessity is a physical policy resetting exactly the positive-debit children. Sufficiency allocates max(K_b,T_b) before the choice and current chosen KL after it. The max is BEFORE averaging. All source-zero/reference-only child mass remains in the normalizer r_b.

Since each opposite sector has positive support mass, r_b>w_b/2, and at most one w_b/r_b exceeds1. Therefore

    B<=mean[-L_b]_++1/2.                            (10)

If each R_b is product then L_b is the sum of marginal binary KLs and is nonnegative, recovering the sharp half-bit guard. After prefixes that hypothesis is lost and must be measured, as our previous accepted obstruction demonstrates. Source sharpness family: rank-two star quadratic versus full bent quadratic, even n>=4, both physical influences1/2; original product uniform gives L=0 and B=(1-log2(1+2^(2-n)))/2 tending to1/2.

Let F_t be the sigma-field of revealed fair bits and predictable coordinate choices, with any declared finite prefix tree fixed in advance. At ordinary nodes the exact normalized common-kernel chain gives K_parent=E+O+mean K_child. For optional pivot stopping debt use the source backward recursion G=max(0,B_if_admitted,max_i(mean G_child-E_i)). Then K_t+G_t+sum_(s<t) O_s is a supermartingale. At pivot/reset boundaries use K_b+[J_b]_+ and then chosen current K; later physical continuations retain the installed reference. Full terminal H is retained on BOTH sides if added, not magically funded. The finite recursion is minimal because every maximizing action and immediate stopping cut is admitted. No optional-stopping limit or pathwise expectation identity is used.

Independent verdict on A064's stated theorem: HOLDS, with no mathematical repair supplied. Its rare dummy-query example is consistent: the root reserve is2^-k B, the continuing branch reserve increases to B, and fair terminal expectation, not pathwise constancy, is the invariant. Old consumed costs remain spent. Source review is distinct from the new GU-valid necessity obstruction in sections1--3.

## 5. First unpaid universal line

The candidate that GU-valid hereditary cores must possess cheap capital for ALL product stopping cuts is REFUTED by(5)--(8), for EVERY initial supporting reference. The next sufficient B13 route must choose an explicit narrower physical rule and terminal/reference class, with a nonnegative correction whose ORIGINAL price is bounded by actual influence and whose complete terminal U is paid. Neither the sector Snell recursion, an initial reference choice, the all-history tensor cocycle nor another product-history depth supplies that universal price. This proof removes a false necessity bridge; universal GU, its sufficient paid U-drift process and full FEI remain OPEN.
