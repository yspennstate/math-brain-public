import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import json,time
import numpy as np
import networkx as nx
from search import matchings,gap
ROOT=Path(__file__).resolve().parents[1]
def scan(name,g):
    a=nx.to_numpy_array(g,dtype=float);n=len(a);d=int(a[0].sum());count=0;best=-1;second=-1;example=None;ties=0;batch=[];ms=[];start=time.monotonic()
    def consume():
        nonlocal best,second,example,ties,count
        if not batch:return
        values=1-np.linalg.eigvalsh(np.array(batch)/(d+1))[:,-2]
        for m,x in zip(ms,values):
            x=float(x);count+=1
            if x>best+1e-9:second=best;best=x;example=m;ties=1
            elif abs(x-best)<1e-9:ties+=1
            elif x>second:second=x
        batch.clear();ms.clear()
    for m in matchings(a):
        b=a.copy()
        for u,v in m:b[u,v]=b[v,u]=1
        batch.append(b);ms.append(m)
        if len(batch)==2048:consume()
    consume()
    r={'name':name,'n':n,'d':d,'g6':nx.to_graph6_bytes(g,header=False).decode().strip(),'matching_count':count,'numerical_best_gap':best,'numerical_second_distinct_gap':second,'one_best_matching':example,'numerical_tie_count':ties,'baseline_gap':gap(a),'elapsed_seconds':time.monotonic()-start,'gap_convention':'nonlazy normalized; lazy gap half this value','heuristic_tested':False}
    (ROOT/'data'/f'family_{name}.json').write_text(json.dumps(r,indent=2)+'\n');print(name,count,best,round(r['elapsed_seconds'],2),flush=True)
if __name__=='__main__':
 for n in range(4,17,2):scan('cycle'+str(n),nx.cycle_graph(n))
 for dims in [(3,4),(4,4)]:scan('torus'+'x'.join(map(str,dims)),nx.convert_node_labels_to_integers(nx.cartesian_product(nx.cycle_graph(dims[0]),nx.cycle_graph(dims[1]))))
