from pathlib import Path
import sys,json,time
from fractions import Fraction as F
import exact as E
R=Path(__file__).resolve().parents[1]
START=time.perf_counter();CHECKS=0
def ck(b):
 global CHECKS
 assert b
 CHECKS+=1
 assert time.perf_counter()-START<55
def save(name,obj):
 (R/'out'/name).write_text(json.dumps(obj,indent=2),encoding='utf-8')
def entropy(p):return E.ent(p.values())
def ce(p,q):return E.add(entropy(p),E.kl(p,q))
def ge(v):ck(not v or E.bounds(v)[0]>=0)
def table(m,r):
 def h(z):
  v=1
  for j in range(m):
   if (z>>(r*j))&((1<<r)-1)==(1<<r)-1:v=-v
  return v
 return tuple(1-2*((u>>1)&1) if not u&1 else h(u>>3) if u&4 else 1 for u in range(1<<(3+m*r)))
def step(t,coords,q,i):
 p,inf=E.spec(t,coords);j=coords.index(i);co=tuple(x for x in coords if x!=i)
 mask=sum(1<<x for x in co);pe=E.marginal(p,mask);qe=E.marginal(q,mask)
 ts=[E.restrict(t,j,b) for b in (0,1)];ps=[E.spec(z,co)[0] for z in ts]
 ck(sum(q.values())==1)
 for s in qe:ck(pe.get(s,F(0))==(ps[0].get(s,F(0))+ps[1].get(s,F(0)))/2)
 joint=[{s:w*(ps[b].get(s,F(0))/(2*pe[s]) if pe.get(s,F(0)) else F(1,2)) for s,w in qe.items()} for b in (0,1)]
 qb=[sum(v.values()) for v in joint];ck(sum(qb)==1 and min(qb)>0)
 Q=[{s:w/qb[b] for s,w in joint[b].items() if w} for b in (0,1)]
 # Independently exact likelihood product on every occupied atom/branch.
 for s,pv in p.items():
  u=s&mask;er=(pv/pe[u])/(q[s]/qe[u])
  for b in (0,1):
   if ps[b].get(u,F(0)):
    ck(pv/q[s]==er*(F(1,2)/qb[b])*(ps[b][u]/Q[b][u]))
 erased=E.add(E.kl(p,q),E.scale(E.kl(pe,qe),-1))
 outcome=E.kl({0:F(1,2),1:F(1,2)},{0:qb[0],1:qb[1]})
 terminal=E.add(*(E.scale(E.kl(ps[b],Q[b]),F(1,2)) for b in (0,1)))
 # Log-vector normalization need not have a unique factorization; intervals
 # are used only for strict inequalities, atom products establish identities.
 ge(erased);ge(outcome)
 ck(sum(inf.values())==inf[i]+sum(sum(E.spec(z,co)[1].values()) for z in ts)/2)
 return ts,co,Q,erased,outcome,terminal
def bracket(v,ds):
 def g(c):
  p=F(1)
  for d in ds:p*=1-c*d/v
  return 1-c-p
 lo=F(1,2);hi=F(1)
 ck(g(lo)>0 and g(hi)<0)
 for _ in range(32):
  mid=(lo+hi)/2
  if g(mid)>0:lo=mid
  else:hi=mid
 ck(g(lo)>0 and g(hi)<0)
 return lo,hi
def ref(c,p,ds):
 v=1-p.get(0,F(0));theta=[c*d/v for d in ds];q={}
 for s in range(1<<len(ds)):
  w=F(1)
  for j,a in enumerate(theta):w*=a if s>>j&1 else 1-a
  q[s]=p.get(0,F(0)) if not s else v*w/c
 norm=sum(q.values());return {s:w/norm for s,w in q.items()},norm
