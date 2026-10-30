from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy

RUN=Path(__file__).resolve().parents[1]; HOME=RUN.parents[1]; SHARED=HOME.parents[1]
BASE=Path('math-open-problems/reports/fei-2026-10-11')
SOURCE=SHARED/'agents/A008/runs/20261023T024024Z-fleet03-A008-gate-label-compression'
S15=SHARED/'agents/A015/runs/20261023T035924Z-fleet03-A015-minterm-barrier-analysis'
assert HOME.name=='A007'
def read(p):return p.read_text(encoding='utf-8')
def load(p):return json.loads(read(p))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s):
 assert p.resolve().is_relative_to(HOME.resolve())
 p.write_text(s,encoding='utf-8')
def save(p,obj):write(p,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
protocol=load(BASE/'EXECUTION_PROTOCOL.json')
main=load(RUN/'out/checks.json'); graph=load(RUN/'out/graph_audit.json'); pilot=load(RUN/'out/pilot.json')
for result,script in [(main,'check.py'),(graph,'graph_audit.py'),(pilot,'check.py')]:
 assert result['status']=='PASS' and result['source_sha256']==sha(RUN/'code'/script)
assert main['assertions']==20464 and graph['assertions']==97682
assert main['counts']['heterogeneous_orbits']==501 and graph['root_target_pairs']==96966
total=main['assertions']+graph['assertions']; assert total==118146
now=datetime.now(timezone.utc).isoformat()
sources=[BASE/'EXECUTION_PROTOCOL.json',SHARED/'BOARD.md',SHARED/'claude/B02/STREAM_NOTES.md',
 BASE/'source_material/reductions/paper/forests.tex',SOURCE/'CENTRAL_PAYMENT.md',SOURCE/'CLAIMS.json',
 SOURCE/'REPORT.md',SOURCE/'REVIEW_A007.md',S15/'REPORT.md',
 HOME/'runs/20261023T010805Z-fleet03-A007-root-normalization/CLAIMS.json']
save(RUN/'out/SOURCE_RECEIPTS.json',{'saved_utc':now,
 'note':'Source bytes at final save; mutable coordination hashes are not proof dependencies.',
 'sources':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sources]})

