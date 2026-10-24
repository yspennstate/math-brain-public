# Accepted theorem and proof-status ledger, stage 3

106 exact statement/version groups have full original-scope review receipts. 14 have only partial review or an unresolved scope objection. Full FEI OPEN; current run is locally saved, not publicly released.

A100 independently accepts only A066 heat ledger v2 and A096 terminal-KL audit v1 this stage. Other entries are recorded upstream acceptance. A066 v1 and A021 expansion v1 do not regain full acceptance. Corrected versions do not erase historical objections.

## A001-FIXED-BOOLEAN-MARGINAL-TENSOR-ADMISSION @ 1

Fix any actual Boolean F0(X,Y0) on disjoint finite input groups and its X spectral marginal. Among Boolean functions with that fixed marginal and admitting fresh arbitrary data tensor factors, the optimal constant in H(S_Y|S_X)<=C I equals C_FEI as an extended-real supremum. Any fixed upper X-degree bound obeyed by F0 is preserved by the embedding.

Review scope receipts: A086/account05 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A001\runs\20261011T210330Z-account05-A001-quantifier-audit\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A086\runs\20261011T214823Z-account05-A086-joint-code-referee\CLAIMS.json

## A002-NEAR-ERASURE-MAX-CONSTANT-BRIDGE @ 1

Fix epsilon in (0,1) and finite C_epsilon>=0. If every finite uniform Boolean sign f with B(f)>=(1-epsilon)H(f) satisfies H(f)<=C_epsilon I(f), then every finite uniform Boolean sign satisfies H(f)<=max(C_epsilon,2/(epsilon ln2))I(f). Conversely universal FEI(C) gives the near-erasure premise with C_epsilon=C. No restriction closure of the near-erasure class is assumed, and the premise remains open.

Review scope receipts: account05/A005 / HOLDS_AT_ORIGINAL_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A002\runs\20261011T234442Z-account05-A002-hardness-preserving-transformations\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A005\runs\20261012T044149Z-account05-A005-noncircular-endpoint-referee\CLAIMS.json

## A079-CORRELATED-BENT-HARDNESS-TRANSPORT @ 1

For every Boolean seed f on n>=1 uniform bits with I(f)>0, the explicit basis-character tagged family F_t(x,a,b)=(-1)^(a dot b+c_b dot x)g_t(x), g_t=z product of t disjoint copies of f, k_t=tn+1, m_t=ceil(log2(k_t+1)), N_t=2^m_t, c_b=e_b for b<k_t and zero otherwise, has pairwise distinct bent data branches, dependent spectral marginals with mutual information >=h2(1/N_t), H(F_t)=tH(f)+2m_t and I(F_t)=tI(f)+J_t with m_t<J_t<m_t+2; hence its full H/I tends to H(f)/I(f). The optimal FEI constant on distinct correlated bent-branch address selectors equals the universal constant, possibly infinity. For every bent-branch selector with d data bits, H=d+E H(sigma_t), I=d/2+E I(sigma_t) with Boolean phase rows sigma_t, so a violation at C>=2 descends to a smaller phase row. For F=(-1)^(a dot b)h_b(x), a physical b-first paired stopping tree removes exactly 2m entropy and m influence while retaining E H(h_b), and aggregate erasure B(F)=m+E B(h_b)+sum_j H(S_j|V,S_-j).

Review scope receipts: account05/A002 / HOLDS_AT_ORIGINAL_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A002\runs\20261013T220534Z-account05-A002-hardness-preserving-transformations\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A079\runs\20261012T044009Z-account05-A079-correlated-auxiliaries\CLAIMS.json

## A003-OPTIMIZED-FOREST-DEBT @ 1

For a Boolean f with v=Var(f)>0, freeze any admissible conditioned-forest representation and globally feasible positive lambda and finite distinct-run sets W_A covering its nonempty spectral support. Put c=Lambda+log2 Z, t_A=sum_(r in W_A)2^(-B_lambda(A;r)), R_*=v c+sum_(A nonempty)p_A(-log2 t_A), Kref=3+2log2 3+log2(6e), and U(A)=2^(-c-Kref|A|)t_A. Then U is a subprobability, min_P(E B-H(P))=-log2 t_A, and h2(v)+Kref I+R_*=H(f)+v D(P^+||U). Consequently universal R_*<=K I implies FEI with C=2+Kref+K. Independently, B<=K I implies good-coordinate B_i<=K alpha_i and FEI(K+2/ln2); full-signed L<=K I implies FEI(K+3/ln2), while FEI(C) implies B<=C I and L<=C I. No reverse admission into the forest reference family is asserted.

Review scope receipts: A086/account05 / HOLDS_AT_STATED_SCOPE; account05/A094, B19 / HOLDS_AT_SPECIFIED_CLAUSE_ONLY

Source: ~\brain_workers\FEI100_20261011\agents\A003\runs\20261011T221324Z-account05-A003-minimal-target-formulation\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A086\runs\20261011T234041Z-account05-A086-joint-code-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A094\runs\20261012T044109Z-account05-A094-proof-chain-challenger\CLAIMS.json

## A003-PARITY-DEFECT-COMPLETE-RESIDUAL @ 1

For every n>=2, set N=2^n,d=n+1,g_n(x)=1-2*1_(x=(1,...,1)) and F_n(x,z)=g_n(x_1z,...,x_nz). Then B(F_n)=L(F_n)=0, I(F_n)=2d/N, and the single-gate conditioned forest for -F_n, ordered support 1,...,d, M=1,lambda=1,pi=1/N and the unique partition run on each nonempty A has complete residual R=(6/5)sum_(A nonempty)p_A log2[(product_(j=1..|A|) i_j)/|A|!] <=(12/5)I(F_n). Here i_1<...<i_|A| enumerate A. Its root rarity cancels against v(Lambda+log2 Z) exactly.

Review scope receipts: A086/account05 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A003\runs\20261011T221324Z-account05-A003-minimal-target-formulation\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A086\runs\20261011T234041Z-account05-A086-joint-code-referee\CLAIMS.json

## B01-MINIMAL-VIOLATOR-STRUCTURE @ 1

Let C*>=0 and let f be Boolean with m>=2 relevant coordinates such that H(f_{i,s}) <= C* I(f_{i,s}) for every relevant i and s in {+1,-1}, and r=H(f)/I(f) > C*. Then for every relevant i: (a) Delta_i(f) >= C* Inf_i(f) + (r-C*) I(f) > r Inf_i(f); (b) B_i(f) > (r-2/ln 2) Inf_i(f) and Inf_i(f) < e^3 2^{-r}; (c) H(f)-B(f) <= (2/ln 2 - (m-1)(r-C*)) I(f) < (2/ln 2) I(f), so (m-1)(r-C*) <= 2/ln 2 and B(f)/H(f) > 1-2/(r ln 2). If some Boolean function violates H <= C* I, a violator with the fewest relevant variables exists and satisfies the hypotheses.

Review scope receipts: account05/A005 / HOLDS_AT_ORIGINAL_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A005\runs\20261012T044149Z-account05-A005-noncircular-endpoint-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B01\runs\20261011T225200Z-claude-B01-erasure-fraction-localization\CLAIMS.json

## A006-SUNFLOWER-POSTERIOR-FOREST-PAYMENT @ 1

For every integer m>=1, f_m=2*1[x0=1]*1[at least one xi=1 for 1<=i<=m]-1 on the uniform (m+1)-cube, represented as the union of the m distinct clauses (x0 AND xi), with supports ordered (0,i), M_i=1, pi_i=1/4 and lambda_i=1/m, has exact finite posterior partition weights S_B({0})=1/4, S_B(T)=m^(-t)*(a/4)^t, and S_B({0} union T)=t!*a^(t-1)/(4*m^t)*(1+(1-t/m)*a), where t=|T|>=1 and a=2^(-6/5). Its complete conditioned all-partition residual is <=(43/10) I(f_m), and its exact conditioned all-partition run-cost expectation is <=(23/2) I(f_m). A normalized prior w_k=1/((k+1)(k+2)) on lambda_i^(k)=2^(-k)/m pays at most v additional bits, giving bounds (53/10) I and (25/2) I respectively. Every point-mass posterior choice in this representation has residual/I tending to infinity as m tends to infinity.

Review scope receipts: A008 / HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR; A086/account05 / ACCEPT_AT_STATED_SCOPE; account05/A094, stream B19 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A006\runs\20261011T210855Z-account05-A006-posterior-forest-optimization\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A008\runs\20261012T005959Z-account05-A008-gate-label-compression\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A086\runs\20261011T214823Z-account05-A086-joint-code-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A094\runs\20261011T224936Z-account05-A094-proof-chain-challenger\CLAIMS.json

## B02-A008-DICTIONARY-QUOTIENT-CODE @ 1

For every finite fixed rational gate table with nonempty supports, positive normalized dictionary-size and local-subset laws, the dictionary-first generator and its finite output quotient admit computable prefix decoders with each selected gate name occurring once in the record and canonical roots/attachments requiring no extra fields. On the sunflower f_m=x0-(1+x0)*prod_i(1-x_i)/2 for every integer m>=1, the specified normalized output reference has nonempty spectral expected ideal cost <25I(f_m)/4 and full-output prefix expected length <33I(f_m)/4; raw latent-record cost is at least (1-2^-m)^2 log2(m). Ordinary addressing has a dedicated exact 2a-bit code.

Review scope receipts: A006 / ACCEPT_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR; A086/account05 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A006\runs\20261011T231903Z-account05-A006-posterior-forest-optimization\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A008\runs\20261011T221357Z-account05-A008-gate-label-compression\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A086\runs\20261011T234041Z-account05-A086-joint-code-referee\CLAIMS.json

## B02-A008-UNEQUAL-READONCE-DNF-FOREST-PAYMENT @ 1

For every nonconstant uniform Boolean read-once DNF consisting of m>=1 disjoint nonempty signed conjunction clauses of arbitrary widths w_l>=1, the original conditioned forests.tex generator with the exact prime-implicant table, lambda_l=1 and one fixed order per clause has one partition-forest run per nonempty set. Its complete source residual R is <=(16/5+log2(e))*I<47I/10. The actual conditioned probabilities of these finite once-per-block zero-child runs have full nonempty spectral cross-entropy C_pf<=(26/5+2log2(3)+2log2(e))*I. Including the empty/nonempty entropy split, h2(Var f)+C_pf<67I/5. These are ideal complete-reference costs, without optional binary-prefix rounding or optional mixture-selector charges, not a new FEI class or a universal PI-J bound.

Review scope receipts: A006 / HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR

Source: ~\brain_workers\FEI100_20261011\agents\A006\runs\20261013T214427Z-account05-A006-posterior-forest-optimization\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A008\runs\20261012T005959Z-account05-A008-gate-label-compression\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A008\runs\20261013T222820Z-account05-A008-gate-label-compression\CLAIMS.json

## A006-ACTUAL-FOREST-DETERMINANT-MOMENT-BOUNDS @ 1

For every fixed finite nonconstant gate table and ordered support covers satisfying the forests.tex interface, positive feasible lambda, nonempty covered set A and eligible assignment tau, let V be the used gates and c its number of source SCCs in the directed ownership-incidence graph, e=|V|-c, and b_tau=2^(-B_nonroot). Put w_uv(x)=sum_{j in A_u intersect R_v}x_(u,j) for u!=v and use incoming Laplacian L_vv=sum_u w_uv, L_vu=-w_uv. Let T_tau(x)=sum_{R selecting one root in each source SCC} product_{r in R}pi_r det L_(V\R,V\R)(x). For the monomial map M(product x^h)=product h!, the exact sum over distinct actual once-per-gate partition-forest queue runs with this assignment is sum_r 2^(-B(A;r))=b_tau M(T_tau). Different assignments are disjoint. With T_can=T_tau(1), D_(u,j)=number of eligible child gates at attachment group (u,j), a_D=(D+1)/2 for D>=1 and a_0=1, T_can<=M(T_tau)<=min(e!T_can,T_tau(a_D)). These determinant bounds are rational for rational pi, and can be summed with the separately algebraic b_tau to bound the full optimized residual cost -log2 sum_tau b_tau M(T_tau). T_tau factors into grounded non-source SCC determinants and rarity-weighted source-SCC cofactor sums, but its factorial-moment expectation need not factor across SCCs. The e! bound is sharp on positive-mass sunflower prime-table assignments. This computes the surrogate B mass, not exact queue probabilities, and asserts no universal O(I) or FEI bound.

Review scope receipts: A007 / HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR; A008 / HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR; A010 / HOLDS_AT_WHOLE_ORIGINAL_SCOPE_NO_REPAIR; A015 / HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR

Source: ~\brain_workers\FEI100_20261011\agents\A006\runs\20261013T214427Z-account05-A006-posterior-forest-optimization\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A007\runs\20261013T220854Z-account05-A007-root-normalization\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A008\runs\20261013T222820Z-account05-A008-gate-label-compression\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A010\runs\20261014T001430Z-account05-A010-universal-residual-falsifier\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A015\runs\20261014T001450Z-account05-A015-minterm-barrier-analysis\CLAIMS.json

## A007-SHARED-CORE-ROOT-CANCELLATION @ 1

For every nonconstant finite Boolean indicator B=OR_l b_l with rho_l=E b_l>0, every r>=1 and every fixed lambda_l>0 with sum lambda_l<=1, let p=2^-r, F=2 A_r B-1 on fresh core coordinates, g=2B-1, v=Var(F), s=sum lambda_l rho_l, D=product(1+p lambda_l rho_l)-1 and delta=log2(D/(p s)). There exist distinct actual partition-forest laws with K=1 when the spectral set meets the core and 1<=K<=|T| otherwise. Their root block equals v log2(s)+v delta+r(E K-v) +E sum_roots log2(1/rho_l), with 0<=r(E K-v)<=p I(g)/2 and v delta<=(log2 e) 2rp E B. Thus normalized common-core rarity overhead is at most (log2 e) I(F), leaving base rarity and all remaining coding costs unpaid. For disjoint private conjunctions rho_l=2^-w_l and Q=product(1-rho_l), E K-v=4p^2 Q(sum rho_l-(1-Q)). All E are unconditioned spectral-weighted sums over nonempty sets; entropy units are bits. A fixed complete-reference scale prior lambda^(j)=2^-j lambda, w_j=1/((j+1)(j+2)) pays v for selecting j=0.

Review scope receipts: A086/account05 / HOLDS_AT_STATED_SCOPE; account05/A094, stream B19 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A007\runs\20261011T215236Z-account05-A007-root-normalization\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A007\runs\20261011T234502Z-account05-A007-root-normalization\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A086\runs\20261011T234041Z-account05-A086-joint-code-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A094\runs\20261011T224936Z-account05-A094-proof-chain-challenger\CLAIMS.json

## A007-INDEPENDENT-REVIEW-A009-INCIDENCE @ 1

The assertions in hash-pinned A009 INCIDENCE_OPTIMIZATION.tex hold at their exact scopes: for fixed actual-run posterior laws with nonempty gate supports and positive root parameters, F(t)=v ln(product_l(1+pi_l exp(t_l))-1)-sum_l c_l t_l is convex under sum_{l:j in R_l}exp(t_l)<=1. The stated Gibbs/Lagrangian dual L(nu,y) is a lower certificate when b_l=c_l-v Pr_nu(l in R)>=0 and its scalar infima are finite; normalized root nu, b_l=lambda_l sum_{j in R_l}y_j and complementary slackness certify equality. Joint posterior optimization is nonconvex: duplicate dictators have residual ln(1+lambda_1 lambda_2/(2(lambda_1+lambda_2))), with second derivative -1/17 at lambda_l=1/4 on the exp(t+-s) path. All r,m>=1 singleton-petal activations have the specified actual-law residual <=8I and paid prior <=10I. Geometric sunflower weights lambda_l=2^-l give positive outer pressure <41I. For all prime powers Q>=16, the affine-plane OR-of-line-conjunctions positive coordinatewise pressure is >=7I log2((Q+1)/2) for every feasible lambda and every pivotal tie decomposition; uniform weights give <=7I log2(Q+1). These are not lower bounds for PI-J or FEI.

Review scope receipts: A007 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A007\runs\20261011T234502Z-account05-A007-root-normalization\CLAIMS.json

## A008-COMPLETE-QUEUE-DEGREE-WEIGHTED-DETERMINANT-MASS @ 1

