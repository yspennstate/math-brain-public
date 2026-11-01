# Rare activation: the actual block limit and the R2 singleton test

Uniform cubes, Boolean signs, entropy in bits. For nonconstant g on n>=1 data bits, put h=(1-g)/2, mu=E g, c=1-mu>0, p=2^-r and F_r=1+1_{y=0}(g-1), r>=1. Physical coordinate blocks are fixed; irrelevant coordinates are allowed, but only positive-influence block ratios are taken. Define phi(F)=min over nonempty proper A of L_A/I_A. Let raw entropy T(g)=sum_S (g-1)hat(S)^2 log2[1/(g-1)hat(S)^2], with zero terms omitted. Thus T(g)=H(g)+mu^2 log2 mu^2-c^2 log2 c^2=4 Fraw(h)-8 E h, and I_B(g)=4 E_B(h).

## 1. A compressed exact expression for every block

Set A(d)=-(1-d)^2 log2(1-d)^2+d^2 log2 d^2 for d in [0,2], using zero-mass continuity. Direct activation Fourier coefficients give

    H(F_r)=p T(g)+4r p c+A(pc),  I(F_r)=p[I(g)+rc].       (1)

This is the arbitrary-mean form of the existing C013 baseline. For a block containing a data subset B and k controls, all off-control branches are constant and the all-on branch is activation of g_b on r-k controls. In particular

    L_(B,k)=H(F_r)-2^-k E_b H(F_(r-k)(g_b)),
    I_(B,k)=p[I_B(g)+kc].                               (2)

Here F_0(g_b)=g_b, k=0,...,r, and the full block (B=[n],k=r) is excluded. This reduction is exact physical control permutation symmetry, not Fourier conditioning. It enumerates every declared block test. Averaged tests alone remain weaker than every individual-child criticality test.

Let Delta_B=T(g)-E_b T(g_b)=4 Lambda_B(h), the raw-indicator entropy decrement. Conservation of E h removes the -8 E h term. The raw block identity or direct partial Fourier entropy expansion proves Lambda_B(h)>=0; no universal bound on Lambda/E is assumed. Define

    epsilon_t(c)=H(F_t(g))/2^-t - T(g)-4t c-2c log2(euler).

For a self-contained justification of raw positivity, let v_T(b) be the T Fourier coefficient of the real restriction h_b and q_T=E_b v_T(b)^2. Fourier expansion on B gives Fraw(h)=Fraw(q)+sum_T q_T H(the normalized B row), while E_b Fraw(h_b)=Fraw(q)-(1/ln2)sum_T Ent_b(v_T^2). Both the normalized row entropies and the squared-amplitude entropy functionals are nonnegative. This proves the stated Lambda identity and positivity for indicators (indeed every real h), without importing a pending component theorem.

The dependence is only on c, not the rest of g. For t>=1,

    epsilon_t(c)=-2^-t c^2[2t-log2 c^2]
                  +s(2^-t c)/2^-t-2c log2(euler),
    s(v)=-(1-v)^2 log2(1-v)^2.                         (3)

Thus (2), divided by p, is exactly

    L_(B,k)/p = 4kc+Delta_B+epsilon_r(c)-E_b epsilon_(r-k)(1-E g_b).  (4)

The formula holds also at t=0, where epsilon_0(c)=H(g)-T(g)-2c log2(euler) depends only on mu=1-c. No unsupported dimension-limit exchange is needed.

## 2. Uniform remainder and the all-proper-block limit

For v in [0,1], 0<=2v log2(euler)-s(v)<=3v^2 log2(euler). In natural units this follows from the convergent expansion s(v)=2v-3v^2+4 sum_(j>=3) v^j/[j(j-1)(j-2)], with the endpoint by continuity, together with s(v)<=2v. The latter follows by differentiating 2v-s(v) or using -(1-v)ln(1-v)<=v. Since 2^-t c<=1 for t>=1, both contributions in (3) are nonpositive. Bounds c^2<=4, -c^2 log2 c^2<=1, and log2(euler)<3/2 give

    |epsilon_t(c)| <= delta_t=(8t+19)2^-t, t>=1.       (5)

delta_t decreases for integer t>=1, with delta_1=27/2<15. At t=0, the bias-only expression, |mu^2 log2 mu^2|<=1, |c^2 log2 c^2|<=8 and 2c log2(euler)<=6 give |epsilon_0(c)|<=15. All constants are explicit and uniform in the child core.

Let

    lambda(g)=min(4, min_(nonempty B subset [n], I_B>0) Delta_B/I_B)
             =min(4, min_B Lambda_B(h)/E_B(h)).         (6)

