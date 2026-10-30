# Three-shared-bit extremes and actual point-controlled phases

All entropy, CE and KL units are bits. Boolean signs use uniform physical cubes. This is a narrow continuation of A013's paid reference transport, consuming A012@2, not a universal FEI claim. Write B_z=H(U|T), where (U,T) is the parent squared Fourier sample split into the selector frequency U and all data frequencies T.

## 1. Independently reconstructed conserved collision budget

For arbitrary G(s,X),H(s,Y), private cubes X,Y disjoint, fresh z, put F=(G+H)/2+z(G-H)/2 and d*=min(Inf_z(F),1-Inf_z(F)). If necessary negate H to fold disagreement. This swaps selector-frequency rows without changing B_z, JS or spectral entropy; physical influence accounting uses the original d>=d*. Let a_T,b_T be the extended child coefficients, C the shared-only sets, e_T=(a_T-b_T)^2/4, delta=sum_C e_T. Then sum_all e_T=d*. Outside C at most one coefficient is nonzero, so its two selector probabilities are equal and its entropy contribution is exactly 2e_T. Thus

    B_z=2(d*-delta)+B_C.                                      (1)

If there are t shared bits, conditional means u(s),v(s) satisfy |u-v|<=1-uv, so |a_T-b_T|<=E|u-v|<=2d*. Hence delta<=min(d*,2^t d*^2). Put m_T=(a_T^2+b_T^2)/2. The shared entropy packet is sum_C m_T h2(e_T/m_T). Add a dummy row of mass 1-sum_C m_T and zero minority mass: concavity gives B_C<=h2(delta). This uses the collision influence only once.

For t=2, A012's rare calculation gives B/d*<=2+2/(sqrt(e)ln2)<4; ln2>2/3 and e>9/4 suffice for the strict sign. Its moderate calculation gives 2+4log2(5/4)<4. We reconstruct this new ownership/payment step without repair. The source's full-reference formula follows directly: calibrate each shared atom to its true mass and retain the incoming conditional private reference. Lift shared rows coherently and each private reference with weight 1/4 in each selector sector. The output KL is exactly half the calibrated child KL sum; output CE is half the calibrated child CE sum plus B_z+JS_z. This derivation confirms the new two-bit interface; it does not independently accept all bundled earlier grammar and activation claims. A013 is credited as a prior one-bit input contributor, so the local source review below is explicitly scoped and is not counted as an independent full-chain acceptance of A012@2.

## 2. Three-bit disagreement regimes, arbitrary private dimension

For t=3 and 0<d*<=1/32, delta<=8d*^2<=1/128. With f(q)=q log2(e/q)-2q, f'(q)=log2(1/q)-2>=0 below 1/4, and h2(q)<=q log2(e/q). Set x=8d*<=1/4. Equation (1) gives

    B_z/d* <=2+x[1+1/ln2-2log2 x]
            <=2+(5+1/ln2)/4 <29/8<4.                    (2)

The bracketed expression multiplied by x increases on (0,1/4]: its derivative is 1-1/ln2-2log2 x>=5-1/ln2>0. The strict bound ln2>2/3 follows, for example, from the positive atanh series whose first term at x=2 is 2/3. The continuous zero endpoint has B=0.

For d*>=1/6, maximize h2(q)-2q: its derivative vanishes at q=1/5 and its maximum is log2(5/4). Consequently

    B_z<=2d*+log2(5/4)<2d*+1/3<=4d*.                   (3)

The strict logarithm bound is certified by (5/4)^3=125/64<2. This moderate estimate actually needs no fixed-width assumption. Thus arbitrary private dimensions with three shared bits remain unresolved only when 1/32<d*<1/6 by this argument. JS_z<=2d*/ln2 is the already reconstructed coefficientwise scalar inequality, independent of shared width; the complete-reference surcharge in either closed regime is Kd*, K=4+2/ln2<7. Both calibrated terminal bills remain present.

## 3. Exact all-controller point-phase theorem

Let c be any sign on three shared bits, w any one of their eight points, V an independent r-bit private cube (r any integer >=0), A_r its all-zero point indicator (A_0=1). Define

    G=c(s), H=c(s)(1-2 1_{s=w} A_r(V)), F=mux_z(G,H).

