#!/usr/bin/env python3
# NUMERICAL SCOUT ONLY -- not a rigorous certificate.
import math, numpy as np
from scipy.integrate import quad
from scipy.optimize import root
from scipy.special import ndtr
KAPPA=-1.0

def relations(p,q):
    r=math.sqrt(p/q)
    gp=.5*(1-q)/(1-p)*r
    c=r/(1-p)-(1/r)/(1-q)
    D=2*gp-c*(1-q)
    return gp,c,D

def inner_f(z,p,c,gamma):
    mu=math.sqrt(p)*z+KAPPA
    sig=math.sqrt(1-p)
    B=c/(4*gamma)
    A=1+2*B*sig*sig
    return ndtr(-mu/sig)+math.exp(-B*mu*mu/A)*ndtr(mu/(sig*math.sqrt(A)))/math.sqrt(A)

def elog(p,c,gamma):
    fun=lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi)*math.log(inner_f(z,p,c,gamma))
    return quad(fun,-10,10,epsabs=1e-11,epsrel=1e-11,limit=200)[0]

def psi(x,alpha):
    p,q,gamma=x
    gp,c,D=relations(p,q)
    return .5*(1-p*q)*c-gp+math.log(D/(2*gp))/(2*c)-q/(2*D)+gamma-(alpha/c)*elog(p,c,gamma)

def grad(x,alpha,h=5e-6):
    ans=[]
    for i in range(3):
        xp=x.copy(); xm=x.copy(); xp[i]+=h; xm[i]-=h
        ans.append((psi(xp,alpha)-psi(xm,alpha))/(2*h))
    return np.array(ans)

for alpha,x0 in [
    (12.32,np.array([.6649,.2780,.1500])),
    (12.50,np.array([.6563,.2796,.1589])),
]:
    sol=root(lambda x: grad(x,alpha,2e-5),x0,tol=1e-10)
    p,q,gamma=sol.x
    gp,c,D=relations(p,q)
    print('alpha',alpha,'success',sol.success)
    print('p q gamma c gamma_p =',p,q,gamma,c,gp)
    print('reduced gradient =',grad(sol.x,alpha))
    print('psi =',psi(sol.x,alpha))
    print()
print('NUMERICAL_ONLY')
