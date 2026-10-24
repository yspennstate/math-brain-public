from pathlib import Path
from fractions import Fraction as F
import json, numpy as np
from scipy.integrate import quad
from scipy.special import betaln
ROOT=Path(__file__).resolve().parent
# Exact polynomial integrations, independent of claimant's checks.
def integral(poly): return sum((c/F(i+1) for i,c in enumerate(poly)),F(0))
def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b): out[i+j]+=x*y
 return out
r=[F(0),F(-1),F(1)]
er=integral(r); er2=integral(mul(r,r))
exact_lhs=2*(er2-er*er)
exact_k=integral(mul([F(0),F(1),F(-1)],mul([F(-1),F(2)],[F(-1),F(2)])))
assert exact_lhs==F(1,90) and exact_k==F(1,30)
# Signed piecewise linear derivative with thin endpoint spikes and a flat interval.
knots=np.array([0,1e-5,3e-5,.01,.1,.4,.6,.9,.99,.99997,.99999,1.])
slopes=np.array([12000.,-7000.,50.,-3.,2.,0.,-1.,4.,-40.,8000.,-9000.])
rv=np.r_[0,np.cumsum(np.diff(knots)*slopes)]
hv=np.r_[0,np.cumsum(np.diff(knots)*np.abs(slopes))]
def R(x): return np.interp(x,knots,rv)
def H(x): return np.interp(x,knots,hv)
rng=np.random.default_rng(1040334)
u=rng.uniform(size=200000); v=rng.uniform(size=200000)
excess=np.abs(R(v)-R(u))-np.abs(H(v)-H(u))
assert excess.max()<1e-12
# Deterministic quadrature of order-statistic expectations. Split at all knots
# and at the crossing u=t to integrate absolute powers accurately.
nodes,weights=np.polynomial.legendre.leggauss(24)
def rule(breaks):
 a=np.asarray(breaks[:-1]); b=np.asarray(breaks[1:])
 return ((a[:,None]+b[:,None])/2+(b-a)[:,None]/2*nodes).ravel(), ((b-a)[:,None]/2*weights).ravel()
un,uw=rule(knots)
results=[]
for p in [1.25,2.,4.]:
 k=sum(abs(s)**p*quad(lambda t:(t*(1-t))**(p/2),a,b,epsabs=1e-12)[0] for a,b,s in zip(knots[:-1],knots[1:],slopes))
 for n in [1,3,20]:
  lhs=0.
  for i in range(1,n+1):
   breaks=np.unique(np.r_[(i-1)/n,knots[(knots>(i-1)/n)&(knots<i/n)],i/n])
   tn,tw=rule(breaks)
   pdf=np.exp((i-1)*np.log(un)+(n-i)*np.log1p(-un)-betaln(i,n-i+1))
   lhs+=np.sum(np.abs(R(un)[:,None]-R(tn)[None,:])**p*(uw*pdf)[:,None]*tw[None,:])
  lhs*=n**(p/2)
  rhs=(5*p)**p*k
  assert lhs<=rhs
  results.append({'p':p,'n':n,'expected_norm_power_quadrature':float(lhs),'K':k,'rhs':rhs,'lhs_over_rhs':float(lhs/rhs)})
# Check the inverse identity at grid boundaries including t=0,1.
errors=[]
for n in [1,3,20,300]:
 order=np.sort(rng.uniform(size=n))
 t=np.unique(np.r_[np.linspace(0,1,1001),np.arange(n+1)/n])
 idx=np.clip(np.ceil(n*t).astype(int)-1,0,n-1)
 vn=order[idx]; gn=np.searchsorted(order,vn,side='right')/n
 alpha=np.sqrt(n)*(gn-vn); beta=np.sqrt(n)*(vn-t)
 errors.append(float(np.max(np.abs(beta+alpha))))
 assert errors[-1]<=1/np.sqrt(n)+1e-12
report={'exact_signed_quadratic_n1':{'E_norm_squared':str(exact_lhs),'K2':str(exact_k)},'pathwise_pairs':len(u),'maximum_domination_excess':float(excess.max()),'quadrature':results,'inverse_errors':errors,'qualification':'Finite deterministic quadrature and random spot checks do not prove weak convergence; analytic argument audited separately.'}
(ROOT/'independent_checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
