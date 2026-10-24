from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
RUN=Path(__file__).resolve().parents[1]; HOME=RUN.parents[1]; BASE=HOME.parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
def canonical(c): return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
orig=[('A013','20261013T222840Z-account05-A013-representation-stability',['DERIVATION.md','REPORT.md','CLAIMS.json','REVIEW_A012.md']),('A097','20261013T222610Z-account05-A097-cross-route-transfer',['DERIVATION.md','CLAIMS.json','BOUNDARY.md']),('A095','20261014T010024Z-account05-A095-restricted-result-extraction',['DERIVATION.md','REPORT.md','CLAIMS.json']),('A094','20261014T001244Z-account05-A094-proof-chain-challenger',['AUDIT.md','CLAIMS.json'])]
source_paths=[BASE/'BOARD.md',BASE/'claude/B18/STREAM_NOTES.md',HOME/'STATUS.md',HOME/'runs/20261013T220217Z-account05-A086-joint-code-referee/RECONSTRUCTION.md']
for a,r,files in orig: source_paths += [BASE/f'agents/{a}/runs/{r}/{f}' for f in files]
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'); source_paths.append(protocol_path)
dump(RUN/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in source_paths])
checkpoint=json.loads((RUN/'out/TWO_CHECKPOINT.json').read_text())
assert checkpoint['completed_pairs']==768 and checkpoint['assertions']==12288
two={**checkpoint,'status':'BOUNDED_PARTIAL_CHECKPOINT_ONLY','reference_pairs':768,'actual_domain':'G words 0..47; H words 37*j modulo 256, j=0..15','planned_pairs':4096,'later_completed_unsaved_pairs_not_credited':76,'cutoff_seconds':55}
dump(RUN/'out/TWO_RESULTS.json',two)
results={m:json.loads((RUN/f'out/{m.upper()}_RESULTS.json').read_text()) for m in ['one','two','boundary']}
total=sum(v['assertions'] for v in results.values()); assert total==19522
dump(RUN/'out/EXACT_RESULTS.json',{'jobs':results,'credited_assertions':total,'floating_point_signs_used':False,'two_bit_full_domain_completed':False})
claims=[]
targets=[('A013',orig[0][1],'A013-ONE-SHARED-BIT-MUX-TRANSPORT','PARTIALLY_INDEPENDENTLY_RECONSTRUCTED_LOCAL','Sections 1-5,7: calibrated full-reference debt, whole label chain, one-bit erasure/CE/influence and growing-width actual Boolean boundary. Section 6 positive-cell/root/restriction ledger and recursive activation grammar NOT reviewed.'),('A095',orig[2][1],'A095-RANK-KL-EQUIVALENCE','PARTIALLY_INDEPENDENTLY_RECONSTRUCTED_NEW_APPLICATION_LOCAL','Version 3 new shared-t application only: DERIVATION sections 1-5, minority cap, all-private-dimension linear-tax optimization, calibrated-reference debt, sharp asymptotic coefficient. Retained rank/KL equivalence and earlier activation/common-spine applications NOT reviewed.'),('A094',orig[3][1],'A094-BALANCED-TERMINAL-TENSOR-SELECTOR-BOUNDARY','INDEPENDENTLY_RECONSTRUCTED_AT_FULL_STATED_SCOPE_LOCAL','Entire exact claim: actual bent/flip boundary, physical influences, arbitrary q and prescribed reference tensor, balanced zero-empty-atom specialization and bounded full H/I.')]
for a,r,cid,status,scope in targets:
 p=BASE/f'agents/{a}/runs/{r}/CLAIMS.json'; c=next(c for c in json.loads(p.read_text(encoding='utf8')) if c['claim_id']==cid)
 plain=hashlib.sha256(c['exact_statement'].encode()).hexdigest(); canon=canonical(c)
 assert c['statement_sha256'] in [plain,canon]
 c['review_records'].append({'reviewer':'A086/account05','verdict':'HOLDS_AT_EXPLICIT_REVIEW_SCOPE','scope':scope,'proof':str(RUN/'RECONSTRUCTION.md'),'validation':str(RUN/'out/EXACT_RESULTS.json'),'source_claims_sha256':sha(p),'declared_statement_sha256':c['statement_sha256'],'canonical_statement_hypotheses_sha256':canon,'plain_statement_sha256':plain,'substantive_repair_supplied':False,'contributor_conflict':False,'method':'Independent coefficient/sector-label/physical influence reconstruction, new Fraction implementation, exact log-prime identities and outward rational signs; all-dimensional analytic proof independent of bounded finite domain'})
 c['status']=status; claims.append(c)
