"""Submit only the task-authorized worker draft; never invoke the integrator."""
import datetime as dt
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
inbox = Path('~/math-brain-inbox/w558').resolve()
inbox.mkdir(parents=True, exist_ok=True)
data = (ROOT / 'bundle_001.json').read_bytes()
destination = inbox / 'bundle_001.json'
if destination.exists():
    if destination.read_bytes() != data:
        raise RuntimeError('Existing worker inbox draft differs; preserve it and choose a new file explicitly.')
    state = 'already present with identical bytes'
else:
    partial = inbox / 'bundle_001.part'
    assert partial.resolve().parent == inbox and destination.resolve().parent == inbox
    if partial.exists():
        raise RuntimeError('A preexisting part file must be preserved; choose a new filename explicitly.')
    partial.write_bytes(data)
    partial.rename(destination)
    state = 'submitted by complete part-file rename'
assert destination.read_bytes() == data
when = dt.datetime.now(dt.timezone.utc).isoformat()
source_path = ROOT / 'SOURCE_STATUS.json'
source = json.loads(source_path.read_text(encoding='utf-8'))
source['store_states']['submitted'] = True
source['draft_submission'] = {'path': str(destination), 'submitted_at_utc': when,
                              'state': state, 'integrator_invoked': False}
source_path.write_text(json.dumps(source, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
packet_path = ROOT / 'REVIEW_PACKET.json'
packet = json.loads(packet_path.read_text(encoding='utf-8'))
packet['states']['submitted'] = True
packet['submitted_at_utc'] = when
packet['draft_path'] = str(destination)
packet['artifact_hashes']['SOURCE_STATUS.json']['sha256'] = hashlib.sha256(source_path.read_bytes()).hexdigest()
packet['artifact_hashes']['bundle_001.json'] = {'path': str(ROOT / 'bundle_001.json'),
                                               'sha256': hashlib.sha256(data).hexdigest()}
packet_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()
lifecycle = {'candidate': 'C0047', 'author': 'w558', 'updated_at_utc': when,
             'prepared': True, 'submitted': True, 'reviewed': False, 'ingested': False, 'retrievable': False,
             'draft_path': str(destination), 'review_packet_path': str(packet_path),
             'review_packet_sha256': packet_hash, 'integrator_invoked': False,
             'author_served_model_evidence': None, 'referee_served_model_evidence': None,
             'review_request_receipt': None, 'integration_routing_receipt': None,
             'NEXT': 'w560 audits factor-line independence and the degree correction; integration follows the required review/model gates.'}
(ROOT / 'LIFECYCLE.json').write_text(json.dumps(lifecycle, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'submitted': str(destination), 'entries': 6, 'relations': 6,
                  'review_packet_sha256': packet_hash, 'integrator_invoked': False}, indent=2))