Unlike the definition of phi(F), the inner data block B can be all data coordinates, because at least one control remains. Put d0=min(c,min_(i:Inf_i(g)>0) Inf_i(g))>0. For r>=2, s=floor(r/2),

    |phi(F_r)-lambda(g)|
       <= 2 delta_s/d0+(30+2delta_r)/(r c).             (7)

Proof of the lower bound: the leading quotient in (4) is the influence-weighted average of 4 and Delta_B/I_B, so it is >=lambda. If k<=r/2 the remainder has size <=2delta_s and the denominator is >=d0. If k>r/2 the denominator is >rc/2 and the remainder has size <=delta_r+15. For the upper bound, if lambda is attained by a data block, choose k=0 and its error is <=2delta_r/d0. If lambda=4, choose all controls and no data; this is a proper block, and its correction has absolute value <=(15+delta_r)/(rc), using |T(g)-H(g)+2c log2(euler)|<=15. These prove (7) without assuming the minimizing k stays bounded.

Consequently

    lim_(r->infinity) phi(F_r)=lambda(g).              (8)

This closes the fixed-core rarity limit for all proper blocks, including growing control subsets. It identifies the unpaid raw-indicator decrement problem rather than solving it. For fixed g, H(F_r)/I(F_r)->4. C013 preserves arbitrary seed ratios by amplifying its core while r grows; it does not claim that a fixed core preserves its ratio as r->infinity.

## 3. Exact control and data singleton R2 prices

Write Phi(a,b)=(a+b)log2(a+b)-a log2 a-b log2 b. For one control i let d=pc. Spectrum pairing gives

    B_i=2d-2d^2+Phi((1-d)^2,d^2),
    beta_i=min(d,1-d), Inf_i=d,
    L_i=4d+A(d)-A(2d)/2.                             (9)

All three are independent of the core beyond its mean. Thus as r->infinity,

    B_i/Inf_i ->2, beta_i/Inf_i ->1,
    (B_i+(2/ln2)beta_i)/Inf_i ->2+2/ln2,
    L_i/Inf_i ->4.                                  (10)

The R2 surrogate's limiting excess over the actual singleton decrement is 2/ln2-2. It is not an actual paid erasure. In a threshold-critical positive-deficit source, R2 requires C Inf_i+D_C<=B_i+kappa beta_i, so a control violates this necessary test exactly when D_C/p>U_i/p-Cc. A genuine actual singleton block fails the stronger criticality comparison exactly when D_C/p>L_i/p-Cc. These different cutoffs are recorded rather than conflated.

For a data singleton j, write a_T=ghat(T), with T not containing j; a_j=ghat({j}), b=1-pc. Define

    Uraw_j=sum_(T!=empty) Phi(a_T^2,a_(T+j)^2)+Phi(c^2,a_j^2),
    Vraw_j=sum_(T!=empty) min(a_T^2,a_(T+j)^2)+min(c^2,a_j^2).

Then exactly

    B_j=p Uraw_j-p^2 Phi(c^2,a_j^2)+Phi(b^2,p^2 a_j^2),
    beta_j=p Vraw_j-p^2 min(c^2,a_j^2)+min(b^2,p^2 a_j^2),
    Inf_j=p Inf_j(g).                               (11)

As r->infinity, the normalized R2 price tends to [Uraw_j+kappa Vraw_j]/Inf_j(g), and the actual normalized decrement tends to Delta_{j}/Inf_j(g). This is an exact first-order interface; raw upper prices are not asserted to equal actual physical decrements.

## 4. The C013 amplified/balanced family has phi tending to zero

Let a fixed nonconstant Boolean seed f have mean mu0, set g_m=z product_(j=1)^m f(x_j), r_m=ceil(2log2(m+1)), p_m=2^-r_m, and F_m=activate(g_m,r_m). Let v_m=mu0^(2m). g_m is balanced, Inf_z(g_m)=1, and only its coefficient at {z} collides with the empty-data sector at this singleton. Hence exactly

    beta_z(F_m)=p_m v_m,
    B_z(F_m)=(p_m-p_m^2)Phi(1,v_m)+Phi((1-p_m)^2,p_m^2 v_m).  (12)

The singleton physical entropy decrement obeys L_z<=B_z+kappa beta_z by the independently reconstructed elementary two-point channel bound. Thus

    phi(F_m)<=L_z/Inf_z(F_m)<=u_m,
    u_m=(1-p_m)Phi(1,v_m)+Phi((1-p_m)^2,p_m^2v_m)/p_m+kappa v_m.

For v_m>0,

    u_m<=v_m[(1+p_m)log2(1/v_m)+1+3log2(euler)
                 +p_m(2r_m+log2(euler))].             (13)