For every fixed finite original forests.tex reference with positive feasible lambda, every nonempty covered A and eligible ownership assignment tau, let V be the used gates, s_u=|A_u|, g=|V|, a=|A|, e=g minus the number of original source SCCs, D=product_all(1+lambda_l*pi_l)-1, and t_u the original size/subset probability. Let T_tau be the incoming-Laplacian forest polynomial weighted by root pi over exactly one root per original source SCC. Define N_s(x^h)=product_u[product_(j in A_u)h_j!/((c_u+1)(c_u+2)*binom(s_u+c_u-1,c_u))], c_u=sum_(j in A_u)h_j. The exact conditioned mass of all distinct actual partition-forest events with this assignment and root restriction is Q_tau=product_used(lambda_u*t_u)*N_s(T_tau)/D. Assignments are disjoint, so Q_part=sum_tau Q_tau<=Q_* is a nonempty output subprobability. For independent per-gate triples B with density 2(1-b), rate-one exponential Y, and uniform simplex Z, N_s(T)=2^(-g)E T(BYZ). With factorial surrogate operator M, 2^(-(a+g+e))*3^(-e)*M(T)<=N_s(T)<=2^(-g)*M(T). Forced e-child sunflower prime assignments have T=pi*x^e and N_s(T)=pi*e!/((e+1)(e+2)*2^e), explicitly separating surrogate credit from complete queue probability. All label, root, subset, size, attachment, child-count and final-output ambiguity factors are retained; no universal O(I) or FEI bound is asserted.

Review scope receipts: A009 / HOLDS_AT_ORIGINAL_WHOLE_SCOPE_NO_REPAIR

Source: ~\brain_workers\FEI100_20261011\agents\A008\runs\20261013T222820Z-account05-A008-gate-label-compression\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A009\runs\20261013T235139Z-account05-A009-fractional-incidence-optimization\CLAIMS.json

## A011-BOUNDARY-RETAINING-SELECTOR-TRANSCRIPT @ 1

For every finite uniform selector decision tree with no repeated query along any path and Boolean leaves on an independent common data cube, given complete leaf spectral prefix codes of expected costs c_l, there is a constructive cover C_l AND [g_l=1] and an exact joint spectral witness with a prefix code of expected cost 2D+sum_l p_l c_l, where p_l=2^(-d_l) and D=sum_l p_l d_l. If I_sel(F)>=gamma D and c_l<=K I(g_l), this full cost is <=max(2/gamma,K) I(F). For unsigned nonempty character leaves with repeated labels allowed, the leaf costs are zero and I_sel=B/2, where B=E_x sum_j 1[label(x)!=label(x^flip_j)]; B>=beta D gives full cost <=(4/beta) I_sel. The alternating two-label first-positive comb has D=2(1-2^(-a)), B>=D/2, I_data=1 and I_sel<1 for every a>=1, hence full cost <=8 I_sel while conjunction-cover read and a are unbounded.

Review scope receipts: A086/account05 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A011\runs\20261011T213831Z-account05-A011-representation-existence\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A086\runs\20261011T214823Z-account05-A086-joint-code-referee\CLAIMS.json

## A011-COMB-PHASE-REFERENCE-TRANSFER @ 1

For every finite first-positive comb on a>=1 fresh uniform physical selector coordinates, with actual Boolean leaves g_1,...,g_(a+1) on one common data cube whose entire squared Fourier spectra agree with P, and every prescribed complete data spectral subprobability reference R positive on P-support with finite cost c=CE(P,R), the explicit normalized-row output subprobability reference Q(U,T)=R(T)*sigma_That(U)^2 (a normalized empty-selector kernel on zero P fibers) has mass sum R and exact cost CE(P_F,Q)=c+sum_T P(T)H(sigma_T)<=c+C_* I_sel(F), C_*=4+2/(e ln2)<41/8. Here sigma_T is the physical scalar sign comb with labels g_jhat(T)/sqrt(P(T)). Also I_data(F)=I(g_1), CE(P_F,Q)-H(F)=c-H(g_1), and c<=K I(g_1) yields ideal full cost <=max(K,C_*)I(F). All translates and sign changes of any fixed Boolean core are admitted. Arbitrary terminal core cost and one-word integer rounding <=1 are retained; no universal common-magnitude admission or general magnitude-change payment is asserted.

Review scope receipts: A086/account05 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A011\runs\20261013T214448Z-account05-A011-representation-existence\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A086\runs\20261013T220217Z-account05-A086-joint-code-referee\CLAIMS.json

## A012-HEREDITARY-ACTIVATION-ADMISSION @ 1

For any Boolean function class C containing constants and literals and closed under sign reversal, physical coordinate restrictions, disjoint Boolean products and point activation on fresh controls, for every Boolean f and integers t,r>=1, membership of f in C is equivalent to membership of g_t=z*product_{j=1}^t f(x^(j)) and equivalent to membership of 1+A_r(g_t-1). Furthermore, Let R consist of Boolean signs with finite globally read-once AND/OR/parity/negation formula certificates, literal or constant leaves and no opaque Boolean leaves. R is closed under restrictions, sign reversal, disjoint substitution, disjoint products, balancing and point activation on fresh controls. Every f in R satisfies corrected product-biased E(f)<=C0*(I(f)-Var(f)), C0=2+4/ln(2), and H(f)<=C0*I(f) for uniform original inputs. The balanced three-bit multiplexer M(x,y,z)=(1+x)y/2+(1-x)z/2 and all its activated balanced tensor powers are outside R. Overlapping OR substitution does not preserve R. For the control-first r-bit point activation of a fresh literal y, with p=2^(-r), the expected control depth D=2(1-p), I_sel=rp, I=p(r+1), and the uncompressed two-bits-per-query transcript has cost/I=4(2^r-1)/(r+1), tending to infinity. Every exact finite spectral witness W retaining its physical leaf label satisfies H(W|S)>=D-H(F)>=2(1-p)-4rp-2p*log2(e), whose displayed lower bound tends to two bits.

Review scope receipts: A086/account05 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A012\runs\20261011T215648Z-account05-A012-sparse-activation-accounting\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A086\runs\20261011T234041Z-account05-A086-joint-code-referee\CLAIMS.json

## A012-CONTROL-FIRST-POSTERIOR-REPAIR @ 1

For every balanced Boolean g, integer r>=1 and complete nonempty core spectral subprobability reference R_g of finite cost c_g, with p=2^(-r) and F=1+A_r(g-1) on fresh independent point controls, the explicit complete output subprobability reference Q_F has vacuum mass (1-p)^2, control-only nonempty mass p^2 per set, and mass p^2 R_g(T) for every control set U and nonempty data set T. It has total mass 1-p+p sum R_g and exact cost CE(P_F,Q_F)=p*c_g+A_r, A_r=2rp(2-p)+(1-p)^2 log2(1/(1-p)^2). The sharp universal selector coefficient is max_{r>=1} A_r/(rp)=C_act=15/4+(49/12)log2(8/7) in (4.536,4.537), uniquely attained at r=3. For the true control-first witness W retaining its physical stopping/core leaf J, actual leaf spectrum and queried membership bits, H(W|S)=2(1-p)+sum_{k=1}^r 2^(-(r-k)) B_k-A_r, B_k=q_k h2(epsilon_k)+(1-m_k^2)/2, m_k=1-2^(-(k-1)), q_k=(1+m_k^2)/2, epsilon_k=2^(-2(k-1))/(2(1+m_k^2)). This posterior is independent of the balanced core and tends to two bits. Disjoint-reference composition and fresh-character balancing preserve the full core bill; no arbitrary-core influence bound or shared-control transfer is assumed.

Review scope receipts: A013/account05 / HOLDS_AT_STATED_SCOPE; A015/account05 / ACCEPT_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR; A086/account05 / HOLDS_AT_STATED_SCOPE; account05/A094, B19 / HOLDS_AT_SPECIFIED_CLAUSE_ONLY

Source: ~\brain_workers\FEI100_20261011\agents\A012\runs\20261011T234525Z-account05-A012-sparse-activation-accounting\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A013\runs\20261012T010150Z-account05-A013-representation-stability\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A015\runs\20261012T044229Z-account05-A015-minterm-barrier-analysis\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A086\runs\20261013T220217Z-account05-A086-joint-code-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A094\runs\20261012T044109Z-account05-A094-proof-chain-challenger\CLAIMS.json

## A012-DISJOINT-PRIVATE-MUX-ADMISSION @ 1

For any Boolean g(a),h(b) on disjoint uniform private cubes and a fresh physical selector z, supplied normalized spectral references can be empty-calibrated without increasing CE. For F=z?g:h the complete coherent reference in DERIVATION.md has CE_F=(CE_g_cal+CE_h_cal)/2+Delta(mu,nu), debt=(D_g_cal+D_h_cal)/2, and Delta<=(6+1/ln2)Inf_z<(15/2)Inf_z when Inf_z>0. I_data=[I(g)+I(h)]/2 and Inf_z=(1-mu*nu)/2. Two opposite shared-literal activations with disjoint private supports therefore retain half their respective weighted terminal costs and pay each physical influence once. The recursive literal/constant certificate closed under sign flips, disjoint products, fresh activation and fresh-selector disjoint-child mux has an explicit normalized calibrated output reference with CE<=(15/2)I and is hereditary under physical restrictions. For every Boolean seed f, membership of f, its fresh balanced disjoint tensor, and a fresh point activation of that tensor is equivalent. No arbitrary opaque terminal admission, general selector substitution, additional shared-private-coordinate payment, optimal constant or universal FEI is asserted.

Review scope receipts: A013/account05 / HOLDS_AT_ENTIRE_ORIGINAL_STATEMENT_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A012\runs\20261013T220914Z-account05-A012-sparse-activation-accounting\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A013\runs\20261013T222840Z-account05-A013-representation-stability\CLAIMS.json

## A016-CONNECTED-SPINE-FACTOR-REPAIR-CONTROL @ 1

For all integers a>=1 and even m>=4, the one-shared-bit Boolean family F defined in REPORT.md has n=1+am coordinates, a connected GF(2) ANF interaction graph at the root, and I(F)=a[(m-1)/2+m*delta]+[1-(-2delta)^a]/2, delta=2^-m. On the actual selector-first stopping tree, the sum of 2I(D_v), even after every disjoint independent factor is removed optimally at every node, is T_factor=a*m*delta+delta*a(a-1)[3(m-2)/4+(4m-2)delta]. At every selected descendant B_v/Inf_v>=(m-1)/2. For any fixed finite K>=0 choosing m with (m-1)/2>K makes all selected nodes bad while T_factor/I tends to infinity as a grows. This rejects only the specified selector-first rule plus factor-removal repair. Revealing the shared bit z first instead gives B_z<=1<=8 Inf_z/3, hence zero K=4 internal bad-node bill, and retains explicit terminal references with costs <=4I(z=0) and <=2I(z=1). The fixed normalized root reference Q(A,R)=[Q0(R)+Q1(R)]/4 has complete CE=am+2-[(1+delta^a)/2]log2(1+4^a)<=8I(F)/3, including every root/branch/terminal/empty-sector cost. Universal adaptive C019 and full FEI remain open.

Review scope receipts: A018/account05 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A016\runs\20261013T214508Z-account05-A016-addressing-benchmark\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A018\runs\20261013T222945Z-account05-A018-shared-data-collision-law\CLAIMS.json

## B04-SEL-LOG-SHARP @ 1

For every multiplexer F(x,y)=g_x(y) with a selector bits, Delta:=H(F)-2^{-a} sum_b H(g_b) satisfies Delta=M_W+B_W with 0<=M_W<=min(a,(2/ln2) I_sel(F)) and 0<=B_W<=a*h2(I_sel(F)/a) (h2(0)=0; for a=0 both sides vanish). Hence Delta<=min(a,(2/ln2) I_sel)+a*h2(I_sel/a)<=I_sel*log2(e^3 a/I_sel). Here M_W=a-sum_T R_T H(r_T), B_W=sum_T R_T H(nu_T)=H(S_sel|S_data) as in threshold paper Prop. 8.6 eq. (75).

Review scope receipts: A018 / HOLDS_AT_STATED_SCOPE; A018 / INDEPENDENT DERIVATION BY A DIFFERENT ROUTE AGREES; claude-B04-lead / EXHAUSTIVE EXACT-WALSH CHECKS A=1 M<=3, A=2 M<=2 (131,600 MULTIPLEXERS), 0 VIOLATIONS

Source: ~\brain_workers\FEI100_20261011\agents\A018\runs\20261012T010436Z-account05-A018-shared-data-collision-law\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B04\runs\20261011T224500Z-claude-B04-sharp-selector-debt\CLAIMS.json

## B04-BENT-SPLICE-SHARP @ 1

For even m>=2 let g_0(y)=(-1)^{y1y2+...+y_{m-1}y_m} and g_1=g_0 with the value at y=0 flipped; F(x,y)=g_x(y) (a=1). With u=2^{-m/2}: I_sel=2^{-m}=u^2 exactly and Delta=m u^2+A+B where A=-2 sum_{e=+-1} w_e (1-e u)^2 log2(1-e u), B=sum_e w_e (1-2eu)^2 log2|1-2eu|, w_e=(1+eu)/2. Consequently Delta=I_sel(m+3/ln2)-(19/(6 ln2)) I_sel^2+O(I_sel^3) and [(2/ln2)I_sel+h2(I_sel)]-Delta=(8/(3 ln2)) I_sel^2+O(I_sel^3)>0. For the t-fold tensor power (a=t selector bits, tm data bits) Delta, I_sel and the B04-SEL-LOG-SHARP bound are t times the one-bit values. Hence for every eps>0 no function psi with psi(s,a)<=(2/ln2)s+a h2(s/a)-eps s bounds Delta over all multiplexers.

Review scope receipts: A018 / HOLDS_AT_STATED_SCOPE; claude-B04-lead / CLOSED FORM INSIDE CERTIFIED ENCLOSURE AT M=2,4,6,8,10,12; SERIES COEFFICIENTS EXACT

Source: ~\brain_workers\FEI100_20261011\agents\A018\runs\20261012T010436Z-account05-A018-shared-data-collision-law\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B04\runs\20261011T224500Z-claude-B04-sharp-selector-debt\CLAIMS.json

## B04-NODE-BOUNDARY @ 1

For every Boolean f on n>=1 coordinates and every coordinate i, with D_i=(f|_{x_i=0}-f|_{x_i=1})/2 on the other n-1 coordinates: Delta_i H:=H(f)-(H(f|_{x_i=0})+H(f|_{x_i=1}))/2 <= (3/ln2) Inf_i(f) + 2 I(D_i), where I(D_i)=sum_{S contains i}(|S|-1) fhat(S)^2. The bound is first-order sharp: on the bent splice of B04-BENT-SPLICE-SHARP, Delta/bound -> 1.

Review scope receipts: A018 / HOLDS_AT_STATED_SCOPE; claude-B04-lead / ALL 65,836 BOOLEAN F ON N<=4 AND EVERY I: 0 VIOLATIONS; BENT SPLICE RATIO 0.99999982 AT M=20

Source: ~\brain_workers\FEI100_20261011\agents\A018\runs\20261012T010436Z-account05-A018-shared-data-collision-law\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B04\runs\20261011T224500Z-claude-B04-sharp-selector-debt\CLAIMS.json

## A019-FOLDED-SEPARATOR-OWNER @ 1

For arbitrary Boolean modules f_j(z,y_j) sharing one uniform separator z with mutually disjoint uniform private cubes, set J_j=(I(f_j|z0)+I(f_j|z1))/2 and fold each module by an optional selector character to delta_j=min(Inf_z(f_j),1-Inf_z(f_j)). With q_j=1-2delta_j>=0, delta_*=(1-product_j q_j)/2, Q_-j=product_(k!=j)q_k and kappa_j=I((a_j-b_j)/2) for the folded children, the folded product has private influence J=sum J_j and separator influence delta_*. Entropy and normalized-reference costs are unchanged by folding and original separator influence is at least delta_*. Its repeated-selector loss satisfies 0<=sum delta_j-delta_*<=J-delta_*, with optimal coefficient1 on J. Its exact derivative energy is I(D)=sum_j t_j, t_j=(1-Q_-j)J_j/2+Q_-j kappa_j<=J_j. Supplied finite normalized complete references of terminal costs c_0,c_1 admit a normalized root reference with CE_root<=(c_0+c_1)/2+(3/ln2)delta_*+2sum_j t_j. Thus exclusive per-module terminal allocations c_j,avg+2t_j<=KJ_j and K>=3/ln2 suffice for CE_root<=K I(original product). No universal terminal allocation or paired-row entropy-subadditivity statement is asserted.

Review scope receipts: A020 / HOLDS_AT_STATED_SCOPE_WITH_ACCEPTED_NODE_BOUNDARY_DEPENDENCY

Source: ~\brain_workers\FEI100_20261011\agents\A019\runs\20261013T235305Z-account05-A019-orthogonality-extensions\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A020\runs\20261014T002716Z-account05-A020-selector-boundary-tests\CLAIMS.json

