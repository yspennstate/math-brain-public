import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq
from scipy.special import ndtr, log_ndtr
from scipy.stats import multivariate_normal

print("PROB10-03 ANALYTICAL SELF-CHECK + NUMERICAL SCOUT")
print("All overlap/facet optimization values below are NUMERICAL_ONLY.")

p,D,B,alpha,IB,C = sp.symbols("p D B alpha IB C", positive=True)
c=(1-D**2)/(D*(1-p)*(1-p*D**2))
cd=sp.simplify(sp.diff(c,D))
cd_claim=(1+D**2*(1-3*p)+p*D**4)/(D**2*(p-1)*(1-p*D**2)**2)
assert sp.simplify(cd-cd_claim)==0
num=1+D**2*(1-3*p)+p*D**4
factor=(1-D**2)*(1-p*D**2)+2*(1-p)*D**2
assert sp.expand(num-factor)==0
poly=C*p*(1-p)*D**3-D**2-C*(1-p)*D+1
cleared=sp.cancel((c-C)*D*(1-p)*(1-p*D**2))
assert sp.expand(cleared-poly)==0
gamma=c/(4*B)
R1=IB+4*gamma**2/alpha
R1_alt=IB+c**2/(4*alpha*B**2)
assert sp.simplify(R1-R1_alt)==0
print("EXACT_2D_COMPILER_ALGEBRA_PASS")

p0=0.656313184757223
D0=0.652653689820474
g0=0.158861855012242
alpha0=12.5
IB0=-0.008075868472937753
def cfun(p,D):
    return (1-D*D)/(D*(1-p)*(1-p*D*D))
c0=cfun(p0,D0)
B0=c0/(4*g0)
C0=2*B0*math.sqrt(-alpha0*IB0)
g1=0.5*math.sqrt(-alpha0*IB0)
print("NUMERICAL_ONLY alpha12.5 p B =", repr(p0), repr(B0))
print("NUMERICAL_ONLY compiler |C-c| =", abs(C0-c0))
print("NUMERICAL_ONLY compiler |gamma_recovered-gamma| =", abs(g1-g0))

def logphi(t):
    return -0.5*t*t-0.5*math.log(2*math.pi)
def invmills_upper(t):
    return math.exp(logphi(t)-log_ndtr(-t))
def stationarity_for_b(b):
    A=1+2*b
    s=1/math.sqrt(A)
    def mean_mu(mu):
        t=(-1-mu)/s
        return mu+s*invmills_upper(t)
    grid=np.linspace(-20,5,1001)
    vals=[mean_mu(float(x)) for x in grid]
    lo=hi=None
    for x0,x1,y0,y1 in zip(grid[:-1],grid[1:],vals[:-1],vals[1:]):
        if y0==0 or y0*y1<0:
            lo=float(x0); hi=float(x1); break
    if lo is None:
        raise RuntimeError("no stationarity bracket")
    mu=brentq(mean_mu,lo,hi)
    a=-mu*A
    t=(-1-mu)/s
    lam=invmills_upper(t)
    var=s*s*(1+t*lam-lam*lam)
    r=var-1
    local=1/(r*r)
    return a,mu,s,r,local
def m0_ab(a,b):
    A=1+2*b
    s=1/math.sqrt(A)
    mu=-a/A
    factor=(1/math.sqrt(A))*math.exp(a*a/(2*A))
    return factor*ndtr((mu+1)/s)
def e_ab_q(a,b,q):
    S=np.array([[1.0,q],[q,1.0]])
    P=np.linalg.inv(S)+2*b*np.eye(2)
    Cmat=np.linalg.inv(P)
    one=np.ones(2)
    mu=-Cmat@(a*one)
    factor=(np.linalg.det(S)**-0.5)*(np.linalg.det(P)**-0.5)
    factor*=math.exp(0.5*a*a*(one@Cmat@one))
    prob=multivariate_normal(mean=-mu,cov=Cmat).cdf([1.0,1.0])
    return factor*prob
def global_scout(b):
    a,mu,s,r,local=stationarity_for_b(b)
    m0=m0_ab(a,b)
    best=(float("inf"),None)
    for q in np.concatenate((np.linspace(-0.99,-0.01,120),np.linspace(0.01,0.99,120))):
        e=e_ab_q(a,b,float(q))
        lr=math.log(e/(m0*m0))
        if lr>1e-9:
            val=-0.5*math.log(1-q*q)/lr
            if val<best[0]:
                best=(val,float(q))
    return a,local,best
for b in (-0.24,0.0):
    a,local,best=global_scout(b)
    print("NUMERICAL_ONLY overlap b =",b,"a =",a,"local_ceiling =",local,
          "grid_global_ceiling =",best[0],"at_q =",best[1])

Phi1=ndtr(1.0)
def facet_entropy(alpha):
    return alpha*math.log(alpha)-(alpha-1)*math.log(alpha-1)
def facet_at_h1(alpha):
    return facet_entropy(alpha)-0.5+(alpha-1)*math.log(Phi1)
root=brentq(facet_at_h1,20.0,30.0)
print("NUMERICAL_ONLY facet exponent at current alpha_U =",
      facet_at_h1(12.78437096216))
print("NUMERICAL_ONLY facet h=1 crossing =",root)
print("ALL_SELF_CHECKS_PASS")