central=next(c for c in load(SOURCE/'CLAIMS.json') if c['claim_id']=='A008-CENTRAL-PRIME-COMPATIBLE-ROOT-AGGREGATION')
canonical=json.dumps({'statement':central['exact_statement'],'hypotheses':central['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False)
assert hashlib.sha256(canonical.encode('utf-8')).hexdigest()==central['statement_sha256']
review={'reviewer':'A007','role':'independent analytic reconstruction, no repair',
 'verdict':'HOLDS_FULL_STATED_SCOPE_WITH_EXPLICIT_THRESHOLD_BASELINE',
 'claim_version':central['claim_id']+'@1','statement_sha256':central['statement_sha256'],
 'evidence':str(RUN/'REVIEW_A008.md'),
 'scope':'Full original central queue statement, including optional wrapper; published threshold premise accepted, not newly audited as a whole paper'}
save(RUN/'out/review_A008.json',review)
central=copy.deepcopy(central)
central['proof_source']=[str(SOURCE/p) for p in central['proof_source']]+['REVIEW_A008.md']
central['review_records'].append(review)
central['status']='INDEPENDENTLY_REVIEWED_A007_AT_STATED_SCOPE'

stmt1=('For every finite nonempty gate table with the original conditioned queue, positive packing-feasible '
 'weights, root activities x_e=lambda_e*pi_e and D=prod_e(1+x_e)-1, let A be a nonempty covered target. '
 'Join coordinates of A when a gate contains both, partitioning A into components C_c. Let G_c be '
 'the gate names meeting C_c and D_c=prod_{e in G_c}(1+x_e)-1. Then the FULL output subprobability '
 'Q_*(A)<=prod_c D_c/D, including repeated and overlapping runs. If S_c=sum_{e in G_c}x_e<=pi<=1/2 '
 'for all k components, then Q_*(A)<=pi^(k-1)/(k(1-pi)^k). At pi=2^-r, '
 '-log2 Q_*(A)>=(k-1)r+log2 k+k log2(1-pi)>=(k-1)r-3k pi. '
 'An uncovered coordinate instead implies Q_*(A)=0. Children must attach through selected coordinates, '
 'and every successful visit selects a nonempty subset.')
stmt2=('For every integer w>=4, put r=2^w and choose any clause widths w_j in {w,w+1}. '
 'On disjoint blocks define f=2 product_{j=1}^r OR_{w_j}(X_j)-1. Its complete positive prime table '
 'consists of the width-r conjunctions choosing one positive variable per clause. For EVERY positive '
 'packing-feasible fixed reference on this table, and EVERY fixed choice of ordered covers, the '
 'original conditioned queue has full nonempty cross entropy C_*(f)/I(f)>r/7=2^w/7. '
 'This remains true after optimizing all actual partition-forest posteriors: their fully conditioned '
 'residual v log2 D+E_A[E_eta B_lambda-H(eta)] is at least C_*(f)-K_ref I(f). '
 'Meanwhile 1/4<Pr(f=1)<2/3, Var(f)>3/4, and H(f)<6I(f). Thus the universal fixed-positive-prime '
 'PI-J influence payment is false for the actual queue itself; full FEI and output-polarity-optimized '
 'or nonprime representations are not refuted.')
def claim(identifier,statement,hypotheses,proof,deps,refutes):
 return {'claim_id':identifier,'version':1,'exact_statement':statement,'hypotheses':hypotheses,
  'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A007'],
  'proof_source':proof,'proof_dependencies':deps,
  'review_records':[{'reviewer':'A007','role':'author proof audit, not independent-agent acceptance',
                    'verdict':'ANALYTIC_PROOF_AND_TWO_EXACT_REPRESENTATIONS_PASS',
                    'evidence':['out/checks.json','out/graph_audit.json']}],
  'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':refutes,
  'first_unproved_line':None,'next_consumers':['A008','A009','A010','A015','A086','A094','B02','B20']}
new=[claim('A007-ACTUAL-QUEUE-ROOT-COMPONENT-BARRIER',stmt1,
 ['Finite original gate table; nonempty targets','Actual root law with nonempty conditioning retained',
  'Nonempty successful subsets and child labels containing selected attachments',
  'Component activity upper bound needed only for its stated quantitative corollary'],
 ['ROOT_COMPONENTS.md','out/checks.json','out/graph_audit.json'],
 ['forests.tex eq:forestrootconstants, queue(i)-(iv), eq:forestconditioning; direct proof supplied'],[]),
 claim('A007-ALL-POSITIVE-PRIME-PIJ-QUEUE-OBSTRUCTION',stmt2,
 ['Uniform cube; w>=4 and r=2^w; any pattern of widths w or w+1',
  'Complete POSITIVE prime table of the stated f, fixed before spectral sampling',
  'All feasible positive lambda and all fixed ordered covers; costs in bits',
  'Polarity selection and nonprime gate representations are outside the refuted claim'],
 ['PRIME_QUEUE_OBSTRUCTION.md','ROOT_COMPONENTS.md','out/checks.json','out/graph_audit.json'],
 ['A007-ACTUAL-QUEUE-ROOT-COMPONENT-BARRIER@1',
  'forests.tex thm:posteriorforest run probability upper cost; Gibbs identity reconstructed',
  'Self-contained product Fourier and physical influence calculations, no assumed FEI bound'],
 ['B02 STREAM_NOTES.md v2 PI-J target: universal influence payment for the conditioned positive-prime posterior residual'])]
claims=[central]+new
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
save(RUN/'CLAIMS.json',claims)
next_action=('Test the root-component criterion simultaneously on both output polarities: '
 'construct an actual both-polarity obstruction, or prove an influence-paid polarity/representation '
 'selection lemma. Retain exact original D and complete output mass; do not further optimize the '
 'now-refuted fixed-positive-prime route. A008/A009/A015/A086/A094 independently reconstruct this obstruction.')
gap=('Full FEI remains OPEN. The original fixed-positive-prime PI-J route is locally refuted; '
 'a universal influence-paid code after polarity/representation selection remains unproved. '
 'New obstruction awaits independent-agent acceptance and canonical downstream adoption.')
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B02','packet_id':'A007',
 'gap_id':'G-J-COST','attempt_id':'A007-root-component-necessary-event-and-nonuniform-dual-tribes',
 'method':'Review-first consumption of A008 central theorem; universal necessary-root factorization with exact D; all-weight prime-table obstruction; product spectrum and independent queue reachability certificates',
 'mathematical_delta':'For near-balanced nonuniform dual tribes, EVERY original positive-prime reference and forest posterior has queue cost/I>2^w/7 although H/I<6. Root normalization refunds one rarity charge, not the remaining component charges. A008 central251I/5 independently HOLDS.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW_AND_SUPERVISOR_COPY',
 'mathematical_status':'LOCALLY_PROVED_PIJ_ROUTE_OBSTRUCTION; UNIVERSAL_COMPONENT_LEMMA; FULL_FEI_OPEN',
 'claim_versions_used':[central['claim_id']+'@1: independently reconstructed without repair; threshold premise explicit',
  'Original forests.tex queue and posterior theorem; necessary event proved directly'],
 'claims_created_or_changed':[c['claim_id']+'@1' for c in claims],
 'source_artifacts':['ROOT_COMPONENTS.md','PRIME_QUEUE_OBSTRUCTION.md','REVIEW_A008.md',
  'FROZEN_SPEC.json','FROZEN_SPEC_GRAPH.json','SPEC_NOTES.md','out/pilot.json','out/checks.json',
  'out/graph_audit.json','out/review_A008.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':['A008','A009','A010','A015','A086','A094','B02','B20'],
 'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':[gap,'Remote mirror copying and shared registry propagation are supervisor-owned and unobserved',
  'Brain self-care degraded: stale owner-model/state-of-mind sources; not used as mathematics'],
 'packet_ids':['A007']}
assert set(progress)=={f.split(' (')[0] for f in protocol['required_per_run']['progress_fields']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)

report=f'''# A007: original positive-prime queue obstruction

## exact target, quantifiers, hypotheses and units

Continue the 2026-10-23 05:38 UTC root-normalization packet toward full uniform-cube FEI, under execution protocol2026-10-11-execution-v2 and the owner's actual campaign deadline2026-10-23 14:49 UTC. The new universal component lemma and actual Boolean family are stated exactly in CLAIMS.json. All costs and entropy are in bits. The refuted target is the precise B02 PI-J fixed-POSITIVE-prime conditioned queue/posterior expression, not full FEI or unrestricted representation existence.

For every w>=4, r=2^w disjoint OR clauses have arbitrary widths w or w+1; f=2 product OR_j-1 has variance>3/4. EVERY feasible positive fractional prime reference and EVERY fixed ordered cover has full original queue cost C_*/I>2^w/7. Nevertheless H(f)<6I(f), proved directly. Distinct widths make the table nonuniform; the homogeneous endpoint is dual tribes. No weights are changed after seeing a Fourier set.

## sources actually read, revisions and theorem locators

Read fresh BOARD.md dated2026-10-23 05:35 UTC, B02 STREAM_NOTES.md v2, own STATUS/LEARNED and previous stage. A008 had already paid the previous central-band NEXT and independently accepted both prior A007 claims: read its20261023T024024Z CENTRAL_PAYMENT.md, REPORT.md, CLAIMS.json and REVIEW_A007.md in full. Read A01520261023T035924Z REPORT.md, which independently accepts central251I/5 and carries paid subprobabilities through histories. That history transport is not used as a root-payment premise here.

Re-read original forests.tex through the actual queue, eq:forestconditioning, partition-forest definition, thm:posteriorforest and its run-cost derivation. The shared campaign/paper baselines and complete protocol are inherited reads; final schema validation rereads the exact protocol. Threshold Theorem A is accepted only for the reviewed central claim, never used to prove the new obstruction or its H<6I check. Source hashes are in out/SOURCE_RECEIPTS.json. A bounded local obstruction/learning search found no corresponding entry in the checked files. One read-only math-store query with three wordings returned weak, unrelated matches and no implicant card; it supplied no proof premise or claim of priority.

## complete derivation or exact first unsupported line

ROOT_COMPONENTS.md proves the universal necessary event directly from queue semantics. In a successful finite run outputting A, every selected subset lies in A and every child attachment is in A and both gates. Thus descendant trees cannot cross the components formed by gates' intersections with A. The initial root set must hit every component's gate class and avoid gates disjoint from A. Summing the EXACT conditioned original product root law gives Q_*(A)<=product D_c/D, where D=product(1+lambda*pi)-1. This includes all actual repeated/overlapping runs and all output ambiguity.

If each component's total activity S_c<=pi<=1/2, finite-product expansion and the packing-row bound give Q_*(A)<=pi^(k-1)/[k(1-pi)^k]. In particular at pi=2^-r its cost is at least r(k-1)-3k pi. The NEGATIVE normalization term is retained in D and refunds one leading rarity charge. It cannot cancel the k-1 remaining charges.

PRIME_QUEUE_OBSTRUCTION.md classifies every actual positive prime of the named CNF: exactly one positive variable per clause, width r. For a Fourier set contained in one clause, the root components are its individual variables and S_i<=2^-r follows from the SAME physical packing row. All-reference name optimization, forest-posterior entropy refunds and rank choices cannot defeat an upper bound on the full output mass itself.

Let epsilon_j=2^-w_j, p_j=1-epsilon_j and P=product p_j. For nonempty A in clause j, exact product Fourier expansion gives fhat(A)^2=4epsilon_j^2(P/p_j)^2. Independent pivotal counting gives I_j=2w_j epsilon_j P/p_j. Summing the signed pointwise cost over these disjoint actual sectors yields C_*>=sum_j I_j(P/p_j)[r(1-2p_j/w_j)-3pi]. Other sectors have nonnegative cost. Since P/p_j>1/3 and w_j>=w>=4, C_*/I>r/6-pi>r/7. No orbit entropy, assumed FEI estimate or finite-to-infinite extrapolation is involved.

The same product spectrum gives a probability law mu with empty mass P and nonempty spectrum4P mu. Therefore H(f)=h2(v)+4P[H(mu)-h2(P)]. Each block contributes at most epsilon_j(2w_j+3/2) to H(mu), so H(f)<=1+(4+3/w)I(f)<6I(f), since I>w/4>=1. This confirms that the family is a coding-route obstruction, not an FEI counterexample.

Finally Gibbs' variational identity and the original forest run-cost bound imply v log D+K_ref I+E_A[E_eta B_lambda-H(eta)]>=C_* for EVERY forest posterior eta. Thus the fully conditioned PI-J residual divided by I is at least r/7-K_ref and is unbounded. No premise asserting that PI-J universally pays remains usable at its fixed-positive-prime scope. The first unsupported line toward full FEI is now a universal influence-paid code AFTER output-polarity or representation selection. Negating the homogeneous endpoint gives ordinary disjoint-block tribes, so the present argument does not refute that broader possibility.

REVIEW_A008.md independently reconstructs the entire central251I/5 theorem, including the optional wrapper, at unchanged source statement hash{central['statement_sha256']}. Verdict HOLDS without repair; its published threshold baseline remains explicit. This review is compatible with, and does not extend beyond, its symmetric-family scope.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json and FROZEN_SPEC_GRAPH.json precede their jobs. From this run directory, `python -X utf8 code/check.py --pilot` passed{pilot['assertions']} assertions in{pilot['seconds']:.3f}s. The full `python -X utf8 code/check.py` passed{main['assertions']} in{main['seconds']:.3f}s. It builds all three complete small Boolean tables, all signed prime faces of both output polarities, integer Walsh coefficients, physical influences and product-spectrum identities. It audits nine feasible family references plus one fixed general-graph guard, all454 output/component cases and2358 enumerated root sets. Its501 heterogeneous width-pattern parameter orbits use exact product moments and rational certificates, not exponentially large truth-table enumeration. The all-w/all-lambda theorem is proved analytically.

The separate `python -X utf8 code/graph_audit.py` passed{graph['assertions']} assertions in{graph['seconds']:.3f}s. It does not import the main checker. For six separately chosen references, all{graph['root_target_pairs']} root/target pairs are tested by maximal reachability through ACTUAL allowed child attachments. A target is reachable only when each root component is hit; direct root-set summation agrees exactly with the component-product expression. This attacks the possible loophole that extra visits, unassigned attachments or overlaps might connect separated target coordinates.

Total nonpilot assertions:{total}; the{pilot['assertions']} pilot checks overlap and are not added. Arithmetic is integer/Fraction; no tolerance or floating sign accepts any case. Explicit guards confirm that dropping root conditioning changes mass and that adding a nonprime full-support gate, or changing polarity, can merge components. SPEC_NOTES.md reconciles the graph spec's printed arithmetic typo134806 with its unchanged formula and actual96966 pairs, and distinguishes the fixed main guard from the nine searched family references. No domain, dimension or case selection was adaptively enlarged. The main code's nonzero domain counts and both landed script hashes are verified before accepting results.

Both jobs were estimated100MB and observed below55s; no >300MB job or memory-admission bypass occurred. No heavy build, compiler, GPU, detached worker or remote job was launched. Existing work was not stopped or throttled. Lean verification is not claimed. Mathematical conclusions rest on the displayed universal proofs plus exact finite checks, not the finite checks alone.

## proof dependencies and changed downstream conclusions

The universal component lemma uses only original queue/root semantics and finite product inequalities. The actual all-prime obstruction depends on that lemma and self-contained Boolean prime classification, product Fourier identities and physical influence counts. Its entropy upper bound does not borrow the entropy theorem being sought. The posterior consequence uses the source's per-run upper-cost inequality and Gibbs identity; the complete proof is in PRIME_QUEUE_OBSTRUCTION.md. Dependencies are acyclic.

A008's central theorem is independently reconstructed at its original hash and explicit threshold dependency, discharging review-first work before this mechanism change. The previous A007 thinning/retuning claims now have A008's independent acceptance; their statements are unchanged. No central-family, universal signed-normalizer or A015 supplied-reference transport theorem is refuted. The refuted statement is exactly B02's universal fixed-positive-prime PI-J payment. C020 with arbitrary representations and C024 transport of an already-paid reference remain open/conditional as before. Supervisor must mark consumers CONDITIONAL or blocked ONLY if they actually assume that universal positive-prime payment; class-specific reviewed payments remain valid. New claims are locally proved and await independent-agent review; no registry acceptance is manufactured.

## one next mathematical action and independent reviewer

{next_action} These are named on-disk review consumers, not a claim that a message was sent or review accepted. The strongest attempted escape is a child path through an off-target coordinate: that would output the off-target coordinate and cannot occur in an exact-A run. The second escape is polarity/nonprime selection; it is real, explicitly outside the refutation, and is NEXT rather than a hidden claim that all coding representations fail.

## actual persistence receipts or precise save blocker

The four exact-schema protocol files, both complete proofs, A008 independent review, frozen specs, accounting notes, scripts and exact outputs are saved in this run. PACKET_DELTA.json equals PROGRESS.json with packet_ids=[A007]. STATUS.md, WORKLOG.md and LEARNED.md are updated in A007 only. out/PERSISTENCE_RECEIPT.json records all landed hashes/byte counts and is reread after writing; no file reaches20MB. No shared index, source tree, other-agent folder, brain data, trading path, mail or git operation was modified/performed. The task-checklist lifecycle is separately recorded as directed by the session hook. Supervisor copying, mirror verification, independent acceptance and downstream adoption remain unobserved; this report does not count receipts as mathematical use.

Brain self-care is degraded/unverified: wake reported owner-model91.3h and state-of-mind75.9h stale. Personal-context freshness remains affected; no affected notes supply mathematical premises. Current explicit instructions and source-checked proofs govern. No other work was stopped and no task-owned calculation remains running after these completed jobs.

## Universal bridge

This stage moves C020/PI-J by deriving a universal actual-queue root-component barrier and locally refuting the precise fixed-positive-prime universal payment: even after ALL compatible-output and posterior entropy refunds, C_*/I>2^w/7 on near-balanced nonuniform dual tribes, while their actual H/I<6. The exact nonempty-root normalizer cancels only one rarity charge and is retained throughout. What remains is the broader FEI bridge: an influence-paid representation selected with polarity or nonprime gates, followed by already-available supplied-reference history transport. NEXT tests that exact escape against both component profiles; it is shorter than further optimizing an all-positive-prime reference that this proof rules out, or repeating an already-known threshold FEI class.
'''
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading+'\n' in report
write(RUN/'REPORT.md',report)
write(RUN/'CHECKPOINT.md',f'COMPLETE_LOCAL {now}\nUniversal root-component lemma and all-positive-prime PI-J queue obstruction proved locally;{total} nonpilot exact assertions PASS. A008 central claim independently HOLDS. Full FEI OPEN; new independent acceptance/mirror unobserved.\nNEXT: '+next_action+'\n')
write(HOME/'STATUS.md',f'STATE: A007 stage saved: ALL original positive-prime queue/posterior cost/I>2^w/7 on nonuniform dual tribes while H/I<6; exact D retained;{total} nonpilot checks PASS; A008 central HOLDS; new review pending; FEI OPEN.\nNEXT: '+next_action+'\n')
entry=f'\n## {now} | {RUN.name}\nConsumed A008 completion of prior central NEXT and independently reconstructed full251I/5 statement. Proved universal component-root necessary event, including repeated actual queue visits, and actual all-weight/all-order positive-prime PI-J obstruction on widths w or w+1, r=2^w. Cost/I>r/7 while H/I<6, variance>3/4. Exact D refunds one root rarity only; all posterior/output entropy refunds already included. {total} nonpilot checks plus{pilot["assertions"]} overlapping pilot PASS. Two independent representations: root-product/event enumeration and allowed-child reachability. No mathematical failure; fixed case-count typo reconciled in SPEC_NOTES. New claims pending independent review and supervisor copy; FEI OPEN. NEXT: {next_action}\n'
old=read(HOME/'WORKLOG.md')
if RUN.name not in old:write(HOME/'WORKLOG.md',old+entry)
lesson=f'''\n## {RUN.name}: actual root components refute fixed-positive-prime PI-J

For target A, join its coordinates when a gate contains both. Every successful original queue tree stays in one component because all selected subsets lie in A and child attachments are selected coordinates. Thus every component needs an initial root. With gate classes G_c, exact conditioned output mass Q_*(A)<=product_c[product_(e in G_c)(1+lambda_e*pi_e)-1]/[product_e(1+lambda_e*pi_e)-1]. This controls the FULL sampler, including repeats and overlaps, so posterior/witness entropy cannot evade it.

If each component activity S_c<=pi<=1/2, then Q_*(A)<=pi^(k-1)/[k(1-pi)^k]. At pi=2^-r the bit cost is >=r(k-1)-3k pi. Keep D: it refunds one leading root-rarity term, not k terms.

For f=2 product_j OR_(w_j)-1, positive primes choose one variable per clause (width r). Any one-clause Fourier set needs one root per coordinate; each component activity<=2^-r by its physical packing row. At r=2^w, ANY widths w_j in {{w,w+1}}, w>=4, EVERY fixed feasible positive-prime reference and ordered cover satisfies full C_*/I>2^w/7, yet variance>3/4 and actual H/I<6 by a direct product-spectrum calculation. Thus fixed-positive-prime universal PI-J is locally refuted at the actual output law, not merely an outer fractional bound. The conditioned forest residual is >=C_*-K_ref I even after all posterior entropy refunds. Independent acceptance pending.

Do not propagate this to full FEI, polarity selection or nonprime regular-gate representations. The homogeneous example is ordinary tribes after sign/coordinate negation; polarity is a genuine escape. NEXT is simultaneous positive/negative component-profile testing, not further lambda optimization of a uniformly refuted route. A008 central251I/5 independently HOLDS at unchanged scope and its explicit threshold premise; its6H/5 comparison is not universal absorption. Spec-count corrections must retain the unchanged domain/formula and actual nonzero receipt, as recorded here.\n'''
old=read(HOME/'LEARNED.md')
if RUN.name not in old:write(HOME/'LEARNED.md',old+lesson)
assert load(RUN/'PROGRESS.json')==load(RUN/'PACKET_DELTA.json')
assert len(read(HOME/'STATUS.md').splitlines())==2
files=sorted(p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json')
assert all(p.stat().st_size<20_000_000 for p in files)
receipt={'saved_utc':now,'run_id':RUN.name,'schema_validation':'PASS','nonpilot_exact_assertions':total,
 'new_independent_review':'PENDING','mirror_verification':'UNOBSERVED','full_FEI':'OPEN',
 'files':[{'relative_path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],
 'rolling_files':[{'path':str(HOME/n),'sha256':sha(HOME/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]}
save(RUN/'out/PERSISTENCE_RECEIPT.json',receipt)
assert load(RUN/'out/PERSISTENCE_RECEIPT.json')==receipt
print(json.dumps({'saved':str(RUN),'nonpilot_assertions':total,'schema':'PASS',
 'files':len(files)+1,'largest_file_bytes':max(p.stat().st_size for p in files)}))
