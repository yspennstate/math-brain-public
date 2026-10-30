"""A017-twelve-edit-plane-frontier-v1: fixed six-control even-lattice tests."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib,time,argparse,importlib.util
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
p=R.parent/'20261011T234546Z-fleet05-A017-recursive-addressing/code/check.py'
s=importlib.util.spec_from_file_location('u',p);U=importlib.util.module_from_spec(s);s.loader.exec_module(U)
def planes():
 spaces=sorted({tuple(sorted([0,a,b,a^b])) for a in range(1,16) for b in range(a+1,16)})
 for V in spaces:
  for coset in sorted({tuple(sorted(x^z for x in V)) for z in range(16)}):yield V,coset
def integer_good(g,n,i):
 W=U.fwht(g);w=[v//2 for v in W];P=Q=1;m=0
 for s in range(1<<n):
  if s>>i&1:continue
  t,u=w[s]**2,w[s|(1<<i)]**2
  if t+u:P*=(t+u)**(t+u)
  if t:Q*=t**t
  if u:Q*=u**u
  m+=u
 return P<=Q<<(4*m),P,Q,m
def restrict(g,n,i,b):return [g[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(1<<(n-1))]
def good_tree(g,n):
 if len(set(g))==1:return 0
 inf=[F(sum(g[x]!=g[x^(1<<j)] for x in range(1<<n)),1<<n) for j in range(n)]
 i=max(range(n),key=lambda j:inf[j]);ok,*_=integer_good(g,n,i);assert ok
 return 1+sum(good_tree(restrict(g,n,i,b),n-1) for b in [0,1])
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--plan',action='store_true');ap.add_argument('--pilot',action='store_true');a=ap.parse_args()
 if a.plan:print(json.dumps(dict(full_cases=sum(1 for _ in planes()),pilot_cases=4)));return
 start=time.perf_counter();q=[(0,1),(1,2),(3,4)];base=U.signs(6,0,q);allE={3|(x<<2) for x in range(16)};bad=queries=cases=0;first=None;digest=hashlib.sha256()
 for V,coset in list(planes())[:4 if a.pilot else None]:
  E=allE-{3|(x<<2) for x in coset};g=[-v if x in E else v for x,v in enumerate(base)]
  ok,P,Q,m=integer_good(g,6,0);assert m==128
  sp={0:U.fwht(g)};inf=U.spectral_metrics(sp,6)[0]
  if not ok:
   bad+=1
   if first is None:
    B=U.erasure(sp,6,0);first=dict(q_edges=q,E=sorted(E),removed_plane=list(coset),influences=[str(t) for t in inf],root_C=str(U.spectral_metrics(U.spectrum(g,[0]*64),6)[2][0]),B=B.json(),badness=dict(P=str(P),Q_times_2_power_512=str(Q<<512),positive_slack=str(P-(Q<<512))))
  queries+=good_tree(g,6);digest.update(json.dumps([V,coset,ok]).encode()+b'\n');cases+=1
 result=dict(status='PASS',helper='A017-twelve-edit-plane-frontier-v1',pilot=a.pilot,cases=cases,minimum_index_root_K4_bad=bad,maximum_influence_repair_K4_bad=0,repaired_query_nodes=queries,first_bad_fixture=first,coverage_sha256=digest.hexdigest(),elapsed_seconds=time.perf_counter()-start)
 (R/'out'/('frontier12_pilot.json' if a.pilot else 'frontier12_certificate.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k!='first_bad_fixture'}))
if __name__=='__main__':main()
