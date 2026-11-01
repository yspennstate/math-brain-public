from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

base=Path(__file__).resolve().parent
packet_path=base/'REVIEW_PACKET.json'
packet=json.loads(packet_path.read_text(encoding='utf-8'))
assert (base/'STATUS.md').read_text(encoding='utf-8').splitlines()[0]=='STATE: NEEDS_REVIEW'
assert packet['review_status'].startswith('SCOPED_DIRECT_KEEP_RECEIVED')
changed=[]
for filename,meta in packet['file_hashes'].items():
    actual=hashlib.sha256((base/filename).read_bytes()).hexdigest()
    if actual!=meta['sha256']:
        changed.append(filename)
        meta['sha256']=actual
# The mathematical attempt remains byte-frozen; metadata may change after receipts.
review=json.loads((base/'REVIEW_RECEIPTS.json').read_text(encoding='utf-8'))
assert packet['file_hashes']['ATTEMPT.md']['sha256']==review['attempt_sha256']
packet['checkpoint_hashes_refreshed_at_utc']=datetime.now(timezone.utc).isoformat()
packet_path.write_text(json.dumps(packet,indent=2),encoding='utf-8')
assert all(hashlib.sha256((base/f).read_bytes()).hexdigest()==m['sha256'] for f,m in packet['file_hashes'].items())
assert Path(packet['submitted_draft_path']).read_bytes()==(base/'DRAFT_bundle_001.json').read_bytes()
source=json.loads((base/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
assert source['current_openness']=='UNKNOWN' and source['parent_result']=='NOT_PROVED'
assert source['brain_states']['submitted'] and not source['brain_states']['reviewed']
assert not source['brain_states']['ingested'] and not source['brain_states']['retrievable']
assert not source['independent_review']['different_model_gate_passed']
assert not source['independent_review']['different_account_gate_passed']
assert json.loads((base/'MATH_CHECKS.json').read_text(encoding='utf-8'))['status']=='PASS'
receipt={'status':'PASS','scope':'final checkpoint metadata and snapshot integrity, not proof or integration certification',
 'refreshed_after_review_metadata_edits':changed,'attempt_still_byte_frozen':True,
 'concept_bundle_still_draft':True,'parent_result':'NOT_PROVED',
 'state':'NEEDS_REVIEW','timestamp_utc':datetime.now(timezone.utc).isoformat()}
(base/'FINAL_CHECKPOINT_VALIDATION.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt),flush=True)
