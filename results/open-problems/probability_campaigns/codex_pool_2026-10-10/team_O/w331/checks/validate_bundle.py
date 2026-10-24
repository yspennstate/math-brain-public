import json,re,sqlite3,time
from pathlib import Path
root=Path(__file__).resolve().parents[1]; start=time.perf_counter()
bundle=json.loads((root/'bundle_001.json').read_text(encoding='utf-8'));entries=bundle['entries']; relations=bundle['relations'];lookup={e['key']:e for e in entries}
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w331'
assert len(entries)==len(lookup)==21 and len(entries)<=200
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
for e in entries:
    assert required<=e.keys()
    assert e['kind'] in {'definition','lemma','theorem','concept'}
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
    assert re.fullmatch(r'[a-z0-9-]+(?:\.[a-z0-9-]+)+',e['namespace'])
    assert e['statement'] and len(e['statement'])>80
    assert isinstance(e['assumptions'],list) and e['assumptions']
    assert bool(e['proof_text']) if e['kind'] in {'lemma','theorem'} else e['proof_text'] is None
    assert {'source_id','url','revision','license','excerpt'}<=e['source'].keys()
    assert e['source']['license'].startswith('owner-own-work')
    source=Path(e['source']['url'].replace('file:///',''))
    assert source.is_file(),source
external={r['to_existing_logical'] for r in relations if 'to_existing_logical' in r}
c=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True)
resolved={}
for logical in external:
    rows=c.execute("SELECT id,body FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=?",(logical,)).fetchall()
    assert rows,logical;resolved[logical]=rows
c.close()
def normal(s):return ' '.join(s.split())
evidence=[json.loads(line) for line in (root/'edge_evidence.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(evidence)==len(relations)
dependency={key:[] for key in lookup}
for relation,row in zip(relations,evidence):
    assert relation['kind'] in allowed and relation['from_key'] in lookup
    assert ('to_key' in relation)!=('to_existing_logical' in relation)
    assert row['from_quote'].removesuffix(' ...') in normal(lookup[relation['from_key']]['statement'])
    assert 'From: "' in relation['rationale'] and 'To: "' in relation['rationale']
    right=row['to_quote'].removesuffix(' ...')
    if 'to_key' in relation:
        assert relation['to_key'] in lookup
        assert right in normal(lookup[relation['to_key']]['statement'])
        if relation['kind']=='depends_on':dependency[relation['from_key']].append(relation['to_key'])
    else:assert any(right in normal(body) for _,body in resolved[relation['to_existing_logical']])
active=set();finished=set()
def visit(key):
    assert key not in active,'depends_on cycle'
    if key in finished:return
    active.add(key)
    for nxt in dependency[key]:visit(nxt)
    active.remove(key);finished.add(key)
for key in lookup:visit(key)
problems=['P0033','P0355','C0075','P0029','P0229','C0008','C0067','C0098','C0146','P0021']
for problem in problems:
    assert (root/'proofs'/f'{problem}.md').is_file()
    r=json.loads((root/'checks'/f'{problem}_receipt.json').read_text(encoding='utf-8'))
    assert r['problem_id']==problem and r['audit_status']=='PENDING w347'
    assert r['elapsed_seconds']>=0
hooks=[json.loads(line) for path in (root/'proposals').glob('*-w331.jsonl') for line in path.read_text(encoding='utf-8').splitlines()]
assert len(hooks)==4
for h in hooks:
    assert len(h['text'])<=300
    assert {'id','area','event','cue','fire_when','silent_when','text','evidence','proposer'}<=h.keys()
    assert h['fire_when']!=h['silent_when'] and h['proposer']=='w331'
source_report=json.loads((root/'primary_source_check_report.json').read_text(encoding='utf-8'))
assert any('Question 17.18.' in r['excerpt'] for r in source_report)
assert any('CONJECTURE 34.' in r['excerpt'] for r in source_report)
assert any('Open Problem 15.1 (ISE' in r['excerpt'] for r in source_report)
# The per-claim audit ledger must stay separate from mathematical/numerical controls.
run=json.loads((root/'RUN_RECEIPT.json').read_text(encoding='utf-8'))
assert run['accepted_results']==0 and run['new_global_open_problem_solutions_claimed']==0 and run['lean_certificate_count']==0
assert run['result_rows']==len((root/'results.jsonl').read_text(encoding='utf-8').splitlines())
receipt={'result':'PASS','draft_nodes':len(entries),'mathematical_nodes':20,'quoted_relations':len(relations),'resolved_external_logicals':len(external),'resolved_external_nodes':sum(len(r) for r in resolved.values()),'unresolved_external_targets':0,'proof_reports':len(problems),'measurement_receipts':len(problems),'hook_proposals':len(hooks),'depends_on_acyclic':True,'quoted_ends_verified':True,'accepted_results':0,'command':'python -B -X utf8 checks/validate_bundle.py','elapsed_seconds':time.perf_counter()-start,'scope':'Structural/source-target checks only; mathematical KEEP and live integrator not run.'}
(root/'checks/bundle_validation_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8');print(json.dumps(receipt))
