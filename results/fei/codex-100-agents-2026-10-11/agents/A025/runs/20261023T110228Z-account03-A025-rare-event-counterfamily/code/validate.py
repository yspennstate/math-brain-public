"""Readback protocol schemas, hashes, exact receipts, scope and bounded artifacts."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]; home=R.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
claimkeys=set('claim_id version exact_statement hypotheses statement_sha256 contributors proof_source proof_dependencies review_records status supersedes refutes first_unproved_line next_consumers'.split())
progresskeys=set('protocol_revision run_id stream packet_id gap_id attempt_id method mathematical_delta deliverable_status mathematical_status claim_versions_used claims_created_or_changed source_artifacts next_consumers next_action stagnant_substantive_attempts blockers packet_ids'.split())
claims=read(R/'CLAIMS.json'); progress=read(R/'PROGRESS.json')
assert set(progress)==progresskeys
assert progress['packet_ids']==['A025'] and progress['packet_id']=='A025'
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for q in claims:
    assert set(q)==claimkeys and q['version']==5
    assert hashlib.sha256(q['exact_statement'].encode('utf-8')).hexdigest()==q['statement_sha256']
    assert q['status']=='AUTHOR_PROVED_AT_STATED_SCOPE_PENDING_INDEPENDENT_REVIEW'
report=(R/'REPORT.md').read_text(encoding='utf-8')
headings=['exact target, quantifiers, hypotheses and units','sources actually read, revisions and theorem locators','complete derivation or exact first unsupported line','executed validation with domain, arithmetic, commands and outputs','proof dependencies and changed downstream conclusions','one next mathematical action and independent reviewer','actual persistence receipts or precise save blocker']
assert [s[2:] for s in report.splitlines() if s.startswith('# ')]==headings
assert report.strip().split('\n\n')[-1].startswith('Universal bridge:')
results={s:read(R/'out'/f'{s}.json') for s in ('pilot','main','scalar','replay')}
assert all(x['status']=='PASS' for x in results.values())
assert results['main']['cases']==24576 and results['main']['roots']==6144
assert results['replay']['cases']==76 and results['replay']['phase_queries']==152
assert results['pilot']['seconds']<60 and results['main']['seconds']<600
assert results['scalar']['seconds']<60 and results['replay']['seconds']<180
assert any(x['charge']=={'15':'1/8'} for x in results['main']['constant_family_receipts'])
for row in results['replay']['receipts']:
    for key in ('old_control','new_DATA'):
        assert len(row[key]['both_inherited_KL'])==2 and len(row[key]['both_target_KL'])==2
assert len((home/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and '__pycache__' not in p.parts:
        assert p.stat().st_size<20*1024*1024,(p,p.stat().st_size)
        if p.name not in ('ARTIFACT_MANIFEST.json','VALIDATION.json'):
            manifest.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
for record in read(R/'out/SOURCE_PINS.json'):
    assert hashlib.sha256(Path(record['path']).read_bytes()).hexdigest()==record['sha256'],record['path']
(R/'out/ARTIFACT_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
result={'status':'PASS','claim_fields':len(claimkeys),'progress_fields':len(progresskeys),'protocol_revision':progress['protocol_revision'],'files_hashed':len(manifest),'exact_assertions':sum(x['assertions'] for x in results.values()),'independent_person_review':'PENDING','full_fei':'OPEN','remote_copy':'UNVERIFIED'}
(R/'out/VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
