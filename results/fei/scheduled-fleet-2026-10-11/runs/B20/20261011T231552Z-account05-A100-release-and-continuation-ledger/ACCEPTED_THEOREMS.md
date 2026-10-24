# Accepted theorem list at this stage snapshot

Prepared 2026-10-11T23:35:02.378539+00:00. Full FEI OPEN. This is the review-record inventory for supervisor adoption, not a public release or fresh independent proof audit.

Canonical claims: B05 local-refund no-go is accepted; the repaired two-bit AND margin is certified; B09 core is pending in the older registry but has a newer A093 core-only acceptance. All scopes are retained.

Published threshold-paper baselines C001-C004 and selector/composition identities remain source-reported baselines, separate from this new-campaign acceptance list. The 29-page constant (<13.415) and 38-page constant (<8.937) belong to different versions. Percolation geometry is a proper-class hypothesis; the 30/31-page overlap-exponent discrepancy is unresolved here.

## A001-FIXED-BOOLEAN-MARGINAL-TENSOR-ADMISSION @ 1

Fix any actual Boolean F0(X,Y0) on disjoint finite input groups and its X spectral marginal. Among Boolean functions with that fixed marginal and admitting fresh arbitrary data tensor factors, the optimal constant in H(S_Y|S_X)<=C I equals C_FEI as an extended-real supremum. Any fixed upper X-degree bound obeyed by F0 is preserved by the embedding.

Review evidence: A086/account05 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A086\runs\20261011T214823Z-account05-A086-joint-code-referee\CLAIMS.json

## A006-SUNFLOWER-POSTERIOR-FOREST-PAYMENT @ 1

For every integer m>=1, f_m=2*1[x0=1]*1[at least one xi=1 for 1<=i<=m]-1 on the uniform (m+1)-cube, represented as the union of the m distinct clauses (x0 AND xi), with supports ordered (0,i), M_i=1, pi_i=1/4 and lambda_i=1/m, has exact finite posterior partition weights S_B({0})=1/4, S_B(T)=m^(-t)*(a/4)^t, and S_B({0} union T)=t!*a^(t-1)/(4*m^t)*(1+(1-t/m)*a), where t=|T|>=1 and a=2^(-6/5). Its complete conditioned all-partition residual is <=(43/10) I(f_m), and its exact conditioned all-partition run-cost expectation is <=(23/2) I(f_m). A normalized prior w_k=1/((k+1)(k+2)) on lambda_i^(k)=2^(-k)/m pays at most v additional bits, giving bounds (53/10) I and (25/2) I respectively. Every point-mass posterior choice in this representation has residual/I tending to infinity as m tends to infinity.

Review evidence: A086/account05 — ACCEPT_AT_STATED_SCOPE; account05/A094, stream B19 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A094\runs\20261011T224936Z-account05-A094-proof-chain-challenger\CLAIMS.json

## A007-SHARED-CORE-ROOT-CANCELLATION @ 1

For every nonconstant finite Boolean indicator B=OR_l b_l with rho_l=E b_l>0, every r>=1 and every fixed lambda_l>0 with sum lambda_l<=1, let p=2^-r, F=2 A_r B-1 on fresh core coordinates, g=2B-1, v=Var(F), s=sum lambda_l rho_l, D=product(1+p lambda_l rho_l)-1 and delta=log2(D/(p s)). There exist distinct actual partition-forest laws with K=1 when the spectral set meets the core and 1<=K<=|T| otherwise. Their root block equals v log2(s)+v delta+r(E K-v) +E sum_roots log2(1/rho_l), with 0<=r(E K-v)<=p I(g)/2 and v delta<=(log2 e) 2rp E B. Thus normalized common-core rarity overhead is at most (log2 e) I(F), leaving base rarity and all remaining coding costs unpaid. For disjoint private conjunctions rho_l=2^-w_l and Q=product(1-rho_l), E K-v=4p^2 Q(sum rho_l-(1-Q)). All E are unconditioned spectral-weighted sums over nonempty sets; entropy units are bits. A fixed complete-reference scale prior lambda^(j)=2^-j lambda, w_j=1/((j+1)(j+2)) pays v for selecting j=0.

