from fractions import Fraction as Q
from pathlib import Path
import json,time,sys,hashlib
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
 if checks%1000==0:assert time.perf_counter()-start<55
def transform(t):
 a=list(t);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return [Q(v,len(a)) for v in a]
def factors(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def plus(a,b,m=Q(1)):
 for p,v in b.items():
  a[p]=a.get(p,0)+m*v
  if not a[p]:del a[p]
 return a
def log(q):return plus({p:Q(v) for p,v in factors(q.numerator).items()},factors(q.denominator),Q(-1))
def cost(ps,qs):
 out={}
 for p,q in zip(ps,qs):
  if p:plus(out,log(q),-p)
 return out
def influence(t,s,n):
 return sum(Q(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(s,n))
def physical_case(s,word,L):
 g=[1 if (word>>z)&1 else -1 for z in range(1<<s)];gh=transform(g)
 false=[z for z in range(1<<s) if g[z]<0];idx={z:j for j,z in enumerate(false)}
 n=s+L*len(false);eps=Q(1,1<<L);q=Q(len(false),1<<s);f=[]
 for x in range(1<<n):
  z=x&((1<<s)-1)
  active=idx.get(z)
  direct=1 if active is None or ((x>>(s+L*active))&((1<<L)-1))==((1<<L)-1) else -1
  # Independent literal CNF: exactly the clause group with core point z can fail.
  cnf=all(z!=v or ((x>>(s+L*j+l))&1) for j,v in enumerate(false) for l in range(L))
  ck(direct==(1 if cnf else -1));f.append(direct)
 fh=transform(f);ck(sum(c*c for c in fh)==1)
 for S in range(1<<s):ck(fh[S]==(1-eps)*gh[S]+(eps if S==0 else 0))
 support_private=0
 for mask in range(1<<s,1<<n):
  S=mask&((1<<s)-1);T=mask>>s
  used=[j for j in range(len(false)) if (T>>(L*j))&((1<<L)-1)]
  if len(used)==1:
   j=used[0];sign=-1 if ((S&false[j]).bit_count()+T.bit_count())%2 else 1
   ck(fh[mask]==sign*Q(2,1<<s)*eps);support_private+=1
  else:ck(fh[mask]==0)
 M=4*q*eps*(1-eps)
 ck(support_private==len(false)*(1<<s)*((1<<L)-1))
 ck(sum(c*c for c in fh[(1<<s):])==M)
 Ig=influence(g,0,s);Icore=influence(f,0,s);Iprivate=influence(f,s,n)
 ck(Iprivate==2*q*L*eps)
 ck(Icore==(1-eps)**2*Ig+2*s*q*eps*(1-eps))
 ck(Icore+Iprivate==sum(mask.bit_count()*c*c for mask,c in enumerate(fh)))
 full_entropy=cost([c*c for c in fh],[c*c if c else Q(1) for c in fh])
 core_entropy=cost([c*c for c in fh[:1<<s]],[c*c if c else Q(1) for c in fh[:1<<s]])
 ck(full_entropy==plus(dict(core_entropy),{2:M*(2*s+2*L-2)}))
 pg=[c*c for c in gh[1:]];pc=[c*c for c in fh[1:1<<s]];vg=sum(pg)
 for style in [0,1]:
  weights=[1 if style==0 else A+1 for A in range(1,1<<n)];D=sum(weights)
  raw=[Q(weights[A-1],D) for A in range(1,1<<s)];Z=sum(raw);conditioned=[p/Z for p in raw]
  ck(0<Z<=1 and sum(conditioned)==1)
  lhs=cost(pg,conditioned)
  rhs={p:v/(1-eps)**2 for p,v in cost(pc,raw).items()};plus(rhs,log(Z),vg)
  ck(lhs==rhs)
  ck(Z==Q(sum(weights[:(1<<s)-1]),D))
 return n,1<<n
def main():
 pilot='--pilot' in sys.argv;cases=points=0;maxn=0
 for s in range(1,3 if pilot else 4):
  for word in range(1,(1<<(1<<s))-1):
   for L in ([1] if pilot or s==3 else [1,2]):
    n,pts=physical_case(s,word,L);cases+=1;points+=pts;maxn=max(maxn,n)
 for s in range(1,65):
  L=4*s+4;eps=Q(1,1<<L)
  ck(Q(2)*eps*(s+L)/(1-eps)**2<=Q(1,1<<(s-1)))
 ck(cases==(16 if pilot else 286));ck(maxn<=10);ck(time.perf_counter()-start<55)
 result={'PASS':True,'pilot':pilot,'physical_cases':cases,'physical_truth_points':points,'maximum_dimension':maxn,'assertions':checks,'elapsed_seconds':time.perf_counter()-start,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (RUN/'out').mkdir(exist_ok=True)
 (RUN/'out'/('pilot.json' if pilot else 'full.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result))
if __name__=='__main__':main()