new={'claim_id':'A086-BENT-FLIP-EXCLUSIVE-CHILD-SLACK-CERTIFICATE','version':1,'exact_statement':'For every even k>=4, let b be the quadratic bent sign on k binary uniform coordinates, bprime its actual zero-point sign flip, epsilon=2^-k and M their fresh fair selector. Exact child references have zero shared-atom calibration savings and zero posterior mismatch, yet Delta(M)/epsilon>=k-log2(16/9). Their price-two average child slack S_2=[2I(b)-H(b)+2I(bprime)-H(bprime)]/2=2k epsilon+[k-H(bprime)]/2 pays the selector excess Delta(M)-2epsilon without reusing a terminal bill: S_2>Delta(M)-2epsilon, hence H(M)<2I(M), for every such k. The all-k proof uses the shared-k linear tax for k>=6 and an outward rational-log certificate at k=4. For any Boolean q on an independent block physically shared by both children and any normalized complete finite-cost supplied spectral reference R_q, the fixed product reference R_q tensor P_M has CE=c_q+H(M)<c_q+2I(M) and exact deficit D(P_q||R_q); c_q<=K I(q) therefore gives CE<=max(K,2)I(qM). No arbitrary overlapping-child slack bound or universal terminal-reference admission is asserted.',
 'hypotheses':['Uniform finite cubes; binary coordinates for the quadratic sign; even k>=4 and a fresh physical selector','Actual point flip at the zero input, not arbitrary independent spectral weights','Independent arbitrary Boolean q, reference R_q normalized and positive on true support with finite cost','All information quantities bits; ideal CE with separate integer output rounding'],
 'statement_sha256':'','contributors':['A086/account05; bent/flip boundary and terminal-tensor setup credited to A097/A094, linear-tax clause to A095'],'proof_source':{'path':str(RUN/'RECONSTRUCTION.md'),'locator':'Section 5','validation':str(RUN/'out/RESERVE_CERTIFICATES.json')},
 'proof_dependencies':[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':3,'scope':'Only new shared-k linear-tax clause','status':'Independently reconstructed here at explicit scope; earlier clauses not premises'}],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A094','A085','A097','A095','A039','B18','B20']}
new['statement_sha256']=canonical(new); claims.append(new); dump(RUN/'CLAIMS.json',claims)
next_action='Audit a named nonreused reference-slack reserve S_K on a non-flat nonlinear shared row, proving Delta-Kd<=S_K and its transport through one composition while retaining arbitrary terminal R_q; A094/A085 review stress reserve.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B18','packet_id':'A086','gap_id':'C020-SHARED-DATA-COLLISION-REFERENCE-PAYMENT','attempt_id':'A086-stage4-shared-collision-audit','method':'Independent complete-reference and signed physical reconstruction, bounded exact finite validation, analytic all-width optimization and child-slack extraction',
 'mathematical_delta':'A013 one-bit/interface boundary clauses and A095 v3 linear shared-width application HOLD at partial broad-statement scope; full A094 balanced terminal tensor HOLD. Price-two exact child slack pays the bent/flip stress family for all even widths, arbitrary terminal bill retained.',
 'deliverable_status':'COMPLETE_LOCAL_WITH_EXPLICIT_PARTIAL_FINITE_DOMAIN','mathematical_status':'THREE_SCOPED_REVIEWS_HOLD; NEW_STRESS_RESERVE_AUTHOR_PROVED_PENDING_REVIEW; UNIVERSAL_FEI_OPEN',
 'claim_versions_used':['A013-ONE-SHARED-BIT-MUX-TRANSPORT@1','A095-RANK-KL-EQUIVALENCE@3:new shared-width clause','A094-BALANCED-TERMINAL-TENSOR-SELECTOR-BOUNDARY@1'],
 'claims_created_or_changed':[str(c['claim_id'])+'@'+str(c['version']) for c in claims],'source_artifacts':[str(p) for p in source_paths],
 'next_consumers':['A013','A095','A097','A094','A085','A039','B18','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Arbitrary overlapping nonlinear child-reference slack transport is unproved; terminal reference admission is unpaid.','A013 section-6 cover/grammar and older A095 equivalence/activation clauses explicitly outside this review.','Full planned two-bit finite domain not completed; only saved 768-pair checkpoint credited.'],'packet_ids':['A086']}