def run(m,r):
 t=table(m,r);coords=tuple(range(3+m*r));p,inf=E.spec(t,coords)
 delta=F(1,1<<r);tau=(1-(1-2*delta)**m)/2
 ck(inf[0]==inf[1]==F(1,2) and inf[2]==tau/2)
 ck(all(inf[j]==delta/2 for j in range(3,len(coords))))
 ck(p[0]==(1-tau)**2/4)
 ans=[]
 for c in bracket(1-p[0],list(inf.values())):
  q,norm=ref(c,p,list(inf.values()));kids,co,Q,eb,ob,tb=step(t,coords,q,2)
  grand,cog,Qg,ez,oz,tz=step(kids[1],co,Q[1],3)
  leaves=[kids[0],*grand];cs=[co,cog,cog];qs=[Q[0],*Qg];weights=[F(1,2),F(1,4),F(1,4)]
  Hf={};If=F(0);KLf={}
  for z,cc,qq,w in zip(leaves,cs,qs,weights):
   pp,ii=E.spec(z,cc);hh=entropy(pp);ii=sum(ii.values())
   Hf=E.add(Hf,E.scale(hh,w));If+=w*ii;KLf=E.add(KLf,E.scale(E.kl(pp,qq),w))
   ge(E.add(hh,{2:F(-2)}));ge(E.add({2:4*ii-2},E.scale(hh,-1)))
  # The active core query has two nonconstant data children.
  for bit in (0,1):
   core=tuple(__import__('functools').reduce(lambda a,b:a*b,(1-2*(((z>>(r*j))&((1<<r)-1))==((1<<r)-1)) for j in range(m)),1) for z in range(1<<(m*r)))
   ck(len(set(E.restrict(core,0,bit)))==2)
  H0=entropy(p);A=E.kl(p,q);CE=ce(p,q);D=E.add(H0,E.scale(Hf,-1));rem=sum(inf.values())-If
  ck(rem==tau/2+delta/2)
  S=E.add({2:4*If},E.scale(Hf,-1));edge=E.add(D,{2:-4*rem})
  # Full source partition verified numerically in addition to atom products.
  ledger=E.add(eb,ob,E.scale(ez,F(1,2)),E.scale(oz,F(1,2)),KLf)
  diff=E.bounds(E.add(A,E.scale(ledger,-1)))
  ck(diff[0]<=0<=diff[1] and diff[1]-diff[0]<F(1,1<<80))
  ge(E.add(S,{2:F(-2)}))
  ge(E.add({2:4*sum(inf.values())},E.scale(CE,-1)))
  # Complete source plus positive edge; preserve negative-edge sign.
  edgepos=edge if E.bounds(edge)[0]>0 else {}
  ck(E.bounds(edge)[1]<0 or E.bounds(edge)[0]>0 or not edge)
  liability=E.add(A,edgepos)
  ge(E.add(S,E.scale(liability,-1)))
  row={'m':m,'r':r,'dimension':len(coords),'c_endpoint':str(c),'normalizer':str(norm),'canonical_endpoint_only':True,'source_KL':E.serial(A),'root_CE':E.serial(CE),'signed_query_deficit':E.serial(edge),'removed_I':str(rem),'terminal_H':E.serial(Hf),'terminal_I':str(If),'terminal_surplus':E.serial(S),'full_liability':E.serial(liability),'remaining_surplus_interval':list(map(str,E.bounds(E.add(S,E.scale(liability,-1))))),'both_core_children_nonconstant':True}
  ans.append(row);save(f'case_m{m}_r{r}_{len(ans)}.json',row)
 return ans
fixtures=[(2,2)] if '--pilot' in sys.argv else [(2,2),(2,3),(2,4),(3,2)]
rows=[]
for m,r in fixtures:rows+=run(m,r)
# Finite rational boundary checks for analytic all-r statement.
ck(F(8*9*21,2**10)<F(3,2))
for r in range(8,33):
 bound=F(r*(r+1)*(2*r+5),1<<(r+2))
 nxt=F((r+1)*(r+2)*(2*r+7),1<<(r+3))
 ck(nxt<bound<F(3,2))
result={'status':'PASS','cases':len(rows),'assertions':CHECKS,'primitive_assertions':E.COUNT,'runtime_seconds':time.perf_counter()-START,'max_dimension':max(x['dimension'] for x in rows),'arithmetic':'Fraction and exact atom likelihood products; 256-bit outward rational log intervals','all_dimension_scope':'Analytic proof only, r>=8 and2<=m<=r; finite exact fixtures do not prove it'}
save('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json',result);print(json.dumps(result))
