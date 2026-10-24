# A087 restriction referee: independent reconstruction

## exact target, quantifiers, hypotheses and units

Audit the available versioned claims of A021-A030 and A061-A065 using actual uniform-cube Boolean children, physical history probabilities, fair conditional assignments, retained boundary entropy, and one influence budget. All Fourier transforms use normalized characters; all entropies, KL divergences, and logarithms are in bits. Verdicts below are acceptance at the stated scope, not universal FEI. Full FEI remains OPEN.

Eleven claims from A021, A022, A026, A027, A061, and A062 are independently accepted as stated. At the source snapshot, no completed claim artifacts from A023-A025, A028-A030, or A063-A065 were available. Absence is not acceptance or refutation; those nine packets remain pending intake. Their previously known obstruction controls remain valid at the recorded scope. This run supplies one additional source-complete bridge: equality of A061's logarithmic charge and A021's magnitude-mismatch KL residual along the balanced-core control-first tree.

## sources actually read, revisions and theorem locators

Protocol 2026-10-11-execution-v2 was read in full. README, current status, claim/obstruction registries, packet status, stream actions, and the plan were accessed, with A087's contract and related restriction contracts inspected. BOARD was read at stage start; its snapshot was 2026-10-11 22:05 UTC. B18/STREAM_NOTES.md was absent. No alternative lead instructions were inferred. New local A022, A027, and A062 artifacts superseded the board's stale stage-zero descriptions during intake.

Proof sources read and reconstructed:

- A021 run 20261011T214020Z-account05-A021-rare-core-asymptotics: REPORT Sections 1-5, RARE_CORE_EXPANSIONS.tex, both v1 claim statements.
- A022 run 20261011T215800Z-account05-A022-one-point-surgery: POINT_SURGERY.tex in full, SURGERY_LOG_CERTIFICATE.md and its single v1 claim.
- A026 run 20261011T214052Z-account05-A026-good-coordinate-erasure: GOOD_COORDINATE_TARGET.tex in full, REPORT, both v1 claims. The finite engine was independently rebuilt rather than imported.
- A027 run 20261011T215911Z-account05-A027-block-selection: ADAPTIVE_BLOCK_SELECTION.tex in full and both v1 claims.
- A061 run 20261011T214516Z-account05-A061-entropy-process: FAIR_TREE_ENTROPY_PROCESS.tex, REPORT Sections 1-5 and both v1 claims.
- A062 run 20261011T220423Z-account05-A062-influence-compensator: FAIR_TREE_INFLUENCE_PROCESS.tex in full, STOPPING_JUSTIFICATION.md and both v1 claims.

Recovered sources: ERASURE_REDUCTION Sections 1-6; BLOCK_RESTRICTION_IDENTITY Sections 1-3; ROUTE_MAP_CURATED Sections 1-2.1; supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING. The earlier B05 rare-restriction no-go and B19 independent review were inspected and are not reopened. The earlier B09 report was inventoried and scoped, but none of its unreviewed inequalities is a proof dependency.

Threshold 38-page text: Proposition 8.9 and Corollary 8.10, lines 2550-2622, and its composition/restriction statement map. The 29-page earlier text's introduction and definitions were inspected and not substituted for the current constant. Percolation 30-page text: introduction and Theorems 3.1-3.2, especially the distinction between pivotal entropy and spectral entropy. The 31-page alternate introduction and Theorems 1.1-1.2 were inspected. Geometry-specific percolation results are not used in any acceptance. All four complete text files were byte-read for hashes; this is not a claim of auditing every theorem in those papers. Source bytes/hashes and read limitations are recorded in out/source_inventory.json and out/live_intake.json.

## complete derivation or exact first unsupported line

### Physical blocks and the conserved budget

Partition the current physical coordinates into queried U and remaining V. Write a_(R,T) for the actual Fourier coefficients with R subset U and T subset V. For a fair physical assignment z to U, the child coefficient is

    childhat_z(T)=sum_R a_(R,T) chi_R(z).

Each squared child spectrum p_z is a probability law because the child is Boolean. Partial Parseval gives q_T=E_z p_z(T)=sum_R a_(R,T)^2, the V-marginal of the parent spectrum. Therefore

    D_U=H(f)-E_z H(f_z)=H(S_U|S_V)+I(Z;T),
    I(f)=I_U(f)+E_z I(f_z).

