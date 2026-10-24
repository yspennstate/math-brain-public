import json
import subprocess
from pathlib import Path
from time import perf_counter

root=Path(__file__).resolve().parent
started=perf_counter()
bundle=json.loads((root/'bundle_001.json').read_text(encoding='utf-8'))
inbox=json.loads(Path('~/math-brain-inbox/w496/bundle_001.json').read_text(encoding='utf-8'))
assert bundle==inbox
entries=bundle['entries']
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
for e in entries:
    assert required<=set(e)
    assert e['kind']=='concept' and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
    assert {'source_id','url','revision','license','excerpt'}<=set(e['source'])
    assert 'draft' in e['statement'].lower()
keys={e['key'] for e in entries}
assert len(keys)==len(entries)
dag={key:[] for key in keys}
for r in bundle['relations']:
    assert r['from_key'] in keys and r['to_key'] in keys
    if r['kind']=='depends_on': dag[r['from_key']].append(r['to_key'])
def visit(key,active,done):
    assert key not in active, 'depends_on cycle'
    if key in done: return
    for target in dag[key]: visit(target,active|{key},done)
    done.add(key)
done=set()
for key in keys: visit(key,set(),done)
claims=[json.loads(s) for s in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
assert len(claims)==8 and len({c['id'] for c in claims})==8
for c in claims:
    assert {'statement','assumptions','source','independent_reviewer','remaining_gap','status'}<=set(c)
    assert c['status']=='sketch'
audits=[json.loads(s) for s in (root/'AUDIT_w495.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
assert len(audits)==7 and all(a['verdict']=='KEEP' for a in audits)
hook=json.loads((root/'HOOK_PROPOSAL.jsonl').read_text(encoding='utf-8'))
assert len(hook['text'])<=300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
status=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
assert status['current_openness']=='UNKNOWN'
assert status['primary_source']['matches_recorded_intake_hash'] is True
bundle2=json.loads((root/'bundle_002.json').read_text(encoding='utf-8'))
assert bundle2==json.loads(Path('~/math-brain-inbox/w496/bundle_002.json').read_text(encoding='utf-8'))
assert len(bundle2['entries'])==2 and len(bundle2['relations'])==1
keys2={e['key'] for e in bundle2['entries']}
for e in bundle2['entries']:
    assert required<=set(e) and e['kind']=='concept' and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work') and 'draft' in e['statement'].lower()
for r in bundle2['relations']:
    assert r['from_key'] in keys2 and r['to_key'] in keys2 and r['kind']=='semantic_association'
correction=json.loads((root/'STORE_CORRECTION.json').read_text(encoding='utf-8'))
assert correction['card_id']=='claim_2b6b7c1da300a8ed1c28367cabd584f2c02769a03a64ed519cf081b1af04693d'
assert correction['live_store_write'] is False and 'UNKNOWN' in correction['corrected']['statement']

# Exercise the actual unified diff on a minimal isolated 120-line fixture.
# Only the named C0120 row is copied; no other intake item or private material is read into the fixture.
patch=root/'patches/01_c0120_source_scope.diff'
patch_lines=patch.read_text(encoding='utf-8').splitlines()
assert patch_lines[0].startswith('--- a/') and patch_lines[1].startswith('+++ b/')
target_relative=patch_lines[1][6:]
assert '..' not in Path(target_relative).parts and not Path(target_relative).is_absolute()
old=[s[1:] for s in patch_lines[3:] if s.startswith('-')]
new=[s[1:] for s in patch_lines[3:] if s.startswith('+')]
assert len(old)==len(new)==1
fixture=root/'review/patch_fixture'
target=fixture/target_relative
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text('\n'*119+old[0]+'\n',encoding='utf-8')
check=subprocess.run(['git','apply','--check',str(patch)],cwd=fixture,capture_output=True,text=True,encoding='utf-8')
assert check.returncode==0, check.stderr
apply=subprocess.run(['git','apply',str(patch)],cwd=fixture,capture_output=True,text=True,encoding='utf-8')
assert apply.returncode==0, apply.stderr
patched=target.read_text(encoding='utf-8').splitlines()
assert len(patched)==120 and patched[:119]==['']*119
assert json.loads(patched[-1])==json.loads((root/'source_row_after.json').read_text(encoding='utf-8'))
result={'command':'python -X utf8 ~/brain_workers/w496/validate_delivery.py','result':'PASS','draft_schema':'PASS','depends_on_acyclic':'PASS','claim_rows':len(claims),'peer_audits':len(audits),'draft_bundles':2,'draft_concepts':len(entries)+len(bundle2['entries']),'draft_relations':len(bundle['relations'])+len(bundle2['relations']),'actual_git_patch_check':'PASS','isolated_patch_apply':'PASS','unrelated_fixture_lines_unchanged':119,'live_file_writes':0,'proof_certificate':False,'elapsed_seconds':round(perf_counter()-started,6)}
(root/'VALIDATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
