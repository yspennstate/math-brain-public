# A018 stage 3: shared-separator collision, data dependence and owned influence

Run 20261013T222945Z-account05-A018-shared-data-collision-law, B04/A018. Full FEI remains OPEN. A016's connected-spine control independently HOLDS at its stated scope. A new exact paired-row/reference interface is proved below; an uncorrected entropy-subadditivity strengthening remains open outside the explicitly certified finite domain.

## exact target, quantifiers, hypotheses and units

Let r>=1, let z be one uniform physical bit, and let y_1,...,y_r be mutually disjoint uniform private input blocks, independent of z. Let f_j(z,y_j)=g_{j,z}(y_j) be arbitrary Boolean signs; no balance, correlation or spectral separation is assumed. Set F(z,y)=product_j f_j(z,y_j). The same physical z occurs in every factor. All entropies, cross-entropies CE and KL divergences use bits. I is Boolean physical influence; a trinary derivative's I is its squared-Fourier/Dirichlet energy.

For module j, write P_{j,b}(T)=hat(g_{j,b})(T)^2, R_j=(P_{j,0}+P_{j,1})/2, B_j=H(S_z^{(j)}|S_{y_j}^{(j)}), and M_j=H(R_j)-(H(g_{j,0})+H(g_{j,1}))/2. For the actual shared product set

R(T_1,...,T_r)=[product_j P_{j,0}(T_j)+product_j P_{j,1}(T_j)]/2,
B_*=H(S_z^F|S_y^F), M_*=H(R)-average_b sum_j H(g_{j,b}),
TC=KL(R || product_j R_j)=sum_j H(R_j)-H(R).

The universal exact identities proved here are

H(F)-sum_j H(f_j)=B_*-sum_j B_j-TC,
M_*=sum_j M_j-TC,
0<=TC<=sum_j M_j, and H(F)<=sum_j H(f_j)+1.

For finite-cost normalized complete module references Q_j(A,T), let q_j(T)=sum_A Q_j(A,T), tau_j(A|T)=Q_j(A,T)/q_j(T), and k_j=E_{R_j} KL(nu_j(.|T)||tau_j(.|T)), where nu_j is the actual module spectral conditional selector law. Define the shared reference Q_*(A,T)=nu_*(A|T) product_j q_j(T_j), with an arbitrary fixed conditional law on zero true rows. Then

CE_*(F)=sum_j CE_{Q_j}(f_j)+B_*-sum_j B_j-sum_j k_j,
CE_*(F)-H(F)=TC+sum_j KL(R_j||q_j).

This is a complete reference accounting identity, not a free use of unknown entropy: B_* is explicitly retained and every marginal/conditional reference law is fixed for the function. Finite CE hypotheses avoid undefined infinity subtraction. Uniform or exact spectral references used in tests are fixtures, not supplied universal FEI certificates.

The physical owner correction is also exact. With d_j=Inf_z(f_j) and d_*=Inf_z(F),

d_*=[1-product_j(1-2d_j)]/2,
I(F)=sum_j average_b I(g_{j,b})+d_*,
sum_j I(f_j)-I(F)=sum_j d_j-d_*=:L>=0.

Thus module budgets count the same physical z repeatedly; a valid transfer must retain L or a proved exclusive reserve. No universal payment for L, B_* or TC is asserted here.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start, snapshot 2026-10-13 22:25 UTC, then the relevant B04/B06/B12/B13/B19/B20 updates. Read B04 STREAM_NOTES v2, still dated 2026-10-11 23:25 UTC, own STATUS.md and durable LEARNED.md. Its A018 three-claim review request was completed in stage 2, so protocol dispatch consumes the new productive A016 dependency rather than re-running that review.

The protocol remains EXECUTION_PROTOCOL.json, fei-execution-protocol/2, revision 2026-10-11-execution-v2. The report/progress/claim field sets are used without editing shared indices. A016 source: agents/A016/runs/20261013T214508Z-account05-A016-addressing-benchmark/REPORT.md Sections 1-6 and CLAIMS.json, A016-CONNECTED-SPINE-FACTOR-REPAIR-CONTROL@1. Its persist.py confirms its plain statement-text hash convention. A017 stage-3 REPORT.md and A019/A020 LEARNED.md provide nonduplication and scope guards: incompatible phase gradients, arbitrary disjoint activation phases, and the five-bit failure of the earlier finite 0.81 discount. The latter does not contradict A018's explicitly four-bit certificate.

