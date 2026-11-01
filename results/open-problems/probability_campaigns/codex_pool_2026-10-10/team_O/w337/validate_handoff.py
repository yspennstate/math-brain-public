from pathlib import Path
import ast
import json
import re
import time

ROOT=Path(__file__).resolve().parent

def norm(text):
    return text.replace('\r',' ').replace('\n',' ')

def main():
    start=time.perf_counter()
    bundle=json.loads((ROOT/'bundles'/'bundle_001.json').read_text(encoding='utf-8'))
    assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w337'
    entries=bundle['entries']; relations=bundle['relations']
    assert len(entries)==20 and len(relations)==34
    bykey={e['key']:e for e in entries}
    assert len(bykey)==len(entries)
    logical={(e['namespace'],e['logical_name']) for e in entries}
    assert len(logical)==len(entries)
    allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
    for e in entries:
        assert set(e)=={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
        assert re.fullmatch(r'[a-z][a-z0-9-]*(?:\.[a-z][a-z0-9-]*)+',e['namespace'])
        assert re.fullmatch(r'[a-z][a-z0-9-]*',e['logical_name'])
        assert len(e['statement'])>=100 and e['title'].startswith('[Blind audit pending]')
        assert isinstance(e['assumptions'],list) and e['assumptions']
        assert e['source']['license'].startswith('owner-own-work')
        assert e['source']['source_id'].startswith('owner-campaign:w337:')
        if e['kind'] in ('lemma','theorem'):
            assert isinstance(e['proof_text'],str) and len(e['proof_text'])>=100
        else:
            assert e['kind'] in ('definition','concept') and e['proof_text'] is None
        assert 'It does not - its standard deviation stays near 1' not in (e['proof_text'] or '')
    cards=json.loads((ROOT/'evidence'/'store_cards.json').read_text(encoding='utf-8'))
    card_byid={c['id']:c for c in cards}
    evidence=json.loads((ROOT/'evidence'/'edge_quotes.json').read_text(encoding='utf-8'))
    assert len(evidence)==len(relations)
    graph={key:[] for key in bykey}
    for rel,ev in zip(relations,evidence):
        assert rel['kind'] in allowed and rel['from_key']==ev['from_key']
        assert ev['source_quote'] in norm(bykey[ev['from_key']]['statement'])
        assert ev['source_quote'] in rel['rationale'] and ev['target_quote'] in rel['rationale']
        if 'to_key' in rel:
            assert 'to_existing_logical' not in rel
            assert ev['target_quote'] in norm(bykey[rel['to_key']]['statement'])
            if rel['kind']=='depends_on':
                graph[rel['from_key']].append(rel['to_key'])
        else:
            card=card_byid[ev['existing_card_id']]
            assert rel['to_existing_logical']==card['metadata']['logical_id']
            assert ev['target_quote'] in norm(card['body'])
    seen=set(); active=set()
    def visit(key):
        if key in seen:
            return
        assert key not in active,'depends_on cycle'
        active.add(key)
        for target in graph[key]:
            visit(target)
        active.remove(key); seen.add(key)
    for key in graph:
        visit(key)
    scripts={p.stem for p in ROOT.glob('*_check.py') if p.stem!='baseline_p0209'}
    metrics={}
    for pid in ('P0209','P0459','C0130','P0088','P0336','C0022','C0076','C0117','P0009','P0035'):
        measurement=ROOT/'measurements'/(pid.lower()+'.json')
        assert measurement.is_file() and (ROOT/(pid+'.md')).is_file()
        m=json.loads(measurement.read_text(encoding='utf-8'))
        assert m['command']=='python -X utf8 '+pid.lower()+'_check.py'
        assert pid.lower()+'_check' in scripts
        metrics[pid]=measurement.as_posix()
    baseline=json.loads((ROOT/'measurements'/'p0209_before_after.json').read_text(encoding='utf-8'))
    assert baseline['baseline']['monte_carlo_scale_count']==4
    assert baseline['replacement']['exact_fraction_identity_cases']==6
    assert json.loads((ROOT/'measurements'/'p0209_boundaries.json').read_text(encoding='utf-8'))['exact_boundary_cases']==2
    lean=json.loads((ROOT/'measurements'/'lean_algebra.json').read_text(encoding='utf-8'))
    assert lean['status']=='UNAVAILABLE' and 'distressed' in lean['error']
    hooks=[json.loads(line) for line in (ROOT/'proposals'/'math-w337.jsonl').read_text(encoding='utf-8').splitlines()]
    assert len(hooks)==2
    for h in hooks:
        assert set(h)=={'id','area','event','cue','fire_when','silent_when','text','evidence','proposer'}
        assert h['proposer']=='w337' and len(h['text'])<=300
        assert re.search(h['cue'],h['fire_when']) and not re.search(h['cue'],h['silent_when'])
    audit=json.loads((ROOT/'AUDIT_REQUEST_w347.json').read_text(encoding='utf-8'))
    assert audit['state']=='PENDING_BLIND_CHECK' and len(audit['entries'])==20
    assert audit['solution_counted'] is False
    assert (ROOT/'patches'/'01_ten_problem_bundle.diff').read_text(encoding='utf-8').startswith('--- a/~/math-brain-inbox/w337/')
    assert (ROOT/'patches'/'02_math_hook_proposals.diff').read_text(encoding='utf-8').startswith('--- a/~/primary_directive/hooks1000/proposals/math-w337.jsonl')
    parsed=0
    for p in ROOT.glob('*.py'):
        ast.parse(p.read_text(encoding='utf-8-sig'),filename=str(p))
        parsed+=1
    result={'command':'python -X utf8 validate_handoff.py','verdict':'PASS',
            'problem_results':10,'draft_nodes':len(entries),'quoted_edges':len(relations),
            'edge_quotes_checked':len(evidence),'dependency_cycles':0,
            'hook_fire_controls_passed':2,'hook_silent_controls_passed':2,
            'python_files_syntax_checked':parsed,'measurement_paths':metrics,
            'blind_audit':'PENDING','lean':'UNAVAILABLE','solutions_promoted':0,
            'elapsed_seconds':time.perf_counter()-start}
    (ROOT/'measurements'/'handoff_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='measurement_paths'},indent=2))

if __name__=='__main__':
    main()
