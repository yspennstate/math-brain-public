# Zero-refund deferral versus influence compression

All entropies and complete cross-entropies use bits. Fix ANY Boolean core g on n coordinates, alpha_j=Inf_j(g), H=H(g), J=I(g). Let L>=2 be an integer and replace input j by the parity of a disjoint L-coordinate block. A deferral query reveals a physical coordinate only while its block has at least two unrevealed coordinates. Stop at any finite adaptive frontier, possibly after reducing every block to one coordinate. References are the exact actual spectral laws, including the empty coefficient. No source construction with cost O(J) is assumed.

## 1. Spectral and influence identities

Write g=sum_S a_S chi_S. At a node, let ell_j>=1 be the remaining block sizes and theta_j the product of the already revealed input signs in block j. The restricted function is g(theta_j product_{k in block j} x_k : j=1..n). Its Fourier coefficient at the union of the remaining blocks indexed by S is a_S product_{j in S}theta_j, and every other coefficient is zero. Distinct S remain distinct because ell_j>=1. Therefore its exact positive probability multiset is {a_S^2:a_S!=0}; entropy and exact-reference CE are H at EVERY node. Every remaining physical coordinate in block j has influence alpha_j. Thus

    I(node)=sum_j ell_j alpha_j.

Input sign changes preserve every alpha_j; this formula remains valid under adaptive histories.

Consider a legal query in block j, ell_j>=2. No occupied Fourier labels differ by this physical singleton: such a difference would contain a nonempty proper part of the block. Consequently every residual fiber has at most one occupied endpoint. Its spectral erasure B_i is zero. The two restricted squared spectra both equal the physical frequency marginal of the parent spectrum. Inherited exact references are consequently exact on BOTH full children. Conditional-occupancy KL, child-calibration KL and CE change are all zero. The queried singleton coefficient and its matched reference mass are both zero. Finally,

    I(parent)-mean I(children)=alpha_j=Inf_i(parent).

This is proved coefficientwise, without any approximation or entropy inequality.

## 2. Two different residuals

Let pi_v be physical fair-branch reach at a frontier F and J_F=sum_v pi_v I(v). Summing the last influence identity gives

    sum_{queried u} pi_u Inf_{i(u)}(u)=LJ-J_F.

All frontier terminal CE costs equal H, and every erasure cost is zero. If the supplied original capacity is A=K L J, the C019 entropy-payment residual is

    A - sum_u pi_u B_i(u) - sum_v pi_v CE(v)=K L J-H.

It is UNCHANGED by deferral. No entropy expense K Inf_i has occurred. If, instead, a continuation explicitly earmarks K Inf_i at each query to retain a rate measured against remaining influence, its residual is

    A - K sum_u pi_u Inf_i(u) - sum_v pi_v CE(v)
       =K J_F-H.

This second ledger is a stronger allocation rule. It must not be substituted silently for the first. At the complete unwrapping frontier ell_j=1, J_F=J, and the second residual is KJ-H. Every complete terminal is an input-sign translate of g, with identical entropy and influence. An arbitrary normalized replacement reference cannot improve on H, since CE(P,Q)=H(P)+D(P||Q)>=H(P). Orbit averaging is already at its CE minimum here. Thus a negative influence residual cannot be repaired by changing an exactly matched reference; the entropy-payment residual can still be nonnegative.

For a concrete distinction take g=Maj_3, L=2 and K=1. Its four nonzero squared coefficients are all 1/4, so H=2 and J=3/2. The six-bit matched root has I=3 and unused entropy capacity 3-2=1. Three legal block queries cost zero erasure and zero CE change, and leave the SAME entropy residual 1. Earmarking their total influence tariff 3/2 instead leaves the different residual -1/2. This refutes same-rate influence heredity at K=1, not FEI with an unspecified absolute constant.

## 3. Cheap matched roots do not imply cheap cores

For every fixed K>0 and nonconstant core, choose integer

    L >= max(2, ceil(n 2^(n-1)/K)).

