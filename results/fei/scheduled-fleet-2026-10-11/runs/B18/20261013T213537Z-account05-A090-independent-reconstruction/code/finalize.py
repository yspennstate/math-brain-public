from pathlib import Path
import json, hashlib, datetime

r=Path(__file__).resolve().parents[1]
root=r.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
source=root.parent/'A099'/'runs'/'20261012T044129Z-account05-A099-candidate-assembly'
c=json.loads((source/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
recorded=c['statement_sha256']
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
c['review_records']=[x for x in c['review_records'] if x.get('reviewer')!='A090']+[{
    'reviewer':'A090','timestamp':now,'verdict':'HOLDS_AT_STATED_SCOPE',
    'independent_method':'Statement-only activation coefficients; tail-supremum cutoff reserve; independent integer Walsh and Fraction/log-dictionary validation',
    'proof_source':str(r/'REPORT.md'),'validation_source':str(r/'out'/'CHECK.json'),
    'source_recorded_statement_sha256':recorded,
    'local_UTF8_exact_statement_sha256':c['statement_sha256'],
    'scope_guard':'Only low-influence v2 fragment accepted; integrated A097/B05 applications and universal R_ge2 payment not accepted',
    'checkpoint_correction':'Reviewer omitted positive pure-control root slices in provisional equality; source formula is correct and needs no repair.'}]
c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A090'
statement=('For every fixed integer ell>=2 and every finite-valued s:N->[0,infinity) with s(N)=o(N), '
 'define R_geell(F)=sum_i sum_(T subset [N] minus {i}, |T|>=ell) phi(Fhat(T)^2,Fhat(T union {i})^2), '
 'where phi(x,y)=(x+y)h2(y/(x+y)) in bits with continuous zero conventions. The supremum '
 'K_geell(s) of R_geell(F)/I(F) over all finite N-bit Boolean signs with 0<I(F)<=2^-s(N) '
 'equals K_E=sup_(all finite nonconstant Boolean f) B(f)/I(f), in the extended reals. '
 'For every actual seed f and integers m,k>=1, let h=chi_Z*f^tensor(m) on ell fresh parity bits, '
 'F=1+A_k(h-1), q=2^-k, with all blocks disjoint. Then B_data(F)=qmB(f), '
 'I(F)=q(mI(f)+ell+k), R_geell(F)=qmB(f)+kq+2kq^2 sum_(r=ell..k-1) binom(k-1,r), '
 'and R_ge2(F)=qmB(f)+2kq(1-kq). Each parity coordinate z has B_z(F)=0 and Inf_z(F)=q>0, '
 'so min_(i relevant) B_i(F)/Inf_i(F)=0. No finiteness of K_E or selected-witness transport is asserted.')
new={'claim_id':'A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS','version':1,'exact_statement':statement,
 'hypotheses':['Uniform finite physical cube; actual Boolean signs; normalized Fourier coefficients',
 'Bits, ordinary influence, continuous zero conventions','ell>=2 fixed; m,k positive; all blocks disjoint',
 'Finite-valued nonnegative s(N)=o(N), not necessarily monotone','Ratio-limit seed is nonconstant'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A090'],
 'proof_source':{'path':str(r/'REPORT.md'),'locators':['equations (8)-(14)','PARITY_TAIL_PROOF.tex'],
 'checker':'code/check_transfer.py','output':'out/CHECK.json',
 'attribution':'B20/A099 tensor-activation interface; new exact remaining-layer transport derived by A090.'},
 'proof_dependencies':[],'review_records':[{'reviewer':'A094','verdict':'PENDING'},{'reviewer':'A085','verdict':'PENDING_ALTERNATE'}],
 'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A099','A096','A064','A005','A089','A094','A085','B18','B20']}
(r/'CLAIMS.json').write_text(json.dumps([c,new],indent=2),encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':r.name,'stream':'B18','packet_id':'A090',
 'gap_id':'OPEN-C018-HIGHER','attempt_id':'A090-independent-reconstruction-2',
 'method':'Statement reconstruction, exact edge partition, parity-tail transfer and nonmonotone cutoff asymptotics',
 'mathematical_delta':'A099 low-influence v2 HOLDS; all fixed-tail cutoff suprema equal K_E without additive loss; exact R_ge2=qmB+2kq(1-kq) and relevant zero-erasure parity bits distinguish aggregate/selectable scope.',
 'deliverable_status':'COMPLETE_LOCAL_SAVED',
 'mathematical_status':'SCOPED_SOURCE_ACCEPTED_NEW_REFINEMENT_PENDING_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':c['claim_id'],'version':2,'acceptance':'INDEPENDENTLY_RECONSTRUCTED_BY_A090',
 'source_recorded_statement_sha256':recorded,'local_UTF8_exact_statement_sha256':c['statement_sha256']},
 {'claim_id':'C018','version':'supplement-2026-10-11','acceptance':'BASELINE_RECONSTRUCTED','used_for':'C_FEI corollary only'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':2,'change':'independent scoped review'},
 {'claim_id':new['claim_id'],'version':1,'change':'new author-proved refinement; not self-accepted'}],
 'source_artifacts':['REPORT.md','CLAIMS.json','BLIND_RECONSTRUCTION.md','CHECKPOINT_CORRECTION.md',
 'RECONSTRUCTION_COMPARISON.md','PARITY_TAIL_PROOF.tex','FROZEN_SPEC.json','SPEC_REVISION.md',
 'code/check_transfer.py','out/CHECK.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':['A094','A085','A099','A096','A064','A005','A089','B18','B20'],
 'next_action':'Audit one normalized derivative reference for R_ge2 on parity-lifted arbitrary-tensor activations, retaining terminal seed entropy and one physical influence ledger.',
 'stagnant_substantive_attempts':0,'blockers':['Universal higher-layer payment R_ge2<=KI is open; no access blocker.'],
 'packet_ids':['A090']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:
    (r/name).write_text(json.dumps(progress,indent=2),encoding='utf-8')
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
fields=json.loads(protocol.read_text(encoding='utf-8-sig'))['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in fields['progress_fields']}
assert all(set(x)==set(fields['claim_fields']) for x in [c,new])
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
check=json.loads((r/'out'/'CHECK.json').read_text());assert check['status']=='PASS'
hash_note=('Source metadata discrepancy: A099 recorded exact-statement hash '+recorded+
 ' differs from UTF8 SHA256 '+c['statement_sha256']+'. Both are preserved in the review record; '
 'source-file byte hashes pin the actual statement. No hash convention is asserted and no mathematical corruption is inferred.\n')
report=r/'REPORT.md';s=report.read_text(encoding='utf-8')
s=s.replace('out/SOURCE_MANIFEST.json pins exact byte hashes.',
 'out/SOURCE_MANIFEST.json pins exact byte hashes. '+hash_note.strip())
report.write_text(s,encoding='utf-8')
with (r/'RECONSTRUCTION_COMPARISON.md').open('a',encoding='utf-8') as f:f.write('\n'+hash_note)
(root/'STATUS.md').write_text(
 'STATE: Stage 2 complete: A099 low-influence v2 HOLDS; exact tail supremum=K_E refinement proved pending review; 4,420 exact checks PASS; FEI OPEN. Older B18 census target superseded by A071/A082; half-tax already closed.\n'
 'NEXT: A094/A085 review parity-tail formula; A099/A096 supply terminal-inclusive R_ge2 reference payment on arbitrary-tensor activations with one physical influence budget.\n',encoding='utf-8')
with (root/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' | '+r.name+' | Read board/B18/status/protocol. Retired duplicate N5/half-tax targets. '
    'Saved statement-only A099 checkpoint; corrected own omitted positive pure-control root slices after source comparison. '
    'A099 v2 HOLDS. Derived exact R_ge2=qmB+2kq(1-kq), zero-erasure relevant parity bits and '
    'all-fixed-tail low-influence suprema=K_E. 4420 exact assertions/312 cases PASS, 1.789s. '
    'Preserved source hash discrepancy; new theorem pending review, universal tail bill remains open.\n')
with (root/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage 2: balanced activation has B_data=qB(h)+q(1-q)sum phi(1,hhat_i^2)'
    '+sum phi((1-q)^2,q^2hhat_i^2). Nonempty-control/empty-core coefficients are -q and cannot be deleted. '
    'Fresh parity ell>=2 kills h singletons: B_data=qmB(seed), I=q(mI+ell+k), '
    'R_geell=qmB(seed)+kq+2kq^2 sum_(r=ell..k-1) C(k-1,r); R_ge2=qmB(seed)+2kq(1-kq). '
    'Each fresh parity bit has B=0 and influence q. For any fixed ell>=2 and finite s=o(N), '
    'cutoff sup R_geell/I=K_E exactly; new refinement pending independent review, no finiteness proof. '
    'For nonmonotone cutoff, eta_m=sup_(N>=mn)s(N)/N->0 and '
    'k=ceil(4(n+1)m sqrt(eta_m)+2sqrt(m))=o(m) leaves enough cutoff reserve.\n')
inputs=[protocol,root.parents[1]/'BOARD.md',root.parents[1]/'claude'/'B18'/'STREAM_NOTES.md',
 source/'CLAIMS.json',source/'REFINEMENT_PROOF.md',source/'CANDIDATE_MANUSCRIPT.tex',
 Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents\sources\ERASURE_REDUCTION.md'),
 root/'runs'/'20261011T231429Z-account05-A090-independent-reconstruction'/'REPORT.md']
inputs+=list((root.parent/'A096'/'runs').glob('*/CLAIMS.json'))+list((root.parent/'A082'/'runs').glob('*/CLAIMS.json'))
manifest=[]
for p in inputs:
    b=p.read_bytes();manifest.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(r/'out'/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(r/'out'/'SCHEMA_VALIDATION.json').write_text(json.dumps({'status':'PASS','exact_claim_field_sets':True,
 'exact_progress_field_set':True,'progress_delta_byte_equal':True,'local_statement_hashes_checked':True,
 'source_hash_discrepancy_preserved':recorded!=c['statement_sha256'],'new_claim_self_accepted':False},indent=2),encoding='utf-8')
receipts={'timestamp':now,'status':'LOCAL_SAVED','external_copy':'NOT_PERFORMED','files':[]}
for p in list(r.rglob('*'))+[root/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]:
    if p.is_file() and p.name!='RECEIPTS.json':
        b=p.read_bytes();assert len(b)<20*1024*1024
        receipts['files'].append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(r/'out'/'RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
print(json.dumps({'schema':'PASS','source_review':'HOLDS_AT_SCOPE','new_claim':'PENDING_INDEPENDENT_REVIEW',
 'exact_assertions':check['assertions'],'receipted_files':len(receipts['files'])}))
