"""Publish only the authorized w492 DRAFT file; no live store integration."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parent
INBOX=Path('~/math-brain-inbox/w492')
MESH='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'

def main() -> None:
    assertion=subprocess.run([sys.executable,'-X','utf8',MESH,'assert','--agent','w492','--resource',str(INBOX)],
                              capture_output=True,text=True,encoding='utf-8',timeout=60)
    if assertion.returncode:
        raise RuntimeError('Inbox lease assertion failed: '+assertion.stdout+assertion.stderr)
    payload=(ROOT/'bundle_001.json').read_bytes()
    bundle=json.loads(payload)
    assert all(entry['kind'] in {'definition','concept'} for entry in bundle['entries'])
    INBOX.mkdir(parents=True,exist_ok=True)
    part=INBOX/'bundle_001.json.part'
    final=INBOX/'bundle_001.json'
    if final.exists():
        if final.read_bytes()!=payload:
            raise RuntimeError('Existing inbox bundle differs; preserve it and choose a new name.')
    else:
        with part.open('xb') as f:
            f.write(payload)
        part.rename(final)
    assert final.read_bytes()==payload
    submitted=datetime.now(timezone.utc).isoformat()
    source_status=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    source_status['brain_states']={'prepared':True,'submitted':True,'reviewed':False,'ingested':False,'retrievable':False}
    source_status['brain_submission']={'path':str(final),'submitted_at_utc':submitted,'kind':'DRAFT concepts/definition'}
    (ROOT/'SOURCE_STATUS.json').write_text(json.dumps(source_status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    packet=json.loads((ROOT/'REVIEW_PACKET.json').read_text(encoding='utf-8'))
    packet['bundle_submission']={'path':str(final),'submitted_at_utc':submitted,'sha256':hashlib.sha256(payload).hexdigest(),
                                'reviewed':False,'ingested':False,'retrievable':False}
    for name in ['SOURCE_STATUS.json','REPORT.md','RELATION_EVIDENCE.jsonl','verify_packet.py']:
        p=ROOT/name
        data=p.read_bytes()
        packet['files'][name]={'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
    (ROOT/'REVIEW_PACKET.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    receipt={'authorized_destination':str(INBOX),'bundle_path':str(final),'sha256':hashlib.sha256(payload).hexdigest(),
      'entries':len(bundle['entries']),'relations':len(bundle['relations']),
      'states':source_status['brain_states'],'lease_assertion':assertion.stdout,'submitted_at_utc':submitted}
    (ROOT/'SUBMISSION_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'submitted':str(final),'entries':len(bundle['entries']),'relations':len(bundle['relations']),
                     'reviewed':False,'ingested':False,'retrievable':False}))

if __name__=='__main__':
    main()
