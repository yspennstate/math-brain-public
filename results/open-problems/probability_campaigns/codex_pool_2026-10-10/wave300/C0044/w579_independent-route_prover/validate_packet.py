"""Structural validation and reproducible review hashes; no live ingestion."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
b=json.loads((ROOT/'DRAFT_BUNDLE.json').read_text(encoding='utf-8'))
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
keys={e['key'] for e in b['entries']}
assert b['spec']=='mathbrain-draft-v1' and b['author_agent']=='w579'
assert len(keys)==len(b['entries'])<=200
for e in b['entries']:
    assert set(['key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'])<=set(e)
    assert e['kind'] in ['definition','concept'] and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
    assert len(e['statement'])>50 and e['assumptions']
graph={k:[] for k in keys}
for r in b['relations']:
    assert r['from_key'] in keys and r['kind'] in allowed and r['rationale']
    assert ('to_key' in r)!=('to_existing_logical' in r)
    if 'to_key' in r:
        assert r['to_key'] in keys
        if r['kind']=='depends_on': graph[r['from_key']].append(r['to_key'])
    else:
        assert r['to_existing_logical']=='math:probability.randomenvironment:open-problem-c0044-zero-one-law-for-directional-transience-in-dimensions-d-3'
seen=set()
def visit(k,active):
    assert k not in active, 'depends_on cycle'
    if k in seen: return
    for target in graph[k]: visit(target,active|{k})
    seen.add(k)
for k in keys: visit(k,set())
rows=[json.loads(x) for x in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
assert len({x['claim_id'] for x in rows})==len(rows)
assert all(x['status'] in ['conjecture','numerical evidence','sketch','proved special case','independently checked proof'] for x in rows)
assert all('pending' in x['independent_reviewer'] or 'not yet reviewed' in x['independent_reviewer'] for x in rows)
assert not any(x['status']=='independently checked proof' for x in rows)
ev=[json.loads(x) for x in (ROOT/'RELATION_EVIDENCE.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(ev)==len(b['relations'])
assert all(x['source_end_quote'] and x['target_end_quote'] for x in ev)
controls=json.loads((ROOT/'CONTROL_RESULTS.json').read_text(encoding='utf-8'))
assert controls['passed'] and controls['max_reverse_density_residual']=='0'
assert controls['max_martingale_energy_residual']=='0' and not controls['parent_problem_proved']
assert 'periodic_stationary_one_step' in controls, 'overlapping peer-owned IID control must be removed'
receipt={'structure_passed':True,'draft_entries':len(keys),'relations':len(ev),
         'claims':len(rows),'independently_checked_claims':0,
         'theorem_or_lemma_promotions':0,'live_ingestion_performed':False,
         'control_assertions':controls['exact_assertions'],
         'scope':'Own draft structural checks and finite exact controls; not mathematical referee approval'}
(ROOT/'VALIDATION_RESULTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
files=['STATEMENT.md','ATTEMPT.md','CLAIMS.jsonl','SOURCE_STATUS.json',
       'C0044_PRIOR_EXTRACT.json','check_controls.py','COMPUTE_GATE.json',
       'CONTROL_RESULTS.json','DRAFT_BUNDLE.json','RELATION_EVIDENCE.jsonl',
       'VALIDATION_RESULTS.json','build_draft.py','validate_packet.py',
       'REVIEW_PACKET.md','REPORT.md','HOOK_PROPOSALS.jsonl']
hashes={}
for name in files:
    p=ROOT/name
    if p.exists(): hashes[name]=hashlib.sha256(p.read_bytes()).hexdigest()
(ROOT/'ARTIFACT_SHA256.json').write_text(json.dumps(hashes,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
print('review_artifact_sha256_count',len(hashes))
