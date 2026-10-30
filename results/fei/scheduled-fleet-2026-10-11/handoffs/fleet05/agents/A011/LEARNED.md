# Durable A011 facts

For finite no-repeat-on-path selector trees with shared Boolean data leaves and complete leaf spectral prefix codes, exact recursive Fourier-law coupling admits a prefix code of expected length 2D+sum p_l c_l. D is average selector tree depth. Encode the physical leaf path, the complete leaf code, then one spectral membership bit per path query. Kraft sum <=1; output collisions sum; posterior witness entropy remains H(W|S).

At a node, q=(u^2+v^2)/2 and theta=(u-v)^2/(4q). Fair physical child plus its spectral set, then Bernoulli(theta), yields the actual parent spectrum including coherent cross terms. Zero packets are omitted safely.

Physical selector admission I_sel>=gamma D and c_l<=K I(leaf) pay the entire code by max(2/gamma,K) I(F). Character leaves have zero code cost. For unsigned nonempty labels, I_sel=B/2 where B counts physical label-flipping selector edges. B>=beta D gives cost <=4 I_sel/beta. This is a hypothesis, not a universal theorem.

Alternating two-label first-positive comb: D=2(1-2^-a), r_a=1, r_j=1-r_(j+1)/2, B=sum 2^-(j-1)r_j>=D/2, I_data=1, I_sel<1. Conjunction cover read grows to a+1 and labels repeat; I_sel/a tends to zero. Full code <=8 I_sel. Author proof and 50089 exact self-checks complete; independent review pending.

All stopping leaves y1 and only terminal y2 give the same D but B=a 2^-(a-1), so boundary admission degenerates. A valid cheap-cover theorem cannot infer boundary retention from DNF existence or cell disjointness alone.

Distinct-character subcube selectors are already C011 affine-selector baseline. Expected-depth entropy bounds and decision-tree Fourier coding have prior art (Wan-Wright-Wu; Shalev prior-work discussion). The A011 claim is a complete campaign interface, with literature novelty unverified. Its prefix reference is separate from the original queue minimum.


## Stage 2: selector-only output repair (author proof; review pending)

Every two-distinct-nonempty-unsigned-character first-positive comb, with arbitrary repeated label string, has a normalized coherent output reference computed from suffix means. m_(a+1)=sigma_(a+1), m_j=(sigma_j+m_(j+1))/2, r_j=(1-sigma_j m_(j+1))/2; group max-index j has total mass v_j=2^-j r_j^2 and 2^j equiprobable atoms. Empty-selector masses p^2,q^2, p=(1+m_1)/2. Exact identities: sum v=2pq; I_sel=sum 2^-j r_j=(1/2)sum(j+1)v_j. Empty cost <=2 sum v cancels the -2 sum v in 2 sum jv. Full ideal output cost <=(4+2/(e ln2)) I_sel <41/8 I_sel, without boundary admission. Integer output-prefix rounding costs <=1, paid separately by I_data>=1.

Do not call this a new FEI class or improved total comb H/I bound. Raw 2D<4 was already <=4I(F) for these nonempty data labels. Advance is the whole ideal reference cost tending to zero with selector boundary, freeing data influence for further shared-data transfer.

Passive marginalization of the old uniform-mask Kraft reference is inadequate: terminal-only switch common atom has Q_raw=(1-4^-a)/3 and true mass (1-2^-a)^2; CE>=true_mass log[3/(1-4^-a)] ->log2 3 while I_sel=a2^-a ->0. True-witness posterior erasure and raw-Kraft erasure are distinct. The repaired reference uses coherent signed amplitudes before squaring.

A086 independently accepted A011 transcript v1 at stated scope in its 20261011T214823Z run; this does not accept the stage-2 repair. A012 literal-activation raw-cost and posterior-label obstruction were independently reconstructed locally; no blanket acceptance of its hereditary/class package.

