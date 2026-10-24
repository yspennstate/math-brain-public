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
fixture=w/'validation'/'patch_target_lf';fixture.mkdir(parents=True,exist_ok=True)
patch=w/'patches'/'01_riesz_scope_warning.diff'
cmd=['git','apply','--no-index','--check','--directory=validation/patch_target_lf',str(patch)]
r=subprocess.run(cmd,cwd=w,capture_output=True,text=True,encoding='utf-8',timeout=60)
patch_result={'check_command':cmd,'check_returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
if r.returncode==0:
 cmd=['git','apply','--no-index','--directory=validation/patch_target_lf',str(patch)]
 a=subprocess.run(cmd,cwd=w,capture_output=True,text=True,encoding='utf-8',timeout=60)
 target=fixture/'.claude'/'dreaming'/'riesz_scope_guard.py'
 patch_result.update({'apply_returncode':a.returncode,'apply_stdout':a.stdout,'apply_stderr':a.stderr,'content_matches':target.is_file() and target.read_text(encoding='utf-8')==(w/'riesz_scope_guard.py').read_text(encoding='utf-8-sig')})
(w/'PATCH_VALIDATION.json').write_text(json.dumps(patch_result,indent=2),encoding='utf-8')
valid={'schema':'mathbrain-draft-v1','entries':len(keys),'relations':len(b['relations']),'all_new_results_concept_draft':True,'dependency_graph_acyclic':True,'existing_targets':resolved,'mathematical_review':False,'patch_validation':patch_result}
(w/'VALIDATION.json').write_text(json.dumps(valid,indent=2),encoding='utf-8')
print(json.dumps(valid,indent=2))
assert r.returncode==0 and patch_result.get('content_matches'), 'Patch must be corrected before publication'