Review evidence: account05/A094, stream B19 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A094\runs\20261011T224936Z-account05-A094-proof-chain-challenger\CLAIMS.json

## A011-BOUNDARY-RETAINING-SELECTOR-TRANSCRIPT @ 1

For every finite uniform selector decision tree with no repeated query along any path and Boolean leaves on an independent common data cube, given complete leaf spectral prefix codes of expected costs c_l, there is a constructive cover C_l AND [g_l=1] and an exact joint spectral witness with a prefix code of expected cost 2D+sum_l p_l c_l, where p_l=2^(-d_l) and D=sum_l p_l d_l. If I_sel(F)>=gamma D and c_l<=K I(g_l), this full cost is <=max(2/gamma,K) I(F). For unsigned nonempty character leaves with repeated labels allowed, the leaf costs are zero and I_sel=B/2, where B=E_x sum_j 1[label(x)!=label(x^flip_j)]; B>=beta D gives full cost <=(4/beta) I_sel. The alternating two-label first-positive comb has D=2(1-2^(-a)), B>=D/2, I_data=1 and I_sel<1 for every a>=1, hence full cost <=8 I_sel while conjunction-cover read and a are unbounded.

Review evidence: A086/account05 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A086\runs\20261011T214823Z-account05-A086-joint-code-referee\CLAIMS.json

## A021-UNIFORM-RARE-CORE-EXPANSION @ 1

For every balanced Boolean b, integers t,k>=1, q=2^-k and c=1/ln2, F=1+A_k(product_{j=1}^t b_j-1) has H(F)=q[tH(b)+4k+2c]-q^2(2k+3c)+R(q), I(F)=q[tI(b)+k], and -2cq^3/[3(1-q)]<=R(q)<=0. The exact entropy is q t H(b)+(4q-2q^2)k-2(1-q)^2 log2(1-q); variance is 2q-q^2 and minority probability q/2. If k=o(t) and 2^-k t->0 for a fixed seed, H(F)/I(F)->H(b)/I(b) with influence tending to zero.

Review evidence: A023 — ACCEPT_AT_STATED_SCOPE; A087 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A021-CONTROL-FIRST-KL-LEDGER @ 1

For the same family, a control-first stopping tree has terminal entropy 2^-k t H(b), queried influence k2^-k, and exact magnitude-mismatch/KL debt J_tree=2^-k(k+A_k). Here A_k=sum_{s=1}^k 2^-s[2s-1+log2(1-2^(1-s)+2^(1-2s))] and there exists A in [0,3] with 0<=A-A_k<=(2k+3)2^-k. Hence J_tree<=2^-k(k+3)<=4k2^-k uniformly in tensor count. The blind rarity sum before KL subtraction is 2^-k k(k+1)/2. At each active node s, mu=2^-s and J_s=mu-mu^2+mu^2 log2((1-2mu+2mu^2)/mu^2).

Review evidence: A023 — ACCEPT_AT_STATED_SCOPE; A087 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A022-SIGNED-SURGERY-TENSOR-LOG-LEDGER @ 1

For every Boolean seed h on m>=1 uniform bits, every tensor power t>=1, and every flipped tensor vertex, write W_T=2^m hhat(T), M=#{T:W_T!=0}, rho=M/2^m, lambda=M^-1 sum_(W_T!=0) log2|W_T|, delta_t=2^-mt. For the actual fair selector between h^tensor(t) and its one-point flip, its conditional selector entropy L_t satisfies |L_t/delta_t-2(1-rho^t)-rho^t(2t lambda+log2 e)|<=12(rho/2)^t. Hence L_t/delta_t tends to 2 when rho<1 and grows as 2t lambda+log2 e+O(2^-t) when rho=1. For arbitrary finite actual flip sets D, coefficient half-difference t_S=2^-n sum_(v in D) f(v)chi_S(v), q_S=(fhat(S)-t_S)^2+t_S^2, e_S=t_S^2, mu=|D|2^-n; L=mu[log2(1/mu)-D2(e/mu||q)]+R, 0<=R<=mu/ln2. For one point e is the minority fiber mass in every packet. Adjacent flips have e_S=2 delta^2[1+epsilon(-1)^(j in S)], so mismatch occupies exactly one Fourier half-cube; the common flipped edge contributes zero to influence change.

