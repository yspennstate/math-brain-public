# A019: exact low-energy collision payment for rare input translations

Run: 20261011T223425Z-account05-A019-orthogonality-extensions. Stream B04; packet A019. Full FEI remains OPEN. This is a narrow structural extension of the existing collision interface, with a complete analytic proof and exact author validation; independent review of the extension is pending. No literature priority claim is made.

## exact target, quantifiers, hypotheses and units

Identify the uniform sign cube with F_2 coordinates, with characters chi_T(y)=(-1)^(T dot y). Let n>=0, r>=0, g:F_2^n->{-1,1} be arbitrary. For each j=1,...,r choose a positive integer k_j, a vector v_j in F_2^n, a point z_j in F_2^(k_j), and a fresh selector block W_j of k_j coordinates. The W_j are pairwise disjoint and independent of y. Translation vectors may coincide, overlap, or be linearly dependent; g need not be balanced, quadratic, or have disjoint Fourier supports. Define

A_j(w_j)=1{w_j=z_j}, tau(w)=sum_j v_j A_j(w_j), F(w,y)=g(y+tau(w)).

All sums in input arguments are mod two. Put p_T=hat(g)(T)^2, delta_j=2^(-k_j), rho_j=Pr_y[g(y)!=g(y+v_j)]=sum_{T:T dot v_j=1}p_T, and a=sum_j k_j. Entropies are in bits, influence is physical edge disagreement. Write E_k for the Fourier entropy of h_k(w)=1-2*1{w=z} on k bits:

E_k=-(1-2delta)^2 log2((1-2delta)^2)+4delta(1-delta)(2k-2), delta=2^(-k),

with 0 log 0=0. The exact conclusion is

H(F)=H(g)+sum_j rho_j E_(k_j),
I_data(F)=I(g), I_W(F)=sum_j rho_j (2 k_j delta_j),
Inf_i(F)=2 delta_j rho_j for each selector i in W_j,
M_W=0, B_W=Delta_W H=sum_j rho_j E_(k_j)<=4 I_W(F).

Consequently a certified H(g)<=C I(g) transfers to H(F)<=max{C,4} I(F). No theorem about arbitrary g's entropy is assumed or concluded. A one-block dictator core with rho=1 has I_W/a=2^(1-k)->0 and B_W/I_W=E_k/(2k2^(-k))->4. Thus 4 is the optimal uniform collision constant for this translation family, even in the low-disagreement regime. This is not an application of a uniform positive neighboring-disagreement bound.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision 2026-10-11-execution-v2. Campaign README, CURRENT_STATUS (snapshot 20:06:24Z), CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS, and FEI_100_agent_research_plan.tex were consulted; the specific A019 contract requires an exact low-energy payment and the bent-splice test. BOARD.md at stage start is dated 22:37 UTC and gives A018's common-spectrum phase handoff. claude/B04/STREAM_NOTES.md was absent at stage start; no lead instruction is overridden.

Threshold 38-page text: Proposition 8.6, equations (75)-(79), and Corollaries 8.7-8.8 are the collision and positive-energy baseline, already proved. Its Section 8.3 arbitrary-selector reduction prevents calling a retained arbitrary core a solved FEI leaf. The threshold 29-page version and both percolation texts were consulted for definitions, introductions, scope and composition context. The percolation versions differ in their overlap conclusion; no percolation theorem is a dependency here, and a complete independent audit of either paper is not claimed. The extracted text has non-UTF-8 bytes; relevant readback used replacement decoding, while hashes refer to original bytes.

Supplement CAMPAIGN.md, CLAIMS.md, COUNTEREXAMPLES.md (especially X005,X007,X009,X011), SEED_LEMMAS.md, NATIVE_MAPPING.md and sources were consulted. sources/ISOSPECTRAL_SPLICING_CURATED.md Sections 4-5 establishes the existing one-bit cancellation and linear signed-translation quotient. Its pinned original is fe94de760ee2b47545419a7447b492816bd16045, blob 3421c0cbfd22031554befb962ec92cd0c8bb45b9. The present conjunction translations are nonlinear for k>=2 and their collision entropy is generally positive, so they are not that zero-cost quotient. sources/OVERLAPPING_PRODUCT_NOTE.md supplies the shared-product guard: only disjoint selector blocks justify the product-spectrum step below.

