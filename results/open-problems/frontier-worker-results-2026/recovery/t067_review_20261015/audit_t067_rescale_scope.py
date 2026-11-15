"""Own exact nine-pair check of the rescale scope defect and valid identity."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
from itertools import product
import json,hashlib
HERE=Path(__file__).resolve().parent
e=F(1,100)
atoms=[tuple(2*e if i==j else -e for i in range(3)) for j in range(3)]
def law(inputs,r):
    out={}
    for a,b in product(inputs,repeat=2):
        v=[(1+r*a[i])*(1+r*b[i]) for i in range(3)]
        total=sum(v); assert total>0
        posterior=tuple(3*x/total-1 for x in v)
        mass=total/27
        out[posterior]=out.get(posterior,F(0))+mass
    assert sum(out.values())==1
    return out
def U(dist):return sum(prob*sum(x*x for x in a)**2 for a,prob in dist.items())
M=6*e*e;inputU=M*M
r=F(9,10)
actual=U(law(atoms,r));rhs=2*r**4*inputU+F(3,5)*M*M
assert actual>rhs
lam,eta=F(4,5),F(9,10)
scaled=[tuple(lam*x/eta for x in a) for a in atoms]
assert law(atoms,lam)==law(scaled,eta),'Identity R failed'
ref=F(2887,5000);lam=F(1,2)
restricted_rhs=2*lam**4*inputU+F(3,5)*(lam/ref)**4*M*M
restricted_actual=U(law(atoms,lam))
assert restricted_actual<=restricted_rhs
out={'at':datetime.now().astimezone().isoformat(),
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'status':'PASS independent exact reproduction of scope defect; unrestricted identity R still valid',
    'wrong_corollary_case':{'lambda':str(r),'eta':str(r),'U_actual':str(actual),
        'U_claimed_upper':str(rhs),'strict_positive_difference':str(actual-rhs)},
    'R_entire_law_equality_case':{'lambda':'4/5','eta':'9/10','checked':True},
    'restricted_corollary_control':{'lambda':'1/2','eta':str(ref),
        'slack':str(restricted_rhs-restricted_actual)},
    'scope':'Nine exact observation pairs, full unconditional likelihood weights, total mass one; source range restriction must be checked in the analytic theorem. No assertion that degree156 is false or passed.'}
(HERE/'T067_RESCALE_SCOPE_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':out['status'],'difference':str(actual-rhs)}))
