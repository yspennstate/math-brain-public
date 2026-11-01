import ast
import itertools
import json
import pathlib
import re
import sqlite3
import time

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()
# Copy only the inspected read-only shape validator and require helper.
live=pathlib.Path('~/math-brain-build/tools/integrate_drafts.py')
with live.open(encoding='utf-8') as stream:
    validator_source=''.join(itertools.islice(stream,138,244))
parsed=ast.parse(validator_source)
assert all(isinstance(node,ast.FunctionDef) for node in parsed.body)
assert len(parsed.body)==2 and parsed.body[0].name=='require'
assert not any(isinstance(node, (ast.Import,ast.ImportFrom)) for node in ast.walk(parsed))
namespace={'json':json,'Path':pathlib.Path,'IDENTIFIER_RE':re.compile(r'[a-z][a-z0-9._-]*'),'DRAFT_KINDS':{k:k for k in ('definition','lemma','theorem','concept')},'PROOF_REQUIRED':{'lemma','theorem'},'DRAFT_RELATIONS':{k:k for k in ('depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association')},'ALLOWED_LICENSE_PREFIXES':('cc-by-sa','cc-by','cc0','apache-2.0','gfdl','public-domain','mit','arxiv-nonexclusive','owner-own-work')}
exec(compile(parsed,'offline-copied-shape-validator','exec'),namespace)
shape_validator=namespace[parsed.body[1].name]
(root/'shape_validator_copy.py').write_text(validator_source,encoding='utf-8')
files=sorted((root/'bundles').glob('bundle_*.json'))
assert len(files)==10
cards=json.loads((root/'baseline_cards.json').read_text(encoding='utf-8'))
card_map={json.loads(card['metadata_json']).get('logical_id'):card for card in cards if json.loads(card['metadata_json']).get('logical_id')}
bundles=[]
errors=[]
global_logical=set()
for path in files:
    bundle,shape_errors=shape_validator(path)
    errors.extend(str(path.name)+': '+error for error in shape_errors)
    bundles.append(bundle)
    for node in bundle['entries']:
        logical='math:'+node['namespace']+':'+node['logical_name']
        if logical in global_logical:
            errors.append('Duplicate global logical id: '+logical)
        global_logical.add(logical)
        if 'pending w347' not in node['title']:
            errors.append('Missing draft audit label: '+node['key'])
        if not pathlib.Path(node['source']['url'].removeprefix('file:///')).is_file():
            errors.append('Missing source artifact: '+node['key'])
requested_targets={relation['to_existing_logical'] for bundle in bundles for relation in bundle['relations'] if relation.get('to_existing_logical')}
ids=[card_map[logical]['id'] for logical in requested_targets if logical in card_map]
connection=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True,timeout=15)
found={}
if ids:
    query='SELECT id,title,body,metadata_json FROM nodes WHERE id IN ('+','.join('?' for _ in ids)+')'
    for node_id,title,body,metadata in connection.execute(query,ids):
        logical=json.loads(metadata).get('logical_id')
        if logical:
            found[logical]={'id':node_id,'title':title,'body':body}
connection.close()
for logical in requested_targets:
    if logical not in found:
        errors.append('Existing target absent from live read-only snapshot: '+logical)
quoted_edges=0
for bundle in bundles:
    nodes={node['key']:node for node in bundle['entries']}
    for relation in bundle['relations']:
        quotes=re.findall(r'"([^\"]+)"',relation['rationale'])
        if len(quotes)!=2:
            errors.append('Expected two endpoint quotes: '+relation['from_key'])
            continue
        source=nodes[relation['from_key']]
        source_text=source['statement']+'\n'+(source['proof_text'] or '')+'\n'+source['title']
        if quotes[0] not in source_text:
            errors.append('Source quote not verbatim: '+relation['from_key']+' -> '+quotes[0])
        if relation.get('to_existing_logical'):
            target=found.get(relation['to_existing_logical'],{})
            target_text=target.get('body','')
        else:
            target=nodes[relation['to_key']]
            target_text=target['statement']+'\n'+(target['proof_text'] or '')+'\n'+target['title']
        if quotes[1] not in target_text:
            errors.append('Target quote not verbatim: '+relation['from_key']+' -> '+quotes[1])
        quoted_edges+=1
measurements={}
problem_ids=['P0205','P0429','C0127','P0050','P0255','C0014','C0073','C0109','P0004','P0027']
for problem_id in problem_ids:
    path=root/(problem_id.lower()+'_measurement.json')
    value=json.loads(path.read_text(encoding='utf-8'))
    if not value['result'].startswith('PASS'):
        errors.append('Measurement did not pass: '+problem_id)
    measurements[problem_id]={'command':value['command'],'elapsed_seconds':value['elapsed_seconds'],'result':value['result']}
receipt={'command':'python -X utf8 validate_deliverables.py','bundles':len(bundles),'entries':sum(len(bundle['entries']) for bundle in bundles),'quoted_edges':quoted_edges,'existing_targets_found':len(found),'measurements':measurements,'sum_measurement_compute_seconds':sum(value['elapsed_seconds'] for value in measurements.values()),'errors':errors,'elapsed_seconds':round(time.perf_counter()-start,6),'result':'PASS' if not errors else 'FAIL','scope':'Actual shape-validator function run in an isolated read-only namespace; no ingestion or live-store write. Identifier rule uses the spec lowercase grammar.'}
(root/'validation_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False,indent=2),flush=True)
raise SystemExit(1 if errors else 0)
