"""Exact rational certificate used for C024's strongly coherent four-mode family."""
from fractions import Fraction as F
import json

# Natural logarithm bounds. After multiplying x by a power of two, both
# logarithms use atanh arguments in [0, 1/3].
def log_unit_bounds(x, terms=12):
    r=(x-1)/(x+1)
    assert 0 <= r <= F(1,3)
    low=2*sum((r**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    tail=2*r**(2*terms+1)/(F(2*terms+1)*(1-r*r))
    return low,low+tail

def log_bounds(x):
    assert x>0
    k=0
    while x<1:
        x*=2;k+=1
    assert x<=2
    lo,hi=log_unit_bounds(x)
    l2,h2=log_unit_bounds(F(2))
    return lo-k*h2,hi-k*l2

atoms=[(2,F(81,10000)),(8,F(369,10000)),(2,F(1681,10000)),
       (2,F(1105,10000)),(2,F(657,10000))]
assert sum(m*p for m,p in atoms)==1
upper=F(0)
cert=[]
for mult,p in atoms:
    lo,hi=log_bounds(p)
    lo+=F(5,2);hi+=F(5,2)
    sq=max(lo*lo,hi*hi)
    upper+=mult*p*sq
    cert.append({'multiplicity':mult,'p':str(p),'shifted_log_low':str(lo),
                 'shifted_log_high':str(hi),'square_upper':str(sq)})
assert upper<F(19,40)
assert log_bounds(F(657,10000))[0]>-3
h=F(1,2000)
theta=4*h/(F(1,10)-h)
assert theta<F(1,49)
var_uniform=F(49,48)*(F(5,7)+F(1,49))**2
assert var_uniform==F(27,49) and var_uniform<F(9,16)
assert F(9,100)-F(4,5)*h-h*h>F(7,80)
curvature=-F(400,9)+F(300,7)
assert curvature==-F(100,63)
results={'atanh_terms':12,'center_log_square_upper':str(upper),
         'center_log_square_upper_float':float(upper),'center_target':'19/40',
         'atom_log_certificates':cert,
         'half_interval':str(h),'max_log_density_change':str(theta),
         'uniform_variance_bound':str(var_uniform),
         'uniform_entropy_second_derivative_bound':str(curvature)}
with open('computations/C024/strong_certificate.json','w') as f:
    json.dump(results,f,indent=2)
print(json.dumps({k:v for k,v in results.items() if k not in ['atom_log_certificates','center_log_square_upper']},indent=2))
