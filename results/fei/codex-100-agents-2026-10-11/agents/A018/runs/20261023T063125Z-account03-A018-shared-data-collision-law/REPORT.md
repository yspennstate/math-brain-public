# A018 stage19: the original bank pays every stopped event-query depth

## exact target, quantifiers, hypotheses and units

Prove payment for EVERY depth of the one-balanced point-event family, every integer k>=2 and any fixed event-bit order, with the SAME original bank, unchanged old U in[0,1/8], complete first-selector bill, conditional conversion charges and all full terminal references retained. Units are bits. Result: the remaining original bank is strictly>1/8 at EVERY stopped-tree prefix. Full FEI remains OPEN; this is not a universal source/reference construction.

## sources actually read, revisions and theorem locators

Read current BOARD.md, B04 STREAM_NOTES.md v2, own STATUS and stage18 proof/checker, A019 stage18 REPORT.md and full CLAIMS.json, A019/A020 latest LEARNED entries, machine-wide AGENTS.md and the complete protocol revision2026-10-11-execution-v2. Prior stages supplied campaign/paper conventions; no new external theorem is assumed here. The board makes clear A019 already completed the first-v step, so that result is reviewed rather than re-presented as new. A020 local inherited-admission obstruction is retained. One read-only math-store search returned weak generic matches, no answering campaign dependency; no card is promoted to a premise. Exact byte receipts are in out/SOURCE_RECEIPTS.json. This run reviews A019 statement hash c4b16abefd9380ebbc0a42bfd3144a9fcacbf9c44610079c59308a49620ed22f without a material repair. Own radial ledger already has A019 independent HOLDS at original scope.

## complete derivation or exact first unsupported line

# Cumulative original-core-marginal payment

Here are all conventions explicitly. The event bits v are uniform in {0,1}^k, u is an independent uniform sign, E_k=1[v=0], h0=u and hk=(1-E_k)u+E_k. The selector chooses h0 at q0 and hk at q1. The two-bit mask s is -1 at one point and +1 at three points, on a disjoint block. F=1 at physical gate x0 and h*s at x1. P_g is the squared Walsh law; CE(P,Q)=-sum P log2 Q and KL(P||Q)=CE(P,Q)-H(P). Original Qb=(P_hb+delta_empty)/2, with c0=1 and ck=CE(P_hk,Qk). The selector parent core reference is the actual q-frequency conditional lift of average(Q0,Qk); all activation references have data marginal (Qcore tensor P_s+delta_empty)/2 and actual gate-frequency conditionals, with the absent convention on zero true rows. Write C0=CE(F_q1), Cq0=CE(F_q0), Croot=CE(F) for these prescribed complete codes. The FULL first-selector rate4 excess is Tq=Croot-(Cq0+C0)/2-e, since Inf_q(F)=e/4. The original B=(4I(h0)-c0+4I(hk)-ck)/4, embedded in the supplied complete child activation surplus, and U are retained without renewal.

Define eta(y)=-y log2 y with eta(0)=0, Psi(b)=eta((1+b)^2/4)+eta((1-b)^2/4)+1-b^2-eta(b^2)/2, phi(b)=Psi(b/2), and A(p,z)=[p log2(p/z)+(1+p)log2((1+z)/(1+p))]/2, with continuous zero conventions. At a depth-t surviving core hk-t, C_t denotes its full activation CE with the original folded core reference R_t. C_u(t) is the stopped u sibling CE with the SAME R_t, and C_const(k) is the final constant+1 core activation CE with R_k. Direct actual edges give I(hk)=1-e+k*e: the u influence is1-e and each event-bit influence is e. The exact Walsh cardinality check independently agrees with this formula.

Put e=2^-k, k>=2. After t actual event-bit queries on the all-zero surviving path, d=2^t e. The frequency marginal R_t of the ORIGINAL Qk has atoms e*d/2 everywhere, plus 1/2 at empty and (1-2e)/2 at the u singleton. This follows directly from Qk=(Pk+delta_empty)/2, whose large u atom is (1-e)^2/2. The uniform part has total mass e at EVERY depth; no reference is renewed. At depth t the actual children are u and h_(k-t), with the same R_t and prescribed actual gate-frequency lifts. Terminal functions and their full activation costs are retained.

