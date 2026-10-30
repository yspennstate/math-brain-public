from pathlib import Path
import json,hashlib,copy,time
from dependency_check import validate,statement_hash,key
RUN=Path(__file__).resolve().parents[1]; OWN=RUN.parents[1]; TEAM=OWN.parents[1]
PREV=OWN/'runs/20261011T234021Z-fleet05-A081-dependency-certificates'
def read(p):
    b=p.read_bytes();return b.decode('utf-16' if b.startswith((b'\xff\xfe',b'\xfe\xff')) else 'utf-8-sig')
def load(p):return json.loads(read(p))
def save(name,obj):(RUN/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
g=load(PREV/'PROOF_DEPENDENCIES.json');g['run_id']=RUN.name
nodes=g['nodes'];sources=g['sources'];units=nodes[0]['units'];receipts=[]
snap=RUN/'out/source_snapshots';snap.mkdir(exist_ok=True)
def pin(sid,p,locator='source read this stage'):
    p=Path(p);raw=p.read_bytes();out=snap/(sid+p.suffix);out.write_bytes(raw)
    sources[sid]={'local_path':str(out),'original_local_path':str(p),'local_sha256':hashlib.sha256(raw).hexdigest(),'pin_scope':'Exact read-source byte snapshot','locator':locator}
    return sid
def find(cid,version=1):return next(n for n in nodes if n['claim_id']==cid and n['version']==version)
def edge(cid,why,version=1):
    n=find(cid,version);return {'claim_key':key(n),'statement_sha256':n['statement_sha256'],'hypothesis_instantiation':why,'unit_conversion':None}
def add(cid,statement,hyp,status,sid,locator,deps=(),evidence=(),first=None,version=1):
    n={'claim_id':cid,'version':version,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':statement_hash(statement,hyp),'units':units,'status':status,'proof_sources':[{'source_id':sid,'locator':locator}],'proof_dependencies':list(deps),'evidence':list(evidence),'first_unproved_line':first};nodes.append(n);return n
def imported(c,status,sid,locator,deps=(),evidence=(),first=None):
    canonical=statement_hash(c['exact_statement'],c['hypotheses']);only=hashlib.sha256(c['exact_statement'].encode()).hexdigest();reported=c['statement_sha256']
    exactkey=hashlib.sha256(json.dumps({'exact_statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    types={canonical:'canonical_statement_hypotheses',only:'statement_only_utf8',exactkey:'canonical_exact_statement_hypotheses'}
    assert reported in types,(c['claim_id'],reported,canonical,only,exactkey)
    receipts.append({'claim_key':key(c),'source_id':sid,'source_recorded_statement_sha256':reported,'canonical_statement_hypotheses_sha256':canonical,'statement_only_utf8_sha256':only,'exact_statement_key_hypotheses_sha256':exactkey,'reported_hash_type':types[reported],'content_identity':'Exact original statement and hypotheses preserved'})
    n=add(c['claim_id'],c['exact_statement'],c['hypotheses'],status,sid,locator,deps,evidence,first,c['version'])
    n['source_hash_receipt']=receipts[-1]
    n['source_declared_dependencies']=copy.deepcopy(c.get('proof_dependencies',[]))
    n['dependency_encoding_basis']='Edges encode the A081 reconstructed proof when admitted. Original source dependency records are retained verbatim here; an unreviewed compound claim remains its own unresolved obligation, not a completed import of its author chain.'
    return n
def run(agent,name):return TEAM/'agents'/agent/'runs'/name
r97=run('A097','20261011T221240Z-fleet05-A097-cross-route-transfer')
r97b=run('A097','20261012T005449Z-fleet05-A097-cross-route-transfer')
r99=run('A099','20261012T044129Z-fleet05-A099-candidate-assembly')
r90=run('A090','20261013T213537Z-fleet05-A090-independent-reconstruction')
r64=run('A064','20261011T224431Z-fleet05-A064-global-debt-potential')
r85=run('A085','20261013T213517Z-fleet05-A085-certificate-adversary')
r83=run('A083','20261012T023941Z-fleet05-A083-formal-core')
r100=run('A100','20261013T213917Z-fleet05-A100-release-and-continuation-ledger')
pin('stage2_graph',PREV/'PROOF_DEPENDENCIES.json');pin('board_stage3',TEAM/'BOARD.md');pin('B17_notes_stage3',TEAM/'claude/B17/STREAM_NOTES.md')
for sid,r,files in [('A097_transfer',r97,['CLAIMS.json','REPORT.md','CROSS_ROUTE_SUBSTITUTION.tex']),('A097_B05',r97b,['CLAIMS.json','REPORT.md','DERIVATION.md']),('A099_v2',r99,['CLAIMS.json','REPORT.md','REFINEMENT_PROOF.md']),('A090_v2',r90,['CLAIMS.json','REPORT.md']),('A064_v1',r64,['CLAIMS.json','REPORT.md']),('A085_contract',r85,['CLAIMS.json','REPORT.md']),('A083_formal',r83,['CLAIMS.json']),('A100_review',r100,['CLAIMS.json'])]:
    for f in files:pin(sid+'_'+Path(f).stem,r/f)
pin('A083_hash_writer',r83/'code/finalize.py','Lines 10-11: canonical JSON with exact_statement key; third source hash convention')
save('out/IMPORT_ATTEMPT_HISTORY.json',{'initial_attempt':'Stopped before graph persistence: A083 recorded hash did not match either of the two then-supported conventions.','resolution':'Read source writer, verified canonical JSON uses exact_statement rather than statement; added a third explicitly typed hash receipt. No source version changed and no mathematical proof was repaired.'})
pin('A081_stage3_review',RUN/'REVIEW.md');pin('A081_stage3_exact',RUN/'out/EXACT_AUDIT.json');pin('A081_stage3_spec',RUN/'out/FROZEN_SPEC.json');pin('A081_stage3_helper',RUN/'code/check_exact.py')
# Latest A064 stage contains a .final marker alone, not a source-complete proof.
latest64=run('A064','20261012T043447Z-fleet05-A064-global-debt-potential')
availability={'latest_A064_run':str(latest64),'files':sorted(p.name for p in latest64.iterdir()),'mathematical_source_complete':False,'fallback':'Read immutable stage-1 source and current STATUS; do not invent stage-2 statements or acceptance.'}
pin('A064_stage2_marker',latest64/'.final');pin('A064_current_status',TEAM/'agents/A064/STATUS.md')
save('out/SOURCE_AVAILABILITY.json',availability)
proof_evidence=[{'reviewer':'A081','verdict':'HOLDS_AT_STATED_SCOPE','method':'Independent joint-likelihood and character-expansion reconstructions, direct character sums/Fraction log identities','source_id':'A081_stage3_review','validation_source_id':'A081_stage3_exact','substantive_source_repair':False}]
# Admit already-source-complete baseline implications through this explicit reconstruction.
for cid,loc in [('BASE-BLOCK','A097 reconstruction: physical channel constant and influence identity'),('BRIDGE-ERASURE','Erasure implication below; conditional implication only')]:
    n=find(cid);n['status']='IMPORTED_ACCEPTED';n['proof_sources'].append({'source_id':'A081_stage3_review','locator':loc});n['evidence'].extend(proof_evidence)
transfer=imported(load(r97/'CLAIMS.json')[0],'IMPORTED_ACCEPTED','A097_transfer_CLAIMS','A097 theorem; independent REVIEW first section',[edge('BASE-BLOCK','Finite fair physical block, signed restriction coefficients, support positivity and physical influence conservation')],proof_evidence)
parity_source=load(r90/'CLAIMS.json')[1]
parity=imported(parity_source,'IMPORTED_ACCEPTED','A090_v2_CLAIMS','Exact claim 2; full independent parity-tail reconstruction',evidence=proof_evidence)
low_source=load(r99/'CLAIMS.json')[0];low_review=load(r90/'CLAIMS.json')[0]
assert low_source['exact_statement']==low_review['exact_statement'] and low_source['hypotheses']==low_review['hypotheses']
low=imported(low_source,'IMPORTED_ACCEPTED','A099_v2_CLAIMS','Version 2 statement; A090 independent review at same literal scope',[edge(parity['claim_id'],'R_geell<=B and the cutoff supremum equality imply aggregate low-influence completeness'),edge('BRIDGE-ERASURE','Use only its proved implication for the explicitly conditional C_FEI comparison')],proof_evidence+[{'reviewer':'A090','verdict':'HOLDS_AT_STATED_SCOPE','source_id':'A090_v2_CLAIMS','binding':'Original source canonical hash and reviewer statement-only hash identify identical statement/hypotheses'}])
low['additional_review_hash_receipt']={'reviewer_recorded_hash':low_review['statement_sha256'],'type':'statement_only_utf8','equals_same_source_statement':True}
# Author-certified compound application is not upgraded by A100's partial verdict.
b05c=load(r97b/'CLAIMS.json')[0]
b05=imported(b05c,'PENDING_FULL_APPLICATION_AUDIT','A097_B05_CLAIMS','All-even-k full compound claim; transfer now reviewed, detailed all-even-k application not fully independently reviewed here',[edge(transfer['claim_id'],'Use fixed complete leaves, same control-first tree; terminal bills retained')],evidence=[{'source_id':'A100_review_CLAIMS','verdict':'ACCEPT_ERASURE_AND_TERMINAL_SLACK_SUBCLAIMS_ONLY','scope_exclusion':'No full compatible-transfer corollary or decimal intervals accepted from this review'}],first='Full compound application acceptance needs source-bound all-even-k and interval reconstruction; universal arbitrary-core payment remains separate.')
boundary=add('A081-INTAKE-A064-BOUNDARY-SIGN','For every finite fresh-coordinate physical tree, if D_v<=C d_v+Q_v-E Q_child, Q_root<=K I_removed, and E(H_leaf-Q_leaf)<=L E I_leaf, then H_root<=max(C+K,L) I_root. For Q=CI-H its drift is Cd-D, so the local debt condition is equivalent to D<=Cd; parent/child H<=CI does not suffice. The actual two-bit sign (-1,1,1,1) at C=2 has H=2,I=1,d=1/2, Q_root=0,E Q_child=1 and violates that debt condition.',['Finite uniform Boolean signs; entropy in bits','Physical no-repeat finite tree; actual reach weights','Finite C,K,L>=0 and stated initial/terminal assumptions'],'IMPORTED_CERTIFIED','A081_stage3_review','Debt sign and boundary section',evidence=proof_evidence)
imported(load(r64/'CLAIMS.json')[0],'PENDING_COMPOUND_REVIEW','A064_v1_CLAIMS','Stage-1 compound reserve theorem; only boundary/sign portion independently reviewed',[edge(boundary['claim_id'],'Boundary and sign clause only; other compound class and no-go clauses are not supplied by this dependency')],first='Other clauses of this compound source theorem were not reconstructed in this stage; no phantom stage-2 theorem imported.')
formal=imported(load(r83/'CLAIMS.json')[0],'KERNEL_CHECK_RECEIPT_PENDING_INDEPENDENT_REVIEW','A083_formal_CLAIMS','Finite rational coefficient core only, not real analytic JS limit',first='No real-series convergence/endpoint or Fourier application was kernel-checked by this source claim.')
formal['units']={'entropy':'none; finite rational polynomial coefficients','influence':'none','log':'none'}
helper=imported(load(r85/'CLAIMS.json')[0],'PENDING_INDEPENDENT_CONTRACT_REVIEW','A085_contract_CLAIMS','Saved helper-contract refutation, preserving its IEEE/NumPy and domain hypotheses',first='A081 consumes the source-bound objection; does not independently rerun the layout-specific floating witness or approve its contributed repair.')
helper['scope_exclusions']=['Not a Boolean counterexample','No invalidation of m=54 census or independent Fraction cutoff certificate','General eta_m repair not independently accepted here']
find('B17-KB5-CUTOFF')['evidence'].append({'reviewer':'A085','verdict':'ACCEPT_AT_STATED_SCOPE','source_id':'A085_contract_CLAIMS','repair':False})
find('B17-KB4-CENSUS')['evidence'].append({'reviewer':'A085','verdict':'SOURCE_LOGIC_RANGE_ORBIT_AUDIT_ONLY','source_id':'A085_contract_REPORT','full_rerun':False,'compound_acceptance_not_inferred':True})
open_tree=add('OPEN-PAID-COMPATIBLE-TREE','There exist finite K,C_leaf such that for every uniform Boolean f one finite allowed physical tree and complete fixed leaf references jointly satisfy sum pi(B-kappa)<=K I_removed and every terminal CE<=C_leaf I_leaf.',['Same tree and same reference construction for both inequalities','All dimensions; same constants; single-use physical influence and complete terminal references'],'OPEN','A081_stage3_review','Exact first unsupported universal line',first='Existence of a jointly paid arbitrary-core/overlapping-history scheme is not proved.')
open_tail=add('OPEN-HIGHER-ERASURE-PAYMENT','There exists finite K such that R_ge2(f)<=K I(f) for every uniform Boolean sign f in every finite dimension.',['R_ge2=sum_i sum_(T not containing i,|T|>=2) phi(fhat(T)^2,fhat(T+i)^2)','Bits; same finite K for all actual Boolean f'],'OPEN','A090_v2_REPORT','Section 4 OPEN line',first='No all-dimensional normalized all-degree derivative reference payment is supplied.')
open_low=add('OPEN-LOW-INFLUENCE-ERASURE-PAYMENT','For s(N)=sqrt(N), there exists finite K such that B(f)<=K I(f) for every N-bit uniform Boolean sign with 0<I(f)<=2^-s(N).',['Aggregate B, not selectable minimum','Finite fixed K independent of N and f'],'OPEN','A081_stage3_review','Low-influence equality only preserves debt; it does not pay it',first='The restricted-class bound is full aggregate FEI-strength and remains unproved.')
g['candidate_routes'].extend([
 {'route_id':'R-C019-C024-COMPATIBLE','conclusion':g['final_claim'],'requires':[key(transfer),key(open_tree)],'derivation':'Compatible reference identity plus one JOINT terminal-inclusive influence payment; no separate existential witness composition.','status':'CONDITIONAL_ROUTE_ONLY'},
 {'route_id':'R-C018-HIGHER','conclusion':g['final_claim'],'requires':[key(parity),'BRIDGE-ERASURE@1',key(open_tail)],'derivation':'Tail supremum equals K_E, then use the independently reconstructed erasure implication.','status':'CONDITIONAL_ROUTE_ONLY'},
 {'route_id':'R-C018-LOW-INFLUENCE','conclusion':g['final_claim'],'requires':[key(low),key(open_low)],'derivation':'Aggregate cutoff supremum equals K_E; finiteness is the unpaid premise.','status':'CONDITIONAL_ROUTE_ONLY'}])
g['source_scope_receipts']={'hash_types':'Canonical hashes include statement+hypotheses; statement-only source hashes retained as explicitly typed aliases, not substitute dependency hashes.','A064_latest_stage':availability,'B05_acceptance':'A100 partial verdict not promoted to full compound acceptance.','A083_formal':'No formal-to-analytic scope widening.','A085_helper':'Generic error contract objection quarantined; no false propagation to independently valid finite certificates.'}
g['prior_change_receipts']=g.get('change_receipts',{})
g['change_receipts']={'prior_graph_sha256':hashlib.sha256((PREV/'PROOF_DEPENDENCIES.json').read_bytes()).hexdigest(),'prior_run_id':PREV.name,'new_nodes':len(nodes)-len(load(PREV/'PROOF_DEPENDENCIES.json')['nodes']),'new_independent_review_fragments':['A097 transfer v1','A090 parity-tail v1','A099 low-influence v2','A064 boundary/sign extracted scope'],'all_original_source_statements_preserved':True,'finite_census_not_repeated':True,'universal_constant_change':None}
save('out/HASH_RECEIPTS.json',receipts)
save('PROOF_DEPENDENCIES.json',g)
v=validate(g);assert v['status']=='STRUCTURALLY_VALID',v['errors'];assert all(not r['eligible_for_mathematical_review'] for r in v['candidate_routes']);save('out/GRAPH_VALIDATION.json',v)
fixtures=[]
def rejects(label,mutate,prefix):
    h=copy.deepcopy(g);mutate(h);w=validate(h,check_files=False);hit=any(e.startswith(prefix) for e in w['errors']);assert hit,(label,w['errors']);fixtures.append({'fixture':label,'PASS':hit,'matched_errors':[e for e in w['errors'] if e.startswith(prefix)]})
def nn(h,cid):return next(n for n in h['nodes'] if n['claim_id']==cid)
rejects('final FEI to transfer to final cycle',lambda h:(nn(h,'FEI-FINAL')['proof_dependencies'].append(edge(transfer['claim_id'],'Forbidden inferred use')),nn(h,transfer['claim_id'])['proof_dependencies'].append(edge('FEI-FINAL','Forbidden hidden final premise'))),'CYCLE_THROUGH_FINAL_FEI:')
rejects('canonical dependency replaced by statement-only alias',lambda h:nn(h,low['claim_id'])['proof_dependencies'][0].update(statement_sha256=hashlib.sha256(parity['exact_statement'].encode()).hexdigest()),'DEPENDENCY_HASH:')
rejects('tail leaf falsely accepted without proof',lambda h:nn(h,open_tail['claim_id']).update(status='IMPORTED_ACCEPTED'),'ACCEPTED_WITHOUT_EVIDENCE:')
rejects('history route silently assumes FEI',lambda h:h['candidate_routes'][-3]['requires'].append(h['final_claim']),'ROUTE_ASSUMES_CONCLUSION:')
rejects('source locator erased from transfer',lambda h:nn(h,transfer['claim_id'])['proof_sources'][0].update(locator=''),'MISSING_LOCATOR:')
rejects('accepted low-influence uses unpaid tail bound',lambda h:nn(h,low['claim_id'])['proof_dependencies'].append(edge(open_tail['claim_id'],'Unpaid premise disguised as source')),'ACCEPTED_DEPENDS_ON_UNRESOLVED:')
rejects('changed parity hypothesis without new hash',lambda h:nn(h,parity['claim_id'])['hypotheses'].append('ell=1 erroneously permitted'),'STATEMENT_HASH:')
save('out/MUTATION_AUDIT.json',{'status':'PASS','fixtures':fixtures,'count':len(fixtures),'scope':'Structural rejection only; analytic proofs are separately reconstructed.'})
print(json.dumps({'status':'PASS','nodes':len(nodes),'source_pins':len(sources),'admitted':sum(n['status'] in ['IMPORTED_ACCEPTED','IMPORTED_CERTIFIED'] for n in nodes),'conditional_routes':len(g['candidate_routes']),'mutation_fixtures':len(fixtures),'new_accepted_closures':{key(n):v['unresolved_closure'][key(n)] for n in [transfer,parity,low,boundary]}},indent=2))