A018 run 20261011T221538Z-account05-A018-shared-data-collision-law, REPORT sections 1-5 and claim A018-COLLISION-BLOCK-INTERFACE v1 were read in full. Its proposed quadratic/common-spectrum direction led to the more sparse conjunction construction here. A017's quadratic rank result is retained as already completed work, not rederived as a new result. A016 run 20261011T213934Z-account05-A016-addressing-benchmark REPORT was read for addressing calibration. Earlier B19 run 20261011T195038Z independently reconstructs B05's sparse activated bent no-go; its analytic sections 2-4 were read. The earlier B05/B09 locations were inspected, but their full reports/checkers were not replayed and none is a positive premise.

out/SOURCE_RECEIPTS.json records source byte hashes. Hash/read receipts do not imply an independent audit. REVIEW_DEPENDENCIES.md records a substantive analytic reconstruction of A018's interface, separately from new author checks. B04 already has pending baselines; this run opens one narrow bundled structural extension, not a new broad universal candidate. Registry adoption and review-queue reconciliation belong to B20.

## complete derivation or exact first unsupported line

### 1. General disjoint-module translation identity

The useful algebra works for arbitrary Boolean activation functions A_j on disjoint W_j. Put h_j=(-1)^A_j. Fix w; a change of variable y'=y+tau(w) gives

hat(g(.+tau(w)))(T)=hat(g)(T)(-1)^(T dot tau(w))
=hat(g)(T) product_{j:T dot v_j=1} h_j(w_j).

All branches have the same squared spectrum p, including the empty Fourier row. Therefore R_T=p_T, r_T is uniform on all 2^a branch labels whenever p_T>0, and M_W=0. For each positive-mass T the selector phase is an actual Boolean function

h_T(w)=product_{j:T dot v_j=1} h_j(w_j).

Because those factors depend on disjoint physical blocks, its Fourier spectrum is their tensor product, with unused blocks carrying the empty Fourier atom. Thus

H(h_T)=sum_{j:T dot v_j=1} H(h_j),
I(h_T)=sum_{j:T dot v_j=1} I(h_j).

Equivalently, the exact parent coefficient is hat(g)(T) times the product of the selected module Fourier coefficients, and is zero if an unselected module has a nonempty selector frequency. Conditional on T, squared selector coefficients are precisely that normalized product distribution. Zero p_T rows are omitted, not assigned artificial conditional laws. Hence directly by the entropy chain rule and mean cardinality,

H(F)=H(g)+sum_j rho_j H(h_j),
I_W(F)=sum_j rho_j I(h_j), I_data(F)=I(g),
B_W=sum_j rho_j H(h_j), M_W=0.

Parseval gives the stated equality between rho_j and physical translation disagreement: E[g(y)g(y+v_j)]=sum_T p_T(-1)^(T dot v_j)=1-2rho_j. Flipping selector i in module j changes tau by v_j exactly when A_j changes. Conditional on every w, y+tau(w) is still uniform. This proves the finer identity

Inf_i(F)=rho_j Inf_i(h_j).

Coincident v_j do not cause unaccounted coefficient collisions: a fixed T selects physical tensor factors on labeled disjoint W_j. It is the physical disjointness of W_j, not any linear independence of v_j, that is used.

### 2. Rare-point module spectrum and constant 4

For h_k=1-2*1{w=z}, the empty coefficient is 1-2delta; every nonempty coefficient is -2delta chi_A(z). Their squared masses are t=(1-2delta)^2 and 4delta^2 repeated 2^k-1 times. Their sum is one. This yields E_k above, including k=1, where h_k is a character and E_1=0. Each physical coordinate is pivotal at two directed endpoints of one edge, so Inf_i(h_k)=2delta and I(h_k)=2kdelta.

For 0<=t<=1, -t ln t<=1-t, with the endpoints interpreted continuously. Here 1-t=4delta(1-delta). Therefore

E_k/(2kdelta)
<= (1-delta)[4-(4-2/ln 2)/k] <4.

The strict final inequality follows from ln 2>1/2 and k>=1. The first inequality is valid also at t=0. This is a complete analytic all-k bound; finite parameter checks are not the dimension bridge.

For k>=2, delta<=1/4 and t=1-u with u=4delta(1-delta). A useful explicit expansion bound is

0<=u+(1-u)ln(1-u)<=u^2/(2(1-u)).

Indeed the left side is sum_{l>=2}u^l/[l(l-1)], so its coefficients are positive and at most 1/2. Consequently

0<=4delta/ln2-[-t log2 t]
<= [4delta^2+u^2/(2(1-u))]/ln2.

After dividing the exact E_k by 2kdelta this proves, with a bounded remainder,

E_k/(2kdelta)=4-(4-2/ln2)/k+O(delta),

