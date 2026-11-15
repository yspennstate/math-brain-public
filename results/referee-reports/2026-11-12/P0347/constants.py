"""Independent exact-rational and quadrature checks of limiting constants."""
from common import log
import mpmath as mp, json, math
from fractions import Fraction as F
mp.mp.dps=60
z=mp.zeta(2);entropy=lambda x: -x*mp.log(x)-(1-x)*mp.log(1-x)
nu=lambda x:1/(2*x*(1-x))
integ=lambda f:mp.quad(f,[0,mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75'),1])
kappa=(2*mp.zeta(3)-z)/z**2
kappa_quad=integ(lambda x:entropy(x)**2*nu(x))/z**2
assert abs(kappa-kappa_quad)<mp.mpf('1e-50')
J3=6*mp.zeta(4)-3*mp.zeta(3)-mp.mpf('1.5')*z
J3_quad=integ(lambda x:entropy(x)**3*nu(x))
assert abs(J3-J3_quad)<mp.mpf('1e-50')
a3=kappa/z-2*J3/(3*z**3)
H2poly=integ(lambda x:entropy(x)**2*(x*x+(1-x)**2)*nu(x))
H4=integ(lambda x:entropy(x)**4*nu(x))
a4=(kappa*kappa/2+3*a3/z+6*kappa*H2poly/z**2+H4/z**4)/(mp.mpf(11)/6)
def entropy_integral_beta(r):
    value=-2*mp.polygamma(r,r)
    for j in range(1,r):
        value+=math.comb(r,j)*mp.diff(lambda u,v:mp.beta(u,v),(mp.mpf(j),mp.mpf(r-j)),(j,r-j))
    return (-1)**r*value/2
H4_beta=entropy_integral_beta(4)
H2dx=mp.mpf(4)/27+2*mp.diff(lambda u,v:mp.beta(u,v),(mp.mpf(2),mp.mpf(2)),(1,1))
H2poly_beta=(2*mp.zeta(3)-z)-H2dx
a4_beta=(kappa*kappa/2+3*a3/z+6*kappa*H2poly_beta/z**2+H4_beta/z**4)/(mp.mpf(11)/6)
assert abs(a4_beta-a4)<mp.mpf('1e-50')
q=[F(1)]
for k in range(1,17):
    h=sum((F(1,i) for i in range(1,2*k)),F(0))
    value=k*q[k-1]
    for j in range(1,k):
        beta=F(math.factorial(2*j-1)*math.factorial(2*(k-j)-1),math.factorial(2*k-1))
        value+=math.comb(k,j)*q[j]*q[k-j]*beta/2
    q.append(value/h)
def dec(x):return mp.mpf(x.numerator)/x.denominator
v=q[2]-1;c3=q[3]-3*q[2]+2;c4=q[4]-4*q[3]+6*q[2]-3
# Independent quadrature recurrence, not beta-function evaluation.
qq=[mp.mpf(1)]
for k in range(1,5):
    psi=integ(lambda x:(1-x**(2*k)-(1-x)**(2*k))*nu(x))
    value=k*qq[k-1]
    for j in range(1,k):value+=math.comb(k,j)*qq[j]*qq[k-j]*integ(lambda x:x**(2*j)*(1-x)**(2*(k-j))*nu(x))
    qq.append(value/psi)
assert max(abs(qq[k]-dec(q[k])) for k in range(5))<mp.mpf('1e-50')
# Conjectural centered Sackin fixed-point moments, for comparison only.
w=[mp.mpf(1),mp.mpf(0)]
for k in range(2,5):
    val=k*w[k-1]
    for j in range(k+1):
        for r in range(k-j+1):
            ell=k-j-r
            if j==k or r==k or w[j]==0 or w[r]==0:continue
            coef=math.factorial(k)//(math.factorial(j)*math.factorial(r)*math.factorial(ell))
            val+=coef*w[j]*w[r]*integ(lambda x:x**j*(1-x)**r*(-entropy(x)/z)**ell*nu(x))
    w.append(val/sum(mp.mpf(1)/j for j in range(1,k)))
assert abs(a3-w[3])<mp.mpf('1e-50') and abs(a4-w[4])<mp.mpf('1e-50')
out={'kappa_S_C':str(kappa),'kappa_quadrature':str(kappa_quad),'QC_raw_moments':[str(v) for v in q], 'QC_variance':str(v),'QC_skewness':str(dec(c3)/dec(v)**mp.mpf('1.5')),'QC_kurtosis':str(dec(c4)/dec(v)**2),'S_centered_moments':[str(v) for v in w],'S_skewness':str(w[3]/w[2]**mp.mpf('1.5')),'S_kurtosis':str(w[4]/w[2]**2),'J3':str(J3),'S_a3_independent':str(a3),'S_a4_independent':str(a4),'S_a4_beta_derivatives':str(a4_beta)}
with open('constants.json','w') as f:json.dump(out,f,indent=2)
log('Constants checked by exact beta integrals and independent quadrature: '+json.dumps(out))
