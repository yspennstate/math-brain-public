# Independent A097 negative-cell floor reconstruction

All costs are ideal bits on uniform physical cubes. Put n=a+b, s=2^-a, t=2^-n, p=2^-r, mu=1-2s, rho=4pt, lambda=2p*2^-b. At a zero point the actual sign is F=1-2A_a+2A_rD_n. Translating the active/control/dummy point changes Fourier signs but preserves probabilities, physical influences and this construction.

An active data coordinate has original influence 2s and loses 2pt; each dummy coordinate gains 2pt; each control coordinate has influence 2pt. Thus I_g=2as, C=2ptb, E=2pta, J=2rpt and I_F=I_g+C-E+J. In particular E/I_g=p*2^-b<=1/2. These are actual edge changes, including destruction, not only the net influence increase.

Let P be the source spectrum. Its amplitudes are mu at empty, -2s on nonempty active-only sets and zero elsewhere. Summing the control spectral atoms of the point edit gives q_T=P_T+rho*ghat(T)+rho*t. Since rho=2s*lambda, this is precisely

    q=(1-lambda)P + lambda*mu*delta_empty + rho*U_n.

The weights sum to one and are nonnegative; rho>0 supplies positive mass on every data set. This identity is reconstructed directly for all widths rather than invoking the broader A086 floor theorem.

For any normalized supplied R with finite source cost c, calibrate R0(empty)=mu^2 and preserve its conditional nonempty law. Its cost c0=c-D_Ber(mu^2||R(empty)) is at most c. Finite c excludes an all-vacuum R because P has positive nonempty mass. The calibrated law may still vanish off source support. Set Rprime to the same three-component mixture with P replaced by R0, and use Q(U,T)=Rprime(T)*P_F(U,T)/q(T). It is a complete probability law; off-source reference zeros are covered by its uniform floor. True conditional output zeros have zero Q and do not incur false success mass.

In the augmented label/data distributions use identical weights and components (P,delta_empty,U)/(R0,delta_empty,U). Their joint KL is (1-lambda)D(P||R0). Disintegration over the observed data set T gives

    D(P_F||Q)=D(q||Rprime)=(1-lambda)D(P||R0)-kappa,

where kappa is the actual posterior-label KL for this same reference. No generic replacement or renewed posterior supplies that credit.

For a>=2, mu>=1/2 and t<=s<=1/4. Empty calibration makes q0=Rprime0=mu^2+rho(mu+t). Put v=1-mu^2, A=(1-lambda)v, B=rho(1-t), M=A+B=1-q0<=v. The nonempty true/reference conditional laws mix the original source conditional and the uniform nonempty law with weights A/M,B/M. Applying the elementary complete-reference mixture inequality to these two labels, and subtracting c0, gives

    CE(q,Rprime)-c0 <= L(q0)-L(mu^2)+L(M)-L(v)
                       +B*log2(2^n-1)+phi(A,B).

The discarded source conditional term is (A-v)*CE(P_positive,R0_positive)<=0, so its removal has the correct sign. Here L(x)=-x log2 x and phi(A,B)=M*h2(B/M). Since q0>=mu^2>=1/4, L'(x)<=1 on the vacuum interval; q0-mu^2=rho(mu+t)<=rho. On (0,1], L'(x)>=-1/ln2, yielding L(M)-L(v)<=rho/ln2. The sum is therefore less than 4rho. Continuous zero limits cover boundary sectors.

We have v<=4s, B>=3rho/4 and M/B<=(4/3)*2^(b+r). The elementary binary bound h2(x)<=x log2(e/x) gives phi(A,B)<=rho*(b+r+2), using log2(4/3)<1/2 and 1/ln2<3/2. The local subset bill is at most rho*n. Hence CE(q,Rprime)<=c+rho*(n+b+r+6).

Every nonempty control set has marginal mass 4p^2t, so their combined probability V=rho*(1-p). Therefore the conditional control entropy is at most

    H(S_controls)=h2(V)+V*log2(2^r-1)
       <=rho*(1-p)*(log2(e/rho)+r)<=rho*(n+2r).

The cancellation of log2(1-p) is retained; log2(e)<2 supplies the last inequality. Combining costs and using b<=n,n+r>=3 gives

    CE_F<=c+rho*(2n+b+3r+6)<=c+5rho*(n+r)
         =c+10(C+E+J).

For a=1, mu=0 and lambda=rho, so the data mixture has only source and uniform components. Directly CE(q,Rprime)<=c+rho*n+h2(rho)<=c+rho*(2n+r); adding control entropy gives c+3rho*(n+r)=c+6(C+E+J), which implies the stated bound even at n=r=1. The constants follow from ln2>2/3 and ln2<1: the positive atanh series gives ln2>2/3, while integrating 1/x<1 on (1,2) gives ln2<1. Squaring 4/3 proves log2(4/3)<1/2. No unreviewed constant estimate is used.

For every K>=10 subtract this complete cost from K I_F:

    K I_F-CE_F >= (K I_g-c)+(K-10)C-(K+10)E+(K-10)J.

If c<=C0 I_g, set K=2C0+10. Created/control coefficients are nonnegative and E<=I_g/2; the remaining source-minus-erasure bank is at least [K-C0-(K+10)/2]I_g=0. This spends the bank once. Structural R=P has H_g<4I_g: for a>=2, v=4s(1-s), L(mu^2)<=v/ln2 and the other contribution is v*(2a-2), strictly less than 8as. For a=1 the entropy is zero. Thus this structural floor has CE_F<=18I_F.

For any independent Boolean terminal h with complete finite-cost R_h, product probabilities and physical influences give exactly CE_total=c_h+CE_F, D_total=D_h+(1-lambda)D(P||R0)-kappa, and I_total=I_h+I_F. The terminal cost is retained with coefficient one and supplies no floor reserve. If c_h<=C_h I_h, payment follows at max(C_h,2C0+10).

This reconstructs all clauses of A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK@1 without repairing them. It does not accept A086's broader subprobability/72-tax theorem. The first unpaid hereditary line remains transporting the incoming Q through an actual active-bit restriction and paying child normalizers/reset from the same unused bank. Closure of the Boolean formula family does not imply closure of an arbitrary supplied reference; the point-edit floor must not be freshly financed at every descendant.
