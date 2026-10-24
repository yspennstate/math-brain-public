"""Run the real draft parser read-only, then check links, quotes and controls."""
import copy
import importlib.util
import json
import os
from pathlib import Path
import sqlite3
import sys
import time

ROOT=Path(__file__).resolve().parent
sys.dont_write_bytecode=True


def readonly_audit(event,args):
    if event=='open' and isinstance(args[0],(str,bytes,os.PathLike)):
        path=Path(os.fsdecode(args[0])).resolve()
        if path.suffix.lower() in {'.pem','.key'} or path.name.lower() in {'auth.json','.env','rclone.conf'}:
            raise PermissionError('secret reads are forbidden')
        if args[2] & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND) and not path.is_relative_to(ROOT):
            raise PermissionError('writes outside worker folder are forbidden')
    elif event=='sqlite3.connect':
        if not str(args[0]).startswith('file:') or 'mode=ro' not in str(args[0]):
            raise PermissionError('only explicit read-only SQLite connections permitted')
    elif event in {'os.remove','os.rmdir','subprocess.Popen','socket.connect'}:
        raise PermissionError('read-only validation: '+event)
    elif event=='os.mkdir' and not Path(args[0]).resolve().is_relative_to(ROOT):
        raise PermissionError('mkdir outside worker folder is forbidden')


sys.addaudithook(readonly_audit)
start=time.perf_counter()
live=Path('~/math-brain-build/tools/integrate_drafts.py')
spec=importlib.util.spec_from_file_location('w342_readonly_integrator',live)
integrator=importlib.util.module_from_spec(spec)
spec.loader.exec_module(integrator)
manifest=json.loads((ROOT/'bundle_handoff.json').read_text(encoding='utf-8'))
db=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True)
entries=relations=existing_links=quote_checks=0
unique_logicals=set()
targets=set()
before=0
parsed=[]
payloads={item['bundle_file']:json.loads((ROOT/item['bundle_file']).read_text(encoding='utf-8')) for item in manifest}
wanted=set()
for payload in payloads.values():
    wanted.update('math:'+e['namespace']+':'+e['logical_name'] for e in payload['entries'])
    wanted.update(edge['to_existing_logical'] for edge in payload['relations'] if edge.get('to_existing_logical'))
placeholders=','.join('?' for _ in wanted)
existing_by_logical={}
for logical,body in db.execute("select json_extract(metadata_json,'$.logical_id'),body from nodes where json_extract(metadata_json,'$.logical_id') in ("+placeholders+")",tuple(sorted(wanted))):
    existing_by_logical.setdefault(logical,[]).append(body)
for item in manifest:
    path=ROOT/item['bundle_file']
    payload,errors=integrator.parse_draft(path)
    assert not errors,(path,errors)
    parsed.append(payload)
    by_key={e['key']:e for e in payload['entries']}
    for entry in payload['entries']:
        logical='math:'+entry['namespace']+':'+entry['logical_name']
        assert logical not in unique_logicals
        unique_logicals.add(logical)
        before+=len(existing_by_logical.get(logical,[]))
        entries+=1
    for edge in payload['relations']:
        relations+=1
        source=by_key[edge['from_key']]['statement'].replace('\n',' ')
        if edge.get('to_existing_logical'):
            rows=existing_by_logical.get(edge['to_existing_logical'],[])
            assert rows,edge['to_existing_logical']
            target_bodies=[body.replace('\n',' ') for body in rows]
            targets.add(edge['to_existing_logical'])
            existing_links+=1
        else:
            target_bodies=[by_key[edge['to_key']]['statement'].replace('\n',' ')]
        rationale=edge['rationale']
        from_quote,rest=rationale[len('FROM "'):].split('"; TO "',1)
        to_quote=rest.split('"; ',1)[0]
        assert rationale.startswith('FROM "') and from_quote in source
        assert any(to_quote in body for body in target_bodies)
        quote_checks+=2
    # A reviewer can reconstruct exactly the file that the unified diff adds.
    patch=(ROOT/item['patch_file']).read_text(encoding='utf-8').splitlines(keepends=True)
    assert patch[0].rstrip()=='--- a/'+item['intended_live_path']
    assert patch[1].rstrip()=='+++ b/'+item['intended_live_path']
    reconstructed=''.join(line[1:] for line in patch[3:] if line.startswith('+'))
    assert reconstructed==path.read_text(encoding='utf-8')

cases=ROOT/'validation_cases'
cases.mkdir(exist_ok=True)
seed=parsed[0]
mutants=[]
x=copy.deepcopy(seed); x['entries'][1]['proof_text']=''; mutants.append(('missing-proof',x))
x=copy.deepcopy(seed); x['entries'][0]['source']['license']='author own work'; mutants.append(('unaccepted-license',x))
x=copy.deepcopy(seed); x['relations'][0]['kind']='fails_under'; mutants.append(('unsupported-relation',x))
x=copy.deepcopy(seed); a,b=x['entries'][0]['key'],x['entries'][1]['key']; x['relations'].extend([{'from_key':a,'to_key':b,'kind':'depends_on','rationale':'control'},{'from_key':b,'to_key':a,'kind':'depends_on','rationale':'control'}]); mutants.append(('dependency-cycle',x))
x=copy.deepcopy(seed); x['entries'][0]['source']['url']=''; mutants.append(('missing-source-url',x))
rejected=[]
for name,payload in mutants:
    path=cases/(name+'.json')
    path.write_text(json.dumps(payload,ensure_ascii=False),encoding='utf-8')
    _,errors=integrator.parse_draft(path)
    assert errors,name
    rejected.append({'control':name,'errors':errors})

receipt={'command':'python -X utf8 validate_bundles.py','parser_used':str(live)+'::parse_draft','valid_bundles':len(manifest),'proposed_entries':entries,'proposed_relations':relations,'existing_parent_targets':len(targets),'resolved_existing_links':existing_links,'exact_endpoint_quote_checks':quote_checks,'rejected_negative_controls':len(rejected),'negative_controls':rejected,'before_matching_new_logical_ids_in_live_store':before,'after_matching_ids_in_prepared_drafts':len(unique_logicals),'deployed_store_change':0,'seconds':round(time.perf_counter()-start,3)}
(ROOT/'bundle_validation.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k!='negative_controls'},indent=2))