## A021-CONTROL-FIRST-KL-LEDGER @ 1

For the same family, a control-first stopping tree has terminal entropy 2^-k t H(b), queried influence k2^-k, and exact magnitude-mismatch/KL debt J_tree=2^-k(k+A_k). Here A_k=sum_{s=1}^k 2^-s[2s-1+log2(1-2^(1-s)+2^(1-2s))] and there exists A in [0,3] with 0<=A-A_k<=(2k+3)2^-k. Hence J_tree<=2^-k(k+3)<=4k2^-k uniformly in tensor count. The blind rarity sum before KL subtraction is 2^-k k(k+1)/2. At each active node s, mu=2^-s and J_s=mu-mu^2+mu^2 log2((1-2mu+2mu^2)/mu^2).

Review scope receipts: A023 / ACCEPT_AT_STATED_SCOPE; A023 / NARROW_REPORT_ACCEPTANCE; EXACT_CLAIM_STILL_HOLDS; A087 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A021\runs\20261011T214020Z-account05-A021-rare-core-asymptotics\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A023\runs\20261011T221608Z-account05-A023-amortized-rarity-budget\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A023\runs\20261012T010933Z-account05-A023-amortized-rarity-budget\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A021-UNIFORM-RARE-CORE-EXPANSION @ 2

For every balanced Boolean b, integers t,k>=1, q=2^-k and c=1/ln2, F=1+A_k(product_{j=1}^t b_j-1) has H(F)=q[tH(b)+4k+2c]-q^2(2k+3c)+R(q), I(F)=q[tI(b)+k], where R(q)=+4c sum_{j>=3}q^j/[j(j-1)(j-2)] and 0<R(q)<=2cq^3/[3(1-q)]. Therefore [tH(b)+4k+2c-q(2k+3c)]/[tI(b)+k] <= H(F)/I(F) <= that lower bound +2cq^2/[3(1-q)(tI(b)+k)]. The exact entropy is q t H(b)+(4q-2q^2)k-2(1-q)^2 log2(1-q); variance is 2q-q^2 and minority probability q/2. If k=o(t) and 2^-k t->0 for a fixed seed, H(F)/I(F)->H(b)/I(b) with influence tending to zero. The entropy control decrement remainder G_s=R(u)-R(2u)/2 at u=2^-s, s>=2, is negative and bounded below by -8cu^3/[3(1-2u)].

Review scope receipts: A087 / HOLDS

Source: ~\brain_workers\FEI100_20261011\agents\A021\runs\20261011T232653Z-account05-A021-rare-core-asymptotics\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261012T004155Z-account05-A087-restriction-referee\CLAIMS.json

## A022-SIGNED-SURGERY-TENSOR-LOG-LEDGER @ 1

For every Boolean seed h on m>=1 uniform bits, every tensor power t>=1, and every flipped tensor vertex, write W_T=2^m hhat(T), M=#{T:W_T!=0}, rho=M/2^m, lambda=M^-1 sum_(W_T!=0) log2|W_T|, delta_t=2^-mt. For the actual fair selector between h^tensor(t) and its one-point flip, its conditional selector entropy L_t satisfies |L_t/delta_t-2(1-rho^t)-rho^t(2t lambda+log2 e)|<=12(rho/2)^t. Hence L_t/delta_t tends to 2 when rho<1 and grows as 2t lambda+log2 e+O(2^-t) when rho=1. For arbitrary finite actual flip sets D, coefficient half-difference t_S=2^-n sum_(v in D) f(v)chi_S(v), q_S=(fhat(S)-t_S)^2+t_S^2, e_S=t_S^2, mu=|D|2^-n; L=mu[log2(1/mu)-D2(e/mu||q)]+R, 0<=R<=mu/ln2. For one point e is the minority fiber mass in every packet. Adjacent flips have e_S=2 delta^2[1+epsilon(-1)^(j in S)], so mismatch occupies exactly one Fourier half-cube; the common flipped edge contributes zero to influence change.

Review scope receipts: A087 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A022\runs\20261011T215800Z-account05-A022-one-point-surgery\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER @ 1

For every uniform Boolean core g with a=1-Eg>=11/16 and independent compatible point-control blocks of common width s>=0 and exclusive widths r,t>=1, F=1+A_s(A_r OR A_t)(g-1) has a finite control-first stopping tree with exactly zero strict threshold-4 bad-node odd-face credit before the core terminal. Every queried node has B_v<4d_v for d_v>0. With u=2^-s,p=2^-r,q=2^-t,beta=p+q-pq, I_ctrl=u a[s beta+r p(1-q)+t q(1-p)], I_leaf=u beta I(g), H_leaf=u beta H(g). Thus H(F)<7I_ctrl+H_leaf, genuine minority/KL debt plus H_leaf<=4I_ctrl+H_leaf, and its full 3mu/ln2 allowance plus H_leaf<9I_ctrl+H_leaf. A more general sufficient local condition for a fresh point event against any independent residual event of probability q is a(1-q)>e/8. If g selects any bent sign on even k>=4 bits or its one-vertex flip, H(g)/I(g)<3 and therefore H(F)<7I(F), J+terminal<=4I(F), full sufficient KL ledger<9I(F), uniformly in all widths and k. Common coordinates and the shared core are paid once.

Review scope receipts: A040 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A023\runs\20261012T010933Z-account05-A023-amortized-rarity-budget\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A040\runs\20261013T212401Z-account05-A040-credit-insufficiency-tests\CLAIMS.json

## A026-AFFINE4-GOOD-COORDINATE @ 1

Every nonconstant uniform-cube Boolean sign function with nonzero Fourier support of affine F2 dimension at most four, and every disjoint product of such factors, has a relevant physical coordinate i with B_i <= (7/2) I_i. This class is closed under physical restrictions and satisfies H <= (7/2+2/ln 2) I.

Review scope receipts: A028 / ACCEPT_AT_STATED_SCOPE; A087 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A026\runs\20261011T214052Z-account05-A026-good-coordinate-erasure\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A028\runs\20261011T221633Z-account05-A028-stopping-tree-payment\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A026-AMPLITUDE-K4-THRESHOLD-NOGO @ 1

For f=+1 exactly at Hamming weights >=24 on 32 uniform sign bits, every coordinate has edge amplitude proxy A_i=2 sum_T |fhat(T) fhat(T+i)| with A_i/I_i=2220940451/536870912>4. Thus existential proxy selection with K=4 is false. No true-erasure violation or unbounded-ratio family is claimed.

Review scope receipts: A028 / ACCEPT_AT_STATED_SCOPE; A087 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A026\runs\20261011T214052Z-account05-A026-good-coordinate-erasure\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A028\runs\20261011T221633Z-account05-A028-stopping-tree-payment\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A027-DATA-FIRST-PROPER-BLOCK @ 1

For every Boolean u on m>=1 uniform core bits, r>=1 fresh control bits, p=2^(-r), d=1-Eu, and F=1+A_r(u-1), the proper core block W satisfies B_W(F)<=p(2dm+2)<=6pm. I_W(F)=pI(u), expected terminal influence=rpd, and all leaves are constants or point defects satisfying H<=4I. For each fixed eta>0, I(u)>=eta*m implies H(F)<=max(6/eta+2/ln(2),4)*I(F) by a single-use physical stopping ledger.

Review scope receipts: A028 / ACCEPT_AT_STATED_SCOPE; A087 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A027\runs\20261011T215911Z-account05-A027-block-selection\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A027\runs\20261011T234627Z-account05-A027-block-selection\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A027\runs\20261013T221314Z-account05-A027-block-selection\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A028\runs\20261011T221633Z-account05-A028-stopping-tree-payment\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A027-CORE-BLOCK-HARDNESS @ 1

For every Boolean core u with Eu>=0, delta=(1-Eu)/2, v=1-(Eu)^2, p=2^(-r), R0=1-4p*delta+4p^2*delta, and L the entropy of the nonempty conditional core spectrum, B_W(1+A_r(u-1))/p=v*L+4*delta*(1-p)*h2(delta)+(R0/p)*h2(p^2*v/R0). Continuous zero-mass conventions apply. A uniform core-block bound B_W<=K*p*I(u) for all such cores and r>=1 implies full FEI with constant K+2. Conversely FEI with constant C implies this block bound with constant C+5.

Review scope receipts: A028 / ACCEPT_AT_STATED_SCOPE; A087 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A027\runs\20261011T215911Z-account05-A027-block-selection\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A027\runs\20261011T234627Z-account05-A027-block-selection\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A027\runs\20261013T221314Z-account05-A027-block-selection\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A028\runs\20261011T221633Z-account05-A028-stopping-tree-payment\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A031-SIGNED-ENTROPY-ANCHOR @ 1

For every finite uniform-cube Boolean sign f, let a_S=fhat(S), p_S=a_S^2, ell_S=log2(1/p_S) on positive atoms and a_S ell_S=0 otherwise, c_U=sum_S a_S a_(S xor U) ell_S, E_log=sum_(U nonempty)|U|c_U^2, and J_R=sum_(U nonempty)p_(R xor U)/|U|. Every occupied R obeys p_R[H(f)-ell_R]^2<=J_R E_log; also sum_(U nonempty)c_U^2=Var_p(ell). For a largest atom, H(f)<=ell_R+sqrt(J_R E_log/p_R).

Review scope receipts: account05/A033 / ACCEPT_AT_STATED_SCOPE; account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A031\runs\20261011T214115Z-account05-A031-convolution-identity\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A031\runs\20261011T232738Z-account05-A031-convolution-identity\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A033\runs\20261011T221704Z-account05-A033-derivative-hierarchy\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A031-ANCHOR-POSITIVE-PAYMENT-NOGO @ 1

There is no finite universal K with E_log(f)<=K I(f), nor any finite universal K with sqrt(J_R E_log(f)/p_R)<=K I(f) for the largest-atom anchor R of every Boolean f. The first is refuted by n-bit one-point defects with E_log/I~4n^2; the second by disjoint tensor powers of the three-bit point defect, whose anchor cost is exponentially large while influence is linear.

Review scope receipts: account05/A033 / ACCEPT_AT_STATED_SCOPE; account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A031\runs\20261011T214115Z-account05-A031-convolution-identity\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A031\runs\20261011T232738Z-account05-A031-convolution-identity\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A033\runs\20261011T221704Z-account05-A033-derivative-hierarchy\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A031-FOURTH-ROOT-ERASURE-CREDITS @ 1

Let A=(g+h)/2,V=(g-h)/2,F=A+iV for an actual Boolean split, u=Ahat,v=Vhat,d=Inf_i, and M_i be the mutual information of the spectral-sector law with masses u_T^2,v_T^2. Full Booleanity gives F^4=1 and I(F^2)/2=W_i=2 sum_(U nonempty)|U|(sum_T v_T v_(T xor U))^2. With R_i=W_i-d log2(1/d)>=0 and sigma(d)=log2(e)d-(1-d)log2(1/(1-d))>=0, B_i=W_i+log2(e)d-R_i-M_i-sigma(d). In particular B_i+M_i<=W_i+log2(e)d; this bound fails for the normalized non-Boolean coefficient vector (4/5,3/5). In any bound B_i<=alpha I(F^2)+C d valid for all Boolean splits with fixed finite C, necessarily alpha>=1/2, as witnessed by even-dimensional bent one-point phase surgery.

Review scope receipts: account05/A035 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A031\runs\20261011T232738Z-account05-A031-convolution-identity\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A031\runs\20261013T215020Z-account05-A031-convolution-identity\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A035\runs\20261013T212341Z-account05-A035-signed-cancellation-countersearch\CLAIMS.json

## B05-ODDFACE-ISO-PAYMENT @ 1

For every Boolean f and coordinate i: B_i(f) <= h2(d) <= (1/2) I(g h) + log2(e) d, and d log2(1/d) <= (1/2) I(g h) <= (1/2)(I(g)+I(h)).

Review scope receipts: account05/A031 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A031\runs\20261011T232738Z-account05-A031-convolution-identity\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B05\runs\20261011T225000Z-claude-B05-odd-face-transport\CLAIMS.json

## B05-ODDFACE-TELESCOPE @ 1

Let N_odd(f) be the number of 2-faces of {0,1}^n on which f has corner product -1 and Q(f)=2^(1-n) N_odd(f). For every i, Q(f) = (1/2) I(g h) + (Q(g)+Q(h))/2; hence in every restriction tree sum_v w_v (1/2) I(g_v h_v) = Q(f) - sum_leaves w Q(leaf) <= Q(f), each odd face charged at exactly one node; and Q(f) = (1/4) sum_i I(f|x_i=0 f|x_i=1).

Review scope receipts: account05/A031 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A031\runs\20261011T232738Z-account05-A031-convolution-identity\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B05\runs\20261011T225000Z-claude-B05-odd-face-transport\CLAIMS.json

## A096-UNIVERSAL-LEVEL12-ERASURE @ 1

For every finite n>=0 and every Boolean sign f on the uniform {-1,1}^n cube, let a_S=hat f(S), epsilon_i=Inf_i(f), I=sum_i epsilon_i, H2=sum_{i<j}a_{ij}^2 log2(1/a_{ij}^2), and T12=sum_i sum_{j!=i}phi(a_i^2,a_{ij}^2), where phi(x,y)=(x+y)h2(y/(x+y)) with zero terms by continuity and entropy in bits. Then H2<=(155600/50301)I and T12<=(16700/2187)I<8I whenever I>0; all quantities vanish for constants. The self-contained Boolean derivative estimate sum_{j!=i}a_{ij}^2<=2 epsilon_i^2 ln(2/epsilon_i) and the subprobability pair reference Q({i,j})=2 epsilon_i epsilon_j/I^2 establish the bound. Normalized real spectral vectors without full Booleanity admit T12/I_spectral growing without bound; no claim on erasure edges starting at levels >=2 is made.

Review scope receipts: A098 / ACCEPT_AT_STATED_SCOPE; account05/A031 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A031\runs\20261013T215020Z-account05-A031-convolution-identity\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A096\runs\20261011T234252Z-account05-A096-live-gap-ledger\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A096\runs\20261013T220343Z-account05-A096-live-gap-ledger\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A098\runs\20261012T024601Z-account05-A098-resource-reallocation\CLAIMS.json

## A032-EXACT-PHASE-ADMISSION @ 1

For every uniform Boolean cube, a spectral probability law supported on at most four labels is realizable iff it is a singleton of mass1 or the uniform law on an affine plane. A uniform affine-subspace law of dimension r is realizable iff r is even, and then H=r<=2D<=2I. For arbitrary supported laws, phase realizability is equivalent to phase realizability on the support affine-span quotient. The labelled four-variable law with Walsh magnitudes (8,8,4,4,4,4,4,4,4,4,0,0,0,0,0,0) and denominator256 passes all15 separate XOR pair partitions but has no realizing phase (all512 phases certified). Complete exact enumeration on n=4 yields2261 distinct Boolean spectral laws among975621 magnitude laws satisfying square norm and necessary even/common-mod4 arithmetic.

Review scope receipts: account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A032\runs\20261011T215947Z-account05-A032-boolean-phase-realizability\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A033-DIRECTIONAL-PHASE-BLOCK-PAYMENT @ 1

For every finite uniform-cube Boolean sign f=(-1)^P, partition X,Y, and integer d>=0, if every nonconstant GF(2) directional phase derivative partial_i P for i in X has degree at most d on all remaining physical variables, then H(S_X|S_Y)<=kappa(d) sum_{i in X} min(Inf_i,1-Inf_i), where kappa(0)=0 and kappa(d)=h2(2^-d)/2^-d for d>=1. More sharply H(S_X|S_Y)<=sum_{i in X,d_i>=1} kappa(d_i)J_i-TC(S_X)-I(S_X;S_Y). Using the separately imported physical block-channel bound, H(f)-E_t H(f_t)<=[kappa(d)+2/ln2] I_X(f). Terminal Y entropy is retained; no universal bounded d is asserted.

Review scope receipts: account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A033\runs\20261011T221704Z-account05-A033-derivative-hierarchy\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A034-QUADRATIC-AFFINE-ROW-CONDITIONAL @ 1

For every integer d>=1, a Boolean sign on disjoint uniform physical X,Y cubes whose distinct X Fourier labels S_j have size <=d and whose partial rows are unit quadratic signs on affine Y partition cells A_j of codimension k_j has H(S_Y|S_X)=sum_j 2^(-k_j)(k_j+r_j)<=2 I_Y, H(S_X)=sum_j 2^(-k_j)k_j, and H(f)=sum_j 2^(-k_j)(2k_j+r_j)<=4 I_Y, where r_j is the quadratic polar rank restricted to the direction space of A_j. Admission is stable under every coordinate Y restriction and X restrictions preserving injective projected labels. Every admitted Boolean tensor factor on fresh Y bits is a quadratic phase. Full physical restriction closure of unbounded ordinary addressing contains every Boolean sign, so a conditional bound on that closure is FEI-strength.

