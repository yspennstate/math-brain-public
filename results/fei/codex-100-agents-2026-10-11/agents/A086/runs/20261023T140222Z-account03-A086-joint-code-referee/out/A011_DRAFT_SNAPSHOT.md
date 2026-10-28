# Arbitrary physical policies for the paid finite-edit construction

Author proof; independent reconstruction pending. Base2 complete CE and divergence. Full FEI OPEN.

## 1. Exact scope and prescribed actual references

Retain the stage20 family: ANY nonconstant Boolean g on a>=1 bits, supplied complete covering subprobability R of mass s in(0,1], c=CE(Pg,R)<=C0 Ig, C0>=0. Fix b>=12 padding bits ONCE. For arbitrary finite M, widths r_j>=1 and actual previous-cube points z_j, F_j flips F_(j-1) at z_j when its r_j new controls are all0. D0=a+b, Dj=D0+sum_(i<=j)r_i, rho_j=2^-Dj. Actual signs may undo old edits. K=4C0+15 and full0<=U<=(C0+37/8)Ig are retained.

NEW: take ANY finite adaptive physical decision tree on the final N=D_M coordinates, with no coordinate queried twice along one branch. Stop anywhere; every physical frontier is a partition of the final cube. It may query source, padding, old controllers, and even coordinates unused at an earlier target prefix, in ANY interleaving. Every F_j is extended trivially to the final cube. The theorem pays its root and EVERY such frontier, for EVERY j<=M. It prices the stated complete signed-reference ledger; it does not discard negative reset credits or assert a positive-part-only bound.

Initially prescribe the ORIGINAL R at all tree nodes by physical mass-preserving restriction, embedding zero frequencies on dummy coordinates. The old complete source inheritance gives average CE<=c at every frontier, including normalized source restrictions and scalar mass penalties. It applies to any order: dummy restrictions do nothing; genuine source steps contract average complete CE, and all individual complete CEs are nonnegative.

Here is the one-step inheritance explicitly. Group parent spectra P,R by the queried coordinate, with marginal m(T)=P(T0)+P(T1), r(T)=R(T0)+R(T1). For true child law P_b use raw reference r(T)P_b(T)/m(T) if m(T)>0, and r(T) on a zero true fiber. If Z_b is its total mass, Z_0+Z_1=2s. Normalize child reference to s times raw/Z_b. The exact averaged complete child divergence is D(m||r)+(1/2)sum_b log(Z_b/s)<=D(P||R), by Jensen and log-sum; no mass penalty is removed. The child spectra average to m, so their average entropy is<=H(m)<=H(P). Adding gives average complete CE<=CE(P,R). Positive true child mass and parent cover ensure Z_b>0, including constant children. Repeating this identity along any finite adaptive tree proves the source contraction used here without a new descendant source certificate.

For a node v, let n be its number of UNQUERIED coordinates <=D_(j-1), r the number of unqueried new stage-j controls, t=2^-n, p=2^-r, rho_local=pt. Previously exposed controls are allowed, so r MAY BE ZERO and rho_local may be1. The local edit hits iff all coordinates already fixed among the first Dj match (z_j,0). A miss keeps the actual old reference, with zero new frequencies. A hit uses its ACTUAL incoming data reference Q and the same floors as before:

    beta=6rho_local (j1), 8rho_local (j2),
    beta=4 B_j rho_local (j>=3), B_j=1+4j(j+1).
    Qdata_new=(Q+beta U_n)/(1+beta).

Lift by the true conditional law of the unqueried fresh-control frequencies. When r=0 this kernel has one element and equals1, INCLUDING a zero true data fiber; retain its reference mass there. When r>=1, every true data marginal is positive. Embed zero frequencies on still-unused future coordinates. Thus old v4 references are EXACTLY unchanged in their former scope; this defines their extension at newly admitted controller-query nodes. Hit mass changes m to(m+beta)/(1+beta), miss mass remains m. No scalar mass penalty or zero-probability reference fiber is erased.

## 2. The cylinder partition identity replaces the single-active-leaf assumption

At ANY frontier, let lambda_v=2^-depth(v). Its hit leaves partition the global edit cylinder E_j={(x_<=D_(j-1))=z_j,new controls0}. Their conditional edit probabilities are rho_local(v). Therefore EXACTLY

    sum_(v hit) lambda_v rho_local(v)=Pr(E_j)=rho_j.       (1)

This permits multiple hit leaves after future coordinates have been exposed. A future query splits a cylinder without changing its total mass. Physical probability, not a spectral selector mass, is used in (1).

## 3. Reprice the existing floors, including exposed controllers

For any local Boolean h, its actual edited data marginal is

    q_T=A_T^2-4rho_local b_T A_T+4pt^2.

Young gives q<=alpha P_h+gamma U_n. Use

    j1: alpha=9/8, gamma=36rho_local;
    j2: alpha=5/4, gamma=20rho_local;
    j>=3: eta=1/[8j(j+1)], alpha=1+eta,
           gamma=4(1+8j(j+1))rho_local<=2beta.

These hold for ALL p<=1, including r=0. First/second ACTUAL floors remain6rho/8rho; gamma is only an analytical domination coefficient.

Write Z=1+beta and d=Dj (GLOBAL dimension). Always log Z<=2beta. Also log Z<=d: for j1,j2 beta<=6,8 respectively; for j>=3, Z<=5+16j(j+1)<=2^(j+5)<=2^d. The middle inequality holds at j3 and propagates because B_(j+1)<=2B_j for j>=2. The conditional fresh-control entropy is zero when r=0. When r>=1, its nonempty mass e=4p(1-p)t satisfies2rho_local<=e<=4rho_local. Jensen and h2(e)<=e log(1/e)+2e give

    H(new-frequency|data)<=4rho_local(n+2r+2)
                             <=16rho_local d.           (2)

