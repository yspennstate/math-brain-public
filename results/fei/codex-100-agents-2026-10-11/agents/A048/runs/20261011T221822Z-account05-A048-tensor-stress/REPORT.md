# exact target, quantifiers, hypotheses and units

A048/B10 verifies the tensor and activation scope of the existing B09-BIASED-BLOCK-UNCERTAINTY v1 candidate. It does not open a third broad potential candidate: A046 and A047 already have complete pending bundles. The original B09 uncertainty theorem remains pending independent review. Full FEI remains OPEN.

For a genuine Boolean sign f under an interior independent product input law, reveal physical block A and let B be its complement. In the normalized product Fourier basis let S have law fhat(S)^2, including the empty atom. Define M_A=H(S_A|S_B), J_A=I(Z;T), where Z is the actual physical assignment on A and T is sampled from the normalized Boolean child spectrum, L_A=H(f)-E_Z H(f_Z)=M_A+J_A, Delta_A=sum_{i in A}[h2(p_i)+log2 max(p_i,1-p_i)], and P_A=M_A+Delta_A. The existing assertion is J_A<=P_A. Entropies are bits. Deterministic coordinates are contracted. Ordinary physical influence and biased spectral energy are explicitly distinguished below.

The target is exact transformation of this ledger under aligned disjoint tensor powers, common unrevealed factors, and sparse activations. No universal bound on M or on terminal entropy is presumed. A separate collision normalization control uses v,Z,L_coll,T_coll; its L is not the restriction decrement L_A.

# sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2; README, CURRENT_STATUS (2026-10-11T20:06:24Z snapshot), claim and obstruction registries, relevant A048 packet and B10 dispatch records, and campaign plan B10/A048 contract. BOARD at start was the supervisor's 2026-10-11 22:16 UTC snapshot. The specified claude/B10/STREAM_NOTES.md was absent; no direction was inferred.

Read original B09 REPORT.md sections 2,3,5,6,8, run 20261011T195500Z-account01-B09-biased-restriction-uncertainty, immutable source commit adb671ffcda143fa68347806bb96e8c305621a7d. Its section 5 tensor discussion is the scope being verified, not a premise for broader composition. Read A046 REPORT.md, especially its frozen candidate and aligned tensor guard; A047 REPORT.md, especially the fixed-child coefficient and common-character balancing; A021 REPORT.md exact balanced activation and control-first KL ledger; A036 REPORT.md normalization/payment versus recovery. These establish that balanced activation identities and the raw collision failure are existing work, not new discoveries here. Earlier B05 and B19 reports were inspected for the fixed-price obstruction's precise scope.

Consulted supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and source catalog. Relevant source passages read were BLOCK_RESTRICTION_IDENTITY equations (1)-(10), ERASURE_REDUCTION section 3, ROUTE_MAP sections 2 and 4, OVERLAPPING_PRODUCT_NOTE, and LOG_ALLOCATION's tensor-invariance guard. Unbundled originals linked from the route map were not fetched or used as proof premises.

Inspected the supplied four paper texts: threshold 38pp sections 7 and 8.3-8.4, Proposition 7.1/Corollary 7.2 and Proposition 8.9/Corollary 8.10; earlier threshold 29pp introduction/definitions; percolation 30pp introduction/Theorems 1.1-1.2 and definition J=sum 4p_i(1-p_i)Inf_i; alternate percolation 31pp introduction and scope. The alternate percolation version has a different singularity claim and is not substituted for the 30pp text. No full independent paper audit or novelty claim is made. Source hashes bind local bytes and stated inspection scope, not proof acceptance.

# complete derivation or exact first unsupported line

**1. Exact product and common-factor laws.** Biased orthonormal Fourier coefficients of f(x)g(y) on disjoint independent inputs are fhat(R)ghat(U); their squared law is a product. For aligned reveals A=A_f union A_g the physical assignment and child-spectrum experiment are also independent products. Entropy chain rules therefore give M=M_f+M_g, J=J_f+J_g, L=L_f+L_g, Delta=Delta_f+Delta_g and P=P_f+P_g. All identities hold for arbitrary finite factor counts and different biases, including zero spectral atoms. Thus t aligned copies give exactly t times each ledger, with no t log t term. Uniform H and I also multiply by t. This independently reconstructs the aligned tensor component of A046 and the narrow valid interpretation of B09 section 5; it does not extend to overlapping variables or nonlinear composition.

