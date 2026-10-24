"""Offline schema, quoted-evidence, dependency and actual local patch-application checks."""
import json
import os
from pathlib import Path
import re
import subprocess
import time

ROOT=Path(__file__).resolve().parent
file=ROOT/'staged'/'math-brain-inbox'/'w345'/'bundle_001.json'
bundle=json.loads(file.read_text(encoding='utf-8'))
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w345'
entries=bundle['entries']
assert 0<len(entries)<=200
keys={e['key'] for e in entries}
assert len(keys)==len(entries)
logical={e['namespace']+':'+e['logical_name'] for e in entries}
assert len(logical)==len(entries)
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
allowed_licenses=('cc-by-sa','cc-by','cc0','apache-2.0','gfdl','public-domain','mit','arxiv-nonexclusive','owner-own-work')
for entry in entries:
    assert required<=entry.keys()
    assert re.fullmatch(r'[a-z][a-z0-9-]*(\.[a-z][a-z0-9-]*)+',entry['namespace'])
    assert re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*',entry['logical_name'])
    assert entry['kind'] in {'definition','lemma','theorem','concept'}
    assert isinstance(entry['statement'],str) and len(entry['statement'])>30
    assert isinstance(entry['assumptions'],list)
    if entry['kind'] in {'lemma','theorem'}:
        assert isinstance(entry['proof_text'],str) and len(entry['proof_text'])>50
    else:
        assert entry['proof_text'] is None
    source=entry['source']
    assert {'source_id','url','revision','license','excerpt'}<=source.keys()
    assert source['license'].lower().startswith(allowed_licenses)
    assert source['url'].startswith('file:///')
    assert 'independent-audit-pending' in source['revision']

cards=json.loads((ROOT/'cards.json').read_text(encoding='utf-8'))
existing={c['logical_id']:c['statement'] for c in cards if c['logical_id'] is not None}
allowed_relations={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
dependency={key:[] for key in keys}
edge_rows=[json.loads(line) for line in (ROOT/'edges.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(edge_rows)==len(bundle['relations'])
for edge,evidence in zip(bundle['relations'],edge_rows):
    assert edge['kind'] in allowed_relations and edge['from_key'] in keys
    assert ('to_key' in edge)^('to_existing_logical' in edge)
    target=next(e for e in entries if e['key']==edge['to_key'])['statement'] if 'to_key' in edge else existing[edge['to_existing_logical']]
    origin=next(e for e in entries if e['key']==edge['from_key'])
    assert evidence['from_quote'] in origin['statement'] or evidence['from_quote'] in (origin['proof_text'] or '')
    assert evidence['to_quote'] in target
    assert '\n' not in edge['rationale']
    assert evidence['audit_status']=='PENDING_W347'
    if edge['kind']=='depends_on' and 'to_key' in edge:
        dependency[edge['from_key']].append(edge['to_key'])

visiting=set()
visited=set()
def visit(key):
    assert key not in visiting,'Cyclic depends_on relation'
    if key in visited:
        return
    visiting.add(key)
    for child in dependency[key]:
        visit(child)
    visiting.remove(key)
    visited.add(key)
for key in keys:
    visit(key)

# Exercise the actual delivered unified diffs on new local empty mirrors.
# Git discovery stops at ROOT, so no original repository is touched.
scratch=ROOT/('patch_validation_'+str(time.time_ns()))
assert scratch.resolve().is_relative_to(ROOT)
scratch.mkdir()
env=dict(os.environ)
env['GIT_CEILING_DIRECTORIES']=str(ROOT)
patches=[('01_brain_drafts.diff','math-brain-inbox/w345/bundle_001.json',file),('02_hook_proposals.diff','primary_directive/hooks1000/proposals/math-w345.jsonl',ROOT/'staged'/'primary_directive'/'hooks1000'/'proposals'/'math-w345.jsonl')]
patch_results=[]
for name,relative,expected in patches:
    target=scratch/relative
    assert target.resolve().is_relative_to(scratch.resolve())
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(b'')
    patch=ROOT/'patches'/name
    for command in (['git','apply','--check',str(patch)],['git','apply',str(patch)]):
        result=subprocess.run(command,cwd=scratch,env=env,capture_output=True,text=True,encoding='utf-8')
        assert result.returncode==0,(name,result.stdout,result.stderr)
    assert target.read_bytes()==expected.read_bytes(),name
    patch_results.append(dict(patch=name,status='PASS',bytes=target.stat().st_size))

out=dict(status='PASS',entries=len(entries),relations=len(bundle['relations']),all_external_targets_resolved_in_read_only_snapshot=True,all_edges_quote_both_ends=True,depends_on_acyclic=True,patches=patch_results,patch_scratch=str(scratch),production_ingestion_run=False,command='python -B -X utf8 validate_bundle.py')
(ROOT/'validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