A097 LEARNED.md supplies the already proved compatible-reference lift and terminal-credit nonreuse guard; the present product-marginal specialization makes its shared-data TC debt explicit. A086 LEARNED.md's disjoint-child transfer does not admit one shared private coordinate. A095 LEARNED.md gives complete common-spine costs and corrects a hashing diagnosis. B04 lead code/write_records.py was read to check that diagnosis directly. A018 stage-2 arithmetic helper supplies existing proven rational logarithm bounds; it is the only imported code, and its main/search section is not executed. No A016 checker is imported. Source byte hashes and read scopes are in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

### 1. Independent A016 reconstruction: HOLDS at stated scope

A016's family uses one common bit z, private selectors x_j and m-1 private data bits t_j, a>=1, even m>=4:

c_j=(-1)^(t_{j,2}t_{j,3}+...+t_{j,m-2}t_{j,m-1}),
f_j=(-1)^(z t_{j,1})c_j-2x_j 1{z=0,t_j=0}, F=product_j f_j.

Let delta=2^{-m}. At z=0 the private module is psi=c_j-2x_j 1{t_j=0}; at z=1 it is the character (-1)^(t_{j,1})c_j. Direct edge differences give

J_0=(m-2)/2+2(m-1)delta,
L_0=J_0+2delta=(m-2)/2+2m delta,
Inf_z(F)=[1-(-2delta)^a]/2,
I(F)=a[(m-1)/2+m delta]+Inf_z(F).

For example, fixing x=1 flips one point of the m-1-bit private c_j extension, creating an extra 4delta influence in each data direction; fair averaging of x gives J_0. The common-z branch ratio has independent factors of mean -2delta, giving the displayed d_z. These normalizers were independently verified physically.

The unique multilinear ANF exponent is a sum of each module's z t_1, its private quadratic pairs, and x_j(1+z) product_l(1+t_{j,l}). At the root its uncancelled highest monomial connects all coordinates to z. After a selector prefix, each earlier x=1 branch still has a monomial z product_l t_l of degree m>=4, so its data remain connected to z. Each earlier x=0 branch detaches exactly its m-2 private quadratic coordinates into independent pairs, retaining z t_1. All remaining selectors still connect their entire private block to z. ANF uniqueness proves that these graph components are the finest possible partition into independent sign factors. The m=2 cancellation endpoint remains excluded exactly as in A016.

At the next queried selector, D is its m-coordinate signed point indicator times the other modules' z=0 values. Its norm is delta. The point indicator contributes m delta/2 energy; each other retained private block contributes delta times its z=0 energy. Averaging all prior selector assignments gives the raw bill

T_raw=a m delta+delta a(a-1)[m-2+(4m-2)delta].

Only the earlier x=0 quadratic pairs can be removed. At prefix depth j their expected removed energy is j(m-2)/4, multiplied by delta in D. Summing 2I(D) gives exactly

T_factor=a m delta+delta a(a-1)[3(m-2)/4+(4m-2)delta].

The exact-B filter survives: in queried data rows with its t_1 Fourier bit absent, the z=1 coefficient is zero. The two parent selector-sector coefficients are (eu-delta)hat(H_0)(R) and delta hat(H_0)(R), u=sqrt(delta). Their row mass divided by delta^2 hat(H_0)^2 is at least 1/(2delta). There are two Fourier z choices and 2^{m-2} private quadratic indices. Parseval of the actual Boolean H_0 yields

B_v >=delta(m-1)/2, Inf_v=delta

at every selector-first descendant. For any fixed K, choosing even m with (m-1)/2>K makes all those nodes bad. T_factor is quadratic in a whereas I(F) is linear: factor removal cannot repair that fixed rule. This is not a counterexample to universal adaptive selection.

Querying z first instead has d_z>=3/8 and B_z<=1<4d_z. Both leaves are explicitly paid: I_0=aL_0, I_1=am/2; uniform private masks cost am<=4I_0 and the character-flat leaf costs a(m-2)<=2I_1. Thus the chosen tree has zero internal K4 bad-node bill without treating leaves as free.

