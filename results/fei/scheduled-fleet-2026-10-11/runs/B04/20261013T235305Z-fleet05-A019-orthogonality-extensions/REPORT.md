# A019 stage 3: folded separator loss and exclusive private-block boundary accounts

Run 20261013T235305Z-fleet05-A019-orthogonality-extensions. Stream B04, packet A019. Full FEI remains OPEN. This stage completes the interrupted stage-2 artifacts, consumes A018's new shared-separator interface, and proves an exact ownership correction valid for arbitrary Boolean modules. Independent review of the new correction is pending.

## exact target, quantifiers, hypotheses and units

Let r>=1 and f_j(z,y_j) be arbitrary Boolean signs. The physical separator z is one common uniform bit; private cubes y_j are mutually disjoint and independent of z. Write g_(j,b)=f_j(b,.), J_j=(I(g_(j,0))+I(g_(j,1)))/2, and d_j=Pr[g_(j,0)!=g_(j,1)]. No balance, symmetry, dimension, or positive-disagreement assumption is made. All entropy/cross-entropy units are bits. I(D) for a real derivative is its squared-Fourier Dirichlet energy.

Multiply module j by the separator character if d_j>1/2. This leaves its Fourier entropy and private influence unchanged and folds its separator influence to delta_j=min(d_j,1-d_j). Let the resulting children be a_j,b_j, q_j=E[a_j b_j]=1-2delta_j>=0, and kappa_j=I((a_j-b_j)/2). Define

Q_(-j)=product_(k!=j)q_k, delta_*=(1-product_j q_j)/2,
J=sum_j J_j, L_fold=sum_j delta_j-delta_*,
t_j=(1-Q_(-j))J_j/2+Q_(-j)kappa_j.

