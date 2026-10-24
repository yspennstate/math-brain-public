"""Structural/source consistency checks only; explicitly not a proof verifier."""
from pathlib import Path
import hashlib
import json
import re

BASE = Path(__file__).resolve().parent

def main():
    load = lambda name: json.loads((BASE / name).read_text(encoding='utf-8'))
    bundle = load('DRAFT_bundle_001.json')
    entries = {e['key']: e for e in bundle['entries']}
    assert len(entries) == 7
    assert bundle['spec'] == 'mathbrain-draft-v1' and bundle['author_agent'] == 'w489'
    required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'}
    for e in entries.values():
        assert required <= e.keys()
        assert e['source']['license'].startswith('owner-own-work')
        for field in ('source_id', 'url', 'revision', 'license'):
            assert isinstance(e['source'].get(field), str) and e['source'][field].strip()
        assert re.fullmatch(r'[a-z][a-z0-9-]*', e['logical_name'])
        assert e['kind'] in {'definition', 'lemma', 'theorem', 'concept'}
        assert e['statement'] and e['title'].startswith('DRAFT')
        if e['kind'] in {'lemma', 'theorem'}:
            assert e['proof_text'] and e['assumptions']
        else:
            assert e['proof_text'] is None
    assert entries['cavity-moment-gap']['kind'] == 'concept'
    assert 'not an established theorem' in entries['cavity-moment-gap']['statement']
    assert entries['invalid-first-moment-route']['kind'] == 'concept'

    live = load('BRAIN_SELECTED_LIVE.json')
    existing = {}
    for r in live['rows']:
        assert r['live_row'] is not None
        existing[json.loads(r['live_row'][4])['logical_id']] = r['live_row'][3]
    allowed = {'depends_on', 'defines', 'proves', 'refutes', 'generalizes', 'specializes', 'analogous_to', 'cites', 'semantic_association'}
    adjacency = {k: [] for k in entries}
    for r in bundle['relations']:
        assert r['kind'] in allowed and r['from_key'] in entries
        if 'to_key' in r:
            assert r['to_key'] in entries
            if r['kind'] == 'depends_on':
                adjacency[r['from_key']].append(r['to_key'])
        else:
            assert r['to_existing_logical'] in existing
    visited, active = set(), set()
    def visit(k):
        assert k not in active, 'dependency cycle'
        if k in visited:
            return
        active.add(k)
        for child in adjacency[k]:
            visit(child)
        active.remove(k)
        visited.add(k)
    for k in entries:
        visit(k)

    edges = [json.loads(s) for s in (BASE / 'EDGES.jsonl').read_text(encoding='utf-8').splitlines()]
    assert len(edges) == len(bundle['relations']) == 8
    for edge in edges:
        assert edge['from_statement'] == entries[edge['from_key']]['statement']
        expected = entries[edge['to_key']]['statement'] if 'to_key' in edge else existing[edge['to_existing_logical']]
        assert edge['to_statement'] == expected
    claims = [json.loads(s) for s in (BASE / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
    assert len(claims) == 6 and len({c['id'] for c in claims}) == 6
    for claim in claims:
        assert all(k in claim for k in ('statement', 'assumptions', 'source', 'proof', 'independent_reviewer', 'remaining_gap', 'status'))
        assert claim['status'] in {'conjecture', 'numerical evidence', 'sketch', 'proved special case', 'independently checked proof'}
        assert claim['status'] != 'independently checked proof'
        assert not claim['reviewed'] and not claim['ingested'] and not claim['retrievable']
    status = load('SOURCE_STATUS.json')
    assert status['current_openness'] == 'UNKNOWN' and not status['mathematics']['parent_target_solved']
    assert 'GOE' in status['intake']['statement']
    assert all(f['match'] for f in load('SOURCE_HASH_CHECK.json')['files'])
    measurement = load('FILTER_MEASUREMENT.json')
    assert measurement['before_precision'] == 0.25 and measurement['after_precision'] == 1.0
    assert len(measurement['retained_known_relevant']) == 1
    packet = load('REVIEW_PACKET.json')
    for file in packet['files']:
        assert hashlib.file_digest(Path(file['path']).open('rb'), 'sha256').hexdigest() == file['sha256']
    receipt = {'command': 'python -X utf8 ~/brain_workers/w489/validate_packet.py',
               'structural_checks_passed': True, 'mathematical_proof_verified': False,
               'source_files_hash_matched': 2, 'live_crosslink_ids_found': len(existing),
               'draft_entries': len(entries), 'claim_rows': len(claims), 'exact_edge_rows': len(edges),
               'independent_mathematical_verdicts': 0, 'formal_receipt': None,
               'live_store_mutation': False}
    (BASE / 'VALIDATION.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
    print(json.dumps(receipt))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
