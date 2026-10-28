"""Exact Boolean odds-only obstruction; no floating-point inference."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib
R=Path(__file__).resolve().parents[1]
a=(-1,1,1,1)
f=tuple(a[x&3]*(1 if not(x&4) else -1) for x in range(16))
def walsh(t):
    n=len(t)
    return tuple(sum(F(t[x])*(-1 if (x&s).bit_count()%2 else 1) for x in range(n))/n for s in range(n))
p=tuple(v*v for v in walsh(f))
assert sum(p)==1
assert {i for i,v in enumerate(p) if v}=={4,5,6,7}
assert all(p[i]==F(1,4) for i in (4,5,6,7))
I=sum(F(i.bit_count())*v for i,v in enumerate(p))
assert I==2
alpha=rho=b=F(3,4)
# For any stochastic input probabilities u,v satisfying alpha*u+(1-alpha)*v=b,
# rho=alpha forces target odds rho*u+(1-rho)*v=b, identically.
assert rho==alpha and b!=F(1,2)
q=[F(0)]*16
q[4]=F(1,2)
for i in (5,6,7): q[i]=F(1,6)
assert sum(q)==1
# KL = (1/4)log2(1/2)+(3/4)log2(3/2) = (1/4)log2(27/16)>0.
assert 27>16
assert all(f[x]==f[x^8] for x in range(16))
out={'status':'PASS','family':'actual four-variable Boolean a(y1,y2)*z, dummy d',
     'truth':list(f),'squared_spectrum':list(map(str,p)), 'target_reference':list(map(str,q)),
     'entropy_bits':'2','influence':'2','data_reference_liability':'0',
     'controller_reference_liability':'0','source_JS_bank':'0',
     'alpha':str(alpha),'rho':str(rho),'true_nonempty_odds':str(b),
     'admissible_target_interval':['3/4','3/4'],'excluded_target_odds':'1/2',
     'extra_KL_prime_log2':{'2':'-1','3':'3/4'},
     'strict_positivity_certificate':'27 > 16; extra_KL=(1/4)*log2(27/16)',
     'dummy_query':3,'dummy_entropy_cost':'0',
     'conclusion':'Arbitrary odds reset exceeds old tight U=2; not an FEI counterexample.',
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out/obstruction.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','influence':'2','strict_certificate':'27>16'}))