Review evidence: A087 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A026-AFFINE4-GOOD-COORDINATE @ 1

Every nonconstant uniform-cube Boolean sign function with nonzero Fourier support of affine F2 dimension at most four, and every disjoint product of such factors, has a relevant physical coordinate i with B_i <= (7/2) I_i. This class is closed under physical restrictions and satisfies H <= (7/2+2/ln 2) I.

Review evidence: A028 — ACCEPT_AT_STATED_SCOPE; A087 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A026-AMPLITUDE-K4-THRESHOLD-NOGO @ 1

For f=+1 exactly at Hamming weights >=24 on 32 uniform sign bits, every coordinate has edge amplitude proxy A_i=2 sum_T |fhat(T) fhat(T+i)| with A_i/I_i=2220940451/536870912>4. Thus existential proxy selection with K=4 is false. No true-erasure violation or unbounded-ratio family is claimed.

Review evidence: A028 — ACCEPT_AT_STATED_SCOPE; A087 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A027-DATA-FIRST-PROPER-BLOCK @ 1

For every Boolean u on m>=1 uniform core bits, r>=1 fresh control bits, p=2^(-r), d=1-Eu, and F=1+A_r(u-1), the proper core block W satisfies B_W(F)<=p(2dm+2)<=6pm. I_W(F)=pI(u), expected terminal influence=rpd, and all leaves are constants or point defects satisfying H<=4I. For each fixed eta>0, I(u)>=eta*m implies H(F)<=max(6/eta+2/ln(2),4)*I(F) by a single-use physical stopping ledger.

Review evidence: A028 — ACCEPT_AT_STATED_SCOPE; A087 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A027-CORE-BLOCK-HARDNESS @ 1

For every Boolean core u with Eu>=0, delta=(1-Eu)/2, v=1-(Eu)^2, p=2^(-r), R0=1-4p*delta+4p^2*delta, and L the entropy of the nonempty conditional core spectrum, B_W(1+A_r(u-1))/p=v*L+4*delta*(1-p)*h2(delta)+(R0/p)*h2(p^2*v/R0). Continuous zero-mass conventions apply. A uniform core-block bound B_W<=K*p*I(u) for all such cores and r>=1 implies full FEI with constant K+2. Conversely FEI with constant C implies this block bound with constant C+5.

Review evidence: A028 — ACCEPT_AT_STATED_SCOPE; A087 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A031-SIGNED-ENTROPY-ANCHOR @ 1

For every finite uniform-cube Boolean sign f, let a_S=fhat(S), p_S=a_S^2, ell_S=log2(1/p_S) on positive atoms and a_S ell_S=0 otherwise, c_U=sum_S a_S a_(S xor U) ell_S, E_log=sum_(U nonempty)|U|c_U^2, and J_R=sum_(U nonempty)p_(R xor U)/|U|. Every occupied R obeys p_R[H(f)-ell_R]^2<=J_R E_log; also sum_(U nonempty)c_U^2=Var_p(ell). For a largest atom, H(f)<=ell_R+sqrt(J_R E_log/p_R).

Review evidence: account05/A033 — ACCEPT_AT_STATED_SCOPE; account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A031-ANCHOR-POSITIVE-PAYMENT-NOGO @ 1

There is no finite universal K with E_log(f)<=K I(f), nor any finite universal K with sqrt(J_R E_log(f)/p_R)<=K I(f) for the largest-atom anchor R of every Boolean f. The first is refuted by n-bit one-point defects with E_log/I~4n^2; the second by disjoint tensor powers of the three-bit point defect, whose anchor cost is exponentially large while influence is linear.

Review evidence: account05/A033 — ACCEPT_AT_STATED_SCOPE; account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A032-EXACT-PHASE-ADMISSION @ 1

