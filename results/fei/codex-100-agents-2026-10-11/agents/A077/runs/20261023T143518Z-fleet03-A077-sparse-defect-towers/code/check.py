from pathlib import Path
from fractions import Fraction as F
from math import comb
from collections import Counter
from functools import lru_cache
import itertools,json,time,sys
R=Path(__file__).resolve().parents[1];start=time.perf_counter();pilot='--pilot' in sys.argv;checks=0;rows=[]
def ck(x):
 global checks
 checks+=1
 assert x
 assert time.perf_counter()-start<(55 if pilot else 120)
def walsh(t):
 a=list(t);step=1
 while step<len(a):
  for j in range(0,len(a),step*2):
   for k in range(j,j+step):a[k],a[k+step]=a[k]+a[k+step],a[k]-a[k+step]
  step*=2
 return a
def ln_interval(x):
 z=(x-1)/(x+1);s=sum((2*z**(2*k+1)/F(2*k+1) for k in range(24)),F(0));tail=2*abs(z)**49/(49*(1-z*z))
 return s-tail,s+tail
ln2=ln_interval(F(2))
@lru_cache(None)
def log(n):
 k=n.bit_length()-1;l,u=ln_interval(F(n,1<<k));return k+l/ln2[1],k+u/ln2[0]
def entropy(a,N):
 lo=hi=F(0);shift=2*(N.bit_length()-1)
 for val,count in Counter(abs(v) for v in a).items():
  if val:
   l,u=log(val);mass=F(count*val*val,N*N);lo+=mass*(shift-2*u);hi+=mass*(shift-2*l)
 return lo,hi
def influence(t):return sum((F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(len(t).bit_length()-1)),F(0))
params=[]
for b in range(3,32,2):
 m=(b-1)//2;c=b+3;d=2*b+3;p=F(1,1<<(b+4));alpha=F(comb(2*m,m),1<<(2*m));I0=F(d*comb(d-1,(d-1)//2),1<<(d-1))
 lm=alpha*b*sum((F(comb(m,l),2*l+1) for l in range(m+1)),F(0));la=(1+lm)/2
 ck(la>=F(2**(m-1),b));ck(d*d*p<1);ck(p*(3*b+7)<=F(1,8));ck(I0>=F(315,128));ck(F(33,8)<=2*I0)
 if b in (3,5):ck(sum(abs(v) for v in walsh([1 if 2*x.bit_count()<b else -1 for x in range(1<<b)]))==lm*(1<<b))
 params.append({'b':b,'d':d,'p':str(p),'indicator_l1':str(la),'I0':str(I0),'d_squared_p':str(d*d*p)})
for b in ([3] if pilot else [3,5]):
 c=b+3;d=2*b+3;N=1<<d;p=F(1,1<<(b+4));h=[1 if 2*s.bit_count()<d else -1 for s in range(N)];event=[s%(1<<c)==0 and 2*(s>>c).bit_count()<b for s in range(N)];ha=walsh(h);aa=walsh([int(x) for x in event]);Hh=entropy(ha,N);CA=entropy(aa,N);I0=influence(h);Ib=F(b*comb(b-1,(b-1)//2),1<<(b-1));ID=F(c+Ib,1<<c)
 ck(sum(event)==p*N);ck(CA[1]<=p*(d+b+4));ck(all(h[s]==h[s^(1<<j)]==1 for s in range(N) if event[s] for j in range(d)))
 for n in range(2 if pilot else 3):
  M=1<<n
  for v in itertools.product((-1,1),repeat=M):
   mu=F(sum(v),M);tt=[v[t] if event[s] else h[s] for s in range(N) for t in range(M)];fa=walsh(tt);va=walsh(v);HH=entropy(fa,N*M);HV=entropy(va,M);iv=influence(v)
   ish=sum((F(sum(tt[x]!=tt[x^(1<<(n+j))] for x in range(len(tt))),len(tt)) for j in range(d)),F(0));ipr=sum((F(sum(tt[x]!=tt[x^(1<<j)] for x in range(len(tt))),len(tt)) for j in range(n)),F(0))
   ck(ish==I0+(1-mu)*ID/2);ck(ipr==p*iv);ck(HH[1]<=p*HV[0]+Hh[0]+F(33,8));ck(HH[1]<=p*HV[0]+11*ish)
   # Complete coefficient formula, including every empty-private row.
   for s in range(N):
    ck(F(fa[s*M],N*M)==F(ha[s],N)+(mu-1)*F(aa[s],N))
    for t in range(1,M):ck(F(fa[s*M+t],N*M)==F(aa[s]*va[t],N*M))
   row={'b':b,'n':n,'V':list(v),'mu':str(mu),'p':str(p),'H_interval':list(map(str,HH)),'H_profile_interval':list(map(str,HV)),'shared_influence':str(ish),'private_influence':str(ipr),'carrier_influence':str(I0)};rows.append(row)
   if not pilot:
    (R/'out'/('spectrum_b'+str(b)+'_n'+str(n)+'_'+str(len(rows))+'.json')).write_text(json.dumps({'normalization':N*M,'integer_walsh':fa,'profile_walsh':va})+'\n',encoding='utf-8')
out={'status':'PASS','pilot':pilot,'exact_assertions':checks,'actual_roots':len(rows),'analytic_parameter_cases':len(params),'seconds':time.perf_counter()-start,'roots':rows,'parameters':params,'full_fei':'OPEN'}
(R/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('roots','parameters')}))
