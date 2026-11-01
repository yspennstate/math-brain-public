# Shared collision code audit and reserve extraction

A086 stage 4; entropy, CE and KL in bits. Uniform finite cubes throughout. A full reference is a fixed probability on physical subsets, chosen before the output draw. A success description names a subset uniquely; latent child descriptions are summed, not separately counted as successes. Single-output integer rounding remains an additive bit.

## 1. Independent normalization, decoding and final-expectation ledger

Let G(s,X),H(s,Y) be Boolean, s a shared block of width t, X,Y disjoint private blocks, z a fresh selector, F=(G+H)/2+z(G-H)/2. Embed actual child coefficients a_T,b_T in their union cube. The parent masses at (0,T),(1,T) are A_T=(a_T+b_T)^2/4, E_T=(a_T-b_T)^2/4, with data marginal q_T=(a_T^2+b_T^2)/2. Its conditional selector row K=(A_T,E_T)/q_T is normalized. At q_T=0 use the fixed selector-absent row. This includes off-support reference fibers and prevents accidental deletion of positive reference mass.

Only shared-only sets C can collide. Partition each child subset space into individual atoms T in C and the complement. Calibrate a supplied normalized positive-support reference R at each C atom to P(T), retaining its original conditional law on the complement and assigning that complement its true mass. If true complement mass is zero it is dropped; otherwise its reference denominator is positive by finite cost. Categorical KL disintegration gives exactly c-c_cal=D(P_categories||R_categories)>=0. The conditional complement debt survives. There is no claim that computing shared coefficients is efficient or free in a generic compressed code: they are fixed instance parameters, and the resulting model and ideal CE are the mathematical interface under audit.

Embed both calibrated references and form r=(R_Gcal+R_Hcal)/2 and Q=rK. At C, r=q. Outside C any true supported data set identifies its child by physical private support. Thus posterior mismatch kappa is zero, by agreement of the true/reference child posteriors. Q sums to one, is positive on every true supported output, and retains off-target mass. Direct expansion gives

D(P_F||Q)=[D(P_G||R_Gcal)+D(P_H||R_Hcal)]/2,
CE_F=(c_Gcal+c_Hcal)/2+Delta,
Delta=H(F)-[H(G)+H(H)]/2=B_z+JS_z.

The complete output code can use Q in a finite Shannon prefix code (zero atoms omitted), with expected length <CE_F+1, or approach CE_F per output using block coding. No physical stopping label is transmitted. For one-bit s, the four shared (z-frequency,s-frequency) atoms and two private ownership sectors form six sector probabilities, equal to their true sector masses. In each private sector the selector bit is fair and the conditional calibrated private reference is transmitted. Chain rule yields H(sectors)+(v_G+v_H)/2 plus half the weighted private conditional costs. Our separate implementation verifies this chain equals CE_F, not a surrogate expectation under Q. Every root label, private bit, reference denominator and entire terminal bill is present.

Physical edge averaging gives I(F)=[I(G)+I(H)]/2+d, d=I_z=Pr(G!=H), including every shared data coordinate once. No transformed influence is substituted for this physical identity.

For use below, JS_z<=2min(d,1-d)/ln2. Here is the complete scalar proof. At a packet u=(a+b)/2,v=(a-b)/2,m=u^2+v^2 and w=2|uv|/m, its JS is m D(w)/ln2, with D(w)=((1+w)ln(1+w)+(1-w)ln(1-w))/2. The difference w/sqrt(1-w^2)-atanh(w) starts at zero and has nonnegative derivative. Integrate to get D(w)<=1-sqrt(1-w^2). The packet is therefore <=2min(u^2,v^2)/ln2. Summing and using sum v^2=d gives 2d/ln2; changing H to -H permutes selector atoms and gives 2(1-d)/ln2. Endpoints follow by continuity.

## 2. A013-ONE-SHARED-BIT-MUX-TRANSPORT@1: HOLDS at explicit interface and boundary scope

Reviewed sections 1-5 and 7 of DERIVATION.md. Positive-cell root/restriction formulas and the structural grammar in section 6 are NOT independently accepted by this review. This is a partial review of the broad bundled statement, not a proof objection to those clauses.

For one shared bit, write alpha(s)=E_X G, beta(s)=E_Y H. Choose c(s)=sign(alpha+beta), +1 at a tie. Any one-bit sign c is a constant or signed character, so multiplying both children/root by c only translates Fourier indices. Entropy, selector erasure, JS and d are unchanged. The original data influence ledger from section 1 still applies; influence of the translated functions is not used to fund anything.