The stronger complete reference uses Q0=2^{-am}, Q1=2^{-a(m-2)} on the exact character-flat support, and Q(A,R)=(Q0(R)+Q1(R))/4. Summing both A gives normalization one. That support's true parent data mass is alpha=(1+delta^a)/2 because the other leaf puts mass delta^a there. Consequently

CE_Q=am+2-alpha log2(1+4^a)<=a(m-1)+2.

With X=a(m-1)>=3, I(F)>=X/2+3/8 and X+2<=(8/3)(X/2+3/8). Thus CE_Q<=(8/3)I(F), including root, posterior and terminal costs. This is a full independent reconstruction of A016's critical claim, supplemented by distinct ANF/derivative/reference code. No mathematical repair to that version is supplied.

### 2. Exact shared-label data law

For each private Fourier set T_j let a_j=hat(g_{j,0})(T_j), b_j=hat(g_{j,1})(T_j). The two parent coefficients are

hat(F)(0,T)=[product_j a_j+product_j b_j]/2,
hat(F)(1,T)=[product_j a_j-product_j b_j]/2.

Their squared sum is R(T) as stated above. Summing over other T coordinates shows its jth marginal is R_j, using Parseval for every branch. Thus H(F)=H(R)+B_* and H(f_j)=H(R_j)+B_j. Subtraction immediately proves

H(F)-sum_j H(f_j)=B_*-sum_j B_j-TC.

All signs are retained in the coefficients before squaring. For one selector bit, exchanging the signs of one row changes which sector is occupied but not its conditional entropy. Zero rows are omitted from conditional entropies and may carry arbitrary fixed conditionals in references.

The physical branch label b is uniform in the auxiliary law P(b,T)=product_j P_{j,b}(T_j)/2. Given b the labels T_j are independent. Its mutual information with T is M_*, and its mutual information with T_j is M_j. The entropy chain rules give M_*=sum_j M_j-TC. Nonnegativity of KL and mutual information gives TC>=0 and TC<=sum_j M_j. Since B_*<=1, B_j>=0 and TC>=0, the universal corrected bound H(F)<=sum_j H(f_j)+1 follows. No novelty claim is made for this elementary shared-bit overlap bound; the important delivered object is its exact residual.

### 3. Complete reference transfer with the missing debt visible

For each finite-cost normalized Q_j, the usual conditional decomposition is

CE_{Q_j}(f_j)=E_{R_j} log2(1/q_j(T_j))+B_j+k_j,
D(P_{f_j}||Q_j)=D(R_j||q_j)+k_j.

Fix nu_*(A|T) to the actual parent conditional law on positive true rows and choose a fixed arbitrary distribution on zero true rows. Then Q_*(A,T)=nu_*(A|T) product_j q_j(T_j) has total mass one. This is the function-specific compatible lift, not a sampled-row-dependent choice of a different reference. Its expected complete cost is

CE_*(F)=B_*+sum_j E_{R_j} log2(1/q_j(T_j))
=sum_j CE_{Q_j}(f_j)+B_*-sum_j B_j-sum_j k_j.

Subtract H(F)=sum H(f_j)+B_*-sum B_j-TC and use the module debt decomposition:

CE_*-H(F)=TC+sum_j D(R_j||q_j).

Equivalently the joint data mismatch to product_j q_j equals TC plus the marginal divergences. The conditional module debts k_j are erased only by explicitly matching the new conditional selector reference; they cannot simultaneously be spent as terminal reserves elsewhere. Even with exact module marginals q_j=R_j, the product-data lift leaves debt TC. This is the precise distinction between zero marginal error and a paid joint shared-separator description.

### 4. Exclusive physical owner correction

Let E_j(y_j)=1{g_{j,0}(y_j)!=g_{j,1}(y_j)}. The shared-z output changes iff sum_j E_j is odd. These E_j are independent on their private blocks, with means d_j. Hence d_*=[1-product(1-2d_j)]/2. Conditioning on z gives every private influence as the corresponding average module influence. Therefore I(F)=sum private averages+d_*, whereas sum I(f_j) uses sum d_j for that same coordinate.

