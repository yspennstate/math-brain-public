from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,itertools,time
import sympy as sy
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter()
a,e,d,q=sy.symbols('a e d q');vars=(a,e,d,q)
v=[4*a*(1-a),4*e*(1-e),4*d*(1-d),4*q*(1-q)]
c=[q*(d-e),d-q*a,e-q*(1-a),1-a*e-(1-a)*d]
dd=[q*(e+d-2*e*d),d+q*a-2*d*q*a,e+q*(1-a)-2*e*q*(1-a),c[3]]
T=v[0]*v[3]*(v[1]+v[2])/16
cases=[]
for signs in itertools.product((-1,1),repeat=3):
 polynomial=sum(v[i]*(2*dd[i]-((signs+(1,))[i])*c[i]-2*c[i]**2+((signs+(1,))[i])*c[i]**3) for i in range(4))-4*T
 pp=sy.Poly(sy.expand(polynomial),*vars)
 deg=tuple(pp.degree(x) for x in vars)
 coeff={idx:Q(int(k.p),int(k.q)) for idx,k in pp.terms()}
 bern={}
 for i in itertools.product(*(range(n+1) for n in deg)):
  value=Q(0)
  for j,z in coeff.items():
   if all(j[k]<=i[k] for k in range(4)):
    f=Q(1)
    for k in range(4):f*=Q(comb(i[k],j[k]),comb(deg[k],j[k]))
    value+=z*f
  bern[i]=value
 negatives=[{'index':list(i),'value':str(z)} for i,z in bern.items() if z<0]
 cases.append({'signs':list(signs),'degrees':list(deg),'power_coefficients':[{'index':list(i),'value':str(z)} for i,z in sorted(coeff.items())],
               'bernstein_coefficients':[{'index':list(i),'value':str(z)} for i,z in sorted(bern.items())],
               'negative_count':len(negatives),'negative_examples':negatives[:5]})
 assert time.perf_counter()-start<60
out={'helper':'A043-quadratic-slack-polynomial-v1','all_nonnegative':all(not x['negative_count'] for x in cases),
     'cases':cases,'runtime_seconds':time.perf_counter()-start,
     'status':'full-box coefficient inspection; failure is not a counterexample to polynomial or entropy inequality'}
(ROOT/'out/bernstein.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_nonnegative':out['all_nonnegative'],'negative_counts':[x['negative_count'] for x in cases],'runtime_seconds':out['runtime_seconds']}))
