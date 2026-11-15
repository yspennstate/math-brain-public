"""Check census invariants, failure-certificate coverage and representative exact spectra."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json
from pathlib import Path
import numpy as np,networkx as nx,sympy as sp
from search import gap
from certify import below,lap,compare
ROOT=Path(__file__).resolve().parents[1]
expected={(3,6):2,(3,8):5,(3,10):19,(3,12):85,(3,14):509,(3,16):4060,(4,6):1,(4,8):6,(4,10):59,(4,12):1544}
intended=set();edgecount=matchcount=graphs=0;sample_comparisons=0
for file in sorted((ROOT/'data').glob('search_d*.jsonl')):
 rows=[json.loads(x) for x in file.open()];s=json.loads((ROOT/'data'/file.name.replace('search_','summary_').replace('.jsonl','.json')).read_text());assert len(rows)==expected[s['d'],s['n']]
 assert len({r['g6'] for r in rows})==len(rows)
 for r in rows:
  g=nx.from_graph6_bytes(r['g6'].encode());assert nx.is_connected(g) and all(d==r['d'] for _,d in g.degree())
  assert len(r['edges'])==r['n']*(r['n']-1-r['d'])//2;assert all(not g.has_edge(*e) for e in r['edges']);edgecount+=len(r['edges']);graphs+=1
  if r['simple']:
   for k in ['naive','corrected']:
    if r[k]['strong_failure']:intended.add((file.name,r['id'],k))
   if r.get('matching',{}).get('strong_failure'):intended.add((file.name,r['id'],'matching'))
  matchcount+=r.get('matching',{}).get('count',0)
  # Independently evaluate the lazy transition matrix on one graph per census.
  if r['id']==0 and r['edges']:
   a=nx.to_numpy_array(g);e=r['edges'][0];a[e[0],e[1]]=a[e[1],e[0]]=1;D=a.sum(axis=1);P=.5*(np.eye(len(a))+a/D[:,None]);ev=np.linalg.eigvals(P);lazy=1-sorted(ev.real)[-2]
   assert abs(2*lazy-r['edge_gaps'][0])<1e-10;sample_comparisons+=1
certs=[json.loads(x) for x in (ROOT/'data/failure_certificates.jsonl').open()];actual={(c['source'],c['id'],c['kind']) for c in certs};assert len(actual)==len(certs) and actual==intended
# A second spectral calculation using exact characteristic-polynomial root isolation.
x=sp.symbols('x');exact=[]
for kind,file,id in [('edge','search_d3_n10.jsonl',9),('matching','search_d4_n8.jsonl',2)]:
 r=next(z for z in map(json.loads,(ROOT/'data'/file).open()) if z['id']==id);a=nx.to_numpy_array(nx.from_graph6_bytes(r['g6'].encode()),dtype=int).tolist()
 candidates=[[[0,2]],[[2,4]]] if kind=='edge' else [m for m,g in r['matching']['heuristic']]+r['matching']['best'][:1]
 vals=[]
 for extra in candidates:
  L,D=lap(a,extra);p=(sp.diag(*[sp.Rational(1,d) for d in D])*sp.Matrix(L)).charpoly(x).as_poly();iv=sp.polys.polytools.intervals(p,eps=sp.Rational(1,10**10));positive=[(a,b,m) for (a,b),m in iv if a>0];lo,hi,m=positive[0];vals.append((lo,hi));exact.append({'kind':kind,'added':extra,'charpoly':str(sp.factor(p.as_expr())),'gap_interval':[str(lo),str(hi)]})
 assert vals[0][1]<vals[1][0]
result={'graphs':graphs,'edges':edgecount,'matchings':matchcount,'failure_certificate_keys_equal_all_observed_strong_failures':True,'certificates':len(certs),'independent_lazy_kernel_checks':sample_comparisons,'exact_root_checks':exact}
(ROOT/'data/audit_summary.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
