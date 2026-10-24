"""Read-only store resolution and exact quote/schema checks; never ingest."""
import json
import re
import sqlite3
from pathlib import Path
from package_result import ROOT,IDS

REQUIRED={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
REL_KINDS={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
LICENSES=('cc-by-sa','cc-by','cc0','apache-2.0','gfdl','public-domain','mit','arxiv-nonexclusive','owner-own-work')

def run():
    c=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True)
    c.row_factory=sqlite3.Row
    cards=json.loads((ROOT/'store_cards.json').read_text(encoding='utf-8'))
    problems=json.loads((ROOT/'problem_cards.json').read_text(encoding='utf-8'))
    cited={}
    for groups in (cards,problems):
        for rows in groups.values():
            for card in rows:
                cited[json.loads(card['metadata_json'])['logical_id']]=card
    totals=dict(bundles=0,entries=0,lemmas=0,concepts=0,relations=0,quoted_edges=0,
                resolved_cross_links=0,acyclic_dependency_checks=0,local_inbox_byte_matches=0)
    keys_seen=set();logical_seen=set();index=[]
    for i,pid in enumerate(IDS,1):
        file=ROOT/'bundles'/f'bundle_{i:03d}.json'
        bundle=json.loads(file.read_text(encoding='utf-8'))
        assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w336'
        assert 'PENDING' in bundle['audit_status']
        assert 0<len(bundle['entries'])<=200
        entries={e['key']:e for e in bundle['entries']}
        assert len(entries)==len(bundle['entries'])
        edges={key:[] for key in entries}
        for e in entries.values():
            assert REQUIRED<=set(e)
            assert e['kind'] in ('definition','lemma','theorem','concept')
            assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
            assert re.fullmatch('[a-z0-9]+(?:[.-][a-z0-9]+)*',e['namespace'])
            assert len(e['statement'])>=80
            assert bool(e['proof_text']) if e['kind'] in ('lemma','theorem') else e['proof_text'] is None
            assert set(e['source'])>={'source_id','url','revision','license','excerpt'}
            assert e['source']['license'].lower().startswith(LICENSES)
            logical=f'math:{e["namespace"]}:{e["logical_name"]}'
            assert e['key'] not in keys_seen and logical not in logical_seen
            keys_seen.add(e['key']);logical_seen.add(logical)
            assert not c.execute('SELECT 1 FROM nodes WHERE json_extract(metadata_json,\'$.logical_id\')=? LIMIT 1',(logical,)).fetchone()
            totals['entries']+=1
            if e['kind']=='lemma':totals['lemmas']+=1
            if e['kind']=='concept':totals['concepts']+=1
            index.append(dict(problem_id=pid,key=e['key'],logical_id=logical,kind=e['kind'],statement=e['statement'],
                              proof=str(ROOT/'proofs'/f'{pid}.md'),audit_status='pending-w346'))
        for rel in bundle['relations']:
            assert rel['kind'] in REL_KINDS and rel['from_key'] in entries
            assert ('to_key' in rel)^('to_existing_logical' in rel)
            assert rel['rationale']
            quotes=re.findall(r'"([^"]+)"',rel['rationale'])
            assert len(quotes)==2 and quotes[0] in entries[rel['from_key']]['statement']
            if 'to_existing_logical' in rel:
                target=rel['to_existing_logical']
                assert target in cited and quotes[1] in cited[target]['body']
                hit=c.execute('SELECT id,body FROM nodes WHERE id=?',(cited[target]['id'],)).fetchone()
                assert hit and quotes[1] in hit['body']
                metadata=c.execute('SELECT metadata_json FROM nodes WHERE id=?',(hit['id'],)).fetchone()[0]
                assert json.loads(metadata)['logical_id']==target
                totals['resolved_cross_links']+=1
            else:
                assert rel['to_key'] in entries and quotes[1] in entries[rel['to_key']]['statement']
                if rel['kind']=='depends_on':edges[rel['from_key']].append(rel['to_key'])
            totals['relations']+=1;totals['quoted_edges']+=1
        done=set();visiting=set()
        def dfs(key):
            assert key not in visiting
            if key in done:return
            visiting.add(key)
            for target in edges[key]:dfs(target)
            visiting.remove(key);done.add(key)
        for key in edges:dfs(key)
        totals['acyclic_dependency_checks']+=1
        live=Path('~/math-brain-inbox/w336')/file.name
        assert live.read_bytes()==file.read_bytes()
        assert (ROOT/'patches'/f'{i:02d}_{pid.lower()}.diff').is_file()
        totals['local_inbox_byte_matches']+=1;totals['bundles']+=1
    c.close()
    totals['verdict']='PASS'
    totals['live_ingestion']='not run; independent KEEP pending'
    (ROOT/'measurements/bundle_validation.json').write_text(json.dumps(totals,indent=2),encoding='utf-8')
    (ROOT/'CARD_INDEX.json').write_text(json.dumps(index,indent=2),encoding='utf-8')
    print(json.dumps(totals))
    return totals

if __name__=='__main__':run()