and in particular convergence to 4. No unsupported exchange of n, r, k or core parameters is needed; the exact weighted identities hold simultaneously for all of them. If I_W>0, B_W/I_W is the weighted average of E_(k_j)/(2k_j delta_j), with weights rho_j 2k_j delta_j/I_W. For I_W=0 the exact debt is zero.

### 3. Unbounded low-disagreement and depth regimes

Take n=1, g(y)=(-1)^y, r=1, v=1. Then F=(-1)^(y+A_k(w)), all 2^k selector labels choose between g and its sign flip, and every selector coordinate has disagreement 2^(1-k). These branches share every data Fourier index. The selector entropy increment divided by selector influence tends to 4, whereas I_W/a tends to zero. This is an actual Boolean family, not an arbitrary amplitude relaxation.

For unbounded module count, take any r, all k_j=K and v_j=1 with the same dictator core. Then I_W/a=2^(1-K), B_W/I_W=E_K/(2K2^(-K)); there is no arity loss and repeated translations are allowed.

For unbounded nesting depth, start with a certified core g_0. At step l, use fresh disjoint rare-point selector modules to translate arbitrary coordinates of the preceding entire data function g_(l-1), including its old selectors if desired. For each step H(g_l)<=H(g_(l-1))+4 I_new and I(g_l)=I(g_(l-1))+I_new. Telescoping yields

H(g_L)<=H(g_0)+4[I(g_L)-I(g_0)].

Hence the same max{C,4} constant holds at all finite depths. This allows sharing all old data coordinates across branches but requires fresh physical selector coordinates at each step. It is not a result for selectors reused as current data without this independence. No positive lower bound on disagreement is used.

### 4. Proper-block stopping certificate and singleton guard

One can query each entire W_j as a block. At every branch the queried translation merely shifts the remaining core, so its squared spectrum and all rho_l stay the same. Eliminating W_j decreases entropy by rho_j E_(k_j) and influence by rho_j 2k_j delta_j. The terminal function is a translate of g; it has entropy H(g) and influence I(g). Thus this is a finite physical block tree with

sum_v pi_v B_(W_v)<=4 sum_v pi_v I_(W_v), sum_v pi_v M_(W_v)=0,

and the complete terminal cost retained. For n>=1, querying all remaining selectors is itself a proper block; alternatively individual complete modules are proper except a degenerate no-data situation where the function is constant. This is a C019 certificate on the class, with no reused physical influence.

The constant 4 must not be applied to every singleton query. For g a dictator and one three-bit module, H(F)=E_3, the two singleton children have entropies 0 and E_2=2, and Inf_i(F)=1/4. Therefore Delta_i H/Inf_i=4(E_3-1)>4. Exactly E_3=4-(9/8)log2 3>2 since 3^9<2^16. The full three-bit block still obeys B_W<=4 I_W. This guard shows why the block certificate is the correct payment granularity.

### 5. Imported bent-splice falsifier

Let m>=2 be even, delta=2^(-m), b(y)=(-1)^(y_1 y_2+...+y_(m-1)y_m), b'=b-2*1{y=0}. A one-bit selector between b and b' has I_sel=delta. The two-bit product transform gives c_T=hat(b)(T)=+/-sqrt(delta). Parent coefficients on the two selector sectors are c_T-delta and delta, so R_T=(c_T-delta)^2+delta^2 and minority-sector mass e_T=delta^2. Since sqrt(delta)<=1/2,

R_T/e_T>=1/(2delta).

The elementary h2(x)>=x log2(1/x) gives B_sel>=sum_T e_T log2(R_T/e_T)>=delta(m-1). Thus B_sel/I_sel>=m-1. M_sel is nonnegative, so the entire increment has the same divergent lower bound. This is the source-credited inherited falsifier, not a new discovery.

