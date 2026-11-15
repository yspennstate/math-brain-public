"""Rebuild the continuum prefix-drift certificate from its displayed sums."""
from pathlib import Path
from datetime import datetime
from fractions import Fraction as F
from math import comb
import hashlib,json,time
import sympy as S
HERE=Path(__file__).resolve().parent
W=Path('~/brain_workers/w682')
started=time.monotonic()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
proof=W/'proofs/T067-LOCAL-RADIUS5-001_v1.md'
assert sha(proof)=='517e75594c92240c4f1202a0cd5f734e92643ee22562dbb020b82ddda27c4e5a'
l,r,z=S.symbols('l r z');R=S.Rational
w=l*l;D=1-w;K=r+2*(1-r)*w
N=R(5,2)*(K*(K-w)+2*(1-K));J=(1+l)*N/3
H1=K*(K-w)-2*w*w;H2=K*(K-w)*(K-2*w)
# These are D^3 times A_k and B_k, derived by summing the printed
# prefix recurrence; no producer polynomial or evaluator is imported.
abar=N*w**3*D/9+D**3*H2/216
abar+=(N*H1*w*(1-l)*(1+l)**2/2+5*H2*(1-l)**2*(1+l)**3/12)/9
bbar=(3*J**2*w**3+l*N*J*w**3+N**2*w**4/12)/9
bbar+=(3*l*J+N*w/2)*(l*J*H1*(1+l)/2+5*H2*(1-l)*(1+l)**2/18)/9
bbar+=(l*J/2+N*w/12)*(N*w*H1*(1+l)/2+5*H2*(1-l)*(1+l)**2/6)/9
g=K*(K-w)/12
p=S.Poly(S.expand((8640000*(R(999,1000)*g*D**3-R(217,500)*abar-R(217,500)**2*bbar)).subs(l,R(559017,1250000)*z)),z,r)
assert p.degree_list()==(17,6)
coef={ij:F(int(v.p),int(v.q)) for ij,v in p.terms()}
bern={}
for i in range(18):
    for j in range(7):
        bern[i,j]=sum((v*F(comb(i,a),comb(17,a))*F(comb(j,b),comb(6,b))
                       for (a,b),v in coef.items() if a<=i and b<=j),F(0))
assert min(bern.values())>=0
positive=sum(v>0 for v in bern.values());zeros=sum(v==0 for v in bern.values())
assert positive==120 and zeros==6
assert 5*559017**2>1250000**2 and R(559017,1250000)<R(2887,5000)
out={'at':datetime.now().astimezone().isoformat(),'status':'PASS independent exact full-rectangle certificate; conditional on reviewed fusion/prefix criterion',
     'proof_sha256':sha(proof),'script_sha256':sha(Path(__file__)),
     'base_criterion_sha256':sha(W/'proofs/T067-UNIFORM-LOCAL-001_v1.md'),
     'degrees':[17,6],'positive':positive,'zero':zeros,
     'minimum_positive':str(min(v for v in bern.values() if v>0)),
     'power_coefficients':{str(k):str(v) for k,v in coef.items()},
     'bernstein_coefficients':{str(k):str(v) for k,v in bern.items()},
     'scope':'Local symmetric calibrated critical fixed points only, x<=217/4500, every integer d>=5. No global entry or degree6 admission. Lead account4 does not provide a distinct-account second receipt.',
     'seconds':time.monotonic()-started}
(HERE/'T067_LOCAL5_LEAD_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps({k:out[k] for k in ['status','positive','zero','minimum_positive','seconds']}))