Here Z is sampled uniformly first and T conditionally from p_Z in a one-node channel. Its posterior Z given T is generally not uniform. That posterior must not replace the physical averaging law in the second identity or in a restriction tree. For a two-control activation of a dictator, the two child empty spectral probabilities are 1 and 1/4. Conditioned on the empty packet, the constant child's probability is 4/5, while its physical probability is 1/2. The physical average child entropy is 1 bit; incorrectly using those empty-packet posterior weights gives 2/5 bit. This is an illustrative false substitution, not an error found in an audited claim.

For each original label j not yet queried, reveals of other labels preserve its conditional expected influence by edge averaging. Querying j removes precisely its current influence and replaces it by that query cost. Thus each label separately conserves expected queried cost plus terminal influence. Summing labels gives the total identity above. It does not give a pathwise decreasing wallet: activated two-bit parity has root influence 3/2 and an active child of influence 2. Summing all node influences rather than queried influences reuses budget; a full three-bit parity chain has sum of node influences 3+2+1=6 but total queried influence 3.

At each reached node the selected fresh block is measurable from the independent policy seed and observed history. Unobserved signs remain independent and fair, so the physical child probabilities are 2^(-|U|). Finite summation, including the predictable stopping indicator, gives

    H(f)=E sum D_v + E H(leaf),
    I(f)=E sum I_(U_v)(f_v) + E I(leaf).

The same tree and the same physical history weights must be used in both. This reconstructs A061-FAIR-TREE-PROCESS v1 and A062-INFLUENCE-STOPPING-INTERFACE v1, including the labelled extension. Independent randomization is handled by conditioning on its seed; averaging afterward changes neither identity.

For one fixed finite dimension, there are at most n fresh reveals even with unbounded waiting. Residual H and I are at most n, and accumulated nonnegative entropy decrements are at most n^2. Bounded convergence therefore justifies passage from finite truncation to the eventual restriction. Across dimensions these bounds are not uniform. In the abstract unbounded extension, nonnegative cumulative costs converge in L1 by monotone convergence and the initial budget. Residual influence is a nonnegative supermartingale. Fatou gives only E cost+E limiting residual <= initial influence; uniform integrability of residual influence gives equality. Entropy needs its own uniform-integrability assumption and limit identification. Those assumptions are explicitly retained by A062.

### A061 logarithmic compensation and scalar boundaries

For a coordinate use actual parent coefficients a_T,b_T, q_T=a_T^2+b_T^2, theta=b_T^2/q_T. The erasure is B=sum q h2(theta), the child-channel information is JS, and the queried influence is d=sum b_T^2. Let lambda=sum b_T^2 log(q_T/b_T^2).

