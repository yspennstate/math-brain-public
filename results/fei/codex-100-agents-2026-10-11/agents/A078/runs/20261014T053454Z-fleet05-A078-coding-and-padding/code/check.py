from pathlib import Path
from fractions import Fraction as F
import json,time,sys,itertools
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();count=0
def ck(x):
 global count
 count+=1
 assert x
 assert time.perf_counter()-start<55,'frozen time guard'
def rank(vs):
 p={}
 for v in vs:
  while v:
   k=v.bit_length()
   if k in p:v^=p[k]
   else:p[k]=v;break
 return len(p)
def basis(cost,n):
 b=[]
 for v in sorted(range(1,1<<n),key=lambda v:(cost[v],v)):
  if rank(b+[v])>len(b):b.append(v)
  if len(b)==n:break
 return sum((cost[v] for v in b),F(0)),b
def walsh(t):
 a=list(t);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
  h*=2
 return a
def dirs(t):return [F(sum(t[y]!=t[y^v] for y in range(len(t))),len(t)) for v in range(len(t))]
def act(g,r):return [g[y%len(g)] if y//len(g)==0 else 1 for y in range(len(g)*(1<<r))]
def family(k):
 def h(s):return -1 if sum(((s>>(2*j))&3)==3 for j in range(k//2))%2 else 1
 return [h(y&((1<<k)-1)) if y>>(k+1) else (-1 if y&((1<<(k+1))-1)==0 else 1) for y in range(1<<(k+2))]
def code(g,cols,mod=0):
 t=[]
 for x in range(1<<len(cols)):
  y=0
  for j,v in enumerate(cols):
   if x>>j&1:y^=v
  t.append(g[y]*(-1 if (x&mod).bit_count()%2 else 1))
 return t
def codecheck(g,cols,mod=0):
 t=code(g,cols,mod);n=len(cols);m=len(g).bit_length()-1
 ck(rank(cols)==m)
 ck(sorted(F(w*w,len(t)**2) for w in walsh(t) if w)==sorted(F(w*w,len(g)**2) for w in walsh(g) if w))
 q=dirs(g)
 ck(sum((F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(n)),F(0))==sum((1-q[v] if mod>>j&1 else q[v] for j,v in enumerate(cols)),F(0)))
 return t
def activationcheck(g,r):
 m=len(g).bit_length()-1;mu=F(sum(g),len(g));c=1-mu;p=F(1,1<<r)
 q=dirs(g);t=act(g,r);qt=dirs(t)
 for v,d in enumerate(qt):ck(d==(p*q[v] if v<len(g) else p*c));ck(d<=F(1,2))
 seed,b=basis([min(d,c) for d in q],m)
 opt,bb=basis(qt,m+r);ck(opt==p*(seed+r*c))
 cols=[v if q[v]<=c else v^len(g) for v in b]+[len(g)<<j for j in range(r)]
 coded=codecheck(t,cols);ck(sum((qt[v] for v in cols),F(0))==opt)
 # A redundant auxiliary and nonzero output modulation are fully charged.
 if m+r<=5:codecheck(t,cols+[cols[0]],(1<<len(cols))|1)
 return {'m':m,'r':r,'mean':str(mu),'T':str(seed),'M':str(opt),'basis':bb}
def main():
 pilot='--pilot' in sys.argv;records=[];small=0
 for m in ([1,2] if pilot else [1,2,3]):
  for mask in range(1<<(1<<m)):
   g=[-1 if mask>>y&1 else 1 for y in range(1<<m)]
   if sum(g)<0:continue
   for r in ([1,2] if m<3 else [1]):
    records.append(activationcheck(g,r));small+=1
 for r in [1,2,3]:
  t=act([1,-1],r);opt,_=basis(dirs(t),r+1);ck(opt==F(r+1,1<<r))
 bent=[]
 for k in ([2] if pilot else [2,4,6]):
  a=F(1,1<<k);b=F(1,1<<(k//2));D=F(1,4)+a/2;cm=(1-b-a)/2;cp=(1-b+a)/2;M=a/2+k*D+cm
  g=family(k);q=dirs(g)
  for v,cost in enumerate(q):
   s=v&((1<<k)-1);e=v>>k&1;z=v>>(k+1)
   odd=sum(((s>>(2*j))&3)==3 for j in range(k//2))%2
   want=(cm if odd else cp) if z else (D if s else (a/2 if e else F(0)))
   ck(cost==want)
  opt,bb=basis(q,k+2);ck(opt==M)
  cols=[1<<j for j in range(k+2)];cols[-1]^=3
  codecheck(g,cols);ck(sum((q[v] for v in cols),F(0))==M)
  ck(sum((q[1<<j] for j in range(k+2)),F(0))==M+a)
  for r in [1,2]:
   rec=activationcheck(g,r);ck(F(rec['M'])==F(1,1<<r)*(M+r*cp))
  bent.append({'k':k,'M':str(M),'I':str(M+a),'basis':bb})
 compressed=[]
 for k in [2,4,6,8,16,32,64]:
  a=F(1,1<<k);b=F(1,1<<(k//2));D=F(1,4)+a/2;cm=(1-b-a)/2;cp=(1-b+a)/2;M=a/2+k*D+cm
  if k>=4:ck(a/2<D<cm<cp);ck(F(k,2)-2*b-2*a>0)
  else:ck(M==1);ck(cm==a/2);ck(D==cp)
  for r in [1,2,4,k]:
   p=F(1,1<<r);ck(p*(M+a+r*cp)-p*(M+r*cp)==p*a)
   compressed.append({'k':k,'r':r,'M':str(p*(M+r*cp)),'I':str(p*(M+a+r*cp)),'saving':str(p*a)})
 out={'status':'PASS','helper':'A078-activation-code-direction-v1','mode':'pilot' if pilot else 'full','assertions':count,'small_core_control_cases':small,'bent_roots':bent,'compressed':compressed,'records':records,'seconds':time.perf_counter()-start,'peak_memory':'unmeasured;estimate120MB'}
 (ROOT/'out'/('pilot.json' if pilot else 'full.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k not in ['records','compressed','bent_roots']}))
if __name__=='__main__':main()
