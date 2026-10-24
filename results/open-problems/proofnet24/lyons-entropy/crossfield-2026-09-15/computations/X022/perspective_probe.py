import sympy as s
import numpy as np
from math import comb
from pathlib import Path
import json
A,B,C,D=s.symbols('a b c d', real=True)
vars=(A,B,C,D)
def mom(k,x):
    return s.Rational(1,2)*((1+x)**(1-k)+(1-x)**(1-k))
res=[]
for n in range(1,7):
    f=sum(s.binomial(2*n,2*j)*B**(2*j)*C**(2*n-2*j)*mom(2*j,A)*mom(2*n-2*j,D) for j in range(n+1))/s.Integer(2*n*(2*n-1))
    h=s.lambdify(vars,s.hessian(f,vars),'numpy',cse=True)
    vals=[]
    for pt in [(0, .25,.25,0),(.2,.2,.3,.1),(.6,.05,.2,.2),(.7,.2,.01,.2),(.2,.001,.001,.3),(.8,.01,.1,.5)]:
        assert pt[1]/(1-pt[0])+pt[2]/(1-pt[3])<1
        vals.append({'point':pt,'eigenvalues':np.linalg.eigvalsh(np.array(h(*pt),float)).tolist()})
    res.append({'n':n,'checks':vals})
Path('computations/X022/perspective_probe.json').write_text(json.dumps(res,indent=2))
for item in res: print(item['n'],min(v['eigenvalues'][0] for v in item['checks']))
