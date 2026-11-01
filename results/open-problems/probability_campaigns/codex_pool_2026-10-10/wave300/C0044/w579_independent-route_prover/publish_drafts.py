"""Publish only the explicitly authorized draft and rolling hook proposal file."""
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

root=Path(__file__).resolve().parent
inbox=Path('~/math-brain-inbox/w579').resolve()
dest=(inbox/'bundle_001.json').resolve()
hooks=Path('~/primary_directive/hooks1000/proposals/math-w579.jsonl').resolve()
mesh=Path('~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py')
assert dest.parent==inbox and dest.name=='bundle_001.json'
assert hooks.parent==Path('~/primary_directive/hooks1000/proposals').resolve()
r=subprocess.run(['python','-X','utf8',str(mesh),'assert','--agent','w579',
                  '--resource',str(dest),'--resource',str(hooks)],
                 capture_output=True,text=True,encoding='utf-8',timeout=60)
(root/'LEASE_ASSERT_RECEIPT.txt').write_text(r.stdout+r.stderr,encoding='utf-8')
if r.returncode:
    raise RuntimeError('Shared-output lease assertion rejected: '+r.stderr)
validation=json.loads((root/'VALIDATION_RESULTS.json').read_text(encoding='utf-8'))
assert validation['structure_passed'] and validation['theorem_or_lemma_promotions']==0
data=(root/'DRAFT_BUNDLE.json').read_bytes()
inbox.mkdir(parents=False,exist_ok=True)
if dest.exists():
    if dest.read_bytes()!=data:
        raise FileExistsError('Refusing to overwrite a different existing draft: '+str(dest))
else:
    part=(root/'bundle_001.part').resolve()
    assert part.parent==root and part.name=='bundle_001.part'
    part.write_bytes(data)
    # Exact resolved source and destination checked above; single-file rename.
    os.rename(part,dest)
known=set()
if hooks.exists():
    for line in hooks.read_text(encoding='utf-8').splitlines():
        if line.strip(): known.add(json.loads(line)['id'])
proposal_rows=[json.loads(x) for x in (root/'HOOK_PROPOSALS.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
appended=0
with hooks.open('a',encoding='utf-8') as f:
    for p in proposal_rows:
        assert p['proposer']=='w579' and len(p['text'])<=300
        if p['id'] not in known:
            f.write(json.dumps(p,ensure_ascii=False)+'\n')
            known.add(p['id']); appended+=1
when=datetime.now(timezone.utc).isoformat()
state={'target':'C0044','bundle':str(dest),'draft_entries':validation['draft_entries'],
       'relations':validation['relations'],'submitted':{'state':True,'at_utc':when},
       'reviewed':{'state':False,'reviewer':'w581','receipt':None},
       'ingested':{'state':False,'receipt':None},
       'retrievable':{'state':False,'query_receipt':None},
       'theorem_promotions':0,'hook_file':str(hooks),'hook_proposals_appended':appended,
       'note':'Author draft submission only. No integrator invocation or live-store write.'}
(root/'BRAIN_OUTPUT_STATUS.json').write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8')
print(json.dumps(state,indent=2))
