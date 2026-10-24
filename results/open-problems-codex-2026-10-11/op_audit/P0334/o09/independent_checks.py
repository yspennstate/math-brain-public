import json, math
from fractions import Fraction as F
import numpy as np
from scipy.integrate import quad
from scipy.special import beta
root=Path.cwd() if False else None
# Exact order-statistic moment computation, not Monte Carlo.
exact=[]
for n in [1,2,3,10,100]:
    total=F(0)
    for i in range(1,n+1):
        a,b=F(i-1,n),F(i,n)
        mean=F(i,n+1); second=F(i*(i+1),(n+1)*(n+2))
        total+=second*(b-a)-mean*(b*b-a*a)+(b**3-a**3)/3
    assert n*total==F(1,6)
    exact.append({'n':n,'n_E_norm2':str(n*total),'K2':str(F(1,6))})
# Signed quadratic n=1: r=t-t^2, E double difference squared=2 Var(r).
mean=F(1,2)-F(1,3)
second=F(1,3)-2*F(1,4)+F(1,5)
variance=second-mean**2
K2=F(1,2)-5*F(1,3)+8*F(1,4)-4*F(1,5)
assert 2*variance==F(1,90) and K2==F(1,30)
# A continuous signed piecewise-linear function, sharp endpoint spikes, flat pieces.
x=np.array([0,1e-5,.003,.03,.17,.4,.55,.8,.98,.999,1.])
slope=np.array([500.,-25.,0.,3.,-1.,0.,5.,-10.,40.,-300.])
y=np.r_[0,np.cumsum(slope*np.diff(x))]
h=np.r_[0,np.cumsum(np.abs(slope)*np.diff(x))]
def interp(z,values):return np.interp(z,x,values)
def power_integral(v0,v1,length,p):
    if v0==v1:return length*abs(v0)**p
    return length*(np.sign(v1)*abs(v1)**(p+1)-np.sign(v0)*abs(v0)**(p+1))/((p+1)*(v1-v0))
def exact_norm(u,p,values):
    n=len(u);cuts=np.unique(np.r_[x,np.arange(n+1)/n]);a,b=cuts[:-1],cuts[1:]
    idx=np.minimum((n*((a+b)/2)).astype(int),n-1)
    rv=interp(u[idx],values);ra=interp(a,values);rb=interp(b,values)
    return n**(p/2)*sum(power_integral(c-d,c-e,l,p) for c,d,e,l in zip(rv,ra,rb,b-a))
rng=np.random.default_rng(33409);max_excess=0.;max_norm_excess=0.;cases=[]
for p in [1.25,1.5,2.,4.]:
    K=sum(abs(s)**p*quad(lambda t:(t*(1-t))**(p/2),a,b,epsabs=1e-11)[0] for s,a,b in zip(slope,x[:-1],x[1:]))
    for n in [1,3,16,64]:
        moments=[]
        for rep in range(150):
            u=np.sort(rng.uniform(size=n))
            nr=exact_norm(u,p,y);nh=exact_norm(u,p,h)
            max_norm_excess=max(max_norm_excess,nr-nh)
            moments.append(nr)
            v,w=rng.uniform(size=(2,100))
            ex=np.abs(interp(v,y)-interp(w,y))-np.abs(interp(v,h)-interp(w,h))
            max_excess=max(max_excess,float(ex.max()))
        cases.append({'p':p,'n':n,'K':K,'MC_E_norm_p':float(np.mean(moments)),'bound':(5*p)**p*K})
assert max_excess<1e-10 and max_norm_excess<1e-8
assert all(c['MC_E_norm_p']<c['bound'] for c in cases)
# Independent endpoint exponent re-derivation for Q=-t^-a.
# Kp=a^p Beta(1-p(a+1/2),1+p/2), finite iff a<1/p-1/2.
p,a=1.5,.1;K=a**p*beta(1-p*(a+.5),1+p/2)
results={'exact_uniform':exact,'signed_quadratic':{'n1_E_norm2':str(2*variance),'K2':str(K2)},'piecewise_cases':cases,'point_comparisons':240000,'max_domination_excess':max_excess,'max_integrated_domination_excess':max_norm_excess,'power_endpoint':{'p':p,'a':a,'Kp':K,'threshold_a':1/p-.5},'note':'Numerics are finite checks, not a proof of the theorem.'}
from pathlib import Path
Path('independent_checks.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in results.items() if k!='piecewise_cases'},indent=2))
