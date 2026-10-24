import json
import pathlib
import re
import sqlite3

here=pathlib.Path(__file__).resolve().parent
refs=json.loads((here/'store_refs.json').read_text(encoding='utf-8'))
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
kinds={'definition','lemma','theorem','concept'}
relations_allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
licenses=('cc-by-sa','cc-by','cc0','apache-2.0','gfdl','public-domain','mit','arxiv-nonexclusive','owner-own-work')
bundles=sorted((here/'drafts').glob('bundle_*.json'))
nodes=relations=lemmas=concepts=0
logical_names=[]
targets=set()
for path in bundles:
    bundle=json.loads(path.read_text(encoding='utf-8'))
    assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w344'
    assert 0<len(bundle['entries'])<=200
    lookup={entry['key']:entry for entry in bundle['entries']}
    assert len(lookup)==len(bundle['entries'])
    for entry in bundle['entries']:
        assert required<=entry.keys()
        assert entry['kind'] in kinds
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',entry['logical_name'])
        assert re.fullmatch(r'[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)+',entry['namespace'])
        assert len(entry['statement'])>60 and isinstance(entry['assumptions'],list)
        if entry['kind'] in {'lemma','theorem'}:
            assert isinstance(entry['proof_text'],str) and len(entry['proof_text'])>100
            lemmas+=1
        else:
            assert entry['proof_text'] is None
            concepts+=1
        assert {'source_id','url','revision','license','excerpt'}<=entry['source'].keys()
        assert entry['source']['license'].lower().startswith(licenses)
        assert 'independent audit pending' in entry['source']['revision']
        logical_names.append('math:'+entry['namespace']+':'+entry['logical_name'])
        nodes+=1
    outgoing={key:[] for key in lookup}
    for relation in bundle['relations']:
        assert relation['from_key'] in lookup and relation['kind'] in relations_allowed
        assert 'New end: "' in relation['rationale']
        assert 'existing end: "' in relation['rationale'] or 'goal end: "' in relation['rationale']
        source_quote=' '.join(lookup[relation['from_key']]['statement'].split()[:18])
        assert source_quote in relation['rationale']
        if 'to_key' in relation:
            assert relation['to_key'] in lookup
            target_quote=' '.join(lookup[relation['to_key']]['statement'].split()[:18])
            assert target_quote in relation['rationale']
            if relation['kind']=='depends_on':
                outgoing[relation['from_key']].append(relation['to_key'])
        else:
            logical=relation['to_existing_logical']
            targets.add(logical)
            found=[item for items in refs.values() for item in items if item['metadata']['logical_id']==logical]
            assert len(found)==1
            body=found[0]['body']
            if body.startswith('OPEN PROBLEM') and '). ' in body:
                body=body.split('). ',1)[1]
            assert ' '.join(body.split()[:18]) in relation['rationale']
        relations+=1
    def visit(key,active,done):
        assert key not in active,'depends_on cycle'
        if key in done:
            return
        for target in outgoing[key]:
            visit(target,active|{key},done)
        done.add(key)
    done=set()
    for key in lookup:
        visit(key,set(),done)
assert len(bundles)==10 and len(set(logical_names))==nodes
with sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True) as conn:
    conn.execute('PRAGMA query_only=ON')
    for logical in targets:
        assert conn.execute("SELECT count(*) FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=?",(logical,)).fetchone()[0]>0
    already_present=sum(conn.execute("SELECT count(*) FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=?",(logical,)).fetchone()[0] for logical in logical_names)
    c0139_anchor_count=conn.execute("SELECT count(*) FROM nodes WHERE json_extract(metadata_json,'$.bundle_entry_key')='op-c0139'").fetchone()[0]
hook_controls=[]
for line in (here/'math-w344.jsonl').read_text(encoding='utf-8').splitlines():
    hook=json.loads(line)
    assert len(hook['text'])<=300
    assert re.search(hook['cue'],hook['fire_when'])
    assert not re.search(hook['cue'],hook['silent_when'])
    hook_controls.append(hook['id'])
# Reconstruct every additive diff inside a local mirror; verify headers and payloads.
mirror=here/'verification'/'patch_mirror'
mirror.mkdir(parents=True,exist_ok=True)
patch_files=0
for diff_path in (here/'patches').glob('*.diff'):
    lines=diff_path.read_text(encoding='utf-8').splitlines(keepends=True)
    cursor=0
    while cursor<len(lines):
        assert lines[cursor].startswith('--- a/')
        live=lines[cursor][6:].strip()
        assert lines[cursor+1]=='+++ b/'+live+'\n'
        count=re.fullmatch(r'@@ -0,0 \+1,(\d+) @@\n',lines[cursor+2])
        assert count
        size=int(count.group(1))
        payload=lines[cursor+3:cursor+3+size]
        assert len(payload)==size and all(line.startswith('+') for line in payload)
        raw=''.join(line[1:] for line in payload)
        candidate=(mirror/live).resolve()
        assert candidate.is_relative_to(mirror.resolve())
        candidate.parent.mkdir(parents=True,exist_ok=True)
        candidate.write_text(raw,encoding='utf-8')
        original=here/'drafts'/pathlib.Path(live).name if live.startswith('math-brain-inbox/') else here/'math-w344.jsonl'
        assert raw==original.read_text(encoding='utf-8')
        patch_files+=1
        cursor+=3+size
report={'bundles':len(bundles),'nodes':nodes,'lemma_nodes':lemmas,'concept_nodes':concepts,'relations':relations,'existing_targets_verified_read_only':len(targets),'proposed_logical_ids_already_in_store':already_present,'exact_c0139_goal_cards_in_store_before':c0139_anchor_count,'additive_patch_payloads_verified':patch_files,'hook_fire_and_silent_controls':hook_controls,'independent_audit':'PENDING w346','live_store_modified':False}
(here/'validation_receipt.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))
