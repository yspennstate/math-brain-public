from fractions import Fraction as R
from pathlib import Path
import json,time
from functools import lru_cache
S=time.monotonic(); count=0
def test(b):
 global count
 count+=1
 if not b: raise AssertionError(count)
 if time.monotonic()-S>55: raise TimeoutError('frozen cap')
@lru_cache(maxsize=4096)
def log_bounds(x):
 # Independent range reduction by repeated scaling, then atanh with 24 terms.
 shift=0
 while x>2: x/=2; shift+=1
 while x<1: x*=2; shift-=1
 def unit(a):
  z=(a-1)/(a+1); p=z; acc=R(0)
  for i in range(24): acc+=2*p/(2*i+1); p*=z*z
  return acc,acc+2*p/(49*(1-z*z))
 a,b=unit(x); c,d=unit(R(2))
 return a+shift*(c if shift>=0 else d),b+shift*(d if shift>=0 else c)
def divergence(p,q):
 a=b=R(0)
 for x,y in zip(p,q):
  if x:
   test(y>0); l,h=log_bounds(x/y); a+=x*l; b+=x*h
 return a,b
def db(k,l): return divergence((1-k,k),(1-l,l))
ln2lo,ln2hi=log_bounds(R(2))
scalar=0
for w0 in range(9):
 for k0 in range(9):
  for k1 in range(9):
   w=R(w0,8); ks=[R(k0,8),R(k1,8)]; eta=w*ks[0]+(1-w)*ks[1]
   ls=[R(15,16)*k+eta/16 for k in ks]
   test(w*ls[0]+(1-w)*ls[1]==eta)
   test(all(eta/16<=l<=1-(1-eta)/16 for l in ls))
   if eta not in (0,1):
    u=w*db(ks[0],ls[0])[1]+(1-w)*db(ks[1],ls[1])[1]
    test(u/ln2lo<R(31,160)*eta)
   scalar+=1
booleans=[]
for n in range(1,7):
 N=2**(n+1); vals=[-1 if x==0 else 1 for x in range(N)]
 hat=[R(sum(vals[x]*(-1 if (x&t).bit_count()%2 else 1) for x in range(N)),N) for t in range(N)]
 P=[a*a for a in hat]; Q=[R(0)]*N; eta=R(1,2**n)
 for t in range(2**n):
  q=P[2*t]+P[2*t+1]
  if q:
   k=P[2*t+1]/q; ell=R(15,16)*k+eta/16
   Q[2*t]=q*(1-ell);Q[2*t+1]=q*ell
 test(sum(P)==sum(Q)==1)
 test(sum(Q[1::2])==eta)
 test(divergence(P,Q)[1]/ln2lo<R(31,160)*eta)
 influence=R(0)
 for i in range(n+1): influence+=R(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N)
 test(influence==(n+1)*eta)
 if n>=6:
  k=P[1]/(P[0]+P[1]); l=Q[1]/(Q[0]+Q[1]); test(l*(1-k)>2*k*(1-l))
 booleans.append({'n_data':n,'influence':str(influence),'full_truth_table_size':N})
out={'status':'PASS','scalar_two_row_laws':scalar,'direct_character_Boolean_guards':booleans,'exact_assertions':count,'seconds':time.monotonic()-S,'no_main_imports':True}
(Path(__file__).resolve().parents[1]/'out'/'independent.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='direct_character_Boolean_guards'}))