L=sum d_j-d_*=E[sum E_j-(sum E_j mod2)]=2E[floor((sum E_j)/2)]>=0.

It is not legitimate to combine module-level C I(f_j) certificates and silently replace sum I(f_j) by I(F). Likewise TC<=sum M_j<=(2/ln2)sum d_j is a bound in a repeated-module selector budget, not in the single physical d_* budget. Private inherited CE and any paid terminal deficits must be retained explicitly. This is where a source-owned influence reserve remains necessary even if the entropy-subadditivity proposal turns out to be true.

### 5. First unsupported line, isolated as a paired-row inequality

The bounded tests prove H(F)<=H(f_1)+H(f_2) for all ordered modules with up to two private bits each. No all-dimensional proof is supplied for

B_* <= B_1+B_2+TC.

This is exactly the missing line in the uncorrected entropy-subadditivity proposal; no counterexample was found in the frozen domain. It can be reformulated for posterior biases U_j=(P_{j,0}-P_{j,1})/(P_{j,0}+P_{j,1}), sampled independently under R_1,R_2, with E U_j=0. Write e(u)=h2((1+sqrt(1-u^2))/2). Then the target is

E[(1+U_1 U_2)e((U_1+U_2)/(1+U_1 U_2))]
<=E e(U_1)+E e(U_2)+E[(1+U_1 U_2)log2(1+U_1 U_2)].

Zero-weight rows 1+U_1 U_2=0 contribute zero. The scalar reformulation itself is proved by the exact product row law. A proof for every zero-mean bias law would suffice; failure for an arbitrary real bias law would still require a Boolean realization before refuting the Boolean target. No non-Boolean relaxation is used to claim FEI progress.

Even proving this optional inequality would not pay the universal C019 tree: the one physical influence loss L and complete terminal costs remain. The next useful step is a signed paired-row bound inserted against an exclusive shared-coordinate reserve, not another assertion that spectral modules are independent.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications: out/FROZEN_SPEC.json before the pilot/product/spine jobs; out/IDENTITY_SPEC.json before testing the new TC/reference quantities on the same domain. Memory estimate 80 MB, fixed pilot 60 seconds and full job 120 seconds; no expected >300 MB job, so memok gate was not required. No GPU, randomization, automatic dimension escalation or simultaneous jobs. Actual peak memory was not measured.

Commands from the A018 directory:

`python -X utf8 runs\20261013T222945Z-account05-A018-shared-data-collision-law\code\check_product.py --pilot`

PASS: all 256 ordered one-private-bit module pairs, 272 checks, no entropy-subadditivity violations or inconclusive signs, 0.002 seconds measured by Python.

`python -X utf8 runs\20261013T222945Z-account05-A018-shared-data-collision-law\code\check_product.py`

PASS: all 65,536 ordered two-private-bit module pairs, 65,792 checks, no violations or inconclusive signs, 0.836 seconds. Each module coefficient is separately Walsh-checked; shared parent coefficients are reconstructed as signed product sums. Entropy signs and the universal +1 bound use exact integer prime-log vectors and outward rational intervals. The absence of a recorded witness is evidence for this finite domain only.

`python -X utf8 runs\20261013T222945Z-account05-A018-shared-data-collision-law\code\check_spine.py`

PASS: 204 assertion groups, five fixtures (a,m)=(1,4),(2,4),(3,4),(1,6),(2,6), 1.673 seconds. Each actual root and every selector-prefix assignment is reconstructed. A separate GF(2) Mobius/interaction graph gives the finest factor partition; actual trinary Walsh derivatives verify retained-coordinate energy and the all-descendant lower B bound; actual edges/spectral influences verify the source formulas. The complete root reference sums exactly to one, its support mass equals alpha, and H<=CE<=8I/3 is certified. These fixture checks supplement the analytic all-a,m reconstruction, not an exhaustive theorem over arbitrary graphs. Completed fixtures were saved immediately to SPINE_PARTIAL.json.

`python -X utf8 runs\20261013T222945Z-account05-A018-shared-data-collision-law\code\check_row_identity.py`

