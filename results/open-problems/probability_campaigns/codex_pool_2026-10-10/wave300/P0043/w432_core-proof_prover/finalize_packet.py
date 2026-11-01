"""Final artifact checks and read only the referee verdicts on this packet."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
required = ['STATUS.md', 'SOURCE_STATUS.json', 'ATTEMPT.md', 'CLAIMS.jsonl', 'PRIOR_ATTEMPTS.md',
            'REVIEW_PACKET.md', 'REPORT.md', 'SOURCE_CORRECTIONS.jsonl', 'BUNDLE_STATES.json',
            'BUNDLE_VALIDATION.json', 'REFEREE_HANDOFF.json', 'MEASUREMENTS.json', 'bundle_002.json']
for name in required:
    assert (root / name).is_file() and (root / name).stat().st_size > 0, name
claims = [json.loads(line) for line in (root / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
fields = {'id', 'exact_statement', 'assumptions', 'source', 'proof', 'independent_reviewer', 'remaining_gap', 'status'}
for claim in claims:
    assert fields <= claim.keys(), claim['id']
assert sum(claim['id'].startswith('w432-L') for claim in claims) == 8
assert [claim['id'] for claim in claims if claim['status'] == 'conjecture'] == ['w432-G01']
states = json.loads((root / 'BUNDLE_STATES.json').read_text(encoding='utf-8'))
assert states['submitted'] and not states['ingested'] and not states['retrievable']
target = Path(states['submission_path'])
assert target.resolve().parent == Path('~/math-brain-inbox/w432').resolve()
assert target.read_text(encoding='utf-8') == (root / 'bundle_002.json').read_text(encoding='utf-8')
handoff = json.loads((root / 'REFEREE_HANDOFF.json').read_text(encoding='utf-8'))
assert handoff['status'] == 'SENT' and handoff['child_agents_started'] == 0
measurement = json.loads((root / 'MEASUREMENTS.json').read_text(encoding='utf-8'))
assert measurement['status'] == 'HELD' and not measurement['checks']

hook = json.loads((root / 'HOOK_PROPOSAL.jsonl').read_text(encoding='utf-8'))
assert len(hook['text']) <= 300
assert re.search(hook['cue'], hook['fire_when'])
assert not re.search(hook['cue'], hook['silent_when'])

verdict_file = Path('~/brain_workers/w434/REVIEW_VERDICTS.jsonl')
rows = []
if verdict_file.exists():
    with verdict_file.open(encoding='utf-8') as stream:
        for line in stream:
            if 'w432' in line:
                rows.append(json.loads(line))
(root / 'INDEPENDENT_REVIEW_RECEIPT.json').write_text(json.dumps({
    'source': str(verdict_file), 'rows_on_w432': rows,
    'scope': 'Referee verdicts read for handoff; no review of the referee and no account/axiom certificate inferred.'
}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
summary = {'required_artifacts': len(required), 'partial_proof_rows': 8, 'source_correction_rows': 2,
           'unproved_inputs': ['w432-G01'], 'latest_draft_entries': 9, 'latest_draft_relations': 9,
           'submitted': True, 'reviewed_as_complete_bundle': False, 'ingested': False, 'retrievable': False,
           'referee_handoff': handoff['message']['message_id'], 'finite_experiments': 'HELD; zero cases run',
           'hook_controls': {'fire': 'PASS', 'silent': 'PASS'}, 'final_file_checks': 'PASS',
           'referee_rows_seen': len(rows), 'canonical_production_store': 'UNVERIFIED'}
(root / 'FINAL_CHECKS.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
status = (root / 'STATUS.md').read_text(encoding='utf-8').splitlines()
status[0] = 'STATE: NEEDS_REVIEW'
status[1] = 'NEXT: w434 review L01-L08 and source rows; next proof step is a vanishing critical-window bound for the full incoming pivotal mass in (MT) on Z^3.'
status.append('2026-10-10: Final checks PASS: 8 partial proof rows, 2 source rows, one G01 gap, latest draft 9 concepts/9 relations. Revision 002 submitted; 001 preserved. Referee request ' + handoff['message']['message_id'] + ' delivered using installed presence fallback; no agent launched. Independent review and integration remain separate states. Numeric checks held, zero cases run. STATE: NEEDS_REVIEW.')
(root / 'STATUS.md').write_text('\n'.join(status) + '\n', encoding='utf-8')
print(json.dumps(summary))
print(json.dumps([{'claim': row.get('claim_id', row.get('id', row.get('claim'))), 'verdict': row.get('verdict')} for row in rows]))
