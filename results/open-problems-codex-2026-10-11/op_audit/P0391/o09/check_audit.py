from fractions import Fraction as F
from math import comb, factorial, exp, log, sqrt
from pathlib import Path
import json, urllib.request, xml.etree.ElementTree as ET

out = {}
# Independent exact evaluation of the two cycle predicates reported by claimant.
rho = F(4, 5)
p1 = sum((1-rho)*rho**n * (1-sum((-1)**k*comb(n,k)*F(2-k)**n for k in range(3) if k <= n)/factorial(n)) for n in range(1,7))
p2 = sum((1-rho)*rho**n * sum(F(comb(n,k),2**n)*(1-F(5,9)**k/factorial(k)) for k in range(1,n+1)) for n in range(1,7))
assert p1 == F(552032,3515625)
assert p2 == F(117178177528,373669453125)
out['exact_cycle_rewards'] = {'constant':str(5*p1), 'marked':str(p2/2)}
# Laplace-generator balance for an original-size marked workload, not just Q.
# For arbitrary positional gamma exchangeability makes its sum equal one.
law = [(F(1),F(9,10)),(F(9),F(1,10))]
m = sum(b*p for b,p in law)
lam = float(rho/m)
errs=[]
for u in [.01,.1,1,5]:
    # V is residual workload in original class {9}; H class probability is 1/2.
    a = sum(float(p*b/m) if b != 9 else float(p/m)*(1-exp(-u*float(b)))/u for b,p in law)
    d = sum(float(p/m)*(1-exp(-u*float(b))) for b,p in law if b == 9)
    arrival = sum(float(p)*(exp(-u*float(b))-1) for b,p in law if b == 9)
    # Sum over geometric Q: service term d * (1-rho)*rho/(1-rho*a).
    total = (1-float(rho))/(1-float(rho)*a)*(float(rho)*d+lam*arrival)
    errs.append(abs(total))
assert max(errs) < 1e-14
out['marked_laplace_balance_max_error'] = max(errs)
# Check exponent arithmetic over 2,700 combinations; no probability proof by numerics.
q=2**(-.25); checked=0
for r in [100,10000,1e8]:
 for C in [1,3,10]:
  for eps in [.01,.1,1]:
   m0=1.8; m2=9.; c=eps**2*(1-q)**2/(4*((C/m0)*m2+eps/3))
   for j in range(100):
    b=r*2**(-(j+1)); a=(1-q)*q**j; x=eps*r*a
    exponent=x*x/(8*((C/m0)*r*b*m2+b*x/3))
    assert exponent >= c*2**(j/2)*(1-1e-13)
    checked+=1
out['dyadic_exponent_combinations'] = checked
out['pareto_interval_tail_constant'] = str(F(4,27)*(F(1,4)-F(1,9)))
assert F(4,27)*(F(1,4)-F(1,9)) == F(5,243)
Path('independent_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
url='https://export.arxiv.org/api/query?search_query=all:%22symmetric%20queue%22%20OR%20(all:%22service%20disciplines%22%20AND%20all:%22heavy%20traffic%22)&max_results=50'
try:
 data=urllib.request.urlopen(url,timeout=40).read()
 Path('arxiv_broad.xml').write_bytes(data)
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in ET.fromstring(data).findall('a:entry',ns):
  print(e.find('a:id',ns).text, e.find('a:title',ns).text)
except Exception as e:
 print('Broad search error:',e)