Let e_s=(1-c alpha)/2, f_s=(1-c beta)/2, s_s=e_s+f_s. Then 0<=s_s<=1 and d=E(s_s-2e_s f_s)>=E(s_s-s_s^2/2). Put eta=Ee,xi=Ef,s=eta+xi. If s<=1/2, exactly two equiprobable rows give E s_s^2<=2s^2, hence d>=s(1-s). If s>=1/2, E s_s^2<=s gives d>=s/2>=1/4. This two-row fact cannot be assumed at growing shared width.

For a binary packet phi(A,B)=(A+B)h2(B/(A+B)), h2(p)<=2sqrt(p(1-p)) implies phi(A,B)<=2sqrt(AB). To prove the scalar inequality independently, G(p)=2sqrt(p(1-p))-h2(p) on (0,1/2) has second derivative [sqrt(p(1-p))/ln2-1/2]/[p(1-p)]^(3/2). Its numerator increases from negative to positive; G' decreases then increases, begins at +infinity, is negative just before 1/2 and equals zero there. Thus it has one interior sign change, and G(0)=G(1/2)=0 forces G>=0. Symmetry gives the other half. Endpoints use continuity, and ln2<1 follows from its integral.

At the translated empty data atom let mu=1-2eta,nu=1-2xi. Its erasure is <=|mu^2-nu^2|/2=2|eta-xi|(1-s). All other atoms together contribute at most their mass [(1-mu^2)+(1-nu^2)]/2. With w=|eta-xi|<=s, this gives
B_z<=2s-s^2-w^2+2w(1-s).
For s<=1/2 the expression increases on w in [0,s], giving <=4s(1-s)<=4d. For s>=1/2 use B_z<=1<=4d. Therefore Delta<=(4+2/ln2)d<7d when d>0; the d=0 case is exact. This closes all private dimensions, not merely our small truth tables.

The growing-block boundary in section 7 also holds: for even k>=4, quadratic bent b and its zero-point flip b' have coefficients sigma_T e and sigma_T e-2epsilon, e=2^(-k/2),epsilon=2^-k. Parent packet A=(sigma e-epsilon)^2, E=epsilon^2. Since (2^(k/2)-1)^2+1>=2^(k-1), phi(A,E)>=E log2((A+E)/E)>=(k-1)E. Summing 2^k packets gives B_z>=(k-1)epsilon. The stronger lower bound in section 3 below is reconstructed too. Neither is an FEI disproof. No source repair was supplied.

## 3. A095-RANK-KL-EQUIVALENCE@3: HOLDS for the new shared-width application only

This review accepts DERIVATION.md sections 1-5 and the new application in the exact statement. The older rank/KL equivalence and common-spine activation applications retained from versions 1-2 are not accepted by this run. No substantive repair to the new application is needed.

Fold by replacing H with -H if necessary, so d*=min(d,1-d)<=1/2. This preserves child squared spectra, their reference costs and all entropies, merely exchanging the two selector-frequency atoms. The actual root influence remains d, not d*. Conditional private independence gives 2d*=E_s(1-alpha beta). For real alpha,beta in [-1,1], |alpha-beta|<=1-alpha beta, because their squared difference is (1-alpha^2)(1-beta^2)>=0. Every shared-only coefficient difference therefore satisfies |a_T-b_T|<=2d*.

Let N=2^t, delta=sum_C(a_T-b_T)^2/4. Parseval gives delta<=d*, and the coordinate cap gives delta<=N d*^2. Each collision packet has mass m_T=(a_T^2+b_T^2)/2 and minority weight e_T=(a_T-b_T)^2/4. Adjoin a dummy zero-minority packet of mass 1-sum_C m_T. Concavity of binary entropy, with weights totaling one, yields B_C<=h2(delta). This uses no independence between spectral bits. Outside C the selector is fair and B_out=[2-E alpha^2-E beta^2]/2<=2d* by E(alpha-beta)^2>=0.

For t>=2, if d*>=1/N, monotonicity up to 1/2 gives B_C<=h2(d*)<=d*log2(e/d*)<=d*(t+1/ln2). If d*<=1/N, put x=N d*<=1. Then delta<=N d*^2<=1/N<=1/4 and
B_C/d*<=x log2(eN/x^2)<=log2(eN).
Indeed the natural-log derivative of x(1+ln N-2ln x) is ln N-1-2ln x>0, since ln N>=ln4>1. The zero endpoint is continuous. Combined with section 1's JS estimate,
Delta<=(t+2+3/ln2)d*.

The exact calibrated reference from section 1 retains both complete child costs, and d*<=d yields the stated conditional max-constant root payment. All off-support mass and zero complement boundaries remain included. This is uniform in private dimensions but depends linearly on shared width.

