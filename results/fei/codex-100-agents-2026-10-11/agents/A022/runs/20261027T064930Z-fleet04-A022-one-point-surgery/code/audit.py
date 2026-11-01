from fractions import Fraction as Q
from pathlib import Path
import json,time
start=time.monotonic();count=0
def ok(x):
 global count
 assert x
 count+=1
def transform(f):
 return [Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(f)),len(f)) for s in range(len(f))]
def seed(x):return (-1 if x%8==0 else 1)*(-1 if x//8==0 else 1)
bs=transform([seed(x) for x in range(64)])
spectra=[];tails=[]
for a,c in [(1,1),(1,-1),(-1,1),(-1,-1)]:
 f=[a if x==0 else -c if x==1 else seed(x) for x in range(64)]
 coeff=transform(f);spectra.append(coeff)
 for s in range(64):
  eps=-1 if s&1 else 1;B=bs[s]-Q(1-eps,64)
  ok(coeff[s]==B+Q(a-eps*c,64))
 p=[x*x for x in coeff]
 Z=[sum(p[t] for t in range(64) if t&s==s) for s in range(64)]
 tails.append(Z)
 ok(sum((1<<s.bit_count())*p[s] for s in range(64))<=Q(961,64))
 ok(sum(Z[1:])<16)
# All 35 laws with positive weights proportional to compositions of 8 into four parts.
# Three independent fixed tangent directions, midpoint radius selected inside simplex.
laws=[tuple(Q(x,8) for x in (a,b,c,8-a-b-c)) for a in range(1,6) for b in range(1,7-a) for c in range(1,8-a-b)]
for q in laws:
 for raw in [(1,-1,0,0),(1,0,-1,0),(1,0,0,-1)]:
  eta=min(q)/2;d=tuple(eta*x for x in raw);J=sum(v*v/p for p,v in zip(q,d))
  total=Q(0);p2=Q(0);ratio=Q(0)
  means=[sum(q[i]*spectra[i][s] for i in range(4)) for s in range(64)]
  for s in range(1,64):
   Z=sum(q[i]*tails[i][s] for i in range(4));Zd=sum(d[i]*tails[i][s] for i in range(4));A=means[s];Ad=sum(d[i]*spectra[i][s] for i in range(4))
   ok(Z>0);ok(A*A<=Z)
   rhs=sum(tails[i][s]*d[i]**2/q[i] for i in range(4))
   ok(Zd*Zd/Z<=rhs);total+=Zd*Zd/Z;p2+=2*Ad*Ad;ratio+=4*Ad*Ad
  u=sum(d[i]*v for i,v in enumerate([1,1,-1,-1]));v=sum(d[i]*v for i,v in enumerate([1,-1,1,-1]));L=u*u+v*v
  ok(total<=16*J);ok(p2<=L/32);ok(ratio<=L/16)
ok(Q(961,64)<16);ok(Q(3225,32)<101<288)
out={'status':'PASS','assertions':count,'laws':len(laws),'tangent_paths':3*len(laws),'seconds':time.monotonic()-start,'representation':'standalone direct characters; exact rational Fisher contraction and derivative-square bounds; no production imports','scope':'finite independent-representation audit, same author; no logarithm or universal inference from samples'}
root=Path(__file__).resolve().parents[1];(root/'out/audit.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
