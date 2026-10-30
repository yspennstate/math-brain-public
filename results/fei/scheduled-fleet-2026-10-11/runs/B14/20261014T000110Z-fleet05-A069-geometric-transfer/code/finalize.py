from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1];ROOT=A.parents[1]
P=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
old=A/'runs/20261011T224507Z-fleet05-A069-geometric-transfer'
stage2=A/'runs/20261012T043929Z-fleet05-A069-geometric-transfer'
review=ROOT/'agents/A070/runs/20261013T212602Z-fleet05-A070-analytic-route-referee'
partial=ROOT/'agents/A017/runs/20261013T220934Z-fleet05-A017-recursive-addressing/REVIEW.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads(P.read_text(encoding='utf-8-sig'))
result=json.loads((R/'out/CHECK.json').read_text())
assert result['result']=='PASS' and result['cases']==69890 and result['seconds']<60
parent=json.loads((old/'CLAIMS.json').read_text())[0]
accepted=json.loads((stage2/'CLAIMS.json').read_text())[0]
dependencies=[{'claim_id':parent['claim_id'],'version':1,'statement_sha256':parent['statement_sha256'],'acceptance':'A070 independent acceptance at scope, first-stage report','source':str(old/'REPORT.md')}]
save(R/'out/REVIEW_RECEIPTS.json',{'stage2_claim':accepted['claim_id'],'statement_sha256':accepted['statement_sha256'],'whole_claim_acceptance':{'reviewer':'A070','verdict':'ACCEPT_AT_STATED_SCOPE_NO_REPAIR','source':str(review/'DERIVATION.md'),'sha256':sha(review/'DERIVATION.md'),'locator':'Section 3'},'partial_acceptance':json.loads(partial.read_text()),'new_claim_review':'PENDING'})
statement=('For every fixed singleton-leaf hierarchy T with internal arity 2 or 3 and '
 'L_T(S)=1+sum_v b_v*1{S meets C_v}, put Gamma_T(u)=sum uhat(S)^2 L_T(S), W_T(u)=Gamma_T(u)-1. '
 'For actual Boolean u,w, W_T(uw)=W_T(u)+W_T(w)-4sum_v b_v P(D_v(u)=D_v(w)=1), '
 'where D_v is disagreement under independent resampling of C_v with its outside held fixed. '
 'For three Boolean signs g,q1,q2, Gamma_T(g*q1*q2)=Gamma_T(g)+W_T(q1)+W_T(q2)'
 '-4sum_v b_v P(D_v(g)+D_v(q1)+D_v(q2)>=2). '
 'For disjoint nonempty coordinate blocks C,U,V,Y of sizes r,s,t,k, compatible events '
 'A={C=c*,U=u*}, B={C=c*,V=v*}, masks q1=1-2*1_A,q2=1-2*1_B and fixed '
 'binary tree T=(T_Y,(T_C,(T_U,T_V))), W_T(qj)<=6I(qj) and '
 'I(q1)+I(q2)<=2I(q1*q2), hence H(g*q1*q2)<=Gamma_T(g*q1*q2)<=Gamma_T(g)+12I(q1*q2) '
 'for every Boolean source g. If g=h(Y) has Gamma_(T_Y)(h)<=K I(h), then '
 'H(g*q1*q2)<=max(K+2,12)I(g*q1*q2). Source-dependent cancellation and a universal source-cost payment are not assumed.')
hyp=['Uniform actual Boolean signs; entropy and code lengths in bits; I is physical pivotal influence.',
 'Tree and ordered child coordinate cells are fixed before sampling the Fourier set.',
 'D_v uses independent uniform resampling inside C_v and identical outside coordinates.',
 'Compatible-mask conclusion requires r,s,t,k>=1 and the common assignment c* to agree.',
 'Edit operation is sequential flips/XOR, so the intersection is flipped twice.',
 'Arbitrary-source conclusion retains Gamma_T(g); it is not replaced by an unproved K I(g).',
 'Final-influence closure additionally requires an independent Y-only source with the specified paid core code.']
