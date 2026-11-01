from fractions import Fraction as F
from collections import defaultdict
import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parent
cases=[0,0]
def marginal(S,n,b):
 ans={}
 for i in range(n):
  T=S^(1<<i)
  rate=F(S.bit_count()-1,n) if S>>i&1 else b
  if rate: ans[T]=rate
 return ans
for n in range(2,8):
 b=F(5,11)
 for X in range(1,1<<n):
  for Y in range(1,1<<n):
   common=X&Y; diff=X^Y
   stage=1 if X&Y==X and diff.bit_count()==1 else (2 if X.bit_count()==Y.bit_count() and diff.bit_count()==2 else 0)
   if not stage: continue
   events=defaultdict(F)
   def add(x,y,rate):
    if rate:
     assert x and y
     events[x,y]+=rate
   for i in range(n):
    mask=1<<i
    if not (X|Y)&mask: add(X|mask,Y|mask,b)
    if common&mask:
     add(X^mask,Y^mask,F(X.bit_count()-1,n))
     if stage==1: add(X,Y^mask,F(1,n))
   if stage==1:
    add(Y,Y,b); add(X,X,F(X.bit_count(),n))
   else:
    add(X|Y,X|Y,b); add(common,common,F(X.bit_count()-1,n))
   mx=defaultdict(F); my=defaultdict(F)
   internal_up=F(0); internal_down=F(0); exits=F(0)
   for (x,y),rate in events.items():
    if x!=X: mx[x]+=rate
    if y!=Y: my[y]+=rate
    if stage==1:
     remains=x&y==x and (x^y).bit_count()==1
     if remains:
      assert abs(x.bit_count()-X.bit_count())==1
      if x.bit_count()>X.bit_count(): internal_up+=rate
      else: internal_down+=rate
     else:
      assert x==y or (x.bit_count()==y.bit_count() and (x^y).bit_count()==2)
      exits+=rate
    else:
     if x==y: exits+=rate
     else:
      assert x.bit_count()==y.bit_count() and (x^y).bit_count()==2
      if x.bit_count()>X.bit_count(): internal_up+=rate
      else: internal_down+=rate
   assert dict(mx)==marginal(X,n,b) and dict(my)==marginal(Y,n,b)
   k=X.bit_count()
   if stage==1:
    assert (internal_up,internal_down,exits)==(b*(n-k-1),F(k*(k-1),n),b+F(2*k,n))
   else:
    r=k-1
    assert (internal_up,internal_down,exits)==(b*(n-r-2),F(r*r,n),b+F(r,n))
   cases[stage-1]+=1
(ROOT/'coupling_results.json').write_text(json.dumps({'exact_stage_I_pairs':cases[0],'exact_stage_II_pairs':cases[1],'n':'2..7','beta':'5/11','result':'all marginals, stage transitions, internal rates and killing rates agree exactly'},indent=2),encoding='utf-8')
print(cases)
