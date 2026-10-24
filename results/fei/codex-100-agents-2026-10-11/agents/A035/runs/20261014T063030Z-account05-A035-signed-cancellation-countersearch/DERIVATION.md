# A private query creates a carrier-support condition and a signed reference change

Uniform binary coordinates represent the sign cube. All functions here are actual Boolean signs and all information units are bits. Lambda denotes oriented spectral erasure, not the earlier sector mutual information.

## 1. Actual family, hypotheses, and the first hereditary step

Use the previous A035 family

    f=b_m(y) product_j b_4(x_j)
      (-1)^(p(y) sum_j 1_{x_j=0} z_j),
    p(y)=[1-(-1)^|y|(1-2 1_{y=y*})]/2,
    pi=E p=1/2+(-1)^|y*|2^-m,

with even m>=2, arbitrary L>=1, any core point y*, and independent private blocks x_j of four bits. b_r is the disjoint-pair quadratic bent sign. Any subset of selectors may first be fixed. Choose a still-free selector i and expose one actual private bit k in any module; no core coordinate is exposed. The two data outcomes have true reach1/2 within that parent. Earlier selector histories retain their original physical reach.

Write c_+=b_m 1_{p=0}, c_-=b_m 1_{p=1} and f=c_+G+c_-T with the signed private factors of the preceding run. Its core row ratio ell=hat c_-/hat b_m has at most four types. Squaring before combining c_+G and c_-T would discard the interference used below.

## 2. Exact incoming-reference transport: two conditional KL terms

For the target selector i at the parent, write normalized Fourier pair alpha(R),beta(R), d=Inf_i, mu(R)=beta(R)^2/d and r(R)=alpha(R)^2+beta(R)^2. Both laws have total1. Let R=(U,t), where t is the spectral bit of the DATA coordinate k. The incoming projected laws are

    mubar(U)=mu(U,0)+mu(U,1), rbar(U)=r(U,0)+r(U,1).

Actual physical children have SIGNED coefficients

    alpha_s(U)=alpha(U,0)+(-1)^s alpha(U,1),
    beta_s(U)=beta(U,0)+(-1)^s beta(U,1).

Let d_s=sum beta_s^2, r_s=alpha_s^2+beta_s^2 and mu_s=beta_s^2/d_s when d_s>0. Averaging the cross terms BEFORE any unsigned estimate gives

    (d_0+d_1)/2=d,
    mubar=sum_s [d_s/(2d)] mu_s,
    rbar=(r_0+r_1)/2.                                (1)

The complete physical joint pair is

    P(s,U)=beta_s(U)^2/(2d), Q(s,U)=r_s(U)/2.         (2)

Even if d_s=0, Q still has mass1/2 in that branch. With the common marginal pair mubar,rbar define

    delta=D(mu||r)-D(mubar||rbar)>=0,
    K=D(P||Q)-D(mubar||rbar)>=0.                      (3)

These are, respectively, the conditional divergence discarded by spectral data-bit collapse and the conditional physical-child divergence. They are different channels, not interchangeable posteriors. The generic KL chain rule establishes their signs, not a Boolean influence payment.

For Lambda_i=d[log2(1/d)-D(mu||r)], the exact source-owned identity is

    (Lambda_i(f|k=0)+Lambda_i(f|k=1))/2 - Lambda_i(f)
                    = d(delta-K).                   (4)

To verify (4), the physical joint KL is

    D(P||Q)=sum_s w_s D(mu_s||r_s)+D(w||fair),
    w_s=d_s/(2d), D(w||fair)=sum_s w_s log2(d_s/d).

The changed derivative normalizers and the child-flag information thus combine exactly, rather than being separately renewed from a fresh bank. The averaged child Lambda is d[log2(1/d)-D(P||Q)]. The source d and source coordinate weight d/I(f) can be retained throughout. Other coordinates and the data query's own cost remain in the complete source budget, not a separate whole I per child. Equations(1)-(4) are generic signed/Fourier and information identities; the new evidence is their checked application to genuine colliding Boolean rows and the finite structural repair below.

