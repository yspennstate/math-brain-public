"""Atomically submit the authorized w423 concept draft; never run an integrator."""
from datetime import datetime, timezone
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
claim = json.loads((ROOT / 'MESH_CLAIM_RECEIPT.json').read_text(encoding='utf-8'))
now = datetime.now(timezone.utc)
matching = [c for c in claim.get('acquired', []) if c.get('resource') == 'topic:C0023:reverse-thinning-bridges']
assert claim.get('agent') == 'w423' and len(matching) == 1
assert datetime.fromisoformat(matching[0]['expires_at'].replace('Z', '+00:00')) > now
validation = json.loads((ROOT / 'BUNDLE_VALIDATION.json').read_text(encoding='utf-8'))
assert validation['status'] == 'PASS' and validation['unreviewed_theorem_or_lemma_entries'] == 0
bundle_text = (ROOT / 'bundle_001.json').read_text(encoding='utf-8')
bundle = json.loads(bundle_text)
assert bundle['author_agent'] == 'w423'
assert all(e['kind'] == 'concept' and e['proof_text'] is None for e in bundle['entries'])
inbox = Path('~/math-brain-inbox/w423').resolve()
assert str(inbox).replace('\\', '/').casefold() == '~/math-brain-inbox/w423'
inbox.mkdir(parents=True, exist_ok=True)
destination = None
reused = False
for index in range(1, 100):
    dest = inbox / f'bundle_{index:03d}.json'
    part = inbox / f'bundle_{index:03d}.json.part'
    assert dest.resolve().parent == inbox and part.resolve().parent == inbox
    if dest.exists():
        if dest.read_text(encoding='utf-8') == bundle_text:
            destination, reused = dest, True
            break
        continue
    if part.exists():
        continue
    with part.open('x', encoding='utf-8', newline='\n') as handle:
        handle.write(bundle_text)
        handle.flush()
    part.rename(dest)
    destination = dest
    break
assert destination is not None
states = json.loads((ROOT / 'SUBMISSION_STATUS.json').read_text(encoding='utf-8'))
states['state_semantics'] = 'True means confirmed by evidence; false means unconfirmed, not a claim that no external integration has happened.'
states['submitted'] = {'status': True, 'at': now.isoformat(), 'path': str(destination), 'atomic_part_rename': True, 'reused_identical_file': reused, 'narrow_claim_id': matching[0]['claim_id']}
states['reviewed']['state'] = 'pending independent mathematical verdict'
states['ingested']['state'] = 'unconfirmed; no integrator run by this worker'
states['retrievable']['state'] = 'unconfirmed; no recall receipt'
(ROOT / 'SUBMISSION_STATUS.json').write_text(json.dumps(states, indent=2) + '\n', encoding='utf-8')
for name in ['REPORT.md', 'REVIEW_PACKET.md']:
    with (ROOT / name).open('a', encoding='utf-8') as out:
        out.write('\nDraft submitted by complete .part-to-.json rename: ' + str(destination) + '. Independent review pending; ingestion and retrieval unconfirmed.\n')
(ROOT / 'STATUS.md').write_text('STATE: WORKING\nNEXT: Send the complete measured review packet to w425, verify delivery, and set NEEDS_REVIEW.\n\n2026-10-10: L1-L4 author proofs and geometric interval gap saved. Exact checks PASS (40 identities, 544 configurations, 10,098 thinning pairs). Six concepts and six relations locally validated.\n2026-10-10: Statement delivered first to w424; narrow resource acquired as ' + matching[0]['claim_id'] + '; concept draft submitted atomically to ' + str(destination) + '. No live integrator run; review, ingestion and retrieval unconfirmed.\n', encoding='utf-8')
print(json.dumps({'submitted': True, 'path': str(destination), 'entries': len(bundle['entries']), 'relations': len(bundle['relations']), 'reviewed': False, 'ingested_confirmed': False, 'retrievable_confirmed': False, 'live_integrator_run': False}, indent=2))
