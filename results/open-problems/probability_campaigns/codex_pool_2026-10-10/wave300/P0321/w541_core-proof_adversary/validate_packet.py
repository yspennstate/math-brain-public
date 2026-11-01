"""Check the narrow draft schema and evidence classifications locally."""
from pathlib import Path
import json
import re

root=Path(__file__).resolve().parent
bundle=json.loads((root/'bundle_001.json').read_text(encoding='utf-8'))
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
keys={e['key'] for e in bundle['entries']}
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w541'
assert 0<len(keys)==len(bundle['entries'])<=200
for e in bundle['entries']:
    assert required<=e.keys() and e['kind']=='concept' and e['proof_text'] is None
    assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
    assert e['source']['license'].startswith('owner-own-work')
    assert 'review' in e['statement'].lower() or 'Open proof obligation' in e['statement']
    assert len(e['statement'])>100
canonical=json.loads((root/'TARGET_RECORDS.json').read_text(encoding='utf-8'))
logical={e['logical_id'] for e in canonical['canonical_records']}
for rel in bundle['relations']:
    assert rel['from_key'] in keys and rel['kind'] in allowed
    if 'to_key' in rel: assert rel['to_key'] in keys
    else: assert rel['to_existing_logical'] in logical
claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
for c in claims:
    assert c['status'] in {'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
    assert all(c.get(k) is not None for k in ['statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap'])
    if c['status']=='independently checked proof':
        assert c.get('review_receipt') and c.get('reviewed_scope')=='stipulated Gaussian special case only; not P0321'
assert json.loads((root/'numerical_probe.json').read_text(encoding='utf-8'))['status']=='pass'
assert json.loads((root/'exact_transfer_probe.json').read_text(encoding='utf-8'))['status']=='pass'
assert json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))['current_openness']=='UNKNOWN'
result={'status':'pass','draft_entries':len(keys),'relations':len(bundle['relations']),'claims':len(claims),'external_target_resolved_read_only':True,'theorem_promotions':0,'live_store_writes':0,'command':'python -X utf8 ~/brain_workers/w541/validate_packet.py','scope':'schema and evidence checks, not mathematical review'}
(root/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
