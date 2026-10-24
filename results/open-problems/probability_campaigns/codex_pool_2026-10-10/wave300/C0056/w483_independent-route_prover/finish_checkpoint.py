from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

base=Path(__file__).resolve().parent
proof_hash=hashlib.sha256((base/'ATTEMPT.md').read_bytes()).hexdigest()
ref_path=Path('~/brain_workers/w485/REVIEW_PACKET.md')
adv_path=Path('~/brain_workers/w484/CORE_AUDIT.md')
ref_bytes=ref_path.read_bytes()
ref_text=ref_bytes.decode('utf-8')
ref_hash=hashlib.sha256(ref_bytes).hexdigest()
expected_ref_hash='0fa7e98db2b3e825bd129bcb5e5cf641a53f60a569d95fc33420f47946128abc'
assert proof_hash.lower() in ref_text.lower(), 'Referee did not bind this attempt snapshot'
assert ref_hash==expected_ref_hash, 'Referee receipt hash changed; do not infer current KEEP'
adv_bytes=adv_path.read_bytes()
assert proof_hash.lower() in adv_bytes.decode('utf-8').lower(), 'Adversary snapshot differs'
review_dir=base/'reviews'
review_dir.mkdir(exist_ok=True)
(review_dir/'w485_direct_snapshot.md').write_bytes(ref_bytes)
(review_dir/'w484_direct_snapshot.md').write_bytes(adv_bytes)
receipt={'received_at_utc':datetime.now(timezone.utc).isoformat(),'attempt_sha256':proof_hash,
 'referee':{'agent':'w485','path':str(ref_path),'sha256':ref_hash,'snapshot_binding_verified':True,
            'scope':['L1','L2','L3','L4','L5','L6 conditional reduction ONLY','L7 free special case ONLY','L8 abstract counterexample ONLY'],
            'verdict':'SCOPED_DIRECT_KEEP','parent_problem_keep':False,'served_model_evidence':None},
 'adversary':{'agent':'w484','path':str(adv_path),'sha256':hashlib.sha256(adv_bytes).hexdigest(),
             'snapshot_binding_verified':True,'scope':['L1','L2','L3','L4','L5'],'verdict':'SCOPED_DIRECT_KEEP',
             'served_model_evidence':None},
 'different_account_gate_verified':False,'different_model_gate_verified':False,
 'formal_check':False,'parent_result':'NOT_PROVED',
 'not_promoted':'Concept bundle itself, source/model provenance gates, ingestion and retrieval remain unverified.'}
(base/'REVIEW_RECEIPTS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')