The inequalities remain valid at n=0. Since every actual model is a subprobability, all code losses are nonnegative. The normalized floor therefore costs at most

    CE_new<=alpha CE_old+(alpha+gamma)log Z
                         +gamma[n+log(1/beta)]+Hcontrol
          <=alpha CE_old+4beta+3gamma d+16rho_local d.

Here log(1/beta)<=n+r<=d and n<=d; alpha<2. Even if log(1/beta) is negative, the displayed bound is a valid upper bound, not a discarded positive penalty. This proves the deliberately loose uniform prices

    CE_new <=(9/8)CE_old+160rho_local d       (j1),
    CE_new <=(5/4)CE_old+112rho_local d       (j2),
    CE_new <=alpha_j CE_old+64B_jrho_local d (j>=3).       (3)

They also cover n=r=0: the actual scalar mass only increases and CE drops. For r=0 and q_T=0 the one-element kernel keeps the floor mass; no division by zero or mass deletion is allowed.

## 4. Average every complete terminal and retain all signed conversions

At any fixed frontier let Cbar_j=sum lambda_v CE_j,v. Miss leaves do not change. Nonnegativity of all leaf CEs and (1) turn (3) into

    Cbar1 <=(9/8)c+160rho1D1,
    Cbar2 <=(45/32)c+200rho1D1+112rho2D2,
    Cbar_j<=alpha_j Cbar_(j-1)+64B_jrho_jDj.

Since sum_(j>=3)eta_j<=1/24, product alpha_j<=24/23. Thus for M>=2,

    Cbar_M <=(135/92)c+(24/23)[200rho1D1+112rho2D2
                                      +64sum_(j>=3)B_jrho_jDj]. (4)

Root CE has the SAME bound, with no frontier restriction. The stage20 scalar entropy comparison remains independent of policy:

    H(F_M)<=(5/4)H(g)+50sum_j j(j+1)rho_jDj.              (5)

For completeness, write F_M=g+sum delta_j and use weights1/[j(j+1)] in Cauchy, then Young eta1/4: P_FM <=(5/4)Pg+sum20j(j+1)rho_j U_Dj. The normalized exact-source mixture is used only to bound scalar entropy; its total floor is<=160*2^-(a+b)<1/2. Complete cost then gives(5). It never replaces an actual terminal reference.

For the FIXED target F_M on any physical tree, the original root CE plus all signed full-divergence resets telescopes exactly to

    L_M=H(F_M)+E D_full_terminal
       =H(F_M)+Cbar_M-E H_true_terminal.                 (6)

This keeps all physical normalizers and all complementary terminals; no claim that a target-changing operation is a KL-only reset is made. Drop only the last nonnegative entropy in(6), combine(4),(5), and put A_j=1+j(j+1), S_M=sum A_jrho_jDj. Then

    L_M <=(125/46)c+320 S_M.                             (7)

Indeed5/4+135/92=125/46. The first two error coefficients are4800/23+100 and2688/23+300; each is <=320A_1,320A_2 respectively. For j>=3 the coefficient is[1536+7294j(j+1)]/23<=320A_j. For M1,19c/8+260rho1D1 also fits(7). Root L=CE_root fits directly.

## 5. One fixed original bank, all prefixes and all policies

The geometric identities are unchanged from v4. D_j>=a+b+j and x2^-x decreases for x>=2. The exact moments sum A_j2^-j=9, sum jA_j2^-j=34 give

    S_M<=2^-(a+b)[9(a+b)+34],
    S_M/Ig<=(9b+43)/2^(b+1)<=151/8192.

For the normalized geometric majorant sum_(j=1)^M A_j(L+j)2^-j, L=a+b, the exact deficit from9L+34 is2^-M[M^3+(L+7)M^2+(5L+23)M+9L+34]. Subtracting consecutive partial sums proves the identity, and its positive polynomial tail tends to0. This is a tail identity for the majorant; arbitrary larger control widths need not give equality for S_M itself. Literal edge changes, with d_(j-1) the ACTUAL previous pivotal degree at z_j, give

    E_j=2rho_j d_(j-1), G_j=2rho_j(Dj-d_(j-1)),
    I(F_M)=Ig+sum(G_j-E_j), sum E_j<=15Ig/4096.

Consequently, at the ORIGINAL K=4C0+15 and after the FULL old U<=(C0+37/8)Ig,

    K I(F_M)-L_M-U
       >=[(6311/23552)C0+18111/4096]Ig+Ksum G_j>0.       (8)

The C0 coefficient is4*(4081/4096)-125/46-1=6311/23552. The constant is15*(4081/4096)-320*(151/8192)-37/8=18111/4096. Both are rational and positive. Source reserve S=KIg-c is not renewed. If an earlier prefix bill is already booked, its actual debit Delta=L_M-L_(M-1) gives B_M=B_(M-1)+K(I_M-I_(M-1))-Delta, with the OLD U retained. This includes target and model changes, not just a reference reset.

## 6. Exact unpaid universal line

The former controller-query policy restriction is removed for the stated conditional family and complete SIGNED ledger, at unchanged b>=12,K and full old U. No positive-part-only reset bound is claimed. The initial supplied c<=C0Ig remains essential. The edit cylinders have total measure<=2^-(a+b); arbitrary fixed-ambient targets still need a new source or a cancellation-aware representation. The saved dictator-to-parity counterexample still rules out universal affordability of the same positive weighted edit majorant. No universal FEI conclusion, arbitrary floor-class compatibility, or new initial supplier follows from(8).
