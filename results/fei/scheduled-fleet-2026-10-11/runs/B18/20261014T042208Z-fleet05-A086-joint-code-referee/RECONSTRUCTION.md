# Independent paid-reference audit and unequal-amplitude continuation

All CE, entropy and KL are bits. Actual uniform finite physical cubes only. References are fixed before sampling, subprobability mass is retained, and one-word prefix rounding is separate. A011's source is read-only. No substantive source repair is supplied.

## 1. Actual signed point-edit law and physical accounts

Let g on m data bits be Boolean and edit one point (x*,y*) with r>=1 fresh point controls. Write p=2^-r,t=2^-m, F=g(1-2 1_x* 1_y*), a_T=ghat(T), b_T=g(y*)chi_T(y*) and rho=4pt. Walsh expansion gives
Fhat(empty,T)=a_T-2pt b_T,
Fhat(U,T)=-2pt b_T chi_U(x*) for nonempty U.
Consequently the data marginal is q_T=a_T^2-rho b_T a_T+rho t. Its sum is one by Fourier inversion at y*. This is a signed expression; a positive mixture is not automatic for arbitrary amplitudes.

Let j be the number of originally pivotal data edges at y*. The edit removes those j data edges and creates m-j. Each change is encountered at one control point and one data edge, so C=2pt(m-j), E=2ptj, I_data=I(g)+C-E. Each fresh control has influence 2pt, so I_sel=2rpt=rho r/2 and I(F)=I(g)+C-E+I_sel. These identities are also checked by independent physical edge enumeration, not only spectral weights.

All nonempty selector-frequency atoms have identical probability 4p^2t^2. Their total probability is V=4p(1-p)t=(1-p)rho, and the selector marginal is uniform on 2^r-1 nonempty choices. Thus B=H(S_controls|S_data)<=H(S_controls)=h2(V)+Vlog2(2^r-1). The bound h2(v)<=v log2(1/v)+v/ln2 and the exact identity log2(2^r-1)=r+log2(1-p) cancel the apparent log(1-p) loss. Since log2(1/V)=m+r-2-log2(1-p),
B<=V(m+2r-2+1/ln2)<=mV+2r rho=mV+4I_sel.
This proves the all-r bound independently; finite checks merely validate it.

## 2. Fixed positive inherited reference shock: A011 source clause HOLDS

For g=chi_A, k=|A|>=1, a_T=1_{T=A} and b_A=1, so
q=(1-rho)delta_A+rho U_m.
I(g)=k, j=k, C=2pt(m-k), E=2ptk. At m4,k2,r1 the data change is neutral, C=E=1/8, I_sel=1/16 and I=33/16. Every non-A data set has probability rho t=1/128.

For integer L>=1, let R_L(A)=1-15*2^(-L-4), R_L(T)=2^(-L-4) otherwise. These masses sum to one, are strictly positive, and R_L(A)>1/2 proves c_L=log2(1/R_L(A))<1 without factoring a huge integer. The lift Q_L=R_L times the actual conditional control kernel has CE=CE(q,R_L)+B, hence CE>=15(L+4)/128. L=256 gives 975/32>8*33/16=33/2. This is an infinite reference family on a fixed Boolean function, not an FEI counterfamily. Bounded source slack and physical charges cannot price this particular unchanged lift uniformly in L. Full support does not cure reference mismatch.

## 3. Independent reconstruction of A011's entire paid floor claim: HOLDS

Supply full positive data subprobability R of mass s<=1 and source c=CE(delta_A,R). Define R'=(1-rho)R+rho U_m. Let K(U|T) be the actual finite conditional control kernel and Q'=R'K. Its total mass is (1-rho)s+rho. Every true output is supported, all off-target reference mass is retained by normalized kernels, and the missing mass is explicitly allowed failure. There is no infinite success procedure: this is a finite reference distribution, or a finite reference plus failure atom. Each successful outcome identifies a physical pair (U,T), so no duplicate latent labels are transmitted. Shannon/block codes under that fixed output reference give CE+1 or asymptotic CE respectively. One-symbol rounding is not erased.

