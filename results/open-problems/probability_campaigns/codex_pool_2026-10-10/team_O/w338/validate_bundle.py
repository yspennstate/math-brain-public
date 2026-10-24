"""Validate draft schema, exact edge quotations, and local evidence coverage.

This is read-only against the live store and never invokes the integrator.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
bundle = json.loads((ROOT/'bundle_001.json').read_text(encoding='utf-8'))
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w338'
entries = bundle['entries']
assert 0 < len(entries) <= 200
keys = {e['key'] for e in entries}
assert len(keys)==len(entries)
names = {f"math:{e['namespace']}:{e['logical_name']}" for e in entries}
assert len(names)==len(entries)
required = {'key','namespace','logical_name','kind','title','statement','proof_text',
            'assumptions','domain','source'}
for e in entries:
    assert required <= e.keys()
    assert e['kind'] in {'definition','lemma','theorem','concept'}
    assert e['statement'] and 'audit PENDING' in e['statement']
    assert e['assumptions'] and isinstance(e['assumptions'],list)
    assert e['proof_text'] if e['kind'] in {'lemma','theorem'} else e['proof_text'] is None
    assert {'source_id','url','revision','license','excerpt'} <= e['source'].keys()
    assert e['source']['license'].startswith('owner-own-work')

all_cards = []
for filename in ['assigned_store_cards.json','matched_store_cards.json']:
    for ns in json.loads((ROOT/filename).read_text(encoding='utf-8')).values():
        all_cards.extend(ns)
actual_cards = {n['logical_id']:n for n in all_cards if n.get('logical_id')}
allowed = {'depends_on','defines','proves','refutes','generalizes','specializes',
           'analogous_to','cites','semantic_association'}
by_key = {e['key']:e for e in entries}
evidence = [json.loads(line) for line in (ROOT/'edge_evidence.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(evidence)==len(bundle['relations'])
for relation,quotes in zip(bundle['relations'],evidence):
    assert relation['from_key'] in keys and relation['kind'] in allowed
    target = relation['to_existing_logical']
    assert target in actual_cards, ('unresolved target',target)
    assert relation['from_key']==quotes['from_key']
    assert target==quotes['to_existing_logical'] and relation['kind']==quotes['kind']
    assert quotes['from_quote'] in by_key[relation['from_key']]['statement'], quotes
    assert quotes['to_quote'] in actual_cards[target]['body'], quotes
    assert quotes['from_quote'] in relation['rationale'] and quotes['to_quote'] in relation['rationale']

# Cross-bundle links have no in-file dependency cycle. Ensure research evidence
# actually accompanies the strongest finite computation and the special cases.
majority = json.loads((ROOT/'majority_measurements.json').read_text(encoding='utf-8'))
assert majority['exact_cost']=='393/64' and majority['exact_revealment']=='131/192'
assert majority['partial_states']==19683 and majority['inputs']==512
assert majority['stop_errors']==majority['bellman_errors']==majority['policy_errors']==0
assert (ROOT/'majority_policy.json').is_file() and (ROOT/'PROOFS.md').is_file()
special = json.loads((ROOT/'special_case_measurements.json').read_text(encoding='utf-8'))
assert {'P0266','C0133','P0090','P0427','C0032','C0077','C0119','P0010','P0036'} <= special.keys()
statuses = [json.loads(line) for line in (ROOT/'problem_statuses.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(set(s['problem_id'] for s in statuses))==10
assert all(s['independent_audit']=='PENDING_W346' for s in statuses)
report = dict(status='PASS_LOCAL_DRAFT_VALIDATION',entries=len(entries),
              relations=len(evidence),existing_targets=len(set(q['to_existing_logical'] for q in evidence)),
              exact_quote_pairs=len(evidence),problems=10,
              store_writes=0,external_verdicts=0,
              limitation='Local checks do not replace w346 KEEP or integrator validation.')
(ROOT/'bundle_validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