For every uniform Boolean cube, a spectral probability law supported on at most four labels is realizable iff it is a singleton of mass1 or the uniform law on an affine plane. A uniform affine-subspace law of dimension r is realizable iff r is even, and then H=r<=2D<=2I. For arbitrary supported laws, phase realizability is equivalent to phase realizability on the support affine-span quotient. The labelled four-variable law with Walsh magnitudes (8,8,4,4,4,4,4,4,4,4,0,0,0,0,0,0) and denominator256 passes all15 separate XOR pair partitions but has no realizing phase (all512 phases certified). Complete exact enumeration on n=4 yields2261 distinct Boolean spectral laws among975621 magnitude laws satisfying square norm and necessary even/common-mod4 arithmetic.

Review evidence: account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A033-DIRECTIONAL-PHASE-BLOCK-PAYMENT @ 1

For every finite uniform-cube Boolean sign f=(-1)^P, partition X,Y, and integer d>=0, if every nonconstant GF(2) directional phase derivative partial_i P for i in X has degree at most d on all remaining physical variables, then H(S_X|S_Y)<=kappa(d) sum_{i in X} min(Inf_i,1-Inf_i), where kappa(0)=0 and kappa(d)=h2(2^-d)/2^-d for d>=1. More sharply H(S_X|S_Y)<=sum_{i in X,d_i>=1} kappa(d_i)J_i-TC(S_X)-I(S_X;S_Y). Using the separately imported physical block-channel bound, H(f)-E_t H(f_t)<=[kappa(d)+2/ln2] I_X(f). Terminal Y entropy is retained; no universal bounded d is asserted.

Review evidence: account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A036-POINT-DEFECT-TENSOR-NORMALIZED-PAYMENT-RECOVERY @ 1

For every finite disjoint tensor product of Boolean one-point defects f_m=1-2*1_point, m>=2, including physical translations, global sign, character multiplication, fresh character coordinates and irrelevant coordinates, let P=fhat^2, Q be the product of its actual spectral coordinate marginals, B=sum_i h2(P(i in S)), K=D2(P||Q), b=sign(fhat)*sqrt(Q) on the common support and zero off it, v_U=(sum_S b_S b_{S xor U})^2, Z=sum_U v_U, T=H(v/Z)-log2 Z, I=sum_i P(i in S). Then K>=max(0,B-4I), K>=T/4-8I, and B<=T/4+8I. In particular the latter two separately proved inequalities imply H(P)<=16I, while the direct factor entropy bound gives H(P)<=4I. All entropy and divergence quantities are in bits.

Review evidence: account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A037-CONDITIONAL-CREDIT-CONSERVATION @ 1

For every finite adaptive transcript tree on a common finite joint law P(W,A,L), sum_h P(h) I(W;Y_h|A,h) + sum_l P(l) H(W|A,l) = H(W|A); every cut and subtree obey the same identity. For finite common-law divergences, K_h+j_h=d_h+E_P K_hy, hence sum_h P(h)d_h+sum_l P(l)K_l=K_root+sum_h P(h)j_h. Shared channels give zero injection; replacing a predicted child reference q by r adds E_p log2(q/r) on the resource side. All terminal terms are retained.

Review evidence: A039 — ACCEPT_AT_STATED_SCOPE; account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A037-PHYSICAL-SPECTRAL-COMMON-LIFT @ 1

For every Boolean function on a finite uniform cube and every finite adaptive physical block restriction tree, the function-specific kernel k_h(y|S_0)=2^(-|B_h|) (f_h|B_h=y)hat(S_0 intersect C_h)^2 / sum_U f_hhat(U union (S_0 intersect C_h))^2, on positive fibers, constructs a common root spectral/physical-transcript law with actual fair physical branches and actual child spectra. It satisfies sum_h P(h) J_h=I(S_0;L) and H(S_0|L)=sum_h P(h) H(S_h intersect B_h|S_h intersect C_h,h)+sum_l P(l)H(f_l). No universal phase-blind channel on parent squared spectra exists, as witnessed by f=[1,1,1,-1], g=[1,1,-1,1].

Review evidence: A039 — ACCEPT_AT_STATED_SCOPE; A063 — ACCEPT_AT_STATED_SCOPE; account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A038-OCCUPANCY-CROSSLAW-AUDIT @ 1