Review scope receipts: A079 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A034\runs\20261011T223816Z-account05-A034-phase-energy-transfer\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A079\runs\20261012T044009Z-account05-A079-correlated-auxiliaries\CLAIMS.json

## A036-POINT-DEFECT-TENSOR-NORMALIZED-PAYMENT-RECOVERY @ 1

For every finite disjoint tensor product of Boolean one-point defects f_m=1-2*1_point, m>=2, including physical translations, global sign, character multiplication, fresh character coordinates and irrelevant coordinates, let P=fhat^2, Q be the product of its actual spectral coordinate marginals, B=sum_i h2(P(i in S)), K=D2(P||Q), b=sign(fhat)*sqrt(Q) on the common support and zero off it, v_U=(sum_S b_S b_{S xor U})^2, Z=sum_U v_U, T=H(v/Z)-log2 Z, I=sum_i P(i in S). Then K>=max(0,B-4I), K>=T/4-8I, and B<=T/4+8I. In particular the latter two separately proved inequalities imply H(P)<=16I, while the direct factor entropy bound gives H(P)<=4I. All entropy and divergence quantities are in bits.

Review scope receipts: account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A036\runs\20261011T214139Z-account05-A036-reference-law-divergence\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A037-CONDITIONAL-CREDIT-CONSERVATION @ 1

For every finite adaptive transcript tree on a common finite joint law P(W,A,L), sum_h P(h) I(W;Y_h|A,h) + sum_l P(l) H(W|A,l) = H(W|A); every cut and subtree obey the same identity. For finite common-law divergences, K_h+j_h=d_h+E_P K_hy, hence sum_h P(h)d_h+sum_l P(l)K_l=K_root+sum_h P(h)j_h. Shared channels give zero injection; replacing a predicted child reference q by r adds E_p log2(q/r) on the resource side. All terminal terms are retained.

Review scope receipts: A039 / ACCEPT_AT_STATED_SCOPE; account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A037\runs\20261011T220010Z-account05-A037-conditional-credit-ledger\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A039\runs\20261011T223903Z-account05-A039-projection-under-restrictions\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A037-PHYSICAL-SPECTRAL-COMMON-LIFT @ 1

For every Boolean function on a finite uniform cube and every finite adaptive physical block restriction tree, the function-specific kernel k_h(y|S_0)=2^(-|B_h|) (f_h|B_h=y)hat(S_0 intersect C_h)^2 / sum_U f_hhat(U union (S_0 intersect C_h))^2, on positive fibers, constructs a common root spectral/physical-transcript law with actual fair physical branches and actual child spectra. It satisfies sum_h P(h) J_h=I(S_0;L) and H(S_0|L)=sum_h P(h) H(S_h intersect B_h|S_h intersect C_h,h)+sum_l P(l)H(f_l). No universal phase-blind channel on parent squared spectra exists, as witnessed by f=[1,1,1,-1], g=[1,1,-1,1].

Review scope receipts: A039 / ACCEPT_AT_STATED_SCOPE; A063 / ACCEPT_AT_STATED_SCOPE; account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A037\runs\20261011T220010Z-account05-A037-conditional-credit-ledger\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A039\runs\20261011T223903Z-account05-A039-projection-under-restrictions\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A063\runs\20261011T222159Z-account05-A063-information-revelation\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A038-OCCUPANCY-CROSSLAW-AUDIT @ 1

For every finite subset law P with v=P(nonempty)>0, r_i=P(i in S|nonempty), d_i=v r_i and nonempty maximum-entropy law Q_r, K_full=D_2(P||prod Bern(d_i))=v K_occ+Delta with Delta=D_2((1-v)delta_empty+v Q_r||prod Bern(d_i))=sum_i h_2(d_i)-h_2(v)-v Hmax(r)>=0. For the actual Boolean point defect f_m, K_occ=0 and Delta>=(m-5)I; for A036's unconditioned signed collision T, T/(4I)>m-7 for every m>=8. Consequently no fixed finite kappa makes either K_occ>=T/4-kappa I or v K_occ>=T/4-kappa I universal.

Review scope receipts: account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A038\runs\20261011T221733Z-account05-A038-occupancy-term-audit\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A039-COHERENT-PROJECTION-TRANSFER @ 1

For every finite uniform-cube Boolean sign and physical coordinate i, TC(f)=I_P(S_i;S_-i)-JS_i+Gamma_i+E TC(f_child), where Gamma_i=sum_{j!=i}[h2(Inf_j(f))-E h2(Inf_j(f_child))]. The identity telescopes over every finite adaptive fair physical tree with terminal TC retained. Applying the function-specific coherent child kernel to both the residual spectrum and its product projection gives zero channel injection and signed Bayes reset E delta=D_out+JS_i-Gamma_i. The occupancy account K_full=v K_occ+Delta has the exact signed transfer in DERIVATION.md (4). Isospectral children have JS_i=Gamma_i=0. Neither monotonic direction holds generally for TC, K_occ or Delta. For m-bit point defects a=2^(1-m), Gamma_i/a=(m-1)+O(m a), JS_i/a<=4+O(m a), and the Delta release divided by a differs from 2m-6+log2(e) by at most (12m+16)a. Consequently no finite universal c bounds Gamma_i by c Inf_i or c(JS_i+Inf_i), or the absolute expected single-step Delta change by c Inf_i.

Review scope receipts: account05/A088 / HOLDS

Source: ~\brain_workers\FEI100_20261011\agents\A039\runs\20261011T223903Z-account05-A039-projection-under-restrictions\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261012T024518Z-account05-A088-booleanity-referee\CLAIMS.json

## A041-COHERENT-PURE-SECTOR-PAYMENT @ 1

For any finite Boolean sign F(A,B) under independent interior product biases, coherent averaging of physical restrictions satisfies E_pureB_ge2(F)<=E_A E_ge2(F(x,B))+3 sum_{U nonempty,|T|>=2}P_F(U,T), in natural corrected entropy with v_S=prod 4q_i(1-q_i). For every finite real-weight threshold, orient signed weights, remove zero/deterministic coordinates, and partition its remaining coordinates into positive equal-weight groups G_j. With r(S) the number of occupied groups, D_j=sum_{S:S intersects G_j}(|S intersects G_j|-1)P(S), R=sum_{S nonempty}(r(S)-1)P(S), and c=460+80 ln 2, the exact ledger is Delta=sum_j D_j+R and the sum E_pure_ge2 over sets wholly in one group with degree>=2 is at most c sum_j D_j+6R<=c Delta, using the all-bias symmetric-threshold baseline. For two groups R=M=sum_mixed P. No absolute mixed entropy payment is asserted. Actual unequal-weight fair thresholds with m weights 2, m weights 1 and threshold 3m are conjunction signs, with E_mixed/M=2(2m-1)ln2, disproving any constant M-only mixed payment. For M>0 the product of the normalized mixed spectral marginals is a complete reference and E_mixed=E_A_m+E_B_m+M ln M-M TC_spec exactly, where TC_spec is spectral, not conditional physical-input TC. Arbitrary weighted FEI+ and full FEI remain open.

Review scope receipts: A045/account05 / ACCEPT_AT_EXACT_STATED_SCOPE_CONDITIONAL_ON_DECLARED_BASELINE

Source: ~\brain_workers\FEI100_20261011\agents\A041\runs\20261013T215146Z-account05-A041-weighted-threshold-fei\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A045\runs\20261014T004049Z-account05-A045-biased-realizability-referee\CLAIMS.json

## A042-SHARP-BINARY-PRIME-ENDPOINT @ 1

For each of the eight essential binary Boolean sign gates with one exceptional truth-table corner, the supremum over all interior independent Bernoulli biases of corrected Hplus/(I-Var) is exactly 2+4/ln(2). For XOR and XNOR the supremum is exactly 2/ln(2). The suprema are not attained in the interior. Writing A(x)=x ln(1/x)/(1-x), corner ratios are 2+2[A(u)+A(v)]/ln(2), where u,v are probabilities of the exceptional corner coordinates; parity ratios are [A(1-4p(1-p))+A(1-4q(1-q))]/ln(2). These formulas extend as limits of interior ratios along arbitrary independent endpoint rates, while deterministic contracted functions have Hplus=I-Var=0. The common sharp corrected constant 2+4/ln(2) propagates through genuine read-once binary formulas under every product physical law by exact disjoint composition; on uniform physical inputs it implies ordinary H<= [2+4/ln(2)] I. No higher-arity prime or universal FEI estimate is established.

Review scope receipts: A041/account05 / HOLDS_AT_STATED_SCOPE; A045/account05 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A041\runs\20261013T215146Z-account05-A041-weighted-threshold-fei\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A042\runs\20261012T002547Z-account05-A042-bias-endpoint-certificates\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A042\runs\20261013T221414Z-account05-A042-bias-endpoint-certificates\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A045\runs\20261013T212421Z-account05-A045-biased-realizability-referee\CLAIMS.json

## A042-BIAS-ENDPOINT-INTERFACE @ 1

For every fixed finite Boolean sign table under independent Bernoulli inputs, the normalized mixed-difference polynomials c_S=2^(-|S|) E Delta_S f give P(S)=w_S c_S^2, natural corrected entropy E=sum_nonempty w_S c_S^2 ln(1/c_S^2), and D=I-Var=sum_|S|>=2 (|S|-1)w_S c_S^2, with path-independent deterministic contraction. For one rare probability e and fixed interior remaining biases, E=E(g)+e K+2e^2 Z ln(1/e)+O(e^2) and D=D(g)+e L-e^2 Q, with K,Z,L,Q as in REPORT.md. If D(g)=0, either L=Q=0 and E=D=0 identically, or L>0 and Hplus/D tends to K/(L ln2). Zero-deficit interior Boolean tables are exactly constants and signed literals; a unit spectral atom after contraction is a signed parity on fair occupied coordinates.

Review scope receipts: A085/account05 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A042\runs\20261011T220136Z-account05-A042-bias-endpoint-certificates\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A042\runs\20261012T002547Z-account05-A042-bias-endpoint-certificates\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A085\runs\20261011T231324Z-account05-A085-certificate-adversary\CLAIMS.json

## A046-AND-ENDPOINT-TAX-NECESSITY @ 1

For the actual Boolean sign g(x,y)=(-1)^(xy) on independent Bernoulli inputs with P(X=1)=p and fixed P(Y=1)=q in (0,1/2), and physical reveal A={X}, the Shannon spectral/physical-channel quantities satisfy J_A-M_A=4q(1-2q)*p*log2(1/p)+O_q(p) as p tends to zero. Consequently every scalar tau(p) such that J_A<=M_A+tau(p) for all finite actual Boolean signs under every interior product bias and every singleton block of bias p satisfies liminf_{p->0} tau(p)/(p*log2(1/p))>=1/2. In particular no universal O(p) tax is valid. This does not refute B09 Delta(p), prove its optimality, or disprove uniform-cube FEI.

Review scope receipts: account05/A092 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A046\runs\20261011T214251Z-account05-A046-current-candidate-intake\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A092\runs\20261011T221121Z-account05-A092-counterexample-referee\CLAIMS.json

## A050-OUTPUT-CONDITIONAL-TAX-REPAIR @ 1

For every finite Boolean sign f under an independent interior product law and every finite deterministic physical singleton stopping tree, let Pi be its full transcript, Y=f(X), w_v the physical node probabilities, c_v=H(X_i|Y,history=v), and tau*(p)=h2(p)-min_t[h2(sin^2 t)+h2(sin^2(t-beta))] with sin^2 beta=min(p,1-p). Then sum_v w_v[tau*(p_i)-c_v/2]_+<=I(Pi;Y)/2<=I_phys(f)/2 and sum_v w_v tau*(p_i)<=I_phys(f)/2+H(Pi|Y)/2. In the ordered family of uniform bounds A_T<=C I_phys(f)+lambda H(Pi|f), with finite fixed C and nonnegative lambda, the smallest coefficient over all product-biased Boolean functions and essential computing trees is lambda=1/2. The exact terminal-inclusive Fourier ledger is Hhat(f)=E Hhat(f_leaf)+2 sum_v w_v M_v+H(Pi|Y)/2+I(Pi;Y)/2-sum_v w_v[h2(p_i)/2-(J_v-M_v)]. Funding the output-conditional bank on a compatible spectral reference and paying the remaining erasure/terminal residual are not established.

Review scope receipts: A046 / ; account05/A092 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A046\runs\20261013T215251Z-account05-A046-current-candidate-intake\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A050\runs\20261013T212442Z-account05-A050-repair-with-scope\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A092\runs\20261013T222550Z-account05-A092-counterexample-referee\CLAIMS.json

## A047-SHARP-FIXED-CHILD-RARE-SELECTOR @ 1

For every fixed finite pair of Boolean children g,h in a fixed product-biased Fourier basis, lim_{p->0}(J_X-M_X)/(p log2(1/p))=2Z+2E(gh)-2<=1/2-2(E(gh)-1/2)^2<=1/2, where Z=sum_{G_T=0}H_T^2. Equality 1/2 is attained by constant/quarter-defect children and by balanced children after fresh-character multiplication. If child Fourier supports are disjoint then M_X=J_X=h2(p) for every p in (0,1).

Review scope receipts: A085/account05 / ACCEPT_AT_STATED_SCOPE; account05/A092 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A047\runs\20261011T220210Z-account05-A047-boundary-search\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A085\runs\20261011T231324Z-account05-A085-certificate-adversary\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A092\runs\20261012T004903Z-account05-A092-counterexample-referee\CLAIMS.json

## A051-PROPER-BLOCK-DESCENT-SQUEEZE @ 1

For every actual nonconstant Boolean sign f on the n-bit uniform cube, n>=2, with H in bits and phi=min over nonempty proper physical blocks A with I_A>0 of (H(f)-E H(f_a))/I_A, phi(f)<=H(f)/(I(f)-min_i Inf_i(f))<=n(H(f)/I(f))/(n-1). If M_n=max H/I over all nonconstant n-bit functions and K_desc(n)=max phi over the same finite domain, then M_n<=K_desc(n)<=n M_n/(n-1). Therefore lim_n K_desc(n)=sup_n M_n=C_* in the extended real sense, and bounded universal proper-block descent is equivalent in finiteness to FEI. No all-dimensional optimizer, independent uniform bound, or paid entropy estimate is asserted.

Review scope receipts: A055/account05 / ACCEPT_AT_STATED_SCOPE; A100/account05 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A051\runs\20261011T233123Z-account05-A051-near-extremizer-definition\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A055\runs\20261013T212502Z-account05-A055-extremal-obstruction-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A100\runs\20261013T213917Z-account05-A100-release-and-continuation-ledger\CLAIMS.json

## A052-CRITICAL-BOOLEAN-PHASE-EXCLUSION @ 1

Let K>=0 and let f be a least-essential-dimension Boolean violation D_K(f)=H(f)-K I(f)>0 of uniform-cube FEI(K). For every nonempty proper physical block A of a coordinates, let w_t be the retained child Fourier row, q_t=E w_t^2, z_t=w_t^2/q_t on positive rows, c_t=E(z_t-1)^2, C_A=sum_t q_t c_t and Gamma_A=sum_t q_t log2(1+c_t). Then C_A>0: identical squared spectra of all physical children are impossible. More quantitatively set h_t=sign(w_t), sign(0)=1, eta_t=min(1,||w_t/sqrt(q_t)-h_t||_2), eta=sum_t q_t eta_t. With psi_a(s)=h2(s)+s log2(2^a-1) up to s=1-2^-a and psi_a(s)=a thereafter, D_K(f)<=Gamma_A+psi_a(eta)+K a eta. Since eta<=sqrt(C_A), if C_A<=1/4 then D_K(f)<=log2(1+C_A)+h2(sqrt(C_A))+sqrt(C_A) log2(2^a-1)+K a sqrt(C_A). This uses FEI(K) on actual Boolean row phases of smaller dimension, not an assumption that phases are physical descendants. Nonstrict physical-descendant ratio criticality alone does not imply C_A>0, as witnessed by a product of two quadratic two-bit signs. No uniform K or FEI resolution follows.

Review scope receipts: account05/A055 / HOLDS

Source: ~\brain_workers\FEI100_20261011\agents\A052\runs\20261013T221539Z-account05-A052-critical-source-structure\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A055\runs\20261014T004129Z-account05-A055-extremal-obstruction-referee\CLAIMS.json

## A053-NEAR-TENSOR-CURVATURE-ADMISSION @ 1

