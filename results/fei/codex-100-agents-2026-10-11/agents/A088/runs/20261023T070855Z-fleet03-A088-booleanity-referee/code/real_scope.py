from fractions import Fraction as F
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1];START=time.perf_counter();N=0
def ck(v,s):
 global N
 N+=1
 if not v:raise AssertionError(s)
 if time.perf_counter()-START>55:raise TimeoutError(s)
def chars(v):return [sum((a*(-1)**((s&x).bit_count()) for x,a in enumerate(v)),F())/len(v) for s in range(len(v))]
def transform(v,labels):
 j,k=labels.index(4),labels.index(5)
 return [v[x]-sum((v[(x&~((1<<j)|(1<<k)))|(a<<j)|(b<<k)] for a in (0,1) for b in (0,1)),F())/2 for x in range(len(v))]
def cut(v,lab,i,b):
 j=lab.index(i)
 return [a for x,a in enumerate(v) if ((x>>j)&1)==b],[a for a in lab if a!=i]
def energy(v,j):return sum(((v[x]-v[x^(1<<j)])**2 for x in range(len(v))),F())/(4*len(v))
v=[F((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(3)))-2*((x&127)==0 and bool(x&128)) for x in range(256)]
labels=list(range(8));tv=transform(v,labels);paths=[[],[(7,0)],[(7,1)]];prefix=[(7,1)]
for a in (0,2):
 paths.extend([prefix+[(a,0)],prefix+[(a,1)],prefix+[(a,0),(a+1,0)],prefix+[(a,0),(a+1,1)]])
 prefix+= [(a,0),(a+1,0)]
rows=[]
for path in paths:
 p=v;q=tv;lab=labels
 for i,b in path:
  old=lab;p,lab=cut(p,old,i,b);q,_=cut(q,old,i,b)
 cp,cq=chars(p),chars(q)
 ck(q==transform(p,lab),'actual physical restriction commutes')
 ck([a*a for a in cp]==[b*b for b in cq],'all Fourier probabilities preserved')
 ck(sum(x*x for x in q)==len(q),'actual real restricted norm1')
 ck(any(x not in (-1,1) for x in q),'actual node is nonBoolean')
 for j in range(len(lab)):ck(energy(p,j)==energy(q,j),'every physical Dirichlet energy preserved')
 rows.append({'path':path,'value_set':sorted(set(map(str,q))),'norm_squared':'1'})
c=chars(tv);t=16;conv=sum((c[s]*c[s^t] for s in range(256)),F());ck(conv!=0,'nonempty phase-convolution violates Booleanity')
out={'status':'PASS','checks':N,'runtime_seconds':time.perf_counter()-START,'nodes':rows,'nonempty_convolution':{'shift':t,'value':str(conv)},'scope':'Prefixes avoiding third pair only; does not certify full-history real extension'}
(R/'out'/'REAL_SCOPE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':out['status'],'checks':N,'nodes':len(rows),'runtime_seconds':out['runtime_seconds'],'convolution':str(conv)}))
