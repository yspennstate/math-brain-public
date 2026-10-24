from pathlib import Path
import json,hashlib,copy,datetime
from dependency_check import validate,statement_hash,key
R=Path(__file__).resolve().parents[1];OWN=R.parents[1];TEAM=OWN.parents[1]
PREV=OWN/'runs/20261013T220111Z-account05-A081-dependency-certificates'
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
proto=load('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
g=load(PREV/'PROOF_DEPENDENCIES.json');g['run_id']=R.name;nodes=g['nodes'];sources=g['sources'];units=nodes[0]['units'];hashes=[]
snap=R/'out/source_snapshots';snap.mkdir(exist_ok=True)
def pin(sid,p,loc='exact read-source snapshot'):
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
    receipt={'claim_key':key(c),'source_recorded_hash':c['statement_sha256'],'source_hash_type':types[c['statement_sha256']],'internal_canonical_hash':canonical,'statement_only_hash':only,'exact_literal_content_preserved':True};hashes.append(receipt)
    n=node(c['claim_id'],c['exact_statement'],c['hypotheses'],status,sid,loc,deps,evidence,first);n['source_hash_receipt']=receipt;n['source_declared_dependencies']=copy.deepcopy(c.get('proof_dependencies',[]));return n
paths={
'A090':TEAM/'agents/A090/runs/20261014T010003Z-account05-A090-independent-reconstruction',
'A001':TEAM/'agents/A001/runs/20261014T011101Z-account05-A001-quantifier-audit',
'A096':TEAM/'agents/A096/runs/20261013T220343Z-account05-A096-live-gap-ledger',
'A099':TEAM/'agents/A099/runs/20261014T001305Z-account05-A099-candidate-assembly',
'A094':TEAM/'agents/A094/runs/20261014T001244Z-account05-A094-proof-chain-challenger',
'A097':TEAM/'agents/A097/runs/20261013T222610Z-account05-A097-cross-route-transfer',
'A086':TEAM/'agents/A086/runs/20261013T220217Z-account05-A086-joint-code-referee'}
for a,files in {'A090':['CLAIMS.json','REPORT.md'],'A001':['CLAIMS.json','REPORT.md'],'A096':['CLAIMS.json','DERIVATION.md','REPORT.md'],'A099':['CLAIMS.json','REPORT.md'],'A094':['CLAIMS.json','AUDIT.md'],'A097':['CLAIMS.json','DERIVATION.md'],'A086':['CLAIMS.json']}.items():
    for f in files:pin(a+'_s4_'+Path(f).stem,paths[a]/f)
pin('board_s4',TEAM/'BOARD.md');pin('B17_notes_s4',TEAM/'claude/B17/STREAM_NOTES.md');pin('protocol_s4','~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json');pin('stage3_graph',PREV/'PROOF_DEPENDENCIES.json')
pin('A081_review_s4',R/'REVIEW.md');pin('A081_exact_s4',R/'out/EXACT_CONTRACT_AUDIT.json');pin('A081_helper_s4',R/'code/check_refund_contract.py');pin('A081_spec_s4',R/'out/FROZEN_SPEC.json')
cs={a:load(p/'CLAIMS.json') for a,p in paths.items()}
def claim(a,cid):return next(c for c in cs[a] if c['claim_id']==cid)
ev=[{'reviewer':'A081','verdict':'INDEPENDENT_RECONSTRUCTION_AT_STATED_SCOPE','source_id':'A081_review_s4','validation_source_id':'A081_exact_s4','upstream_repair':False}]
base=node('A081-COMPLETE-ROW-KL-INTERFACE','For every actual uniform Boolean f with I>0, complete row laws mu_i(T)=p_(T+i)/e_i and r_i(T)=p_T+p_(T+i) and joint laws P(i,T)=p_(T+i)/I, Q(i,T)=(e_i/I)r_i(T) normalize to one. Their row/coordinate KL chain gives L=sum_i e_i log2(1/e_i)-I D(P||Q), with 0<=L<=B<=L+I/ln2. If one finite K satisfies D(P||Q)>=Gamma-K for all f, then full FEI holds with K+3/ln2; conversely FEI(C) implies L<=CI. Constants have L=B=I=0.',['Actual finite uniform Boolean sign; bits; relevant rows only','Complete residual law, not conditioned on derivative support','Universal payment occurs only as antecedent of implication'],'IMPORTED_CERTIFIED','A081_review_s4','Sections 1 and 3',[edge('BRIDGE-ERASURE','From L<=KI obtain B<=(K+1/ln2)I and use its conditional implication')],ev)
refund_c=claim('A096','A096-TERMINAL-KL-REFUND-AUDIT');refund_review=claim('A001',refund_c['claim_id'])
assert refund_c['exact_statement']==refund_review['exact_statement'] and refund_c['hypotheses']==refund_review['hypotheses']
refund=intake(refund_c,'IMPORTED_ACCEPTED','A096_s4_CLAIMS','Original scoped transport; literal full A001/A073 review',[edge(base['claim_id'],'Complete normalized row and joint law definitions; no universal payment assumed')],[{'reviewer':'A001','source_id':'A001_s4_CLAIMS','verdict':'ACCEPT_AT_FULL_ORIGINAL_STATED_SCOPE_NO_REPAIR','binding':'Identical literal statement/hypotheses; terminal seed bill explicitly unpaid'},{'reviewer':'A073','source_id':'A001_s4_CLAIMS','verdict':'Existing complete normalization acceptance consumed; not rerun here'}])
disjoint_c=claim('A086','A086-DISJOINT-SELECTOR-PRESCRIBED-REFERENCE');disjoint_review=claim('A094',disjoint_c['claim_id'])
shared_c=claim('A097','A097-ONE-SHARED-DATA-COLLISION-TRANSFER');shared_review=claim('A094',shared_c['claim_id'])
for c,review in [(disjoint_c,disjoint_review),(shared_c,shared_review)]:assert c['exact_statement']==review['exact_statement'] and c['hypotheses']==review['hypotheses']
disjoint=intake(disjoint_c,'IMPORTED_ACCEPTED','A086_s4_CLAIMS','A094 entire disjoint-child reference review',[edge('BASE-BLOCK','Fresh selector with actual physical children; calibration and retained KL reconstructed in A094 audit')],[{'reviewer':'A094','source_id':'A094_s4_CLAIMS','proof_source_id':'A094_s4_AUDIT','verdict':'HOLDS_AT_STATED_SCOPE','scope':'Normalized supplied child references and retained terminal costs only'}])
shared=intake(shared_c,'IMPORTED_ACCEPTED','A097_s4_CLAIMS','A094 entire shared-bit transfer and explicit larger-block/boundary clauses',[edge('A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER','Use actual one-node conditional kernel, calibrated complete terminal reference laws; no unpriced reset'),edge(disjoint['claim_id'],'Collision-atom calibration and scalar packet estimate; extension only under one-shared-bit/l1 admission or stated dimension-dependent coefficient')],[{'reviewer':'A094','source_id':'A094_s4_CLAIMS','proof_source_id':'A094_s4_AUDIT','verdict':'HOLDS_AT_FULL_STATED_SCOPE','scope':'No arbitrary-sharing selector-only extension or universal seed-cost bound'}])
degree_c=claim('A090','A090-DEGREE-COARSENED-REFUND-OBSTRUCTION')
degree=intake(degree_c,'IMPORTED_ACCEPTED','A090_s4_CLAIMS','Entire independently reconstructed degree-obstruction statement',[edge(base['claim_id'],'Use normalized complete row KL; derive actual tribes degree laws and H<=6I independently without FEI')],ev)
bounded_c=claim('A001','A001-BOUNDED-DEGREE-REFUND-LOSS')
intake(bounded_c,'PENDING_INDEPENDENT_RECONSTRUCTION','A001_s4_CLAIMS','Full-support/small-I fixed-low-degree obstruction author scope; not a proof premise here',first='A081 has not independently reconstructed the entire fixed-cutoff tensor argument; preserve its separate review queue.')
adapter=node('A081-COARSENING-REFUND-CONTRACT','For every actual finite uniform Boolean f and deterministic finite partition C_i of each complete residual subset space, D(mu_i||r_i)=D(C_i mu_i||C_i r_i)+W_i, W_i=sum_c mu_i(c)D(mu_i(.|c)||r_i(.|c))>=0, and L^C-L=sum_i e_i W_i exactly. Reference-only cells retain their mass. For a disjoint tensor f(x)g(y), each f-coordinate has mu_i^fg=mu_i^f tensor p_g and r_i^fg=r_i^f tensor p_g. Retaining the full core residual subset with any deterministic spectator partition preserves full row KL and gives W_i=0; retaining separate core/spectator degrees preserves only the core degree KL. These identities do not pay the arbitrary core L or terminal CE.',['Complete normalized mu_i,r_i; relevant coordinates; bits','Partition fixed for the function before a spectral draw','Physical tensor blocks disjoint; i belongs to f','Zero-true/reference-only cells are not deleted or renormalized'],'IMPORTED_CERTIFIED','A081_review_s4','Section 1, exact chain and non-product core tensor fixture',[edge(base['claim_id'],'Same complete row laws and influence; no paid endpoint inferred')],ev)
adapter['information_contract']={'complete_reference':True,'partition_declared':True,'conditional_refund':'W_i=sum_c mu_C(c) D(mu(.|c)||r(.|c))','reference_only_cells':'retained','terminal_core_payment':'UNRESOLVED','spectator_influence_reuse':False}
false=node('PROPOSED-DEGREE-ONLY-KL-PAYMENT','There exists a finite absolute K such that L_degree(f)<=K I(f) for every finite uniform Boolean sign, where each full row KL is replaced by its pushforward under residual degree.',['Same finite K for all actual Boolean signs','Complete degree marginals; bits'],'REFUTED','A090_s4_CLAIMS','Actual tribes family w>=32, L_degree/I>=w/2',[edge(degree['claim_id'],'All-width actual Boolean family has ratio diverging')],ev,first='False: actual tribes give L_degree/I>=w/2 for all w>=32.')
unpaid=node('OPEN-TERMINAL-KL-PAYMENT','There exists finite K such that for every finite uniform Boolean f with I>0 the actual complete normalized joint laws satisfy D(P_f||Q_f)>=Gamma(f)-K, Gamma=sum_i(e_i/I)log2(1/e_i).',['Actual complete rows, same finite K for every dimension','Bits; single original influence ledger; no lost conditional refund'],'OPEN','A081_review_s4','Section 3 first unsupported universal line',first='No signed-Boolean lower bound pays the retained complete terminal seed divergence universally.')
g['candidate_routes'].append({'route_id':'R-C018-COMPLETE-KL','conclusion':g['final_claim'],'requires':[key(base),key(unpaid)],'derivation':'The explicit complete-KL lower bound gives L<=KI then B<=(K+1/ln2)I and FEI(K+3/ln2); open K remains unpaid.','status':'CONDITIONAL_ROUTE_ONLY'})
g['rejected_proof_attempts']=[{'attempt':'Degree-only terminal refund','refuted_claim_key':key(false),'actual_family':degree_c['exact_statement'],'scope':'Prospective shortcut only; not an assertion made by A096 or A099; full complete-KL route survives.'}]
g['prior_change_receipts_stage3']=g['change_receipts'];g['change_receipts']={'prior_run':PREV.name,'prior_graph_sha256':hashlib.sha256((PREV/'PROOF_DEPENDENCIES.json').read_bytes()).hexdigest(),'independent_review_closed':key(degree),'source_reviews_consumed':[key(refund),key(disjoint),key(shared)],'universal_constant_change':None,'new_scoped_adapter':key(adapter),'false_shortcut':key(false)}
save(R/'out/HASH_RECEIPTS.json',hashes);save(R/'PROOF_DEPENDENCIES.json',g)
def contracts(h):
    errors=[]
    for n in h['nodes']:
        c=n.get('information_contract')
        if c is not None:
            if c.get('complete_reference') is not True:errors.append('INCOMPLETE_REFERENCE:'+key(n))
            if not c.get('partition_declared'):errors.append('UNDECLARED_PARTITION:'+key(n))
            if not c.get('conditional_refund'):errors.append('LOST_CONDITIONAL_REFUND:'+key(n))
            if c.get('reference_only_cells')!='retained':errors.append('REFERENCE_MASS_RESET:'+key(n))
            if c.get('spectator_influence_reuse') is not False:errors.append('SPECTATOR_INFLUENCE_REUSE:'+key(n))
    return errors
v=validate(g);assert v['status']=='STRUCTURALLY_VALID' and not contracts(g);save(R/'out/GRAPH_VALIDATION.json',v)
fixtures=[]
def ng(h,c):return next(n for n in h['nodes'] if n['claim_id']==c)
def rejection(label,mut,prefix):
    h=copy.deepcopy(g);mut(h);errs=validate(h,check_files=False)['errors']+contracts(h);hits=[e for e in errs if e.startswith(prefix)];assert hits,(label,errs);fixtures.append({'fixture':label,'PASS':True,'rejection':hits})
rejection('Final FEI cycle via refund',lambda h:(ng(h,'FEI-FINAL')['proof_dependencies'].append(edge(refund['claim_id'],'Forbidden')) ,ng(h,refund['claim_id'])['proof_dependencies'].append(edge('FEI-FINAL','Forbidden'))),'CYCLE_THROUGH_FINAL_FEI:')
rejection('Admitted refund assumes refuted degree payment',lambda h:ng(h,refund['claim_id'])['proof_dependencies'].append(edge(false['claim_id'],'Illicit shortcut')),'ACCEPTED_DEPENDS_ON_UNRESOLVED:')
rejection('Drop within-cell refund',lambda h:ng(h,adapter['claim_id'])['information_contract'].update(conditional_refund=''),'LOST_CONDITIONAL_REFUND:')
rejection('Condition reference onto derivative support',lambda h:ng(h,adapter['claim_id'])['information_contract'].update(reference_only_cells='deleted'),'REFERENCE_MASS_RESET:')
rejection('Borrow spectator influence for unpaid core',lambda h:ng(h,adapter['claim_id'])['information_contract'].update(spectator_influence_reuse=True),'SPECTATOR_INFLUENCE_REUSE:')
rejection('Shared-bit source hypothesis silently generalized',lambda h:ng(h,shared['claim_id'])['hypotheses'].append('Arbitrary overlapping data now permitted at the same constant'),'STATEMENT_HASH:')
rejection('Literal dependency alias replaces canonical content hash',lambda h:ng(h,shared['claim_id'])['proof_dependencies'][1].update(statement_sha256=hashlib.sha256(disjoint_c['exact_statement'].encode()).hexdigest()),'DEPENDENCY_HASH:')
rejection('Route presumes final FEI',lambda h:h['candidate_routes'][-1]['requires'].append(h['final_claim']),'ROUTE_ASSUMES_CONCLUSION:')
save(R/'out/MUTATION_AUDIT.json',{'status':'PASS','fixtures':fixtures,'contract_check_scope':'Declaration checks only, not automated inference validity'})
save(R/'out/REFUTATION_DELTA.json',{'false_exact_version':key(false),'witness_family':'Actual OR of 2^w disjoint width-w point conjunctions; w>=32 gives retained coarse cost/I>=w/2','downstream_accepted_versions_depending_on_false_leaf':[],'effect_on_A096_A099':'No refutation; complete reference remains valid and universal payment remains OPEN','propagation_owner':'B20; saved source-bound delta only; no external adoption claimed'})
# Protocol claim reviews preserve original statements and source hashes.
degree_out=copy.deepcopy(degree_c);degree_out['review_records'].append({'reviewer':'A081','timestamp':now,'verdict':'ACCEPT_AT_FULL_ORIGINAL_STATED_SCOPE','method':'Independent occupancy-count/head-tail proof and exact rational polynomial, direct-character and partition checks','proof_source':str(R/'REVIEW.md'),'validation_source':str(R/'out/EXACT_CONTRACT_AUDIT.json'),'reviewer_contributed_repair':False});degree_out['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A081'
refund_out=copy.deepcopy(refund_review);shared_out=copy.deepcopy(shared_review)
claims=[degree_out,refund_out,shared_out]
def own(n,status,contributors):return {'claim_id':n['claim_id'],'version':n['version'],'exact_statement':n['exact_statement'],'hypotheses':n['hypotheses'],'statement_sha256':n['statement_sha256'],'contributors':contributors,'proof_source':{'path':str(R/'REVIEW.md'),'validation':str(R/'out/EXACT_CONTRACT_AUDIT.json')},'proof_dependencies':n['proof_dependencies'],'review_records':[],'status':status,'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A096','A001','A073','A099','A094','B20']}
claims.append(own(adapter,'EXACTLY_CERTIFIED_SCOPED_ADAPTER_PENDING_INDEPENDENT_REVIEW',['A081; partition KL chain credited to the existing A090/A001 mechanism']))
exact=load(R/'out/EXACT_CONTRACT_AUDIT.json');N=len(nodes);S=len(sources);A=sum(n['status'] in ['IMPORTED_ACCEPTED','IMPORTED_CERTIFIED'] for n in nodes);routes=len(g['candidate_routes'])
s=f'A081 stage-4 dependency certificate has {N} exact nodes, {S} source byte pins and an acyclic graph. It independently accepts A090 degree-coarsening obstruction v1, consumes full scoped A096 refund and A097 shared-bit reviews, retains the complete conditional refund under arbitrary declared partitions, and preserves unpaid terminal-core and shared-collision leaves. It passes {exact["assertions"]} exact assertions and eight mutation fixtures. All {routes} FEI routes remain conditional; no universal constant is obtained.'
h=['Exact pinned source versions and graph hashes','Finite implementation checks do not replace all-dimensional proofs','Integrated certificate acceptance remains pending']
cert={'claim_id':'A081-VERSIONED-DEPENDENCY-CERTIFICATE','version':4,'exact_statement':s,'hypotheses':h,'statement_sha256':statement_hash(s,h),'contributors':['A081'],'proof_source':{'path':str(R/'PROOF_DEPENDENCIES.json'),'files':['REVIEW.md','out/GRAPH_VALIDATION.json','out/MUTATION_AUDIT.json','out/REFUTATION_DELTA.json']},'proof_dependencies':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in claims],'review_records':[],'status':'EXACTLY_VALIDATED_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[{'claim_id':'A081-VERSIONED-DEPENDENCY-CERTIFICATE','version':3}],'refutes':[],'first_unproved_line':None,'next_consumers':['A094','A085','B20']};claims.append(cert)
for c in claims:assert set(c)==set(proto['required_per_run']['claim_fields'])
save(R/'CLAIMS.json',claims)
next_action='Audit one source-complete signed-Boolean conditional refund/payment on a non-product core row, retaining W_i, the complete joint reference and terminal CE; test spectator compatibility and actual tribes with one physical influence reserve. No degree-only, fixed-tail or influence-only substitution.'
progress={'protocol_revision':proto['revision'],'run_id':R.name,'stream':'B17','packet_id':'A081','gap_id':'G-C018-TERMINAL-KL-PAYMENT','attempt_id':'A081-stage4-coarsening-debt-and-review-intake','method':'Independent all-width Boolean obstruction reconstruction; complete-row partition/spectator exact certificate; source-bound full review intake and refutation scope propagation','mathematical_delta':'A090 degree-coarsening obstruction independently accepted; exact conditional refund debt retained under all partitions; protected spectator coarsening preserves full non-product core refund but supplies no core payment. A096 normalized refund and A097 shared-bit transfer reviews incorporated.','deliverable_status':'LOCAL_COMPLETE; EXACT_GRAPH_REVIEW_AND_SCOPE_DELTA_SAVED','mathematical_status':'DEGREE_ONLY_PAYMENT_REFUTED_AT_SCOPED_MECHANISM; COMPLETE_KL_PAYMENT_OPEN; FULL_FEI_OPEN','claim_versions_used':[key(degree),key(refund),key(shared),key(disjoint),key(adapter),'A001-BOUNDED-DEGREE-REFUND-LOSS@1'],'claims_created_or_changed':[key(c) for c in claims],'source_artifacts':['PROOF_DEPENDENCIES.json','REVIEW.md','out/EXACT_CONTRACT_AUDIT.json','out/REFUTATION_DELTA.json','out/HASH_RECEIPTS.json','out/MUTATION_AUDIT.json','out/source_snapshots/'],'next_consumers':['A096','A001','A073','A097','A099','A094','A085','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal signed-Boolean lower bound for complete terminal KL remains unpaid.','Shared-data excess beyond l1 admission has no named nonreused core reserve.','Fixed-low-degree single-tail claim and new adapter/integrated certificate retain separate pending independent reviews.'],'packet_ids':['A081']}
assert set(progress)=={x if not x.startswith('packet_ids (') else 'packet_ids' for x in proto['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A081 / B17 dependency certificates, stage 4. Audit the current C018 terminal-KL payment frontier while preserving exact claim versions, hypotheses, units, source pins and unresolved leaves. All functions are actual Boolean signs on finite uniform physical cubes. Information is in bits; influence is pivotal probability/spectral expected cardinality. Full normalized residual laws retain reference-only cells. Final FEI is OPEN, and any cycle through it is rejected.

# sources actually read, revisions and theorem locators

Read BOARD snapshot 2026-10-14 01:30 UTC, B17 STREAM_NOTES v2, own STATUS and prior immutable certificate, and the entire execution protocol {proto['revision']}. The lead's six-claim/MU assignment was completed previously; dispatch now consumes new terminal-KL and shared-bit dependencies, avoiding repeated finite censuses. Source receipts are pinned in this graph and out/source_snapshots.

Primary originals: A090 20261014T010003Z REPORT/CLAIMS equations (1)-(19); A001 20261014T011101Z CLAIMS/REPORT sections 1-3; A096 20261013T220343Z CLAIMS/REPORT/DERIVATION equations (1)-(6); A099 20261014T001305Z REPORT/CLAIMS assembled frontier and scoped reviews; A097 20261013T222610Z CLAIMS/DERIVATION sections 1-4; A094 20261014T001244Z CLAIMS/AUDIT full disjoint/shared-bit reviews and one-node limitation; A086 20261013T220217Z original disjoint claim. Three hash conventions remain explicitly typed in out/HASH_RECEIPTS.json. No literature priority assertion or threshold/percolation theorem enters this proof.

# complete derivation or exact first unsupported line

REVIEW.md contains the all-dimensional reconstruction. A090-DEGREE-COARSENED-REFUND-OBSTRUCTION@1 receives independent full-scope acceptance without repair: actual tribes satisfy L_degree/I>=w/2 for every w>=32, while 0<=L<=B<=H<=6I for w>=4. Thus the discarded within-degree refund/I grows at least w/2-6. The proof reconstructs the actual factor spectra, two degree-law descriptions, active-block likelihood domination, exact mean, head/tail KL bound and complete entropy upper bound. This is an information-loss obstruction, not an FEI counterexample.

The narrow new adapter retains the full conditional information contract for ANY deterministic residual partition: D(mu||r)=D(C mu||C r)+W, W>=0, and L^C-L=sum_i e_i W_i. On f(x)g(y), keeping the full active-core residual subset and any independent spectator partition preserves full core KL exactly. Separate core/spectator degrees retain only core-degree KL. A named actual non-product three-bit point-defect row with a bent4 spectator has a positive exact total-degree defect, yet zero protected-partition defect. This controls valid spectator cancellation but pays no arbitrary core bill or terminal CE.

The exact first unsupported universal line remains D(P_joint||Q_joint)>=Gamma(f)-K for one finite K and every actual Boolean seed, using its COMPLETE normalized joint reference. This would give L<=KI, B<=(K+1/ln2)I and FEI(K+3/ln2). No such lower bound is supplied. The false degree-only replacement is explicitly refuted, while the full A096 reference and its activation audit survive unchanged. A097's accepted shared-bit theorem still retains complete calibrated child costs and has only its stated one-bit/l1/dimension-dependent admission.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC was written before computation. Fixed domain: 24 core truth tables (all one/two-bit signs and four named three-bit signs), six named spectator functions, exactly 144 actual Boolean tensor products; 228 relevant core rows and 684 partition cases. Three partitions are total degree, separate core/spectator degree, and full-core/spectator degree. One compressed actual tribes function at w=4,m=16 has all 64 degree packets checked through an independent occupancy-count mixture. No coordinate orbits or symmetry are used for tensor cases; tribes uses proven coordinate transitivity only.

Commands from A081:

    python -X utf8 runs\\{R.name}\\code\\check_refund_contract.py --pilot
    python -X utf8 runs\\{R.name}\\code\\check_refund_contract.py
    python -X utf8 runs\\{R.name}\\code\\finish.py

Pilot PASS: 998 assertions, six tensors, 54 partition cases. Full PASS: {exact['assertions']} assertions, {exact['partition_cases']} partitions, {exact['nonzero_conditional_defects']} nonzero discarded conditional refunds, helper runtime {exact['runtime_seconds']:.3f} seconds. Arithmetic: direct integer character sums and physical tensor checks; Fraction normalization and inequalities; exact prime-log coefficient cancellation; integer binomial occupancy laws. There is no floating-point entropy sign and no all-width extrapolation from w=4. REVIEW's analytic proof establishes all widths and divergence.

Estimated memory 64 MB, maximum runtime 60 seconds. No job above 300 MB, GPU, automatic dimension increase or background process. Eight fixtures reject final-FEI cycles, admitted dependence on a refuted shortcut, erased conditional refund, dropped reference-only mass, borrowed spectator influence, changed shared-bit hypotheses, wrong hash alias, and a route assuming FEI. Declaration guards do not claim automated semantic proof checking.

# proof dependencies and changed downstream conclusions

Updated graph: {N} nodes, {S} source byte pins, {A} admitted scoped nodes, acyclic; all {routes} FEI routes conditional. Exact graph hashes use canonical statement+hypotheses; source hashes retain their original typed conventions. A096's full literal refund statement is paired with A001/A073 saved reviews; A097/A086 literal statements are paired with A094's full accepted scopes. These are consumed independent records, not additional A081 proofs of already-reviewed baselines.

A090's degree theorem has a new full A081 review. A001's fixed-low-degree single-tail obstruction remains a separately pinned pending import; its full-support and I->0 hypotheses are preserved. A094's author balanced-tensor extension is not absorbed into A097 acceptance. Its one-node review does not establish a second full stopping-tree/integrated certificate acceptance.

out/REFUTATION_DELTA records the exact false prospective degree-only version, actual all-width Boolean witness and affected scope. No previously accepted A096/A099 version is refuted. The graph preserves the full unpaid KL route while rejecting its degree-only shortcut. No other-agent file, shared registry or public release is changed. Conditional refund preservation is not represented as universal payment.

# one next mathematical action and independent reviewer

{next_action} A096/A001/A073 own the next terminal-core payment. The protected partition is a test contract, not a completed proof: a candidate must pay the retained Gamma-D and cannot merely discard W or transfer spectator energy into the same core budget. Independently review the new A081 adapter and this certificate with A085; alternate A094. The degree theorem now has one complete independent acceptance, but no claim of canonical adoption or integrated-chain approval is made.

# actual persistence receipts or precise save blocker

Saved REPORT, CLAIMS, PROGRESS and byte-identical PACKET_DELTA with packet_ids=[A081], code/out, REVIEW, graph, frozen spec, pilot/full certificates, mutation audit, hash receipts, refutation scope delta and immutable source snapshots. Protocol fields, status length, final Universal bridge paragraph and file sizes are checked. STATUS is two lines, WORKLOG appended and LEARNED updated. out/PERSISTENCE_RECEIPTS and FINAL_VALIDATION record actual byte hashes/checks. No local save blocker. Supervisor copying, shared adoption, remote mirrors, downstream use and independent integrated certificate review remain unobserved. Finalized {now}.

# Universal bridge

This stage moves C018 terminal-KL payment by independently closing A090's degree-coarsening obstruction: the missing conditional refund/I is at least w/2-6 on actual tribes, while the complete bill/I stays at most6. It supplies an exact spectator-compatible partition contract that preserves a non-product seed's full refund without borrowing spectator influence, and consumes the complete A096 and scoped shared-bit C020/C019 transfer reviews. The universal upper-constant improvement is zero: Gamma-D, excess shared collision and complete terminal CE remain unpaid. NEXT audits one signed-Boolean conditional refund/payment with that retained W and one original influence reserve, because the new certificate specifies the exact information that a full-FEI proof must preserve rather than closing another isolated class.
'''
assert all('# '+s+'\n' in report for s in proto['required_per_run']['report_fields']);assert report.rstrip().split('# Universal bridge\n')[-1].startswith('\nThis stage moves C018')
(R/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text(f'STATE: A081 stage 4 complete: A090 degree-refund obstruction independently HOLDS; {exact["assertions"]} exact assertions and eight guards PASS; A096/A097 scoped reviews pinned; {routes} FEI routes conditional; FEI OPEN.\nNEXT: Audit signed-Boolean terminal-core payment retaining conditional W, complete Q and terminal CE on non-product rows/tribes with one influence reserve; A085/A094 review.\n',encoding='utf-8')
if R.name not in (OWN/'WORKLOG.md').read_text(encoding='utf-8'):
    with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n[{now}] {R.name}: independently accepted full A090 degree-coarsened refund obstruction; consumed source-bound A096 full and A097 shared-bit reviews; verified 144 actual Boolean tensors, 684 partitions and named width4 tribes by 8225 exact assertions in {exact["runtime_seconds"]:.3f}s. Conditional W is explicit; protected core/spectator partition cancels no unpaid seed debt. Graph {N} versions/{S} pins/{routes} conditional routes; eight rejection fixtures PASS. Universal terminal KL payment remains open.\n')
if 'Stage 4 refund-contract facts:' not in (OWN/'LEARNED.md').read_text(encoding='utf-8'):
    with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage 4 refund-contract facts: full row KL equals coarse KL plus nonnegative conditional W; coarse retained price equals full retained price plus influence-weighted W. Complete reference-only cells cannot be deleted. A090 tribes obstruction independently HOLDS: degree-only price/I>=w/2, full price/I<=6; dropped refund/I>=w/2-6. For physical tensors the same spectator law cancels from mu/r, and full core subset plus any spectator partition retains full KL exactly; retaining core degree loses only the original core-degree refund, not a paid seed. One-bit shared collision transfer is independently reviewed by A094 only at original one-bit/l1/dimension-dependent scope with full terminal costs. No universal Gamma-D or collision seed reserve has been paid.\n')
files=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or '__pycache__' in str(p) or p.name in ['PERSISTENCE_RECEIPTS.json','FINAL_VALIDATION.json']:continue
    raw=p.read_bytes();assert len(raw)<20*1024*1024;files.append({'path':str(p.relative_to(R)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save(R/'out/PERSISTENCE_RECEIPTS.json',{'saved_at':now,'files':files,'rolling':[{'path':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [OWN/'STATUS.md',OWN/'WORKLOG.md',OWN/'LEARNED.md']]})
assert len((OWN/'STATUS.md').read_text().splitlines())==2;assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes();assert all(not x['eligible_for_mathematical_review'] for x in v['candidate_routes'])
final={'status':'PASS','nodes':N,'source_pins':S,'admitted_scoped_nodes':A,'graph_acyclic':True,'conditional_FEI_routes':routes,'exact_assertions':exact['assertions'],'mutation_fixtures':len(fixtures),'all_routes_have_unresolved_leaves':True,'protocol_fields_exact_with_packet_ids_annotation_normalized':True,'delta_identical':True,'report_ends_with_universal_bridge':True,'files':len(files),'maximum_file_bytes':max(f['bytes'] for f in files),'full_FEI':'OPEN','integrated_review':'PENDING_A085_A094'};save(R/'out/FINAL_VALIDATION.json',final);print(json.dumps(final,indent=2))
