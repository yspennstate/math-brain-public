"""Independent exact Bellman check: all character pairs on three private bits."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];O=R/'out'
(O/'INDEPENDENT_SPEC.json').write_text(json.dumps({'version':'A078-direct-character-Bellman-1','family':'all 16 signed characters on 3 bits, all 256 ordered pairs; two shared widths; every adaptive private stopping tree via exact Bellman recursion','case_count':512,'arithmetic':'integer direct Walsh; Fraction; all nonzero controller amplitudes are signed one, so collision is exactly 0 or -4e','symmetry':'none in root domain; memoization identifies identical restricted tables','memory_estimate_MB':30,'max_runtime_seconds':55},indent=2),encoding='utf-8')
t0=time.monotonic();checks=0
def check(c):
 global checks
 checks+=1;assert c,checks
 if time.monotonic()-t0>55:raise TimeoutError('55 second cap')
def chars(n):
 return [tuple(sign*(-1 if (x&s).bit_count()%2 else 1) for x in range(2**n)) for s in range(2**n) for sign in [-1,1]]
def coeffs(v):
 return [F(sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(v)),len(v)) for s in range(len(v))]
def child(v,i,b):
 ids=[x for x in range(len(v)) if (x>>i)&1==b];return tuple(v[x] for x in ids)
def collision(v,w,e):
 a,b=coeffs(v),coeffs(w)
 check(sum(x*x for x in a)==1 and sum(x*x for x in b)==1)
 check(all(x in [-1,0,1] for x in a+b))
 # Nonempty coincident character labels contribute k(+/-1,+/-1)=-4.
 return -4*e*sum(abs(a[s]*b[s]) for s in range(1,len(a)))
@lru_cache(None)
def bellman(v,w,e):
 xi=collision(v,w,e);check(-4*e<=xi<=0)
 choices=[xi]
 for i in range(len(v).bit_length()-1):
  choices.append(sum((bellman(child(v,i,b),child(w,i,b),e) for b in [0,1]),F(0))/2)
 z=min(choices)
 check(-4*e<=z<=xi)
 return z
count=0
for v in chars(3):
 for w in chars(3):
  for d in [1,2]:
   e=F(1,2**d);xi=collision(v,w,e);m=bellman(v,w,e)
   # Budget after the first booked debit; every subsequent adaptive cut included.
   B=7*e;check(B-xi+m>=3*e)
   count+=1
out={'status':'PASS','root_cases':count,'exact_assertions':checks,'distinct_Bellman_states':bellman.cache_info().currsize,'runtime_seconds':time.monotonic()-t0,'coverage':'all adaptive stopping policies on the frozen signed-character domain; no universal-FEI inference'}
(O/'INDEPENDENT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out),flush=True)
