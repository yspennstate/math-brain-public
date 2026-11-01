"""Place the authorised own draft and hook proposal; never ingest or change the live store."""
from pathlib import Path
import hashlib
import json
import time

BASE = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w489')
HOOK = Path('~/primary_directive/hooks1000/proposals/math-w489.jsonl')

def load(name):
    return json.loads((BASE / name).read_text(encoding='utf-8'))

def write_local(name, obj):
    (BASE / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def main():
    validation = load('VALIDATION.json')
    draft_check = load('INTEGRATOR_VALIDATION.json')
    assert validation['structural_checks_passed']
    assert draft_check['valid'] and not draft_check['errors']
    assert not validation['mathematical_proof_verified']
    receipts = [json.loads(s) for s in (BASE / 'COMMUNICATION_RECEIPTS.jsonl').read_text(encoding='utf-8').splitlines()]
    assert any(r['recipient'] == 'w490' and r['kind'] == 'claim' for r in receipts), 'statement-first notice must be queued'
    source = BASE / 'DRAFT_bundle_001.json'
    bundle = json.loads(source.read_text(encoding='utf-8'))
    assert bundle['author_agent'] == 'w489'
    INBOX.mkdir(exist_ok=True)
    part, final = INBOX / 'bundle_001.part', INBOX / 'bundle_001.json'
    if final.exists() or part.exists():
        raise FileExistsError('Own draft already exists; preserve it and review before preparing a new numbered draft.')
    with part.open('x', encoding='utf-8', newline='\n') as handle:
        handle.write(source.read_text(encoding='utf-8'))
    part.rename(final)

    hook = {
        'id': 'spectral-first-moment-w489-01', 'area': 'math', 'event': 'PostToolUse',
        'cue': 'A proof infers almost-sure spectral absolute continuity solely from a bound on E Im G, a first Poisson moment, or the density of an averaged measure.',
        'fire_when': 'The returned Stieltjes density clause is used to establish its own absolute-continuity premise, or a bounded annealed first moment is promoted to samplewise absolute continuity.',
        'silent_when': 'A genuine p>1 Poisson moment, joint uniform-integrability proof, or an independently conditioned exceptional-set argument has already excluded sample singular mass.',
        'text': 'Check what the resolvent bound averages and its moment order before claiming samplewise absolute continuity. Bounded first moments and an annealed density permit atoms. Identify an Lp/uniform-integrability or independent-exceptional-set argument.',
        'evidence': '~/brain_workers/w489/ATTEMPT.md L1-L4; BRAIN_HYPOTHESIS_COMPARISON.md; FILTER_MEASUREMENT.json (1/4 -> 1/1 relevant returned Poisson cards).',
        'proposer': 'w489',
    }
    assert len(hook['text']) <= 300
    prior = HOOK.read_text(encoding='utf-8') if HOOK.exists() else ''
    if any(json.loads(line).get('id') == hook['id'] for line in prior.splitlines() if line.strip()):
        raise ValueError('Hook proposal ID already exists; do not duplicate it.')
    with HOOK.open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(hook, ensure_ascii=False) + '\n')
    write_local('HOOK_PROPOSAL.json', hook)

    state = load('SOURCE_STATUS.json')
    state.update({'submitted': True, 'reviewed': False, 'ingested': False, 'retrievable': False,
                  'inbox_draft': str(final)})
    write_local('SOURCE_STATUS.json', state)
    claims = [json.loads(s) for s in (BASE / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
    for claim in claims:
        claim['submitted'] = True
    (BASE / 'CLAIMS.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in claims), encoding='utf-8')
    packet = load('REVIEW_PACKET.json')
    packet.update({'submitted': True, 'reviewed': False, 'ingested': False, 'retrievable': False,
                   'inbox_draft': str(final), 'hook_proposal': str(HOOK),
                   'statement_first_message_id': next(r['api_result']['message_id'] for r in receipts if r['recipient'] == 'w490' and r['kind'] == 'claim')})
    for file in packet['files']:
        file['sha256'] = hashlib.file_digest(Path(file['path']).open('rb'), 'sha256').hexdigest()
    write_local('REVIEW_PACKET.json', packet)
    submission = {'submitted_at_unix': time.time(), 'inbox_file': str(final),
                  'local_source_file': str(source), 'draft_content_equal': final.read_bytes() == source.read_bytes(),
                  'submitted': True, 'reviewed': False, 'ingested': False, 'retrievable': False,
                  'hook_proposal_file': str(HOOK), 'parent_target_solved': False,
                  'live_store_mutation': False}
    write_local('SUBMISSION_STATUS.json', submission)
    print(json.dumps(submission))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