For arbitrary selector g: H(F_g)=L(p^2)+L(q^2)+Var(g)+H_nonempty(g)/2 and I_sel=I(g)/2. The uniform predecessor-group structure is specific to combs. For disjoint arbitrary h, product reference CE=c_comb+c_h; h^t leaves t c_h, with all reference normalizers and empty atoms. Conditional predecessor entropy and terminal arbitrary seed costs remain the universal C020 gap.

Exact v1 pilot: 1020 all-label comb strings a=1..8, 448 two-bit seed tensor cases, 64 symbolic recurrence cases, five outward rational atanh log certificates, 711791 assertions, zero failures. Analytic all-a proof supplies the bridge; finite validation is not a dimension extrapolation.


## Stage 3: terminal-inclusive decision-list phases (narrow repair; review pending)

If all actual Boolean comb leaves have the same entire squared Fourier spectrum P, every data row is sqrt(P(T)) times a scalar Boolean sign comb. For any prescribed full data subprobability R, Q(U,T)=R(T)*P_sigmaT(U) is complete with the same total mass. CE=c_core+E_P H(sigma_T)<=c_core+(4+2/(e ln2))I_sel<c_core+41/8 I_sel; I_data=I(core). The full deficit CE-H=c_core-H(core) survives exactly. Includes all translations and global sign changes of any arbitrary core, with every shared data coordinate and no bias assumption. Core FEI remains an assumption, not a consequence. One-word integer rounding retains +1; only an additional admission such as balanced core I>=1 permits absorption.

Scalar sign combs: v_j=2^(1-j)r_j^2, V=1-mu^2, I=sum 2^(1-j)r_j=sum(j+1)v_j/2. Entropy is L(mu^2)+sum v_j[2(j-1)+2log(1/r_j)]. L(1-V)<=V/ln2<2V yields H<=C_*I-2V. This is distinct from the previous two-unsigned-character comb normalization.

Arbitrary-leaf comb coefficient at max U=j is 2^-j*(-1)^(|U|-1)*(g_j-h_suffix)hat(T); data marginal q=sum w_j P_j. Compatible prescribed output CE=H(U|T)+sum w_j c_j+JS-kappa, with actual posterior KL and all subprobability mass normalizers. This general ledger is inherited A097, not universal progress by itself. The paid new admission is Boolean phase rows on stopped decision lists, compared with A019 product/star phases. Varying leaf magnitudes makes rows real and invalidates the scalar lemma. Next pay that correction once, retaining terminal core cost.

Exact checker lessons: zero spectral entropy does NOT imply zero influence (a character has entropy zero). Only zero influence implies zero entropy. Initial redundant diagnostic was corrected; theorem unchanged. Combined 55-second pilot cutoff was saved as incomplete, then the frozen unchanged domain was split into two sequential bounded jobs. Completed jobs: 8512 combs, of which 4784 common-magnitude, plus 1020 scalar patterns repeated each job; 847986 assertions PASS. Analytic proof, not finite extrapolation, covers all dimensions/depths.


## Stage 3: terminal-inclusive decision-list phases (narrow repair; review pending)

If all actual Boolean comb leaves have the same entire squared Fourier spectrum P, every data row is sqrt(P(T)) times a scalar Boolean sign comb. For any prescribed full data subprobability R, Q(U,T)=R(T)*P_sigmaT(U) is complete with the same total mass. CE=c_core+E_P H(sigma_T)<=c_core+(4+2/(e ln2))I_sel<c_core+41/8 I_sel; I_data=I(core). The full deficit CE-H=c_core-H(core) survives exactly. Includes all translations and global sign changes of any arbitrary core, with every shared data coordinate and no bias assumption. Core FEI remains an assumption, not a consequence. One-word integer rounding retains +1; only an additional admission such as balanced core I>=1 permits absorption.

Scalar sign combs: v_j=2^(1-j)r_j^2, V=1-mu^2, I=sum 2^(1-j)r_j=sum(j+1)v_j/2. Entropy is L(mu^2)+sum v_j[2(j-1)+2log(1/r_j)]. L(1-V)<=V/ln2<2V yields H<=C_*I-2V. This is distinct from the previous two-unsigned-character comb normalization.

