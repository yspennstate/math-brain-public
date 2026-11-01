"""Local BUNDLE_SPEC validation and atomic submission of this owned DRAFT only."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLE = ROOT / 'bundle_001.json'
KINDS = {'definition', 'lemma', 'theorem', 'concept'}
RELATIONS = {'depends_on', 'defines', 'proves', 'refutes', 'generalizes', 'specializes',
             'analogous_to', 'cites', 'semantic_association'}
LICENSES = ('cc-by-sa', 'cc-by', 'cc0', 'apache-2.0', 'gfdl', 'public-domain', 'mit',
            'arxiv-nonexclusive', 'owner-own-work')


def validate():
    draft = json.loads(BUNDLE.read_text(encoding='utf-8'))
    assert draft['spec'] == 'mathbrain-draft-v1' and draft['author_agent'] == 'w402'
    assert 1 <= len(draft['entries']) <= 200
    keys = set()
    for entry in draft['entries']:
        assert set(('key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text',
                    'assumptions', 'domain', 'source')).issubset(entry)
        assert entry['key'] not in keys
        keys.add(entry['key'])
        assert entry['kind'] in KINDS and isinstance(entry['assumptions'], list)
        assert entry['namespace'] == entry['namespace'].lower() and '.' in entry['namespace']
        assert entry['logical_name'] == entry['logical_name'].lower()
        assert entry['statement'] and entry['title']
        if entry['kind'] in {'lemma', 'theorem'}:
            assert isinstance(entry['proof_text'], str) and entry['proof_text'].strip()
        else:
            assert entry['proof_text'] is None
        source = entry['source']
        assert set(('source_id', 'url', 'revision', 'license', 'excerpt')).issubset(source)
        assert source['source_id'] and source['revision']
        assert source['license'].lower().startswith(LICENSES)
    graph = {key: [] for key in keys}
    for relation in draft['relations']:
        assert relation['from_key'] in keys and relation['kind'] in RELATIONS
        assert relation['rationale']
        assert ('to_key' in relation) != ('to_existing_logical' in relation)
        if 'to_key' in relation:
            assert relation['to_key'] in keys
            if relation['kind'] == 'depends_on':
                graph[relation['from_key']].append(relation['to_key'])
        else:
            assert relation['to_existing_logical'].startswith('math:')
    visiting, done = set(), set()
    def visit(key):
        assert key not in visiting, 'cyclic depends_on'
        if key in done:
            return
        visiting.add(key)
        for other in graph[key]:
            visit(other)
        visiting.remove(key)
        done.add(key)
    for key in keys:
        visit(key)
    evidence = [json.loads(x) for x in (ROOT / 'RELATIONS.jsonl').read_text(encoding='utf-8').splitlines()]
    assert len(evidence) == len(draft['relations'])
    assert all(row['from_quote'] and row['to_quote'] for row in evidence)
    hook = json.loads((ROOT / 'HOOK_PROPOSAL.jsonl').read_text(encoding='utf-8'))
    assert len(hook['text']) <= 300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
    result = {'local_schema': 'PASS', 'entries': len(keys), 'relations': len(draft['relations']),
              'acyclic_dependencies': True, 'hook_characters': len(hook['text']),
              'live_integrator_run': False, 'store_write': False,
              'validation_is_mathematical_proof': False}
    (ROOT / 'VALIDATION.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    return result


def publish():
    receipt = json.loads((ROOT / 'RESOURCE_CLAIM.json').read_text(encoding='utf-8'))
    assert receipt['agent'] == 'w402' and receipt['claim_id'] == 'clm-2002bb0c70'
    assert datetime.now(timezone.utc) < datetime.fromisoformat(receipt['expires_at'].replace('Z', '+00:00'))
    owned_dir = Path('~/math-brain-inbox/w402').resolve()
    target = (owned_dir / 'bundle_001.json').resolve()
    part = (owned_dir / 'bundle_001.json.part').resolve()
    assert target.parent == owned_dir and part.parent == owned_dir
    assert target.as_posix().lower() == receipt['resource'].replace('\\', '/').lower()
    owned_dir.mkdir(parents=True, exist_ok=True)
    content = BUNDLE.read_bytes()
    if target.exists():
        assert target.read_bytes() == content, 'existing draft differs; preserve it'
    else:
        assert not part.exists(), 'existing .part preserved; inspect it before retry'
        with part.open('xb') as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        assert not target.exists(), 'target appeared; preserve all files'
        os.rename(part, target)
    lifecycle_path = ROOT / 'BRAIN_LIFECYCLE.json'
    lifecycle = json.loads(lifecycle_path.read_text(encoding='utf-8'))
    lifecycle.update({'submitted': True, 'submitted_at': datetime.now(timezone.utc).isoformat(),
                      'resource_claim_id': receipt['claim_id'], 'reviewed': 'partial: w404 KEEP of S1.P0003.w402.002; full packet pending',
                      'ingested': False, 'retrievable': False})
    lifecycle_path.write_text(json.dumps(lifecycle, indent=2) + '\n', encoding='utf-8')
    return str(target)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--publish', action='store_true')
    requested = args.parse_args()
    result = validate()
    if requested.publish:
        result['submitted_path'] = publish()
    print(json.dumps(result))