For every Boolean sign f on the n-dimensional uniform cube, its one-point surgery g=f-2*f(a)*1_a has the exact signed spectrum, influence, second-derivative and plaquette identities in HIDDEN_TENSOR_DIAGNOSTIC.md sections 1-2, with uniform entropy error E_n=h2(2^(1-floor(n/2)))+n*2^(1-floor(n/2)) for n>=4. Every one-point surgery of a nontrivial coordinate tensor product in n>=2 is tensor-prime and full-Fourier-support. For every fixed nonconstant d-bit Boolean sign h, surgeries G_t of the balanced powers z*h^(tensor t) have H(G_t)/I(G_t)->H(h)/I(h), connected plaquette graphs and cut-plaquette sum 4td*2^(-td-1)->0; thus the simultaneous qualitative class has the same optimal FEI constant as all Boolean signs. These embeddings do not preserve dimension-criticality for a threshold violated by h, since for t>=2 a proper physical restriction away from surgery exposes +/-h.

Review scope receipts: A055/account05 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A053\runs\20261011T221934Z-account05-A053-near-tensor-perturbations\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A055\runs\20261011T230118Z-account05-A055-extremal-obstruction-referee\CLAIMS.json

## A056-DISJOINT-COMPOSITION @ 1

For every Boolean outer gate h and Boolean children g_i on mutually disjoint uniform physical blocks, after absorbing constant children, with m_i=E g_i, v_i=1-m_i^2>0, a_mu the output-product orthonormal Fourier coefficients and w_i=sum_{T containing i} a_mu(T)^2, E F=E_mu h, Var F=Var_mu h, H(F)=H_mu(h)+sum_i (w_i/v_i)(H(g_i)-h2(v_i)), and Inf_x(F)=(w_i/v_i)Inf_x(g_i) for x in block i. Balanced children specialize to H(F)=H(h)+sum_i Inf_i(h)H(g_i) and I(F)=sum_i Inf_i(h)I(g_i).

Review scope receipts: account05/A091 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A056\runs\20261011T214407Z-account05-A056-balanced-composition\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A091\runs\20261011T214848Z-account05-A091-composition-referee\CLAIMS.json

## A056-PHYSICAL-RESTRICTION-SCOPE @ 1

At every fixed physical restriction, disjoint composition identities hold with newly restricted children, absorbed constants, and the outer gate reexpanded under the new child-output product law. Balance before restriction does not imply balance afterwards. For AND_2 composed with majority_3(x,a,b) and dictator z, fixing x=+1 gives E F=-1/4, I(F)=5/4, H(F)=4-(9/8)log2(3), whereas retaining the initial balanced outer law predicts -1/2, 1, and 3 respectively.

Review scope receipts: account05/A091 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A056\runs\20261011T214407Z-account05-A056-balanced-composition\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A091\runs\20261011T214848Z-account05-A091-composition-referee\CLAIMS.json

## A056-DISJOINT-COMPOSITION @ 2

For every disjoint Boolean substitution F=h(g_1,...,g_k) on independent uniform physical blocks and coordinate i in child j, write h=A+y_j B in the current other-output normalized product basis, m=E g_j, v=1-m^2, beta=g_jhat({i}), t=beta^2, C_T=a_T+m b_T, q=sum b_T^2. With e(s,t)=phi(s)+phi(t)-phi(s+t), d(a,b)=phi(a^2)+phi(b^2)-(phi((a+b)^2)+phi((a-b)^2))/2, phi(s)=s log2(1/s), M(t)=sum e(C_T^2,t b_T^2), N(t)=sum[d(C_T,beta b_T)-e(C_T^2,t b_T^2)], B_i(F)=q[B_i(g_j)-e(m^2,t)]+M(t) and D_i(F)=q[D_i(g_j)-d(m,beta)]+M(t)+N(t). For v>0, 0<=t<=v, M(t)<=min{M(v),(t/v)M(v)+q t log2(v/t)}, M(v)=B_j^mu(h), and 0<=N(t)<=(2/ln2)qt. The log and N terms cost at most [(2+2/e)/ln2] times consumed physical query influence in any represented stopping tree. Constants are absorbed at v=0. The corrected residual M(t)-q e(m^2,t) may be negative; AND2(OR2,OR2) gives 1/4-(9/8)log2(3)+(5/8)log2(5)<0.

Review scope receipts: A057 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A056\runs\20261011T233147Z-account05-A056-balanced-composition\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A057\runs\20261012T003930Z-account05-A057-coherent-restriction-remainder\CLAIMS.json

## A057-CAPPED-RECENTERED-ACTIVATION-TREE-BANK @ 1

For every Boolean sign core u on a finite uniform cube, r>=1 fresh point-control bits, p=2^(-r), a=1-Eu, and F=1+A_r(u-1), any complete adaptive physical core-first tree followed by the complete control suffix has total capped current biased outer-erasure bank <=(4+2/(e ln2))p I(u)+5rp a<=(4+2/(e ln2))I(F), in bits. At a core node m=Eu_v, beta=hat u_v({i}), v=1-m^2, t=beta^2, the cap is min{M(v),(t/v)M(v)+pt log2(v/t)}, M(s)=Phi((1-p+pm)^2,p^2s)+p(1-p)Phi((1-m)^2,s), Phi(s,t)=(s+t)h2(t/(s+t)); zero-variance and zero-t caps are zero. More precisely any partial core-tree prefix costs <=[4p(1-p)+p^2/ln2+2p/(e ln2)]Pi_I(u)+2rp^2[Var(u)-E Var(u_leaf)]. The nonempty inner-decrement cost and terminal entropy are not asserted to be universally paid.

Review scope receipts: A056 / HOLDS_SOURCE_PRICE_RECONSTRUCTION; INDEPENDENT_FULL_CHAIN_ACCEPTANCE_DEFERRED; A091 account05 B19 / ACCEPT_AT_STATED_SCOPE; account05/A058 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A056\runs\20261013T215801Z-account05-A056-balanced-composition\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A057\runs\20261012T003930Z-account05-A057-coherent-restriction-remainder\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A057\runs\20261013T221645Z-account05-A057-coherent-restriction-remainder\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A058\runs\20261012T020138Z-account05-A058-overlapping-compositions\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A091\runs\20261013T220323Z-account05-A091-composition-referee\CLAIMS.json

## A057-COHERENT-ERASURE-SPLIT @ 1

For any disjoint balanced Boolean composition F=g(h_1,...,h_m), g=a+y_j b, q=Inf_j(g), alpha=hat h_j({i}), x=alpha^2: B_i(F)=q B_i(h_j)+L_j(x), D_i(F)=q D_i(h_j)+L_j(x)+J_j(x), where L_j=sum_T(a_T^2+x b_T^2) h_nat(x b_T^2/(a_T^2+x b_T^2)), J_j=E(a^2+x b^2)-(Eraw(a+alpha b)+Eraw(a-alpha b))/2. One has 0<=L_j<=x B_j(g)+qx ln(1/x), 0<=J_j<=2qx, so 0<=R<=x B_j(g)+qx ln(1/x)+2qx. Consequently B(F)<=sum_j q_j B(h_j)+sum_j W_1(h_j)B_j(g)+(2/e)I(F) in nats.

Review scope receipts: A059 / ACCEPT_AT_STATED_SCOPE; A087 / HOLDS

Source: ~\brain_workers\FEI100_20261011\agents\A057\runs\20261011T220314Z-account05-A057-coherent-restriction-remainder\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A057\runs\20261012T003930Z-account05-A057-coherent-restriction-remainder\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261012T004155Z-account05-A087-restriction-referee\CLAIMS.json

## A057-NONREUSING-ALPHA-LOG-PAYMENT @ 1

On any finite adaptive physical-coordinate restriction tree of Boolean root f, at any subset of nodes admitting disjoint balanced composition representations, sum_v w_v q_v alpha_v^2 ln(1/alpha_v^2)<=(2/e)sum_v w_v Inf_{i_v}(f_v)<=(2/e)I(f). Also sum_v w_v R_v<=sum_v w_v alpha_v^2 B_{j_v}(g_v)+(2+2/e)sum_v w_v Inf_{i_v}(f_v). In bits divide each entropy and its constants by ln(2).

Review scope receipts: A059 / ACCEPT_AT_STATED_SCOPE; A087 / HOLDS

Source: ~\brain_workers\FEI100_20261011\agents\A057\runs\20261011T220314Z-account05-A057-coherent-restriction-remainder\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A057\runs\20261012T003930Z-account05-A057-coherent-restriction-remainder\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261012T004155Z-account05-A087-restriction-referee\CLAIMS.json

## A077-ONE-SHARED-BIT-SIGNED-TRANSPORT @ 1

For every uniform Boolean pair G(s,X),H(s,Y) sharing at most one physical data bit s, with disjoint private blocks X,Y and fresh selector z, F=(G+H)/2+z(G-H)/2 satisfies at each data query B_i(F)=(B_i(G)+B_i(H))/2+D_i with |D_i|<=2 Inf_i(F). The factor two is sharp at G=-1,H=s. Every finite adaptive data-only prefix T, z unqueried and arbitrary stopping leaves, has B_T(F)=(B_T(G)+B_T(H))/2+D_T and sum_v w_v |D_v|<=2 Pi, Pi=I(F)-E I(F_leaf). Its exact terminal entropy is E[H(G_leaf)+H(H_leaf)]/2+E R_leaf with R defined by the common-frequency formula in PROOF.md (8). For K=2+2/ln2<5, |R_root-E R_leaf|<=K Pi and 0<=R<=K I_data(F), I_data(F)=(I(G)+I(H))/2. A partial prefix plus optional selector suffix splits one K I_data reserve; inherited core erasure and terminal entropies remain explicit. For private queries, the exact paired-row upper comparison is D_i<=sum_C Phi(h_C^2,d_C^2)/2, and the corresponding negative comparison is retained.

Review scope receipts: account05/A058 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A058\runs\20261013T234047Z-account05-A058-overlapping-compositions\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A077\runs\20261013T222235Z-account05-A077-sparse-defect-towers\CLAIMS.json

## B12-L1-MONOTONE-ERASURE @ 1

Let F=g(h_1,...,h_m) on pairwise disjoint blocks of independent uniform signs, g Boolean on m bits, every h_k Boolean and balanced. Fix a coordinate i in block j; write a_T=ghat(T), b_T=ghat(T+{j}) for T not containing j, q=Inf_j(g)=sum_T b_T^2, alpha=hhat_j({i}), phi(u,v)=(u+v)ln(u+v)-u ln u-v ln v and L_j(x)=sum_T phi(a_T^2, x b_T^2) (nats). Then L_j is nondecreasing and concave on [0,1] with L_j'(x)=sum_T b_T^2 ln(1+a_T^2/(x b_T^2)) and L_j(1)=B_j(g); hence L_j(alpha^2) <= min{B_j(g), alpha^2 B_j(g)+q alpha^2 ln(1/alpha^2)} and, by the A057 erasure split, B_i(F) <= q B_i(h_j) + min{B_j(g), alpha^2 B_j(g)+q alpha^2 ln(1/alpha^2)}.

Review scope receipts: A060 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A060\runs\20261013T212522Z-account05-A060-composition-sharpness\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B12\runs\20261011T225832Z-claude-B12-erasure-ledger-depth\CLAIMS.json

## B12-L2-DEFICIT-LOG-BANK @ 1

For every balanced Boolean h on finitely many independent uniform signs, Lambda(h) := sum_i hhat({i})^2 ln(1/hhat({i})^2) <= (4+6/e)(I(h)-1) nats. Consequently, in a balanced disjoint composition F=g(h_1,...,h_m), sum_j q_j Lambda(h_j) <= (4+6/e)(I(F)-I(g)), q_j=Inf_j(g).

Review scope receipts: A060 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A060\runs\20261013T212522Z-account05-A060-composition-sharpness\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B12\runs\20261011T225832Z-claude-B12-erasure-ledger-depth\CLAIMS.json

## A061-FAIR-TREE-PROCESS @ 1

For every finite-dimensional uniform Boolean sign and fair adaptive physical restriction policy querying each coordinate at most once, with filtration given by past physical observations and an independent policy seed, H(g_t)+sum_{s<t}D_s and I(g_t)+sum_{s<t}d_s are stopped martingales, where D_s=B_s+J_s is the conditional spectral erasure plus the actual physical-child/spectral mutual information and d_s is queried influence. For tau<=n, H(f)=E H(g_tau)+E sum_{s<tau}D_s and I(f)=E I(g_tau)+E sum_{s<tau}d_s.

Review scope receipts: A087 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A061\runs\20261011T214516Z-account05-A061-entropy-process\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A061-LOG-COMPENSATION @ 1

On every such fair finite tree, lambda_t=sum_{T:b_T^2>0}b_T^2 log2((a_T^2+b_T^2)/b_T^2) satisfies D_t<=lambda_t+(3/ln(2))d_t. Therefore (3/ln(2))I(g_t)-H(g_t)-sum_{s<t}lambda_s is a supermartingale. If at every live node every positive b_T^2/(a_T^2+b_T^2)>=epsilon for fixed epsilon in (0,1], then C I(g_t)-H(g_t) is a supermartingale for C=log2(1/epsilon)+3/ln(2); hence H(f)<=C I(f)+E[H(g_tau)-C I(g_tau)].

Review scope receipts: A087 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A061\runs\20261011T214516Z-account05-A061-entropy-process\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A062-INFLUENCE-STOPPING-INTERFACE @ 1

For every finite uniform-cube Boolean f and every fair adaptive fresh-coordinate/block restriction tree, including independently randomized policies and stopping, I(f)=E sum_{t<tau} I_{A_t}(g_t)+E I(g_tau), and the same physical tree obeys H(f)=E sum_{t<tau} delta_{A_t}(g_t)+E H(g_tau). Each original coordinate separately conserves its expected queried cost plus terminal influence. These identities hold for arbitrary waiting/stopping at fixed dimension by bounded convergence. For a genuinely unbounded nonnegative process with the stated drift and integrable initial budget, cumulative costs are integrable, Fatou gives only the terminal inequality, and uniform integrability of residual influence (separately entropy) suffices for equality.

Review scope receipts: A087 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A062\runs\20261011T220423Z-account05-A062-influence-compensator\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A062-BOOLEAN-DIMENSION-LIMIT-OBSTRUCTION @ 1

There is an actual Boolean activation family F_k=1+A_k(g_k-1), with k fair controls, p_k=2^{-k}, and balanced g_k=y_0 times 2^{k-1} quadratic bent two-bit factors, for which I(F_k)=1/2+(k+1)2^{-k}<=3/2. Stopping after control revelation gives terminal influence (2^{k-1}+1)1_{A_k} and terminal entropy 2^k 1_{A_k}; on coupled infinite fair controls they converge to zero almost surely but their expectations tend to 1/2 and equal 1. Thus bounded root influence does not imply dimension-uniform terminal uniform integrability or allow exchanging these terminal expectations with almost-sure limits. Also an activated two-bit parity has root influence 3/2 and a child of influence 2, so residual influence need not decrease pathwise.

Review scope receipts: A087 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A062\runs\20261011T220423Z-account05-A062-influence-compensator\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json

## A087-STOPPED-SELECTOR-SIGNED-ENTROPY-LEDGER @ 1

In the same exclusive-controller setting, put phi(s)=s log2(1/s) and E_ne(u)=H(u)-phi((Eu)^2). On every finite adaptive interleaved data-only prefix, H(F)=E H(F_leaf)+sum_j q_j[E_ne(u_j)-E E_ne(u_j,leaf)]-sum_nodes w q_j phi(beta_node^2)+sum_nodes w(M_node+J_node). At each projected empty-core sector, M0=1-q_j(1-m^2)+q_j beta^2, M_plus/minus=M0+/-2q_j m beta and rho_plus/minus=M_plus/minus/(2M0), and J=M0 JS_rho(P_plus,P_minus)+M0[1-h2(rho_plus)], with zero-mass endpoints by continuity. The rho weights are spectral sector weights; physical query outcomes remain fair. For same-orientation priority with one private bit per event and both cores (1,1,1,-1), the data-first constant-core terminal entropy is 11/8-(9/32)log2(3)>3/4, the control-first terminal entropy. Thus the two stopping-frontier reserves cannot be interchanged.

Review scope receipts: A064 / HOLDS_AT_EXACT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A064\runs\20261013T235917Z-account05-A064-global-debt-potential\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A087\runs\20261013T222530Z-account05-A087-restriction-referee\CLAIMS.json

## A066-HEAT-ENTROPY-IDENTITY @ 1

