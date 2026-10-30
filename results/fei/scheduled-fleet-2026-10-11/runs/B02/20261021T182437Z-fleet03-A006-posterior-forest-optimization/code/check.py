"""Floating proposal, exact rational upper certificates for tangent support LPs."""
import os
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,json,time
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from math import prod
from scipy.optimize import linprog
BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
OLD=ROOT/'runs/20261014T074929Z-fleet05-A006-posterior-forest-optimization'
sys.path.insert(0,str(OLD/'code'))
from star_full import enumerate_runs
checks=0
def ck(p):
 global checks
 checks+=1
 assert p,checks
def spectrum(E,n):
 f=[1 if any(all(x>>v&1 for v in e) for e in E) else -1 for x in range(1<<n)]
 w=f[:];s=1
 while s<len(w):
  for i in range(0,len(w),2*s):
   for j in range(i,i+s):w[j],w[j+s]=w[j]+w[j+s],w[j]-w[j+s]
  s*=2
 P={A:F(z*z,1<<(2*n)) for A,z in enumerate(w) if A and z}
 I=sum(A.bit_count()*p for A,p in P.items())
 ck(I==F(sum(f[x]!=f[x^(1<<v)] for x in range(1<<n) for v in range(n)),1<<n))
 ck(sum(F(z*z,1<<(2*n)) for z in w)==1)
 return P,I
def cuts(E,n,lifted):
 N=len(E);M=1<<N;out={}
 def add(d,label):
  key=tuple(sorted((T,z) for T,z in d.items() if z))
  out.setdefault(key,label)
 ts=[F(0),F(1,4),F(1,2),F(1),F(2),F(4)]
 for i,j in combinations(range(N),2):
  if not set(E[i])&set(E[j]):continue
  pair=(1<<i)|(1<<j)
  for U in (range(M) if lifted else [0]):
   if U&pair:continue
   for t in ts:
    add({U|1<<i:-t*t,U|1<<j:F(-1),U|pair:4*(t+1)**2},['pair',U,i,j,str(t)])
 if lifted:
  for U in range(1,M):
   for v in range(n):
    row=[i for i,e in enumerate(E) if v in e and not U>>i&1]
    if row:add({U:F(-1),**{U|1<<i:F(4) for i in row}},['row',U,v])
 return [(dict(key),label) for key,label in out.items()]
def cap_support(score,caps):
 left=F(1);p={};theta=None
 for T in sorted(score,key=lambda t:(score[t],t),reverse=True):
  z=min(left,caps[T]);p[T]=z;left-=z
  if not left:theta=score[T];break
 ck(left==0)
 val=sum(p[T]*score[T] for T in p)
 ck(val==theta+sum(caps[T]*max(score[T]-theta,0) for T in score))
 return val,theta
def certificate(h,caps,rows,pactual):
 T=list(h);N=len(T)
 for a,label in rows:ck(sum(z*pactual[t] for t,z in a.items())<=0)
 if not rows:
  value,theta=cap_support(h,caps)
  return {'value':str(value),'theta':str(theta),'multipliers':[],'cut_count':0}
 matrix=[[float(a.get(t,0)) for t in T] for a,_ in rows]
 result=linprog([-float(h[t]) for t in T],A_ub=matrix,b_ub=[0]*len(rows),A_eq=[[1]*N],b_eq=[1],bounds=[(0,float(caps[t])) for t in T],method='highs',options={'time_limit':5.0,'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9,'threads':1})
 ck(result.success)
 # Neither the solver status nor its primal floating value proves a sign.
 multipliers=[];score=dict(h)
 for j,z in enumerate(result.ineqlin.marginals):
  y=F(max(0.,-float(z))).limit_denominator(10**8)
  if not y:continue
  multipliers.append([j,str(y)])
  for t,a in rows[j][0].items():score[t]-=y*a
 value,theta=cap_support(score,caps)
 # All constraints in the final certificate are exact and finite.
 for t in T:ck(h[t]<=theta+sum(F(y)*rows[j][0].get(t,0) for j,y in multipliers)+max(score[t]-theta,0))
 return {'value':str(value),'theta':str(theta),'multipliers':multipliers,'cut_count':len(rows)}
def graph(row):
 E=tuple(map(tuple,row['edges']));n=row['n'];N=len(E)
 deg=[sum(v in e for e in E) for v in range(n)]
 lam=[F(1,2*max(deg))]*N;D=prod(1+x/4 for x in lam)-1
 P,I=spectrum(E,n);v=sum(P.values());C={};Q={};runs=0
 for A in range(1,1<<n):
  if any(A>>j&1 and not deg[j] for j in range(n)):ck(A not in P);continue
  C[A],r=enumerate_runs(A,n-1,edges=E);runs+=r
  Q[A]=sum(c*prod(lam[i] for i in range(N) if U>>i&1) for U,c in C[A].items())/D
 ck(sum(Q.values())<=1)
 h={U:sum(P[A]*C[A].get(U,F(0))*4**U.bit_count()/Q[A] for A in P) for U in range(1,1<<N)}
 ck({str(t):str(z) for t,z in h.items()}==row['h'])
 ck(str(I)==row['I'] and str(v)==row['V'] and runs==row['runs'])
 p={U:prod(lam[i]/4 for i in range(N) if U>>i&1)/D for U in h}
 ck(sum(p.values())==1 and sum(p[t]*h[t] for t in h)==v)
 caps={int(t):F(data['cap']) for t,data in row['root_caps'].items()}
 ck(all(0<p[t]<=caps[t] for t in h))
 results={}
 for name,cc in [('cap',[]),('pair',cuts(E,n,False)),('lifted',cuts(E,n,True))]:
  c=certificate(h,caps,cc,p);c['gap']=str(F(c['value'])-v);ck(F(c['gap'])>=0);results[name]=c
 ck(F(results['cap']['gap'])==F(row['new_gap']))
 # Rounded duals need not be monotone. Taking the best earlier certified bound is valid.
 results['pair']['best_value']=str(min(F(results[x]['value']) for x in ['cap','pair']))
 results['lifted']['best_value']=str(min(F(results[x]['value']) for x in results))
 return {'n':n,'edges':E,'I':str(I),'v':str(v),'runs':runs,'h':{str(t):str(z) for t,z in h.items()},'caps':{str(t):str(z) for t,z in caps.items()},'certificates':results,'strict_pair':F(results['pair']['best_value'])<F(results['cap']['value']),'strict_lifted':F(results['lifted']['best_value'])<F(results['pair']['best_value']),'best_bit_gap_over_I':str(2*(F(results['lifted']['best_value'])-v)/I)}
def main():
 start=time.monotonic();pilot='--pilot' in sys.argv
 source=ROOT.parent/'A010/runs/20261021T161852Z-fleet03-A010-universal-residual-falsifier/out'/('PILOT.json' if pilot else 'CHECK.json')
 data=json.loads(source.read_text(encoding='utf-8'));rows=[]
 for row in data['rows']:
  rows.append(graph(row))
  (BASE/'out'/('PILOT_CHECKPOINT.json' if pilot else 'CHECKPOINT.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
  ck(time.monotonic()-start<55)
 out={'status':'PASS','helper_version':'A006-anchored-root-packing-v1','graphs':len(rows),'assertions':checks,'distinct_runs':sum(r['runs'] for r in rows),'strict_pair':sum(r['strict_pair'] for r in rows),'strict_lifted':sum(r['strict_lifted'] for r in rows),'seconds':time.monotonic()-start,'rows':rows}
 (BASE/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':main()