This uses Phi(a,b)<=b[log2((a+b)/b)+log2(euler)], with (1-p)^2+p^2 v<=1. Since |mu0|<1 for a nonconstant sign, the right side tends to zero exponentially in m. For mu0=0 all quantities in (12) vanish exactly: the balancing spectral bit is determined by the rest, and L_z=0.

Therefore phi(F_m)->0, while H(F_m)/I(F_m)->H(f)/I(f) by the exact activation identity (1), and I(F_m)->0. For any fixed C>0, eventually u_m<C. If the seed violates C, then eventually D_C(F_m)>0 as well, and R2 fails already at the balancing singleton: its left side is Cp_m+D_C(F_m)>Cp_m while its right side is <=p_m u_m<Cp_m. This is a quantitative obstruction to genuine criticality, despite preservation of the arbitrary seed ratio. Neither an unbounded Boolean ratio nor a universal restriction theorem is inferred.

## 5. Review and the remaining unsupported line

Independent review of A051's descent squeeze accepts that analytic claim without accepting its separate NAND census. Independent review of the analytic portion of A052's singleton-collapse claim accepts only the distributional theorem and explicit tensor controls, not the unreplayed 1,150 finite decisions. These reviews prevent opening a new broad conjecture behind an uncleared review queue.

The first unsupported universal line is a uniform bound on actual retained conditional spectral entropy, or on the raw-indicator lambda interface, for genuine all-child-certified critical sources without relying on the exposed arbitrary violating core. The rare-activation family itself has cheap balancing descent; it cannot establish a hard critical obstruction. NEXT should use actual joint-channel/child-slack data on the existing NAND false-negative block, not enlarge this completed activation census.

## 6. A certified first-failure boundary with numbers

Use f=1-2*1_0 on three bits, H(f)=4-(9/8)log2(3), I(f)=3/4, and g=z f. Set C=2. Its seed deficit delta=5/2-(9/8)log2(3) is positive (about 0.716917186689 bits). All displayed decimals below are rounded displays of rational interval certificates, not sign proofs.

At r=1, D_C(F)/p=delta. Each of the three original data singleton comparisons has exactly zero criticality residual, because its L_i/p is H(f)-1 and C Inf_i/p+D_C(F)/p equals the same expression. For the balancing singleton, L_z/p=2.814441635490..., while C+D_C(F)/p=2.716917186689...; its actual comparison passes. The control's actual price is 4 and its comparison also passes. Every R2 singleton comparison passes too. Nevertheless the proper block comprising z and the sole control has L_A/I_A=2, and its necessary criticality comparison falls short by p delta>0. The exact finite minimum is phi(F)=2. Thus passing all root singleton averages or R2 tests does not imply passing every proper block or every individual descendant.

At r=2, D_C(F)/p=3.584585933443..., so the left side per unit p for z or a control is 5.584585933443.... The actual prices are L_z/p=3.279827850181... and L_control/p=4.867668746755..., hence both singleton averaged comparisons now fail. Their R2 upper prices are 3.499329638273... and 5.557879065751..., respectively. The R2 failure gaps are therefore 2.085256295171... and 0.026706867692...; both are rigorously positive. Along these fixed-core rarities, the first explicit mixed-block averaged failure occurs already at r=1, while the first root singleton averaged-decrement and root singleton-R2 inequality failures occur at r=2. There is no universal chronological ordering of blocks; these statements refer to this fixed seed, C and r=1,2 boundary.

An individual singleton child already violates C at r=1: fixing z to its positive sign leaves the four-bit point defect. Its influence is 1/2, and its nonempty spectral atoms alone contribute 15*(1/64)*6=45/32 entropy bits. Its empty atom contributes positively, so its C=2 deficit is strictly greater than 13/32. Thus passing the averaged singleton comparisons never certified the individual children. The r=2 boundary above concerns detection by root inequalities, not the first existence of a violating singleton child.

More generally for g_m=z f^(tensor m), the block of all controls plus z exposes +/-f^(tensor m) with total probability p. It always has

    L_A-C I_A-D_C(F_m)=-p m D_C(f).                   (14)

So the block fails for any violated seed threshold, even when an earlier root R2 singleton test does not yet fail. Equation (14) retains the terminal core cost and is not a component-pruning inference.

In the corresponding physical stopping tree the terminal entropy is exactly p m H(f), and terminal influence is p m I(f). Cheap root balancing descent does not pay these terminal quantities: the two balancing children are activations of +/-f^(tensor m), still retaining the arbitrary seed. Thus phi(F_m)->0 and full-FEI hardness of the activation class are compatible. The class does not certify its own arbitrary terminal cores, and the remaining deficit p m D_C(f) in (14) must be retained in any C019 handoff.