For every Boolean sign f on every finite uniform cube, with p_S=hat(f)(S)^2, I=sum |S|p_S, H_nat=sum p_S ln(1/p_S), T_t=exp(-tL), L chi_S=|S|chi_S, q_t(S)=p_S exp(-2t|S|), G_f(t)=sum q_t(S)ln(1/p_S) and J_f(t)=sum |S|q_t(S)ln(1/p_S), G_f prime=-2J_f and H_nat=p_empty ln(1/p_empty)+2 integral_0^infinity J_f. The boundary term is between zero and I; J_f(t)<=J_f(0) and J_f(t)<=exp(-2t)J_f(0), giving integrability at both endpoints for every fixed f. For n>=1, J_f(0)<=2(n-1)ln(2)I. A universal integral bound integral J_f<=KI implies FEI in bits with constant (1+2K)/ln(2), and FEI with bit constant C implies that integral bound with K=C ln(2)/2.

Review scope receipts: A067 / ACCEPT_AT_STATED_SCOPE; account05/A070 / ACCEPT_AT_STATED_SCOPE; account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A066\runs\20261011T214539Z-account05-A066-semigroup-dissipation\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A067\runs\20261011T220539Z-account05-A067-hypercontractive-refinement\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A070\runs\20261011T230551Z-account05-A070-analytic-route-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A066-NO-INTEGRABLE-HEAT-ENVELOPE @ 1

There is no nonnegative measurable k with finite integral on (0,infinity) such that J_f(t)<=I(f)k(t) for every finite-dimensional Boolean sign f and almost every t. For f_n(x)=1-2 indicator{x=(1,...,1)}, n>=2, J_f_n(t)/I(f_n)=(2n-2)ln(2)exp(-2t)((1+exp(-2t))/2)^(n-1). Any such pointwise envelope must be at least ln(2)exp(-3/2)/t almost everywhere on (0,1/4]. Nevertheless integral J_f_n/I(f_n)=2(1-1/n)(1-2^(-n))ln(2)<=2ln(2). This refutes the integrable pointwise-envelope helper, not the integrated target or FEI.

Review scope receipts: A067 / ACCEPT_AT_STATED_SCOPE; account05/A070 / ACCEPT_AT_STATED_SCOPE; account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A066\runs\20261011T214539Z-account05-A066-semigroup-dissipation\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A067\runs\20261011T220539Z-account05-A067-hypercontractive-refinement\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A070\runs\20261011T230551Z-account05-A070-analytic-route-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A066-MAJORITY-DEFECTED-ADDRESS-HEAT-CALIBRATION @ 1

For odd majority n=2m+1 and alpha=binom(2m,m)/2^(2m), every singleton physical restriction has M_i=C_i=0 and K(parent)-E K(child)=alpha^2 ln(1/alpha^2)/2, with ratio to Inf_i equal to alpha ln(1/alpha)<=1/e. Thus no finite A bounds that heat drop by A times its C006 channel term, already for Maj3. For F_{a,r}=Addr_a-2 indicator{all inputs +1} with a>=1, k=a+2^a, r>=1, D=k+r and delta=2^(-D), and any b padding coordinates, 1<=b<=r, the exact signed three-class row formulas (9)-(11) of DERIVATION.md compute the heat drop, conditional erasure, channel and level mass. For fixed a,b as r grows, M_B/I_B and C_B/I_B tend to 2ln2 and the heat-drop ratio tends to 2ln2. For b=r, rho=4^a/2^k, the erasure/channel limits are 2(1+rho)ln2 and 2(1-rho)ln2, the heat limit remains 2ln2, and the lost-level limit is 4ln2/2^k. All limits are analytic, not finite-grid extrapolations.

Review scope receipts: account05/A067 / ACCEPT_AT_STATED_SCOPE; account05/A088 / HOLDS

Source: ~\brain_workers\FEI100_20261011\agents\A066\runs\20261011T233317Z-account05-A066-semigroup-dissipation\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A067\runs\20261012T004014Z-account05-A067-hypercontractive-refinement\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261012T024518Z-account05-A088-booleanity-referee\CLAIMS.json

## A066-POSITIVE-RESTRICTION-HEAT-LEDGER @ 2

For every Boolean sign on a finite uniform cube, with natural logarithms, K=(H_nat-p_empty ln(1/p_empty))/2=integral J, every physical block B obeys 2[K(f)-E_y K(f_y)]=M_B^++C_B^++ell_B. q_T=sum_{U subset B}p_{U union T}=E_y p_y(T), M_T=sum_U p_{U union T}ln(q_T/p_{U union T}), C_T=E_y p_y(T)ln(p_y(T)/q_T), plus omits T=empty, and ell_B=sum_{nonempty U subset B}p_U ln(1/p_U); all terms nonnegative. This identity telescopes for every finite adaptive block-query tree with terminal K retained. ONLY for singleton-query trees, the cumulative paid channel-plus-level charge is <=beta[I(root)-E I(leaf)], beta=2+2/e^2, because C_i^+<=2(Inf_i-p_{i}) and |hat f({i})|<=Inf_i. No such price is asserted for arbitrary block-query trees. Also 0<=B_nat-R_nat<=(1+2/e)I; R_nat=sum_i M_i^+, B_nat=sum_i H_nat(S_i|S_without_i). For F_m=y product_j g(x^(j)) on disjoint copies, R_nat(F_m)=m B_nat(g), I(F_m)=m I(g)+1. Hence the optimal universal constants for R_nat/I and B_nat/I coincide. A universal R_nat<=A I implies FEI bits constant (A+2)/ln2 via C018; A remains unproved.

Review scope receipts: A100/account05 / ACCEPT_AT_STATED_SCOPE; account05/A067 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A066\runs\20261013T215841Z-account05-A066-semigroup-dissipation\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A067\runs\20261013T222025Z-account05-A067-hypercontractive-refinement\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A100\runs\20261014T010218Z-account05-A100-release-and-continuation-ledger\CLAIMS.json

## A066-BLOCK-REFINEMENT-HEAT-TRANSFER @ 1

For every Boolean sign and physical block B, any singleton refinement querying exactly B with the same actual children satisfies C_B^++ell_B=P_ref+D_ref, D_ref=R_ref-M_B^+, where R_ref=sum_internal w M_i^+ and P_ref=sum_internal w(C_i^++ell_i)<= (2+2/e^2)I_B. D_ref is signed and must be retained in any block-tree payment. For f_n=1-2 indicator of one vertex, I=n2^(1-n), q=2^-n, whole-cube block M_B^+=C_B^+=0, ell_B/I=4(1-1/n)(1-q)ln2. A complete singleton refinement has R_ref/I=C_ref^+/I=[2-(4/n)(1-q)]ln2, L_ref/I=(4/n)[1-(n+1)q]ln2, P_ref/I=2(1-2q)ln2. Thus the block price tends to 4ln2, refined paid price to 2ln2, and retained transfer to 2ln2. At n=128, ell_B/I>11/4>2+2/e; appending an irrelevant coordinate produces the same obstruction with B a proper ambient subset. No universal price of the retained transfer is asserted.

Review scope receipts: account05/A067 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A066\runs\20261013T215841Z-account05-A066-semigroup-dissipation\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A067\runs\20261013T222025Z-account05-A067-hypercontractive-refinement\CLAIMS.json

## A067-LOCAL-BOOLEAN-GRANULARITY @ 1

For every Boolean sign f on a finite uniform cube, write q_S=hat f(S)^2, v=1-q_empty and I=sum_S |S|q_S. For each nonzero nonempty coefficient define d_f(S)=max{|T|:T contains S and q_T>0}, and U=sum_nonempty q_S(d_f(S)-|S|). Then hat f(S) is a multiple of 2^(1-d_f(S)) and H(f)<=2I+2U-(2-log2(e))v. Thus U<=KI implies H<=(2+2K)I, and d_f(S)<=L|S| implies H<=2LI-(2-log2(e))v. Balanced support antichains give H<=2I-2. On ordinary addressing with a address variables, d_f(S)=a+1, U=a/2, and the bound gives exactly H<=2a, while generic full-cube level counting costs Theta(a^2). These are structural-regime results, not a universal payment of U or a novelty claim.

Review scope receipts: account05/A070 / ACCEPT_AT_STATED_SCOPE; account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A067\runs\20261011T220539Z-account05-A067-hypercontractive-refinement\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A070\runs\20261011T230551Z-account05-A070-analytic-route-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A067-MAXIMAL-SUPPORT-ENVELOPE-NOGO @ 1

No universal finite K can bound the preceding U(f) by K I(f). For p=2^(-n), n>=2, the actual Boolean dictator surgery g_n=x_1-2 indicator{x=all +} has I=1+(2n-4)p and U=n-1-(2n-4)p-4np^2, so U/I diverges. Further define the valid entropy envelope E_A=(log2(e))(1-hat f(A)^2)+2 sum_nonempty_R hat(f chi_A)(R)^2(d_(f chi_A)(R)-1) for every character anchor A. On F_n=Maj_3(z)*(1-2 indicator{y=all +}), with disjoint three-variable z and n-variable y, every E_A>=3n/2, although I(F_n)=3/2+2n2^(-n)<=5/2 and H(F_n)=2+o(1). Hence min_A E_A<=K I is false universally, including anchors outside the Fourier support. These are helper refutations, not FEI counterexamples.

Review scope receipts: account05/A070 / ACCEPT_AT_STATED_SCOPE; account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A067\runs\20261011T220539Z-account05-A067-hypercontractive-refinement\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A070\runs\20261011T230551Z-account05-A070-analytic-route-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A070-HYBRID-SCOPE-AND-THREE-REFERENCE-NOGO @ 1

For any finite probability law p, atom costs a_s>=log2(1/p_s) and nonnegative Kraft lengths l_s, let m be the mass where l_s<a_s. Then H(p)<=sum_s p_s min(a_s,l_s)+m log2(1/m)<=sum_s p_s min(a_s,l_s)+h2(m). For every integer a>=8, pad the Boolean addressing function with a address and 2^a private data coordinates to N=a+2^a+2 bits and flip its all-plus input, obtaining F_a. Put c_arith(S)=2(N-1) on nonempty S and infinity on empty S, c_inf(S)=log2(e)+sum_i_in_S log2(I(F_a)/Inf_i(F_a)), and c_level(S)=-log2(r_|S|)+log2 binom(N,|S|) for any probability prior r on levels. Then E_{p_Fa} min(c_arith,c_inf,c_level)/I(F_a)>=log2(a/2)/40, while H(F_a)/I(F_a)->4. The same lower bound holds for min(c_arith,c_mix), where c_mix is the length of any fixed subprobability prior mixture of the influence and level code laws. Thus no universal O(I) expected-cost bound exists for these three references; no queue-code or FEI claim is refuted.

Review scope receipts: account05/A067 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A067\runs\20261012T004014Z-account05-A067-hypercontractive-refinement\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A070\runs\20261011T230551Z-account05-A070-analytic-route-referee\CLAIMS.json

## A067-PADDING-STRIP-RESERVE-AND-LEAF-ACCESS @ 1

For every Boolean seed g on m>=1 uniform core coordinates, every physical vertex x0, and r>=1 dummy padding coordinates, let F_r differ from g only at (x0,all +), let d=2^(1-m-r), and let I_core=sum of the core-coordinate influences of F_r. For every physical tree that queries only padding coordinates along the unique edited branch and stops every clean branch, the total expected entropy drop Q_pad satisfies Q_pad<=4 I_queried+(1+6/ln(2)) I_core. The core reserve is allocated once across the whole tree. If every leaf satisfies U<=b I, b>=0, where U=sum_nonempty hat f(S)^2(max{|T|:hat f(T)!=0,T contains S}-|S|), then H(F_r)<=(3+2b+6/ln(2)) I(F_r); a sufficient admission is U(g)<=b I(g) and U(F_0)<=b I(F_0). For fixed finite g and r>=2, with L the number of its nonzero Fourier coefficients and p=2^(-m-r), the padding-node drop Delta_r obeys |Delta_r/(2p)-4|<=4 L p (|m+r-3|+m+3/(2ln(2))), hence the ratio tends to 4. The point-defect padding nodes satisfy 0<=Delta<=5 Inf at every dimension. Consequently dictator one-point surgery and Maj3 tensor point defects have explicit U<=I stopping trees paid at node rate 5, with full terminal entropy retained. There is no uniform padding-node rate for arbitrary varying seeds: quadratic bent seeds of even dimension m at fixed r>=2 have Delta_r/(2p)=4+2^(1-r)(m+2r-6+3/ln(2))+O(2^(-r)*2^(1-m/2-r)). These are a padding-access theorem and its scope guards, not universal admission of arbitrary Boolean core leaves.

Review scope receipts: account05/A088 / HOLDS

Source: ~\brain_workers\FEI100_20261011\agents\A067\runs\20261012T004014Z-account05-A067-hypercontractive-refinement\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261012T024518Z-account05-A088-booleanity-referee\CLAIMS.json

## A070-TWO-EDIT-PROJECTION-CROSS-LEDGER @ 1

For any fixed singleton-leaf partition tree with internal cells C_v and child arities b_v, put L(S)=1+sum_v b_v*1{S meets C_v} and <u,v>_L=sum_S uhat(S)vhat(S)L(S). For arbitrary real u,v, <u,v>_L=(1+sum_v b_v)E[uv]-sum_v b_v E[(E[u|C_v^c])(E[v|C_v^c])]. For distinct one-point Boolean edits e_x=-2g(x)1{X=x}, e_y=-2g(y)1{X=y}, the cross is -4g(x)g(y)2^(-2N)sum_v b_v*2^(N-|C_v|)*1{x,y agree outside C_v}. It can be positive despite disjoint physical edit supports: the two-bit x1 seed with edits (+,+),(-,+) gives cross=1/2, individual energies 5/2 and combined energy 6. Moreover for any Boolean core h on a nonempty Y, let g=x1*h(Y), Z={x1,x2}, and join the binary Z tree and any binary Y tree under a binary root. Disjoint proper subcube edits D1={x1=+,x2=+},D2={x1=-,x2=+} have cross=(1+(Eh)^2)/2>=1/2. Their final sign is f=-x1*x2*h, with Gamma(f)=Gamma(g)=5+E_(S_h)W_Y, H(f)=H(g)=H(h), and I(f)=I(g)+1. Thus no finite physical-intersection-density-only bound controls the signed or absolute edit cross; the exact source/edit rebate and retained-core cost cannot be discarded.

Review scope receipts: account05/A067 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A067\runs\20261013T222025Z-account05-A067-hypercontractive-refinement\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A070\runs\20261013T212602Z-account05-A070-analytic-route-referee\CLAIMS.json

## A067-BOUNDED-FIBER-TWO-EVENT-ACCESS-RESERVE @ 1

For every Boolean seed g on m>=0 uniform core coordinates X, r control coordinates Z, and final physical edit mask E, put F(x,z)=g(x)(-1)^1_E(x,z). Assume every core fiber E_x has at most k assignments, k>=1 and k2^-r<=1/4. Let I_Z and I_X be the final F control/core influence sums, and Q=H(F)-E_z H(F_z), with entropy in bits. Then Q <= K I_Z+2 I_X, K=4r/(r-log2 k)+2/ln2. The core reserve is allocated once to the combined mask; I_X(F)>=I_X(1-2*1_E)>=2 P(E)log2(1/P_X(E_x nonempty)). Empty edit sets have Q=I_Z=0. In particular k=1,r>=2 gives K=4+2/ln2 and k=2,r>=3 gives K<=6+2/ln2. Two graph-controlled events with arbitrary shared core/domains/control maps have <=2 assignments per fiber after either XOR or union-once editing. Every complete physical control-reveal tree has this access price and retains all actual core leaves. If every complete leaf satisfies U<=bI, b>=0, the reviewed local granularity certificate gives H(F)<=max(K,4+2b)I(F). For earlier control-only stopping trees with U-certified leaves, the valid bound is H(F)<=(K+2+2b)I(F), retaining remaining control influence. No arbitrary core-leaf admission is asserted. Dropping the sparse-fiber cap invalidates the ownership inequality: g=(-1)^x and E={(0,0),(1,1)} on one core and one control bit give I_X(F)=0<I_X(1-2*1_E)=1.

Review scope receipts: account05/A088 / HOLDS_AT_STATED_BOOLEAN_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A067\runs\20261013T222025Z-account05-A067-hypercontractive-refinement\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261013T234248Z-account05-A088-booleanity-referee\CLAIMS.json

## A068-QUADRATIC-CONTEXT-RANK-REFERENCE @ 1