If an arbitrary independent Boolean factor g is wholly unrevealed, M,J,L,Delta,P are unchanged, while H(fg)=H(f)+H(g) and E H((fg)_Z)=E H(f_Z)+H(g). The proof follows either from the product channel or by cancellation in these two entropies. Taking g as t independent copies of any seed makes the unpaid terminal entropy exactly tH(seed). This is a mathematical obstruction to interpreting a paid local decrement as a paid whole entropy. It does not refute any claim that actually includes the terminal cost.

**2. Irrelevant-coordinate tax.** Append a fresh biased coordinate X which f ignores and include X in A. Its spectral label is deterministic empty and its physical value is independent of T. Hence M,J,L and revealed-block influence do not change, but Delta increases by delta(p). For 0<p<1/2, delta(p)=p log2((1-p)/p)>0. An explicit witness is f(y)=2y-1 with y fair, A={X}, p=1/8: M=J=L=I_A=0, P=(log2 7)/8>0. Even total-influence payment P<=K I(f) is impossible for the unreduced displayed P: append r such revealed dummies, retain I(f)=1, and P=r(log2 7)/8.

This is a failed *payment* of the displayed upper bound, not a failure of J<=P, and no source is alleged to have already proved that payment. Contracting physically irrelevant coordinates repairs this specific problem: apply the original candidate to A_eff, the coordinates in A on which f actually depends. Independence proves the same M,J and removes the dummy tax. It does not solve payment on essential coordinates. A character factor has positive influence and is not an irrelevant coordinate; these two operations must not be conflated.

**3. Shared biased selector and moving tensors.** Let g be any Boolean core under a fixed product law, with coefficients G_T, mean m, v=1-m^2, and F=1+X(g-1), where X is a fresh bit with P(X=1)=p. Then, for each nonempty data label T, the selector-absent/present squared masses are p^2 G_T^2 and p(1-p)G_T^2. At the empty data label they are a0=(1-p+pm)^2 and b0=p(1-p)(1-m)^2, whose sum is q0=1-pv. The residual marginal is q0 at empty and pG_T^2 elsewhere. Consequently, writing e(x)=-x log2 x and e(0)=0,

    M=e(a0)+e(b0)-e(q0)+pv h2(p),
    J=h2(pv)-p h2(v),
    H(F)=pH(g)+M+J.

The last identity follows because the two physical children are constant 1 and g. Thus M,J and debt depend only on p and the core mean, not on its Fourier entropy. For g_t=product of t disjoint copies of a fixed core with mean mu, replace m by mu^t and H(g) by tH(g_1). A common selector is not an aligned product of t selectors: its ledger is this mean-dependent expression, rather than t copies of the one-core ledger. For balanced cores, M=J=h2(p), L=2h2(p), debt zero, and the terminal term is ptH(g_1). This is consistent with A047's constant/balanced zero-debt class; it is a scope test, not a new endpoint discovery.

For |mu|<1 and fixed p, the displayed expressions are continuous as mu^t tends to zero, so M,J tend to h2(p) despite the growing core entropy. No dimension-dependent asymptotic remainder is needed: the formula is exact at every t. For a balanced core the selector's biased spectral energy is Q_X=sum_T b_T=2p(1-p), whereas its physical pivotal probability is 1/2. L/Q_X=h2(p)/(p(1-p)) diverges logarithmically as p tends to zero. This diagnostic cannot be called a divergence of L divided by physical influence; it uses spectral energy under bias. The terminal term still contains the arbitrary core problem.

**4. Uniform point-control activation, including unbalanced cores.** Now A_k is the indicator of one point on k fresh fair bits, p=2^-k, and F=1+A_k(g-1), with uniform Boolean core g and m=E g. Write d=1-m and v=1-m^2. All nonempty-data masses are p^2 G_T^2 for each of 2^k control labels. At empty data the empty-control mass is (1-pd)^2 and each nonempty-control mass is p^2d^2. Put q0=1-pv and r=p(1-p)d^2. The exact ledgers are

    M=q0 h2(r/q0)+r log2(2^k-1)+pv k,
    J=h2(pv)-p h2(v),
    L=e((1-pd)^2)+(p-p^2)d^2[2k-log2(d^2)]+2kpv-p e(m^2),
    I_A=kp d,   I(F)=pI(g)+kp d,   E H(F_Z)=pH(g).