For a query let Ract be the literal frequency marginal of the incoming activation reference. Its data marginal is (R_t tensor P_s+delta_empty)/2, equal to that of the prescribed child references. Hence conversion CE(Pchild,Ract)-CE(Pchild,Qchild) is conditional KL>=0. The decrement to literal marginals is sum Pparent log2(Ract/Qparent)>=0, because every atom of Ract is a sum including that parent atom. Thus the FULL prescribed decrement D_t is nonnegative and includes conversion. At original physical reach 2^-t, the sum S=sum_{t=1}^k 2^-t D_t telescopes to (C_0-L)/2, where L=sum_{t=1}^k 2^-t C_u(t)+e C_const(k). This is a stopped physical tree, not a declaration that individual inherited leaves are rate4 eligible.

The original core bank B=7/4+(k-1)e-c_k/4, where c_k=CE(Pk,Qk). The incoming q1 activation CE is C_0=1+c_k/2+phi(e)-A(e^2/4,(1+e^2)/8). Here phi(e)=Psi(e/2)<=2 and A>=0 as p<=z. Every u stopped activation has true entropy3, so full CE>=3; the final constant-core activation has entropy1+Psi(1/2)>2. Therefore L>3-e, and

B-S > 7/4+(k-3/2)e-c_k/2.

Original core KL<=1 gives c_k<=Hk+1. With f(e)=eta((1-e)^2), Hk=f(e)+4ke-2ke^2, and f(e)<=3e follows from -x ln x<=1-x and ln2>2/3. Consequently B-S>5/4-(k+3)e. For k>=3, (k+3)2^-k<=3/4, giving B-S>1/2. After the OLD U<=1/8 and FULL first-query positive Tq<1/4, B-U-(Tq)_+-S>1/8. No new v-influence credit is used.

The k2 endpoint is certified directly with exact prime-log intervals for the SAME B,Tq and all full leaves, and independently by clearing the rational log coefficients to a strict integer-product inequality in CERTIFICATES.json. The frozen main checker passed 835 exact assertions over 6 chains and 27 data queries. The all-k argument uses entropy lower bounds only on actual complete leaves and the original incoming reference only once; inherited KL need not remain<=1/2.

Because D_t>=0, each partial stopped tree spends no more than the full tree. Thus the >1/8 remainder holds at EVERY prefix, after retaining the q0 sibling and all first-one stopped leaves. This is uniform in the chosen fixed event-bit order by coordinate symmetry. The hierarchy fixes original Qk at q1 and carries its frequency marginals; the exact full selector debit already accounts for the change from the parent conditional lift to the supplied q children. No assertion equates these supplied q-child references with literal q marginals of the root activation reference.

For completeness, A>=0 used above follows from A(p,p)=0 and dA/dz=(z-p)/(2 ln(2) z(1+z))>=0 for z>=p. The concavity of phi follows from phi''(b)=log2(b^2/(4-b^2))/4<0 on (0,1], with even continuous phi and phi(0)=2. The terminal u activation has H=3 exactly, and the constant-core activation has H=1+Psi(1/2)>2; the latter sign is a separate rational-log certificate in the main checker. At each queried surviving node every true core Fourier coefficient and every mask coefficient is nonzero, so the inherited activation reference supports both full child laws; the zero-row absent convention at stopped u leaves causes no support loss.

## Independent reconstruction of A019-INHERITED-V-QUERY-SAME-BANK@1

This review addresses the original statement/hash c4b16abefd9380ebbc0a42bfd3144a9fcacbf9c44610079c59308a49620ed22f, without a substantive repair. Write f(e)=eta((1-e)^2). The exact Hk identity above gives DeltaH_core/2=2e+[f(e)-f(2e)/2]/2+(k-2)e^2. Direct differentiation gives f''=-2[3+2ln(1-e)]/ln2, negative on [0,1/2] and with magnitude<9 because ln2>2/3. The midpoint gap is therefore <(9/2)e^2; DeltaH_core/2<2e+(k+1/4)e^2<=41/64 for k>=2. Phi concavity makes C(e)=phi(e)-[phi(0)+phi(2e)]/2 increasing: C'(e)=phi'(e)-phi'(2e)>=0. Thus C(e)<=C(1/4)<1/16, with the endpoint certified independently in CERTIFICATES.json. Full true activation entropy decrement is <45/64. Incoming activation KL<=KL(Pk,Qk)/2<=1/2 follows by the physical-label log-sum identity: append the gate's deterministic branch and then merge it. For any finite prescribed children the complete CE decrement is DeltaH+KL_parent-average KL_child, so Tv<77/64. This inequality INCLUDES conditional conversion; no child KL allowance is renewed. Original A018 full first-query remainder>5/8 minus physical-reach bill Tv_+/2<77/128 leaves>3/128. Direct own Walsh/reference reconstruction checks that original first-node bound for all frozen k, while the preceding calculus proves all k. Verdict HOLDS at the complete original stated scope, no material repair; the new all-prefix continuation is separate A018 author work.

