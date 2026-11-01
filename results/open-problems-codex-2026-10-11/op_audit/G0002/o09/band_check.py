from fractions import Fraction as F
import math
from itertools import product
for d in range(1001):
 assert F(math.comb(2*d,d)**2,16**d)<=F(1,d+1)
 assert 4*(d+1)**3-(2*d+1)**2*(d+2)==3*d+2
print('Central binomial induction and exact values d=0..1000: PASS',flush=True)
# Arbitrary monotone band families, directly use literal (49.1).
for n in [2,4]:
 d=n//2; count=0
 for truth in product([False,True],repeat=2**n):
  if any(truth[w] and not truth[w|(1<<i)] for w in range(2**n) for i in range(n)): continue
  if any((w.bit_count()>=d+1 and not truth[w]) or (truth[w] and w.bit_count()<d-2) for w in range(2**n)): continue
  count+=1
  for w in range(2**n):
   if not truth[w]: continue
   P=set()
   for x in [w]+[w&~(1<<j) for j in range(n) if (w>>j)&1]:
    P.update(i for i in range(n) if not truth[x&~(1<<i)] and truth[x|(1<<i)])
   if P: assert d-2<=w.bit_count()<=d+2
 print('Band support direct check',n,count,'families: PASS',flush=True)
