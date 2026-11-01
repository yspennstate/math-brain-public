"""Validate drafts with the isolated live parser, endpoints and deployment diffs."""
import ast
import itertools
import json
import pathlib
import re
import sqlite3
import subprocess
import types

ROOT=pathlib.Path(__file__).resolve().parent
LIVE=pathlib.Path('~/math-brain-build/tools/integrate_drafts.py')
with LIVE.open(encoding='utf-8') as f:
    constants=''.join(itertools.islice(f,68,97))
with LIVE.open(encoding='utf-8') as f:
    functions=''.join(itertools.islice(f,138,244))
tree=ast.parse(constants+'\n'+functions)
assert all(isinstance(n,(ast.Assign,ast.FunctionDef)) for n in tree.body)
assert {n.name for n in tree.body if isinstance(n,ast.FunctionDef)}=={'require','parse_draft'}
ns={'Path':pathlib.Path,'json':json}
for label in ['ClaimKind','EdgeKind']:
    attrs={n.attr for n in ast.walk(tree) if isinstance(n,ast.Attribute)
           and isinstance(n.value,ast.Name) and n.value.id==label}
    # The pure parser uses these enums only as dictionary/set identities.
    ns[label]=types.SimpleNamespace(**{k:label+'.'+k for k in attrs})
overlay=pathlib.Path('~/math-brain-build/src/math_brain/overlay.py')
with overlay.open(encoding='utf-8') as f:
    regex_line=next(line for line in itertools.islice(f,60) if line.startswith('IDENTIFIER_RE ='))
regex_ast=ast.parse(regex_line).body[0]
pattern=ast.literal_eval(regex_ast.value.args[0])
ns['IDENTIFIER_RE']=re.compile(pattern)
(ROOT/'parser_snapshot.py').write_text(constants+'\n'+functions,encoding='utf-8')
exec(compile(tree,'isolated_live_parse_draft','exec'),ns)
bundle,errors=ns['parse_draft'](ROOT/'drafts/bundle_001.json')
assert not errors,errors
by_key={e['key']:e for e in bundle['entries']}
quotes=[json.loads(s) for s in (ROOT/'edge_quotes.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(quotes)==len(bundle['relations'])
normalize=lambda s:' '.join(s.split())
store=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True)
external=0
for edge,q in zip(bundle['relations'],quotes):
    assert q['from_key']==edge['from_key']
    assert q['from_quote'] in normalize(by_key[q['from_key']]['statement'])
    if 'to_existing_logical' in edge:
        row=store.execute('SELECT body,metadata_json FROM nodes WHERE id=?',(q['target'],)).fetchone()
        assert row
        assert json.loads(row[1])['logical_id']==edge['to_existing_logical']
        assert q['to_quote'] in normalize(row[0])
        external+=1
    else:
        assert q['target']==edge['to_key']
        assert q['to_quote'] in normalize(by_key[edge['to_key']]['statement'])
store.close()
patch_results=[]
check_dir=ROOT/'patch_check';check_dir.mkdir(exist_ok=True)
for name,target,payload in [
    ('01_team_o_bundle','math-brain-inbox/w343/bundle_001.json',ROOT/'drafts/bundle_001.json'),
    ('02_hooks_proposals','primary_directive/hooks1000/proposals/math-w343.jsonl',ROOT/'hooks_proposals.jsonl')]:
    review=(ROOT/'patches'/f'{name}.diff').read_text(encoding='utf-8').splitlines(keepends=True)
    assert review[0]=='--- a/'+target+'\n' and review[1]=='+++ b/'+target+'\n'
    assert review[2].startswith('@@ -0,0 +1,')
    assert all(line.startswith('+') for line in review[3:])
    reconstructed=''.join(line[1:] for line in review[3:])
    assert reconstructed==payload.read_text(encoding='utf-8')
    apply_file=ROOT/'patches'/f'{name}.apply.diff'
    r=subprocess.run(['git','apply','--check',str(apply_file)],cwd=check_dir,
                     capture_output=True,text=True,encoding='utf-8',timeout=30)
    patch_results.append({'patch':apply_file.name,'exit_code':r.returncode,'stderr':r.stderr})
    assert r.returncode==0,patch_results[-1]
hooks=[json.loads(s) for s in (ROOT/'hooks_proposals.jsonl').read_text(encoding='utf-8').splitlines()]
required={'id','area','event','cue','fire_when','silent_when','text','evidence','proposer'}
for h in hooks:
    assert required<=h.keys() and len(h['text'])<=300
    assert h['fire_when'] and h['silent_when'] and h['fire_when']!=h['silent_when']
audit=json.loads((ROOT/'W347_AUDIT_PACKET.json').read_text(encoding='utf-8'))
assert {p['key'] for p in audit['result_packets']}==by_key.keys()
assert all(p['audit_status']=='PENDING' for p in audit['result_packets'])
rows=[json.loads(s) for s in (ROOT/'results.jsonl').read_text(encoding='utf-8').splitlines()]
assert len({r['row_id'] for r in rows})==len(rows)
assert not any(r.get('new_solution_certified') for r in rows)
statuses=[]
for pid in ['P0340','C0036','P0013','P0150','C0003','C0060','C0085','C0131','P0016','P0046']:
    measure=ROOT/('measurement_'+pid.lower()+'.json')
    assert measure.exists()
    result={'problem_id':pid,'fresh_web_search':False,'current_literature_status':'not exhaustively verified',
            'audit_keeps':0,'measurement_file':measure.name,
            'candidate_keys':[p['key'] for p in audit['result_packets'] if p['problem_id']==pid]}
    result['outcome']=('author-checked linear expectation proof candidate' if pid=='P0340' else
                       'literature answer identified in cached receipt; primary check pending' if pid=='P0016' else
                       'partial lemma, reduction or route obstruction; general target not resolved in this pass')
    statuses.append(result)
(ROOT/'source_status_manifest.json').write_text(json.dumps(statuses,indent=2),encoding='utf-8')
measurement={'parser':'isolated actual parse_draft and require from live integrator; no integrator initialization',
             'identifier_pattern':pattern,'parser_errors':errors,'entries':len(by_key),
             'relations':len(quotes),'quoted_external_endpoints_verified':external,
             'quoted_internal_endpoints_verified':len(quotes)-external,
             'deployment_patches':patch_results,'hook_proposals_validated':len(hooks),
             'result_rows':len(rows),'problems_with_measurements':len(statuses),
             'independent_keeps':0,'current_lean_status':'SETUP_UNVERIFIED',
             'integration_ran':False,'live_store_modified':False}
(ROOT/'VALIDATION.json').write_text(json.dumps(measurement,indent=2),encoding='utf-8')
timings={f:json.loads((ROOT/f).read_text(encoding='utf-8'))['elapsed_seconds']
         for f in ['measurement_p0340.json','measurement_remaining_summary.json']}
(ROOT/'COSTS.json').write_text(json.dumps({'agent':'w343','calculation_seconds_as_reported':timings,
    'input_tokens':None,'output_tokens':None,'monetary_cost':None,
    'cost_note':'Session token and monetary telemetry is not exposed. Calculation timings exclude shell/tool waiting and module import.',
    'new_solution_certified':False},indent=2),encoding='utf-8')
print(json.dumps(measurement))
