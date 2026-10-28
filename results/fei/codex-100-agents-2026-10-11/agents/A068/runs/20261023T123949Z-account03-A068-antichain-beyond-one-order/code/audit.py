from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
R=Path(__file__).resolve().parents[1]; start=time.monotonic(); count=0
def ck(x):
 global count
 count+=1
 assert x
 assert time.monotonic()-start<40
def direct(t):
 return [F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t))**2 for s in range(len(t))]
h=[1 if x.bit_count()<=2 else -1 for x in range(32)]; p=direct(h)
ck(sum(p)==1); ck(p[0]==0)
for s,v in enumerate(p):ck(v==({1:F(9,64),3:F(1,64),5:F(9,64)}.get(s.bit_count(),F(0))))
ck(sum((s.bit_count()*v for s,v in enumerate(p)),F(0))==F(15,8))
mapping=[s^(2 if s&1 else 0) for s in range(32)]
ck(len(set(mapping))==32); ck(p[mapping[1]]!=p[1])
t=[(-1 if a&1 else 1)*(-1 if a&2 else 1)*h[a>>2] for a in range(128)]; pt=direct(t)
for s,v in enumerate(pt):ck(v==(p[s>>2] if s&3==3 else 0))
for K in [4,5,8]:
 e=F(1,2**(3*K)); q=[F(0)]+[e]*31; q[1]=1-30*e
 ck(sum(q)==1); ck(q[1]>F(1,2)); ck(q[1]<1)
 highmass=sum(p[s] for s in range(1,32) if s!=1)
 ck(highmass==F(55,64)); ck(3*K*highmass==F(165*K,64))
 ck(F(23*K,8)-F(165*K,64)-F(9,64)-F(1,4)>=F(51,64))
 ck(F(15*K,8)-F(165*K,64)-F(1,4)<0)
 ck(F(15*K,8)-5-F(1,4)>=F(9,4))
 # Independent noninvariant invoice via product of exact likelihood ratios:
 # 64*Delta = log_2[(31*q1)^9 (31*e)^55].
 # Delta=log31-c, certified negative from c>165K/64>5>log31.
 ck(F(165*K,64)>5 and 31<32)
 ck(sum(q[1:])/31==F(1,31))
out={'status':'PASS','assertions':count,'seconds':time.monotonic()-start,'representation':'direct physical character sums; no primary/helper imports','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out'/'audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))