Terms involving zero d are zero by continuity. Direct edge counting proves the influence: each control is pivotal with probability 2p P(g=-1)=pd, and each data influence is multiplied by p. The entropy expression follows by summing the two explicit mass classes and subtracting pH(g).

There is an elementary paid local bound for this specific activation block. Since e((1-y)^2)<=2y/ln2 for 0<=y<=1, and d^2 log2(1/d^2)<=2d/(e ln2) for 0<d<=1 (for d>=1 this term is nonpositive), discard the negative -p e(m^2) and -2kp^2d^2 terms to obtain

    0<=L<=4kp d+[2(1+1/e)/ln2]pd
            <=[4+2(1+1/e)/(k ln2)] I_A <=8 I_A.

Here d^2+v=2d. The constant in square brackets is below 8: e>8/3 and ln2>11/16 imply 2(1+1/e)/ln2<4. The latter logarithm bound follows from the first two positive atanh terms, ln2>2(1/3+1/81)=56/81>11/16. The final inequality is strict when I_A>0; the d=0 case is identically zero. Positivity of L follows from L=M+J, each an entropy/information. This paid activation decrement is compatible with arbitrary terminal entropy pH(g); it does not close FEI for arbitrary activated cores.

Keeping logarithms and remainders separate gives a uniform estimate across every m in [-1,1], including moving tensors:

    |L-4pk(1-m)|<=17p+8kp^2,
    |J-pkv|<3p,
    |M-pk(3-4m+m^2)|<=20p+8kp^2.

To check the first bound, the empty term is at most 4p/ln2<8p; |d^2 log2 d^2|<=8 on [0,4]; e(m^2)<=1/(e ln2)<1; and 2kp^2d^2<=8kp^2. For J, expand h2(pv)-p h2(v)=pvk+e(1-pv)-p e(1-v); the remaining absolute value is at most p/ln2+p/(e ln2)<3p. Thus the only activation logarithm is k=log2(1/p); no t log t appears. The balanced case reduces to the exact identities already proved in threshold Proposition 8.9 and A021. The present general-mean ledger supplies a verification envelope across unbalanced tensor cores.

**5. Collision normalization and Renyi guards.** For any finite nonnegative collision array v with total Z>0, L_coll=sum e(v_U), R=v/Z and T_coll=L_coll/Z, direct expansion gives T_coll=H(R)-log2 Z. For product-compatible amplitude references the collision arrays tensor, so Z_t=Z^t, L_t=t Z^(t-1)L_coll, T_t=tT_coll, H(R_t)=tH(R). The raw exponential factor is a known control, not a discovery here. Rescaling v by c>0 preserves R but sends T to T-log2 c. A collision tensor factor with Z!=1 must therefore retain its log normalizer; arbitrary independent factors cannot be erased from raw-L payments. Product phase completions must also be preserved; pointwise sign choices at zeros are not a tensor theorem. No new Boolean collision payment or recovery bound is claimed.

The supplied exact point-defect calculation shows each fixed lower-order spectral Renyi entropy H_alpha/I tends to infinity for alpha<1, whereas Shannon H/I tends to 4. A fixed-Renyi substitution cannot be used to repair any of the tested budgets. This is an existing control, not a new disproof of Shannon FEI.

The first unsupported universal line is: after contracting irrelevant revealed coordinates, pay the complete stopping-tree conditional cost plus the expected terminal entropy by one dimension-independent influence budget. Aligned additivity, common-factor cancellation and a paid point-control decrement do not establish that statement.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before computation: 1,962 cases, no symmetry quotient or random search, maximum explicit dimension 7, estimated memory 80 MB, pilot/runtime cap 60 seconds. Cases: all 278 actual Boolean sign tables on n=0,1,2,3, each with k=1,2,3 point controls (834) and selector p=1/8,1/2,7/8 (834); all 278 as common unrevealed factors; nine moving-tensor selector cases; three aligned biased AND tensors; four rational collision algebra controls. The last four are algebra checks and not Boolean counterexamples. No heavy job or >300 MB allocation was planned.

