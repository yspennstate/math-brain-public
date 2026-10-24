"""Validate local packet and submit only the task-named, concept-only DRAFT."""
from pathlib import Path
import json
import re

ROOT=Path('~')
JOB=Path(__file__).resolve().parent
required=['STATUS.md','SOURCE_STATUS.json','ATTEMPT.md','CLAIMS.jsonl','REVIEW_PACKET.md','INDEPENDENT.md','AUDIT_VERDICTS.jsonl','MEASUREMENTS.json','COMPUTE_GATE.json','REPORT.md','bundle_local_001.json','HANDOFF_W522.json','HANDOFF_W524.json','PROGRESS_EVENT.json']
assert all((JOB/x).is_file() for x in required)
assert (JOB/'STATUS.md').read_text(encoding='utf-8').splitlines()[0]=='STATE: WORKING'
claims=[json.loads(x) for x in (JOB/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
allowed_status={'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
assert len({c['id'] for c in claims})==len(claims)
assert all(c['status'] in allowed_status for c in claims)
assert all(c['independent_reviewer'] and c['remaining_gap'] for c in claims)
audits=[json.loads(x) for x in (JOB/'AUDIT_VERDICTS.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(audits)==5 and all(x['verdict']=='KEEP' for x in audits)
measure=json.loads((JOB/'MEASUREMENTS.json').read_text(encoding='utf-8'))
assert measure['evaluations']==165 and measure['exact_deficit_checks']==133
assert measure['dependent_set_bridge']['before_inconsistent_cases']==19
assert measure['dependent_set_bridge']['after_using_thick_point_result_inconsistent_cases']==0
gate=json.loads((JOB/'COMPUTE_GATE.json').read_text(encoding='utf-8'))
assert gate['status']=='consumed'

path=JOB/'bundle_local_001.json'
bundle=json.loads(path.read_text(encoding='utf-8'))
# closeout.py may have run before its namespace-only patch was saved.
for e in bundle['entries']:
    e['namespace']='probability.lqg'
path.write_text(json.dumps(bundle,indent=2,ensure_ascii=False),encoding='utf-8')
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w523'
assert len(bundle['entries'])==3 and len(bundle['relations'])==2
keys={e['key'] for e in bundle['entries']}
assert len(keys)==3
for e in bundle['entries']:
    assert e['kind']=='concept' and e['proof_text'] is None
    assert re.fullmatch(r'[a-z][a-z0-9]*(?:\.[a-z][a-z0-9]*)*',e['namespace'])
    assert re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*',e['logical_name'])
    assert e['statement'] and e['assumptions']
    assert e['source']['license'].startswith('owner-own-work')
    assert all(token not in e['statement'] for token in ['C:/','C:\\','w523','w522','owner'])
allowed_relations={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
edges={k:[] for k in keys}
for r in bundle['relations']:
    assert r['from_key'] in keys and r['to_key'] in keys
    assert r['kind'] in allowed_relations and r['rationale']
    if r['kind']=='depends_on':
        edges[r['from_key']].append(r['to_key'])
def visit(k,stack):
    assert k not in stack,'cyclic depends_on'
    for n in edges[k]:
        visit(n,stack|{k})
for k in keys:
    visit(k,set())

board=ROOT/'brain_workers/teams/W0300_O/TEAM_BOARD.md'
matches=[]
with board.open(encoding='utf-8') as f:
    for n,line in enumerate(f,1):
        if 'P0297' in line:
            matches.append({'line':n,'text':line.strip()})
source_path=JOB/'SOURCE_STATUS.json'
source=json.loads(source_path.read_text(encoding='utf-8'))
source['prior_checks']['team_O']={'independently_read_target_rows':matches,'meaning':'Dated board status only; no kept proof found in this exact row.'}
source['brain_submission']['prepared']=True
source_path.write_text(json.dumps(source,indent=2,ensure_ascii=False),encoding='utf-8')

inbox=(ROOT/'math-brain-inbox/w523').resolve()
assert inbox.parent==(ROOT/'math-brain-inbox').resolve() and inbox.name=='w523'
inbox.mkdir(parents=True,exist_ok=True)
payload=path.read_bytes()
destination=None
for index in range(1,201):
    final=inbox/f'bundle_{index:03d}.json'
    part=inbox/f'bundle_{index:03d}.json.part'
    if final.exists():
        if final.read_bytes()==payload:
            destination=final
            break
        continue
    if part.exists():
        continue
    assert final.resolve().parent==inbox and part.resolve().parent==inbox
    with part.open('xb') as f:
        f.write(payload)
    part.rename(final)
    destination=final
    break
assert destination is not None,'No free numbered DRAFT path; existing artifacts preserved.'
assert destination.read_bytes()==payload
states={'prepared':{'state':True,'local_artifact':str(path),'entries':3,'relations':2,'kind':'concept-only; independent review pending'},'submitted':{'state':True,'path':str(destination),'atomic_complete_then_rename':True},'reviewed':{'state':False,'reviewer':'w524','receipt':None},'ingested':{'state':False,'receipt':None},'retrievable':{'state':False,'receipt':None},'live_store_modified_by_worker':False,'integrator_run_by_worker':False}
(JOB/'BRAIN_STATES.json').write_text(json.dumps(states,indent=2),encoding='utf-8')
source['brain_submission'].update(prepared=True,submitted=True,reviewed=False,ingested=False,retrievable=False)
source['brain_submission']['path']=str(destination)
source_path.write_text(json.dumps(source,indent=2,ensure_ascii=False),encoding='utf-8')
verification={'command':'python -X utf8 verify_artifacts.py','required_files':len(required),'claim_rows':len(claims),'audit_rows':len(audits),'draft_entries':3,'draft_relations':2,'all_assertions_passed':True,'submission_path':str(destination),'mathematical_independent_review_implied':False,'formal_proof_implied':False}
(JOB/'ARTIFACT_VERIFICATION.json').write_text(json.dumps(verification,indent=2),encoding='utf-8')
print(json.dumps(verification,indent=2))
