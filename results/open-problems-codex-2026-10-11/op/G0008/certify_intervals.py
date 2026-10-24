from pathlib import Path
from fractions import Fraction as F
from math import comb
import sympy as S,json
x=S.symbols('x');expr=S.sympify(Path('free_wired_polynomial.txt').read_text());H=S.Poly(S.cancel(expr/(x*(1-x)**6)),x);N=H.degree();c=[int(H.nth(i)) for i in range(N+1)]
def bern(a,b):
 power=[sum(F(c[j])*comb(j,i)*a**(j-i)*(b-a)**i for j in range(i,N+1)) for i in range(N+1)]
 return [sum(power[j]*F(comb(k,j),comb(N,j)) for j in range(k+1)) for k in range(N+1)]
cert=[]
for a,b in [(F(0),F(2,5)),(F(19,20),F(1)),(F(23,25),F(1))]:
 bb=bern(a,b);mn=min(bb);print(a,b,'MIN_SIGN',mn>0,'min_float',float(mn))
 if mn>0:cert.append({'a':str(a),'b':str(b),'degree':N,'bernstein_coefficients':[str(v) for v in bb]})
Path('interval_certificates.json').write_text(json.dumps({'H_power_coefficients':c,'certificates':cert},indent=2),encoding='utf8')