## 3. One private restriction: support and signed-ratio alphabets

Within the exposed module, permute its quadratic pair so the queried bit is u and its mate is v. The remaining intact pair is a,b. This permutation is an exact symmetry of b_4 and the origin indicator. For physical outcome u=1 the activation point is impossible, so G=T=(-1)^v b_2(a,b). The exposed selector is irrelevant. If another selector is the target, this module is an ordinary normalized Boolean spectator and the old trace applies after removing this inactive module from its count groups. Its terminal entropy/influence must remain.

For physical outcome u=0,

    G=b_2(a,b), independent of v,
    h_3=G (-1)^(1_{v=a=b=0} z).

The G spectrum is supported exactly at mate frequency v*=0. On that carrier Ghat=epsilon/2, epsilon=+1 at three intact-pair labels and -1 at one. The point indicator has amplitude1/8 in every retained private row. Thus

    H=0 (on carrier): T_0/G=1-epsilon/4, T_1/G=epsilon/4,
    H=1 (off carrier): G=0, T_0=-1/8, T_1=1/8.       (5)

This is the first departure from the old full-flat four-bit private factor. Both signs of (5) are retained.

If the TARGET selector belongs to this exposed module, d_0=pi/8 and d_1=0. In the active child, all H=1 rows have

    mu_0/r_0=1/(2d_0).                               (6)

They can be merged to one additional structural state with total derivative mass1/2 and reference mass pi/8. On H=0 use the previous trace: either another free selector frequency kills the G branch, giving ratios1/(10d_0) or1/(26d_0), or retain ell, the queried intact-pair sign and the two signed-factor counts. The coherent expression remains

    w=(3/4)^A(5/4)^(F-A)(1/2)^B(3/2)^(J-B),
    U=(1-ell)+ell w(1-epsilon/4), V=ell w epsilon/4,
    mu_0/r_0=V^2/[d_0(U^2+V^2)].                    (7)

Here F,J count the OTHER free and fixed-one modules. At most3+8(F+1)(J+1) states suffice: one private-off-carrier state, two other-off states, and the signed count states. This is lossless by the exact likelihood equality criterion; it is not a paid code length.

If the target selector is in an UNEXPOSED module, its d stays pi/16 in both physical children. In the active child extend the old other-off flag to include any other factor outside its G carrier, including the exposed module's mate frequency. Once G=0 the queried ratio is again1/(10d) or1/(26d). When all G factors survive, the SAME coherent w expression applies: the exposed module still contributes3/4 or5/4 if free, and1/2 or3/2 if fixed-one, but its sign multiplicities become3/1 rather than10/6. Fixed-zero factors contribute1. Thus the old count alphabet, with this additional support test and its correct masses, remains sufficient with at most2+8(F+1)(J+1) states.

For complete-law normalization in that latter active child, the restricted other module's T mass in the surviving G carrier is eta=13/16 when its selector is free, eta=3/4 when fixed to one, and eta=1 when fixed to zero. The ordinary other free factors give(15/16) each. Replace the old coherent T mass by eta*(15/16)^(number of ordinary other free factors); the complementary T mass belongs to the enlarged other-off state. Physical orthogonality c_+c_-=0 still cancels the signed cross sum. This retains every reference-only row. These arguments prove the single-private-bit trace repair for ALL stated finite m,L,points and prior selector histories; finite case checks are not an extrapolation.

## 4. An actual six-bit child refutes unchanged trace transport

Take m=2,L=1,y*=1, then physically set the first private bit to0. This is an actual six-bit Boolean child with d_0=1/32. Two retained rows share the old core ratio ell=1/2, queried intact-pair sign+1 and zero signed-factor counts. They differ only in the new mate-frequency support condition. Complete direct character sums yield

    on carrier:  signed Walsh pair (14,2), mu_0/r_0=16/25,
    off carrier: signed Walsh pair (-2,2), mu_0/r_0=16.

