from functools import lru_cache
from fractions import Fraction as F
from itertools import product
import pathlib,json
P=pathlib.Path(__file__).parent
results=[]
for k,c in ((F(1,4),F(3,16)),(F(1,4),F(1,10)),(F(1,2),F(1,4)),(F(1),F(1,4)),(F(2),F(1,4)),(F(2),F(1,10))):
 @lru_cache(None)
 def H(n):
  return F(1) if n==0 else 1-c/k if n==1 else H(n-1)-c*H(n-2)
 @lru_cache(None)
 def g(word):
  j=word.find('DE')
  if j>=0:return c*(g(word[:j]+'D'+word[j+2:])+g(word[:j]+'E'+word[j+2:]))
  a=word.count('E');b=word.count('D');assert word=='E'*a+'D'*b
  return (c/k)**a*H(b)
 for n in range(1,9):
  words=[''.join(w) for w in product('ED',repeat=n)]
  assert sum(g(w) for w in words)==1
  assert min(g(w) for w in words)>0
  for w in words:
   assert g(w+'E')+g(w+'D')==g(w)
   assert g('E'+w)==c/k*g(w)
   # Test all reduction locations, independently of first-occurrence recursion.
   for j in range(n-1):
    if w[j:j+2]=='DE':assert g(w)==c*(g(w[:j]+'D'+w[j+2:])+g(w[:j]+'E'+w[j+2:]))
  residual={w:F(0) for w in words}
  for w in words:
   rate_mass=[]
   if w[0]=='E':rate_mass.append(('D'+w[1:],k*g(w)))
   if w[-1]=='D':rate_mass.append((w[:-1]+'E',c*g(w[:-1])))
   for j in range(n-1):
    if w[j:j+2]=='DE':rate_mass.append((w[:j]+'ED'+w[j+2:],g(w)))
   for t,flow in rate_mass:residual[t]+=flow;residual[w]-=flow
  assert all(v==0 for v in residual.values())
  for j in range(n-1):assert sum(g(w) for w in words if w[j:j+2]=='DE')==c
  results.append({'kappa':str(k),'c':str(c),'length':n,'minimum_cylinder_probability':str(min(g(w) for w in words)),'normalization':'1','all_stationarity_residuals':'0','bulk_currents':str(c)})
 # Right boundary rates need not be constant; full stationary generator tested above.
 assert k*g('E')==c
(P/'halfline_checks.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print('PASS: 48 exact half-line cylinder/finite-generator tests; lengths 1-8; six parameter pairs.')
