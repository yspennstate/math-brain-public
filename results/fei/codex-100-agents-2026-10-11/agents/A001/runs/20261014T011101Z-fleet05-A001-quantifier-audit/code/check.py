from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import comb
import json,sys,time
RUN=Path(__file__).resolve().parents[1]
SPEC=json.loads((RUN/'out/FROZEN_SPEC.json').read_text())
checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
@lru_cache(None)
def factors(n):
 out={};d=2
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d=3 if d==2 else d+2
 if n>1:out[n]=out.get(n,0)+1
 return out
@lru_cache(None)
def lg(q):
 q=F(q);a=factors(q.numerator).copy()
 for p,k in factors(q.denominator).items():a[p]=a.get(p,0)-k
 return {p:F(k) for p,k in a.items() if k}
def plus(*terms):
 d={}
 for weight,term in terms:
  for p,c in term.items():d[p]=d.get(p,F(0))+weight*c
 return {p:c for p,c in d.items() if c}
def kl(a,b):
 return plus(*[(x,lg(x/y)) for x,y in zip(a,b) if x])
def walsh(a):
 a=a[:];d=1
 while d<len(a):
  for b in range(0,len(a),2*d):
   for j in range(b,b+d):
    u,v=a[j],a[j+d];a[j],a[j+d]=u+v,u-v
  d*=2
 return a
def analyze(values,L=None):
 N=len(values);n=N.bit_length()-1;w=walsh(values);p=[F(c*c,N*N) for c in w]
 ck(sum(p)==1);es=[];Ds=[];Ms=[];tails=[];coarses=[];joint=[]
 for i in range(n):
  bit=1<<i;lower=[s for s in range(N) if not s&bit]
  e=sum(p[s|bit] for s in lower)
  physical=F(sum(values[x]!=values[x^bit] for x in range(N)),N)
  ck(e==physical);es.append(e)
  if not e:Ds.append({});Ms.append({});tails.append({});coarses.append(None);continue
  mu=[p[s|bit]/e for s in lower];q=[p[s]+p[s|bit] for s in lower]
  ck(sum(mu)==1);ck(sum(q)==1)
  D=kl(mu,q);M=plus(*[(p[s|bit],lg((p[s]+p[s|bit])/p[s|bit])) for s in lower if p[s|bit]])
  ck(M==plus((e,lg(1/e)),(-e,D)));Ds.append(D);Ms.append(M)
  tails.append(plus(*[(p[s|bit],lg((p[s]+p[s|bit])/p[s|bit])) for s in lower if p[s|bit] and s.bit_count()>=2]))
  joint.extend((p[s|bit],e*(p[s]+p[s|bit])) for s in lower if p[s|bit])
  if L is not None:
   small=[j for j,s in enumerate(lower) if s.bit_count()<=L]
   a=[mu[j] for j in small];b=[q[j] for j in small]
   a.append(1-sum(a));b.append(1-sum(b));ck(sum(a)==sum(b)==1)
   coarses.append(dict(D=kl(a,b),tail_mu=a[-1],tail_q=b[-1]))
  else:coarses.append(None)
 I=sum(es)
 if I:
  direct=plus(*[(x/I,lg(x/y)) for x,y in joint])
  ck(direct==plus(*[(e/I,D) for e,D in zip(es,Ds)]))
  ck(sum(es)/I==1)
 return dict(p=p,es=es,I=I,Ds=Ds,Ms=Ms,M=plus(*[(1,t) for t in Ms]),tail=plus(*[(1,t) for t in tails]),coarses=coarses)
def seed_values(name):
 if name=='plus':return [1,1]
 if name=='minus':return [-1,-1]
 if name=='dictator':return [1,-1]
 if name=='and2':return [-1,1,1,1]
 if name=='parity2':return [1,-1,-1,1]
 if name=='majority3':return [1 if x.bit_count()<2 else -1 for x in range(8)]
 if name=='bent4':return [(-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16)]
 if name=='point4':return [-1]+[1]*15
 raise ValueError(name)
def build(seed,m,ell,k):
 n=len(seed).bit_length()-1;dn=m*n+ell
 hv=[]
 for x in range(1<<dn):
  v=(-1)**((x>>(m*n)).bit_count())
  for b in range(m):v*=seed[(x>>(b*n))&((1<<n)-1)]
  hv.append(v)
 return hv,[hv[x&((1<<dn)-1)] if x>>dn==0 else 1 for x in range(1<<(dn+k))]
