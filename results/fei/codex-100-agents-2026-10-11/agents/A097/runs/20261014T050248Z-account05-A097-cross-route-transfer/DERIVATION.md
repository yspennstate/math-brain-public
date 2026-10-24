# Transfer the unequal-amplitude floor into an owned erased-edge bank

Entropy, CE and KL are in bits; ordinary influence uses the original uniform physical coordinates. The underlying Boolean class is a read-once formula class already known to satisfy FEI. The result here is the complete supplied-reference transfer and the explicit source/erased-edge ownership, not a novelty claim for its entropy bound.

## 1. Actual family and source substitution

Let a>=1 active bits, b>=0 dummy data bits, n=a+b, r>=1 fresh point controls, s=2^-a,t=2^-n,p=2^-r. At the zero-point convention put g=1-2 A_a, so its negative cell contains all 2^b dummy assignments. Edit one full negative data point only when the controls equal their point:

    F=g+2 A_r D_n = 1-2 A_a(1-A_r A_b).

Translations cover any negative cell, dummy point and control point, preserving spectral probabilities and actual influences. Supply a NORMALIZED data reference R positive on the actual source support, of finite raw cost c=CE(P_g,R). Off-source zeros are allowed. Empty-calibrate R to R0(empty)=mu^2, mu=1-2s; this decreases c by exactly D_Ber(mu^2||R(empty)), and keeps its conditional nonempty law. For a=1, mu=0, this just removes the reference vacuum. All references are fixed instance parameters before the spectral draw.

Original pivotal degree at the edited data point is a. Exact physical surgery gives

    I(g)=2as, C=2pt b, E=2pt a, J=I_controls(F)=2rpt,
    I(F)=I(g)+C-E+J.

The erased term E is retained even when b=a and data influence is neutral. Put rho=4pt, lambda=rho/(2s)=2p*2^-b<=1. Walsh coefficients of g are mu at empty, -2s on nonempty active-only sets and zero elsewhere. For the actual data-frequency marginal q of F,

    q_T=ghat(T)^2+rho ghat(T)+rho t,
    q=(1-lambda)P_g+lambda mu delta_empty+rho U_n.

The component weights are (1-lambda,lambda mu,rho); they sum to one because rho=2s lambda and mu=1-2s. They are nonnegative for all a>=1. At a=3,b=3 this is EXACTLY A086's (1-4rho,3rho,rho) unequal-amplitude floor; this is the source lemma substituted with arbitrary active/dummy widths rather than an analogy. At a=1 it is A011's parity floor (1-rho)P_g+rho U_n. Zero-weight labels are omitted.

## 2. Complete reference, retained KL and analytical labels

Set R'=(1-lambda)R0+lambda mu delta_empty+rho U_n. Use the actual finite conditional control spectral kernel K(U|T)=P_F(U,T)/q(T), and Q(U,T)=R'(T)K(U|T). Since rho>0, q and R' are positive on every data set. Q is normalized and supports every true output. Zero actual conditional outputs retain zero reference probability; every success describes exactly one physical set. Mixture labels are only analytical, not an extra transmitted fair-child history. Integer-word rounding is separate.

For true/reference mixture components (P_g,delta_empty,U_n)/(R0,delta_empty,U_n) with those common weights, define kappa=sum_T q(T)D(pi_true(.|T)||pi_ref(.|T)). Exact log-sum disintegration gives

    D(P_F||Q)=(1-lambda)D(P_g||R0)-kappa,
    CE_F=(1-lambda)c0+rho n+H(weights)-H(label|T)-kappa+B,

where c0=CE(P_g,R0)<=c and B=H(S_controls|S_data). All normalizers and the entire conditional source debt remain with their explicit weight; kappa is measured for this same reference. This is not a free generic reset credit.

## 3. Paying the floor without charging its coarse label entropy

