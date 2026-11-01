import json
from pathlib import Path

home = Path(__file__).parent
claims = [json.loads(line) for line in (home / 'CLAIMS.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
verdicts = [json.loads(line) for line in (home / 'REVIEW_VERDICTS.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
assert len({r['id'] for r in claims}) == len(claims)
assert all(r.get('statement') and r.get('assumptions') is not None and r.get('source') and r.get('proof_or_counterexample') and r.get('independent_reviewer') and r.get('remaining_gap') and r.get('status') for r in claims)
for name in ('SOURCE_STATUS.json', 'W432_BUNDLE_AUDIT.json', 'W433_BUNDLE_AUDIT.json'):
    json.loads((home / name).read_text(encoding='utf-8-sig'))
bundle = json.loads(Path('~/math-brain-inbox/w434/bundle_001.json').read_text(encoding='utf-8-sig'))
assert bundle['spec'] == 'mathbrain-draft-v1' and bundle['author_agent'] == 'w434'
keys = {e['key'] for e in bundle['entries']}
assert len(keys) == len(bundle['entries'])
assert all(r['from_key'] in keys and r['to_key'] in keys for r in bundle['relations'])
hook = [json.loads(line) for line in Path('~/primary_directive/hooks1000/proposals/math-w434.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
assert all(len(r['text']) <= 300 for r in hook)
status = (home / 'STATUS.md').read_text(encoding='utf-8-sig').splitlines()
assert status[0] == 'STATE: NEEDS_REVIEW' and any(line.startswith('NEXT: ') for line in status)
print(f'PASS claims={len(claims)} verdicts={len(verdicts)} bundle_entries={len(bundle["entries"])} bundle_relations={len(bundle["relations"])} hooks={len(hook)}')