Command from A048: `python -X utf8 runs/20261011T221822Z-account05-A048-tensor-stress/code/check.py`. Actual truth tables are reconstructed, integer FWHT spectra are compared with the displayed signed coefficients, physical edge influences are compared with spectral cardinality, and biased squared spectra are independently computed using centered nonnormalized rational bases divided by their exact squared norms. Entropy equalities are verified as rational coefficient vectors of prime logarithms; cancellation of identical vectors proves equality and does not assume logarithms are linearly independent.

Two strict signs use a separate rational logarithm enclosure: scale x to [1,2), set z=(x-1)/(x+1), take 24 positive atanh terms, and bound the tail by 2z^49/[49(1-z^2)]. Divide by a positive ln2 interval and restore the integer scale; negative weights reverse endpoints. Exact numerators/denominators are saved in out/CHECK.json. The original AND debt is independently certified >1195/10000 bits, and the dummy tax is strictly positive. These are component reconstructions, not a full acceptance of B09's uncertainty proof.

The first run found a physical branch-convention bug, documented in out/INITIAL_FAILURE.md: the uniform point helper activated at zero, while the biased selector formula activated at one. The corrected biased truth tables reverse that control bit; formulas and frozen parameter domains were unchanged. Final results and observed arithmetic runtime are in out/CHECK.json; final schema/source validation is in out/VALIDATION.json. Finite checks validate the implementation; the displayed proofs supply all-parameter transformation laws and the local bound. No process was intentionally started to survive its command.

# proof dependencies and changed downstream conclusions

The verification uses only product Fourier expansion, exact physical channels, entropy chain rules, elementary one-variable calculus and the proved rational logarithm remainder. No unaccepted B09 upper inequality is a premise. CLAIMS.json retains B09's existing exact statement/version and records a partial tensor/channel scope review, without claiming acceptance of the Maassen-Uffink step. No third broad candidate is opened.

Downstream scope correction: A040/A049/A050 should contract irrelevant coordinates before attempting to pay the displayed tax; A023/A028/A064 should retain arbitrary terminal entropy even when the activation decrement has a local influence payment; A047's fixed-child endpoint cannot be replaced by t-fold additivity when a selector is shared. A036's normalized collision payment remains separate from recovery and unchanged by this control. No shared registry was edited.

# one next mathematical action and independent reviewer

Next action: A050/A064 should construct a factor-aware, essential-coordinate stopping-tree ledger in which arbitrary unrevealed tensor entropy remains as an explicit terminal obligation, then test its claimed nonreuse payment on the already accepted sparse-bent point-surgery tree. This addresses the exact unpaid bridge rather than repeating balanced activation or the fixed-child boundary census. A092 is primary independent reviewer, A087 alternate; A040/A049 are assigned consumers.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, matching PACKET_DELTA.json, FROZEN_SPEC.json, TENSOR_POTENTIAL_LEDGER.tex, TENSOR_GUARDS.md, scripts and exact outputs are saved only inside the assigned A048 folder. Rolling STATUS, WORKLOG and LEARNED are current. code/finalize.py checks exact protocol key sets, claim statement hash, progress-copy identity and all file sizes below 20 MB, and creates SHA256 persistence receipts. Source hashes state inspection scopes. No git, messages, brain writes, another-agent changes, shared-tree mutations or publication occurred. Supervisor copy, mirror verification, independent acceptance and downstream use remain unverified. Missing B10 lead notes are an access fact, not a mathematical block.

# Universal bridge

This stage moves C019 stopping-tree payment by exactly separating tensor-additive local debt, the paid point-control activation decrement (L<=8I_A, strict for I_A>0), bias tax from irrelevant revealed coordinates, and arbitrary terminal entropy hidden by a common unrevealed factor. The local tensor review and concrete scope guards are complete; the essential-coordinate whole-tree payment and terminal entropy bound remain open. NEXT is the shortest bridge to full FEI because it targets those conserved-budget and terminal obligations directly on the already established obstruction tree, rather than proving another isolated activated-core class result.
