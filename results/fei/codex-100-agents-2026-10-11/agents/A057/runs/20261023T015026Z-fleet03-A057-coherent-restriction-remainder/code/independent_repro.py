from pathlib import Path
from fractions import Fraction as Q
import json,time
ROOT=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
ns={'__file__':str(ROOT/'code/check_nonflat.py')}
exec((ROOT/'code/check_nonflat.py').read_text(encoding='utf-8').split('worst_lower=None')[0],ns)
def ck(x):
 global checks
 assert x;checks+=1
def factor(n):
 out={};p=2
 while n>1:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 return out
def direct_entropy(v):
 N=len(v);out={}
 for s in range(N):
  z=sum(a*(-1 if (x&s).bit_count()%2 else 1) for x,a in enumerate(v))
  if not z:continue
  mass=Q(z*z,N*N)
  for p,e in factor(mass.denominator).items():out[p]=out.get(p,Q(0))+mass*e
  for p,e in factor(mass.numerator).items():out[p]=out.get(p,Q(0))-mass*e
 return {p:z for p,z in out.items() if z}
b=[(-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16)]
for gt in range(16):
 if time.monotonic()-start>55:raise RuntimeError('frozen55-second cap')
 g=[1 if(gt>>j)&1 else -1 for j in range(4)]
 f0=[g[j] for j in range(4) for x in range(16)]
 f1=[g[j] if x==0 else b[x] for j in range(4) for x in range(16)]
 for vals in [g,f1,f0+f1]:ck(direct_entropy(vals)==ns['entropy'](vals))
 directD=ns['add']((1,direct_entropy(f0+f1)),(-Q(1,2),direct_entropy(g)),(-Q(1,2),direct_entropy(f1)))
 d=Q(sum(x!=y for x,y in zip(f0,f1)),64)
 ck(d==(Q(15,16)-Q(3,16)*Q(sum(g),4))/2)
 ck(ns['nonneg'](ns['add']((1,{2:6*d-Q(1,8)-d/3}),(-1,directD))))
for r,k in [(1,2),(2,2),(2,4),(3,2),(4,2)]:
 n=r*k;p=Q(1,1<<r);v=[]
 for x in range(1<<n):v.append(1 if any(((x>>(r*j))&((1<<r)-1))==0 for j in range(k)) else -1)
 I=sum(Q(sum(v[x]!=v[x^(1<<j)] for x in range(1<<n)),1<<n) for j in range(n))
 ck(I==2*k*r*p*(1-p)**(k-1))
 ck(Q(sum(v),len(v))==1-2*(1-p)**k)
 # Full Walsh influence independently sums cardinality-weighted exact masses.
 w=ns['walsh'](v);ck(sum(Q(z*z*s.bit_count(),len(v)**2) for s,z in enumerate(w))==I)
for m in range(4,257):
 c=Q(1,1<<m);a=(1+c)/2
 ck(21*a-(20+c*(20+m))/2>=Q(13,32))
ck(Q(5,2)+Q(2,9)<3);ck(Q(48,12)>Q(27,8))
result={'status':'PASS','exact_assertions':checks,'direct_character_source_roots':16,'small_priority_fixtures':5,
        'allocation_cases':253,'elapsed_seconds':time.monotonic()-start,'arithmetic':'direct character sums/Fraction; independent factorization; physical edge enumeration'}
(ROOT/'out/repro.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