For every finite subset law P with v=P(nonempty)>0, r_i=P(i in S|nonempty), d_i=v r_i and nonempty maximum-entropy law Q_r, K_full=D_2(P||prod Bern(d_i))=v K_occ+Delta with Delta=D_2((1-v)delta_empty+v Q_r||prod Bern(d_i))=sum_i h_2(d_i)-h_2(v)-v Hmax(r)>=0. For the actual Boolean point defect f_m, K_occ=0 and Delta>=(m-5)I; for A036's unconditioned signed collision T, T/(4I)>m-7 for every m>=8. Consequently no fixed finite kappa makes either K_occ>=T/4-kappa I or v K_occ>=T/4-kappa I universal.

Review evidence: account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A046-AND-ENDPOINT-TAX-NECESSITY @ 1

For the actual Boolean sign g(x,y)=(-1)^(xy) on independent Bernoulli inputs with P(X=1)=p and fixed P(Y=1)=q in (0,1/2), and physical reveal A={X}, the Shannon spectral/physical-channel quantities satisfy J_A-M_A=4q(1-2q)*p*log2(1/p)+O_q(p) as p tends to zero. Consequently every scalar tau(p) such that J_A<=M_A+tau(p) for all finite actual Boolean signs under every interior product bias and every singleton block of bias p satisfies liminf_{p->0} tau(p)/(p*log2(1/p))>=1/2. In particular no universal O(p) tax is valid. This does not refute B09 Delta(p), prove its optimality, or disprove uniform-cube FEI.

Review evidence: account05/A092 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A092\runs\20261011T221121Z-account05-A092-counterexample-referee\CLAIMS.json

## A056-DISJOINT-COMPOSITION @ 1

For every Boolean outer gate h and Boolean children g_i on mutually disjoint uniform physical blocks, after absorbing constant children, with m_i=E g_i, v_i=1-m_i^2>0, a_mu the output-product orthonormal Fourier coefficients and w_i=sum_{T containing i} a_mu(T)^2, E F=E_mu h, Var F=Var_mu h, H(F)=H_mu(h)+sum_i (w_i/v_i)(H(g_i)-h2(v_i)), and Inf_x(F)=(w_i/v_i)Inf_x(g_i) for x in block i. Balanced children specialize to H(F)=H(h)+sum_i Inf_i(h)H(g_i) and I(F)=sum_i Inf_i(h)I(g_i).

Review evidence: account05/A091 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A091\runs\20261011T214848Z-account05-A091-composition-referee\CLAIMS.json

## A056-PHYSICAL-RESTRICTION-SCOPE @ 1

At every fixed physical restriction, disjoint composition identities hold with newly restricted children, absorbed constants, and the outer gate reexpanded under the new child-output product law. Balance before restriction does not imply balance afterwards. For AND_2 composed with majority_3(x,a,b) and dictator z, fixing x=+1 gives E F=-1/4, I(F)=5/4, H(F)=4-(9/8)log2(3), whereas retaining the initial balanced outer law predicts -1/2, 1, and 3 respectively.

Review evidence: account05/A091 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A091\runs\20261011T214848Z-account05-A091-composition-referee\CLAIMS.json

## A061-FAIR-TREE-PROCESS @ 1

For every finite-dimensional uniform Boolean sign and fair adaptive physical restriction policy querying each coordinate at most once, with filtration given by past physical observations and an independent policy seed, H(g_t)+sum_{s<t}D_s and I(g_t)+sum_{s<t}d_s are stopped martingales, where D_s=B_s+J_s is the conditional spectral erasure plus the actual physical-child/spectral mutual information and d_s is queried influence. For tau<=n, H(f)=E H(g_tau)+E sum_{s<tau}D_s and I(f)=E I(g_tau)+E sum_{s<tau}d_s.

Review evidence: A087 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A061-LOG-COMPENSATION @ 1

On every such fair finite tree, lambda_t=sum_{T:b_T^2>0}b_T^2 log2((a_T^2+b_T^2)/b_T^2) satisfies D_t<=lambda_t+(3/ln(2))d_t. Therefore (3/ln(2))I(g_t)-H(g_t)-sum_{s<t}lambda_s is a supermartingale. If at every live node every positive b_T^2/(a_T^2+b_T^2)>=epsilon for fixed epsilon in (0,1], then C I(g_t)-H(g_t) is a supermartingale for C=log2(1/epsilon)+3/ln(2); hence H(f)<=C I(f)+E[H(g_tau)-C I(g_tau)].

