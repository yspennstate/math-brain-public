from pathlib import Path
from fractions import Fraction as R
from itertools import product
import json,time,math
RUN=Path(__file__).resolve().parents[1]
(RUN/'out').mkdir(exist_ok=True)
start=time.monotonic()
base=[R(8,13),R(2,13)]+[R(1,26)]*6
# The y0 singleton is index 1, hence the preceding frequency order is canonical.
def fw(a):
 a=list(a);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h):
    x,y=a[i],a[i+h];a[i],a[i+h]=x+y,x-y
  h*=2
 return a
def core(c,u,y):
 s=[1 if (y>>i)&1 else -1 for i in range(3)]
 maj=1 if sum(s)>0 else -1
 return [maj,s[0],-s[0],-maj][c+2*u]
def data(pat,m):
 free=[i for i,v in enumerate(pat) if v==2]
 tab=[]
 for x in range(1<<(m+2+len(free))):
  c=x&1;u=(x>>1)&1;z=(x>>2)&((1<<m)-1)
  y=sum((pat[i] if pat[i]!=2 else ((x>>(m+2+free.index(i)))&1))<<i for i in range(3))
  tab.append(core(c,u,y)*(-1 if c==0 and z==0 else 1))
 N=len(tab);P=[R(v*v,N*N) for v in fw(tab)]
 dmask=(1<<(m+2))-1
 ry=[R(0)]*(1<<len(free))
 for s,r in enumerate(base):
  t=sum(((s>>i)&1)<<j for j,i in enumerate(free));ry[t]+=r
 alpha=sum(p for s,p in enumerate(P) if s&dmask)
 inf=[sum(p for s,p in enumerate(P) if (s>>i)&1) for i in range(m+2+len(free))]
 B=sum(float(p)*math.log2(1/float(ry[s>>(m+2)])) for s,p in enumerate(P) if p)
 h=lambda a: -sum(float(q)*math.log2(float(q)) for q in [a,1-a] if q)
 rho=R(1,1<<m);beta=2*rho*(1-rho)
 C=B+h(alpha)+2*float(sum(inf[:2]))+float(beta)*math.log2(float((1-rho)/rho*R(20,7)))
 return {'C':C,'I':sum(inf),'inf':inf,'B':B,'alpha':alpha,'free':free}
rows=[]
for m in (1,2,3):
 for pat in product(range(3),repeat=3):
  p=data(pat,m)
  for j,i in enumerate(p['free']):
   children=[]
   for b in (0,1):
    ch=list(pat);ch[i]=b;children.append(data(tuple(ch),m))
   delta=p['C']-sum(c['C'] for c in children)/2
   assert p['I']==p['inf'][m+2+j]+sum(c['I'] for c in children)/2
   rows.append({'m':m,'pattern':pat,'query':i,'influence':str(p['inf'][m+2+j]),'delta':delta,'K4_price':4*float(p['inf'][m+2+j])-delta,'K4_parent':4*float(p['I'])-p['C'],'K4_children':[4*float(c['I'])-c['C'] for c in children],'K56_price':5.6*float(p['inf'][m+2+j])-delta})
   assert time.monotonic()-start<55
assert len(rows)==81
out={'status':'NUMERICAL_DISCOVERY_ONLY','rows':rows,'elapsed_seconds':time.monotonic()-start}
(RUN/'out/PILOT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'cases':len(rows),'elapsed':out['elapsed_seconds'],'negative_K4':sum(r['K4_price']<0 for r in rows),'min_parent':min(r['K4_parent'] for r in rows),'min_child':min(min(r['K4_children']) for r in rows),'worst':min(rows,key=lambda r:r['K4_price'])}))