mode=sys.argv[1];t0=time.perf_counter();rows=[]
if mode=='review':
 for name in ['plus','minus','dictator','and2','parity2','majority3','bent4','point4']:
  seed=seed_values(name);n=len(seed).bit_length()-1;base=analyze(seed)
  for m in ([1,2] if n<=2 else [1]):
   for ell in (2,3):
    for k in (1,2,4):
     hv,fv=build(seed,m,ell,k);h=analyze(hv);f=analyze(fv)
     q=F(1,1<<k);d=(1-q)**2+q*q;J=m*base['I']+ell
     Dc=plus(((1-q)*(k-1),{2:F(1)}),(q,lg(q/d)))
     Mc=plus((q*(1-q),{2:F(1)}),(q*q,lg(d/(q*q))))
     ck(h['I']==J);ck(f['I']==q*(J+k))
     for i in range(m*n+ell):
      if h['es'][i]:
       expected=base['Ds'][i%n] if i<m*n else {}
       ck(h['Ds'][i]==expected);ck(f['Ds'][i]==plus((1,expected),(k,{2:F(1)})))
     for i in range(m*n+ell,m*n+ell+k):ck(f['Ds'][i]==Dc)
     ck(f['M']==plus((q*m,base['M']),(k,Mc)))
     ck(f['tail']==plus((q*m,base['M']),(k*q*(1-k*q),{2:F(1)})))
     total=plus(*[(e,D) for e,D in zip(f['es'],f['Ds'])])
     ck(total==plus(*[(q*m*e,D) for e,D in zip(base['es'],base['Ds'])],(q*k*J,{2:F(1)}),(q*k,Dc)))
     rows.append(dict(seed=name,m=m,ell=ell,k=k,N=(len(fv).bit_length()-1),status='PASS'))
 ck(len(rows)==78)
elif mode=='coarse':
 for n in (2,3,4):
  seed=[-1]+[1]*((1<<n)-1)
  for m in ([1,2] if n<=3 else [1]):
   for L in (0,1,2):
    ell=L+2
    for k in (1,2):
     hv,fv=build(seed,m,ell,k);f=analyze(fv,L);q=F(1,1<<k)
     tail=q+q*q*sum(comb(k,j) for j in range(L+1,k+1))
     for i in range(m*n):
      c=f['coarses'][i];ck(c['tail_mu']==1);ck(c['tail_q']==tail);ck(c['D']==lg(1/tail))
      ck(tail>=q)
      seedbank=plus((f['es'][i],lg(1/f['es'][i])),(-f['es'][i],c['D']))
      ck(seedbank==plus((f['es'][i]*(n-1),{2:F(1)}),(f['es'][i],lg(tail/q))))
     rows.append(dict(n=n,m=m,L=L,ell=ell,k=k,N=len(fv).bit_length()-1,tail_mass=str(tail),status='PASS'))
 ck(len(rows)==30)
elif mode=='symbolic':
 for n in (6,8,12,20):
  e=F(1,1<<(n-1));m=1<<n;k=n;q=F(1,1<<k)
  ck(m*n*e==2*n);ck(2*(n-1)*e<=1);ck((1-e)**2+e*e<=1)
  for L in (0,1,2):
   ell=L+2;tail=q+q*q*sum(comb(k,j) for j in range(L+1,k+1));ck(q<=tail<=1)
   I=q*(3*n+ell);lower=q*2*n*(n-1)
   ck(lower/I==F(2*n*(n-1),3*n+ell))
   rows.append(dict(n=n,m=m,L=L,N=m*n+ell+k,I=str(I),coarse_M_over_I_at_least=str(lower/I),true_M_over_I_at_most='2',true_H_over_I_less_than='4',status='PASS'))
 ck(len(rows)==12)
else:raise ValueError(mode)
result=dict(status='PASS',mode=mode,cases=len(rows),assertions=checks,failures=0,runtime_seconds=time.perf_counter()-t0,arithmetic='Integer/Fraction; exact prime-log dictionaries, no float sign tests',rows=rows,full_FEI='OPEN')
(RUN/('out/'+mode.upper()+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
