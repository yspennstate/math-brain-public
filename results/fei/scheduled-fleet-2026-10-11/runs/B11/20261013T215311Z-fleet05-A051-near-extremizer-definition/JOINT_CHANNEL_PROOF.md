# Joint collision certificate and finite extremality

All entropies are in bits. All cubes are finite and uniform; f takes values in {-1,1}. This is a replacement upper certificate for a physical block decrement, not a universal payment theorem. A is a queried set, C its complement, and S is the squared Fourier spectral set. Write

    w_T(a)=hat(f restricted at X_A=a)(T),
    q_T=E_a w_T(a)^2,
    B_A=H(S_A | S_C),
    J_A=H(q)-E_a H(f restricted at a),
    L_A=B_A+J_A=H(f)-E_a H(f restricted at a),
    I_A=sum_(i in A) Inf_i(f).

Zero-q rows are omitted. Define the joint collision cost

    Gamma_A=sum_T q_T log2( E_a w_T(a)^4 / q_T^2 ),
    V_A=B_A+Gamma_A.

## 1. Universal row bound, equality and signed cancellation

Conditional on retained spectral row T, the physical assignment has law r_T(a)=w_T(a)^2/(2^|A| q_T). Its density relative to uniform is z_T(a)=w_T(a)^2/q_T. Thus

    J_A=sum_T q_T E_a z_T(a) log2 z_T(a).

For the tilted probability measure with density z_T, concavity of log gives

    E_a z_T log2 z_T <= log2(E_a z_T^2).

The lower bound is nonnegativity of relative entropy, proved directly by convexity of z log z and E z=1. Also E z^2>=1 by the square inequality. Since r_T(a)<=1, z_T(a)<=2^|A| and E z_T^2<=2^|A|. Consequently

    0 <= J_A <= Gamma_A <= |A|,    L_A <= V_A.       (1)

Equality J_A=Gamma_A holds precisely when each positive-q row has w_T(a)^2 constant on its nonzero physical assignments. Gamma_A=0 iff each such row has constant square on all assignments; this is also equivalent to J_A=0. These statements follow respectively from strict concavity of log on positive values and E(z-1)^2=0. No approximation or realizability hypothesis beyond the actual Boolean f enters.

For a Fourier row c_(U,T)=hat f(U union T), set

    k_(V,T)=sum_(U subset A) c_(U,T)c_(U symmetric-difference V,T).

Expanding w_T(a)=sum_U c_(U,T) chi_U(a) gives the Fourier expansion of its square, with coefficients k_(V,T); Parseval gives k_(empty,T)=q_T and

    Gamma_A=sum_T q_T log2(1+sum_(V nonempty) k_(V,T)^2/q_T^2).   (2)

The sums in k are signed sums before squaring. Replacing them by sums of magnitudes would discard the cancellation responsible for this certificate's improvement. Multiplying a row by a character preserves its square and hence its collision cost.

## 2. Tensor stability and full-factor cuts

For f(x)g(y) on disjoint cubes and A=A_f union A_g, rows, row probabilities and fourth-moment ratios factor. Logs turn the product of ratios into a sum, and summing the product row masses gives

    Gamma_A(fg)=Gamma_(A_f)(f)+Gamma_(A_g)(g).

The squared spectral laws are independent, so the same additivity holds for B, V, H and I_A. Empty queried sets have zero B and Gamma. A complete queried factor has Gamma=0 because its restricted child is a scalar Boolean sign; its cost B=H(factor). Thus a proper full-factor cut has V_A/I_A=R(factor). This certifies the quadratic tensor obstruction that additive recentring misses, and survives disjoint tensor powers.

This stability does not assert that criticality is inherited by arbitrary children. The next identity explicitly retains their deficits.

## 3. Fixed thresholds, finite maxima and the exact surviving gap

For D_K(h)=H(h)-K I(h), constants have D_K=0. Influence averaging under physical restriction gives I(f)=I_A+E_a I(f_a). Therefore

    D_K(f)=L_A-K I_A+E_a D_K(f_a).               (3)

If a violating Boolean function exists for a fixed K>=0, choose one with least essential dimension (a nonempty set of positive integers has a least member); every proper physical child then has D_K<=0. Such a witness has dimension at least two, since one-bit Boolean functions have entropy zero. Equations (1),(3) force

    V_A >= L_A >= K I_A+D_K(f)                 (4)

