from pathlib import Path
from fractions import Fraction as R
from math import factorial,comb
from itertools import permutations
from bisect import bisect_left
import json
D=4
def L(j,both):
 return {(r,s):R(1,factorial(r)*factorial(s)*factorial(r+s+j)) for r in range(D+1) for s in range(D+1-r) if both or r==0}
def plus(a,b,sign=1):
 out=a.copy()
 for rs,v in b.items():out[rs]=out.get(rs,R(0))+sign*v
 return out
def times(a,b):
 out={}
 for (r,s),x in a.items():
  for (u,v),y in b.items():
   if r+s+u+v<=D:out[r+u,s+v]=out.get((r+u,s+v),R(0))+x*y
 return out
C=plus(times(L(1,True),plus(L(1,False),L(2,False),-1)),times(plus(L(3,True),L(2,True),-1),L(0,False)))
checks=[]
for n in range(3,D+4):
 counts={}
 for word in permutations(range(1,n+1)):
  tops=[]
  for x in word:
   i=bisect_left(tops,x)
   if i==len(tops):tops.append(x)
   else:tops[i]=x
  if len(tops)>=3 and tops[2]==n:
   b=tops[1];counts[b]=counts.get(b,0)+1
 for b in range(2,n):
  r=b-2;s=n-b-1;expected=R(counts.get(b,0),factorial(n)*factorial(r)*factorial(s))
  assert C[r,s]==expected,(r,s,C[r,s],expected)
  checks.append({'r':r,'s':s,'coefficient':str(expected),'result':'PASS'})
Path('triple_density_checks.json').write_text(json.dumps({'degree':D,'checks':checks},indent=2),encoding='utf8')
print('PASS: closed triple density coefficients',len(checks))