For a>=2, mu>=1/2 and t<=s<=1/4. Because the source vacuum was calibrated, R'(empty)=q(empty)=q0=mu^2+rho(mu+t). Let v=1-mu^2 and M=1-q0. The nonempty true/reference sectors have weights A=(1-lambda)v and B0=rho(1-t), M=A+B0<=v. They use the retained source conditional reference and uniform nonempty sets, respectively. Let L(x)=-x log2 x, phi(A,B0)=M h2(B0/M). The two-component complete-reference mixture bound and nonnegativity of conditional CE give

    CE(q,R')-c0 <= L(q0)-L(mu^2)+L(M)-L(v)
                     +B0 log2(2^n-1)+phi(A,B0).

This collapses the common vacuum analytically; merely dropping the original mixture posterior would charge an unneeded lambda log(1/lambda) term. No reference mass or sector label is removed from the actual complete cost.

Since q0>=mu^2>=1/4, L'(x)=log2(1/x)-1/ln2<=1, and q0-mu^2=rho(mu+t)<=rho. Hence the vacuum change is <=rho. Also L(M)-L(v)<(v-M)/ln2<3rho/2. We may conservatively bound their sum by 4rho. At zero nonempty sectors use continuous limits.

Use h2(x)<=x log2(e/x), t<=1/4, v<=4s and B0>=3rho/4:

    phi(A,B0)<=B0 log2(e M/B0)
                 <=rho[b+r+2],

because M/B0<= (4/3)*2^(b+r), log2(4/3)<1/2 and 1/ln2<3/2. The local-subset bill is <=rho n. Therefore CE(q,R')<=c+rho(n+b+r+6).

Every nonempty control set has equal marginal probability 4p^2t; total V=(1-p)rho. Consequently

    B<=H(S_controls)=h2(V)+V log2(2^r-1)<=rho(n+2r),

by h2(V)<=V log2(e/V) and cancellation of log2(1-p), as in A086's physical control lemma. Thus

    CE_F <=c+rho(2n+b+3r+6)
           <=c+5rho(n+r)=c+10(C+E+J).                 (T)

Here b<=n and n+r>=3. The elementary constants use ln2>2/3 and ln2<1. For a=1 the parity mixture directly gives CE_F<=c+3rho(n+r)=c+6(C+E+J), so (T) also holds. This includes normalized source references with zeros off support: the positive uniform floor covers them and the same finite log-sum proof applies. No generic signed profile is admitted.

## 4. Spend an actual unused source bank once

For any K>=10 put S_K=K I(g)-c. The complete-reference transfer (T) and actual edge accounts imply

    K I(F)-CE_F >= S_K+(K-10)C-(K+10)E+(K-10)J.       (S)

This is a sufficient signed certificate, not an assertion that any arbitrary incoming code is paid. Suppose the supplied raw source cost is certified c<=C0 I(g), C0>=0. Then E/I(g)=p*2^-b<=1/2. Choose K=2C0+10. In (S) the nonnegative created/control terms may be dropped and

    S_K-(K+10)E >= [K-C0-(K+10)/2]I(g)=0.

Hence the floor's complete reference satisfies CE_F<= (2C0+10)I(F), uniformly in a,b,r and the negative edited point. The source bank is debited once; it pays both the real reference change and the erased edges. No selector-only claim is made.

For the explicit structural source reference R=P_g, H(g)<4I(g): the spectrum has vacuum mu^2 and all 2^a-1 other active masses 4s^2. With v=4s(1-s), L(mu^2)<=v/ln2 and its remaining entropy is v(2a-2), giving H(g)<8as=4I(g) for a>=2; at a=1 entropy is zero. Thus this specified family has a fixed complete reference with CE_F<=18 I(F). Its FEI conclusion is already covered by read-once composition; the paid supplied-reference/erased-edge inequality is the transferred mechanism.

## 5. Arbitrary terminal and honest hereditary boundary

For any independent Boolean terminal h with prescribed normalized finite-cost R_h, the physical tensor and product reference retain exactly

    CE_total=c_h+CE_F,
    D_total=D_h+(1-lambda)D(P_g||R0)-kappa,
    I_total=I(h)+I(F).

No terminal influence funds the source edit bank. Conditional c_h<=C_h I(h) gives max(C_h,2C0+10) total payment. The full c_h is retained once, with a single global integer-rounding convention.

A negative active-bit restriction of the BOOLEAN FUNCTION moves a to a-1, and its other child is constant +1. This alone does NOT transport an arbitrary incoming reference or certify its new cost against the smaller source influence. The first unsupported universal/hereditary line is constructing the actual descendant reference and funding its reset from the SAME remaining bank. Positive-cell edits or arbitrary three-amplitude sources also lack this nonnegative three-component marginal. Naming fresh R for each restriction would change the supplied-reference problem. These gaps remain explicit.
