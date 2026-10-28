# Singleton-to-high import: one-boundary payment and a depth obstruction

All entropy charges use natural logarithms. This repairs the high-degree scale composition interface without paying the still-open universal prime charge. The argument is an author proof pending independent review.

## Exact composition and import owners

For a Boolean sign h at an interior product law, use normalized coefficients c_A=hat h(A)/sqrt(v_A), P_A=hat h(A)^2, and dyadic scales j_A with 1/2<2^j_A |c_A|<=1, zero-mass terms omitted. Write

    J_1(h)=ln4 sum_singletons P_A j_A,
    J_hi(h)=ln4 sum_{|A|>=2}P_A j_A,
    Delta_h=I_h-Var(h), R_h=sum_{|A|>=3}(|A|-2)P_A,
    M_h=sum_{|A|>=2}P_A=Delta_h-R_h.

Let F=g(f_1,...,f_m) be a genuine disjoint composition at the actual induced independent child law; contract constant children. Put w_i=Var(f_i)>0, a_i=I_i(g)/w_i, s_i=P_g({i}), and b_i=(I_i(g)-s_i)/w_i>=0. All I_i here are orthonormal spectral influences, sum_{A containing i}P_g(A).

For an occupied physical set S let A be its occupied-block set and T_i its nonempty child sets. Unique disjoint Fourier factorization gives c_F(S)=c_g(A)product c_i(T_i) and the conditional probability factorization from the earlier A043 reference proof. Define the nonnegative integer carry

    kappa(S)=j_F(S)-j_g(A)-sum_{i in A}j_i(T_i),
    C_hi=sum_{|S|>=2}P_F(S)kappa(S).

The SINGLETON-TO-HIGH import is the nonnegative actual charge

    T_out=ln4 sum_i (s_i/w_i) M_i j_g({i}),
    T_in =sum_i b_i J_1(f_i),
    T=T_out+T_in.                                          (1)

When s_i=0 its summand is zero with no scale assigned to a zero coefficient. Direct partition of the actual final Fourier labels gives

    J_hi(F)=J_hi(g)+sum_i a_i J_hi(f_i)+ln4 C_hi+T.           (2)

Proof of the partition: every outer high label already becomes a physical high set; a singleton outer label becomes high precisely when its selected child set has degree at least two, yielding T_out. A child high label contributes its scale charge at every outer occurrence, yielding a_i J_hi(f_i). A child singleton scale contributes to a final high label precisely when the outer set has degree at least two, yielding b_i J_1(f_i). The remaining rounding is exactly C_hi. There is no assumption that J_hi itself is composition additive and no deletion of the full singleton terminal.

## A universal payment at ONE boundary

For an integer j>=1, j/2^j<=1/2. Therefore every scalar dyadic cell satisfies t j<=1/2. At a Boolean coordinate, D=(h|1-h|0)/2 lies in {-1,0,1}. If t=|E D| and d=E D^2, then d>=t, so

    P_i j_i=v_i t^2 j_i <= (1/2)v_i d=(1/2)I_i(h).

Consequently

    J_1(h)<=(ln4/2) I(h),
    s_i j_g({i})<=(1/2) I_i(g).                            (3)

The integer inequality follows from j<=2^(j-1) by induction (equality at j=1,2); j=0 contributes zero. This is a genuine Boolean admission step, not a statement about arbitrary spectra.

Use (3) in the two imports:

    T_out <=(ln4/2)sum_i a_i(Delta_i-R_i),
    T_in <=(ln4/2)[2Delta_g-R_g+sum_i b_i Delta_i].          (4)

Here sum_i b_i w_i=sum_{|A|>=2}|A|P_g(A)=2Delta_g-R_g and I(f_i)=Delta_i+w_i for each child's TOTAL influence.

Combining (4) with Delta_F=Delta_g+sum_i a_i Delta_i gives the universal one-boundary theorem

    T <=ln4 Delta_F
        -(ln4/2)[R_g+sum_i{(a_i-b_i)Delta_i+a_i R_i}]
      <=ln4 Delta_F.                                      (5)