Then d=2^(-r)/8<=1/8. Define c'_T=chat(T)c(w)chi_T(w). For every shared-only row the parent amplitudes, up to a common sign, are c'_T-d and d. All 8 minority row masses equal d^2, so delta=8d^2. Therefore

    B_z=2(d-8d^2)+sum_T E((c'_T-d)^2,d^2),             (4)
    E(a,b)=(a+b)h2(b/(a+b)), E(0,0)=0.

This is an exact actual-Boolean identity. Indeed Hhat(T)=Ghat(T)-2d c(w)chi_T(w)chi_private(T), extending Ghat by zero on private sets. The private rows are owned by H alone, so (1) evaluates their entire bill without an approximation.

There are exactly four multisets of the eight c'_T. Here is a proof rather than a search inference. Put W'_T=8c'_T; Parseval gives sum W'^2=64 and Fourier inversion gives sum W'=8. If the number of positive truth entries is even, each integer Walsh coefficient is divisible by 4. The sum of squares permits either one coefficient of magnitude 8, or four of magnitude 4. The sum condition forces respectively +8, or three +4 and one -4. If the number is odd, every Walsh coefficient is 2 mod 4. The sum of squares forces one coefficient of magnitude 6 and seven of magnitude 2. The sum condition forces either +6 with four +2 and three -2, or -6 with seven +2. Dividing by 8 gives

    (1,0^7);
    ((1/2)^3,-1/2,0^4);
    (3/4,(1/4)^4,(-1/4)^3);
    (-3/4,(1/4)^7).                                    (5)

For r>=2, d<=1/32 and (2) proves B<4d uniformly. For r=0,1, substitute (5) in (4). The eight resulting expressions 4d-B have rigorous strictly positive rational lower bounds in out/PROFILE_CERTIFICATES.json. Each expression is an exact rational linear combination of log2 primes. Bounds use ln x=2 sum_{j<20} u^(2j+1)/(2j+1)+R, u=(x-1)/(x+1), 0<=R<=2u^41/(41(1-u^2)), after reduction to x in [1,2]. Divide by outward positive ln2 bounds and respect coefficient signs. These explicit eight certificates together with (2),(4),(5) prove, for every c,w and all r>=0,

    B_z<4d, Delta=B_z+JS_z<=(4+2/ln2)d.

The all-r bridge is the analytic rare regime, not extrapolation from finite r. A private point controller is restrictive: arbitrary G(s,X),H(s,Y) can have other row masses. This theorem does not close the whole three-bit middle band.

## 4. Fixed common terminal and retained reference debt

Let q on an arbitrary independent cube Q be a common factor of both branches, with a supplied normalized finite-cost reference R_q positive on P_q. For any fixed normalized profile reference Q_F, define the full reference R_q tensor Q_F. Actual output is qF, with P_(qF)=P_q tensor P_F. Direct sums give

    CE(qF;R_q tensor Q_F)=c_q+CE(F;Q_F),
    D(P_(qF)||R_q tensor Q_F)=D_q+D(P_F||Q_F).

Also B_z(qF)=B_z(F), JS_z(qF)=JS_z(F), d_z(qF)=d_z(F) and I(qF)=I(q)+I(F). Given separately supplied factorized child references R_q tensor R_G and R_q tensor R_H, calibrate only the profile shared rows and build Q_F as in Section 1. The retained output debt is D_q plus half the two calibrated profile debts, exactly half the two full calibrated factorized child debts. The output CE is half their full calibrated costs plus Delta. Thus Section 3 pays the selector with K while retaining c_q unchanged, even though the physical shared support may now be arbitrarily large. Do not calibrate away q's individual Fourier atoms: R_q is a prescribed fixed terminal reference. Nothing bounds c_q by an absolute multiple of I(q) without a supplied certificate. This is an application of tensor transport, not a new tensor theorem or a universal overlap bound.

## 5. Physical restrictions, gates, labels and root probabilities

Physical shared-bit restrictions which miss w remove the point edit and give identical branches. Those matching w leave a phase on at most two shared bits, covered by the existing two-bit interface. Fixing a controller to 1 removes the edit; fixing it to 0 reduces r by one. Fixing z selects the actual branch. Restricting Q replaces q with its actual cofactor; it requires that cofactor's own supplied reference bill, and no parent-to-child CE contraction is asserted. The point-profile identity therefore transports through physical restrictions without any virtual restriction of a Fourier variable.

For an explicit uncompressed positive-cell ordered cover of F, let N_c be the number of positive c points. The G branch uses N_c gates of width 4 (three shared literals and one selector), and the H branch uses 2^r N_c-c(w) gates of width 4+r. Thus

    N=N_c(1+2^r)-c(w).

Composition adds exactly one selector literal incidence per branch gate and no other gates. Densities are respectively 2^-4 and 2^(-4-r). With uniform label weights 1/N, root odds are pi/N and root probabilities pi/(N+pi). Under a physical restriction, discard incompatible gates, delete fixed literals in each retained gate, let N_child count retained gates with multiplicity, and recompute pi=2^(-remaining width). Roots become pi/(N_child+pi), exactly; they need not contract. Constant children use the point-mass spectral reference; an empty cover has no roots. Arbitrary common q may use any supplied cover: disjoint positive/negative sign products give N_(qF)=N_q+ N_F+ + N_q- N_F- product gates, each literal width sums. This is a cover count identity, not a paid universal witness bound.

The coherent spectral reference has 16 shared (u,T) sectors and at most two private-owner sectors. Here G has no private sets, so at most 17 sectors are nonzero. If v_H=1-sum_C P_H=4(d-8d^2), their true label probabilities are P_F(u,T) on C and v_H/2 for H ownership. Inside this private-owner sector pay one selector bit and retain the supplied conditional private reference. Label entropy is at most log2(17), but the exact chain, not this fixed bound, is used: CE=H(labels)+(v_H/2)[1+CE(private conditional)]. For the common factor add c_q; arbitrary q references must not be silently replaced with exact spectra. No original ordered-cover L,S,R bound is claimed. The stream lead's unchanged monotonicity target remains false by the saved stage-2 R inflation example.

## 6. Source review and exact unpaid line

The source A012@2 new ownership/payment calculation in Sections 1-3 is valid without repair. Its four-bit 2-of-4 nonmember certificate was independently reconstructed: all eight cofactors use all three remaining coordinates, and all seven unordered coordinate bipartitions have a nonzero integer rank-one minor. This validates that new root-exclusion witness, not all earlier structural claims. Records will retain the source's exact statement hash and prior-contribution limitation.

First unsupported line: for arbitrary three-shared-bit children in the band 1/32<d*<1/6, their actual joint collision masses enforce B_C<=2d*+2delta. The scalar cap alone permits a maximum B/d*=2+2sqrt(2/e)/ln2>4. The point-profile classification forbids that relaxation's row configuration in the family above, but does not exclude it for arbitrary conditional means and private spectra. Any growing-width universal extension still needs a nonreused shared-core/terminal reserve; bent point-edit selector-only impossibility is already established and is not reproved here.
