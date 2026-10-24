"""Check draft contracts, edge references, and patch application in this folder."""
import json
import datetime as dt
import os
from pathlib import Path
import subprocess
import time

ROOT=Path(__file__).resolve().parent
bundle_fields={'spec','author_agent','bundle_slug','entries','relations'}
entry_fields={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
source_fields={'source_id','url','revision','license','excerpt'}
kinds={'definition','lemma','theorem','concept'}
relation_kinds={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
start=time.perf_counter(); entries=edges=0
drafts=sorted((ROOT/'drafts').glob('bundle_*.json'))
assert len(drafts)==10
for file in drafts:
    bundle=json.loads(file.read_text(encoding='utf-8'))
    assert set(bundle)==bundle_fields
    assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w341'
    assert 0<len(bundle['entries'])<=200
    keys={e['key'] for e in bundle['entries']}
    assert len(keys)==len(bundle['entries'])
    for entry in bundle['entries']:
        assert set(entry)==entry_fields
        assert set(entry['source'])==source_fields
        assert entry['kind'] in kinds and entry['statement']
        assert '[audit pending w347]' in entry['title']
        assert entry['source']['license'].startswith('owner-own-work')
        if entry['kind'] in {'lemma','theorem'}:
            assert len(entry['proof_text'])>100
        else:
            assert entry['proof_text'] is None
        entries+=1
    for rel in bundle['relations']:
        assert rel['from_key'] in keys and rel['kind'] in relation_kinds
        assert ('to_key' in rel)^('to_existing_logical' in rel)
        if 'to_key' in rel:assert rel['to_key'] in keys
        assert 'From: "' in rel['rationale'] and 'To: "' in rel['rationale']
        assert '\n' not in rel['rationale']
        edges+=1
hooks=[json.loads(line) for line in (ROOT/'proposals'/'math-w341.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(hooks)==4
for h in hooks:
    assert len(h['text'])<=300 and h['fire_when']!=h['silent_when'] and h['evidence']

# The path of every patch target has been explicitly inspected below. Both git
# commands run outside any original repository, with discovery stopped here.
stage=ROOT/'patch_application_checks'/dt.datetime.now().strftime('%Y%m%dT%H%M%S%f')
assert stage.resolve().is_relative_to(ROOT.resolve())
stage.mkdir(parents=True,exist_ok=False)
env=dict(os.environ)
env['GIT_CEILING_DIRECTORIES']=str(ROOT.parent)
env['GIT_OPTIONAL_LOCKS']='0'
patch_records=[]
for patch in sorted((ROOT/'patches').glob('*.diff')):
    targets=[]
    for line in patch.read_text(encoding='utf-8').splitlines():
        if line.startswith('+++ b/'):
            relative=line[6:]
            final=(stage/relative).resolve()
            assert final.is_relative_to(stage.resolve())
            assert relative.startswith(('math-brain-inbox/w341/','primary_directive/hooks1000/proposals/'))
            assert not final.exists()
            final.parent.mkdir(parents=True,exist_ok=True)
            final.write_bytes(b'')
            targets.append(relative)
    assert targets
    command=['git','apply','--directory',stage.relative_to(ROOT).as_posix(),str(patch)]
    check=subprocess.run(command[:2]+['--check']+command[2:],cwd=ROOT,env=env,capture_output=True,text=True)
    assert check.returncode==0,check.stdout+check.stderr
    applied=subprocess.run(command,cwd=ROOT,env=env,capture_output=True,text=True)
    assert applied.returncode==0,applied.stdout+applied.stderr
    for relative in targets:
        local=ROOT/'drafts'/Path(relative).name if relative.startswith('math-brain-inbox/') else ROOT/'proposals'/Path(relative).name
        assert (stage/relative).read_bytes()==local.read_bytes()
    patch_records.append({'patch':patch.name,'target_files':len(targets),'git_apply_check':'PASS','local_replay_bytes':'IDENTICAL'})
rows=[json.loads(line) for line in (ROOT/'READY_ROWS.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(rows)==entries and all(r['counted_keeps']==0 for r in rows)
claims=json.loads((ROOT/'CLAIMS_FOR_BLIND_AUDIT.json').read_text(encoding='utf-8'))
assert len(claims)==entries
claimed={(r['problem'],r['key']):r for r in claims}
for pid,bundle_file in zip(['P0288','C0034','C0151','P0127','P0456','C0058','C0082','C0126','P0014','P0042'],drafts):
    bundle=json.loads(bundle_file.read_text(encoding='utf-8'))
    for entry in bundle['entries']:
        claim=claimed[pid,entry['key']]
        assert claim['claim']==entry['statement'] and claim['assumptions']==entry['assumptions']
        if entry['proof_text'] is not None:
            proof_name=entry['source']['url'].rsplit('/',1)[-1]
            assert entry['proof_text']==(ROOT/'proofs'/proof_name).read_text(encoding='utf-8')
result={'status':'PASS','bundles':len(drafts),'typed_nodes':entries,'edges':edges,'rows':len(rows),'hook_proposals':len(hooks),'patches':patch_records,'stage':str(stage),'seconds':round(time.perf_counter()-start,3),'live_files_modified':0}
(ROOT/'measurements'/'package_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2),flush=True)
