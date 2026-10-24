"""Submit exactly one explicitly authorized inbox draft; never ingest it."""
from pathlib import Path
import json

root = Path(__file__).resolve().parent
validation = json.loads((root/'VALIDATION.json').read_text(encoding='utf-8'))
assert validation['status'] == 'PASS'
source = root/'drafts/bundle_001.json'
payload = source.read_text(encoding='utf-8')
bundle = json.loads(payload)
assert bundle['author_agent'] == 'w400'
assert all(e['kind'] == 'concept' and e['proof_text'] is None for e in bundle['entries'])
destination = Path(r'~\math-brain-inbox\w400\bundle_001.json')
part = destination.with_suffix('.part')
destination.parent.mkdir(parents=True,exist_ok=True)
if destination.exists():
    assert destination.read_text(encoding='utf-8') == payload, 'different existing bundle; do not overwrite'
else:
    assert not part.exists(), 'existing partial draft; do not overwrite'
    part.write_text(payload,encoding='utf-8')
    part.rename(destination)
assert json.loads(destination.read_text(encoding='utf-8')) == bundle
handoff = json.loads((root/'BRAIN_HANDOFF.json').read_text(encoding='utf-8'))
handoff.update(submitted=True,submitted_path=str(destination),submission_receipt='complete JSON written via .part rename under clm-566fec9e28; lease assertion checked before this command',reviewed=False,ingested=False,retrievable=False,next='w401 independently checks original proofs; validating coordinator integrates only after review.')
(root/'BRAIN_HANDOFF.json').write_text(json.dumps(handoff,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'submitted':True,'entries':len(bundle['entries']),'path':str(destination),'reviewed':False,'ingested':False,'retrievable':False}))
