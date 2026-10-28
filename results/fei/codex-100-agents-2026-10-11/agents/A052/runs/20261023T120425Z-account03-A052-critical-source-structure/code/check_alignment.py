from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util,json,sys,time,hashlib
R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261023T014825Z-account03-A052-critical-source-structure/code/check_rank_pair.py'
sp=importlib.util.spec_from_file_location('arith',OLD);h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
PR=(2,3,5,7);S=1<<80;COUNT=0;START=time.perf_counter()
def ck(t):
 global COUNT
 COUNT+=1
 if not t:raise AssertionError(COUNT)
def budget():
 if time.perf_counter()-START>53:raise TimeoutError('frozen 53s')
def logs():
 out=[]
 for p in PR:
  lo,hi=h.interval({p:F(1)});out.append((lo.numerator*S//lo.denominator,-(-hi.numerator*S//hi.denominator)))
 return out
LOGS=logs()
def cmp(a,b):
 d=tuple(x-y for x,y in zip(a,b))
 if not any(d):return 0
 lo=sum(x*(LOGS[j][0] if x>=0 else LOGS[j][1]) for j,x in enumerate(d));hi=sum(x*(LOGS[j][1] if x>=0 else LOGS[j][0]) for j,x in enumerate(d))
 if lo>0:return 1
 if hi<0:return -1
 raise ArithmeticError('80bit exact interval undecided')
def walsh(f):
 out=list(f);s=1
 while s<len(out):
  for i in range(0,len(out),2*s):
   for j in range(i,i+s):a,b=out[j],out[j+s];out[j],out[j+s]=a+b,a-b
  s*=2
 return tuple(out)
@lru_cache(None)
def contribution(w):
 out=[]
 for p in PR:
  z=abs(w);v=0
  while z and z%p==0:v+=1;z//=p
  out.append(-2*w*w*v)
 return tuple(out)
def rawprofile(f):
 N=len(f);n=N.bit_length()-1;W=walsh(f);H=[2*n*N*N,0,0,0]
 for w in W:
  for j,c in enumerate(contribution(w)):H[j]+=c
 J=sum(s.bit_count()*w*w for s,w in enumerate(W))
 return tuple(H),J,W
def table(n,t):return tuple(1-2*(t>>x&1) for x in range(1<<n))
@lru_cache(None)
def smallprofile(n,t):return rawprofile(table(n,t))
def profile(f):
 n=len(f).bit_length()-1
 return smallprofile(n,sum((v<0)<<x for x,v in enumerate(f))) if n<=3 else rawprofile(f)
def deficit(p,K):return (p[0][0]-K*p[1],)+p[0][1:]
def phase_class(n,t):
 a=[t>>x&1 for x in range(1<<n)]
 for j in range(n):
  for x in range(1<<n):
   if x>>j&1:a[x]^=a[x^(1<<j)]
 return sum(a[x]<<z for z,x in enumerate(x for x in range(1<<n) if x.bit_count()>=3))
def children(f,i):
 return [tuple(f[(x&((1<<i)-1))|((x>>i)<<(i+1))|(u<<i)] for x in range(len(f)//2)) for u in [0,1]]
def glue(g,hv,i,sgn):
 N=2*len(g);out=[]
 for x in range(N):
  z=(x&((1<<i)-1))|((x>>(i+1))<<i)
  out.append(g[z] if not x>>i&1 else sgn*hv[z])
 return tuple(out)
def alignment(f,i,v,sgn,K,critical=False):
 p=profile(f);g,hh=children(f,i);M=len(g);N=len(f);pg=profile(g);ph=profile(hh)
 hv=tuple(a*(-1 if (x&v).bit_count()%2 else 1) for x,a in enumerate(hh));ff=glue(g,hv,i,sgn);pn=profile(ff)
 expected=[]
 for T in range(M):
  a,b=pg[2][T],sgn*ph[2][T^v]
  expected.extend([a+b,a-b])
 ck(sorted(expected)==sorted(pn[2]))
 # Exact coefficient identities, retaining original index labels.
 for T in range(M):
  z=(T&((1<<i)-1))|((T>>i)<<(i+1))
  ck(pn[2][z]==pg[2][T]+sgn*ph[2][T^v]);ck(pn[2][z|(1<<i)]==pg[2][T]-sgn*ph[2][T^v])
 c0=F(sum(a*b for a,b in zip(g,hh)),M);cv=F(sum(g[x]*hh[x]*(-1 if (x&v).bit_count()%2 else 1) for x in range(M)),M)
 di=sum(F(1)-F(2*sum(hh[x]!=hh[x^(1<<j)] for x in range(M)),M) for j in range(M.bit_length()-1) if v>>j&1)
 ck(F(pn[1]-p[1],N*N)==(di+c0-sgn*cv)/2)
 ck(F(ph[1],M*M)+di==F(profile(hv)[1],M*M))
 expectedH=[2*(N.bit_length()-1)*N*N,0,0,0]
 for w in expected:
  for j,c in enumerate(contribution(w)):expectedH[j]+=c
 ck(tuple(expectedH)==pn[0])
 if critical:
  ck(c0>=0);ck(cmp(deficit(pn,K),deficit(p,K))<=0)
 return ff,pn
def main():
 pilot='--pilot' in sys.argv;maxn=3 if pilot else 4;rates=[1,2,3];census=[];selected={};positives=[];phase_best={}
 for n in range(1,maxn+1):
  best={K:((0,0,0,0),[]) for K in rates}
  for t in range(1<<(1<<n)):
   f=table(n,t);p=profile(f)
   for K in rates:
    d=deficit(p,K);c=cmp(d,best[K][0])
    if c>0:best[K]=(d,[t])
    elif c==0:best[K][1].append(t)
   if n==4 and cmp(deficit(p,3),(0,0,0,0))>0:positives.append(t)
   if n==maxn:
    c=phase_class(n,t);d=deficit(p,3)
    if c not in phase_best or cmp(d,phase_best[c][0])>0:phase_best[c]=(d,t)
   if t%2048==0:budget()
  for K in rates:
   d,ts=best[K];sgn=cmp(d,(0,0,0,0));ck(sgn>=0)
   census.append({'n':n,'K':K,'max_D_scaled_prime_log':list(d),'scale':(1<<n)**2,'max_count':len(ts),'first_table':ts[0],'positive':sgn>0})
   if sgn>0 and K not in selected:selected[K]=(n,ts[0],d)
 cases=0
 for n in range(1,3 if pilot else 4):
  for t in range(1<<(1<<n)):
   f=table(n,t)
   for i in range(n):
    for v in range(1<<(n-1)):
     for s in [-1,1]:alignment(f,i,v,s,2);cases+=1
   budget()
 critical=[]
 for K,(n,t,d) in selected.items():
  f=table(n,t);ncases=0
  for i in range(n):
   for v in range(1<<(n-1)):
    for s in [-1,1]:alignment(f,i,v,s,K,True);ncases+=1
  critical.append({'K':K,'n':n,'table':t,'D_scaled_prime_log':list(d),'competitors':ncases})
 phase_cases=0
 for c,(d,t) in phase_best.items():
  f=table(maxn,t)
  for i in range(maxn):
   for v in range(1<<(maxn-1)):
    for s in [-1,1]:
     ff,pn=alignment(f,i,v,s,3,True);ck(phase_class(maxn,sum((z<0)<<x for x,z in enumerate(ff)))==c);phase_cases+=1
  budget()
 # Search at most128 positive critical-dimension sources for a witness
 # that MINIMAL DIMENSION alone does not imply rematching stationarity.
 guard=None;searched=0
 for t in positives[:128]:
  searched+=1;f=table(4,t);p=profile(f)
  for i in range(4):
   for v in range(8):
    g,hh=children(f,i);cv=sum(g[x]*hh[x]*(-1 if (x&v).bit_count()%2 else 1) for x in range(8));sgn=1 if cv>=0 else -1
    ff,pn=alignment(f,i,v,sgn,3)
    if cmp(deficit(pn,3),deficit(p,3))>0:
     guard={'n':4,'K':3,'table':t,'i':i,'v':v,'cofactor_sign':sgn,'competitor_table':sum((z<0)<<x for x,z in enumerate(ff)),'old_D_scaled_prime_log':list(deficit(p,3)),'new_D_scaled_prime_log':list(deficit(pn,3)),'gain_scaled_prime_log':[a-b for a,b in zip(deficit(pn,3),deficit(p,3))]};break
   if guard:break
  if guard:break
  budget()
 if not pilot:ck(set(selected)=={1,2,3})
 out={'status':'PASS','pilot':pilot,'checks':COUNT,'census':census,'algebra_cases':cases,'critical_sources':critical,'quadratic_phase_classes':len(phase_best),'phase_optimal_competitors':phase_cases,'phase_class_representatives':[{'class':c,'n':maxn,'K':3,'table':t,'D_scaled_prime_log':list(d)} for c,(d,t) in phase_best.items()],'minimal_dimension_only_guard':guard,'guard_sources_searched':searched,'guard_exhaustive':False,'seconds':time.perf_counter()-START,'logs_denominator_bits':80,'log2_prime_intervals':{str(p):list(bounds) for p,bounds in zip(PR,LOGS)},'helper_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest()}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='');print(json.dumps({k:v for k,v in out.items() if k not in ['census','log2_prime_intervals','phase_class_representatives']}))
if __name__=='__main__':main()
