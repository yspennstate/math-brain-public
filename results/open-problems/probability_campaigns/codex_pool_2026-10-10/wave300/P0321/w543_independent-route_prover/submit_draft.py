"""Submit the explicitly authorized worker DRAFT only; never invoke ingestion."""
import datetime
import difflib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
INBOX=Path('~/math-brain-inbox/w543')
assert INBOX.resolve()==Path('~/math-brain-inbox/w543').resolve()
validation=json.loads((ROOT/'VALIDATION.json').read_text(encoding='utf-8'))
assert validation['checks_failed']==0
body=(ROOT/'bundle_001.json').read_text(encoding='utf-8')
draft=json.loads(body)
assert draft['author_agent']=='w543'
assert all(e['kind'] in ('definition','concept') for e in draft['entries'])
INBOX.mkdir(exist_ok=True)
destination=None
for index in range(1,1000):
    candidate=INBOX/('bundle_%03d.json'%index)
    partial=INBOX/('bundle_%03d.part'%index)
    if candidate.exists():
        if candidate.read_text(encoding='utf-8')==body:
            destination=candidate
            break
        continue
    if partial.exists():
        continue
    assert candidate.parent.resolve()==INBOX.resolve()
    with partial.open('x',encoding='utf-8') as f:
        f.write(body)
        f.flush()
    # Complete file first; rename only within the explicitly authorized inbox.
    partial.rename(candidate)
    destination=candidate
    break
if destination is None:
    raise RuntimeError('No unused draft slot; no existing data overwritten')
assert destination.read_text(encoding='utf-8')==body
live=destination.as_posix()
(ROOT/'patches'/'01_p0321_draft_bundle.diff').write_text(''.join(difflib.unified_diff([],body.splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live)),encoding='utf-8')
status={'target':'P0321','worker':'w543','bundle_path':str(destination),
    'entry_count':len(draft['entries']),'relation_count':len(draft['relations']),
    'submitted':{'state':'submitted','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                 'receipt':'complete JSON renamed from .part; exact readback matched'},
    'reviewed':{'state':'scoped_auxiliary_KEEP_by_w544_and_w545' if (ROOT/'AUDIT_RECEIPTS.json').exists() else 'pending',
               'independent_reviewer':'w545','different_login_provenance':'UNVERIFIED','coordinator_admission':'pending'},
    'ingested':{'state':'not_observed','responsible':'validating coordinator'},
    'retrievable':{'state':'not_observed','responsible':'post-ingestion retrieval check'},
    'live_store_mutated_by_worker':False,'proof_promotion':False}
(ROOT/'PUBLICATION_STATUS.json').write_text(json.dumps(status,indent=2),encoding='utf-8')
print(json.dumps(status,indent=2))
