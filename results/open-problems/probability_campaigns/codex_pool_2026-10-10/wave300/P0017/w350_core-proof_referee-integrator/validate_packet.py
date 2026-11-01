from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parent
BASE=Path('~')
required=['SOURCE_STATUS.json','ATTEMPT.md','CLAIMS.jsonl','REVIEW_PACKET.json','REVIEW_PACKET.md','REPORT.md','BUNDLE_STATES.json','RELATIONS.jsonl','STATUS.md','OPERATOR_WEIGHTED_COUNTEREXAMPLE.md']
assert all((ROOT/p).is_file() for p in required)
source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
# Only the initials in the inspected primary bibliography were established for Song-Zhang.
source['recent_primary_claims'][1]['authors']=['Z. Song','X. Zhang']
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

states=json.loads((ROOT/'BUNDLE_STATES.json').read_text(encoding='utf-8'))
peer_paths=list((BASE/'math-brain-inbox'/'w348').glob('bundle_*.json'))
states['bundle_002']['duplicate_author_check']={'observed_queued_peer_files':[str(p) for p in peer_paths],'decision':'Keep the reviewer copy unsubmitted. Apply the w350 KEEP verdicts to the original author bundle; the coordinator must avoid duplicate mathematical nodes.'}
for key in ['bundle_001','bundle_002','bundle_003']:
    states[key]['ingestion_verification']='No coordinator receipt or retrieval run has been checked; the false flags mean unverified, not a claimed inspection of integration.'
(ROOT/'BUNDLE_STATES.json').write_text(json.dumps(states,indent=2)+'\n',encoding='utf-8')
packet=json.loads((ROOT/'REVIEW_PACKET.json').read_text(encoding='utf-8'))
packet['bundle_states']=states
packet['independent_account_identity']='Not verified from private profiles; one independent worker KEEP is recorded for each peer claim, not two account keeps.'
(ROOT/'REVIEW_PACKET.json').write_text(json.dumps(packet,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
summaries=[]
for filename in ['bundle_001.json','bundle_002.json','bundle_003.json']:
    b=json.loads((ROOT/'drafts'/filename).read_text(encoding='utf-8'))
    assert b['spec']=='mathbrain-draft-v1' and b['author_agent']=='w350'
    keys={e['key'] for e in b['entries']}
    assert len(keys)==len(b['entries'])
    for e in b['entries']:
        assert all(k in e for k in ['key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'])
        assert e['namespace']=='probability.core'
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
        assert e['kind'] in {'definition','concept','lemma','theorem'}
        assert e['statement'].strip()
        assert e['source']['license'].startswith('owner-own-work')
        if e['kind'] in {'lemma','theorem'}:assert e['proof_text'] and e['proof_text'].strip()
        else:assert e['proof_text'] is None
    graph={k:[] for k in keys}
    for rel in b['relations']:
        assert rel['from_key'] in keys and rel['kind'] in allowed
        if 'to_key' in rel:assert rel['to_key'] in keys
        else:assert rel['to_existing_logical'].startswith('math:probability.core:')
        if rel['kind']=='depends_on' and 'to_key' in rel:graph[rel['from_key']].append(rel['to_key'])
    visiting=set();done=set()
    def visit(k):
        assert k not in visiting,'Dependency cycle'
        if k in done:return
        visiting.add(k)
        for child in graph[k]:visit(child)
        visiting.remove(k);done.add(k)
    for key in keys:visit(key)
    summaries.append({'file':filename,'entries':len(b['entries']),'relations':len(b['relations']),'dependency_cycle':False})

rows=[json.loads(s) for s in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
assert all(r['status'] in {'conjecture','numerical evidence','sketch','proved special case','independently checked proof'} for r in rows)
assert all(r['parent_problem_solved'] is False for r in rows)
edges=[json.loads(s) for s in (ROOT/'RELATIONS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
assert all(r['from_statement_quote'] and r['to_statement_quote'] for r in edges)
assert len(packet['verdicts'])==14
assert sum(v['verdict']=='KEEP' for v in packet['verdicts'])==13
assert sum(v['verdict']=='FIX' for v in packet['verdicts'])==1
assert packet['own_review_status']=='PENDING'

hooks=[json.loads(s) for s in (ROOT/'drafts'/'math-w350.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
assert len(hooks)==2 and all(len(hook['text'])<=300 for hook in hooks)
assert re.search(hooks[0]['cue'],'September ranking P0017 attempted_un')
assert not re.search(hooks[0]['cue'],'Scoped Gaussian lemma; exact current primary sources recorded; no novelty claim')
assert re.search(hooks[1]['cue'],'Variance-weighted covariance bound inferred from an unweighted expectation')
assert not re.search(hooks[1]['cue'],'Exact conditional expectation estimate proved with all dependence retained')
assert states['bundle_001']['submitted'] is True and states['bundle_002']['submitted'] is False
assert (BASE/'math-brain-inbox'/'w350'/'bundle_002.part').exists()
assert states['bundle_003']['submitted'] is False
assert (BASE/'math-brain-inbox'/'w350'/'bundle_003.part').exists()
assert len(rows)==10 and len(edges)==15
assert all(r['status']=='sketch' and r['independent_reviewer']=='w353' for r in rows if r['id'] in {'w350-C005','w350-C006'})
for number,suffix in [('001','.json'),('002','.part'),('003','.part')]:
    assert json.loads((ROOT/'drafts'/('bundle_'+number+'.json')).read_text(encoding='utf-8'))==json.loads((BASE/'math-brain-inbox'/'w350'/('bundle_'+number+suffix)).read_text(encoding='utf-8'))
result={'status':'PASS','command':'python -X utf8 validate_packet.py','bundles':summaries,'claim_rows':len(rows),'peer_KEEPs':13,'historical_FIXs':1,'relations_with_both_ends_quoted':len(edges),'hook_controls':{'fire':True,'silent':True},'formal_proof_assistant_used':False,'live_store_written':False}
(ROOT/'measurements'/'packet_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result),flush=True)