canonical=json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':'))
claim={'claim_id':'A069-BOOLEAN-MASK-REFUND','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(canonical.encode()).hexdigest(),'contributors':['fleet05/A069'],'proof_source':{'path':str(R/'DERIVATION.md'),'sha256':sha(R/'DERIVATION.md'),'locators':'equations (1)-(10)'},'proof_dependencies':dependencies,'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A070','A088','A094','A017','A067','B05','B13','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields']);save(R/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B14','packet_id':'A069','gap_id':'G-A069-STABLE-ENCODING','attempt_id':'A069-stage3-simultaneous-mask-refund','method':'Boolean cell-resampling disagreement parity; exact simultaneous refund; fixed aligned-mask hierarchy and net physical influence; integer Walsh and resampling certificates','mathematical_delta':'C020 exact shared-variable code-product refund and complete two-compatible-subcube mask surcharge <=12 I(net mask), retaining full source cost; previous stage accepted by A070 and partial interface by A017; final-influence/source payment remains open.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT; NEW_INDEPENDENT_REVIEW_AND_MIRRORS_PENDING','mathematical_status':'SCOPED_THEOREM_AUTHOR_PROVED; FULL_FEI_OPEN','claim_versions_used':dependencies+[{'claim_id':accepted['claim_id'],'version':1,'statement_sha256':accepted['statement_sha256'],'use':'independent whole-claim acceptance consumed; no repair'}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],'source_artifacts':['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/REVIEW_RECEIPTS.json','out/SOURCE_MANIFEST.json'],'next_consumers':claim['next_consumers'],'next_action':'Introduce one shared-control dependence in g with unequal conditional core references, compare exact simultaneous refund to lost physical influence and both terminal bills.','stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A069']}
assert set(progress)=={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
sources=[P,ROOT/'BOARD.md',ROOT/'claude/B14/STREAM_NOTES.md',old/'REPORT.md',old/'CLAIMS.json',stage2/'DERIVATION.md',stage2/'CLAIMS.json',review/'REPORT.md',review/'DERIVATION.md',partial]
save(R/'out/SOURCE_MANIFEST.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sources])
report=(R/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().split('\n')[-1].startswith('This stage moves C020')
save(R/'out/SCHEMA_CHECK.json',{'claim_fields':'PASS','progress_fields':'PASS (packet_ids parenthetical is annotation)','report_fields':'PASS','statement_hash':'PASS','compatibility_copy':'IDENTICAL','exact_cases':result['cases'],'exact_assertions':result['assertions']})
(A/'STATUS.md').write_text('STATE: A069 stage3 complete: exact Boolean mask refund and overlapping-subcube surcharge <=12 I(net mask); 69,890 cases / 144,390 exact checks PASS; stage2 accepted by A070; new review pending; FEI OPEN.\nNEXT: A070/A088/A094 review; one shared-control source dependence with unequal core references: compare exact refund against lost final influence and retain both terminal bills.\n',encoding='utf-8')
marker='2026-10-14 00:01 UTC stage 3:'
if marker not in (A/'WORKLOG.md').read_text():
 with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(marker+' Read current board/unchanged B14 lead, consumed A070 whole stage2 acceptance and A017 partial S1-S5 acceptance. Derived exact resampling-XOR product code subadditivity and one simultaneous refund, avoiding false physical-overlap-only cross payment. Compatible overlapping subcube masks paid by 12 times net mask influence; arbitrary source Gamma retained. Frozen 69,890 cases / 144,390 exact checks PASS in 6.499 s. Universal final-influence conversion open; new review/mirror pending.\n')
fact='Stage 3 simultaneous refund:'
if fact not in (A/'LEARNED.md').read_text():
 with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
  f.write(fact+' W_T(u)=2 sum b_v P(resampling C_v changes u). Boolean product changes combine by XOR, so W_T(uw)=W_T(u)+W_T(w)-4 sum b_v P(both change). This is hierarchy CODE-cost subadditivity, not general entropy subadditivity.\n')
  f.write('For g*q1*q2, one refund event per cell pair is >=2 of the three factors changing: Gamma(final)=Gamma(g)+W(q1)+W(q2)-4 sum b_v P(at least2). It preserves positive edit/edit Fourier cross and exact source/edit rebates; ownership here is cell-resampling, not a physical stopping-tree budget.\n')
  f.write('Compatible overlapping point-block masks with nonempty common and private blocks use T=(Y,(C,(U,V))); W(qj)<=6I(qj), sum input I<=2I(net mask), so Gamma(g*q)<=Gamma(g)+12I(q). Identical masks cancel and are outside the private-block hypotheses. Arbitrary g=q also cancels final influence; retain source Gamma instead of claiming universal final I payment.\n')
assert len((A/'STATUS.md').read_text().splitlines())==2
files=sorted(p for p in R.rglob('*') if p.is_file() and p.name!='RECEIPTS.json')+[A/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
for p in files:assert p.stat().st_size<20_000_000
save(R/'out/RECEIPTS.json',{'scope':'LOCAL_ONLY; new independent review, supervisor copy and mirrors pending','files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]})
print(json.dumps({'schema':'PASS','cases':result['cases'],'assertions':result['assertions'],'receipt_files':len(files),'receipts_sha256':sha(R/'out/RECEIPTS.json')},indent=2))
