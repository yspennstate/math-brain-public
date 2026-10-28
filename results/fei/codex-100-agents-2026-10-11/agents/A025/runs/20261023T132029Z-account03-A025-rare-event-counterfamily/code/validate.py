"""Protocol/source/receipt readback; mathematical checks live in check.py/replay.py."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]; home=R.parents[1]
rd=lambda p:json.loads(p.read_text(encoding='utf-8'))
protocol=rd(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
progress=rd(R/'PROGRESS.json'); claims=rd(R/'CLAIMS.json')
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert progress['packet_ids']==['A025'] and progress['packet_id']=='A025'
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for x in claims:
    assert set(x)==set(protocol['claim_fields'])
    assert hashlib.sha256(x['exact_statement'].encode('utf-8')).hexdigest()==x['statement_sha256']
    assert x['version']==6 and x['status']=='AUTHOR_PROVED_AT_STATED_SCOPE_PENDING_INDEPENDENT_REVIEW'
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert [x[2:] for x in report.splitlines() if x.startswith('# ')]==protocol['report_fields']
assert report.strip().split('\n\n')[-1].startswith('Universal bridge:')
outputs={s:rd(R/'out'/f'{s}.json') for s in ('pilot','main','family','replay')}
assert all(x['status']=='PASS' for x in outputs.values())
assert outputs['pilot']['roots']==32 and outputs['pilot']['query_nodes']==224 and outputs['pilot']['seconds']<60
assert outputs['main']['roots']==512 and outputs['main']['query_nodes']==3584 and outputs['main']['seconds']<300
assert outputs['main']['positive_calibrations']==732
assert outputs['family']['cases']==16 and outputs['family']['seconds']<60
assert outputs['replay']['roots']==42 and outputs['replay']['family_cases']==6 and outputs['replay']['seconds']<180
assert outputs['replay']['frontier_snapshots']==200
assert all(x['selector_refund']=={} for x in outputs['family']['witnesses'])
for x in outputs['main']['receipts']:
    assert len(x['both_inherited_KL'])==len(x['both_target_KL'])==2
p=rd(R/'out/HELPER_PROVENANCE.json')
assert hashlib.sha256((R/p['target']).read_bytes()).hexdigest()==p['sha256']==hashlib.sha256(Path(p['source']).read_bytes()).hexdigest()
for x in rd(R/'out/SOURCE_PINS.json'):
    # A live BOARD can advance after the read; proof files must remain immutable.
    if Path(x['path']).name!='BOARD.md':assert hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256']
assert len((home/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file():
        assert p.stat().st_size<20*1024*1024
        if '__pycache__' not in p.parts and p.name not in ('ARTIFACT_MANIFEST.json','VALIDATION.json'):
            manifest.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(R/'out/ARTIFACT_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
out={'status':'PASS','files_hashed':len(manifest),'exact_assertions':sum(x['assertions'] for x in outputs.values()),'claim_version':6,'independent_person_review':'PENDING','full_fei':'OPEN','remote_copy':'UNVERIFIED'}
(R/'out/VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))
