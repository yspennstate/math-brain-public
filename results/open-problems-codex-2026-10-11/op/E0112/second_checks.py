"""Bounded deterministic checks of the second attempt's identities."""
from pathlib import Path
import json, math
import numpy as np
from scipy.stats import poisson, chi2
from numpy.polynomial.legendre import leggauss

# Explicit Gaussian joining error, equal to the L1 distance of two normals.
gaussian=[]
for d in [1,3,6]:
    for ratio in [0.01,0.1,0.24]:
        s=1-2*ratio
        A=s**(-d/2)
        crossing=math.log(A)*s/ratio
        exact=2*(chi2.cdf(crossing/s,d)-chi2.cdf(crossing,d))
        bound=A-1+A*d*ratio/s
        assert -1e-12<=exact<=bound+1e-12
        gaussian.append(dict(d=d,l_over_t=ratio,L1_error=exact,bound=bound))

# Two deterministic path tubes with shared volume c and exclusive volume a.
# This is a finite Poisson model, not a discretized Brownian polymer.
nodes,weights=leggauss(40)
nodes=(nodes+1)/2;weights=weights/2
counts=np.arange(81)
a,c=0.7,0.3

def halfmoment_and_derivative(h,beta):
    lam=math.expm1(beta)
    probs=poisson.pmf(counts,h*a)
    w=np.exp(beta*counts-h*lam*a)
    Z=(w[:,None]+w[None,:])/2
    root=np.sqrt(Z)
    joint=probs[:,None]*probs[None,:]
    affinity_shared=math.exp(-h*c*math.expm1(beta/2)**2/2)
    p1=w[:,None]/(w[:,None]+w[None,:]);p2=1-p1
    loss1=(np.sqrt(1+lam*p1)-1)**2
    loss2=(np.sqrt(1+lam*p2)-1)**2
    f=affinity_shared*float(np.sum(joint*root))
    rhs=0.5*affinity_shared*float(np.sum(joint*root*(
        c*math.expm1(beta/2)**2+a*(loss1+loss2))))
    return f,rhs

interpolation=[]
for beta in [-1.1,0,0.8,2]:
    f1,_=halfmoment_and_derivative(1,beta)
    integral=sum(float(w)*halfmoment_and_derivative(float(h),beta)[1]
                 for h,w in zip(nodes,weights))
    err=abs((1-f1)-integral)
    assert err<2e-10,(beta,err)
    interpolation.append(dict(beta=beta,deficit=1-f1,integrated_loss=integral,
                              absolute_error=err))

noise=[]
p,q,rho,mu=1.2,1.5,0.5,1.0
for k in [1,3,5,8,10]:
    ek=math.exp(k);z=1+rho*(ek-1)
    log_input=mu*((math.exp(p*k)-1)/p-(ek-1))
    log_output=mu*((z**q-1)/q-rho*(ek-1))
    noise.append(dict(k=k,log_norm_ratio=log_output-log_input))

for beta in [-1.1,0.8]:
    rho=0.4;lam=math.expm1(beta);beta1=math.log1p(rho*lam)
    for n in [0,1,3,8]:
        # Retention expectation in a single count, with immigrants integrated.
        lhs=(1+rho*lam)**n*math.exp(-rho*lam)
        rhs=math.exp(beta1*n-math.expm1(beta1))
        assert abs(lhs-rhs)<=1e-12*max(1,lhs,rhs)

out=dict(gaussian_joining=gaussian,two_tube_interpolation=interpolation,
         poisson_hypercontractivity_obstruction=noise,
         limitations="Floating-point checks, not interval certificates. Finite tubes are identity checks, not evidence of Brownian threshold equality.")
Path('second_numerical_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(dict(interpolation=interpolation,noise=noise),indent=2))
