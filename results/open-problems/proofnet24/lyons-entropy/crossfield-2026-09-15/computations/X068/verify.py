"""Exact algebra for X068; decimal optimum is a separate diagnostic."""
import json
from pathlib import Path
import sympy as s
import numpy as np
from scipy.linalg import eigvals
from scipy.optimize import brentq

checks = []
def check(name, expr):
    assert s.simplify(expr) == 0, (name, s.simplify(expr))
    checks.append(name)

u, up, hr, hi = s.symbols('u up hr hi', positive=True)
check('Pauli X actual atom Fisher',
      (up/2+hr)**2/(u/2)+(up/2-hr)**2/(u/2)-up**2/u-4*hr**2/u)
check('Pauli Y actual atom Fisher',
      (up/2+hi)**2/(u/2)+(up/2-hi)**2/(u/2)-up**2/u-4*hi**2/u)
y,z,yp,zp=s.symbols('y z yp zp',positive=True)
check('original contrast exact loss',yp**2/y+zp**2/z-(yp+zp)**2/(y+z)
      -(z*yp-y*zp)**2/(y*z*(y+z)))

alpha,gamma,b,t,v,zr,zi=s.symbols('alpha gamma b t v zr zi',positive=True)
sig=alpha*gamma
eta=b+sig
k=eta/sig
d1=(t+v)/alpha;d2=(t-v)/gamma
detE=d1*d2-(zr*zr+zi*zi)/sig
C=alpha**2*d1**2+2*b*d1*d2+gamma**2*d2**2
check('Lorentz normalization',sig*detE-t*t+v*v+zr*zr+zi*zi)
check('count uncertainty norm',C-2*eta*detE-4*v*v-2*k*(zr*zr+zi*zi))

# Generic rational Schur completion, with epsilon at its defining root.
eps,g0=s.symbols('eps g0',positive=True)
ds=s.symbols('d0:3',positive=True)
gs=s.symbols('g0v:3',real=True)
rs=s.symbols('r0:3',real=True)
c=sum(gs[i]**2/(ds[i]+eps) for i in range(3))
a=g0/(1+c)
r0=[a*gs[i]/(ds[i]+eps) for i in range(3)]
# Verify entries, avoiding expansion of a large rational expression.
for i in range(3):
    check(f'Schur cross entry {i}',(ds[i]+eps)*r0[i]+gs[i]*sum(gs[j]*r0[j] for j in range(3))-g0*gs[i])
check('Schur constant',sum((ds[i]+eps)*r0[i]**2 for i in range(3))
      +sum(gs[i]*r0[i] for i in range(3))**2-g0*g0*c/(1+c))
check('monotone root derivative',s.diff(eps*(1+c),eps)
      -1-sum(gs[i]**2*ds[i]/(ds[i]+eps)**2 for i in range(3)))

lam=s.Rational(1,5);mu=s.Rational(3,5)
cs=s.Rational(3,5);sn=s.Rational(4,5)
V=s.Matrix([[cs,sn],[-sn,cs]])
J=V*s.diag(lam,mu)*V.T
w=s.factor(J.det());x=s.factor((s.eye(2)-J).det());u0=1-x-w
B=J-w*s.eye(2)
y0,z0=B[0,0],B[1,1]
check('rational basis unitary',sum((V.T*V-s.eye(2)).applyfunc(lambda q:q*q)))
check('measured J11',J[0,0]-s.Rational(57,125))
check('measured J22',J[1,1]-s.Rational(43,125))
check('measured coherence',J[0,1]-s.Rational(24,125))
check('one particle total',u0-s.Rational(14,25))
check('one particle first',y0-s.Rational(42,125))
check('one particle second',z0-s.Rational(28,125))