The present structural hypothesis excludes this family at an exact line: branch magnitudes must be identical. Here hat(b')(T)=c_T-2delta and its squared magnitude equals c_T^2 only if c_T=delta, impossible for 0<delta<1 and c_T=+/-sqrt(delta). An input translation cannot implement this point surgery. In contrast, rare translations can have small physical disagreement while preserving every magnitude. Common magnitudes alone remain insufficient for a universal constant, because branches h(w)(-1)^y encode arbitrary Boolean h; our disjoint point-module factorization supplies the additional paid structure.

### 6. First unproved universal line

There is no unproved line in the stated translation-class theorem. The universal extension is not proved: an arbitrary Boolean function need not admit a proper-block restriction tree whose selector coefficient rows factor into these disjoint rare-point phases and whose remaining terminal entropy is already certified. Allowing arbitrary row phases would recover the full FEI problem. Allowing overlapping selector modules invalidates the product-law proof and requires a new collision calculation. The singleton guard also prevents silently refining the block certificate at the same constant.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was written before enumeration by helper A019-translation-v1. Domain: all 16 two-bit Boolean cores, one selector module k=1,2,3 and all four vectors v; two modules with block sizes (1,1),(1,2),(2,2) and all 16 ordered vector pairs. No symmetry quotient, randomness, dimension escalation, GPU or heavy job. Total 960 actual Boolean cases. Additional closed-form spectrum/bound checks use k=1,...,100, and actual bent-splice truth tables m=2,4,6,8. Memory estimate 40 MB; peak memory was not instrumented. No >300 MB job was planned, so memok preflight was inapplicable.

Command from A019:

`python -X utf8 runs/20261011T223425Z-account05-A019-orthogonality-extensions/code/check_translation.py`

Integer FWHT and Fraction probabilities checked every data marginal and selector physical influence against the closed forms. Entropy identities were checked exactly as finite rational linear combinations of log2(prime), not floating subtraction. An 80-term positive rational atanh expansion with geometric tail enclosed ln 2, certified ln2>1/2, and outwardly bounded the analytic ratio upper estimate at all 100 specified k. The singleton obstruction uses the exact integer inequality 3^9<2^16. No finite numerical entropy sign is treated as a proof. out/CHECK.json contains counts, rational endpoints, bent guard, observed runtime and script hash. Initial pilot: PASS, 960 cases, 12,649 assertions, 0.544 seconds. Final guard-inclusive check: PASS, 960 cases, 12,650 assertions, 1.065 seconds, recorded in out/CHECK.json. The all-dimensional theorem is supplied by the analytic argument above.

## proof dependencies and changed downstream conclusions

Baseline source: threshold Proposition 8.6 / C035; the coefficient derivation here is also self-contained. The point-defect module spectrum is inherited elementary input (also used in SEED_LEMMAS's fixed-Renyi obstruction), not advertised as new. The new mathematical use is its exact rho-weighted debt for arbitrary shared cores and arbitrary repeated translation vectors, a sharp low-selector-energy closure and a complete physical block certificate. No pending theorem about weighted biased thresholds, arbitrary cores or quadratic address ranks is required.

A018-COLLISION-BLOCK-INTERFACE v1 has been analytically reconstructed in REVIEW_DEPENDENCIES.md. Its M_W payment is compatible but the present family actually has M_W=0. The new B_W payment closes the named G-LOWSEL-COLLISION obligation on this explicit unbounded structural class. A017/A020/A058/A060 can use it without a disagreement floor. A027/A028/A064 can use the complete block-tree ledger, but must retain the terminal core and cannot assign constant 4 to each singleton. The universal G-R-SELECT/G-R-MISMATCH gaps remain open.

## one next mathematical action and independent reviewer

Next action: introduce one shared selector coordinate between two rare-point modules and derive the exact signed row spectrum and influence correction, with the conditional T weights rho retained. Start with two events intersecting in exactly one physical bit; use a proper-block tree and compare its complete debt with the disjoint certificate, rather than repeat a one-point/module FEI estimate. This tests the precise hypothesis that currently prevents transfer toward arbitrary B_W and C019 stopping payment. Reviewers requested: A091 and A090; reconstruct the parent coefficient product and the singleton counterexample, and independently check the all-k constant and residual core scope. No messages were sent to other agents.

## actual persistence receipts or precise save blocker

All artifacts are written solely in the assigned A019 folder: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, NEW_SHARED_DATA_CLASS.tex, COLLISION_PAYMENT.md, REVIEW_DEPENDENCIES.md, code/check_translation.py, code/persist_stage.py, out/FROZEN_SPEC.json, out/CHECK.json, out/SOURCE_RECEIPTS.json and out/PERSISTENCE_RECEIPTS.json. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. Persistence receipts check exact schema keys, statement hash, compatibility identity and file hashes. No git, brain write, external publication, shared index edit or other-agent mutation occurred. Supervisor copying, mirror verification and independent acceptance of the new theorem remain pending.

## Universal bridge

This stage moves C018 erasure and C019 stopping-tree payment by paying the entire previously unpaid B_W at constant 4, with M_W exactly zero, for an explicit nonlinear translation class having arbitrarily small neighboring disagreement and unbounded selector arity/depth. It gives a proper-block certificate and preserves the full terminal core; it does not pay arbitrary residual entropy or show that arbitrary Boolean rows have such a factorization. The shortest next route is to test the exact lost hypothesis by sharing one physical selector coordinate between rare modules and computing its signed collision correction: that probes whether this paid block mechanism can extend toward the universal stopping debt, instead of producing another isolated positive-correlation class.
