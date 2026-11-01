"""Validate local deliverables and stage reviewable external-file diffs; no live write."""
from __future__ import annotations

import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
bundle_path = ROOT / 'draft_bundles' / 'bundle_001.json'
hook_path = ROOT / 'hook_proposals' / 'math-w395.jsonl'
bundle = json.loads(bundle_path.read_text(encoding='utf-8'))
assert bundle['spec'] == 'mathbrain-draft-v1'
assert bundle['author_agent'] == 'w395'
assert 1 <= len(bundle['entries']) <= 200
keys = {entry['key'] for entry in bundle['entries']}
assert len(keys) == len(bundle['entries'])
for entry in bundle['entries']:
    assert entry['kind'] in {'definition', 'lemma', 'theorem', 'concept'}
    assert entry['proof_text'] is None if entry['kind'] in {'concept', 'definition'} else bool(entry['proof_text'])
    assert entry['source']['license'].startswith(('owner-own-work', 'arxiv-nonexclusive'))
    assert entry['statement'] and entry['assumptions']
for relation in bundle['relations']:
    assert relation['from_key'] in keys
    assert relation['kind'] in {'depends_on', 'defines', 'proves', 'refutes', 'generalizes', 'specializes', 'analogous_to', 'cites', 'semantic_association'}
    assert relation.get('to_key') in keys or relation.get('to_existing_logical') == 'math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp'
    assert relation['rationale']
hooks = [json.loads(line) for line in hook_path.read_text(encoding='utf-8').splitlines() if line]
assert len(hooks) == 1
for hook in hooks:
    assert set(('id', 'area', 'event', 'cue', 'fire_when', 'silent_when', 'text', 'evidence', 'proposer')) <= set(hook)
    assert len(hook['text']) <= 300
    assert hook['fire_when'] and hook['silent_when'] and hook['evidence']
claim_rows = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
result_rows = [json.loads(line) for line in (ROOT / 'RESULT_ROWS.jsonl').read_text(encoding='utf-8').splitlines() if line]
assert all(row.get('independent_reviewer') for row in claim_rows)

patch_dir = ROOT / 'patches'
patch_dir.mkdir(exist_ok=True)
for source, target, patch_name in [
    (bundle_path, '~/math-brain-inbox/w395/bundle_001.json', '01_p0117_fixed_label_gap_bundle.diff'),
    (hook_path, '~/primary_directive/hooks1000/proposals/math-w395.jsonl', '02_p0117_quantifier_hook.diff'),
]:
    lines = source.read_text(encoding='utf-8').splitlines(keepends=True)
    diff = ''.join(difflib.unified_diff([], lines, fromfile='a/' + target, tofile='b/' + target))
    assert diff.startswith('--- a/' + target + '\n+++ b/' + target + '\n')
    (patch_dir / patch_name).write_text(diff, encoding='utf-8')

result = {'status': 'pass', 'draft_entries': len(bundle['entries']), 'draft_relations': len(bundle['relations']), 'hook_proposals': len(hooks), 'claim_rows': len(claim_rows), 'result_rows': len(result_rows), 'external_writes': 0}
(ROOT / 'VALIDATION.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result))
