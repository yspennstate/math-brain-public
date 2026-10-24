from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
result=json.loads((R/'out/LEAN_RESULT.json').read_text())
log=(R/'out/LEAN_CHECK.txt').read_text(encoding='utf-8')
assert result['exit_code']==0 and 'sorryAx' not in log and 'error:' not in log
assert 'four_corner_enclosure' in log and 'old_negative_rule_reverses' in log
statement='For all rational a,b,c,d,x,y, if 0<c, c<=y<=d and a<=x<=b, then min(a/c,a/d,b/c,b/d)<=x/y<=max(a/c,a/d,b/c,b/d).'
hyp=['all variables rational','0<c','c<=y<=d','a<=x<=b','exact rational arithmetic; no entropy unit']
canonical=json.dumps({'exact_statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':'))
claim={'claim_id':'A083-SIGNED-RATIONAL-INTERVAL-DIVISION','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(canonical.encode()).hexdigest(),'contributors':['A083'],'proof_source':{'run_id':R.name,'path':'code/RationalDivision.lean','theorem':'FEICertificate.four_corner_enclosure'},'proof_dependencies':[],'review_records':[],'status':'KERNEL_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A085','A073','A090','A094']}
(R/'CLAIMS.json').write_text(json.dumps([claim],indent=2)+'\n',encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B17','packet_id':'A083','gap_id':'G-A083-SIGNED-INTERVAL-SOUNDNESS','attempt_id':'A083-1','method':'Lean core rational sign-split proof, kernel-decided regression witnesses','mathematical_delta':'Universal rational four-corner division rule formally checked; concrete B09 sign-reversal risk isolated. No new FEI bound.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_LEMMA_KERNEL_CHECKED_FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':['A083-SIGNED-RATIONAL-INTERVAL-DIVISION-v1'],'source_artifacts':['REPORT.md','FORMAL_SCOPE.md','code/RationalDivision.lean','out/LEAN_CHECK.txt','out/LEAN_RESULT.json','out/source_inventory.json'],'next_consumers':['A085','A090','A094','A073'],'next_action':'A090/A094 reconstruct rational proof and A085 audit one new certificate using the rule; do not rebuild general formalization infrastructure.','stagnant_substantive_attempts':0,'blockers':['B17 STREAM_NOTES.md absent at stage start; independent review and supervisor mirror pending'],'packet_ids':['A083']}
for n in ['PROGRESS.json','PACKET_DELTA.json']:
    (R/n).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
fields=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())['required_per_run']
assert set(progress)==set(x.split(' (')[0] for x in fields['progress_fields'])
assert set(claim)==set(fields['claim_fields'])
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: A083 signed rational interval division kernel-checked; two regression propositions checked; local packet complete, review pending; full FEI OPEN.\nNEXT: A090/A094 review exact proof and axiom scope; A085 apply the rule to a new certificate, preserving the real-log analytic obligations.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp}: Read protocol, board, campaign interfaces and B09 repair. A081 already certified the fixed margin. Mathlib import attempts reached the 1400 MiB cap and failed; narrowed to Lean core Rat. Corrected one draft inequality reversal. Final kernel check passed in {result["seconds"]:.3f}s, peak commit {result["peak_commit_bytes"]} bytes. No universal FEI term paid.\n')
(A/'LEARNED.md').write_text('Signed numerator interval division by a strictly positive interval requires extrema of four endpoint quotients. The old (a/d,b/c) rule reverses even [-1,-1]/[1,2]. Lean core Init.Data.Rat.Lemmas suffices for the universal rational theorem and kernel-decided regression examples. Narrow Mathlib imports still reached the memory cap on this machine. Real log enclosure, tail estimates, Python agreement and global FEI payment remain outside this formal certificate.\n',encoding='utf-8')
receipts=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        data=p.read_bytes(); assert len(data)<20*2**20
        receipts.append({'path':str(p.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(R/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps({'saved_at':stamp,'scope':'local persistence only; no mirror receipt','files':receipts},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'schema':'PASS','claims':1,'local_files_hashed':len(receipts),'status':'COMPLETE_LOCAL','full_FEI':'OPEN'}))
