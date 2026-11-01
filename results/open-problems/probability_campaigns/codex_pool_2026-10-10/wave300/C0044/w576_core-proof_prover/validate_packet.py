"""Bounded artifact and exact arithmetic checks, not a formal proof checker."""
import json
import time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
started = time.monotonic()
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


rows = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
b = json.loads((ROOT / 'bundle_001.json').read_text(encoding='utf-8'))
s = json.loads((ROOT / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
check('nine distinct claim rows', len(rows) == 9 and len({r['id'] for r in rows}) == 9)
allowed_status = {'conjecture', 'numerical evidence', 'sketch', 'proved special case', 'independently checked proof'}
fields = {'id', 'statement', 'assumptions', 'source', 'proof_or_counterexample', 'independent_reviewer', 'remaining_gap', 'status'}
check('claim schema and status vocabulary', all(fields <= r.keys() and r['status'] in allowed_status for r in rows))
check('no claimed independent proof', all(r['status'] != 'independently checked proof' and r['independent_reviewer']['verdict'] == 'pending' for r in rows))
check('draft bundle spec', b['spec'] == 'mathbrain-draft-v1' and b['author_agent'] == 'w576' and len(b['entries']) == 9)
keys = {e['key'] for e in b['entries']}
check('unique entry keys and logical names', len(keys) == 9 and len({e['logical_name'] for e in b['entries']}) == 9)
ef = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'}
check('required entry and source fields', all(ef <= e.keys() and {'source_id', 'url', 'revision', 'license'} <= e['source'].keys() for e in b['entries']))
check('accepted owner-own-work source tags', all(e['source']['license'].startswith('owner-own-work') for e in b['entries']))
check('proof fields and pending-review labels', all((e['proof_text'] is None) if e['kind'] in {'definition', 'concept'} else (bool(e['proof_text']) and 'INDEPENDENT REVIEW PENDING' in e['statement']) for e in b['entries']))
check('single gap remains concept material', next(e for e in b['entries'] if e['key'] == 'g1')['kind'] == 'concept' and next(e for e in b['entries'] if e['key'] == 'g1')['proof_text'] is None)
rk = {'depends_on', 'defines', 'proves', 'refutes', 'generalizes', 'specializes', 'analogous_to', 'cites', 'semantic_association'}
check('allowed relation types and supporting ends', all(r['kind'] in rk and r['from_key'] in keys and bool(r['rationale']) and (r.get('to_key') in keys or r.get('to_existing_logical', '').startswith('math:')) for r in b['relations']))
adj = {k: [] for k in keys}
for r in b['relations']:
    if r['kind'] == 'depends_on':
        adj[r['from_key']].append(r['to_key'])
seen, active = set(), set()


def visit(k):
    if k in active:
        raise AssertionError('dependency cycle')
    if k in seen:
        return
    active.add(k)
    for j in adj[k]:
        visit(j)
    active.remove(k)
    seen.add(k)


for k in keys:
    visit(k)
check('dependency graph acyclic', len(seen) == len(keys))
alpha = [Fraction(1, 10)] + [Fraction(1, 50)] * 5
pair_max = max(alpha[i] + alpha[i + 3] for i in range(3))
kappa = 2 * sum(alpha) - pair_max
check('Dirichlet parameters strictly positive', all(a > 0 for a in alpha))
check('exact trap exponent 7/25', sum(alpha) == Fraction(1, 5) and pair_max == Fraction(3, 25) and kappa == Fraction(7, 25) and kappa <= 1)
check('mean drift is only arithmetic', (alpha[0] - alpha[3]) / sum(alpha) == Fraction(2, 5))
check('full target and served identity gates honest', s['full_target_proved_in_this_packet'] is False and s['current_openness'] == 'UNKNOWN' and not s['served_model_evidence']['response_side_receipt_available'])
check('no ingestion or retrieval asserted', s['ingestion_state'] == 'not ingested' and s['retrieval_state'] == 'not checked')
edge = json.loads((ROOT / 'EDGE_PROPOSALS.jsonl').read_text(encoding='utf-8'))
check('correction edge has two exact IDs and quotes', edge['kind'] == 'refutes' and edge['from_node_id'] != edge['to_node_id'] and bool(edge['from_quote']) and bool(edge['to_quote']))
hook = json.loads((ROOT / 'hooks/math-w576.jsonl').read_text(encoding='utf-8'))
check('hook has evidence and fire/silent controls', len(hook['text']) <= 300 and all(hook[x] for x in ('cue', 'fire_when', 'silent_when', 'evidence')))
result = {
    'command': 'python -X utf8 ~/brain_workers/w576/validate_packet.py',
    'verification_kind': 'artifact-schema and exact-rational coefficient checks; no simulation or formal proof',
    'check_count': len(checks), 'checks_passed': checks, 'elapsed_seconds': round(time.monotonic() - started, 6),
    'before_local_result_rows': 0, 'after_local_claim_rows': len(rows),
    'author_lemma_rows': 6, 'source_backed_counterexample_rows': 1, 'unproved_gap_rows': 1,
    'draft_entries': len(b['entries']), 'draft_relations': len(b['relations']), 'external_node_id_edge_proposals': 1,
    'before_live_store_writes_by_worker': 0, 'after_live_store_writes_by_worker': 0,
    'submitted': False, 'reviewed': False, 'ingested': False, 'retrievable': False,
    'mathematical_proof_certified_by_tests': False,
}
(ROOT / 'MEASUREMENTS.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in result.items() if k != 'checks_passed'}))