All refunds in brackets are nonnegative and have their original owners. This pays singleton import at one composition boundary; it does not pay C_hi or the inherited J_hi, and does not authorize restarting the same Delta_F budget at every depth.

The T_out bound alone is sharp: take g to be binary AND at induced probabilities (1/2,1/2), the first child a fair two-bit parity and the second a fair literal. The only importing outer singleton has s=1/4,j=1, I_i(g)=1/2, child M=1, so T_out=ln4/4=(ln4/2)a_i M. The combined coefficient in (5) is not claimed sharp.

## Actual ternary-majority tower: the boundary allowance cannot be renewed

Let F_0 be a fair sign literal and F_d=Maj_3(F_(d-1)^(1),F_(d-1)^(2),F_(d-1)^(3)) on disjoint fair blocks. The actual prime gate is

    Maj_3(x,y,z)=(x+y+z-xyz)/2.

It is prime under genuine Boolean disjoint decomposition: every proper two-variable block has three distinct cofactor rows. Every F_d is an actual Boolean sign on 3^d distinct inputs. At every gate, singleton mass is3/4, triple mass1/4, every occupied coefficient has absolute value1/2, and each child weight a_i=1/2. Thus

    I(F_d)=(3/2)^d, Delta(F_d)=(3/2)^d-1,
    J_1(F_d)/ln4=d(3/4)^d,
    J_all(F_d)/ln4=2 Delta(F_d).

All nonzero coefficients of every subtree are signed dyadic powers, so every carry, including singleton and high carry, is ZERO. Every dyadic flat/paid-sector reference equals its actual spectrum, so its normalizer and ordinary KL are also zero; the composed complete reference is likewise the actual law. The weighted internal-gate count is2 Delta(F_d); its total prime high-scale source is (ln4/2)Delta(F_d). Summing the exact recurrence (2), with the original node weights omega, therefore yields

    T_total=sum_internal_nodes omega_v T_v,
    T_total/ln4=(3/2)Delta(F_d)-d(3/4)^d,                   (6)
    T_total/[ln4 Delta(F_d)] ->3/2.

For d=4, Delta=65/16 and T_total/ln4=309/64, hence

    T_total-ln4 Delta(F_4)=(49/64)ln4>0.                   (7)

This explicitly refutes the tempting all-depth assertion T_total<=ln4 Delta(F), even though (5) holds at EVERY boundary and carries vanish. It is not a FEI counterexample: E(F_d)=J_all(F_d)=2ln4 Delta(F_d). The issue is reuse of an inherited boundary budget, not excessive entropy.

The tower formulas follow directly from the displayed gate polynomial and unique disjoint Fourier expansion. For a compressed exact certificate one may use the bivariate generating recursion

    G_0(z,t)=z,
    G_d(z,t)=t[(3/4)G_(d-1)(z,t)+(1/4)G_(d-1)(z,t)^3],

where z records physical degree and t records dyadic scale. Distinct outer/child supports are disjoint alternatives, so no coefficient collisions occur. Evaluating derivatives at1 gives the influence and scale moments; selecting the degree-one coefficient gives 3^d4^-d with scale d. This is an all-depth structural proof, not numerical extrapolation from finitely many towers.

## Remaining original-source requirement

The previous paid-sector complete reference remains valid, including exact ordinary KL and full singleton/high terminal laws. Equation (5) adds a dimension-independent boundary payment, but (6)-(7) prove why that payment is not itself a universal depth-free closure. At all depths the original complete entropy/deficit telescope must allocate each gate's actual singleton entropy, mantissa refund, and prime J_hi once. The universal remaining line is still J_hi(g)<=K Delta(g), or the sharper original-reserve inequality, for ALL irreducible gates at ALL induced biases. No bound on this charge or on all high carries follows from the new import theorem.

This stage repairs a specific composition component and identifies a rigorous failure of renewing it. Independent review of the new quantitative import bound and tower identity is pending. Full FEI remains OPEN.
