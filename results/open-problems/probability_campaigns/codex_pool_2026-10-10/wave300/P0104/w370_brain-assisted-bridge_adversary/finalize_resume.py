"""Consume narrow referee receipts and checkpoint this resumed task locally."""
import sys
sys.dont_write_bytecode = True
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REVIEWER = Path('~/brain_workers/w371/PEER_VERDICTS.jsonl')
ids = {'w370-P0104-002', 'w370-P0104-003', 'w370-P0104-005'}
verdicts = [json.loads(line) for line in REVIEWER.read_text(encoding='utf-8').splitlines() if line.strip()]
keeps = [v for v in verdicts if v.get('claim_id') in ids]
assert {v['claim_id'] for v in keeps} == ids
assert all(v['verdict'] == 'KEEP' and v['reviewer'] == 'w371' for v in keeps)
receipt_path = ROOT/'review/REFEREE_VERDICTS.jsonl'
receipt_path.write_text(''.join(json.dumps(v, ensure_ascii=False)+'\n' for v in keeps), encoding='utf-8')
lookup = {v['claim_id']:v for v in keeps}

claims_path = ROOT/'CLAIMS.jsonl'
claims = [json.loads(line) for line in claims_path.read_text(encoding='utf-8').splitlines() if line.strip()]
for c in claims:
    if c['id'] in ids:
        c['status'] = 'independently checked proof'
        c['independent_reviewer'] = 'w371; KEEP; review/REFEREE_VERDICTS.jsonl'
        c['independent_review'] = lookup[c['id']]
        for prefix in [
            'DRAFT concept; independent referee pending. ',
            'DRAFT concept; referee pending. ',
            'DRAFT concept; w369 proof audited by w370, referee w371 pending. '
        ]:
            c['statement'] = c['statement'].removeprefix(prefix)
        if c['id'] == 'w370-P0104-002':
            c['remaining_gap'] = 'No iid lattice FPP realization; no P0104 conclusion. Integration and account-level admission are not certified.'
    if c['id'] == 'w370-P0104-source-001':
        c['independent_reviewer'] = 'w371; narrow historical-source KEEP in ~/brain_workers/w371/REVIEW_PACKET.md'
        c['remaining_gap'] = 'The exact primary specialization is recorded in SOURCE_STATUS.json; current global openness remains UNKNOWN. The historical ranking is not a mathematical proof.'
    if c['id'] == 'w370-P0104-006':
        c['statement'] = c['statement'].replace('two fresh gates', 'three fresh gates')
        c['proof_or_counterexample'] = c['proof_or_counterexample'].replace('CPU 80.9% then 88.4%', 'CPU 80.9%, 88.4%, then 85.5% on the resumed check')

new_id = 'w370-P0104-007'
if not any(c['id'] == new_id for c in claims):
    claims.append({
        'id': new_id,
        'kind': 'resumed-validation-receipt',
        'statement': 'The unchanged fresh gate declined the resumed reader-lock runtime checks: CPU 85.5% exceeds the 75% cap; available RAM 4468535296 bytes clears the 2 GiB minimum. No fixture tests ran. Referee w371 separately returned KEEP for claims 002, 003 and 005.',
        'assumptions': ['The same 75% CPU and 2 GiB RAM limits and 20-second budget were retained', 'A mathematical referee receipt is separate from runtime validation, formal checking and live integration'],
        'source': {'gate': 'fresh_compute_gate.json', 'measurement': 'review/RESUME_RECEIPT.json', 'verdicts': 'review/REFEREE_VERDICTS.jsonl'},
        'proof_or_counterexample': 'Command: python -X utf8 ~/brain_workers/w370/test_read_lock.py. Result: not_run, admitted false. Referee decisions copied from the three named claim rows only.',
        'independent_reviewer': 'w371 for the three mathematical claims; engineering validation pending',
        'remaining_gap': 'Runtime lock behavior and integration review remain outstanding. No repair speedup or FPP exponent claim follows.',
        'status': 'numerical evidence'
    })
claims_path.write_text(''.join(json.dumps(c, ensure_ascii=False)+'\n' for c in claims), encoding='utf-8')

state_path = ROOT/'drafts/STATE.json'
state = json.loads(state_path.read_text(encoding='utf-8'))
state['math_review'] = {'reviewer':'w371', 'verdict':'KEEP', 'claim_ids':sorted(ids), 'receipt':'review/REFEREE_VERDICTS.jsonl'}
state['reason'] = 'Staged locally under the worker-folder restriction. The three mathematical claims received w371 KEEP; full bundle/edge integration review and submission remain pending.'
state_path.write_text(json.dumps(state, indent=2)+'\n', encoding='utf-8')

bundle_path = ROOT/'drafts/bundle_001.json'
bundle = json.loads(bundle_path.read_text(encoding='utf-8'))
reviewed_keys = {'uniform-kurtosis-bridge', 'rare-event', 'interval-variance'}
for e in bundle['entries']:
    if e['key'] in reviewed_keys:
        for old in ['independent referee pending', 'referee pending']:
            e['statement'] = e['statement'].replace(old, 'independent mathematical KEEP by w371; integration pending')
        for field,value in e['source'].items():
            if isinstance(value,str):
                e['source'][field] = value.replace('independent referee pending', 'independent mathematical KEEP by w371; integration pending')
        assert e['kind'] == 'concept' and e['proof_text'] is None
bundle_path.write_text(json.dumps(bundle, indent=2)+'\n', encoding='utf-8')

attempt_path = ROOT/'ATTEMPT.md'
attempt = attempt_path.read_text(encoding='utf-8')
note = '\n2026-10-10 resume: w371 independently returned KEEP for claims 002, 003 and 005; exact receipts are in review/REFEREE_VERDICTS.jsonl. This discharges those mathematical referee requests only. The third unchanged compute gate declined runtime checks at CPU 85.5%; the code remains an unvalidated proposal.\n'
if note not in attempt:
    attempt_path.write_text(attempt+note+'\nNEXT: Bound the actual FPP Doob martingale cross and cubic sums relative to Var(T_n)^2 before asserting uniform kurtosis; the reviewed conditional bridge does not provide these bounds.\n', encoding='utf-8')

progress_path = ROOT/'outbox/progress.jsonl'
event = {'agent':'w370', 'row':'S1.P0104', 'event':'w371 independently kept the counterexample, conditional variance bridge and interval correction; resumed runtime gate declined at CPU 85.5%; repair remains unvalidated.', 'evidence':str(ROOT/'review/RESUME_RECEIPT.json'), 'posted':False}
existing = progress_path.read_text(encoding='utf-8') if progress_path.exists() else ''
if json.dumps(event)+'\n' not in existing:
    with progress_path.open('a', encoding='utf-8') as f:
        f.write(json.dumps(event)+'\n')

print(json.dumps({'claims':len(claims), 'independently_checked':sorted(ids), 'runtime_tests':'not_run', 'live_integration':False}))