Universal gap: replacing this specific stopped point-event family by arbitrary overlapping branches still needs a single conserved reference/bank invariant. Stopping after an event fails and retaining all its full leaves does not prove arbitrary-core FEI.


The endpoint certificate, after multiplying the exact k2 remaining-minus1/8 log expression by512, is the strict integer inequality

17^297 * 3^16 * 5^434 * 109^257 * 11^7 * 7^392 > 2^2048 * 257^257 * 73^64 * 37^72.

Both integers are saved in out/CERTIFICATES.json; their bit lengths are5112 and4877, and a second reader reconstructs them from the saved exponents. This is a finite k2 certificate, while the displayed monotonicity/entropy argument proves every k>=3.

The first unsupported universal line is a terminal-cost lower bound payable from the SAME original signed reserve for arbitrary overlapping branches whose stopped siblings remain interacting. No argument here supplies such arbitrary terminals or proves local rate4 admission.

## executed validation with domain, arithmetic, commands and outputs

The frozen out/FROZEN_SPEC.json precedes the pilot. Command: python -X utf8 agents\A018\runs\20261023T063125Z-account03-A018-shared-data-collision-law\code\check_chain.py --pilot; PASS,1 chain,2 nodes,100 assertions,0.124 seconds. After adding independent endpoint/portable integer certificates and removing two redundant expressions, the main command omits --pilot: PASS,6 chains,k2..7,27 nodes,835 exact assertions in2.2270446000038646 seconds. The literal full activation truth-table check is k2,3; core Walsh coefficients are also compared to character sums in the helper. Full arrays independently check the folded-reference closed form and scalar activation CE, while exact spectral cardinality agrees with the analytical actual-edge influence formula. Every nonnegative marginal charge and conversion KL, the telescoping equality, all leaf costs and first-v original A019 bounds are checked. Fractions and exact prime-log vectors are used; signs use rational36-term atanh enclosures. The k2 final sign is ALSO checked by integer products. No float sign is accepted. Estimated memory120MB, no >300MB job or compiler job was launched; no memory admission bypass or automatic dimension increase. Pilot is excluded from835. No Lean or kernel certificate is claimed.

## proof dependencies and changed downstream conclusions

Dependency chain: previous accepted original bank/full-q specialization -> this original-marginal cumulative proof. The reviewed A019 first-v theorem is independently reconstructed, but the new cumulative estimate does not assume its conservative77/128 debit. That ceiling is not charged as an actual expense: exact query decrements are retained and telescope. The SAME old U and exact positive full Tq stay booked; all new v influence is left unspent. New claim A018-ORIGINAL-MARGINAL-ALL-DEPTH-PAYMENT@1 is author-proved/exact-checked and awaits independent review. There is no priority/novelty claim. The local complete-reference eligibility obstruction remains valid and is not contradicted by a paid weighted account.

## one next mathematical action and independent reviewer

Consume A016/A020 original-reference cleanup obstruction; replace point-event stopping by two overlapping event tests whose first-one siblings remain interacting, and derive a full original signed-reserve leaf criterion without a renewed half-core allowance. A019/A020 independently review all-depth theorem. This is a source-bound local handoff; no messages were sent or shared registries modified.

## actual persistence receipts or precise save blocker

All four protocol files, code and exact outputs are saved in this run, with byte-identical PROGRESS/PACKET_DELTA. STATUS is exactly two lines; WORKLOG and LEARNED receive dated appends. out/VALIDATION.json checks exact schemas, report headings, portable certificate and file sizes; out/MANIFEST.json records local byte hashes. Independent acceptance, supervisor copying and remote mirrors remain unverified. Brain self-care remains degraded/unverified: stale owner-model and state-of-mind notes affect personal-context reliability and are not mathematical inputs. No background research job remains; no existing work was stopped.

## Universal bridge

This stage advances C024 history transfer toward C019 stopping-tree payment from one inherited query to every k-step stopped event history, uniformly for all k>=2: the SAME original bank retains>1/8 after the old debit, FULL selector bill, all conditional conversions and every complete terminal. It removes renewed incoming-KL admission from this unbounded-depth fixture. Arbitrary interacting stopped leaves still have no universal payable reference/signed-reserve invariant. The shortest next route is to keep two overlapping event tests live in stopped siblings and audit the full original signed reserve against A016/A020 cleanup obstructions, because that challenges the terminal-cost step a universal stopping tree needs rather than rechecking another depth of this now closed family.
