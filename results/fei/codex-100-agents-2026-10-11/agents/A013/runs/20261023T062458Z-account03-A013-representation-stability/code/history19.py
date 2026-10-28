from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,time
R=Path(__file__).resolve().parents[1]
SRC=Path('agents/A012/runs/20261023T053904Z-account03-A012-sparse-activation-accounting')
start=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v,checks
 checks+=1
 ck_time=time.perf_counter()-start
 assert ck_time<50,ck_time
def fw(v):
 a=list(v);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def spec(v):return [F(x*x,len(v)**2) for x in fw(v)]
def influence(v):
 n=(len(v)-1).bit_length()
 return F(sum(v[x]!=v[x^(1<<i)] for i in range(n) for x in range(len(v))),len(v))
@lru_cache(None)
def ln(q):
 q=F(q);k=0
 while q<1:q*=2;k-=1
 while q>2:q/=2;k+=1
 def series(x):
  u=(x-1)/(x+1);n=28
  lo=sum((2*u**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
  return lo,lo+2*u**(2*n+1)/F(2*n+1)/(1-u*u)
 l,h=series(q);l2,h2=series(F(2))
 return l+k*(l2 if k>=0 else h2),h+k*(h2 if k>=0 else l2)
def ce(p,q):
 lo=hi=F(0)
 for x,y in zip(p,q):
  if x:
   ck(y>0);l,h=ln(1/y);lo+=x*l;hi+=x*h
 return lo,hi
def margin(i,c):
 l,h=ln(F(2));return 4*i*l+2*i-c[1]-F(5,4),4*i*h+2*i-c[0]-F(5,4)
def avg(v):return (sum(x[0] for x in v)/len(v),sum(x[1] for x in v)/len(v))
def encode(obj):
 if isinstance(obj,F):return str(obj)
 if isinstance(obj,dict):return {str(k):encode(v) for k,v in obj.items()}
 if isinstance(obj,(list,tuple)):return [encode(x) for x in obj]
 return obj
target=json.loads((SRC/'out/NEXT_TARGET.json').read_text(encoding='utf-8'))
truth=target['F'];q=list(map(F,target['root_Q']));p=spec(truth)
ck(sum(q)==1);ck(sum(p)==1);ck(influence(truth)==F(7,8))
states={}
for state in product((-1,0,1),repeat=3):
 fixed={j:a for j,a in enumerate(state) if a!=-1};free=[j for j in range(6) if j not in fixed]
 def inject(x):return sum(a<<j for j,a in fixed.items())+sum(((x>>k)&1)<<j for k,j in enumerate(free))
 child=[truth[inject(x)] for x in range(1<<len(free))]
 qp=[sum(q[t] for t in range(64) if all(((t>>j)&1)==((x>>k)&1) for k,j in enumerate(free))) for x in range(1<<len(free))]
 pc=spec(child);ic=influence(child);cc=ce(pc,qp)
 ck(sum(qp)==1);ck(sum(pc)==1)
 # Independently verify amplitudes by physical character sums, no FWHT.
 direct=[F(sum(child[x]*(1-2*((x&t).bit_count()%2)) for x in range(len(child))),len(child)) for t in range(len(child))]
 ck([x*x for x in direct]==pc)
 states[state]={'I':ic,'CE':cc,'margin':margin(ic,cc),'Q':qp,'P':pc,'truth':child}
root=(-1,-1,-1);rootce=states[root]['CE'];rootmargin=states[root]['margin']
# ALL policies; each is a rational weighted terminal expected I and CE interval.
@lru_cache(None)
def policies(state):
 s=states[state];out=[(s['I'],s['CE'],('stop',))]
 for j,a in enumerate(state):
  if a!=-1:continue
  daughters=[]
  for bit in (0,1):
   v=list(state);v[j]=bit;daughters.append(tuple(v))
  for u in policies(daughters[0]):
   for v in policies(daughters[1]):
    out.append(((u[0]+v[0])/2,avg([u[1],v[1]]),(j,u[2],v[2])))
 return out
pol=policies(root);ck(len(pol)==244)
records=[]
for i,c,tree in pol:
 m=margin(i,c);records.append({'I':i,'CE_ln':c,'margin_ln':m,'tree':tree})
ck(all(x['margin_ln'][0]>0 or x['margin_ln'][1]<0 for x in records))
positive=sum(x['margin_ln'][0]>0 for x in records)
one=[]
for j in range(3):
 ss=[]
 for b in (0,1):
  v=list(root);v[j]=b;ss.append(states[tuple(v)])
 i=sum(x['I'] for x in ss)/2;c=avg([x['CE'] for x in ss]);m=margin(i,c)
 # Signed consumption of the exact original reserve, preserving old debit.
 consumed=(rootmargin[0]-m[1],rootmargin[1]-m[0])
 one.append({'query':j,'remaining_I':i,'CE_ln':c,'margin_ln':m,'consumed_original_ln':consumed,'daughter_margins_ln':[x['margin'] for x in ss]})
out={'status':'PASS','assertions':checks,'states':27,'policies':244,'positive_policies':positive,'negative_policies':244-positive,'root_margin_ln':rootmargin,'one_query':one,'worst_policy':min(records,key=lambda x:x['margin_ln'][0]),'best_policy':max(records,key=lambda x:x['margin_ln'][0]),'policies_detail':records,'states_detail':{str(k):v for k,v in states.items()},'seconds':time.perf_counter()-start}
(R/'out/HISTORY.json').write_text(json.dumps(encode(out),indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','assertions':checks,'positive':positive,'negative':244-positive,'one_query_approx':[{'j':x['query'],'margin_ln':float(x['margin_ln'][0]),'consumption_ln':float(x['consumed_original_ln'][0]),'daughter_margins_ln':[float(y[0]) for y in x['daughter_margins_ln']]} for x in one],'root_margin_ln':float(rootmargin[0]),'worst':float(out['worst_policy']['margin_ln'][0]),'seconds':out['seconds']}))