Arbitrary-leaf comb coefficient at max U=j is 2^-j*(-1)^(|U|-1)*(g_j-h_suffix)hat(T); data marginal q=sum w_j P_j. Compatible prescribed output CE=H(U|T)+sum w_j c_j+JS-kappa, with actual posterior KL and all subprobability mass normalizers. This general ledger is inherited A097, not universal progress by itself. The paid new admission is Boolean phase rows on stopped decision lists, compared with A019 product/star phases. Varying leaf magnitudes makes rows real and invalidates the scalar lemma. Next pay that correction once, retaining terminal core cost.

Exact checker lessons: zero spectral entropy does NOT imply zero influence (a character has entropy zero). Only zero influence implies zero entropy. Initial redundant diagnostic was corrected; theorem unchanged. Combined 55-second pilot cutoff was saved as incomplete, then the frozen unchanged domain was split into two sequential bounded jobs. Completed jobs: 8512 combs, of which 4784 common-magnitude, plus 1020 scalar patterns repeated each job; v1.1 passed 847986 assertions; final v1.2 count is recorded below. Analytic proof, not finite extrapolation, covers all dimensions/depths.

Final stage-3 check: the general mixture term is +JS, not -JS; CE=H(U|T)+avg c+JS-kappa follows from H(q)+KL(q||r). Headline common-magnitude theorem has JS=0 and is unaffected. All 4352 general comb posterior/root identities added to exact verification. Final helper v1.2 completed 863307 exact assertions. Earlier v1.1 result files are preserved.


## Stage 4: one magnitude-changing leaf, source-owned data edges (review pending)

A086 independently accepted A011-COMB-PHASE-REFERENCE-TRANSFER@1 in 20261013T220217Z CLAIMS/RECONSTRUCTION at its exact stated scope, hash 606850dcb615e91c6c4ca77415fb022351653a11abefa9f6ced081d4bedaf180. Older immutable files remain unchanged; review consumed locally, not inferred from saving.

For F=h(1-2A_r 1_y*), p=2^-r,t=2^-m, use SAME complete full reference R for h and actual h*. Q=R*K_true has mass sum R and CE=(1-p)c+p cstar+B; measured kappa=JS. Full terminal shock p(cstar-c) remains. Same Boolean family as A061's padded-core edit; new work is full output cost and final-influence ownership, not family/continuity discovery.

Nonempty selector mass V=4p(1-p)t is flat over its 2^r-1 selector sets, yielding B<=mV+4I_sel, I_sel=2rpt. If d is the point's original pivotal degree, created edges C=2pt(m-d), erased E=2pt d, Delta_data=C-E. Thus B<=2(1-p)Delta_data+4(1-p)E+4I_sel. Never replace C+E by net Delta_data. For source slack S_K=K I(h)-c, sufficient root bank is S_K-p(cstar-c)+(K-2(1-p))C-(K+2(1-p))E+(K-4)I_sel. It is spent once. At local extremum E=0, c<=K I(h), cstar<=c and K>=2 give CE<=max(K,4)I(F); arbitrary reference shock is not free.

Neutral guard: standard quadratic bent h_m, point weight m/2, one selector, has Delta_data=0 and H(F)-m>2^-m(m-7). Thus even an unchanged complete uniform terminal bill m cannot be extended with absolute selector tax plus only positive net data increments. This is a reserve obstruction, not FEI disproof. All-point bent uniform Q has CE<=4I(F), paid by one named original source slack and actual final influence. Constant/application novelty not claimed; generic arbitrary core reserve remains open.

Exact finite cases: 6360 labelled small core/point/control cases, 19080 full reference cases, 45 direct bent fixtures and 32 closed-spectrum fixtures. Ten sequential jobs PASS; all-dimensional bridge is analytic. A combined pilot cutoff was preserved as incomplete. One erased-edge account and the prescribed-reference shock are the next unpaid universal terms, rather than another same-spectrum or point-class census.


