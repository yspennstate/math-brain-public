"""Independent normalized-matrix check of every rational spectral bracket."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[k]='1'
import json
from pathlib import Path
import networkx as nx
import numpy as np


def main():
    certificates=json.loads(Path('data/regular_exact_certificates.json').read_text())
    total_edges=total_matchings=0;max_discrepancy=0.
    for record in certificates:
        g=nx.from_graph6_bytes(record['graph6'].encode())
        n,d=record['n'],record['d']
        assert nx.is_connected(g) and set(dict(g.degree()).values())=={d}
        a=nx.to_numpy_array(g)
        assert len(record.get('edges',[]))==n*(n-1-d)//2
        for kind in ['edges','matchings']:
            for candidate in record.get(kind,[]):
                b=a.copy()
                edges=[candidate['edge']] if kind=='edges' else candidate['edges']
                for u,v in edges:
                    assert b[u,v]==0
                    b[u,v]=b[v,u]=1
                if kind=='matchings':
                    assert sorted(u for edge in edges for u in edge)==list(range(n))
                deg=b.sum(axis=1)
                normalized=np.eye(n)-b/np.sqrt(deg[:,None]*deg[None,:])
                value=float(np.linalg.eigvalsh(normalized)[1])
                lo,hi,q=candidate['bracket']
                assert lo/q-1e-12<value<hi/q+1e-12
                max_discrepancy=max(max_discrepancy,abs(value-(lo+hi)/(2*q)))
                if kind=='edges':total_edges+=1
                else:total_matchings+=1
    for n in [2,4,6]:
        atlas=[g for g in nx.graph_atlas_g() if len(g)==n and nx.is_connected(g)
               and len(set(dict(g.degree()).values()))==1]
        selected=[r for r in certificates if r['n']==n]
        assert len(atlas)==len(selected)
        assert all(any(nx.is_isomorphic(g,nx.from_graph6_bytes(r['graph6'].encode()))
                       for r in selected) for g in atlas)
    result=dict(graphs=len(certificates),edges=total_edges,matchings=total_matchings,
                max_distance_to_certified_interval_midpoint=max_discrepancy,
                independent_atlas_orders=[2,4,6],all_checks_passed=True)
    Path('data/graph_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
