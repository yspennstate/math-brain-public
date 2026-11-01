"""Validate the draft contract and stage reviewer patches without live writes."""
import difflib
import json
import re
import sqlite3
from pathlib import Path

ROOT=Path(__file__).resolve().parent
bundle=json.loads(ROOT.joinpath('drafts/bundle_001.json').read_text(encoding='utf-8'))
mapping=json.loads(ROOT.joinpath('entry_problem_map.json').read_text(encoding='utf-8'))
cards=json.loads(ROOT.joinpath('store_cards.json').read_text(encoding='utf-8'))
metrics=json.loads(ROOT.joinpath('measurements.json').read_text(encoding='utf-8'))
assert metrics['completed'] is True
assert 'a bounded density, then the convergence is almost sure.' in ROOT.joinpath('source_scope_checks.md').read_text(encoding='utf-8')
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w339'
assert 0<len(bundle['entries'])<=200
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
source_required={'source_id','url','revision','license','excerpt'}
licenses=('cc-by-sa','cc-by','cc0','apache-2.0','gfdl','public-domain','mit','arxiv-nonexclusive','owner-own-work')
by_key={e['key']:e for e in bundle['entries']}
assert len(by_key)==len(bundle['entries'])
identities=set()
for e in bundle['entries']:
    assert required<=e.keys()
    assert e['kind'] in ('definition','lemma','theorem','concept')
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
    assert re.fullmatch(r'[a-z0-9-]+(?:\.[a-z0-9-]+)+',e['namespace'])
    assert isinstance(e['statement'],str) and len(e['statement'])>30
    assert not e['statement'].endswith('...')
    if e['kind'] in ('lemma','theorem'):
        assert isinstance(e['proof_text'],str) and len(e['proof_text'])>80
    else:assert e['proof_text'] is None
    assert source_required<=e['source'].keys()
    assert e['source']['license'].lower().startswith(licenses)
    identity='math:'+e['namespace']+':'+e['logical_name']
    assert identity not in identities
    identities.add(identity)

existing={c['metadata']['logical_id']:c for c in cards if c['metadata'].get('logical_id')}
allowed=('depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association')
deps={key:[] for key in by_key}
cross_links=0
quote_errors=[]
for relation in bundle['relations']:
    assert relation['from_key'] in by_key and relation['kind'] in allowed
    assert ('to_key' in relation)!=('to_existing_logical' in relation)
    if 'to_key' in relation:
        assert relation['to_key'] in by_key
        if relation['kind']=='depends_on':deps[relation['from_key']].append(relation['to_key'])
    else:
        assert relation['to_existing_logical'] in existing
        cross_links+=1
    # Every rationale already quotes both ends; verify those quotes are actual slices.
    quotes=[json.loads(q) for q in re.findall(r'"(?:[^"\\]|\\.)*"',relation['rationale'])]
    assert len(quotes)>=2
    assert quotes[0] in by_key[relation['from_key']]['statement']
    target=by_key[relation['to_key']]['statement'] if 'to_key' in relation else existing[relation['to_existing_logical']]['body']
    if quotes[1] not in target:
        quote_errors.append({'relation':relation,'parsed_quotes':quotes,'resolved_target_prefix':target[:700],
                             'other_observed_targets':[c['body'][:700] for c in cards if c['metadata'].get('logical_id')==relation.get('to_existing_logical')]})

if quote_errors:
    ROOT.joinpath('validation_failures.json').write_text(json.dumps(quote_errors,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(quote_errors[:2],ensure_ascii=False,indent=2),flush=True)
    raise AssertionError(f'{len(quote_errors)} quoted target mismatches; inspect saved node versions')

def visit(key,active,done):
    assert key not in active, 'depends_on cycle'
    if key in done:return
    for parent in deps[key]:visit(parent,active|{key},done)
    done.add(key)
done=set()
for key in deps:visit(key,set(),done)
assert set(mapping.values())=={'P0267','C0031','C0134','P0092','P0439','C0040','C0079','C0122','P0011','P0037'}
for key in by_key:
    assert any(r['from_key']==key and 'to_existing_logical' in r for r in bundle['relations'])

hooks=[json.loads(line) for line in ROOT.joinpath('hooks-proposals.jsonl').read_text(encoding='utf-8').splitlines()]
controls=[]
for hook in hooks:
    assert len(hook['text'])<=300 and hook['proposer']=='w339'
    fire=bool(re.search(hook['cue'],hook['fire_when']))
    silent=not bool(re.search(hook['cue'],hook['silent_when']))
    assert fire and silent, hook['id']
    controls.append({'id':hook['id'],'fire_pass':fire,'silent_pass':silent})
ROOT.joinpath('hook_controls.json').write_text(json.dumps(controls,indent=2)+'\n',encoding='utf-8')

dbpath=Path('~/math-brain-build/local/population/brain.sqlite3')
with sqlite3.connect(dbpath.as_uri()+'?mode=ro',uri=True,timeout=3) as db:
    sql='SELECT count(*) FROM nodes WHERE json_extract(metadata_json,\'$.logical_id\') IN ('+','.join('?' for _ in identities)+')'
    baseline_count=db.execute(sql,tuple(identities)).fetchone()[0]

patchdir=ROOT/'patches'
patchdir.mkdir(exist_ok=True)
targets=[('drafts/bundle_001.json','~/math-brain-inbox/w339/bundle_001.json','01_w339_brain_bundle.diff'),
         ('hooks-proposals.jsonl','~/primary_directive/hooks1000/proposals/math-w339.jsonl','02_w339_hook_proposals.diff')]
for local,live,name in targets:
    lines=ROOT.joinpath(local).read_text(encoding='utf-8').splitlines(keepends=True)
    diff=''.join(difflib.unified_diff([],lines,fromfile='a/'+live,tofile='b/'+live))
    assert diff.startswith('--- a/'+live+'\n+++ b/'+live+'\n')
    patchdir.joinpath(name).write_text(diff,encoding='utf-8')

summary={'valid':True,'entries':len(by_key),'relations':len(bundle['relations']),
         'cross_links_to_observed_existing_cards':cross_links,'internal_relations':len(bundle['relations'])-cross_links,
         'problems':len(set(mapping.values())),'schema':'mathbrain-draft-v1',
         'proposed_logical_ids_already_live':baseline_count,'staged_new_entries':len(identities),
         'live_after_measurement':'not run; deployment reserved for reviewer after audit',
         'hooks':len(hooks),'hook_fire_passes':len(controls),'hook_silent_passes':len(controls),
         'keeps_received':0,'patches':[name for _,_,name in targets],
         'command':'python -X utf8 ~/brain_workers/w339/validate_package.py'}
ROOT.joinpath('validation.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
