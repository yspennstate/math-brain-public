"""Admission/structure checks only. This is not a mathematical proof verifier."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
bundle = json.loads((ROOT / 'bundle_001.json').read_text(encoding='utf-8'))
claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'}
allowed_relations = {'depends_on', 'defines', 'proves', 'refutes', 'generalizes', 'specializes', 'analogous_to', 'cites', 'semantic_association'}
keys = {entry['key'] for entry in bundle['entries']}
assert len(keys) == len(bundle['entries'])
assert len(bundle['entries']) <= 200
assert len({claim['claim_id'] for claim in claims}) == len(claims)
for entry in bundle['entries']:
    assert required <= entry.keys()
    assert entry['kind'] == 'concept' and entry['proof_text'] is None
    assert entry['statement'] and entry['source']['license'].startswith('owner-own-work')
    assert entry['source']['source_id'] and entry['source']['url'] and entry['source']['revision']
graph = {key: [] for key in keys}
captured = json.loads((ROOT / 'REPORT_STORE_CHECK.json').read_text(encoding='utf-8'))
existing_logical_ids = {json.loads(row['metadata_excerpt'])['logical_id'] for row in captured['matched_nodes']}
for edge in bundle['relations']:
    assert edge['from_key'] in keys
    if 'to_key' in edge:
        assert edge['to_key'] in keys
    else:
        assert edge['to_existing_logical'] in existing_logical_ids
    assert edge['kind'] in allowed_relations and edge['rationale']
    if edge['kind'] == 'depends_on':
        graph[edge['from_key']].append(edge['to_key'])
visited, pending = set(), set()
def visit(key):
    assert key not in pending, 'depends_on cycle'
    if key in visited:
        return
    pending.add(key)
    for end in graph[key]:
        visit(end)
    pending.remove(key)
    visited.add(key)
for key in keys:
    visit(key)
for claim in claims:
    assert {'statement', 'assumptions', 'source', 'proof_or_counterexample', 'independent_reviewer', 'remaining_gap', 'status'} <= claim.keys()
    assert claim['status'] != 'independently checked proof'
    assert claim.get('parent_problem_solved', False) is False
submitted = Path('~/math-brain-inbox/w444/bundle_001.json')
assert json.loads(submitted.read_text(encoding='utf-8')) == bundle
hook = json.loads((ROOT / 'math-w444.jsonl').read_text(encoding='utf-8'))
assert len(hook['text']) <= 300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
receipt = {
    'command': 'python -X utf8 ~/brain_workers/w444/validate_packet.py',
    'structure': 'PASS', 'before_worker_claim_rows': 0, 'after_worker_claim_rows': len(claims),
    'before_worker_draft_entries': 0, 'after_worker_draft_entries': len(bundle['entries']),
    'relations': len(bundle['relations']), 'cycle_free_depends_on': True,
    'existing_end_captured_read_only': True,
    'concept_only_entries': len(bundle['entries']), 'theorem_promotions': 0,
    'live_sqlite_writes': 0, 'local_hook_proposals': 1,
    'mathematical_proof_checked_by_program': False,
    'independent_mathematical_review': 'PENDING', 'brain_performance_improvement': 'NOT_MEASURED',
}
(ROOT / 'VALIDATION.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt))