claim_rows=[json.loads(line) for line in (base/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
for row in claim_rows:
    if re.fullmatch(r'w483-L[1-8]',row['id']):
        row['review_status']='SCOPED_DIRECT_KEEP_RECEIVED; served-identity gates unverified'
        row['independent_review_evidence']={'reviewer':'w485','receipt':'REVIEW_RECEIPTS.json',
          'attempt_sha256':proof_hash,'review_sha256':ref_hash,'parent_proof_certified':False}
        if row['id'] in ['w483-L1','w483-L2','w483-L3','w483-L4','w483-L5']:
            row['additional_reviewer']='w484; direct scoped KEEP; response-side model evidence unavailable'
        row['remaining_gap']='Scoped auxiliary argument received direct referee KEEP; proof/model provenance gate not verified. Parent marked-pair estimate, nonzero weight and GOE limit are not proved.'+(' Conditional eigenvector mark hypothesis remains UNPROVED.' if row['id']=='w483-L6' else '')
        # Keep the conservative status until the required served-identity gates pass.
        row['status']='proved special case'
(base/'CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in claim_rows),encoding='utf-8')

statement_path=base/'STATEMENT_TO_ADVERSARY.md'
statement_path.write_text(statement_path.read_text(encoding='utf-8').replace('Short source quote (20 words):','Short source quote:'),encoding='utf-8')
source_path=base/'SOURCE_STATUS.json'
source=json.loads(source_path.read_text(encoding='utf-8'))
source['independent_review'].update({'status':'SCOPED_DIRECT_KEEP_RECEIVED','receipt':'REVIEW_RECEIPTS.json',
                                   'attempt_snapshot_verified':True,'parent_result':'NOT_PROVED'})
source['brain_states']['review_note']='Proof L1-L8 has direct scoped KEEP; the six-concept bundle, served-identity gates and seven relation rows are not separately certified.'
source_path.write_text(json.dumps(source,indent=2,ensure_ascii=False),encoding='utf-8')

packet_path=base/'REVIEW_PACKET.json'
packet=json.loads(packet_path.read_text(encoding='utf-8'))
packet['review_status']='SCOPED_DIRECT_KEEP_RECEIVED; MODEL/ACCOUNT GATES UNVERIFIED'
packet['direct_review_receipt']=str(base/'REVIEW_RECEIPTS.json')
packet['brain_states']=dict(source['brain_states'])
for filename,meta in packet['file_hashes'].items():
    meta['sha256']=hashlib.sha256((base/filename).read_bytes()).hexdigest()
packet_path.write_text(json.dumps(packet,indent=2),encoding='utf-8')

next_line='NEXT: w485/coordinator verifies review provenance; the next proof step is a volume-uniform bound on conditional eigenvector-pair marks at fixed nonzero disorder.'
gap=(base/'GAP.md').read_text(encoding='utf-8')
gap=re.sub(r'(?m)^NEXT:.*$',next_line,gap)
(base/'GAP.md').write_text(gap,encoding='utf-8')
report='\n'.join(line for line in (base/'REPORT.md').read_text(encoding='utf-8').splitlines() if not line.startswith('NEXT:')).rstrip()
report+='\n\nDirect review received: w485 KEEP for L1-L8, with L6 conditional and L7 zero-disorder scope; w484 KEEP for L1-L5. Both receipts bind the unchanged ATTEMPT.md snapshot. Served-model/account gates remain unverified, so the claims stay conservatively labeled and the concept bundle remains DRAFT.\n\n'+next_line+'\n'
(base/'REPORT.md').write_text(report,encoding='utf-8')

updated_receipts=[]
mesh='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
for target in ['w485','codex-01a12190']:
    body='C0056 w483 direct scoped KEEP received and hash-bound: w485 L1-L8 (L6 conditional ONLY), w484 L1-L5. Proof SHA256 '+proof_hash+'. Updated evidence: ~/brain_workers/w483/REVIEW_RECEIPTS.json and REVIEW_PACKET.json. Model/account gates UNKNOWN; parent, marked-pair estimate and GOE NOT PROVED. Six-concept bundle remains DRAFT; no ingestion or retrieval claim.'
    result=subprocess.run(['python','-X','utf8',mesh,'send','--agent','w483','--to',target,
       '--topic','probability300/C0056/scoped-review-receipt','--kind','message','--body',body],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=60)
    updated_receipts.append({'to':target,'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
    print(json.dumps(updated_receipts[-1]),flush=True)
(base/'REVIEW_UPDATE_SEND_RECEIPTS.json').write_text(json.dumps(updated_receipts,indent=2),encoding='utf-8')

progress=subprocess.run(['python','-X','utf8','~/primary_directive/pd_progress.py',
 '--event','C0056 w483: exact-snapshot referee KEEP L1-L8; adversary KEEP L1-L5. Conditional mark and GOE gaps persist; model gates unknown, DRAFT only.',
 '--agent','w483','--row','S1.3','--evidence',str(base/'REVIEW_RECEIPTS.json')],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=60)
(base/'FINAL_PROGRESS_RECEIPT.json').write_text(json.dumps({'returncode':progress.returncode,'stdout':progress.stdout,'stderr':progress.stderr},indent=2),encoding='utf-8')
print('Progress:',progress.returncode,progress.stdout.strip(),flush=True)

release=subprocess.run(['python','-X','utf8',mesh,'release','--agent','w483',
 '--resource','~/math-brain-inbox/w483/bundle_001.json',
 '--resource','~/primary_directive/hooks1000/proposals/math-w483.jsonl'],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=60)
(base/'LEASE_RELEASE_RECEIPT.json').write_text(json.dumps({'returncode':release.returncode,'stdout':release.stdout,'stderr':release.stderr},indent=2),encoding='utf-8')
print('Release:',release.returncode,release.stdout.strip(),flush=True)

status=(base/'STATUS.md').read_text(encoding='utf-8')
status=re.sub(r'(?m)^STATE:.*$','STATE: NEEDS_REVIEW',status,count=1)
status=re.sub(r'(?m)^NEXT:.*$',next_line,status,count=1)
status+='\n2026-10-10: Completed measured deliverables and submission. Direct referee KEEP L1-L8 and adversary KEEP L1-L5 bind ATTEMPT SHA256 '+proof_hash+'. Mathematical scope remains conditional/special-case; model/account provenance and bundle/relations certification pending. Six DRAFT concepts, seven supported relation proposals and two hooks submitted; live store untouched. Referee/integration updated and progress posted. STATE NEEDS_REVIEW; parent NOT PROVED.\n'
(base/'STATUS.md').write_text(status,encoding='utf-8')
print(json.dumps({'state':'NEEDS_REVIEW','proof_sha256':proof_hash,'scoped_referee_keep':8,'scoped_adversary_keep':5,
                  'bundle_reviewed':False,'ingested':False,'retrievable':False}),flush=True)
