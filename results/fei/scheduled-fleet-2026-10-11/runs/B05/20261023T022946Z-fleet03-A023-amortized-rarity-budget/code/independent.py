"""No production imports: direct character sums instead of FWHT."""
from pathlib import Path
from fractions import Fraction as F
import json,time
RUN=Path(__file__).resolve().parents[1];START=time.perf_counter();COUNT=0
def ck(ok):
 global COUNT
 assert ok
 COUNT+=1
 assert time.perf_counter()-START<60
def logarithm(v,x,c):
 x=F(x)
 if not c:return
 for num,sgn in [(x.numerator,1),(x.denominator,-1)]:
  div=2
  while div*div<=num:
   while num%div==0:
    v[div]=v.get(div,F(0))+sgn*c;num//=div
   div+=1
  if num>1:v[num]=v.get(num,F(0))+sgn*c
 for p in list(v):
  if not v[p]:del v[p]
def combo(*parts):
 z={}
 for a,v in parts:
  for p,c in v.items():z[p]=z.get(p,F(0))+a*c
 return {p:c for p,c in z.items() if c}
def spectrum(t):
 N=len(t);ret={}
 for s in range(N):
  a=sum((-b if (s&x).bit_count()%2 else b) for x,b in enumerate(t))
  if a:ret[s]=F(a*a,N*N)
 ck(sum(ret.values())==1);return ret
def entropy(p):
 v={}
 for a in p.values():logarithm(v,a,-a)
 return v
def cross(p,q):
 v={}
 for s,a in p.items():logarithm(v,q[s],-a)
 return v
def edge(t,i):return F(sum(a!=t[x^(1<<i)] for x,a in enumerate(t)),len(t))
def scatter(x,indices,fixed):
 y=sum(v*(1<<i) for i,v in fixed.items())
 for j,i in enumerate(indices):y+=((x>>j)&1)*(1<<i)
 return y
def b(x,m):
 r=1
 for i in range(0,m,2):
  if x&(1<<i) and x&(1<<(i+1)):r=-r
 return r
rows=json.loads((RUN/'out/rows.json').read_text(encoding='utf-8'))
lookup={(r['m'],r['w'],tuple(sorted((int(i),v) for i,v in r['fixed'].items()))):r for r in rows}
cases=[(4,w,fix) for w in [1,3] for fix in [{},{0:0},{5:1},{0:1,5:1,6:0}]]
cases +=[(8,1,dict.fromkeys(range(j),0)|{j:1}) for j in range(8)]+[(8,1,dict.fromkeys(range(8),0))]
checks=[];frontier={}
for m,w,fix in cases:
 data=[i for i in range(m) if i not in fix];ctrl=[i for i in [m+1,m+2] if i not in fix];indices=data+[m]+ctrl
 t=[]
 for x in range(1<<len(indices)):
  y=scatter(x,indices,fix);c=y% (1<<m);A=(y>>(m+1))&1;B=(y>>(m+2))&1
  f=b(c,m)*(-1 if y&(1<<m) else 1)
  if A and ((not B and c==0) or (B and c==w)):f=-f
  t.append(f)
 p=spectrum(t);H=entropy(p)
 corefix={i:v for i,v in fix.items() if i<m};seed=[b(scatter(x,data,corefix),m) for x in range(1<<len(data))];ps=spectrum(seed)
 q={s:(ps.get(s,F(0))+F(1,len(seed)))/2 for s in range(len(seed))};nu={s:F(0) for s in range(1<<len(ctrl))};delta=F(1,1<<m)
 for mask,a in enumerate([1-3*delta/2]+[delta/2]*3):
  s=sum(((mask>>(i-m-1))&1)*(1<<j) for j,i in enumerate(ctrl));nu[s]+=a
 py={s:F(0) for s in nu};ref={}
 for mask,a in p.items():
  ds=mask%len(seed);cs=mask>>(len(data)+1);py[cs]+=a;ref[mask]=q[ds]*nu[cs]
 C=cross(p,ref);CY=cross(py,nu);K=combo((1,C),(-1,H))
 ii=[edge(t,j) for j in range(len(indices))];ID=sum(ii[:len(data)+1]);IC=sum(ii[len(data)+1:])
 pi=[F(0)]*3
 for x in range(1<<len(ctrl)):
  y=scatter(x,ctrl,{i:v for i,v in fix.items() if i>m});A=(y>>(m+1))&1;B=(y>>(m+2))&1;pi[0 if A==0 else 1+B]+=F(1,1<<len(ctrl))
 cores=[]
 for j in range(3):cores.append([v*(-1 if j and scatter(x,data,corefix)==(0 if j==1 else w) else 1) for x,v in enumerate(seed)])
 R=F(0)
 for j in range(3):
  for k in range(j):
   prod=[a*b for a,b in zip(cores[j],cores[k])];R+=2*pi[j]*pi[k]*sum(edge(prod,i) for i in range(len(data)))
 B=combo((1,{2:4*ID-F(m,8)-R}),(-1,C));key=(m,w,tuple(sorted(fix.items())));row=lookup[key]
 for n,val in [('H',H),('C',C),('CY',CY),('K',K),('B',B)]:ck(val=={int(k):F(v) for k,v in row[n].items()})
 for n,val in [('ID',ID),('IC',IC),('R',R)]:ck(val==F(row[n]))
 ck(pi==list(map(F,row['pi'])))
 if m==8:
  reach=F(1,1<<(max(fix)+1));frontier=combo((1,frontier),(reach,B))
  if all(x==0 for x in fix.values()):
   ck(ID==1 and R==0 and H=={2:F(2)})
   formula={};logarithm(formula,1-3*delta/2,F(1,4));formula=combo((1,formula),(1,{2:4-F(m,8)-F(3*(m+1),4)}));ck(B==formula)
 checks.append({'m':m,'w':w,'fixed':fix})
deep=json.loads((RUN/'out/deep_frontier.json').read_text(encoding='utf-8'));ck(frontier=={int(k):F(v) for k,v in deep['expected_B'].items()})
result={'status':'PASS','cases':len(cases),'checks':COUNT,'elapsed_seconds':time.perf_counter()-START,'scope':'Independent representation/code reconstruction by same author; independent-person mathematical review still pending.'}
(RUN/'out/independent_rows.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
(RUN/'out/independent_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
