"""Independent polynomial logit-operator and whole-simplex sign audit."""
from pathlib import Path
from datetime import datetime
import hashlib,json,time
import sympy as s
HERE=Path(__file__).resolve().parent;W=Path('~/brain_workers/w682')
started=time.monotonic();R=s.Rational
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
proof=W/'proofs/T067-COMPENSATED-CUBIC-001_v1.md'
digest=sha(proof)
a,b=s.symbols('a b');p=[a,b,1-a-b]
def D(i,f):
    return s.Poly(s.expand(a*(int(i==0)-p[i])*s.diff(f,a)+b*(int(i==1)-p[i])*s.diff(f,b)),a,b).as_expr()
def ell(i,f):
    j,k=[j for j in range(3) if j!=i]
    third=sum(D(q,D(q,D(q,f))) for q in range(3))
    cross=D(j,D(j,f))-2*D(j,D(k,f))+D(k,D(k,f))
    return s.expand((third-D(i,f)-cross)/4)
def S(f):return s.expand(sum(p[i]*ell(i,f) for i in range(3)))
dev=[3*q-1 for q in p];A=s.expand(sum(q*q for q in dev));J=s.expand(sum(q**3 for q in dev))
SA=S(A);SQ=S(A*A)
assert s.expand(SA+(6-A)*(A-J)/18)==0
assert s.expand(SQ-(4*A-4*A*A+R(2,3)*A**3+J*(-2+3*A-R(5,9)*A*A)))==0
# Verify the calibration identity needed by H_i=Q+9 beta F_i;
# differentiating radial Q+beta A alone is not a substitute for this.
assert s.expand(SA-9*sum(p[i]*ell(i,p[i]) for i in range(3)))==0
e2=sum(p[i]*p[j] for i in range(3) for j in range(i+1,3));e3=p[0]*p[1]*p[2]
assert s.expand(J+3-R(3,2)*A-81*e3)==0
disc=s.prod((dev[i]-dev[j])**2 for i in range(3) for j in range(i+1,3))/3
assert s.expand(A**3/6-J*J-disc)==0
X,T=s.symbols('X T');beta=R(49,4)
C=(4-beta/3)*X+(-4+beta/18)*X*X+R(2,3)*X**3
B=beta/3-2+(3-beta/18)*X-R(5,9)*X*X
upper=s.expand((C+B*6*T**3).subs(X,6*T*T))
square=-2*T*T*(1-T)**2*(48*(T-R(23,384))**2+R(239,3072)+60*T**3)
assert s.expand(upper-square)==0
lower=s.expand(C+B*(R(3,2)*X-3))
assert s.expand(lower+(6-X)**2*(24*X+25)/144)==0
assert sha(proof)==digest,'Source changed during audit'
out={'at':datetime.now().astimezone().isoformat(),'status':'PASS exact operator identities and analytic whole-simplex two-case sign',
     'proof_sha256':digest,'script_sha256':sha(Path(__file__)),
     'identities':['S_A','S_Q','S_A=9 sum p ell(F_i)','simplex cubic/product identity','discriminant','B>=0 square factorization','B<0 boundary factorization'],
     'scope':'Compensated cubic sign only; does not certify fourth derivatives, replacement errors, Gaussian fourth moment, or cutoff91. Lead account4 is not a distinct-account second receipt.',
     'seconds':time.monotonic()-started}
(HERE/'T067_COMPENSATED_CUBIC_LEAD_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps(out))
