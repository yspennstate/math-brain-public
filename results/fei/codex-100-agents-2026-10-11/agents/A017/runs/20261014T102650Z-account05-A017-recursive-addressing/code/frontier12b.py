"""A017-twelve-edit-coupled-point-frontier-v1: nonflat children at same edit count."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import importlib.util,json,time,hashlib,argparse
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('frontier',R/'code/frontier12.py');T=importlib.util.module_from_spec(s);s.loader.exec_module(T);U=T.U
def cases():
 allE={3|(x<<2) for x in range(16)}
 for V,coset in T.planes():
  original=allE-{3|(x<<2) for x in coset}
  for w in sorted(original):yield V,coset,w,original^{w,w^1}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');a=ap.parse_args();start=time.perf_counter();base=U.signs(6,0,[(0,1),(1,2),(3,4)])
 bad=queries=count=0;first=None;digest=hashlib.sha256()
 for V,coset,w,E in list(cases())[:2 if a.pilot else None]:
  assert len(E)==12;g=[-v if x in E else v for x,v in enumerate(base)];ok,P,Q,m=T.integer_good(g,6,0);assert m==128
  if not ok:
   bad+=1
   if first is None:
    sp=U.spectrum(g,[0]*64);inf,pairs,C,dc=U.spectral_metrics(sp,6);B=U.erasure(sp,6,0)
    first=dict(q_edges=[(0,1),(1,2),(3,4)],E=sorted(E),removed_plane=list(coset),coupled_edge=w,influences=[str(t) for t in inf],root_C=str(C[0]),B=B.json(),badness=dict(P=str(P),Q_times_2_power_512=str(Q<<512),positive_slack=str(P-(Q<<512))))
  queries+=T.good_tree(g,6);digest.update(json.dumps([V,coset,w,ok]).encode()+b'\n');count+=1
 result=dict(status='PASS',helper='A017-twelve-edit-coupled-point-frontier-v1',pilot=a.pilot,cases=count,minimum_index_root_K4_bad=bad,maximum_influence_repair_K4_bad=0,repaired_query_nodes=queries,first_bad_fixture=first,coverage_sha256=digest.hexdigest(),elapsed_seconds=time.perf_counter()-start)
 (R/'out'/('frontier12b_pilot.json' if a.pilot else 'frontier12b_certificate.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k!='first_bad_fixture'}))
if __name__=='__main__':main()
