from pathlib import Path
import json, hashlib, copy, datetime
from dependency_check import validate, statement_hash, key
R=Path(__file__).resolve().parents[1];OWN=R.parents[1];TEAM=OWN.parents[1]
PREV=OWN/'runs/20261014T013521Z-account05-A081-dependency-certificates'
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
pp=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json');proto=load(pp)
g=load(PREV/'PROOF_DEPENDENCIES.json');g['run_id']=R.name;nodes=g['nodes'];sources=g['sources'];units=nodes[0]['units'];hashes=[]
snap=R/'out/source_snapshots';snap.mkdir(exist_ok=True)
def pin(sid,p,loc='Exact observed source bytes'):
    p=Path(p);raw=p.read_bytes();out=snap/(sid+p.suffix);out.write_bytes(raw)
    sources[sid]={'local_path':str(out),'original_local_path':str(p),'local_sha256':hashlib.sha256(raw).hexdigest(),'locator':loc,'pin_scope':'Immutable observed bytes; no upstream mutation'}
def find(cid):return next(n for n in nodes if n['claim_id']==cid)
def edge(cid,why):
    n=find(cid);return {'claim_key':key(n),'statement_sha256':n['statement_sha256'],'hypothesis_instantiation':why,'unit_conversion':None}
def node(cid,s,h,status,sid,loc,deps=(),evidence=(),first=None):
    n={'claim_id':cid,'version':1,'exact_statement':s,'hypotheses':h,'statement_sha256':statement_hash(s,h),'units':units,'status':status,'proof_sources':[{'source_id':sid,'locator':loc}],'proof_dependencies':list(deps),'evidence':list(evidence),'first_unproved_line':first};nodes.append(n);return n
