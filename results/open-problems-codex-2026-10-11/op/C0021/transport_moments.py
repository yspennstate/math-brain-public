"""Exact exhaustive checks for a mean- and bottleneck-optimal monotone bijection."""
import pathlib,json
from fractions import Fraction
P=pathlib.Path(__file__).parent;mapping={0:3,1:5,2:6,4:7}
def f(x):
 if len(x)==1:return x[0]
 m=len(x)//3;return int(sum(f(x[i*m:(i+1)*m]) for i in range(3))>=2)
def T(x):
 assert f(x)==0
 if len(x)==1:return (1,)
 m=len(x)//3;cs=[x[i*m:(i+1)*m] for i in range(3)];b=sum(f(c)<<i for i,c in enumerate(cs));c=mapping[b]
 return sum((T(s) if ((c>>i)&1)>((b>>i)&1) else s for i,s in enumerate(cs)),())
rows=[]
for k in (0,1,2):
 n=3**k;seen=set();ds=[]
 for v in range(1<<n):
  x=tuple((v>>i)&1 for i in range(n))
  if f(x):continue
  y=T(x);assert f(y)==1 and all(a<=b for a,b in zip(x,y)) and y not in seen;seen.add(y);ds.append(sum(a!=b for a,b in zip(x,y)))
 mean=Fraction(sum(ds),len(ds));second=Fraction(sum(z*z for z in ds),len(ds));mu=Fraction(3,2)
 assert mean==mu**k and max(ds)==2**k
 assert second==Fraction(4,3)*mu**(2*k)-Fraction(1,3)*mu**k
 rows.append(dict(k=k,inputs=len(ds),mean=str(mean),second_moment=str(second),maximum=max(ds),distribution={str(z):ds.count(z) for z in sorted(set(ds))}))
(P/'transport_moments.json').write_text(json.dumps(rows,indent=2),encoding='utf8');print(json.dumps(rows,indent=2))
