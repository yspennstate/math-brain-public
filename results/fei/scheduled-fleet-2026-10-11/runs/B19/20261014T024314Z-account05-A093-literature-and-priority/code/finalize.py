from pathlib import Path
import json,hashlib,datetime,urllib.request
R=Path(__file__).resolve().parents[1];A=R.parent.parent
prior=R.parent/'20261013T234909Z-account05-A093-literature-and-priority'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(name,obj):(R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
source=[]
for name,url,loc in [
 ('gmp26.pdf','https://arxiv.org/pdf/2606.00246v2','Proposition 6.1; Theorems 5.3,6.3,6.8; Appendix (32)'),
 ('gmp26.txt','https://arxiv.org/pdf/2606.00246v2','Extracted source sections 5-6 and appendix'),
 ('ckls_corrected.pdf','https://eccc.weizmann.ac.il/report/2013/052/revision/2/download','Theorem 5.11 and Remark 5.1'),
 ('ckls_corrected.txt','https://eccc.weizmann.ac.il/report/2013/052/revision/2/download','Extracted PDF pp.25-26')]:
 p=prior/'out'/name;b=p.read_bytes()
 source.append({'path':str(p),'url':url,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'locator':loc,'acquisition':'REUSED_PINNED_PREVIOUS_RUN'})
try:
 url='https://arxiv.org/abs/2606.00246'
 b=urllib.request.urlopen(url,timeout=20).read();(R/'out/GMP_VERSION_PAGE.html').write_bytes(b)
 source.append({'path':'out/GMP_VERSION_PAGE.html','url':url,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'retrieved_at_utc':now,'regenerate':'python -X utf8 code/finalize.py (urllib.request.urlopen(url,timeout=20))'})
except Exception as e:source.append({'url':url,'save_blocker':str(e),'verification':'Primary page read via web tool this stage; raw HTML save failed'})
for p in [A/'STATUS.md',Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B19\STREAM_NOTES.md')]:
 source.append({'path':str(p),'sha256_before_rolling_update':hashlib.sha256(p.read_bytes()).hexdigest(),'kind':'DISPATCH_INPUT'})
save('out/SOURCE_RECEIPTS.json',source)
claim={'claim_id':'A093-GMP26-CLASS-REPAIR','version':'v1',
 'exact_statement':'For every finite uniform Boolean restriction stopping tree with a single uniform terminal FEI constant C0, Boolean semi-separated children at each internal node give H(f)<=max(C0,12)I(f); monotone tribe-separated nodes give H(f)<=max(C0,14)I(f). Every GMP delta-tribes function H+(G-H)AND_u, where H is disjoint tribes on m bits and G is OR of those bits and one new bit, satisfies H(f)<=23I(f), with disjoint-tribes terminals paid by the reconstructed 14-rate theorem. These are conservative corrections of the source consequences, not optimality or priority claims.',
 'hypotheses':['Uniform measure on {-1,1}^n; f sign-valued; Shannon entropy in bits','Physical finite restriction tree; no repeated query along a path; node reach weights 2^-depth','A common dimension-independent C0 for all terminal functions in the class','Semi-separated children: pq and pr with sign-valued p,q,r on pairwise disjoint coordinate sets','Tribe-separated node: monotone children h and max(h,k) with h,k on disjoint coordinates','Delta-tribes: shared AND width u>=1; disjoint positive widths for H; m=0 allowed with H=-1; G includes one fresh bit'],
 'statement_sha256':'','contributors':['A093'],
 'proof_source':['DERIVATION.md','REPORT.md','code/check_classes.py','out/VALIDATION.json','GMP26 v2 Proposition 6.1 and source class structure'],
 'proof_dependencies':[], 'review_records':[], 'status':'SOURCE_COMPLETE_PENDING_REVIEW',
 'supersedes':[], 'refutes':[], 'first_unproved_line':None,
 'next_consumers':['B19 lead','A090','A085','A028','A041','A069','A095','A099','A100']}
claim['statement_sha256']=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
save('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B19','packet_id':'A093',
 'gap_id':'B19-GMP26-CORRECTION-IMPACT','attempt_id':'A093-class-repair-v1',
 'method':'Reconstruct theorem-level source dependencies with corrected entropy factor and retained refund/terminals; exact finite Boolean and ternary checks',
 'mathematical_delta':'GMP class consequences restored at conservative node rates 12,14,23; self-contained disjoint-tribes terminal bound 14 yields delta-tribes H<=23I. No universal payment or priority claim.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SOURCE_CLASS_REPAIR_PROVED_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':[], 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':'v1'}],
 'source_artifacts':['DERIVATION.md','CITATION_IMPACT.md','out/FROZEN_SPEC.json','out/VALIDATION.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Reconstruct GMP Proposition 5.1 actual monotone wrong-variable family; separate variance-surrogate growth from true decrement growth with terminal core retained; A090/A085 independently review repair.',
 'stagnant_substantive_attempts':0,'blockers':['Independent review and downstream adoption unrecorded.','No universal node-selection/payment bound established.'],
 'packet_ids':['A093']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
proto=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf8'))['required_per_run']
assert set(claim)==set(proto['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in proto['progress_fields']}
report=(R/'REPORT.md').read_text(encoding='utf8')
assert all('## '+x in report for x in proto['report_fields'])
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
cert=json.loads((R/'out/VALIDATION.json').read_text());assert cert['status']=='PASS'
assert cert['script_sha256']==hashlib.sha256((R/'code/check_classes.py').read_bytes()).hexdigest()
(A/'STATUS.md').write_text('STATE: A093 GMP class consequences repaired at node rates 12/14/23 with uniform terminals retained; delta-tribes H<=23I proved; 8,706 exact checks PASS; independent review pending; full FEI OPEN.\nNEXT: A090/A085 review source repair; reconstruct GMP Proposition5.1 wrong-variable Boolean family and distinguish V growth from true decrement growth for C019 with terminal core retained.\n',encoding='utf8')
with (A/'WORKLOG.md').open('a',encoding='utf8') as f:
 f.write(f'\n{now} | {R.name}: Read supervisor board 02:33, unchanged B19 notes and own status. No preceding correction review found. Reconstructed GMP Prop6.1 and Theorems5.3/6.3/6.8 with corrected h<=2sqrt, R<=4I and full terminals; conservative rates12/14/23. Proved terminal disjoint tribes14 internally, hence delta-tribes23. 7290 ternary pairs,256 semi nodes,36 monotone pairs,24 roots/48 prefixes;8706 exact assertions PASS. All four protocol files and rolling records saved locally; independent review pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf8') as f:
 f.write('\n'+now+' | Source repair: V=sum|a²-b²|, D=sum(a-b)²=4Iquery. Correct h<=2sqrt gives E<=V/2; refund R<=D implies Delta<=V/2+4I. GMP semi-separated ternary Prop6.1 V<=4D survives, hence Boolean node rate12. Tribe beta nonempty scaling4 plus empty4I gives V<=20I, rate14. Delta source sectors4+4+30=38I give rate23; disjoint-tribes full tree supplies terminal14. Uniform C0 is essential for class statements. These are conservative source repairs, not new/best constants. Next obstruction question: Proposition5.1 proves V growth at a wrong split, not automatically true-Delta growth.\n')
entries=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20_000_000
  entries.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save('out/ARTIFACT_RECEIPTS.json',{'saved_at_utc':now,'validation':'PASS: protocol field sets, headings, hash, packet compatibility, exact certificate, file sizes','files':entries,'local_only':True,'independent_review':False,'remote_verified':False})
print(json.dumps({'status':'PASS','files_pinned':len(entries),'exact_assertions':cert['exact_assertions'],'statement_sha256':claim['statement_sha256'],'rolling_files_updated':True}))