For sharpness, tensor the explicit two-bit quadratic Walsh transform (+,+,+,-)/2. For even t>=4, coefficients of b are sigma e and the zero-point flip subtracts 2epsilon. There are (2^t+2^(t/2))/2 plus signs and the complementary minus count. Each selector-absent mass A>=(9/16)epsilon and each selector-present mass E=epsilon^2. The positive packet satisfies phi(A,E)>=E log2(A/E), so B_C>=epsilon[t-log2(16/9)]. JS>=0 and d*=epsilon. One dummy shared coordinate handles odd t. Thus t-1-log2(16/9)<=kappa_t<=t+2+3/ln2 for all t>=4 and kappa_t/t->1. This is a genuine actual Boolean lower family, not a freely chosen spectral distribution. The private dimensions in the supremum create no gap in the upper proof.

## 4. A094-BALANCED-TERMINAL-TENSOR-SELECTOR-BOUNDARY@1: HOLDS, full scope

Let M select b,b'. Each bent coordinate has influence 1/2. The original zero-to-unit-vector edges are nonpivotal; flipping zero creates one boundary edge per coordinate, adding 2epsilon. Thus I(b')=k/2+2k epsilon, I(M)=k/2+(k+1)epsilon. The preceding packet bound proves Delta(M)/epsilon>=k-log2(16/9).

For ANY Boolean q on an independent block physically shared by the children, G=q b,H=q b',M_q=q M. Fourier tensor factorization gives H(M_q)=H(q)+H(M), I(M_q)=I(q)+I(M) and Delta(M_q)=Delta(M). For any complete normalized supplied R_q and Q_M, the fixed product reference has CE=c_q+c_M and KL=D_q+D_M. Expanding the product expectation proves these equalities including masses at zero true frequencies. No assumed influence bound on c_q is used.

A fresh shared character q has H(q)=0,I(q)=1 and makes both children/root balanced with zero empty atom. Since the actual M support has at most 2^(k+1) atoms, H(M)<=k+1<2[I(M)+1]. Hence H(M_q)/I(M_q)<2 while its selector-only ratio diverges. Our implementation independently checks exact tensor reference identities for every two-bit q and two prescribed references at k=4,6. No source repair was supplied; this full claim receives an independent scoped acceptance.

## 5. New signed reserve extraction on the unbalanced bent/flip stress family

This is an author proof pending independent review, with no novelty claim. It tightens A094's unbalanced support-size diagnostic by using A095's linear bound. It is a reserve certificate on the universal payment stress family, not a universal reserve theorem.

Use exact child references for b,b'. Shared-only calibration savings and posterior mismatch are BOTH zero, since the entire data cube is shared and the references are exact. Nevertheless Delta/d diverges. Thus a reserve built only from calibration savings or posterior mismatch cannot pay the excess beyond a fixed selector price on this family.

At price K=2, the actual average child slack is
S_2=[2I(b)-H(b)+2I(b')-H(b')]/2
=2k epsilon+[k-H(b')]/2>=2k epsilon,
because H(b)=k and H(b')<=k by support size. The unpaid selector excess after price two is E_2=Delta-2epsilon. The accepted linear tax gives
E_2<=(k+3/ln2)epsilon<=(2k)epsilon<=S_2
for every even k>=6, using ln2>2/3 and k>=6. Therefore the exact child-slack account, with no reuse of its separately retained terminal entropy, pays the root and proves H(M)<2I(M). At k=4, our rational log certificate proves the same strict margin directly. In fact H(M)=8-[180log2(3)+300log2(5)]/256 and 2I(M)=37/8, so the margin is [180log2(3)+300log2(5)]/256-27/8>0. Together this proves all even k>=4. The sharper assertion is separately authored; it was not needed to repair A094's original claim.

An arbitrary retained q causes no cancellation of this reserve: use R_q tensor P_M, obtaining CE=c_q+H(M)<c_q+2I(M), with exact deficit D(P_q||R_q). Conditional c_q<=K I(q) gives CE<=max(K,2)I(qM). This retains the full c_q once. The reserve was spent at the actual M node; tensor addition does not create a second allocation of it.

First unsupported universal line: the analogue of S_K>=Delta-Kd for arbitrary overlapping unequal-magnitude children, with prescribed calibrated references rather than exact entropy and with a source-compatible allocation surviving every recursive use. The family-specific edge increment 2k epsilon and support entropy bound used above do not hold for arbitrary children. Merely naming S_K is an identity, not a payment proof. NEXT should ask A097/A095 to identify a concrete reserve from actual child slack on a nonlinear, non-flat shared row, then audit its one-use transport and complete terminal costs.