dump(RUN/'PROGRESS.json',progress); dump(RUN/'PACKET_DELTA.json',progress)
now=datetime.now(timezone.utc).isoformat()
(HOME/'STATUS.md').write_text('STATE: Stage 4 complete: A013 interface/A095 linear-tax clauses HOLD; full A094 tensor HOLD; bent/flip price-two child reserve proved pending review; 19,522 credited exact assertions; FEI OPEN.\nNEXT: Audit non-flat shared-row reference slack Delta-Kd<=S_K and one-use recursive transport with arbitrary terminal R_q; A094/A085 review stress reserve; broad unreviewed clauses remain explicit.\n',encoding='utf8')
for f,entry in [('WORKLOG.md','Consumed new shared-data results instead of duplicating one-bit target. Independently reconstructed A013 one-bit interface/boundary, A095 v3 new linear-tax clause and full A094 balanced arbitrary-terminal tensor. Saved exact reference-sector/debt checks and child-slack proof for bent/flip stress, including all-even-width analytic continuation. One-bit 6,912 checks passed. First two-bit attempt interrupted with no credited output; revised 55-second cutoff reached at 844 pairs, credit only durable 768-pair/12,288-check checkpoint. Boundary/tensor 322 checks passed. Total 19,522, finite domain honest. Initial missing cutoff corrected; no source repair.'),('LEARNED.md','Every shared-only atom must be calibrated individually to remove posterior mismatch; off-target reference fibers need normalized kernels. A013 one-bit common character yields B<=4d; A095 collision mass delta<=min(d*,2^t d*^2) yields linear tax t+2+3/ln2 and sharp asymptotic coefficient one. On exact bent/flip child references both calibration saving and posterior mismatch are zero, so neither alone pays the growing selector excess. Actual price-two average child slack 2k*2^-k+[k-H(bprime)]/2 pays the excess for all even k>=4 (analytic k>=6, exact k=4 certificate), with arbitrary independent terminal reference CE retained. This does not prove arbitrary-row or recursive reserve ownership. Common rational-grid log rounding is rigorous, but external polling alone does not enforce pilot runtime; use internal cutoff and durable checkpoints.')]:
 with (HOME/f).open('a',encoding='utf8') as out: out.write('\n'+now+' '+RUN.name+': '+entry+'\n')
protocol=json.loads(protocol_path.read_text()); req=protocol['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in req['progress_fields']}
for c in claims: assert set(c)==set(req['claim_fields'])
assert canonical(new)==new['statement_sha256']
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
report=(RUN/'REPORT.md').read_text(encoding='utf8')
for h in req['report_fields']: assert '## '+h in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len((HOME/'STATUS.md').read_text().splitlines())==2
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file():
  assert p.stat().st_size<20*1024*1024
  receipts.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(RUN/'out/PERSISTENCE_RECEIPTS.json',{'saved_at':now,'protocol_field_checks':'PASS','local_only':True,'files':receipts,'rolling_files':[{'path':str(HOME/f),'sha256':sha(HOME/f)} for f in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'saved_run':RUN.name,'protocol_checks':'PASS','claims':len(claims),'credited_assertions':total,'two_bit_pairs_credited':768,'universal_FEI':'OPEN'}))