Some physical edge changes sign, so one core coordinate has influence at least 2^(1-n). Hence J>=2^(1-n). The spectral law has at most 2^n atoms, so H<=n. Consequently the EXACT matched root is unconditionally priced:

    CE(root,P_root)=H<=n<=K L J.

This admission uses no FEI conjecture. It can require a very large lift and makes no claim of efficiency or bounded dimension. Constants have H=J=0 and need no division.

For a fixed K>0, the following universal endpoint assertion is EQUIVALENT to FEI(K): every such cheaply admitted exactly matched parity-expanded root can be fully unwrapped with nonnegative remaining-influence residual at the SAME K. FEI(K) suffices since J_F>=J and H<=KJ; necessity follows by applying the assertion to the cheap lift above, whose endpoint residual is exactly KJ-H. This exact-constant equivalence is the rate-compression obligation, not a FEI proof or a known counterexample.

More generally, if 0<=lambda<1 and a proposed transfer guarantees H<=KJ+lambda H at every such unwrapped endpoint, it is exactly equivalent to FEI(K/(1-lambda)). Necessity is algebra; sufficiency follows from that FEI constant. There is no 2/ln(2) loss here, because all erasure and Jensen-Shannon costs along these particular histories vanish.

## 4. Consequences for the minimal targets

A090's no-reset deferral is correct: no positive conversion is locally required on the matched isospectral sector. A085's arbitrary-core nullspace is also correct. The present addition separates an unchanged ORIGINAL entropy bank from an allowance newly expressed using CURRENT influence, and tracks the entire unwrapping frontier. An assumption that the latter is automatically paid would assume the desired FEI bound at its endpoint, even when the root was admitted without FEI.

For arbitrary active queries the existing diagram remains: FEI(C) => total erasure B<=CI => some B_i<=C Inf_i; a universal good-coordinate bound B_i<=K Inf_i implies FEI(K+2/ln2). The fractional bound B<=lambda H+K I implies FEI((K+2/ln2)/(1-lambda)). A low-influence version with max Inf_i<tau, and B_i<=(lambda H/I+K)Inf_i, implies FEI(max(log2(e/tau)+2/ln2,(K+2/ln2)/(1-lambda))). Signed-Booleanity downward fiber cost L_i satisfies L_i<=B_i<=L_i+Inf_i/ln2; some L_i<=K Inf_i implies FEI(K+3/ln2). The witness residual route still needs its full previously specified posterior KL bound and normalizers; this stage does not replace it with a marginal entropy statement.

No canonically smallest stronger lemma exists across these routes. At fixed quantitative targets the existing genuinely stronger candidates remain: in the weak-coordinate regime tau=1/4, find an i with Inf_i>=I/(2d) and B_i<=4Inf_i; or prove a signed coefficient condition ensuring L_i<=4Inf_i; or pay the previously fixed witness residual. The first unproved line is the corresponding all-dimensional inequality, not any of the arrows. The newly exposed matched-frontier compression condition is FEI-equivalent and therefore DOES NOT qualify as an independent stronger structural lemma.

## 5. Scope and novelty boundary

Parity lifting, zero-erasure deletion and arbitrary-core nullspaces are prior work (A085/B17) and are not claimed new. Exact-match deferral is A090's reviewed corollary and is not claimed new. A068 refutes arbitrary-source profile heredity and repairs a symmetric family; A066 pays an actually necessary nonempty handoff after a specified influence invoice. Neither is contradicted: the present source is already exact, and its two account conventions are displayed separately. The delta is the exact all-frontier influence residual and exact-constant FEI-hardness of compressing an unconditionally cheaply admitted matched lift back to the core's current-influence scale. Independent review of this delta is pending.

First unsupported universal line: obtain a dimension-independent O(I(g)) ORIGINAL entropy capacity for arbitrary cores, or prove a noncircular structural inequality that bounds H at the quotient frontier. Mere cost-free deferral, or reclassification of the old bank as K times current influence, supplies neither.