G11=(1-mu)**2/x+mu**2/w+(1-2*mu)**2/u0
G22=(1-lam)**2/x+lam**2/w+(1-2*lam)**2/u0
G12=(1-mu)*(1-lam)/x+mu*lam/w+(1-2*mu)*(1-2*lam)/u0
check('count diagonal one',G11-s.Rational(25,7))
check('count diagonal two',G22-s.Rational(125,42))
check('count cross',G12-1/u0)
al=s.sqrt(G11);ga=s.sqrt(G22);sg=al*ga;et=G12+sg;kk=et/sg
q1,q2,qr,qi=s.symbols('q1 q2 qr qi',real=True)
Ee=s.Matrix([[q1,qr+s.I*qi],[qr-s.I*qi,q2]])
Em=V*Ee*V.T
wp=mu*q1+lam*q2
Bp=Em-wp*s.eye(2)
contrast=s.expand((z0*Bp[0,0]-y0*Bp[1,1])/s.sqrt(u0*y0*z0))
normcontrast=s.expand(contrast.subs({q1:(t+v)/al,q2:(t-v)/ga,qr:zr/s.sqrt(sg),qi:zi/s.sqrt(sg)}))
gg=[normcontrast.coeff(q) for q in (t,v,zr,zi)]
check('no unobserved imaginary contrast',gg[3])
check('measured strict gain contrast',gg[0]-(28/ga-42/al)/(625*s.sqrt(u0*y0*z0)))
check('strict gain witness',4*G11-9*G22+s.Rational(25,2))
# In this example g0=0 would force 2*alpha=3*gamma, impossible by this rational identity.
assert 4*G11 != 9*G22
checks.append('strict coefficient gain is exact')

gn=np.array([float(q.evalf()) for q in gg])
en=float(et);snorm=float(sg);kn=float(kk)
fun=lambda ep:ep*(1+gn[1]**2/(4+ep)+(gn[2]**2+gn[3]**2)/(2*kn+ep))-gn[0]**2
ep=brentq(fun,0,gn[0]**2+1e-12,xtol=1e-15)
beta=en+snorm*ep/2
dn=np.array([4.,2*kn,2*kn])
gaplower=snorm*gn[0]**2/(2*(1+np.sum(gn[1:]**2/dn)))
# Independent derivative construction in the original measured basis.
a0=float(J[0,0]);b0=float(J[1,1]);r0n=float(J[0,1]);wf=a0*b0-r0n*r0n
atoms=np.array([1-a0-b0+wf,a0-wf,b0-wf,wf])
jets=np.array([[-(1-b0),-(1-a0),-2*r0n],[1-b0,-a0,2*r0n],[-b0,1-a0,2*r0n],[b0,a0,-2*r0n]])
G=jets.T@np.diag(1/atoms)@jets
Lorentz=np.array([[0.,1.,0.],[1.,0.,0.],[0.,0.,-2.]])
ev=eigvals(G,Lorentz)
positive=[q.real for q in ev if abs(q.imag)<1e-9 and q.real>0]
assert len(positive)==1 and abs(positive[0]-beta)<1e-10

# Exact failure of FI transfer to the complementary experiment at a product base.
prodJ=s.diag(lam,mu);prodE=s.Matrix([[0,1],[1,0]])
check('product full determinant first jet',s.diff((prodJ+s.Symbol('q')*prodE).det(),s.Symbol('q')).subs(s.Symbol('q'),0))
check('positive complementary Fisher',4/u0-s.Rational(50,7))

result={'status':'PASS','exact_assertions':len(checks),'assertions':checks,
        'rational_example':{'J':str(J),'atoms':[str(q) for q in (x,y0,z0,w)]},
        'decimal_diagnostic_only':{'count_eta':en,'sharp_measured_beta':beta,
            'proved_formula_lower_bound_on_gain_evaluation':gaplower,
            'independent_generalized_eigenvalue':positive[0]},
        'scope':'Exact two-site measured coefficient; three-site joint uncertainty comparison remains open.'}
Path(__file__).with_name('verified_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='assertions'},indent=2))
