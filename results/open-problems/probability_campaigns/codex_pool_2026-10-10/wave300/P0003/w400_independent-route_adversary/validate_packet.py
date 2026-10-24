"""Static artifact validation, not a scientific experiment or proof checker."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
bundle = json.loads((ROOT/'drafts/bundle_001.json').read_text(encoding='utf-8'))
claims = [json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
audits = [json.loads(line) for line in (ROOT/'AUDIT_VERDICTS.jsonl').read_text(encoding='utf-8').splitlines() if line]
keys = {e['key'] for e in bundle['entries']}
assert len(keys) == len(bundle['entries']) <= 200
assert bundle['spec'] == 'mathbrain-draft-v1' and bundle['author_agent'] == 'w400'
for e in bundle['entries']:
    assert e['kind'] == 'concept' and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
    assert e['statement'] and e['assumptions']
    assert all(k in e for k in ('key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'))
allowed = {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
dependencies = {k:[] for k in keys}
for r in bundle['relations']:
    assert r['from_key'] in keys and r['kind'] in allowed
    assert ('to_key' in r) != ('to_existing_logical' in r)
    if 'to_key' in r:
        assert r['to_key'] in keys
        if r['kind'] == 'depends_on': dependencies[r['from_key']].append(r['to_key'])
def visit(k, active):
    assert k not in active, 'dependency cycle'
    for dest in dependencies[k]: visit(dest, active|{k})
for k in keys: visit(k,set())
required = {'id','exact_statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status'}
assert len({r['id'] for r in claims}) == len(claims)
for r in claims:
    assert required <= set(r)
    assert r['status'] in {'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
assert not any(r['status'] == 'independently checked proof' for r in claims)
source = json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
assert source['primary_statement']['source_id'] == 'arxiv:2205.07318v1'
assert source['current_openness'] == 'UNKNOWN'
gate = json.loads((ROOT/'COMPUTE_GATE.json').read_text(encoding='utf-8'))
measure = ROOT/'MEASUREMENTS.json'
ran = measure.exists()
if not ran:
    for r in audits:
        if r['id'] == 'P0003-w399-three-probe':
            r['why'] = 'Independent hand Taylor/Ito and rational-matrix audit agrees. Exact diagnostic code is prepared, but its fresh compute gate did not permit a run. Semimartingale regularity, a common fixed positive exponent, valid stopped maps, local invertibility and global coverage remain explicit. This is not a complete SAW proof.'
    (ROOT/'AUDIT_VERDICTS.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in audits),encoding='utf-8')
receipt = {'status':'PASS','validation_kind':'static format/scope only; not mathematical proof',
           'claim_rows':len(claims),'audit_rows':len(audits),'draft_concept_entries':len(keys),
           'relations':len(bundle['relations']),'scientific_diagnostics_executed':ran,
           'compute_gate_allowed':gate['allow'],'formal_check_receipt':None,
           'mathematical_review':'pending w401'}
(ROOT/'VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