Introduce an analytical label J with true joint masses (1-rho)delta_A(T),rho U_m(T), and reference joint masses (1-rho)R(T),rho U_m(T). The label is not a fair physical-child sampler. The true conditional posterior pi and normalized reference posterior pi_R give kappa=sum_T q_T KL(pi(.|T)||pi_R(.|T))>=0. Factor the joint likelihood ratio first through J then through T. This gives
D(q||R')=(1-rho)c-kappa,
CE(P_F,Q')=(1-rho)c+rho m+h2(rho)-H(J|T)-kappa+B.
Zero-weight labels are omitted at rho=1. This retains every reference normalizer; kappa is the measured posterior KL for the same reference, not an assumed free refund.

Use nonnegativity of the subtracted terms, c>=0, h2(rho)<=rho(m+r-2+1/ln2), and section 1's B bound. Since 1/ln2<2,
CE_F<=c+rho[(3-p)m+3r-2+1/ln2]<=c+3rho(m+r)
=c+6(C+E)+6I_sel.
For any rate K, S_K=Kk-c yields exactly the source's one-use lower certificate
K I(F)-CE_F>=S_K+(K-6)C-(K+6)E+(K-6)I_sel.
The sign of the erased-edge coefficient is negative and its magnitude is K+6. It is not replaced by net created influence. This bound is sufficient, not an assertion that its right side is nonnegative for every supplied reference.

For arbitrary independent Boolean terminal h with prescribed complete reference R_h, the actual tensor and product reference have additive entropy/influence, CE=c_h+CE_F and KL=D_h+(1-rho)c-kappa. The entire c_h is retained once. We reconstruct these product likelihood identities independently and check finite terminals. The source's exact scope, including the infinite inherited-reference shock, all parity points/widths, subprobability mass, negative erased-edge debit and arbitrary-terminal tensor, therefore HOLDS without repair. No generic core floor or hereditary reserve follows.

## 4. Unequal-amplitude neutral core: complete positive mixture and paid floor

This is a separate A086 author proof pending independent review, not a repair needed for A011 acceptance. It closes A011's named next test with a nonoptimal absolute transfer coefficient.

Fix six data bits. Let g(y)=-1 exactly when its first three bits are at their specified point (take zero by translation), and +1 otherwise; the other three bits are dummies. Any of the eight negative points y* is allowed, and the control point x* is arbitrary. The source has mean 3/4, Fourier coefficients a_empty=3/4, a_T=-1/4 for the seven nonempty active-only subsets, and zero at sets meeting dummy bits. Therefore P_g(empty)=9/16, P_g(T)=1/16 on those seven subsets. I(g)=3/4. At y* every active coordinate is originally pivotal and every dummy is nonpivotal, so j=3, C=E=6pt and I(F)=3/4+I_sel.

For active-only T, b_T=-1 after the coordinate translation; more generally its phase matches the translated source coefficient. The scalar coefficient identity at the zero-point convention is
a_T=-4P_g(T)+3*1_{T=empty}
on the old active-only support. On dummy-containing T, a_T=0. Substitution into the ACTUAL signed marginal in section 1 proves for every r>=1 and every allowed edited point
q=(1-4rho)P_g+3rho delta_empty+rho U_6,
rho=4pt=2^(-r-4).
The weights w=(1-4rho,3rho,rho) are positive and sum to one. Moving the negative point among dummy coordinates or moving x* changes coefficient phases only, so this marginal identity and all costs/physical charges persist. Translating the active cell is likewise a physical coordinate sign change; no arbitrary linear influence transform is used.

Supply any fixed complete data subprobability R with finite c=CE(P_g,R), positive on the true source support (it may have zeros elsewhere), mass s<=1. Define
R'=(1-4rho)R+3rho delta_empty+rho U_6,
Q'=R'K_true.
The floor ensures full data positivity, and total output reference mass is (1-4rho)s+4rho. True supported outputs are covered. All successful output descriptions are physical subsets; the three mixture labels are analytical alternatives, not duplicated code successes.

Introduce analytical J for components (P_g,delta_empty,U_6) with prior w; reference components are (R,delta_empty,U_6). Define measured kappa from their conditional true/reference posteriors as in section 3. Exact log-sum/chain rules give
CE_F=(1-4rho)c+6rho+H(w)-H(J|T)-kappa+B,
CE_F-H(F)=(1-4rho)D(P_g||R)-kappa.
The latter is nonnegative because it is the divergence to the complete subprobability Q'. It does not replace D(P_g||R) by zero. In the cost identity all original conditional source debt remains with its explicit mixture weight; an additional independent terminal's cost has coefficient one.

Now H(w)=h2(4rho)+4rho h2(1/4), log2(1/(4rho))=r+2, and B<=6rho+2r rho from section 1. Dropping only the measured nonnegative H(J|T),kappa terms yields
CE_F<=c+rho[6r+20+4/ln2+4h2(1/4)]
<=c+rho(6r+30)<=c+72 I_sel,
using ln2>2/3, h2(1/4)<1 and I_sel=rho r/2, r>=1. The constant 72 is deliberately nonoptimal; no float optimization is used. Crucially, this payment uses the fresh controller budget although the net data influence increment is zero. It pays the replacement reference rather than claiming unchanged-R transport.

For every K, the exact inherited-slack consequence is
K I(F)-CE_F>=S_K+(K-72)I_sel, S_K=3K/4-c.
Thus supplied c<=K I(g) gives full CE_F<=max(K,72)I(F), with the inherited slack appearing once. One actual insertion is paid; no second copy of the source bank is introduced. For arbitrary independent terminal h,R_h, use R_h tensor Q': exact CE=c_h+CE_F, KL=D_h+(1-4rho)D(P_g||R)-kappa and I=I(h)+I(F). Conditional c_h<=K_h I(h) and c<=K_g I(g) give max(K_h,K_g,72) physical payment. Single-word rounding remains +1 globally.

## 5. First unsupported line and next handoff

The negative-point two-level coefficient identity above provides a positive mixture; it is not available for a general unequal-amplitude Boolean core. Nor does a one-use certificate at the root automatically remain paid after exposing an active data bit: incoming references and source slack then require actual restriction and compatible transport. The first unsupported universal line is a complete floor/reference change whose full CE and destroyed-edge debit are paid from one inherited slack for arbitrary signed magnitude profiles through that exposure. NEXT should restrict one active bit of this paid six-bit core and preserve its incoming reference, then test a positive-point edit or a source with three nonzero coefficient amplitudes where the current three-component identity fails. Another quadratic or negative-cell enumeration would leave that exact gap unchanged.