Both derivative probabilities are positive. Thus the old trace, if transported WITHOUT the mate support condition, is not sufficient. The lost conditional KL is rigorously in[1.504147797209,1.504147797210] bits. This is a concrete failure of an UNATTRIBUTED hereditary extension, not a refutation of the previous theorem, whose hypotheses expressly excluded private-data exposure. New support states repair it; no FEI counterexample is claimed.

The incoming reference is also NOT the actual active-child reference. At those two rows the exact pairs are

    on carrier:  rbar=25/1024, r_0=25/512;
    off carrier: rbar=33/1024, r_0=1/512.

The incoming derivative law mubar equals mu_0 because the other child's derivative vanishes. Replacing only its reference by r_0 nevertheless changes KL substantially. The complete physical joint Q gives the inactive child reference mass1/2. If that branch is discarded and the remaining Q renormalized, the joint KL drops by EXACTLY one bit:

    D(P||Q)=1+D(mu_0||r_0).

The removed reference branch therefore changes the source-owned averaged price by exactly d=1/64. Its own Boolean function is nonconstant, and its terminal H/I are not zero.

For this minimal witness, direct-character certificates also give

    delta in[0.021845011081,0.021845011082],
    K in[2.522197059679,2.522197059680],
    signed reset E_mu0 log2(rbar/r_0)=K-1,
    mean child Lambda-parent Lambda
       in[-0.039068000760,-0.039068000759].

The formula(4) agrees with independently computed parent and child prices. A different actual fixture m=2,L=2,y*=1, expose a bit of module0 and query module1 with no previous selector restrictions has POSITIVE averaged drift in[0.000531915908,0.000531915909]. Thus neither monotonicity direction applies to selector Lambda under private exposure. Both signs are already rigorous; more floating search or precision is unnecessary.

## 5. Physical terminal entropy and influence stay in the ledger

After the core and remaining selectors are fixed, all private blocks are actual b_4 factors or their origin flips; the exposed block is a three-bit quadratic carrier or its origin flip, or the inactive linear-quadratic carrier. Put

    H4*=6-(27/16)log2(3), I4*=5/2,
    H3*=4-(9/8)log2(3), I3*=7/4.

For module h let a_h be its prior fixed selector value0 or1, or1/2 if it was free. Every UNEXPOSED module's physically averaged terminal costs are

    I_h=2+(pi a_h)/2, H_h=4+pi a_h(H4*-4).

For the exposed module the physical0 child has

    I_h=1+(3/4)pi a_h, H_h=2+pi a_h(H3*-2),

and the physical1 child has I_h=2,H_h=2. These costs add on each physical product leaf and are then averaged with the original reaches. They are kept separately for both data outcomes in validation.json. In particular the inactive-child reference branch cannot be replaced by zero terminal entropy.

Each listed primitive satisfies H<=2I, so the complete terminal private data bill does too. The source influence also telescopes exactly:

    I(parent)=Inf_k(parent)+(I(child0)+I(child1))/2.

Every frozen case checks this with direct physical edge counts. An independent Boolean spectator tensors each selector row pair with its SAME normalized law and retains its own H and I in source/terminal expressions. There is no vacuous one-coordinate conditional-law hypothesis.

## 6. What remains universal

The countertest closes the first private-bit support/likelihood repair and its exact two-channel reference transfer for this explicit signed family. It provides no new universal FEI constant and no universal bank paying d(delta-K). KL identities and trace sufficiency remain generic facts until a Boolean-specific unused physical reserve pays the remaining complete log price. The first unsupported line is hereditary influence payment after arbitrary non-flat/core exposure with actual child references, signed resets, and both terminal bills. NEXT should expose a shared CORE bit: the core carrier becomes an affine-support quadratic slice, point surgery can leave rows with zero carrier amplitude but opposite nonzero branch amplitudes, and the current ell ratio may fail there. Derive its signed zero-carrier state before selecting or renewing any bank. That is the next concrete gap toward full C018/C024 transport, rather than another private flat-family entropy constant.