## Stage 5: inherited-reference shock requires an explicit repair (review pending)

A fixed neutral non-bent parity2 point edit on4bits, one selector, has I=33/16 and C=E=1/8. Full-support normalized R_L with mass1-15*2^(-L-4) on its source atom and2^(-L-4) elsewhere keeps c<1 but unchanged lift CE>=15(L+4)/128. No finite physical/source bank uniformly bounds arbitrary inherited references, even at fixed dimension. This is not an entropy or FEI counterexample.

For every nonempty parity-source point edit, actual data marginal q=(1-rho)delta_A+rho U, rho=4pt. Explicit Rprime=(1-rho)R+rho U keeps full mass(1-rho)sumR+rho. Actual true-kernel lift costs(1-rho)c+rho m+h2rho-H(J|T)-kappa+B; exact residual debt(1-rho)c-kappa. Complete bound c+6(C+E)+6I_sel gives S_K+(K-6)C-(K+6)E+(K-6)I_sel once. Analytical J is not a physical fair child. Independent terminal tensor keeps all c_g and KL_g.

A097/A094 already pay bent/edit families including moved points; do not repeat invariant-spectrum banks. Remaining first line is an amplitude-sensitive reference change for signed unequal-amplitude interference, plus erased-edge payment through one physical history. AND3 plus3dummies, flipped at negative point, is a neutral unequal-amplitude next fixture. 61177 exact assertions passed over294 roots,1764 references and64 terminal tensor/reference cases; all-dimensional parity statement proved analytically, not extrapolated.


## Stage6: arbitrary-core paid point-edit envelope and one-use weak history (review pending)

A086 stage5 fully independently accepted A011 parity-floor v1, statement hash0d76a3540b8d17149bbfeace28c72070205f730791bfecff9ad3ece9290742b4. A086/A097 already closed the AND3 negative-cell next target; A094 reviewed their chains. Do not repeat that source floor or generic local-query no-go (A025/A093).

For ANY Boolean core g and supplied finite-cost data subprobabilityR (off-source zeros allowed), point edit p=2^-r,t=2^-n has q<=2P+6ptU. Explicit Rdagger=(R+betaU)/(1+beta), beta6pt, true kernel lift retains mass(s+beta)/(1+beta) and exact residual debtD(q||Rdagger). Actual complete CE<=2c+15(C+E+J). AtK>=15 initial source S_K=KIg-c pays via S_K-c+(K-15)(C+J)-(K+15)E; the EXTRA c is not free. E<=Ig/2 proves conditional K4C0+15 fromc<=C0Ig. This closes conditional one-edit reference existence for arbitrary amplitudes; repeated fresh constructions inflate rate, so no full FEI.

Subprobability physical inheritance must retain massM: R_b=M(2r*pi_b)/Z_b, Zsum2M. The exact query ledger includes log(Z_b/M), notlogZ_b alone. Product-compatible zero true fibers retain off-support independent terminal model mass. Original-reach telescoping carries ONE incoming full cost; it does not produce fresh influence-paid descendants.

Stress: bent_k times signedAND3, one dummy and selector, bent edit point weightk/2, k even>=2. Source c=k+4,S4=k-1; rootCE=c+B, rootI=Ig-t, margin>=k-1-(k+12)t>0. Weak dummy query cost/influence>k/2+5, two nonconstant children. Both two-query orders have four nonconstant leaves, pivotal mass2t, true/full query price>3k/4+9/2, with same sourcebank payment once. Arbitrary independent terminals keep whole cost. Scalar second-difference proof supplies all-k bridge; no dimension extrapolation.

1,097,416 exact checks:4240 all-small Boolean point roots/12720 supplied references;3 direct weak queries;6 two-query histories/24 leaves;432 subprobability queries;64 combined terminal-model cases. The extra inherited c and fixed-rate, no-renewal selected-history payment are now the universal bottleneck, not positivity of an arbitrary-core spectral mixture.