PASS: all 65,536 module pairs, 328,269 checks, 2.891 seconds. Independently formed actual data row masses verify TC>=0, the exact B/TC entropy correction and the exact reference debt identity. Four fixture references are explicitly normalized and their target cross-entropies exactly checked, including zero rows and the empty Fourier set. This repetition of the fixed finite domain tests new mathematical quantities, rather than expanding a search already completed.

Total: 394,537 checks across the four commands. Exact entropy expressions are rational/integer linear forms in ln(prime), with 36-term Fraction atanh enclosures, positive geometric remainder, range reduction and outward 2^-80 rounding inherited from A018 stage 2. No floating sign or limiting ratio is a proof. out/PRODUCT_PILOT.json, PRODUCT_CHECK.json, SPINE_REVIEW.json and ROW_IDENTITY_CHECK.json contain the executed domain/counts/runtime/certificates.

## proof dependencies and changed downstream conclusions

A016-CONNECTED-SPINE-FACTOR-REPAIR-CONTROL@1 receives independent A018 HOLDS at its stated scope: optimal factor removal still overcharges the specified bad-selector-first rule, while the paid separator and normalized CE bound are valid. No source repair is made, so reviewer independence is preserved. This does not refute general adaptive tree selection.

The new A018-SHARED-SEPARATOR-TC-REFERENCE@1 is an elementary exact interface derived from Parseval and finite entropy/KL chain rules. It uses no pending A016 claim as a premise. It specializes, rather than re-proves, A097's already available compatible-reference framework. Consumers A019/A020/A086/A095/A097 obtain the exact joint-data TC debt and the physical repeated-selector loss L. No imported complete module reference or child FEI certificate is assumed universal. The uncorrected shared-bit product bound is recorded as finite evidence plus an honest scalar gap, not as an all-dimensional claim.

Metadata correction: stage 2 wrongly described the B04 lead's source hashes as mismatching. Its code hashes canonical JSON of {statement,hypotheses}, with sorted keys and compact separators; those digests match the original three claims. A018 had compared plain statement UTF-8 instead. out/HASH_CONVENTION_CORRECTION.json checks both recipes and identifies the affected stage-2 review records. The three mathematical verdicts remain valid, but no lead hash required repair. Earlier run files are preserved immutably; this correction and rolling LEARNED.md supersede that metadata diagnosis. B20/A081 may adopt this source-bound bookkeeping correction separately from mathematical acceptance.

## one next mathematical action and independent reviewer

Next: prove or refute the displayed zero-mean paired-row inequality analytically, then insert its exact correction against L and one exclusive shared-coordinate deficit reserve on the smallest two-separator fixture. If the unrestricted bias inequality fails, check Boolean realizability rather than treating a real-vector witness as a Boolean obstruction. Retain both marginal KL bills and terminal core CE, and use exact B to filter bad nodes. This directly consumes the shared-separator interaction found by A016 and the retained-core interfaces pursued by A086/A095/A097.

Independent reviewers: A090/A091 for the new row/reference interface; A016 can challenge the shared-spine reconstruction and A095/A097 the complete debt accounting. No tools sent messages to other agents. This local source-bound artifact is the handoff.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code and out specifications/certificates, independent review and hash-convention correction receipts are saved inside the assigned run. STATUS.md is two lines; WORKLOG.md is appended; LEARNED.md retains prior durable facts and explicitly retracts only the erroneous metadata diagnosis. out/PERSISTENCE_RECEIPTS.json verifies claim/progress field sets, declared hash recipes, JSON parsing, equal packet delta, the final Universal bridge paragraph and per-file limits. No git, protected trading tree access, brain write, external communication, other-agent modification, supervisor adoption or mirror verification is claimed.

## Universal bridge

This stage advances C019's shared-coordinate payment target by independently confirming that factor removal fails on a connected all-dimensional family and by isolating the exact entropy correction B_*-sum B_j-TC plus the physical repeated-selector loss L. It advances the C020 reference interface by proving that the conditional-product lift's debt is precisely TC plus marginal KL, so dependence is no longer hidden behind independently cheap module references. No universal influence constant is obtained: the paired-row subadditivity inequality, exclusive payment of L/remaining data debt and complete terminal reserve are still open. NEXT targets that scalar signed-collision bottleneck before a two-separator insertion, which tests the actual shared-budget mechanism rather than collecting another disconnected class or extending a blind census.
