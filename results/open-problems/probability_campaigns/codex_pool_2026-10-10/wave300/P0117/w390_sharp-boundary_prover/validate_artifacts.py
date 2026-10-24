"""Artifact/schema checks only; this is not a mathematical or formal proof audit."""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    bundle = json.loads((ROOT / 'bundles/bundle_001.json').read_text(encoding='utf-8'))
    assert bundle['spec'] == 'mathbrain-draft-v1'
    assert bundle['author_agent'] == 'w390'
    entries = bundle['entries']
    assert len(entries) == 6
    keys = {e['key'] for e in entries}
    assert len(keys) == len(entries)
    required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'}
    for e in entries:
        assert required <= e.keys()
        assert e['kind'] in {'definition', 'lemma', 'theorem', 'concept'}
        assert e['statement'] and e['statement'].startswith('DRAFT')
        assert e['source']['license'].startswith('owner-own-work')
        assert {'source_id', 'url', 'revision', 'license'} <= e['source'].keys()
        assert e['assumptions']
        if e['kind'] in {'lemma', 'theorem'}:
            assert e['proof_text'] and 'independent review pending' in e['statement']
        else:
            assert e['proof_text'] is None
    allowed = {'depends_on', 'defines', 'proves', 'refutes', 'generalizes', 'specializes', 'analogous_to', 'cites', 'semantic_association'}
    baseline = json.loads((ROOT / 'reports/store_target_baseline.json').read_text(encoding='utf-8'))
    existing = {r['logical_id'] for r in baseline if r.get('logical_id')}
    graph = {k: [] for k in keys}
    for r in bundle['relations']:
        assert r['from_key'] in keys and r['kind'] in allowed and r['rationale']
        assert ('to_key' in r) != ('to_existing_logical' in r)
        if 'to_key' in r:
            assert r['to_key'] in keys
            if r['kind'] == 'depends_on':
                graph[r['from_key']].append(r['to_key'])
        else:
            assert r['to_existing_logical'] in existing
    visited = set()
    def visit(node, path):
        assert node not in path, 'depends_on cycle'
        if node not in visited:
            for child in graph[node]:
                visit(child, path | {node})
            visited.add(node)
    for key in keys:
        visit(key, set())
    rows = [json.loads(s) for s in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s]
    assert len({r['id'] for r in rows}) == len(rows)
    status = json.loads((ROOT / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    assert status['current_openness'] == 'UNKNOWN' and status['novelty_claim'] is False
    gate = json.loads((ROOT / 'reports/geometry_gate.json').read_text(encoding='utf-8'))
    checks_file = ROOT / 'reports/geometry_checks.json'
    checks = 'NOT_RUN_RESOURCE_GATE' if not checks_file.exists() else json.loads(checks_file.read_text(encoding='utf-8'))['status']
    result = {'at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
              'artifact_structure': 'PASS', 'draft_entries': len(entries),
              'relations_with_resolved_ends': len(bundle['relations']),
              'depends_on_acyclic': True, 'claim_rows': len(rows),
              'mathematical_review': 'PENDING', 'formal_proof': False,
              'finite_geometry_checks': checks, 'last_geometry_gate_permit': gate['permit'],
              'checks_command': 'python -X utf8 resource_checked_geometry.py'}
    (ROOT / 'reports/artifact_validation.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