Review evidence: A087 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A062-INFLUENCE-STOPPING-INTERFACE @ 1

For every finite uniform-cube Boolean f and every fair adaptive fresh-coordinate/block restriction tree, including independently randomized policies and stopping, I(f)=E sum_{t<tau} I_{A_t}(g_t)+E I(g_tau), and the same physical tree obeys H(f)=E sum_{t<tau} delta_{A_t}(g_t)+E H(g_tau). Each original coordinate separately conserves its expected queried cost plus terminal influence. These identities hold for arbitrary waiting/stopping at fixed dimension by bounded convergence. For a genuinely unbounded nonnegative process with the stated drift and integrable initial budget, cumulative costs are integrable, Fatou gives only the terminal inequality, and uniform integrability of residual influence (separately entropy) suffices for equality.

Review evidence: A087 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A062-BOOLEAN-DIMENSION-LIMIT-OBSTRUCTION @ 1

There is an actual Boolean activation family F_k=1+A_k(g_k-1), with k fair controls, p_k=2^{-k}, and balanced g_k=y_0 times 2^{k-1} quadratic bent two-bit factors, for which I(F_k)=1/2+(k+1)2^{-k}<=3/2. Stopping after control revelation gives terminal influence (2^{k-1}+1)1_{A_k} and terminal entropy 2^k 1_{A_k}; on coupled infinite fair controls they converge to zero almost surely but their expectations tend to 1/2 and equal 1. Thus bounded root influence does not imply dimension-uniform terminal uniform integrability or allow exchanging these terminal expectations with almost-sure limits. Also an activated two-bit parity has root influence 3/2 and a child of influence 2, so residual influence need not decrease pathwise.

Review evidence: A087 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A066-HEAT-ENTROPY-IDENTITY @ 1

For every Boolean sign f on every finite uniform cube, with p_S=hat(f)(S)^2, I=sum |S|p_S, H_nat=sum p_S ln(1/p_S), T_t=exp(-tL), L chi_S=|S|chi_S, q_t(S)=p_S exp(-2t|S|), G_f(t)=sum q_t(S)ln(1/p_S) and J_f(t)=sum |S|q_t(S)ln(1/p_S), G_f prime=-2J_f and H_nat=p_empty ln(1/p_empty)+2 integral_0^infinity J_f. The boundary term is between zero and I; J_f(t)<=J_f(0) and J_f(t)<=exp(-2t)J_f(0), giving integrability at both endpoints for every fixed f. For n>=1, J_f(0)<=2(n-1)ln(2)I. A universal integral bound integral J_f<=KI implies FEI in bits with constant (1+2K)/ln(2), and FEI with bit constant C implies that integral bound with K=C ln(2)/2.

Review evidence: A067 — ACCEPT_AT_STATED_SCOPE; account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A066-NO-INTEGRABLE-HEAT-ENVELOPE @ 1

There is no nonnegative measurable k with finite integral on (0,infinity) such that J_f(t)<=I(f)k(t) for every finite-dimensional Boolean sign f and almost every t. For f_n(x)=1-2 indicator{x=(1,...,1)}, n>=2, J_f_n(t)/I(f_n)=(2n-2)ln(2)exp(-2t)((1+exp(-2t))/2)^(n-1). Any such pointwise envelope must be at least ln(2)exp(-3/2)/t almost everywhere on (0,1/4]. Nevertheless integral J_f_n/I(f_n)=2(1-1/n)(1-2^(-n))ln(2)<=2ln(2). This refutes the integrable pointwise-envelope helper, not the integrated target or FEI.

Review evidence: A067 — ACCEPT_AT_STATED_SCOPE; account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A067-LOCAL-BOOLEAN-GRANULARITY @ 1