def intake(c,status,sid,loc,deps=(),evidence=(),first=None):
    canonical=statement_hash(c['exact_statement'],c['hypotheses']);only=hashlib.sha256(c['exact_statement'].encode()).hexdigest();exkey=hashlib.sha256(json.dumps({'exact_statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    types={canonical:'canonical statement+hypotheses',only:'statement-only UTF8',exkey:'canonical exact_statement+hypotheses'};assert c['statement_sha256'] in types
    receipt={'claim_key':key(c),'source_recorded_hash':c['statement_sha256'],'source_hash_type':types[c['statement_sha256']],'internal_canonical_hash':canonical,'exact_literal_content_preserved':True};hashes.append(receipt)
    n=node(c['claim_id'],c['exact_statement'],c['hypotheses'],status,sid,loc,deps,evidence,first);n['source_hash_receipt']=receipt;n['source_declared_dependencies']=copy.deepcopy(c.get('proof_dependencies',[]));return n
A090=TEAM/'agents/A090/runs/20261014T034626Z-account05-A090-independent-reconstruction'
A001=TEAM/'agents/A001/runs/20261014T035113Z-account05-A001-quantifier-audit'
for a,p in [('A090',A090),('A001',A001)]:
    for f in ['CLAIMS.json','DERIVATION.md']:pin(a+'_s5_'+Path(f).stem,p/f)
for sid,p in [('board_s5',TEAM/'BOARD.md'),('B17_notes_s5',TEAM/'claude/B17/STREAM_NOTES.md'),('protocol_s5',pp),('stage4_graph',PREV/'PROOF_DEPENDENCIES.json'),('A081_review_s5',R/'REVIEW.md'),('A081_exact_s5',R/'out/EXACT_SIGNED_PARTITION.json'),('A081_helper_s5',R/'code/check_signed_partition.py'),('A081_spec_s5',R/'out/FROZEN_SPEC.json')]:pin(sid,p)
c=load(A090/'CLAIMS.json')[0]
ev=[{'reviewer':'A081','verdict':'HOLDS_AT_ENTIRE_ORIGINAL_STATED_SCOPE','source_id':'A081_review_s5','validation_source_id':'A081_exact_s5','substantive_source_repair':False,'independence':'Direct physical character sums and conditional-law likelihood reconstruction; source helper not reused'}]
signed=intake(c,'IMPORTED_ACCEPTED','A090_s5_CLAIMS','Original entire arbitrary-gate statement; independently reconstructed REVIEW sections 1-2',[edge('A081-COARSENING-REFUND-CONTRACT','Instantiate complete KL chain with signed core/residual gate mask partition; derive physical bent coefficients and aggregate reserve independently')],ev)
signed['reserve_contract']={'owner':'single physical core coordinate y_1','fraction':'1/4','allowed_charges':['sum of gate-mask quotient losses'],'charged_items':['sum of gate-mask quotient losses'],'capacity_evidence':'Dedicated local bound only','claims_positive_child_slack':False,'terminal_gate_mask_payment':'UNRESOLVED','complete_reference':True}
pending=next(c for c in load(A001/'CLAIMS.json') if c['claim_id']=='A001-SHARED-CORE-FOUR-CELL-OWNERSHIP')
intake(pending,'PENDING_INDEPENDENT_RECONSTRUCTION','A001_s5_CLAIMS','Preserve full author root-ledger scope and explicit nonhereditary restriction; no theorem premise imported',first='Full independent reconstruction of the shared-core four-cell root ledger is queued; even acceptance would not certify an unused child reserve.')
capacity=node('A081-LOCAL-RESERVE-DOES-NOT-CERTIFY-CHILD-SLACK','There exists an actual six-bit bent-core point-edit Boolean sign F with d=4 and gate positive exactly on 0,1,2, split on physical y_1, whose children have influences 21/16 and 2. Complete leaf subprobability references Q_l=P_l 2^(H_l-12 I_l) are positive on true support and satisfy CE_l=12 I_l, so their unused child surpluses are both zero. Each gate-mask quotient loss is strictly positive; row 1 has L=(1/64)log2(31)-(5/256)log2(5)-(3/512)log2(41). Yet the A090 bound sum L_i<=Inf_(y_1)(F)/4 holds with Inf_(y_1)=17/32. Thus child CE<=C I alone does not certify any positive unused child capacity to pay these quotient losses. This does not rule out better chosen references or the existing terminal KL correction.',['Actual six-bit sign and physical y_1 split; information in bits','Complete leaf subprobability laws are allowed, fixed before spectral sampling, and positive on true support','Unused child surplus means C I(f_l)-CE(P_l,Q_l), not D(P_l||Q_l) or a different signed correction'],'IMPORTED_CERTIFIED','A081_review_s5','Section 3 exact actual-function insufficiency witness',[edge(signed['claim_id'],'d=4, r=2 gate with coefficients a_empty=a_i=1/2; conditional laws unequal, dedicated quarter bound holds'),edge('A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER','Only its complete subprobability leaf-reference hypotheses; no unproved payment consequence invoked')],[{'reviewer':'A081','verdict':'EXACT_LOCAL_CERTIFICATE','source_id':'A081_review_s5','validation_source_id':'A081_exact_s5','scope':'Insufficiency of inferring positive child CE slack; not a universal payment obstruction'}])
false=node('PROPOSED-LOCAL-RESERVE-IMPLIES-CHILD-SLACK','For every actual Boolean tree node with the A090 local dedicated quotient-loss bound and complete child references satisfying CE_l<=C I(f_l), the reach-weighted unused child surplus is at least the positive combined quotient loss.',['Complete subprobability references positive on true support','Unused child surplus is C I(f_l)-CE_l; same fixed C at both children','No separate available-capacity receipt or joint debit hypothesis'],'REFUTED','A081_review_s5','Section 3 zero-surplus actual-function witness',[edge(capacity['claim_id'],'Both child surpluses zero, quotient losses strictly positive')],first='False for C=12 and the explicit actual six-bit sign; no accepted source made this prospective implication.')
g['prior_change_receipts_stage4']=g['change_receipts'];g['change_receipts']={'prior_run':PREV.name,'prior_graph_sha256':hashlib.sha256((PREV/'PROOF_DEPENDENCIES.json').read_bytes()).hexdigest(),'independent_review_closed':key(signed),'new_capacity_test':key(capacity),'pending_root_ledger':key(find(pending['claim_id'])),'universal_constant_change':None,'rejected_inference':key(false)}
g['rejected_proof_attempts'].append({'attempt':'Convert a dedicated local influence bound into unused child CE slack without a capacity receipt','refuted_claim_key':key(false),'scope':'Prospective implication only; A090 scoped theorem and A097 transfer remain accepted; better reference choices and terminal KL correction remain available.'})
def contracts(h):
    errors=[]
    for n in h['nodes']:
        z=n.get('information_contract')
        if z:
            if z.get('complete_reference') is not True:errors.append('INCOMPLETE_REFERENCE:'+key(n))
            if not z.get('partition_declared'):errors.append('UNDECLARED_PARTITION:'+key(n))
            if not z.get('conditional_refund'):errors.append('LOST_CONDITIONAL_REFUND:'+key(n))
            if z.get('reference_only_cells')!='retained':errors.append('REFERENCE_MASS_RESET:'+key(n))
            if z.get('spectator_influence_reuse') is not False:errors.append('SPECTATOR_INFLUENCE_REUSE:'+key(n))
        z=n.get('reserve_contract')
        if z:
            if z.get('charged_items')!=z.get('allowed_charges'):errors.append('RESERVE_REUSE:'+key(n))
            if z.get('claims_positive_child_slack') is not False:errors.append('UNPROVED_CHILD_CAPACITY:'+key(n))
            if z.get('capacity_evidence')!='Dedicated local bound only':errors.append('ROOT_BOUND_PROMOTED_TO_CAPACITY:'+key(n))
            if z.get('terminal_gate_mask_payment')!='UNRESOLVED':errors.append('UNPAID_TERMINAL_MASK:'+key(n))
            if z.get('complete_reference') is not True:errors.append('INCOMPLETE_REFERENCE:'+key(n))
    return errors
save(R/'PROOF_DEPENDENCIES.json',g);save(R/'out/HASH_RECEIPTS.json',hashes)
v=validate(g);assert v['status']=='STRUCTURALLY_VALID' and not contracts(g);save(R/'out/GRAPH_VALIDATION.json',v)
fixtures=[]
def ng(h,cid):return next(n for n in h['nodes'] if n['claim_id']==cid)
def reject(label,mut,prefix):
    h=copy.deepcopy(g);mut(h);errors=validate(h,check_files=False)['errors']+contracts(h);hits=[x for x in errors if x.startswith(prefix)];assert hits,(label,errors);fixtures.append({'fixture':label,'PASS':True,'rejection':hits})
reject('Cycle through final FEI and signed lemma',lambda h:(ng(h,'FEI-FINAL')['proof_dependencies'].append(edge(signed['claim_id'],'Forbidden cycle')),ng(h,signed['claim_id'])['proof_dependencies'].append(edge('FEI-FINAL','Forbidden cycle'))),'CYCLE_THROUGH_FINAL_FEI:')
reject('Accepted lemma borrows isolated refuted capacity leaf',lambda h:(ng(h,false['claim_id'])['proof_dependencies'].clear(),ng(h,signed['claim_id'])['proof_dependencies'].append(edge(false['claim_id'],'Forbidden prospective payment'))),'ACCEPTED_DEPENDS_ON_UNRESOLVED:')
reject('Changed exact gate hypotheses',lambda h:ng(h,signed['claim_id'])['hypotheses'].append('All non-flat Boolean cores'),'STATEMENT_HASH:')
reject('Wrong source hash alias on proof edge',lambda h:ng(h,capacity['claim_id'])['proof_dependencies'][0].update(statement_sha256=c['statement_sha256']),'DEPENDENCY_HASH:')
reject('Final FEI in route premises',lambda h:h['candidate_routes'][-1]['requires'].append(h['final_claim']),'ROUTE_ASSUMES_CONCLUSION:')
reject('Borrow dedicated quarter for terminal CE',lambda h:ng(h,signed['claim_id'])['reserve_contract']['charged_items'].append('terminal CE'),'RESERVE_REUSE:')
reject('Assume positive unused child slack',lambda h:ng(h,signed['claim_id'])['reserve_contract'].update(claims_positive_child_slack=True),'UNPROVED_CHILD_CAPACITY:')
reject('Promote a root bill to hereditary capacity',lambda h:ng(h,signed['claim_id'])['reserve_contract'].update(capacity_evidence='Root ledger bound'),'ROOT_BOUND_PROMOTED_TO_CAPACITY:')
reject('Erase retained gate-mask debt',lambda h:ng(h,signed['claim_id'])['reserve_contract'].update(terminal_gate_mask_payment='PAID'),'UNPAID_TERMINAL_MASK:')
reject('Drop reference-only mass',lambda h:ng(h,'A081-COARSENING-REFUND-CONTRACT')['information_contract'].update(reference_only_cells='deleted'),'REFERENCE_MASS_RESET:')
save(R/'out/MUTATION_AUDIT.json',{'status':'PASS','fixtures':fixtures,'scope':'Structural and declared ledger-contract tests; mathematical inference validity is not automated'})
save(R/'out/REFUTATION_DELTA.json',{'false_exact_version':key(false),'actual_witness':key(capacity),'accepted_dependents':[],'effect':'No accepted A090/A097 theorem refuted; reference choice/joint payment remain open','propagation_owner':'B20; no external adoption claimed'})
exact=load(R/'out/EXACT_SIGNED_PARTITION.json');N=len(nodes);S=len(sources);A=sum(n['status'] in ['IMPORTED_ACCEPTED','IMPORTED_CERTIFIED'] for n in nodes);routes=len(g['candidate_routes'])
reviewed=copy.deepcopy(c);reviewed['status']='INDEPENDENTLY_ACCEPTED_AT_ENTIRE_STATED_SCOPE_BY_A081';reviewed['review_records'].append({'reviewer':'A081','timestamp':now,'verdict':'ACCEPT_AT_ENTIRE_ORIGINAL_STATED_SCOPE','method':'Independent likelihood/physical-edge proof and direct-character exact certificate','proof_source':str(R/'REVIEW.md'),'validation_source':str(R/'out/EXACT_SIGNED_PARTITION.json'),'reviewer_contributed_repair':False})
def own(n):return {'claim_id':n['claim_id'],'version':n['version'],'exact_statement':n['exact_statement'],'hypotheses':n['hypotheses'],'statement_sha256':n['statement_sha256'],'contributors':['A081'],'proof_source':{'path':str(R/'REVIEW.md'),'locator':'Section 3','validation':str(R/'out/EXACT_SIGNED_PARTITION.json')},'proof_dependencies':n['proof_dependencies'],'review_records':[],'status':'EXACT_LOCAL_LEDGER_TEST_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[key(false)],'first_unproved_line':None,'next_consumers':['A090','A001','A096','A097','A099','A094','A085','B20']}
claims=[reviewed,own(capacity)]
cert_s=f'A081 stage-5 dependency certificate has {N} exact nodes and {S} source byte pins, an acyclic graph, and {routes} FEI routes with unresolved leaves. It independently accepts A090 arbitrary-gate signed refund partition v1 at its entire original scope, retains its single dedicated quarter-core reserve, and certifies an actual six-bit zero-child-slack witness separating local loss bounds from available child capacity. It passes {exact["assertions"]} exact checks and ten declared ledger/graph rejection fixtures. Full FEI remains OPEN; no universal constant or non-flat terminal payment is obtained.'
cert_h=['Exact source versions, canonical internal statement hashes and immutable source pins','All-dimensional review is analytic; finite checks are corroboration','Structural and ledger declaration checks do not automate inference validity; integrated review remains pending']
claims.append({'claim_id':'A081-VERSIONED-DEPENDENCY-CERTIFICATE','version':5,'exact_statement':cert_s,'hypotheses':cert_h,'statement_sha256':statement_hash(cert_s,cert_h),'contributors':['A081'],'proof_source':{'path':str(R/'PROOF_DEPENDENCIES.json'),'files':['REVIEW.md','out/GRAPH_VALIDATION.json','out/MUTATION_AUDIT.json']},'proof_dependencies':[edge(signed['claim_id'],'Entire independent review'),edge(capacity['claim_id'],'Exact local capacity test')],'review_records':[],'status':'EXACTLY_VALIDATED_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[{'claim_id':'A081-VERSIONED-DEPENDENCY-CERTIFICATE','version':4}],'refutes':[],'first_unproved_line':None,'next_consumers':['A085','A094','B20']})
for x in claims:assert set(x)==set(proto['required_per_run']['claim_fields'])
save(R/'CLAIMS.json',claims)
next_action='Consume a source-complete non-flat conditional terminal reference construction that jointly pays retained gate/core mask CE and quotient loss, with an explicit available child-surplus receipt or conserved terminal-KL debit; independently review with A094, alternate A085.'
progress={'protocol_revision':proto['revision'],'run_id':R.name,'stream':'B17','packet_id':'A081','gap_id':'G-C018-TERMINAL-KL-PAYMENT','attempt_id':'A081-stage5-signed-partition-and-reserve-availability','method':'Independent entire arbitrary-gate analytic proof; direct character/rational prime-log checks; actual zero-unused-child-capacity witness and versioned dependency guards','mathematical_delta':'A090 signed arbitrary-gate partition independently accepted: full sign+mask KL retained; all mask-only losses fit one dedicated quarter-core influence. Actual six-bit complete child references have zero CE surplus despite positive quotient loss, so local/root quota does not certify available terminal child capacity.','deliverable_status':'LOCAL_COMPLETE; SOURCE_BOUND_REVIEW_AND_CAPACITY_TEST_SAVED','mathematical_status':'SCOPED_SIGNED_PARTITION_ACCEPTED; UNIVERSAL_COMPLETE_KL_AND_TERMINAL_PAYMENT_OPEN; FULL_FEI_OPEN','claim_versions_used':[key(signed),key(capacity),'A081-COARSENING-REFUND-CONTRACT@1','A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER@1',key(find(pending['claim_id']))],'claims_created_or_changed':[key(x) for x in claims],'source_artifacts':['PROOF_DEPENDENCIES.json','REVIEW.md','out/EXACT_SIGNED_PARTITION.json','out/FROZEN_SPEC.json','out/HASH_RECEIPTS.json','out/MUTATION_AUDIT.json','out/REFUTATION_DELTA.json','out/source_snapshots/'],'next_consumers':['A090','A001','A096','A097','A099','A094','A085','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Complete normalized universal terminal Gamma-D payment remains open.','Dedicated quarter-core loss bound does not prove available child CE slack or a joint debit.','A001 shared-core four-cell root theorem remains pending independent reconstruction and supplies no hereditary reserve even if accepted.','Local negative ledger test and integrated certificate need independent review.'],'packet_ids':['A081']}
assert set(progress)=={x if not x.startswith('packet_ids (') else 'packet_ids' for x in proto['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A081/B17 dependency certificates, stage 5. Independently review A090's entire arbitrary-gate signed refund partition and determine whether its dedicated local reserve establishes available child capacity for a terminal-tree payment. Uniform finite actual Boolean signs; d even >=4; arbitrary finite gates on disjoint physical bits. Information/KL in bits; influence is physical pivotal probability. Preserve exact statement versions, complete references, source pins, unresolved leaves and reject any proof cycle through final FEI.

# sources actually read, revisions and theorem locators

Read BOARD dated 2026-10-14 04:19 UTC, B17 STREAM_NOTES v2, own STATUS and stage-4 certificate, and the full execution protocol {proto['revision']}. B17's original six-claim/Maassen-Uffink assignment was completed earlier; protocol dispatch consumes a new useful dependency. A090 20261014T034626Z CLAIMS and DERIVATION: signed conditional partition, exact empty-mask loss, aggregate Parseval reserve, first unreconstructed universal implication. A001 20261014T035113Z CLAIMS and DERIVATION: shared-core four-cell root ledger and explicit nonhereditary scope. A096's new ownership CLAIMS and BOARD frontier were read for orientation but no new A096 theorem is independently accepted or used. Prior A097 complete leaf transfer statement was inspected for its subprobability hypothesis. All premises actually used are source pinned; source hash conventions are typed in out/HASH_RECEIPTS. Earlier accepted threshold/percolation and literature pins remain unchanged; no new literature-priority assertion enters.

# complete derivation or exact first unsupported line

REVIEW.md sections 1-2 independently reconstruct the entire A090-ARBITRARY-GATE-SIGNED-REFUND-PARTITION@1 without repair. Physical character expansion gives its exact coefficients and row laws. Keeping residual gate mask and bent Fourier sign preserves full normalized KL; deleting sign loses precisely delta a_i^2 D0_i. Conditional likelihood <=4 gives 0<=D0_i<=2. First-level Parseval gives sum_i L_i<=2delta, independent of gate dimension. The physical core influence is 1/2+delta(1-a_empty); hence all losses fit one dedicated quarter of y_1 influence. No residual-mask complexity or universal non-flat payment is established.

REVIEW section 3 certifies a precise missing-capacity implication. An actual six-bit d=4/AND-sign point-edit split on y_1 has child influences 21/16 and 2. Complete subprobability references Q_l=P_l 2^(H_l-12 I_l) satisfy CE_l=12 I_l exactly and have zero unused child CE surplus. Each gate quotient loss is strictly positive; row 1 is (1/64)log2(31)-(5/256)log2(5)-(3/512)log2(41). Thus a dedicated local bound and child CE<=CI do not alone prove any available positive child surplus. This prospective implication is refuted, not any accepted A090/A097 theorem, existential better-reference construction, or terminal KL correction.

The first unsupported universal line remains sum_i e_i D(mu_i||r_i)>=sum_i e_i log2(1/e_i)-K I(f) for a finite K and every actual Boolean sign. Complete references and the residual gate/core mask remain. A joint terminal payment or explicit available-capacity receipt is required before the same physical owner can be used in a full tree.

# executed validation with domain, arithmetic, commands and outputs

Frozen before jobs: core d in {{4,6}}, every r=1,2 gate, four named r=3 gates. Exactly 48 actual functions, all physical spectra and gate coordinates; no symmetry or dimension escalation. Direct integer character sums and physical edge counts; Fraction normalization/bounds; exact rational prime-log KL coefficient identities. Pilot d=4/r=2/positive gate mask7: 171 assertions PASS. Full: {exact['assertions']} assertions PASS, 76 relevant gate rows, 56 nonzero exact quotient losses, runtime {exact['runtime_seconds']:.3f}s. The general proof is analytic, not an extrapolation. Strict positive fixture loss uses unequal normalized laws and the KL equality case, not floating point.

Executed from A081:

    python -X utf8 runs\\{R.name}\\code\\check_signed_partition.py --pilot
    python -X utf8 runs\\{R.name}\\code\\check_signed_partition.py
    python -X utf8 runs\\{R.name}\\code\\finish.py

Memory estimate 64 MB, frozen maximum runtime60 seconds, observed full helper under one second. No >300 MB job, GPU or background process. Ten mutations reject final-FEI cycle, unresolved refuted capacity premise, expanded core hypotheses, wrong hash alias, FEI as route premise, quarter-reserve reuse, assumed child slack, root quota promoted to hereditary capacity, erased terminal-mask debt and dropped reference-only mass. These are declaration and structural checks, not an inference prover.

# proof dependencies and changed downstream conclusions

Graph: {N} exact nodes, {S} source byte pins, {A} admitted scoped nodes, no cycle; all {routes} FEI routes retain unresolved leaves. Original A090 statement/hypotheses/hash are preserved in CLAIMS; a typed receipt connects its source hash to the internal canonical graph hash. Its independent review depends on the already-certified complete KL partition chain, not on an unpaid universal bound.

The actual capacity witness depends only on A090's scoped family and A097's allowed complete subprobability leaf-reference hypothesis. The false prospective implication has no accepted dependent versions. Its refutation delta does not mark A090, A097, A096 or A099 false. A001's exact new root-ledger statement is imported pending full independent reconstruction; a root bound is not silently upgraded to unused child capacity. Existing degree-only and parity-tail obstructions, all complete terminal references and prior reviewed claims survive unchanged.

# one next mathematical action and independent reviewer

{next_action} A001/A096/A097/A099 are the mathematical consumers. A090's full new claim now has one independent complete acceptance. A094 (alternate A085) should review the local capacity test and integrated certificate. Canonical adoption, a second integrated review and downstream use are not claimed.

# actual persistence receipts or precise save blocker

Saved the four protocol files with exact fields and byte-identical PACKET_DELTA packet_ids=[A081], code/out, frozen spec, pilot/full checks, analytic REVIEW, graph, source snapshots, hash receipts and ten rejection fixtures. STATUS remains two lines; WORKLOG appended and LEARNED updated. out/PERSISTENCE_RECEIPTS contains actual file byte hashes; FINAL_VALIDATION checks fields, graph, unresolved routes, file sizes and report ending. All files <20 MB. No local save blocker; supervisor copying, remote mirrors, external adoption and integrated review remain unobserved. Finalized {now}.

# Universal bridge

This stage moves C018 complete-terminal-KL payment and C019/C024 reference-history compatibility by independently closing A090's arbitrary-gate signed partition: all discarded-sign losses fit a single quarter-core reserve, while retaining the sign preserves full KL exactly. It adds an actual zero-child-CE-surplus certificate showing why that local quota cannot become an available terminal reserve without a separate receipt. The universal constant improvement is zero: arbitrary non-flat core/refund, retained terminal mask CE and their joint nonoverlapping payment remain unpaid. NEXT seeks one source-complete conditional reference and joint debit with available-capacity evidence, the shortest route to full FEI because it attacks the exact missing terminal payment rather than closing another isolated class.
'''
assert all('# '+s+'\n' in report for s in proto['required_per_run']['report_fields'])
(R/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text(f'STATE: A081 stage 5 complete: A090 arbitrary-gate signed refund partition independently HOLDS; {exact["assertions"]} exact checks/10 ledger guards PASS; zero-child-slack witness saved; {routes} routes conditional; FEI OPEN.\nNEXT: Audit a non-flat complete terminal reference with joint retained-mask/quotient payment and explicit available child surplus or conserved KL debit; A094/A085 independent review.\n',encoding='utf-8')
if R.name not in (OWN/'WORKLOG.md').read_text(encoding='utf-8'):
    with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n[{now}] {R.name}: independent full A090 arbitrary-gate signed partition acceptance without repair; 48 actual functions/76 rows/{exact["assertions"]} exact checks, {exact["runtime_seconds"]:.3f}s. Aggregate losses fit one dedicated quarter-core influence. Actual six-bit child refs saturate C=12 CE budgets while loss remains positive, refuting only prospective quota-to-unused-slack inference. {N} nodes/{S} source pins/{routes} conditional routes; ten declaration guards PASS. A001 four-cell root ledger pending; universal terminal joint payment OPEN.\n')
if 'Stage 5 reserve-availability facts:' not in (OWN/'LEARNED.md').read_text(encoding='utf-8'):
    with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage 5 reserve-availability facts: A090 arbitrary-gate signed refund partition v1 independently accepted at entire original scope. Keeping gate residual mask plus bent Fourier sign preserves full KL; mask-only loss delta a_i^2 D0_i with 0<=D0_i<=2; first-level Parseval bounds aggregate by2delta<=one dedicated quarter-core influence, without a gate-dimension factor. This pays only quotient loss, not residual terminal CE. Actual d4/AND2 point edit split on y1 has child I=21/16,2 and core I=17/32. Complete subprobability Q_l=P_l*2^(H_l-12I_l) exhaust child CE budgets, leaving zero child surplus although quotient loss is positive. Hence CE<=CI plus a local/root quota is not an available-capacity receipt. This does not forbid better references or use of an explicitly conserved terminal KL correction.\n')
files=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or '__pycache__' in str(p) or p.name in ['PERSISTENCE_RECEIPTS.json','FINAL_VALIDATION.json']:continue
    raw=p.read_bytes();assert len(raw)<20*1024*1024;files.append({'path':str(p.relative_to(R)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save(R/'out/PERSISTENCE_RECEIPTS.json',{'saved_at':now,'files':files,'rolling':[{'path':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [OWN/'STATUS.md',OWN/'WORKLOG.md',OWN/'LEARNED.md']]})
assert len((OWN/'STATUS.md').read_text().splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all(not x['eligible_for_mathematical_review'] for x in v['candidate_routes'])
assert len(fixtures)==10 and report.rstrip().split('# Universal bridge\n')[-1].startswith('\nThis stage moves C018')
for f in files:assert hashlib.sha256((R/f['path']).read_bytes()).hexdigest()==f['sha256']
final={'status':'PASS','nodes':N,'source_pins':S,'admitted_scoped_nodes':A,'graph_acyclic':True,'conditional_FEI_routes':routes,'exact_assertions':exact['assertions'],'mutation_fixtures':len(fixtures),'all_routes_have_unresolved_leaves':True,'protocol_fields_exact_with_packet_ids_annotation_normalized':True,'delta_identical':True,'report_ends_with_universal_bridge':True,'file_hashes_readback_verified':len(files),'maximum_file_bytes':max(f['bytes'] for f in files),'full_FEI':'OPEN','integrated_review':'PENDING_A094_A085'}
save(R/'out/FINAL_VALIDATION.json',final);print(json.dumps(final,indent=2))
