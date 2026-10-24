"""Stage the explicitly assigned math-brain draft; never edit a live store.

Use only after the local report and audit handoff are ready. All entries clearly
carry independent-audit-pending status. Atomic publication never replaces a
different existing draft or deletes any file.
"""
from pathlib import Path
import json
import os
import subprocess
import uuid

root = Path(__file__).resolve().parent
assert (root/'REPORT.md').is_file() and (root/'AUDIT_REQUEST_w346.md').is_file()
validation = subprocess.run(['python','-X','utf8',str(root/'validate_bundle.py')],
                            capture_output=True,text=True,encoding='utf-8',check=True)
bundle = json.loads((root/'bundle_001.json').read_text(encoding='utf-8'))
raw = (root/'bundle_001.json').read_bytes()
folder = Path('~/math-brain-inbox/w338')
folder.mkdir(parents=True,exist_ok=True)
destination = folder/'bundle_001.json'
if destination.exists():
    if destination.read_bytes()!=raw:
        raise RuntimeError('Existing draft differs; preserve it and choose a new bundle number.')
    action='ALREADY_STAGED_IDENTICAL'
else:
    part = folder/f'bundle_001.{uuid.uuid4().hex}.part'
    with part.open('xb') as f:
        f.write(raw)
        f.flush()
        os.fsync(f.fileno())
    # On Windows rename fails rather than replacing an existing destination.
    part.rename(destination)
    action='STAGED_NEW_DRAFT'
receipt = dict(action=action,path=str(destination),bytes=len(raw),
               entries=len(bundle['entries']),relations=len(bundle['relations']),
               audit_status='PENDING_W346',promoted_solutions=0,store_writes=0,
               validation=json.loads(validation.stdout))
(root/'delivery_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
