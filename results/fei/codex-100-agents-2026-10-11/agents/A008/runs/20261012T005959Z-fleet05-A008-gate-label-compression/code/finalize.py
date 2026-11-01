from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parent.parent;RID=RUN.name
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
full=read(RUN/'out'/'BLOCK_CERTIFICATES.json');pilot=read(RUN/'out'/'PILOT_V5_CHECK.json');review=read(RUN/'out'/'REVIEW_A006_CHECK.json')
assert full['completed'] and full['cases']==96 and full['seconds']<900
assert pilot['completed'] and pilot['seconds']<60
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
author=ROOT.parent/'A006'/'runs'/'20261011T210855Z-fleet05-A006-posterior-forest-optimization'
old=read(author/'CLAIMS.json')[0]
assert old['statement_sha256']==review['reviewed_statement_sha256']
old['status']='INDEPENDENTLY_RECONSTRUCTED_ACCEPTED_LOCALLY_ADOPTION_PENDING'
old['review_records']=old['review_records']+[{'reviewer':'A008','verdict':'HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR','source':str(RUN/'REVIEW_A006.md'),'validation':str(RUN/'out'/'REVIEW_A006_CHECK.json'),'method':'generic assignment/source-SCC/parent/attachment enumeration; formal residual polynomial and independent sequential queue probabilities; analytic all-m proof','reviewer_supplied_substantive_repair':False,'timestamp_utc':now}]
base=Path(r'~\mop_fei100\reports\fei-2026-10-11')
forest=base/'source_material'/'reductions'/'paper'/'forests.tex'
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
statement='For every nonconstant uniform Boolean read-once DNF consisting of m>=1 disjoint nonempty signed conjunction clauses of arbitrary widths w_l>=1, the original conditioned forests.tex generator with the exact prime-implicant table, lambda_l=1 and one fixed order per clause has one partition-forest run per nonempty set. Its complete source residual R is <=(16/5+log2(e))*I<47I/10. The actual conditioned probabilities of these finite once-per-block zero-child runs have full nonempty spectral cross-entropy C_pf<=(26/5+2log2(3)+2log2(e))*I. Including the empty/nonempty entropy split, h2(Var f)+C_pf<67I/5. These are ideal complete-reference costs, without optional binary-prefix rounding or optional mixture-selector charges, not a new FEI class or a universal PI-J bound.'
hyp=['all finite m and positive integer clause widths','uniform independent physical signs; entropy in bits and gamma=6/5','each variable occurs in one clause and blocks are pairwise disjoint','one globally fixed prime-implicant table, feasible lambda_l=1 and full orders','original queue conditioned on nonempty initial roots; failed and infinite paths retain no output mass','selected finite run family uses all touched blocks as roots, zero children, and disjoint selected subsets','no sampled-set-dependent table or scale selection']
hash_statement=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
new={'claim_id':'B02-A008-UNEQUAL-READONCE-DNF-FOREST-PAYMENT','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hash_statement,'contributors':['A008'],'proof_source':{'path':str(RUN/'READ_ONCE_DNF.tex'),'ledger':str(RUN/'CODE_COST_LEDGER.json'),'certificate':str(RUN/'out'/'BLOCK_CERTIFICATES.json')},'proof_dependencies':[{'source':str(forest),'sha256':sha(forest),'locators':['eq:forestconditioning','eq:forestcost','thm:posteriorforest','lem:forestnormalizer','h2(v)<=2I source-level entropy estimate'],'status':'SOURCE_COMPLETE_BASELINE_READ'}],'review_records':[],'status':'AUTHOR_PROVED_RATIONAL_INTERVAL_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A006','A007','A009','A010','A086','A094','B20']}
dump(RUN/'CLAIMS.json',[old,new])
total=review['checks']+full['checks']+pilot['checks']
report=f'''# A008 stage 2: reviewed sunflower forests and unequal block-forest payment

## exact target, quantifiers, hypotheses and units

The B02 lead assigns A008 to reconstruct A006 v1 as a whole, then close the positive block-forest side for every read-once DNF. Both tasks are complete locally. The new theorem covers every m>=1 and every positive integer width tuple (w_1,...,w_m), arbitrary literal signs, disjoint supports, and one fixed prime-implicant table and feasible incidence vector lambda_l=1. Entropy and ideal costs are in bits; the source F statistic is in natural logs and its conversion is explicit. READ_ONCE_DNF.tex gives the complete proof.

The ORIGINAL conditioned queue has residual

    R <= (16/5+log2 e) I < 47I/10.

The actual finite once-per-block run probabilities, rather than the coarser generic forest bound, have complete nonempty cost

    C_pf <= (26/5+2log2 3+2log2 e) I.

Including the empty/nonempty entropy split gives h2(v)+C_pf<67I/5. This is a PI-J reference-cost closure on an already known FEI class. It is not a new Boolean FEI class or a universal bound. Optional prefix rounding and optional selector costs are not included or silently charged to I. Full FEI remains OPEN; the new result awaits independent review.

## sources actually read, revisions and theorem locators

BOARD.md was read at stage start, supervisor snapshot 2026-10-12 01:00 UTC. Own STATUS.md and B02/STREAM_NOTES.md v2 (2026-10-11 23:35 UTC) were read in full. The lead directs whole A006 review before the unequal-block positive result, sets PI-J as stream target, and forbids repeating single-gate tribes obstructions. The protocol was reread in full: fei-execution-protocol/2, revision 2026-10-11-execution-v2; its exact report/claim/progress fields govern the saved files.

A006's full stage-1 REPORT.md, CLAIMS.json and source manifest were read, and the original statement hash was recomputed. The review binds A006-SUNFLOWER-POSTERIOR-FOREST-PAYMENT@1. A006 stage-2 AUDIT_A008.md and A086 stage-2 JOINT_CODE_REVIEW.md were read: both independently accept A008 v1 at its original scope, without repairs. A094's durable review facts also accept A006 v1; this stage's lead-directed generic enumeration is an additional source-bound reconstruction, not a shared index edit. A007 stage-2 REPORT.md and claims were consumed for nonduplication: activated equal-width tribes are already closed there; this stage pays all unequal unactivated disjoint clause widths in the original lambda=1 reference independently.

The full source forests.tex was read, especially eq:forestpacking, eq:forestconditioning, eq:forestcost, thm:posteriorforest, lem:forestnormalizer and weighted activation. Its child-label law is lambda_child, not the distinct uniform-neighbor public queue. The proof imports only this complete baseline interface and its stated h2(v)<=2I estimate. The new spectral, hit-mass and conditional-binomial identities are derived directly. The prior-mixture source from the previous stage is only used when reconstructing A006's paid-prior clause. No unreviewed new campaign theorem is assumed. Byte hashes and locators are in out/SOURCES.json.

## complete derivation or exact first unsupported line

### Whole A006 review

REVIEW_A006.md records HOLDS at the original stated scope, with no repair supplied. Independent construction starts with every assignment of spectral coordinates to eligible gates, computes source SCCs, enumerates their root choices and incoming parent maps, checks reachability, enumerates attachments and chronological child-label orders, then deduplicates actual queue keys. It does not import or execute the author's checker or assume the star classification before enumerating.

The all-m proof then reconstructs why private-only sets have one isolated-root run, common singleton has m runs, and common+private sets have t! inside-root runs and (m-t)t! outside-root runs. Formal residual weights are independently summed as a-polynomials, a=2^-6/5. The complete actual probabilities multiply root conditioning, subset sizes, elementary normalizers, zero-child counts, root child counts, attachment multisets and each lambda-child draw. This yields exactly A006's residual S_B and complete W formulas. The source root normalizer D lies in [1/4,1/3); the two binomial recurrences prove R<=43I/10 and actual nonempty cost<=23I/2 for all m. The deterministic residual diverges on the common singleton. The normalized scale prior adds exactly v bits at component zero, preserving A006's 53I/10 and 25I/2 conclusions. Complete entropy inference still includes h2(v). No unsupported line remains in the reviewed restricted statement.

### Fixed unequal-block prime table and exact decoder

For disjoint clauses, p_l=2^-w_l, q_l=1-p_l, Q0=product q_l, v=4Q0(1-Q0), and lambda_l=1. The clauses are precisely the prime implicants: a partial assignment containing no full clause can be extended to make one unspecified literal false in every block. Signed literals can be flipped physically without changing the squared spectrum or influence.

Every spectral coordinate has a unique owner. Each used block is an isolated source SCC and hence one root; there are no children, no attachments and no extra child-order choices. Every root's selected subset is A intersect its block, so kappa=s and M=1. This is a finite terminating decoder: encode the root set once under the fixed initial-root law, read one local subset per root in fixed order, and take their union. The selected run family has no final output ambiguity and receives no posterior entropy credit. Additional successful queue runs are omitted, not presumed impossible.

The direct expansion f=1-2product_l(1-a_l) gives nonempty spectrum P(A)=4product_used p_l^2 product_unused q_l^2 and empty atom (1-2Q0)^2. Summing the other blocks yields mu_l=P(A hits block l)=4p_lQ0. Conditional on a block hit, its subset is uniform on all nonempty subsets; conditional on a coordinate being selected, all other within-block selections are independent fair bits. Physical pivotal events independently give I_l=2Q0 w_l p_l/q_l and I=sum I_l.

### Original residual paid in full

Put D=product_l(1+p_l)-1, so Lambda+log Z=log D exactly. The entire residual is

    R=v log D+sum_l mu_l w_l+(6/5) E sum_selected log(rank/(selected_predecessors+1)).

Labels L_l=0 because lambda=1, but the initial root-name selection cost is paid, not free: its exact contribution is v log D+sum mu_l w_l. Root rarity is <=2I. For normalization, T=sum w_l p_l/q_l>=2sum p_l, since w_l/q_l>=2. Also log D<=sum log(1+p_l)<=log(e)sum p_l. Thus v log D<=log(e)I, retaining its sign. This has a direct block proof and agrees with the baseline weighted activation estimate.

Conditional on selecting rank r, predecessor count X is Bin(r-1,1/2). The exact reciprocal identity E[r/(1+X)]=2(1-2^-r)<=2 and log concavity give expected rank cost <=1 bit per selected coordinate. Therefore the full rank bill is <=(6/5)I. Adding all components gives R<47I/10. This replaces the earlier loose factorial/concavity checkpoint R<13I/2; it is the same mechanism with the sharper exact conditional law.

### Actual queue cost, rather than generic K_ref overhead

With theta_s(j)=min(1,(s/rank(j))^(6/5)) and t_l(B)=[1/(s(s+1))]product_B theta_s/Z_s, the one specified successful run has

    q_pf(A)=D^-1 product_used [(p_l/2)*t_l(A_l)].

Every factor is retained: roots and their absence, subset sizes, subset normalizers/weights, and probability 1/2 of child count zero. Its empty attachment multiset has probability one. Each q_pf is an actual finite conditioned event and these events are disjoint, so sum q_pf<=1. The roots are paid once per used gate. This is the ORIGINAL generator, unlike A008 v1's separate dictionary generator.

The expected root block is <=(2+log e)I. The zero-child bill is <=I. Size costs <=log3 I follow from s(s+1)<=3^s. Subset normalizers <=log(6e)I follow from sum theta_s<=6s and the elementary symmetric polynomial bound. Pointwise log^+(rank/s)<=log(rank/(selected_predecessors+1)), so the actual subset weights cost <=(6/5)I by the same conditional rank law. The resulting nonempty constant is 26/5+2log3+2log e. Gibbs with reference masses 1-v and v*q_pf(A), and h2(v)<=2I, proves full reference cost <67I/5. Rational comparisons 3^5<2^8 and ln2>2/3 certify the displayed constant without floating-point signs.

### Honest boundary

No line in the new restricted theorem remains unsupported; independent review is pending. The first unsupported universal PI-J line is a bound on the ENTIRE joint label/rank/subset expectation under one fixed feasible prime-table reference when supports overlap. The exact uniform local law and forced ownership proved here do not follow from Booleanity alone. Neither A009's coordinatewise pressure obstruction nor A007's root cancellation settles that joint term. Physical prefix rounding adds less than one whole-message bit and is not claimed to be O(I) when I tends to zero.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded every search. The original full domain remains 96 width multisets, every integer partition of n=1,...,9; no automatic dimension escalation occurred. Block permutations and literal sign flips are the only symmetry reductions, justified by physical coordinate relabeling and invariance of the squared spectrum/influence. Memory estimate is 100 MB, below the 300 MB preflight threshold; no GPU or background job was used, and only one certificate computation ran at a time.

Whole A006 review: code/review_a006.py, integer FWHT and independent physical edges for m=1,...,8; generic assignment/SCC/forest/attachment/chronological traces for m=1,...,5; formal a-polynomial residual identities and sequential rational actual probabilities at a=2/5 and 1/2. Counts 3,11,37,143,681; {review['checks']:,} recorded assertions, {review['seconds']:.6f} seconds. Rational substitutions validate identities; the analytic proof handles the actual algebraic a.

Block certificate: code/check_blocks.py --pilot passed its final one-variable feasibility pilot in {pilot['seconds']:.6f} seconds with {pilot['checks']:,} recorded assertions. The separate full command without --pilot passed all {full['cases']} frozen cases, {full['checks']:,} recorded assertions, in {full['seconds']:.6f} seconds, within its explicit 900-second cap (under 30 minutes). Each completed full case was immediately written to out/BLOCK_PARTIAL.json. Final out/BLOCK_CERTIFICATES.json contains rational interval endpoints for residual, actual complete run cost and entropy in every case.

The full checker verifies truth tables by integer FWHT and exact physical edges, the exact spectral products/mu/I/v identities, conditional reciprocal identities, local elementary normalizers by independent subset enumeration, and the actual source subset/count costs. Irrational theta values are isolated by rational fifth-power bisection; logarithms use 24 atanh terms after reduction to 1<=y<=2 with remainder <=9/(196*3^49). All operations are rounded OUTWARD to the 2^-80 dyadic grid by exact signed integer floor/ceiling. Thus no floating-point entropy sign supplies a certificate. Histogram aggregation avoids repeating interval arithmetic for equal spectral masses; factorial log aggregation gives the exact uniform-subset rank expectation.

Earlier bounded checks are preserved honestly: v1 hit Python's integer-to-string limit while serializing a large rational; v2 had a stale equality check where outward interval containment was needed; v3 stopped at its 59-second pilot guard; v4 completed 11 mathematical cases but exceeded the pilot time cap. These are implementation/resource failures, not mathematical refutations. The checker changed to symbolic/histogram aggregation, an explicit small feasibility pilot and the originally frozen full domain under a separate bounded job. Exact partial cases remain evidence, but only v5's completed output is reported as the full passing certificate. Total recorded assertions across the completed review, v5 pilot and v5 full job are {total:,}; each saved counter excludes its final runtime assertion.

Commands from A008:

    python -X utf8 runs/{RID}/code/review_a006.py
    python -X utf8 runs/{RID}/code/check_blocks.py --pilot
    python -X utf8 runs/{RID}/code/check_blocks.py

## proof dependencies and changed downstream conclusions

Source dependencies: the baseline original conditioned forest interface, elementary symmetric normalizer and h2(v)<=2I estimate; finite entropy/Kraft principles, basic binomial identities and exact Boolean product expansion. A006's v1 is reviewed independently, not assumed for the new unequal-block proof. A007's new equal-width activation theorem is read for scope but not used as an accepted premise. A008 v1's accepted dictionary theorem is likewise not a premise for this ORIGINAL-queue result.

Changed conclusions: (1) the whole A006 statement has another locally saved independent acceptance; (2) the positive block side of the lead's single-gate tribes contrast now has a full all-width original-reference theorem; (3) gate names occur once, roots and zero-child costs are paid, and actual complete run accounting avoids an unnecessary generic multiset/child overhead. This stage follows the lead's review-first rule and produces one scoped continuation, not another broad universal candidate. Independent review and supervisor adoption remain separate events.

## one next mathematical action and independent reviewer

Next: replace the forced-owner/binomial block calculation by a joint posterior label-and-rank moment on the affine/projective line-DNF prime table, consuming A009/A014's existing line-incidence and disjoint-piece proofs. First estimate the expected once-per-used-line name/rank bill for actual source-SCC forests, rather than reoptimizing the already obstructed coordinatewise pressure. A006 can review the unique partition-run and actual probability ledger; A086 or A094 should independently reconstruct the all-width binomial payment and rational certificates. No messages were sent and no other agent's files were changed.

## actual persistence receipts or precise save blocker

The requested run contains REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, REVIEW_A006.md, READ_ONCE_DNF.tex, CODE_COST_LEDGER.json, DERIVATION_NOTES.md, frozen/refined compute specs, author-independent code and exact outputs. out/SOURCES.json pins actual reads; out/RECEIPTS.json records sizes and SHA256. All files are below 20 MB. STATUS.md, WORKLOG.md and LEARNED.md are current inside A008. Shared registries, Brain, git and other agent folders were not modified. Mirror verification, supervisor copying and independent acceptance of the new claim are unobserved, not claimed.

## Universal bridge

C020 whole-set witness cost, under the lead's PI-J target, moves by a complete all-width block-forest closure: residual <47I/10 and full original-queue entropy-reference cost <67I/5, with every gate-name/root/subset/zero-child charge retained; the whole A006 v1 chain is independently accepted at scope. Universally, overlapping prime implicants still lack the forced owner and conditional binomial laws used in this proof. NEXT asks for their joint posterior replacement on the live line-DNF test using existing incidence/orthogonal-piece inputs, so it attacks the unpaid universal name/rank term rather than adding another isolated FEI class result.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RID,'stream':'B02','packet_id':'A008','gap_id':'G-J-COST','attempt_id':'A008-block-forest-2','method':'whole A006 independent reconstruction, then exact unequal disjoint-clause original-queue ledger and binomial rank payment','mathematical_delta':'A006 v1 independently accepted without repair; every unequal read-once DNF has original residual <47I/10 and complete ideal entropy-reference cost <67I/5; 96 finite cases certified','deliverable_status':'COMPLETE_LOCALLY_SAVED','mathematical_status':'A006_REVIEW_HOLDS_RESTRICTED_BLOCK_FOREST_AUTHOR_PROVED_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':old['claim_id'],'version':1,'use':'independent review only, not premise for new theorem'}],'claims_created_or_changed':[old['claim_id']+'@1',new['claim_id']+'@1'],'source_artifacts':['REPORT.md','REVIEW_A006.md','READ_ONCE_DNF.tex','CODE_COST_LEDGER.json','FROZEN_SPEC.json','REFINEMENT_SPEC.json','out/REVIEW_A006_CHECK.json','out/BLOCK_CERTIFICATES.json','out/SOURCES.json','out/RECEIPTS.json'],'next_consumers':new['next_consumers'],'next_action':'Bound the joint once-per-used-line name/rank bill for actual source-SCC forests on line-DNF PI-J, consuming A009/A014 inputs; A006/A086/A094 review new all-width closure','stagnant_substantive_attempts':0,'blockers':['new theorem independent review pending','universal overlapping prime-table label/rank/subset payment open'],'packet_ids':['A008']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)
reads=[(base/'EXECUTION_PROTOCOL.json','complete protocol'),(forest,'full section; original queue conditioning/cost/normalizer'),(supp/'baseline'/'current-threshold-paper.tex','standard h2(v)<=2I source locator'),(author/'REPORT.md','whole original claim reconstruction'),(author/'CLAIMS.json','original source statement/hash'),(ROOT.parent/'A006'/'runs'/'20261011T231903Z-fleet05-A006-posterior-forest-optimization'/'AUDIT_A008.md','whole local independent acceptance of prior A008'),(ROOT.parent/'A086'/'runs'/'20261011T234041Z-fleet05-A086-joint-code-referee'/'JOINT_CODE_REVIEW.md','A008 whole independent review, scope guards'),(ROOT.parent/'A007'/'runs'/'20261011T234502Z-fleet05-A007-root-normalization'/'REPORT.md','activated equal-width scope and nonduplication'),(ROOT.parent.parent/'claude'/'B02'/'STREAM_NOTES.md','lead v2 review-first and all-readonce-DNF target'),(ROOT.parent.parent/'BOARD.md','stage-start observed snapshot 2026-10-12 01:00 UTC; current hash recorded at finalization')]
dump(RUN/'out'/'SOURCES.json',[{'path':str(p),'sha256':sha(p),'locator':loc} for p,loc in reads])
(ROOT/'STATUS.md').write_text(f'STATE: A008 stage 2 complete: A006 v1 independently accepted; all unequal read-once DNFs R<47I/10 and complete reference<67I/5; {total:,} exact assertions; new review pending; FEI OPEN.\nNEXT: A006/A086/A094 review original-queue block ledger; replace forced-owner/binomial laws with joint source-SCC label/rank payment on line-DNF PI-J using A009/A014 inputs.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now}: Stage {RID}, lead-directed review first. Reconstructed full A006 v1 from generic assignment/SCC/parent/attachment/chronological choices; HOLDS, no repair. Proved all unequal read-once DNF residual <47I/10 and original full entropy-reference <67I/5. Preserved serialization/check/time-cap failures; changed interval aggregation, passed bounded v5 pilot and 96-case full exact job ({full["seconds"]:.3f}s). {total:,} recorded completed-run assertions; files saved for independent review.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
Stage 2: A006 v1 whole claim HOLDS under independent generic source-SCC/parent/attachment/chronological trace enumeration; totals at m=1..5 are 3,11,37,143,681. Child permutations at shared attachments are real random-event multiplicities; abstract edge-list permutations are not. Actual complete costs still require h2(v) before an entropy inference.
Unequal read-once DNF in original PI-J queue: lambda_l=1, pi_l=2^-w_l, one order per disjoint clause. Forced owner => one finite partition forest, roots all touched blocks, zero children. mu_l=4p_l Q0 and I_l=2Q0 w_l p_l/q_l. Conditional on a selected coordinate, predecessor count is Bin(rank-1,1/2), giving expected rank <=1 bit per selected coordinate.
Keep original root normalizer D=product(1+p_l)-1: v log D+sum mu_l w_l<=(2+log2 e)I. Complete residual R<47I/10. Actual subset sizes/normalizers/weights and zero-child probabilities give C_pf<=(26/5+2log2 3+2log2 e)I; including h2(v) gives complete ideal reference<67I/5. This is coding payment on a known class, not a new FEI class. An optional binary-prefix rounding bit is not automatically O(I) for rare functions.
Outward interval arithmetic: compare independently enumerated exact polynomial endpoints for CONTAINMENT in a rounded DP interval, not equality. Large rational serialization can be avoided by exact dyadic outward rounding and factorial/histogram aggregation. Persist each exact case before the next one; distinguish mathematical assertions from resource-pilot success.
Universal gap: overlapping prime implicants need replacements for forced owners and conditional binomial rank law. A root cancellation or a coordinatewise fractional obstruction alone does not settle the complete joint posterior name/rank/subset bill.
''')
protocol=read(base/'EXECUTION_PROTOCOL.json')
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
for c in [old,new]:assert set(c)==set(protocol['required_per_run']['claim_fields'])
assert read(RUN/'PROGRESS.json')==read(RUN/'PACKET_DELTA.json')
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20_000_000
  receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
dump(RUN/'out'/'RECEIPTS.json',{'saved_at':now,'local_only':True,'files':receipts})
print(json.dumps({'persisted_files':len(receipts)+1,'recorded_assertions':total,'new_claim_sha256':hash_statement,'protocol_fields':'PASS','full_FEI':'OPEN','new_independent_review':'PENDING'},indent=2))