For the folded shared product F'=product_j f'_j, the exact influence identities are I_private(F')=J and Inf_z(F')=delta_*. The original product F differs only by an overall separator character, so H(F')=H(F), private influences are identical, and Inf_z(F)>=delta_*.

The new ownership statements are

0<=L_fold<=J-delta_*,
I(D_z F')=sum_j t_j, with 0<=t_j<=J_j.

The coefficient 1 in the private-budget loss bound is optimal: modules with g_(j,0)=1, g_(j,1)=(-1)^(y_j) give J=r/2, delta_*=1/2 and L_fold=(r-1)/2=J-delta_*.

Given finite normalized complete references for the two actual terminal products, with costs c_0,c_1, the compatible conditional-selector lift gives one normalized root reference with

CE_root <=(c_0+c_1)/2+(3/ln2)delta_*+2sum_j t_j.

In particular an exclusive module allocation

(c_(j,0)+c_(j,1))/2+2t_j<=K J_j for every j, K>=3/ln2,

is sufficient for CE_root<=K I(F). Both terminal reference bills are retained. This is a sufficient owned-budget certificate, not a universal assertion that its hypotheses hold. The paired-row entropy-subadditivity inequality posed by A018 remains open.

## sources actually read, revisions and theorem locators

Read the current BOARD.md supervisor snapshot 2026-10-13 23:49 UTC, especially B04, A028/A050/A057/A064, A090/A091/A095/A097, and the stream lead B04/STREAM_NOTES.md v2 dated 2026-10-11 23:25 UTC. Read own STATUS.md and the interrupted stage-2 report/output state. The lead's original A019 direction (general activations, overlap, majority-core tree) is fulfilled by the now completed stage-2 star theorem. This stage follows dispatch by consuming the new shared-separator dependency rather than repeating those classes.

Protocol revision remains fei-execution-protocol/2, 2026-10-11-execution-v2; field sets are read directly for persistence. Stage 1 pinned the threshold 38-page Proposition8.6 and all required campaign/context sources. No percolation, biased-threshold or external literature theorem is newly used here.

Read A018 run 20261013T222945Z-fleet05-A018-shared-data-collision-law REPORT.md, sections2-5 in full: its exact B/TC/reference ledger and physical repeated-selector loss L, plus the missing zero-mean paired-row inequality. Read A097 run 20261013T222610Z-fleet05-A097-cross-route-transfer REPORT.md for the calibrated complete-reference/nonreuse scope, including its unrestricted bent-splice obstruction. The earlier A018 stage-2 independent reconstruction of B04-NODE-BOUNDARY@1 is already consumed and reconstructed in own stage-2 report. That accepted local lemma is used below without re-running its census. A018's new optional entropy-subadditivity inequality is not assumed as a premise.

The new board's connected-spine, priority control, shared-data lift and half-output tax results are source navigation, not automatically accepted premises. Current source hashes and exact read scopes are in out/SOURCE_RECEIPTS.json. No external novelty or literature priority is asserted.

## complete derivation or exact first unsupported line

### 1. Close the interrupted stage-2 artifact honestly

The stage-2 theorem/report and pilot were saved, but CLAIMS/PROGRESS/PACKET_DELTA and tree validation had not been finalized when the next stage arrived. The initial complete-domain checker timed out at its frozen300-second limit; there was no completed full census then. The corrected cached-sign helper was resumed on the same fixed domain, without raising n or the timeout. It passed9,764 cases and608,203 exact assertions in56.109seconds. A separate implementation checked204 actual selector-tree internal nodes on four majority-core fixtures,1,253 assertions,0.519seconds. Its exact leaf translations, entropy/influence telescopes, K3 local erasure and raw core-boundary surplus all passed. The previous run's persistence script then saved its missing protocol files and rolling state. Stage2 is now complete locally, not independently accepted by this step.

Metadata correction to the old prose: code/failed_star_v1.py is a reconstructed minimal exact witness of the omitted nonempty-frequency erasure term, not an original byte archive of the first failing program. The failed equation/witness and timeout amendment are preserved. The current stage records that distinction explicitly; no original proof claim is upgraded by a file receipt. The stage-2 result is B_W<=5I_W for one-shared-bit point-translation stars and zero localized selector boundary bill at threshold3 with terminal core H retained. It is not reranked as a new theorem here.

### 2. Character folding preserves the relevant entropy and reference costs

Multiplying f_j by chi_{z} shifts every Fourier set by symmetric difference with {z}; it is a permutation of squared Fourier probabilities. H is unchanged; pushing a complete reference through the same permutation preserves normalization, KL and CE. The physical influence of z changes from d_j to1-d_j, while all private influences stay fixed. For d_j>1/2 choose this character multiplication. The transformed correlation q_j=1-2delta_j is nonnegative.

The product acquires at most one global separator character. Its actual separator influence is delta_* or1-delta_*, and therefore at least delta_*; its entropy and private resources do not change. The exact product formula for delta_* follows from independence of the private disagreements conditioned on the common z. This is the same physical normalization as A018, now in an entropy-invariant folded orientation.

Folding is essential. The uncorrected raw loss sum_j d_j-d_* cannot be bounded by a constant times J: take every f_j=chi_z and even r, with arbitrary irrelevant private cubes. The product is constant, J=0, and raw loss r. Folding removes these character-only influences at no entropy cost. This witness is elementary; it is not an FEI counterexample.

### 3. The folded owner loss is paid by the private budget

For the private Boolean sign k_j=a_j b_j, its variance is1-q_j^2=4delta_j(1-delta_j). Poincare follows directly from Parseval, Var(k_j)<=I(k_j). On every private edge, a product changes only if at least one factor changes, so

I(k_j)<=I(a_j)+I(b_j)=2J_j.

Thus J_j>=2delta_j(1-delta_j)>=delta_j, because0<=delta_j<=1/2. Summing gives sum delta_j<=J. The shared output is pivotal exactly when an odd number of the independent folded module disagreements occur, so

L_fold=E[number of disagreements-(number mod2)]>=0.

Subtracting delta_* from sum delta_j<=J proves L_fold<=J-delta_*. This pays a duplicated separator bill using named disjoint private blocks, with no core reference or entropy assumed cheap. It does not authorize spending the same J_j again without increasing the total assigned rate.

Sharpness: if a_j=1 and b_j is its own private coordinate character, q_j=0, J_j=delta_j=1/2. Then delta_*=1/2 and L_fold=J-delta_* for every r. Also L_fold/J=1-1/r tends to1. These are actual Boolean modules in arbitrarily large dimensions, not abstract bias laws. A lower universal coefficient on J is impossible.

### 4. Exact derivative energy and one account per private block

Let A=product_j a_j, B=product_j b_j, D=(A-B)/2. For a private derivative in block j, the cross term factorizes over all other disjoint blocks. Put C_j=sum_U |U| ahat_j(U)bhat_j(U). Direct expansion yields

I(D)=(1/4)sum_j[I(a_j)+I(b_j)-2C_j Q_(-j)].

Since kappa_j=(I(a_j)+I(b_j)-2C_j)/4 and J_j=(I(a_j)+I(b_j))/2, rearranging proves

I(D)=sum_j[(1-Q_(-j))J_j/2+Q_(-j)kappa_j]=sum_j t_j.

Parallelogram/Cauchy-Schwarz gives kappa_j<=J_j, and0<=Q_(-j)<=1. Thus t_j<=((1+Q_(-j))/2)J_j<=J_j. Each t_j is assigned solely to physical private block j. The first component is the spectator contribution caused by other modules' possible mismatch; the second is the intrinsic module derivative energy. Their mixture, rather than their separately repeated worst-case bounds, is the budget that may be spent.

Apply the accepted B04-NODE-BOUNDARY@1 to the folded Boolean product:

H(F)-[H(A)+H(B)]/2 <=(3/ln2)delta_*+2sum_j t_j.

This controls one named separator step with actual terminal entropy. It is neither a universal fixed-price selector-only payment nor a proof that a cumulative adaptive boundary bill is universally bounded. Exact B may still be needed to choose or reject the separator, and no terminal budget is free.

### 5. Complete root reference with terminal CE retained

Supply finite-cost normalized complete references Q_0,Q_1 on the same private Fourier-set space for A,B. Let q=(Q_0+Q_1)/2. Let P_0,P_1 be the two true squared spectral laws and R=(P_0+P_1)/2. Fix the actual parent conditional selector law nu(.|T) on positive true rows, and an arbitrary fixed conditional on zero rows. Then

Q_root(S_z,T)=nu(S_z|T)q(T)

is one normalized reference. KL convexity/log-sum gives

KL(P_F'||Q_root)=KL(R||q)<=[KL(P_0||Q_0)+KL(P_1||Q_1)]/2.

Subtracting the actual terminal entropies therefore proves

CE_root <=(c_0+c_1)/2+Delta_z H
<=(c_0+c_1)/2+(3/ln2)delta_*+2sum_j t_j.

For disjoint terminal products, Q_b=product_j Q_(j,b) and c_b=sum_j c_(j,b); these are supplied complete references, not universally constructed ones. If each private account satisfies c_(j,avg)+2t_j<=KJ_j and K>=3/ln2, adding all accounts and the one physical separator account gives CE_root<=K[J+delta_*]<=K I(F). The root reference's character permutation restores the original un-folded product at identical CE.

This explicitly distinguishes a valid larger-rate sufficient allocation from preserving the old module rate for free. A crude terminal certificate c_(j,avg)<=C J_j yields rate max(C+2,3/ln2) at this one step. Iterating this crude rate adds slack costs; it is not the universal bridge. The exact t_j is retained to test whether existing terminal slack pays the insertion at a fixed campaign-wide K without reuse.

### 6. Paired-row discovery and first unsupported line

A018's stronger optional inequality B_*<=sum B_j+TC is not used above. To test its sufficient scalar relaxation, use independent two-point zero-mean bias laws supported on +a,-b with weights b/(a+b),a/(a+b). The specified81 laws have nine rational Pythagorean magnitudes and rational complementary square roots. Thus the e(u)=h2((1+sqrt(1-u^2))/2) and combined posterior terms admit exact rational entropy expressions.

The frozen6,561 ordered-law discovery grid had no negative floating margin. The selected floating minimum (law50,50) was separately enclosed by exact rational log intervals with NONNEGATIVE sign. This does NOT certify every grid sign, identify a rigorous minimum, or prove the universal scalar inequality; unselected floats remain evidence. No Boolean realization of an arbitrary bias law is asserted. The exact first unsupported line remains the all-zero-mean expectation inequality in A018 section5, or a weaker signed-excess bound paid by the newly isolated exclusive terminal reserve. Showing folded L is affordable does not make that spectral excess disappear. A naive pointwise strengthening is exactly false: at u=v=7/25 its gap is 2+(2304/625)log2(5)-(2352/625)log2(7)<0, certified by the integer comparison 2^1250*5^2304<7^2352. out/POINTWISE_DIAGNOSTIC.json preserves this single-case certificate. Those fixed biases do not have zero mean, so this does not refute A018's averaged target or provide a Boolean product counterexample; it rules out dropping the zero-mean cancellations in a proof.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json froze the81-law/6,561-pair scalar discovery domain before search, helper A019-paired-bias-v1. Double arithmetic ranked candidates only; the selected pair's rational-log expression and outward60-term atanh interval are in out/BIAS_CHECK.json. Observed runtime2.198seconds, no negative floating candidates. The complementary square roots are rational by construction; zero-weight rows are omitted.

The independent ownership helper A019-folded-owner-v1 froze its actual Boolean family before each pilot/full job. Pilot: all256 ordered pairs with one private bit per module. Full: those pairs plus4,096 ordered pairs with private sizes2,1 and4,096 ordered triples with one private bit each, total8,448 products. Module tables include every Boolean truth table in the stated domains; no symmetry quotient. Maximum actual parent dimension4, no automatic dimension increase. The sharp parity family r=1,...,32 is checked through its proved closed forms, not exponentially growing tables.

Integer Walsh and direct edge differences independently verify folded physical influences. Fraction identities check J>=sum delta, exact product/folding sector permutations, owner loss, module derivative energy and the total cross-energy decomposition. Entropy boundary signs use outward40-term rational atanh intervals, signed endpoints and cached exact rational masses. Exact d=0 nodes are checked by identical child truth tables and absent selector coefficients, not an approximate zero tolerance. An initial pilot's tolerance fallback was removed; only the strict final runs are used as proof validation.

Commands from A019:

`python -X utf8 runs/20261013T235305Z-fleet05-A019-orthogonality-extensions/code/paired_bias.py`

`python -X utf8 runs/20261013T235305Z-fleet05-A019-orthogonality-extensions/code/check_owner.py --pilot`

`python -X utf8 runs/20261013T235305Z-fleet05-A019-orthogonality-extensions/code/check_owner.py`

Final pilot PASS:256 cases,2,944 assertions,0.377seconds. Full PASS:8,448 cases,98,432 exact assertions,12.780seconds. out/OWNER_PILOT.json and OWNER_CHECK.json preserve outcomes, sharp-family data and helper hashes. Memory estimates30MB and60MB; no >300MB job planned, so memok was not triggered. No GPU, heavy job, simultaneous heavy computation, floating proof sign, git or background process. The all-r/domain theorem rests on the complete analytic argument, not this finite coverage.

## proof dependencies and changed downstream conclusions

The exact ownership and derivative decomposition are self-contained Fourier/physical identities with elementary Poincare and union bound. Entropy boundary uses B04-NODE-BOUNDARY@1 with independent A018 stage-2 acceptance; complete-reference lift uses the compatible conditional-mixture mechanism already established by A097, reconstructed here by KL log-sum. The new theorem does not assume A018's unproved paired-row subadditivity or a universal terminal reference certificate.

A018/A095/A097 can replace raw sum d_j by the entropy-invariant folded orientation and charge its remaining loss to disjoint private budgets at optimal coefficient1. A016/A020 can test the exact t_j decomposition on connected shared-separator examples, with the necessary orientation and terminal CE specified. A064/A091 can insert the sufficient per-block inequality c_(j,avg)+2t_j<=KJ_j into their owned-slack tree ledgers. No existing terminal budget is credited twice. New claim independent review and supervisor adoption remain pending.

## one next mathematical action and independent reviewer

Next: evaluate the exact per-module reserve c_(j,avg)+2t_j-KJ_j on the connected bent-spine terminal references already supplied by A016/A018, using their true row normalizations and one shared-coordinate orientation. Determine whether excess collision/TC consumes the same slack, or whether a separator-first tree pays it with a distinct account. This is a concrete application of the exact owner correction at the live universal gap, not another search over a solved translation class. Independent reviewers: A090/A091 for ownership; A018 for the paired-row interface and A097 for complete-reference nonreuse. No tools send messages to other agents.

## actual persistence receipts or precise save blocker

The assigned current run contains REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, code/ and out/ with frozen specs, exact ownership output, selected bias certificate, old-stage completion receipts and source hashes. The prior unfinished run was finalized only inside A019's own tree. Rolling STATUS.md is two lines, WORKLOG.md appended and LEARNED.md records folding, sharpness, derivative ownership and the still-unpaid spectral excess. Final schema/hash/size readbacks are saved in out/PERSISTENCE_RECEIPTS.json. Supervisor copying, mirror verification and independent acceptance are not claimed.

## Universal bridge

This stage advances C019's shared-coordinate ownership by bounding the folded repeated-selector loss at the sharp private-budget coefficient1 and splitting the exact boundary derivative into disjoint t_j accounts; C020 obtains a normalized root-reference insertion with both terminal CE bills retained. The universal spectral excess/TC payment and existence of fixed-rate terminal slack remain open, and raw unfolded ownership remains false. NEXT applies these exact accounts to the campaign's connected bent-spine reference rather than another isolated class: it tests whether the same real slack can pay the collision insertion once, which is the remaining step needed for a universal stopping/reference bridge.