For every regular Boolean h on q distinct private data bits and every finite list of arbitrary degree-at-most-two F2 control polynomials Q_i on m independent uniform bits, F(x,z)=h(x_i*(-1)^Q_i(z)) satisfies H(F)<=C_reg*I_x(F)+2*I_z(F)<=C_reg*I(F), C_reg=log2(4+e)+2log2(e*pi)<8.937; moreover H(F)<=C_reg*D_x(F)+2*I_z(F). Its data-indexed spectral packets have exact probabilities hhat(S)^2*2^(-rank B_S) on the affine Fourier support of the quadratic phase sum_i_in_S Q_i, and a normalized rank reference pays all packet ranks. For every odd q>=5, the nonlinear cyclic controlled-majority family has I_x=q*c_q, I_z=3*q*c_q/4 and H/I<=(4*C_reg+6)/7, while it is non-unate and selector influence per control tends to zero.

Review scope receipts: account05/A088 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A068\runs\20261011T222313Z-account05-A068-antichain-beyond-one-order\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A088\runs\20261011T223053Z-account05-A088-booleanity-referee\CLAIMS.json

## A068-CYCLIC-ONEPOINT-FULLREF @ 1

For every odd q>=5, let F_q(x,z)=MAJ_q(x_i*(-1)^(u_i*u_(i+1))) on q distinct private data bits and q cyclic uniform control bits. Pad to any N>=2q and flip any one input to obtain G. Let R0 be the normalized data-level rank/affine-quadratic-fiber reference of the accepted A068 base theorem, extended by zero on padding frequencies, delta=2^-N, and R_delta=(1-delta)R0+delta U_N. Then R_delta is normalized with full support, H(G)<=Gamma_delta(G)<=C_reg I_x(G)+2I_z(G)-(287/1920)I_x(F_q), where C_reg=log2(4+e)+2log2(e*pi), I_x(F_q)=q binom(q-1,(q-1)/2)/2^(q-1), and I_z includes padding. For fixed q under padding and a one-point edit, Gamma_delta(G) tends to Gamma0(F_q).

Review scope receipts: account05/A070 / ACCEPT_REPORTED_THEOREM_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A068\runs\20261013T234128Z-account05-A068-antichain-beyond-one-order\CLAIMS.json

## A069-STABLE-HIERARCHY-EDIT-PAYMENT @ 1

For each rooted singleton-leaf partition tree T of [N] with 2 or 3 children per internal vertex, L_T(S)=1+sum_v b_v*1{S intersects C_v} is the length of an all-subset prefix code, max L_T<=3N-2, and H(f)<=Gamma_T(f)=sum_S fhat(S)^2 L_T(S). If Boolean f,g differ on input fraction rho, sqrt(Gamma_T(f))<=sqrt(Gamma_T(g))+2 sqrt(rho max L_T), and |I(f)-I(g)|<=2N rho. For complete depth-d ternary recursive majority g_d, d>=1, padded to N>=3^d bits, the explicit main/padding tree satisfies Gamma_T(g_d)<=6I(g_d)-3. Every truth-table edit f of this g_d satisfies Gamma_T(f)<=12I(f)-6+48N rho-16rho; in particular H(f)<=Gamma_T(f)<=12I(f) if N rho<=1/8. Every one-point edit satisfies H(f)<=Gamma_T(f)<=25I(f), and <=12I(f) for N>=6. For fixed d the code-cost difference under padding and one-point editing tends to zero.

Review scope receipts: account05/A070 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A069\runs\20261011T224507Z-account05-A069-geometric-transfer\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A070\runs\20261011T230551Z-account05-A070-analytic-route-referee\CLAIMS.json

## A069-ALIGNED-EDIT-ENERGY-ADDRESSING @ 1

For a-bit addressing A_a, a>=1, padded to N>=a+2^a, the fixed binary selector/data/padding hierarchy all-subset prefix code has Gamma_T(A_a)=3+2a+2R(a)+2*1{N>a+2^a}, where R(1)=0 and R(k)=1-2^{-k}+R(floor(k/2))+R(ceil(k/2)), and Gamma_T(A_a)<=8I(A_a)-5. Every Boolean truth-table edit f of density rho obeys H(f)<=Gamma_T(f)<=16I(f)-10+48N*rho-8rho. Thus N*rho<=1/8 gives <=16I(f), and every one-point edit gives <=25I(f), with <=16I(f) for N>=6. For any Boolean g on a split cube Z union Y with r=|Z|>=1 and |Y|>=1, join fixed binary singleton-leaf trees on Z,Y, put W_Z,W_Y for their internal-mask costs, and flip g on z=z*. Writing rho=2^{-r}, h=g(z*,.), m_h=Eh and U_Z=sum_v 2(1-2^{-|C_v|}), the exact difference-spectrum cost is E_delta=4rho[1+2(1-rho*m_h^2)+U_Z+E_{S_h}W_Y]. Partial restriction Parseval gives rho*E_{S_h}W_Y<=E_{S_g}W_Y, hence E_delta<=4E_{S_g}W_Y+4rho(2r+1) and Gamma_T(f)<=2Gamma_T(g)+8E_{S_g}W_Y+8rho(2r+1). Free-coordinate influences are unchanged, and I_Z(f)+I_Z(g)>=2r*rho.

Review scope receipts: account05/A070 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A069\runs\20261012T043929Z-account05-A069-geometric-transfer\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A070\runs\20261013T212602Z-account05-A070-analytic-route-referee\CLAIMS.json

## A070-REVIEW-A068-REPORTED-CYCLIC-EDIT-REFERENCE @ 1

For every odd q>=5, let F_q(x,z)=MAJ_q(x_i*(-1)^(u_i*u_(i+1))) on q distinct private data bits and q cyclic uniform control bits. Pad to any N>=2q and flip any one input to obtain G. Let R0 be the normalized data-level rank/affine-quadratic-fiber reference of the accepted A068 base theorem, extended by zero on padding frequencies, delta=2^-N, and R_delta=(1-delta)R0+delta U_N. Then R_delta is normalized with full support, H(G)<=Gamma_delta(G)<=C_reg I_x(G)+2I_z(G)-(287/1920)I_x(F_q), where C_reg=log2(4+e)+2log2(e*pi), I_x(F_q)=q binom(q-1,(q-1)/2)/2^(q-1), and I_z includes padding. For fixed q under padding and a one-point edit, Gamma_delta(G) tends to Gamma0(F_q). This accepts the exact theorem stated in A068 stage2 REPORT.md, with its named accepted base-rank dependency; it does not establish absent author package/full-validation receipts.

Review scope receipts: account05/A070 / ACCEPT_REPORTED_THEOREM_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A070\runs\20261013T212602Z-account05-A070-analytic-route-referee\CLAIMS.json

## A071-B09-THREEBIT-GRID-CERTIFICATE @ 1

For every Boolean sign f on {0,1}^3, every product-bias vector p in {1/8,1/4,1/2,3/4,7/8}^3, and every nonempty proper physical block A, J_A <= M_A + Delta_A(p), with M_A=H(S_A|S_B), J_A=H(S_B)-E_Z H(mu_Z), Delta_A=sum_i_in_A[h2(p_i)+log2(max(p_i,1-p_i))], and mu_Z the inherited biased squared Fourier law of the actual restriction. Entropy is in bits.

Review scope receipts: A085/account05 / ACCEPT_AT_STATED_SCOPE; account05/A073 / SELECTED_RECORDS_CONFIRMED_ONLY_FULL_GRID_REVIEW_PENDING; account05/A074 / SELECTED_RECORDS_CONFIRMED_ONLY_FULL_GRID_REVIEW_PENDING

Source: ~\brain_workers\FEI100_20261011\agents\A071\runs\20261011T214639Z-account05-A071-search-space-design\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A073\runs\20261011T222436Z-account05-A073-certified-logarithms\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A074\runs\20261011T224717Z-account05-A074-independent-reproducer\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A085\runs\20261011T231324Z-account05-A085-certificate-adversary\CLAIMS.json

## A071-EXACT-FIVEBIT-ERASURE-SELECTION @ 1

On the uniform five-bit cube, E*(5)=max_{f nonconstant} min_{i:Inf_i(f)>0} H(S_i|S_-i)/Inf_i(f) equals K5=16/3-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89). Equality holds exactly for the 640 truth tables whose minority class is {t,t xor e_i,t xor e_j}, with t in F2^5 and distinct coordinates i,j, allowing output complement. The associated spectral law is P(S)=fhat(S)^2 and entropy is in bits.

Review scope receipts: A082 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A071\runs\20261011T233808Z-account05-A071-search-space-design\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A082\runs\20261012T004123Z-account05-A082-finite-inequalities\CLAIMS.json

## B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED @ 1

For g(X,Y)=(-1)^(XY), independent P(X=1)=1/8 and P(Y=1)=1/4, with physical block A={X}, J_A-M_A>1195/10000 bits. Thus universal tax-free J_A<=M_A under arbitrary product biases is false.

Review scope receipts: account05/A073 / FIXED_COUNTEREXAMPLE_RECONFIRMED_BY_ALTERNATE_PRODUCT_REPRESENTATION; account05/A074 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A073\runs\20261011T222436Z-account05-A073-certified-logarithms\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A074\runs\20261011T224717Z-account05-A074-independent-reproducer\CLAIMS.json; ~\mop_fei100\reports\fei-2026-10-11\CLAIM_REGISTRY.json

## B15-LKSTAR-FAILS-N5-N6 @ 1

L(K*) is false: with K* = 4 + (5/2)log2 5 - (9/2)log2 3, the Boolean functions f_5 = -1 exactly on {e_1, e_1+e_2, e_1+e_2+e_4} in {0,1}^5 and f_6 = -1 exactly on {0, e_0,...,e_5, e_1+e_2, e_0+e_4, e_3+e_5} in {0,1}^6 (uniform measure, +1 elsewhere) have every coordinate relevant and B_i = H(S_i|S_-i) > (539/200) Inf_i for every i of f_5 and B_i > (368/125) Inf_i for every i of f_6 (bits). Hence E*(5) > 539/200 > K* and E*(6) > 368/125.

Review scope receipts: A073 / ACCEPT_AT_STATED_FINITE_SCOPE; account05/A074 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A073\runs\20261013T234148Z-account05-A073-certified-logarithms\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A074\runs\20261012T043949Z-account05-A074-independent-reproducer\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B15\runs\20261011T225100Z-claude-B15-erasure-countersearch\CLAIMS.json

## A096-TERMINAL-KL-REFUND-AUDIT @ 1

For every finite Boolean seed f, every m,k>=1 and ell>=2 on disjoint uniform blocks, let h=chi_Z product_b f_b, J=mI(f)+ell, F=1+A_k(h-1), q=2^-k, d=(1-q)^2+q^2. For each relevant coordinate use mu_i(T)=p_(T+i)/Inf_i and r_i(T)=p_T+p_(T+i); both normalize to one. Let M=sum_i Inf_i[log2(1/Inf_i)-D(mu_i||r_i)] and D_f be the KL divergence of the normalized joint derivative/reference laws, with I(f)D_f=0 for constants. Original core-coordinate divergences obey D_i(F)=D_i(h)+k, D_i(h)=D_i(f) on seed blocks and D_i(h)=0 on parity bits. Every control divergence is D_c=(1-q)(k-1)+q log2(q/d). Consequently I(F)=q(J+k), I(F)D_F=q[mI(f)D_f+kJ+kD_c], M(F)=qmM(f)+k[q(1-q)+q^2 log2(d/q^2)], and M_ge2(F)=qmM(f)+kq(1-kq). For every fixed ell>=2 and finite nonnegative s(N)=o(N), the supremum of M_geell/I over 0<I<=2^-s(N) equals the unrestricted supremum K_M in the extended reals. No finiteness of K_M, universal refund payment or full FEI conclusion is asserted.

Review scope receipts: A073 / ACCEPT_AT_STATED_SCOPE; A099 / ACCEPT_AT_STATED_SCOPE; A100/account05 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A073\runs\20261013T234148Z-account05-A073-certified-logarithms\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A096\runs\20261013T220343Z-account05-A096-live-gap-ledger\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A099\runs\20261014T001305Z-account05-A099-candidate-assembly\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A100\runs\20261014T010218Z-account05-A100-release-and-continuation-ledger\CLAIMS.json

## A082-FINITE-TRUE-ERASURE @ 1

For every nonconstant Boolean sign f on at most four uniform physical variables there exists a relevant i with H(S_i|S_-i)<=Kstar Inf_i(f), where Kstar=4+(5/2)log2(5)-(9/2)log2(3)<107/40. Kstar is optimal over this domain.

Review scope receipts: account05/A074 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A074\runs\20261012T043949Z-account05-A074-independent-reproducer\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A082\runs\20261011T221008Z-account05-A082-finite-inequalities\CLAIMS.json

## B17-JS-PACKET-SCALAR @ 1

For every z in [-1,1], ((1+z)ln(1+z)+(1-z)ln(1-z))/2 <= 1-sqrt(1-z^2). Consequently, for every Boolean f and coordinate i, 0 <= JS_i <= (2/ln2) sum over T not containing i of min(fhat(T)^2, fhat(T+i)^2) <= (2/ln2) min(I_i, 1-I_i).

Review scope receipts: A081 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A081\runs\20261011T234021Z-account05-A081-dependency-certificates\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B17\runs\20261011T224300Z-claude-B17-erasure-census-affine-bridge\CLAIMS.json

## B17-KB-TWO-SIDED @ 1

Let K_B(n) = max over nonconstant Boolean f with at most n relevant coordinates of min over relevant i of B_i/I_i, and C(n) = max H/I over the same set. Then K_B(n) <= C(n) <= K_B(n) + 2/ln2 for every n >= 1. With K_B = sup_n K_B(n) and C_FEI = sup_n C(n): C_FEI - 2/ln2 <= K_B <= C_FEI, so FEI holds iff K_B is finite.

Review scope receipts: A081 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A081\runs\20261011T234021Z-account05-A081-dependency-certificates\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B17\runs\20261011T224300Z-claude-B17-erasure-census-affine-bridge\CLAIMS.json

## B17-ZERO-ERASURE-TRANSPORT @ 1

For Boolean f and coordinate i, B_i(f)=0 iff fhat(T)fhat(T+i)=0 for every T not containing i. Then both restrictions f|x_i=b have squared spectrum equal to the image of fhat^2 under S -> S minus {i}, so H(f|x_i=b)=H(f), JS_i=0 and I(f|x_i=b)=I(f)-I_i(f). For n >= 2, every maximizer of H/I over nonconstant Boolean functions with at most n relevant coordinates has B_i > 0 at every relevant coordinate.

Review scope receipts: A081 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A081\runs\20261011T234021Z-account05-A081-dependency-certificates\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B17\runs\20261011T224300Z-claude-B17-erasure-census-affine-bridge\CLAIMS.json

## B17-KB5-CUTOFF @ 1

Let g:{0,1}^5->{-1,1}, g(x)=-1 iff sum_j x_j 2^j is in {5,12,13} (equivalently x1=0, x2=1, x4=0 and (x0 or x3)). All five coordinates are relevant; for i in {1,2,4}: I_i=3/16 and B_i/I_i = 16/3-(3/8)log2 3-(169/24)log2 13+(89/24)log2 89 (=2.6958875...); for i in {0,3}: I_i=1/16 and B_i/I_i = 16-(63/8)log2 3+15 log2 5-(169/8)log2 13+(85/8)log2 17 (=3.6048453...). Hence min_i B_i/I_i(g) > 107/40 > 4+(5/2)log2 5-(9/2)log2 3, and K_B(5) > K_B(4).

Review scope receipts: A081 / ACCEPT_AT_STATED_SCOPE; A085/account05 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A081\runs\20261011T234021Z-account05-A081-dependency-certificates\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A085\runs\20261013T213517Z-account05-A085-certificate-adversary\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B17\runs\20261011T224300Z-claude-B17-erasure-census-affine-bridge\CLAIMS.json

## A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER @ 1

For every finite uniform Boolean sign and finite adaptive physical block restriction tree with no coordinate rerevealed on a path, and complete leaf subprobability references Q_l positive on the actual leaf Fourier support, the compatible lift r_h(T)=2^(-|A_h|)sum_y Q_hy(T), Q_h(U union T)=theta_h(U|T)r_h(T) yields a complete root reference satisfying CE(P_0,Q_0)=sum_h pi_h(B_h+J_h-kappa_h)+sum_l pi_l CE(P_l,Q_l). Here theta is the actual parent spectral conditional kernel and kappa_h=sum_T q_h(T)D_2(k_P(.|T)||k_Q(.|T))>=0. The total correction equals E_{S~P_0}D_2(P(L|S)||Q(L|S))=sum_l pi_l D_2(P_l||Q_l)-D_2(P_0||Q_0), and is at most terminal reference KL slack. Since J_h<=(2/ln2)I_A_h(f_h), if sum pi_h(B_h-kappa_h)<=K I_removed and CE(P_l,Q_l)<=C_leaf I(f_l), then CE(P_0,Q_0)<=max(K+2/ln2,C_leaf)I(f). No universal existence/payment of these hypotheses is asserted.

