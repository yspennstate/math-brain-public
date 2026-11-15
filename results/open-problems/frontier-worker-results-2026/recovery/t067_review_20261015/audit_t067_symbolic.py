"""Independent all-simplex proof of the signed cubic term; no solver imports."""
from pathlib import Path
from datetime import datetime
import json
import sympy as s

p = s.symbols('p1 p2 p3')
def Dz(f,j):
    return s.expand(sum(p[k]*((1 if k==j else 0)-p[j])*s.diff(f,p[k]) for k in range(3)))
def direction(f,v):
    return s.expand(sum(v[j]*Dz(f,j) for j in range(3)))
def normalized(f):
    return s.expand(f.subs(p[2],1-p[0]-p[1]))

e2=p[0]*p[1]+p[0]*p[2]+p[1]*p[2]
e3=p[0]*p[1]*p[2]
ell=[]
for i in range(3):
    j,k=[a for a in range(3) if a!=i]
    v=[s.Rational(1,3) if a==i else -s.Rational(1,6) for a in range(3)]
    h=[1 if a==j else -1 if a==k else 0 for a in range(3)]
    raw=(-direction(p[i],v)/2-direction(direction(p[i],h),h)/4
         +sum(Dz(Dz(Dz(p[i],a),a),a) for a in range(3))/4)
    advertised=-p[i]*(p[j]-p[k])**2/2+s.Rational(3,2)*e3*(1-3*p[i])
    assert normalized(raw-advertised)==0
    ell.append(raw)
assert normalized(sum(p[i]*ell[i] for i in range(3))+e2*(e2-9*e3))==0
positive_certificate=sum(p[k]*(p[i]-p[j])**2 for i,j,k in [(0,1,2),(1,2,0),(2,0,1)])
assert normalized(e2-9*e3-positive_certificate)==0
result={'at':datetime.now().astimezone().isoformat(),'status':'PASS exact polynomial identities',
    'method':'Differentiated softmax through its polynomial vector field; normalized only after all derivatives',
    'signed_cubic':'sum_i p_i ell_i = -e2*(e2-9e3)',
    'sign_certificate':'e2-9e3 = sum_cyclic p_k*(p_i-p_j)^2 >= 0 on the closed probability simplex',
    'scope':'Proves the pointwise averaged polynomial sign. Bayesian calibration is needed to turn it into E_1 ell_1 <= 0; individual ell_1 need not be nonpositive.'}
Path(__file__).with_name('T067_SYMBOLIC_RECEIPT.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'))
print(json.dumps(result),flush=True)