The inequality -(1-theta)ln(1-theta)<=theta proves B<=lambda+d/ln2, including theta=0,1 by continuity. For z=2|ab|/q, set dnat(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2. The derivative difference between z/sqrt(1-z^2) and atanh(z) has derivative (1-z^2)^(-3/2)-(1-z^2)^(-1)>=0 and starts at zero. Integration gives dnat(z)<=1-sqrt(1-z^2). The JS packet is consequently at most 2min(a^2,b^2)/ln2, hence JS<=2d/ln2.

Thus D<=lambda+3d/ln2. The conditional drift of (3/ln2)I-H-sum previously charged lambda is D-3d/ln2-lambda<=0: it is a supermartingale, with the sign exactly as A061 states. If every positive theta>=epsilon, lambda<=log(1/epsilon)d and CI-H is a supermartingale with C=log(1/epsilon)+3/ln2. Stopping yields H(root)<=CI(root)+E[H(leaf)-CI(leaf)], retaining the terminal defect. Zero b packets are exempt and theta=1 contributes zero lambda. At fixed n every positive squared coefficient is at least 2^(-2n), giving integrability. Verdict: A061-LOG-COMPENSATION v1 accepted without alteration.

### A021 rare-core identity, remainder and the cross-ledger equality

Let g be balanced, q=2^(-k), and F=1+A_k(g-1). Its Fourier probabilities are (1-q)^2 at the empty set; q^2 at each nonempty pure-control set; and q^2 ghat(T)^2 at every nonempty data set T and every control set. The three total masses are (1-q)^2, q-q^2, q. Hence

    H(F)=qH(g)+(4q-2q^2)k-2(1-q)^2 log(1-q),
    I(F)=qI(g)+kq.

Direct edge counting gives each queried control influence q, and each data influence q times its core influence. For a disjoint t-fold balanced core, H(g)=tH(b), I(g)=tI(b). Multiplying the convergent -ln(1-q) series by 2(1-q)^2 gives 2cq-3cq^2-4c sum_(j>=3) q^j/[j(j-1)(j-2)], c=1/ln2. Bounding each tail coefficient by 1/6 yields the claimed remainder interval [-2cq^3/(3(1-q)),0], uniformly in the tensor count and seed. The ratio limits follow by dividing by q(tI(b)+k); balanced I(b)>=1 prevents degeneracy. An unbalanced seed is balanced by a fresh sign, adding one influence and no entropy. Verdict: A021-UNIFORM-RARE-CORE-EXPANSION v1 accepted.

At the active node with s controls left, put u=2^(-s). Its children are constant 1 and 1+A_(s-1)(g-1). The empty packet has Q0=1-2u+2u^2 and magnitude mismatch m0=u^2. Every other packet has one zero child coefficient, so m_T=Q_T/2; total mismatch is u. Importantly, the active child's constant coefficient 1-2u is nonnegative, including the boundary s=1. Thus signed and magnitude mismatch agree in this family. Equivalently the parent queried sector has b_T^2=m_T in every packet. It follows that A061's one-sided lambda equals A021's KL residual exactly:

    lambda_s=sum m_T log(Q_T/m_T)
             =u-u^2+u^2 log(Q0/u^2)
             =u[log(1/u)-D2(m/u || Q)].

The physical reach probability is q/u. Summing gives sum w lambda=q(k+A_k), with A_k=sum_(s<=k)2^(-s)[2s-1+log Q0]. For s=1 this summand is zero. For s>=2, 1/2<=Q0<=1, hence each bracket lies between 2s-2 and 2s-1. Therefore 0<=A_k increases to A<=3 and its tail is at most sum_(s>k)(2s-1)2^(-s)=(2k+3)2^(-k). The charged controls cost kq, terminal influence qI(g), and terminal entropy qH(g). The blind scalar rarity cost is q sum_(s<=k)s=qk(k+1)/2. The KL credit, not an extra influence allocation, removes that quadratic cost. Verdict: A021-CONTROL-FIRST-KL-LEDGER v1 accepted. The additional lambda equality is our new scoped bridge, proved without changing either source claim.

The ancillary expansions were also checked analytically: |log Q0|<=4cu for s>=2 gives the residual error bound 4cu^3. Expanding the remaining binary entropy gives the stated 5cu^3 packet-entropy bound. For the true decrement the residual difference R(u)-R(2u)/2 is nonnegative and at most 8cu^3/[3(1-2u)], giving the reported boundary-safe bound. The s=1 node uses its exact formulas rather than those expansions.

### A022 signed surgery and fixed-seed classification

For an actual flip set D, Fourier linearity gives half-difference t_S=2^(-n)sum_(v in D) f(v)chi_S(v), midpoint a_S-t_S, and selector probabilities t_S^2 and (a_S-t_S)^2. Parseval of f1_D gives sum t_S^2=|D|2^(-n)=mu. Expanding binary entropy gives L=J+R with J=sum e log(q/e)=mu[log(1/mu)-D2(e/mu||q)] and 0<=R<=mu/ln2. Zero mismatch and zero packets are handled by continuity.

For one point, e=delta^2 on every label and the normalized signed ratio r=a/(delta f(v)chi_S(v)) is an even integer whenever n>=1. Hence |r-1|>=1 and the signed mismatch equals the minority packet mass. Flipping an edge endpoint changes its influence by 2delta f(v)f(v^i). For adjacent flips, the half-difference contains 1+epsilon(-1)^(j in S); its square is 2delta^2[1+epsilon(-1)^(j in S)]. Only one Fourier half-cube is active and the shared physical edge does not change status. Original-table one-point changes require the -4delta f(v)f(v^j) interaction correction. Opposite constant children show why signed and magnitude mismatch must not generally be identified for adjacent flips.

Define Phi(r)=((r-1)^2+1)h2(1/((r-1)^2+1)). For |r|>=2, B=1-2/r+2/r^2>=1/2 gives |ln B|<=6/|r|. Also (A-1)ln(1+1/(A-1)) lies in [1-1/(2(A-1)),1], where A=(r-1)^2+1 and A-1>=r^2/4. Thus |Phi(r)-2log|r|-c|<=7/(ln2|r|)<12/|r|. All nonzero integer Walsh sums on an m>=1 cube have absolute value at least two. In a t-fold tensor, the occupied fraction is rho^t, every occupied |r|>=2^t, and the uniform-on-occupied mean log|r| is t lambda. On zero labels Phi(0)=2. Averaging proves the claimed 12(rho/2)^t error and the fixed-seed dichotomy. Sign multiplicities for a bent source follow from inversion at the flipped vertex; restricting to the active adjacent half-cube and inversion at both endpoints gives its stated multiplicities. Character padding multiplies support sparsity and integer coefficient sizes exactly as claimed. Verdict: A022-SIGNED-SURGERY-TENSOR-LOG-LEDGER v1 accepted. The asymptotic theorem is reconstructed analytically; its author's logarithm interval implementation is not independently certified by this run.

### A026 affine support and finite physical selection

For p in [0,1], h2(p)<=2sqrt(p(1-p)): the derivative after t=sqrt((1-p)/p) substitution is t-1/t-2ln(t)/ln2. Its derivative has one turning point for t>1, giving the necessary single sign change and nonnegative difference with zeros at p=0,1/2. Multiplying packetwise proves B_i<=A_i=2sum|a_T a_(T+i)|.

Our direct character-sum enumeration of all tables modulo global output sign gives exact maxima of min_(relevant i) A_i/I_i equal to 0,2,3,7/2 at n=1,2,3,4. The integer selection inequality is 4sum|W_T W_(T+i)|<=7sum W_(T+i)^2 with a positive denominator. No logarithm comparison is used.

If support lies in c+V and a relevant physical e_i is outside V, adjacent support pairs are absent, so B_i=A_i=0. The children have equal squared spectra and JS=0. If every relevant e_i lies in V, their independence implies at most dim V<=4 relevant variables. Thus finite selection applies. Physical restriction projects c+V, preserving the dimension bound. Disjoint factors give independent spectral laws, preserving factor B_i and I_i and their restriction classes. Induct with D_i<=B_i+2I_i/ln2 and exact influence conservation to get H<=(7/2+2/ln2)I. This uses physical coordinates throughout, not arbitrary Fourier linear reparametrization. Verdict: A026-AFFINE4-GOOD-COORDINATE v1 accepted.

For the second claim we independently evaluate integer Walsh sums on each level j by counting the z selected negative bits:

    W_j=sum_(w=0..32) sign(w>=24) sum_z (-1)^z binom(j,z)binom(32-j,w-z).

Then A_i/I_i=2sum_j binom(31,j)|W_jW_(j+1)| / sum_j binom(31,j)W_(j+1)^2 =2220940451/536870912>4. Its denominator independently agrees with the direct pivotal probability binom(31,23)/2^31. Permutation symmetry covers every coordinate. This refutes only K=4 amplitude-proxy selection, not true erasure selection or FEI. Verdict: A026-AMPLITUDE-K4-THRESHOLD-NOGO v1 accepted.

### A027 the proper data block and its FEI-strength boundary

For arbitrary core u on m bits let mu=Eu, d=1-mu, v=1-mu^2, p=2^(-r). The proper block W is all core variables. For every nonempty control Fourier set the fiber mass is 2p^2d and its normalized law is the squared spectrum of u-1, of entropy at most m. The empty-control fiber has R0=1-2pd+2p^2d and nonempty-core mass p^2v. Its entropy is R0 h2(p^2v/R0)+p^2vL, where L is the normalized nonempty core entropy. These are coherent actual fibers, including the shifted constant coefficient.

The nonempty fibers plus the L term are at most 2pdm since v<=2d. The remaining binary term is at most p^2[2rv+vlog(1/v)+cv]<2p: use v<=1, max v log(1/v)=1/(e ln2), rp<=1/2, p<=1/2 and (1+1/e)/ln2<2. The latter follows from ln2>=56/81 and e>8/3. Thus B_W<=p(2dm+2)<=6pm. Query cost is pI(u); terminal influence rpd comes from negative core assignments, each of probability d/2, with point-defect influence 2rp. Those leaves have H<=4I: their entropy is the constant-atom entropy plus 8p(1-p)(r-1), bounded by 4p/ln2+8p(r-1)<=8rp. The r=1 case has zero entropy. The recovered block-channel estimate J_W<=2I_W/ln2 follows from the cube two-point entropy inequality applied to absolute child amplitudes, tensorized in W; its complete proof was inspected in BLOCK_RESTRICTION_IDENTITY Section 2. This gives max(6/eta+2/ln2,4) when I(u)>=eta m. No hereditary density assumption is smuggled into this one-step theorem. Verdict: A027-DATA-FIRST-PROPER-BLOCK v1 accepted.

Put delta=d/2. The squared spectrum of u-1 has empty mass delta and nonempty mass 1-delta. Summing the same fibers exactly gives

    B_W/p=vL+4delta(1-p)h2(delta)+(R0/p)h2(p^2v/R0).

The last term tends to zero as p->0 for a fixed core. For mu>=0, edge isoperimetry gives I(u)>=2delta log(1/delta). When delta<=1/4, h2(v)<=vlog(e/v)<=4delta log(e/(4delta))<=2I(u); when delta in [1/4,1/2], the concavity chord gives I(u)>=1 and h2(v)<=1. The source's isoperimetric induction is valid: within-half boundaries plus at least the difference of half-set sizes reduce exactly to h2(a/(a+b))>=2a/(a+b). Consequently a universal block bound with K implies H(u)<=KI(u)+h2(v)<= (K+2)I(u); complementing extends it to negative means. Conversely Parseval gives v<=I(u), the exceptional row contributes <=3I(u), and 4delta h2(delta)<=2I(u). Hence B_W/p<=H(u)+5I(u), proving the C+5 implication. Verdict: A027-CORE-BLOCK-HARDNESS v1 accepted. Properness of this block does not make its unrestricted payment easier than FEI.

### A062 dimension-limit obstruction

The quadratic two-bit sign has four probabilities 1/4, entropy 2 and influence 1. Balance the product of 2^(k-1) such independent factors with a fresh sign. Then H(g_k)=2^k and I(g_k)=2^(k-1)+1. Activate with k fresh controls. A021's directly reconstructed spectrum gives root influence 1/2+(k+1)2^(-k)<=3/2. Under control-first stopping, terminal influence is (2^(k-1)+1)1_(A_k) and entropy is 2^k 1_(A_k). On coupled infinite fair controls they tend to zero almost surely because the first negative control occurs at finite time almost surely, but expectations are 1/2+2^(-k) and 1. Tail masses therefore stay positive for arbitrary cutoffs: uniform integrability fails. This is a family across increasing dimensions, not an optional-stopping failure on any one fixed cube. Verdict: A062-BOOLEAN-DIMENSION-LIMIT-OBSTRUCTION v1 accepted.

### Exact first unsupported universal line

Neither the stopped identities nor these acceptances establish a policy on every Boolean function with dimension-free paid erasure/logarithmic cost and paid terminal entropy. A021's terminal qH(g) preserves arbitrary core difficulty; A027 proves its unrestricted core-block payment equivalent to FEI; A062 forbids disposing of that difficulty through almost-sure terminal limits alone. A026's hereditary affine-dimension hypothesis and A061's fixed density hypothesis cannot be deleted. The missing universal line remains: construct a realizable stopping tree or debt satisfying D_v<=C d_v+Q_v-E[Q_child|history], with root and terminal debt both paid from the same physical influence reserve.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the initial combined pilot. That pilot stopped at its 55-second guard with no final output; no mathematical acceptance relies on its unpersisted execution. SPEC_REVISION.md records the sequential split of the unchanged domain and a count correction in EXTRA_SPEC.json (68 adjacent surgeries rather than the mistaken 36; no domain change).

From A087 run:

    python -X utf8 runs\20261011T221055Z-account05-A087-restriction-referee\code\check.py identity
    python -X utf8 runs\20261011T221055Z-account05-A087-restriction-referee\code\check.py selection
    python -X utf8 runs\20261011T221055Z-account05-A087-restriction-referee\code\check.py activation
    python -X utf8 runs\20261011T221055Z-account05-A087-restriction-referee\code\extras.py

All saved phases PASS. Identity: 37,151 assertions, 278 functions, 3,252 block checks including adaptive rechecks, 556 trees, 184 nonzero-entropy terminal trees; 17.9805 seconds. Selection: 32,909 assertions on 32,906 sign-reduced tables; 1.9499 seconds. Activation: 1,035 assertions on 48 functions and 120 active nodes; 0.3146 seconds. Extras: 3,692 assertions, 72 point and 68 adjacent surgeries, 48 arbitrary-bias core activations, 2,336 labelled survival checks, 10 exact terminal-family parameters; 0.2042 seconds. Total counted assertions: 74,787; the library import additionally repeats three already checked threshold assertions and is excluded from that total.

The checker uses direct character matrices, integer Walsh sums, Fraction arithmetic, and rational coefficient vectors of prime logarithms. Entropy comparisons are exact identities of the same expanded logarithmic terms; they do not rely on unproved linear independence of logarithms. Selection and the 32-bit threshold witness use integer inequalities. All infinite-parameter remainder bounds and limit claims rest on the reconstructed analytic proofs above. Finite tests are independent implementation checks, not finite-to-infinite proofs. No heavy job, GPU, window, subprocess surviving its command, automatic n increase, or modification outside A087 occurred.

## proof dependencies and changed downstream conclusions

Accepted source versions retain their authors and hypotheses. CLAIMS.json copies each exact source statement and records this independent reconstruction as review evidence; shared ledgers and source claims were not modified. The new A087 equality depends only on the directly proved balanced activation spectrum and finite probability, and contributes no repair to any accepted claim. A094 remains the independent challenger for wider chains.

Persistence audit found eight metadata discrepancies: both A021, both A026, both A061 and both A062 recorded statement hashes differ from SHA256 of their exact_statement UTF-8 text. A source hash convention was not specified, so this is not asserted to be corruption. out/live_intake.json preserves recorded and computed values and pins the source files by byte hashes. The local CLAIMS.json copies use the computed UTF-8 statement hash, with each original recorded value preserved in the review record. The exact statements and mathematical verdicts are unchanged. B20 should normalize or document the convention before relying on those hash fields for automated dependency matching.

Downstream A023/A064 can substitute the complete KL residual for the one-sided logarithmic charge on the actual balanced control-first family, paying <=4 times queried control influence and retaining qH(g). A028/A029 receive a conserved physical block/label ledger. A027's unrestricted all-core block is now independently confirmed FEI-strength, preventing an apparent shortcut. A062's terminal tail guard is independently accepted and must be retained in all dimension-limit handoffs. Nine unavailable packets remain pending intake rather than being silently closed.

## one next mathematical action and independent reviewer

Next: reconstruct a proposed A023/A064 transport on the accepted sparse-bent point-surgery selector-first and control-first descendants, track per-label reserve, and demand a paid terminal boundary. For its selector, use A022's actual signed surgery coefficients and check where they equal magnitude minority before importing KL debt. Independent reviewer: A094. B20 may adopt these source-bound review records after verifying persistence.

## actual persistence receipts or precise save blocker

All artifacts are inside the assigned A087 run: report, claims, canonical progress and identical packet delta, frozen specs, independent scripts, exact outputs, source inventory and live intake. The rolling STATUS, WORKLOG and LEARNED files are local. out/persistence_receipts.json records final file hashes and sizes; out/schema_validation.json checks exact protocol field sets and byte-equal progress copies. No git, mail, brain write, other-agent write, upload or shared-index mutation was performed. Supervisor copy, mirror verification, downstream use and public release are not claimed.

### Universal bridge

This stage advances C019 stopping-tree payment by independently validating eleven source claims, the physical block and per-label budget, the retained terminal boundary, and the exact equality between two previously separate logarithmic ledgers on balanced-core activations. It does not advance the universal constant numerically: arbitrary core entropy and general selector surgery transport remain unpaid. C018's physical selection reduction is validated on the stated affine-support class, while A027's hardness guard blocks a false generalization. The shortest next route to full FEI is an explicit nonreusing transport for the known sparse-bent surgery descendants with paid root and leaf debt, because that attacks the live universal payment obstruction rather than adding another isolated class.
