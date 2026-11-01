import json,pathlib,re,sqlite3,subprocess
w=pathlib.Path('~/brain_workers/w538')
for name in ['ATTEMPT.md','HYPOTHESIS_AUDIT.md']:
 p=w/name;p.write_text(p.read_text(encoding='utf-8').replace('https://arxiv.org/html/2405.06616v2#S3.Thmtheorem13','https://arxiv.org/html/2405.06616v2'),encoding='utf-8')
b=json.loads((w/'bundle_001.json').read_text(encoding='utf-8'))
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
keys={r['key'] for r in b['entries']}
assert len(keys)==len(b['entries']) and len(keys)<=200
for e in b['entries']:
 assert required<=e.keys()
 assert e['kind'] in {'definition','concept'} and e['proof_text'] is None
 assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
 assert e['source']['license'].startswith('owner-own-work')
 assert all(k in e['source'] for k in ['source_id','url','revision','license','excerpt'])
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
adjacency={k:[] for k in keys}
for r in b['relations']:
 assert r['from_key'] in keys and r['kind'] in allowed and r['rationale']
 if 'to_key' in r:assert r['to_key'] in keys
 else:assert r['to_existing_logical'].startswith('math:')
 if r['kind']=='depends_on':adjacency[r['from_key']].append(r['to_key'])
def visit(k,path):
 assert k not in path,'dependency cycle'
 for t in adjacency[k]:visit(t,path|{k})
for k in keys:visit(k,set())
p=pathlib.Path('~/math-brain-build/local/population/brain.sqlite3')
c=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True,timeout=5)
c.execute('PRAGMA query_only=ON')
targets=[r['to_existing_logical'] for r in b['relations'] if 'to_existing_logical' in r]
resolved={s:bool(c.execute("SELECT 1 FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=? LIMIT 1",(s,)).fetchone()) for s in targets}
c.close();assert all(resolved.values()),resolved
patch_result=json.loads((w/'PATCH_VALIDATION.json').read_text(encoding='utf-8'))
assert patch_result['check_returncode']==0 and patch_result['content_matches'] and not patch_result['apply_stderr']
valid={'schema':'mathbrain-draft-v1','entries':len(keys),'relations':len(b['relations']),'all_new_results_concept_draft':True,'dependency_graph_acyclic':True,'existing_targets':resolved,'mathematical_review':False,'patch_validation':patch_result}
(w/'VALIDATION.json').write_text(json.dumps(valid,indent=2),encoding='utf-8')
print(json.dumps(valid,indent=2))
