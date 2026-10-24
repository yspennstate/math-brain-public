"""Verify read-only rescue fidelity and silence; create no SQLite fixtures."""
import json
from pathlib import Path
from unittest.mock import patch
import math_problem_probe

ROOT=Path(__file__).resolve().parent
STORE=Path('~/math-brain-build/local/population/brain.sqlite3')

def main():
    checks=[]
    for query in ['referee proof assumptions mistakes','P0017x','xP0017','P001','P00170']:
        with patch.object(math_problem_probe.sqlite3,'connect',side_effect=AssertionError('silent query accessed a store')):
            result=math_problem_probe.probe(query,STORE)
        assert result['status']=='not_applicable'
        checks.append({'query':query,'result':'silent; no connection'})
    with patch.object(math_problem_probe.sqlite3,'connect',side_effect=AssertionError('ambiguous query accessed a store')):
        result=math_problem_probe.probe('P0017 and P0018',STORE)
    assert result['status']=='ambiguous_problem_ids'
    checks.append({'query':'P0017 and P0018','result':'ambiguous; no connection'})
    missing=ROOT/'nonexistent_probe_store.sqlite3'
    assert not missing.exists()
    result=math_problem_probe.probe('P0017',missing)
    assert result['status']=='lookup_unavailable' and not missing.exists()
    checks.append({'query':'P0017; nonexistent path','result':'failed softly; no file created'})
    connections=[]
    real_connect=math_problem_probe.sqlite3.connect
    def observed_connect(*args,**kwargs):
        connections.append({'uri':args[0],'uri_flag':kwargs.get('uri')})
        assert str(args[0]).endswith('?mode=ro') and kwargs.get('uri') is True
        return real_connect(*args,**kwargs)
    with patch.object(math_problem_probe.sqlite3,'connect',side_effect=observed_connect):
        result=math_problem_probe.probe('P0017 KLS referee proof assumptions mistakes',STORE,2.0)
    assert result['status']=='historical_cards_found'
    assert len(result['hits'])==2
    assert all('p0017' in hit['logical_id'] for hit in result['hits'])
    assert any('This special case does not prove' in hit['statement'] for hit in result['hits'])
    assert all(hit['truth_status']=='unverified' for hit in result['hits'])
    assert all(hit['independent_proof_review']=='not_established_by_this_lookup' for hit in result['hits'])
    (ROOT/'probe_after.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    checks.append({'query':'P0017 exact rescue','result':'2 complete historical cards; truth status preserved','seconds':result['elapsed_seconds']})
    report={'checks':checks,'passed':len(checks),'connections':connections,
            'baseline_file':'recall_mistakes.txt','baseline_relevant_top3':0,
            'rescue_relevant_hits':len(result['hits']),
            'comparison_scope':'One observed query, explicit standalone rescue; no live ranking/global-recall change or general performance claim.'}
    (ROOT/'PROBE_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()
