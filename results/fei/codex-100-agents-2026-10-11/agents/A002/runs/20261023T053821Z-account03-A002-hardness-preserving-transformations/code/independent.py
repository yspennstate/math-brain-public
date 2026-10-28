from fractions import Fraction as Q
from pathlib import Path
import itertools,json,time
R=Path(__file__).resolve().parents[1]; start=time.monotonic(); c=0; leaves=0
def ok(x):
 global c
 assert x
 c+=1
 assert time.monotonic()-start<55
def direct(f):
 N=len(f); n=N.bit_length()-1
 a=[Q(sum(f[x]*(-1)**((x&s).bit_count()%2) for x in range(N)),N) for s in range(N)]
 I=sum((Q(sum(f[x]!=f[x^(1<<j)] for x in range(N)),N) for j in range(n)),Q(0))
 ok(I==sum((s.bit_count()*a[s]**2 for s in range(N)),Q(0))); ok(sum(x*x for x in a)==1)
 return a,I
def rest(f,A,b):
 n=len(f).bit_length()-1; free=[j for j in range(n) if j not in A]
 return tuple(f[sum(((x>>j)&1)<<i for j,i in enumerate(free))+sum(((b>>j)&1)<<i for j,i in enumerate(A))] for x in range(1<<len(free)))
for t in (1,2):
 d=2*t; h=tuple((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(t)) for x in range(1<<d))
 mu=Q(sum(h),len(h)); F=tuple(h[x>>2] if x%4==0 else 1 for x in range(1<<(d+2)))
 ah,ih=direct(h); af,iF=direct(F); ok(iF==Q(1,4)*(ih+2*(1-mu)))
 for s,a in enumerate(af):
  u=s>>2; z=s%4
  expected=(1-Q(1,4)*(1-mu) if z==0 else -Q(1,4)*(1-mu)) if u==0 else ah[u]/4
  ok(a==expected)
 for q in range(min(2,d)+1):
  for A in itertools.combinations(range(d),q):
   for b in range(1<<q):
    hb=rest(h,A,b); physical=rest(F,tuple(j+2 for j in A),b)
    expected=tuple(hb[x>>2] if x%4==0 else 1 for x in range(len(hb)*4)); ok(physical==expected)
    ab,ib=direct(hb); ac,ic=direct(physical); mb=Q(sum(hb),len(hb)); ok(ic==Q(1,4)*(ib+2*(1-mb)))
    leaves+=1
# exact scalar missing-tail guards at k10, no enormous truth table
ok(Q(2)-Q(115,1024)>Q(9,8)); ok(Q(1)-Q(135,1024)==Q(889,1024)>0)
out={'status':'PASS','assertions':c,'roots':2,'complete_children':leaves,'elapsed_seconds':time.monotonic()-start,'method':'direct characters and physical edges, no imported primary helper'}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2),encoding='utf-8'); print(json.dumps(out))