for every proper queried block. This gives a necessary joint-channel condition on dimension-critical witnesses without assuming an all-dimensional optimizer. Conversely any proper block with V_A<=K I_A rules out such a witness. In a general adaptive stopping tree, (3) telescopes and retains all terminal deficits; paying the queried blocks alone never eliminates the terminal obligation.

For n>=2 let M_n=max H(f)/I(f) over nonconstant functions on at most n bits, and define

    psi(f)=min_(empty != A proper, I_A>0) V_A/I_A,
    K_col(n)=max_(nonconstant n-bit f) psi(f).

These are finite maxima of finite sets; irrelevant coordinates are allowed. A maximizing M_n function (embedded if needed) has every proper physical child ratio <=M_n, so (3) at K=M_n implies L_A>=M_n I_A. Hence psi>=M_n at that function and K_col(n)>=M_n.

Reveal all coordinates except a coordinate i. Every one-bit Boolean child is constant or a character, so each retained row square is 0 or 1. The equality criterion in section 1 gives Gamma_A=J_A=H(q). As B_A=H(f)-H(q), V_A=H(f) EXACTLY. Choose i of smallest influence. Then I_A=I-Inf_i >=(n-1)I/n, and

    psi(f)<=n R(f)/(n-1),
    M_n <= K_col(n) <= n M_n/(n-1).             (5)

Thus lim K_col(n)=sup_n M_n in the extended nonnegative reals. A dimension-independent bound on K_col is equivalent to full FEI (an FEI constant bounds K_col by twice that constant for n>=2). This is the compactness substitute needed for the packet: finite maxima and minimal witnesses suffice, and no global optimizer is asserted. The collision certificate preserves the same co-singleton squeeze as exact block descent while permitting useful cancellation on intermediate blocks.

FIRST UNSUPPORTED LINE: There is a finite K independent of n such that every dimension-critical K-witness has a proper block A with V_A<=K I_A. Equation (4) explains why this would finish FEI; the present proof neither supplies that K nor bounds K_col universally.

## 4. Exact six-bit separation from singleton certificates

The previously saved NAND case0006 is the tree

    (((((),()),(),()),()),())

Leaves are bits 0 through 5 in recursive order. The selected block is A={4,5} (mask 48). This is an actual Boolean truth table, source-hashed in out/CONTROL_NAND6_case0006.json. Its exact values are

    H=10-(27/128)log2 3-(507/512)log2 13-(361/512)log2 19,
    I=5/4, I_A=1,
    B=2+(217/256)log2(217)-(507/512)log2 13-(361/512)log2 19,
    J=13/2+(25/128)log2 5-(217/256)log2(217),
    Gamma=2+(217/256)log2(12913/47089).

The retained constant-row mass is 217/256, its four child coefficients are (1,1,-1,5/8), and its collision ratio is 51652/47089. All other positive rows are supported only on physical assignment 3 and have collision ratio 4; their total mass is 39/256. This proves the Gamma formula, since 51652=4*12913 and 12913=37*349.

Outward rational logarithm enclosures certify

    L_A<23/10, V_A<47/20<12/5<R(f),
    Gamma_A-J_A<11/250,
    min_(singletons i) V_i/Inf_i > 319/100 > R(f).

So unlike U_A, the joint certificate does NOT collapse to singleton optimization. Mask48 is the unique labelled block with V_A/I_A<R(f) in this six-bit table and is its global minimum. These finite inequalities are verified by exact prime-log comparisons, not rounded decimal values.

Three physical children are constants; assignment 3 has H=6-(27/32)log2 3-(25/32)log2 5 and I=1. Its root-ratio deficit is between 44/100 and 45/100. The mean deficit is therefore positive (between 11/100 and 45/400), exactly equal to R(f)I_A-L_A. This explains the strict descent: a higher-ratio child survives. The root is not dimension-critical; this example is a certificate improvement, not a paid high-threshold critical structure theorem.

## 5. Why zero channel still does not pay entropy

Let h be any Boolean sign on A and let y be one additional fair physical bit. For F(x,y)=h(x)y, all children after querying A are signed characters y. Their squared spectra coincide, so Gamma_A=J_A=0, but B_A=H(h) and I_A=I(h). Thus paying every such prescribed zero-channel block by a universal constant is exactly the original FEI problem for h. A valid route must select a block using the critical structure, rather than claim that signed cancellation itself pays B. Section 3's finite equivalence and section 4's strict finite separation do not bypass this obstruction.