For every Boolean sign f on a finite uniform cube, write q_S=hat f(S)^2, v=1-q_empty and I=sum_S |S|q_S. For each nonzero nonempty coefficient define d_f(S)=max{|T|:T contains S and q_T>0}, and U=sum_nonempty q_S(d_f(S)-|S|). Then hat f(S) is a multiple of 2^(1-d_f(S)) and H(f)<=2I+2U-(2-log2(e))v. Thus U<=KI implies H<=(2+2K)I, and d_f(S)<=L|S| implies H<=2LI-(2-log2(e))v. Balanced support antichains give H<=2I-2. On ordinary addressing with a address variables, d_f(S)=a+1, U=a/2, and the bound gives exactly H<=2a, while generic full-cube level counting costs Theta(a^2). These are structural-regime results, not a universal payment of U or a novelty claim.

Review evidence: account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A067-MAXIMAL-SUPPORT-ENVELOPE-NOGO @ 1

No universal finite K can bound the preceding U(f) by K I(f). For p=2^(-n), n>=2, the actual Boolean dictator surgery g_n=x_1-2 indicator{x=all +} has I=1+(2n-4)p and U=n-1-(2n-4)p-4np^2, so U/I diverges. Further define the valid entropy envelope E_A=(log2(e))(1-hat f(A)^2)+2 sum_nonempty_R hat(f chi_A)(R)^2(d_(f chi_A)(R)-1) for every character anchor A. On F_n=Maj_3(z)*(1-2 indicator{y=all +}), with disjoint three-variable z and n-variable y, every E_A>=3n/2, although I(F_n)=3/2+2n2^(-n)<=5/2 and H(F_n)=2+o(1). Hence min_A E_A<=K I is false universally, including anchors outside the Fourier support. These are helper refutations, not FEI counterexamples.

Review evidence: account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A068-QUADRATIC-CONTEXT-RANK-REFERENCE @ 1

For every regular Boolean h on q distinct private data bits and every finite list of arbitrary degree-at-most-two F2 control polynomials Q_i on m independent uniform bits, F(x,z)=h(x_i*(-1)^Q_i(z)) satisfies H(F)<=C_reg*I_x(F)+2*I_z(F)<=C_reg*I(F), C_reg=log2(4+e)+2log2(e*pi)<8.937; moreover H(F)<=C_reg*D_x(F)+2*I_z(F). Its data-indexed spectral packets have exact probabilities hhat(S)^2*2^(-rank B_S) on the affine Fourier support of the quadratic phase sum_i_in_S Q_i, and a normalized rank reference pays all packet ranks. For every odd q>=5, the nonlinear cyclic controlled-majority family has I_x=q*c_q, I_z=3*q*c_q/4 and H/I<=(4*C_reg+6)/7, while it is non-unate and selector influence per control tends to zero.

Review evidence: account05/A088 — ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED @ 1

For g(X,Y)=(-1)^(XY), independent P(X=1)=1/8 and P(Y=1)=1/4, with physical block A={X}, J_A-M_A>1195/10000 bits. Thus universal tax-free J_A<=M_A under arbitrary product biases is false.

Review evidence: account05/A074 — ACCEPT_AT_STATED_SCOPE

Source: ~\mop_fei100\reports\fei-2026-10-11\CLAIM_REGISTRY.json

## B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO @ 1

For every finite K,A,B >= 0 there is a genuine Boolean physical split with L > K*d + A*V_post + B*M_inf, where q_W=(Ghat(W)^2+Hhat(W)^2)/2, e_W=(Ghat(W)-Hhat(W))^2/4, theta_W=e_W/q_W, d=sum e_W, L=sum q_W*h2(theta_W), V_post=sum q_W*(theta_W-d)^2, and M_inf=sum_i(Inf_i(G)-Inf_i(H))^2.

Review evidence: account01/B19 — ACCEPT_AT_STATED_SCOPE

Source: ~\mop_fei100\reports\fei-2026-10-11\CLAIM_REGISTRY.json

## Partial reviews

- B09-BIASED-BLOCK-UNCERTAINTY @ 1: A093 account05 B19 / ACCEPT_AT_STATED_SCOPE_CORE_ONLY / Primary Maassen-Uffink theorem matched to physical normalized fibers; independent rational child-marginal implementation
- A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER @ 1: A098 / ACCEPT_KL_CONSERVATION_SUBCLAIM_ONLY / Compatible lift global posterior credit identity, terminal-slack ceiling, and complete-charge corollaries; no acceptance of full block information theorem or all full-claim dependencies.
