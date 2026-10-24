"""Submit only the explicitly authorized w414 concept draft; never ingest it."""
from datetime import datetime, timezone
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w414')


def main():
    bundle_text = (ROOT / 'bundle_001.json').read_text(encoding='utf-8')
    bundle = json.loads(bundle_text)
    assert bundle['author_agent'] == 'w414'
    assert all(e['kind'] == 'concept' and e['proof_text'] is None
               and e['statement'].startswith('DRAFT;') for e in bundle['entries'])
    INBOX.mkdir(parents=True, exist_ok=True)
    destination = None
    replay = False
    for number in range(1, 201):
        candidate = INBOX / f'bundle_{number:03d}.json'
        partial = candidate.with_suffix('.part')
        if candidate.exists():
            if candidate.read_text(encoding='utf-8') == bundle_text:
                destination, replay = candidate, True
                break
            continue
        if partial.exists():
            continue
        # Exclusive creation plus Windows rename avoids replacing an existing
        # final draft, including one created concurrently by another command.
        with partial.open('x', encoding='utf-8', newline='\n') as handle:
            handle.write(bundle_text)
        partial.rename(candidate)
        destination = candidate
        break
    if destination is None:
        raise RuntimeError('No fresh own-inbox slot; no file overwritten.')
    assert json.loads(destination.read_text(encoding='utf-8')) == bundle
    state_path = ROOT / 'BUNDLE_STATE.json'
    state = json.loads(state_path.read_text(encoding='utf-8'))
    state.update({'submitted': True, 'submitted_at': datetime.now(timezone.utc).isoformat(),
                  'inbox_path': str(destination), 'idempotent_replay': replay,
                  'reviewed': False, 'ingested': False, 'retrievable': False,
                  'live_integrator_executed': False})
    state_path.write_text(json.dumps(state, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(state, indent=2))


if __name__ == '__main__':
    main()