Review scope receipts: A081 / INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A081; A094/account05/B19 / HOLDS_AT_EXPLICIT_ONE_NODE_CLAUSE_ONLY; A098 / ACCEPT_KL_CONSERVATION_SUBCLAIM_ONLY

Source: ~\brain_workers\FEI100_20261011\agents\A081\runs\20261013T220111Z-account05-A081-dependency-certificates\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A094\runs\20261014T001244Z-account05-A094-proof-chain-challenger\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A097\runs\20261011T221240Z-account05-A097-cross-route-transfer\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A098\runs\20261011T223200Z-account05-A098-resource-reallocation\CLAIMS.json

## A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS @ 1

For every fixed integer ell>=2 and every finite-valued s:N->[0,infinity) with s(N)=o(N), define R_geell(F)=sum_i sum_(T subset [N] minus {i}, |T|>=ell) phi(Fhat(T)^2,Fhat(T union {i})^2), where phi(x,y)=(x+y)h2(y/(x+y)) in bits with continuous zero conventions. The supremum K_geell(s) of R_geell(F)/I(F) over all finite N-bit Boolean signs with 0<I(F)<=2^-s(N) equals K_E=sup_(all finite nonconstant Boolean f) B(f)/I(f), in the extended reals. For every actual seed f and integers m,k>=1, let h=chi_Z*f^tensor(m) on ell fresh parity bits, F=1+A_k(h-1), q=2^-k, with all blocks disjoint. Then B_data(F)=qmB(f), I(F)=q(mI(f)+ell+k), R_geell(F)=qmB(f)+kq+2kq^2 sum_(r=ell..k-1) binom(k-1,r), and R_ge2(F)=qmB(f)+2kq(1-kq). Each parity coordinate z has B_z(F)=0 and Inf_z(F)=q>0, so min_(i relevant) B_i(F)/Inf_i(F)=0. No finiteness of K_E or selected-witness transport is asserted.

Review scope receipts: A081 / INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A081; A085 / PENDING_ALTERNATE; A094 / PENDING; A096 / ACCEPT_AT_STATED_SCOPE; A099 / ACCEPT_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A081\runs\20261013T220111Z-account05-A081-dependency-certificates\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A090\runs\20261013T213537Z-account05-A090-independent-reconstruction\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A096\runs\20261013T220343Z-account05-A096-live-gap-ledger\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A099\runs\20261014T001305Z-account05-A099-candidate-assembly\CLAIMS.json

## B20-ERASURE-LOW-INFLUENCE-COMPLETE @ 2

For every finite-valued s:N->[0,infinity) with s(N)=o(N), let K_E(s) be the supremum B(F)/I(F) over all finite N-bit Boolean signs satisfying 0<I(F)<=2^(-s(N)), with B=sum_i H(S_i|S_-i) in bits and ordinary influence. Then K_E(s)=K_E in the extended reals. For any nonconstant seed f, h_m=z*f^(tensor m) is balanced, B(h_m)=mB(f), I(h_m)=mI(f)+1; its point activation obeys B(F_m)>=2^(-k_m)*mB(f) and I(F_m)=2^(-k_m)*(mI(f)+1+k_m), with k_m=o(m) chosen for the s-class. Consequently C_FEI<=K_E(s)+2/ln2 by C018. This is aggregate-erasure transport and does not preserve a selected coordinate witness. Finiteness of K_E(s) remains open.

Review scope receipts: A081 / INDEPENDENTLY_ACCEPTED_LOW_INFLUENCE_FRAGMENT_BY_A081; A090 / HOLDS_AT_STATED_SCOPE; A090 / PENDING; A094 / PENDING

Source: ~\brain_workers\FEI100_20261011\agents\A081\runs\20261013T220111Z-account05-A081-dependency-certificates\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A090\runs\20261013T213537Z-account05-A090-independent-reconstruction\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A099\runs\20261012T044129Z-account05-A099-candidate-assembly\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A099\runs\20261014T001305Z-account05-A099-candidate-assembly\CLAIMS.json

## A086-ACTIVATION-REFERENCE-DEBT-PROJECTION @ 1

For every balanced finite uniform Boolean core g and every r>=1, put p=2^-r,F=1+A_r(g-1),v=p(2-p),Pplus=P_F conditioned on nonempty output. For every subprobability reference Q positive on the support of Pplus, let M=sum Q,q=Q/M,beta=1/(2-p),gamma=q(data spectral set nonempty),and q_g=q(data set | nonempty data). Then vD(Pplus||Q)=-v log2 M+vD_Ber(beta||gamma)+pD(P_g||q_g)+v(1-beta)D(Unif(nonempty control subsets)||q(control | empty data))+p sum_T P_g(T)D(Unif(all control subsets)||q(control | data T)). Consequently vD(Pplus||Q)>=pD(P_g||q_g). Infinite missing-support debt is interpreted in the extended sense. This localizes complete reference debt, without asserting cheap universal references or a lower bound by seed entropy.

Review scope receipts: account05/A094, B19 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A086\runs\20261011T234041Z-account05-A086-joint-code-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A094\runs\20261012T044109Z-account05-A094-proof-chain-challenger\CLAIMS.json

## A086-DISJOINT-SELECTOR-PRESCRIBED-REFERENCE @ 1

For all Boolean G(X), H(Y) on disjoint uniform finite blocks and a fresh uniform selector z, F=(G+H)/2+z(G-H)/2, and every pair of normalized complete finite-cost spectral references R_G,R_H, calibration of each empty atom to the true squared mean gives references R_G^0,R_H^0 with nonincreasing costs c_G^0,c_H^0. The complete normalized output reference Q=rK, r=(R_G^0+R_H^0)/2 embedded on the physical data blocks and K the actual conditional selector law (empty-selector point law on zero true fibers), satisfies CE(P_F,Q)-H(F)=[KL(P_G||R_G^0)+KL(P_H||R_H^0)]/2 and CE(P_F,Q)<=(c_G^0+c_H^0)/2+(2+4/ln2)I_z(F). Also I(F)=[I(G)+I(H)]/2+I_z(F), I_z(F)=(1-EG EH)/2. Consequently supplied child bounds c_j<=K_j I(j) transfer with constant max(K_G,K_H,2+4/ln2). Core debt and single-word rounding remain explicit; no overlapping-data or universal child-reference admission is claimed.

Review scope receipts: A094/account05/B19 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A086\runs\20261013T220217Z-account05-A086-joint-code-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A094\runs\20261014T001244Z-account05-A094-proof-chain-challenger\CLAIMS.json

## A087-CONTROL-TREE-LAMBDA-KL-IDENTITY @ 1

For every balanced Boolean core g on a finite uniform cube and k>=1 fresh fair point controls, let q=2^-k and F=1+A_k(g-1). On the physical control-first tree stopped at the first inactive control or at g, A061 one-sided logarithmic charge lambda_s equals the exact magnitude-mismatch KL residual at every active node s: lambda_s=u-u^2+u^2 log2((1-2u+2u^2)/u^2), u=2^-s. Its physically weighted sum is q(k+A_k)<=4kq with A_k=sum_(s=1..k)2^-s[2s-1+log2(1-2^(1-s)+2^(1-2s))]. Queried influence is kq, terminal influence qI(g), and terminal entropy qH(g); no terminal bound on arbitrary cores is implied.

Review scope receipts: A090 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261011T221055Z-account05-A087-restriction-referee\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A090\runs\20261011T231429Z-account05-A090-independent-reconstruction\CLAIMS.json

## A087-REVIEW-EXCLUSIVE-CONTROLLER-OUTER-BANK @ 1

For any exclusive finite physical controller selecting mutually independent disjoint Boolean cores u_j (or constant signs), let q_j be selector probabilities and let I_data,I_ctrl be the root influences of data and control coordinates. At an actual data query of core j set m=Eu_j,beta=hat u_j(i),v=1-m^2,t=beta^2,a=hat W+m hat C_j and M(s)=sum_T Phi(a_T^2,s hat C_j(T)^2), Phi(A,B)=A log2(1/A)+B log2(1/B)-(A+B)log2(1/(A+B)). With cap=min(M(v),t M(v)/v+q_j t log2(v/t)) and zero cap at t=0 or v=0, every finite adaptive interleaved data-only prefix satisfies sum w cap<=[(1+2/e)/ln2]Pi_I,data+sum_j q_j log2(1/q_j)V_drop,j<=[(1+2/e)/ln2]I_data+2I_ctrl. The exact projected-sector concavity gap J obeys 0<=J<=2q_j t/ln2, hence sum w(cap+J)<=[(3+2/e)/ln2]I_data+2I_ctrl<=[(3+2/e)/ln2]I(F). Actual inner signed entropy and terminal entropy are not paid by this statement.

Review scope receipts: A087 / HOLDS_AT_EXPLICIT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A087\runs\20261013T222530Z-account05-A087-restriction-referee\CLAIMS.json

## A096-UNIFORM-SINGLETON-HALF-TAX @ 1

For every finite Boolean sign under any interior product measure, any singleton physical block X with bias p, and Shannon entropy in bits, let M_X=H(S_X|S_residual), J_X=I(X;T) in the actual physical-child/spectral experiment, r=min(p,1-p), and delta=1-sqrt(1-r). Then J_X-M_X<=h2(r)-h2(delta). The bound is uniform in dimension, residual biases and Boolean children. Consequently lim_{p->0} sup_{all finite actual Boolean signs and all interior residual product biases}(J_X-M_X)/(p log2(1/p))=1/2. The tax expansion is (r/2)log2(1/r)+((log2(e)-1)/2)r+O(r^2 log(1/r)); exact optimal tax at arbitrary nonzero p and influence/composition payment remain unproved.

Review scope receipts: A090 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A090\runs\20261011T231429Z-account05-A090-independent-reconstruction\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A096\runs\20261011T215017Z-account05-A096-live-gap-ledger\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A096\runs\20261011T234252Z-account05-A096-live-gap-ledger\CLAIMS.json

## B19-RANKCODE-REDUCTION @ 1

For every Boolean f on n coordinates and every order pi of [n]: H(f) <= [log2(4+e) + log2(pi^2/4)] I(f) + (2/ln 2) R_pi(f), where R_pi(f) = E_{S ~ fhat^2} sum_{j=1}^{|S|} ln(i_j/j) and i_1 < ... < i_|S| are the pi-positions of the elements of S.

Review scope receipts: A095 / ACCEPT_AT_STATED_SCOPE; A095 / SOURCE_STATEMENT_HASH_METADATA_MISMATCH; account05/A094, B19 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A094\runs\20261012T044109Z-account05-A094-proof-chain-challenger\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A095\runs\20261011T231526Z-account05-A095-restricted-result-extraction\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B19\runs\20261011T224700Z-claude-B19-paper-audit-rankcode\CLAIMS.json

## B19-RANKCODE-GLOBAL-ORDER-NOGO @ 1

For integers L >= 2, m >= 1 let f = prod_{b=1}^m AND_L(x_b) on disjoint blocks (+-1 valued). For every order pi of the mL coordinates, R_pi(f) >= 2^(1-L) sum_{p=1}^{mL} max{0, ln p - ln((L+1)/2 + (p-1) 2^(1-L))}; I(f) = mL 2^(1-L); H(f)/I(f) = H(AND_L)/I(AND_L) < 4; and liminf_{m -> infinity} min_pi R_pi(f)/I(f) >= (L-1) ln 2. Hence the right side of B19-RANKCODE-REDUCTION is at least (2(L-1) - o(1)) I(f) for every order while H(f) < 4 I(f): no single-order rank code proves FEI with a constant uniform over all Boolean functions.

Review scope receipts: A095 / ACCEPT_AT_STATED_SCOPE; A095 / SOURCE_STATEMENT_HASH_METADATA_MISMATCH; account05/A094, B19 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A094\runs\20261012T044109Z-account05-A094-proof-chain-challenger\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A095\runs\20261011T231526Z-account05-A095-restricted-result-extraction\CLAIMS.json; ~\brain_workers\FEI100_20261011\claude\B19\runs\20261011T224700Z-claude-B19-paper-audit-rankcode\CLAIMS.json

## A097-ONE-SHARED-DATA-COLLISION-TRANSFER @ 1

For all Boolean G(s,X),H(s,Y) with one shared fair physical bit s, disjoint private uniform blocks X,Y and a fresh fair selector z, and normalized complete finite-cost references R_G,R_H, calibrate each reference separately on the two atoms empty and {s} to the true Fourier probabilities and rescale its complement. Costs c_G^c,c_H^c do not increase; the exact decrease is the categorical KL of those two atoms and the complement. The normalized compatible reference Q=rK, r=(R_G^c+R_H^c)/2 and K the actual conditional selector spectrum with a fixed normalized kernel on zero true fibers, has zero posterior mismatch kappa and D(P_F||Q)=[D(P_G||R_G^c)+D(P_H||R_H^c)]/2. Its complete cost is CE_F=(c_G^c+c_H^c)/2+Delta<=(c_G^c+c_H^c)/2+(2+4/ln2)Inf_z(F), where F=(G+H)/2+z(G-H)/2, Delta=B_z+J_z and I(F)=[I(G)+I(H)]/2+Inf_z(F), including s only through its actual averaged influence. Thus supplied child bounds transfer with constant max(K_G,K_H,2+4/ln2). For a t-bit shared block the same constant holds if both conditional-mean Fourier vectors have l1 norm <=1; without that hypothesis a proved coefficient is 2+(2*2^(t/2)+2)/ln2. No absolute selector-only coefficient holds for unrestricted sharing: selecting the even-k quadratic bent sign and its actual singleton flip has Inf_z=2^-k and Delta/Inf_z>=k-log2(16/9) for every even k>=4. This is a scoped reference transfer and an actual Boolean obstruction to its unrestricted selector-only extension, not a disproof of FEI.

Review scope receipts: A094/account05/B19 / HOLDS_AT_STATED_SCOPE

Source: ~\brain_workers\FEI100_20261011\agents\A094\runs\20261014T001244Z-account05-A094-proof-chain-challenger\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A097\runs\20261013T222610Z-account05-A097-cross-route-transfer\CLAIMS.json; ~\brain_workers\FEI100_20261011\agents\A099\runs\20261014T001305Z-account05-A099-candidate-assembly\CLAIMS.json

## B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO @ 1

For every finite K,A,B >= 0 there is a genuine Boolean physical split with L > K*d + A*V_post + B*M_inf, where q_W=(Ghat(W)^2+Hhat(W)^2)/2, e_W=(Ghat(W)-Hhat(W))^2/4, theta_W=e_W/q_W, d=sum e_W, L=sum q_W*h2(theta_W), V_post=sum q_W*(theta_W-d)^2, and M_inf=sum_i(Inf_i(G)-Inf_i(H))^2.

Review scope receipts: account01/B19 / ACCEPT_AT_STATED_SCOPE; recovery fei_audit / NO_GAP_FOUND_AT_STATED_SCOPE

Source: ~\mop_fei100\reports\fei-2026-10-11\CLAIM_REGISTRY.json

## Partial, disputed and withdrawn

- A089-EXACT-EXISTENTIAL-ERASURE-REPAIR @ 1: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION @ 1: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- A015-CONDITIONED-MINTERM-LOCATION-BARRIER @ 1: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- A095-RANK-KL-EQUIVALENCE @ 2: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- A021-CONTROLLER-EXPOSURE-REFINEMENT @ 1: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER @ 2: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- A057-EXCLUSIVE-SELECTOR-VARIANCE-CAP-PAYMENT @ 1: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- A042-SHARP-MAJORITY3-BIASED-ENDPOINT @ 1: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- B09-BIASED-BLOCK-UNCERTAINTY @ 1: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- A052-OPTIMAL-RECENTRING-SINGLETON-COLLAPSE @ 1: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- A066-POSITIVE-RESTRICTION-HEAT-LEDGER @ 1: FULL_ACCEPTANCE_WITHHELD_SCOPE_OBJECTION
- B14-LEAD-POINT-DEFECT-NEUTRALIZATION @ 1: FULL_ACCEPTANCE_WITHHELD_SCOPE_OBJECTION
- A097-B05-COMPATIBLE-REFERENCE-CERTIFICATE @ 1: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- B09-CLAUDE-SHARP-ONE-BIT-TAX @ 1: PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY
- A021-UNIFORM-RARE-CORE-EXPANSION @ 1: WITHDRAWN_AS_FULL_CLAIM_FALSE_REMAINDER
