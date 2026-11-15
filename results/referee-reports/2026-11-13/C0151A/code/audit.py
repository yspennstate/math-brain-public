"""Independent checks of saved experiment witnesses, summaries and inputs."""
import json
import math
from pathlib import Path
import statistics

ROOT=Path(__file__).resolve().parents[1]
folder=ROOT/'data'/'final'
rows=[json.loads(line) for line in (folder/'samples.jsonl').read_text().splitlines()]
checks=0
for row in rows:
    n=row['n'];edges=[tuple(edge) for edge in row['edges']]
    assert len(edges)==3*n//2 and len(set(edges))==len(edges)
    degrees=[0]*n
    for u,v in edges:
        assert 0<=u<v<n;degrees[u]+=1;degrees[v]+=1
    assert set(degrees)=={3}
    candidates=[('heuristic_set','heuristic_size')]
    if 'exact_set' in row:candidates.append(('exact_set','exact_size'))
    for skey,zkey in candidates:
        S=set(row[skey]);assert len(S)==len(row[skey])==row[zkey]
        assert all(u not in S or v not in S for u,v in edges);checks+=1
    for S,size in zip(row['local_sets'],row['local_sizes']):
        S=set(S);assert len(S)==size
        assert all(u not in S or v not in S for u,v in edges);checks+=1
    if 'exact_size' in row:
        assert max(row['local_sizes'])<=row['exact_size']
        assert row['heuristic_size']<=row['exact_size']
    if 'independent_milp_size' in row:
        assert row['exact_size']==row['independent_milp_size']

for summary in json.loads((folder/'summary.json').read_text()):
    group=[row for row in rows if row['n']==summary['n']];n=summary['n']
    assert len(group)==summary['graphs']
    for key in ['local','parallel_greedy','gaussian_only']:
        means=[statistics.mean(row[key+'_sizes'])/n for row in group]
        assert math.isclose(statistics.mean(means),summary[key+'_mean'],abs_tol=1e-14)
        se=statistics.stdev(means)/math.sqrt(len(means))
        assert math.isclose(se,summary[key+'_graph_SE'],abs_tol=1e-14)
    assert math.isclose(statistics.mean(row['heuristic_size']/n for row in group),summary['heuristic_mean'],abs_tol=1e-14)

for path in ROOT.rglob('*'):
    if path.is_file():
        assert path.suffix.lower()!='.pdf',str(path)
        if path.parent==ROOT/'sources':
            assert path.suffix=='.txt'
            assert not path.read_bytes().startswith(b'%PDF')
            path.read_text()  # verify UTF-8

result={'graphs_checked':len(rows),'independent_sets_checked':checks,
        'exact_graphs':sum('exact_size' in row for row in rows),
        'separate_MILP_cross_checks':sum('independent_milp_size' in row for row in rows),
        'summary_recalculated':True,'pdf_files':0}
(folder/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
