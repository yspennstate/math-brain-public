from pathlib import Path
import json,hashlib,datetime
run=Path(__file__).resolve().parents[1]; agent=run.parents[1]
def save(p,x): p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
final=json.loads((run/'out/FINAL_VALIDATION.json').read_text(encoding='utf-8'))
final['final_baseline_replay']='Stopped by 59-second runtime guard; original 5958-assertion certificate retained; no second pass claimed.'
final['saved_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
save(run/'out/FINAL_VALIDATION.json',final)
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(final['saved_at']+': Final restored baseline replay reached runtime guard; preserved original 5958-assertion PASS and recorded exact failed replay receipt. No further repetition; mathematical all-dimensional proofs, full n=4 certificate and separate root reset certificate remain complete.\n')
manifest=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_SHA256.json':
        assert p.stat().st_size<20*1024*1024
        manifest.append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
for p in [agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md']:
    manifest.append({'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
save(run/'out/ARTIFACT_SHA256.json',manifest)
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
print(json.dumps({'status':'FINAL_LOCAL_READBACK_PASS','files_hashed':len(manifest),'failed_replays_recorded':2,'complete_certified_assertions':437915,'full_FEI':'OPEN'}))
