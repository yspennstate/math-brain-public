from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];TEAM=A.parents[1]
OLD=A/'runs/20261022T231100Z-fleet03-A099-candidate-assembly'
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
save(R/'out/FROZEN_SPEC.json',{'at':stamp,'helper_version':'A099-v8 independent checker, '+hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest(),
 'actual_Boolean_family':'ALL labelled n=2 pilot; ALL labelled n=3 primary; parity3 profile-change control',
 'parameter_domain':'eta in {1/4,1/2}, gamma in {1/2,3/4}; calibrated true/uniform source; occupied-support subprobability; Q vacuum fixed and uniform residual nonempty mass',
 'case_count':'pilot16 tables*4 source/floor pairs*3 policies=192; main256*4*3=3072 full adaptive ledgers; no count combines pilot/main',
 'symmetry':'NONE; every labelled table', 'arithmetic':'Fraction, exact prime-log expressions;18-term atanh rational intervals with proved remainder',
 'memory_estimate_MB':120,'max_runtime_seconds_per_command':55,'automatic_dimension_increase':False,
 'policies':'0 no reset;1 first reset when first outcome0, repeat on descendants and stop old outcome1 at depth2;2 first eligible reset at depth>=2 when last outcome1; every branch retained',
 'max_physical_dimension':3,'source_checker_imported':False})
claims=rd(OLD/'CLAIMS.json');save(R/'CLAIMS.json',claims)
p=rd(OLD/'PROGRESS.json');p.update(run_id=R.name,attempt_id='A099-assembly-v8',method='Independent reconstruction and one-source synthesis of supplied-reference history-transfer chain',
 mathematical_delta='CHECKPOINT: repeated original-source calibrated return and first-frontier proofs consumed; exact independent reconstruction pending; conditional nonempty profile liability isolated.',
 deliverable_status='CHECKPOINT',mathematical_status='VALIDATION_PENDING_FULL_FEI_OPEN',claims_created_or_changed=[],source_artifacts=[str(R/'out/FROZEN_SPEC.json')],
 next_action='Finish independent supplied-reference proof audit; retain original version/hash and exact remaining shape-payment leaf.',
 blockers=['Universal influence-priced source/floor open','Actual changed conditional-nonempty profile payment open','Two integrated full-candidate audits pending'])
save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
fields=rd(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']['report_fields']
(R/'REPORT.md').write_text('# A099 candidate assembly v8 checkpoint\n\n'+'\n\n'.join('## '+s+'\n\nCheckpoint: proof intake complete; validation/assembly in progress.' for s in fields)+'\n\n## Universal bridge\n\nC024 supplied-reference history transfer is being assembled; universal source pricing and changed nonempty-profile payment remain open.\n',encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A099 v8 checkpoint saved; reconstructing supplied-reference first-frontier and repeated original-source canonical returns; FEI OPEN.\nNEXT: Verify complete query/reset ledgers, assemble exact sources and retire only canonical-return liability; changed nonempty profile stays unpaid.\n',encoding='utf-8')
sources=[Path('~/AGENTS.md'),Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),TEAM/'BOARD.md',TEAM/'claude/B20/STREAM_NOTES.md',OLD/'CANDIDATE_MANUSCRIPT.tex',OLD/'CLAIMS.json',OLD/'out/PROOF_DEPENDENCIES.json']
for agent,run,files in [
 ('A096','20261023T010221Z-fleet03-A096-live-gap-ledger',['REPORT.md','DERIVATION.md','CLAIMS.json']),
 ('A097','20261023T021120Z-fleet03-A097-cross-route-transfer',['REPORT.md','DERIVATION.md','CLAIMS.json']),
 ('A085','20261022T234859Z-fleet03-A085-certificate-adversary',['REPORT.md','PROOF.md','CLAIMS.json']),
 ('A098','20261023T031803Z-fleet03-A098-resource-reallocation',['REPORT.md','REVIEW.md','CLAIMS.json'])]:
 sources += [TEAM/'agents'/agent/'runs'/run/f for f in files]
sources += [TEAM/'agents/A050/STATUS.md',TEAM/'agents/A079/STATUS.md']
receipts=[]
for pth in sources:
 raw=pth.read_bytes();raw.decode('utf-8-sig');receipts.append({'path':str(pth),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':'UTF-8'})
save(R/'out/SOURCE_RECEIPTS.json',receipts)
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+': v8 starts from current board. A085 closes our immediate-conversion scoped review; A096/A097/A098 deliver arbitrary exit trees and repeated canonical returns. Freeze small independent reconstruction before evaluation. No broad new candidate.\n')
print('CHECKPOINT_SAVED; SPEC_FROZEN',len(receipts))
