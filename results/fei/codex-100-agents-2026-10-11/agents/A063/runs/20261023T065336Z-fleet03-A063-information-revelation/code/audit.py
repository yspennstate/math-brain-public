from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def scale(c,a):return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def total(v):
 a=(F(0),F(0))
 for b in v:a=add(a,b)
 return a
def mean(v):return scale(F(1,2),total(v))
def meet(a,b):ck(a[0]<=b[1] and b[0]<=a[1])
def ln(x):
 z=(x-1)/(x+1);v=2*sum((z**(2*k+1)/F(2*k+1) for k in range(40)),F(0));e=2*abs(z)**81/(81*(1-z*z));return v-e,v+e
LN2=ln(F(2))
@lru_cache(None)
def log(x):
 k=0;ck(x>0)
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 a=ln(x);return k+a[0]/LN2[1],k+a[1]/LN2[0]
def H(p):return total(scale(-x,log(x)) for x in p if x)
def KL(p,q):return total(scale(x,log(x/y)) for x,y in zip(p,q) if x)
def law(t):
 N=len(t);p=[F(sum(value*(-1 if (s&z).bit_count()%2 else 1) for z,value in enumerate(t))**2,N*N) for s in range(N)];ck(sum(p)==1);return p
def influences(t):
 return [F(sum(t[z]!=t[z^(1<<j)] for z in range(len(t))),len(t)) for j in range(len(t).bit_length()-1)]
def marg(p):return [sum((v for s,v in enumerate(p) if s>>j&1),F(0)) for j in range(len(p).bit_length()-1)]
def prod(d):
 q=[]
 for s in range(1<<len(d)):
  a=F(1)
  for j,x in enumerate(d):a*=x if s>>j&1 else 1-x
  q.append(a)
 return q
def hb(d):return H([d,1-d])
out=[]
for n in [4,6]:
 N=1<<n;r=n//2;U=sum(1<<(2*j) for j in range(r));V=sum(1<<(2*j+1) for j in range(r))
 dense=[(-1)**sum(((z>>(2*j))&1)*((z>>(2*j+1))&1) for j in range(r)) for z in range(N)]
 sparse=[(-1)**(((z&U).bit_count()%2)*((z&V).bit_count()%2)) for z in range(N)]
 tab=[dense[z>>1] if not(z&1) else sparse[z>>1] for z in range(2*N)]
 ps=[law(dense),law(sparse)];p=law(tab);d=influences(tab)
 ck(d==marg(p));ck(all(influences(t)==[F(1,2)]*n for t in [dense,sparse]))
 ck(ps[0]==[F(1,N)]*N);ck(ps[1]==[F(1,4) if s in [0,U,V,U|V] else F(0) for s in range(N)])
 q=prod(d);er=[p[2*s]+p[2*s+1] for s in range(N)];qr=[q[2*s]+q[2*s+1] for s in range(N)]
 ck(qr==[F(1,N)]*N);ck(er==[(x+y)/2 for x,y in zip(*ps)])
 ker=[[p1[s]/(2*er[s]) for s in range(N)] for p1 in ps]
 pi=[sum((x*y for x,y in zip(qr,k)),F(0)) for k in ker];ck(pi==[F(N,N+4),F(4,N+4)])
 pred=[[x*y/z for x,y in zip(qr,k)] for k,z in zip(ker,pi)]
 O=KL([F(1,2)]*2,pi);J=sub(H(er),mean([H(p1) for p1 in ps]));B=sub(H(p),H(er));E=sub(KL(p,q),KL(er,qr))
 fresh=[KL(p1,[F(1,N)]*N) for p1 in ps];old=[KL(p1,q1) for p1,q1 in zip(ps,pred)]
 sigma=sub(mean(fresh),mean(old));meet(sigma,add(J,O));meet(E,sub(hb(d[0]),B));meet(KL(p,q),add(E,add(O,mean(old))))
 meet(O,scale(F(1,2),log(F((N+4)**2,16*N))))
 ck(J[1]<1);ck(O[0]>F(n-4,2));ck(sigma[0]>F(n-4,2))
 if n==6:ck(sigma[0]>1)
 out.append({'n':n,'reference_outcomes':[str(x) for x in pi],'J':[str(x) for x in J],'O':[str(x) for x in O],'signed_actual_reset':[str(x) for x in sigma],'physical_influences':[str(x) for x in d]})
ck(time.perf_counter()-start<60)
result={'status':'PASS','assertions':checks,'cases':out,'seconds':time.perf_counter()-start,'method':'independent direct character sums plus physical edge counts, exact coherent normalization and rational atanh log bounds','scope':'finite independent reconstruction; all-even-n proof in PROOF_OBSTRUCTION.md; independent agent review pending'}
(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
