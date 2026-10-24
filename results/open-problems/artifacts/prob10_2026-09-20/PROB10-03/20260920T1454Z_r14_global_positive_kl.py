#!/usr/bin/env python3
"""Numerical self-check for the exact positive thermodynamic compiler
K(t,a)=1/4 int_0^a s [q_s M4(s)-q_s^2 M2(s)^2] ds.
No value here is a source endpoint.
"""
import math
import numpy as np
from scipy.special import log_ndtr
from scipy.integrate import quad

def moments(t,s):
    r=1+s; mu=t/r; sig2=1/r; z=t/math.sqrt(r)
    mills=math.exp(-0.5*z*z-0.5*math.log(2*math.pi)-float(log_ndtr(z)))
    m1=mu+math.sqrt(sig2)*mills
    m2=mu*m1+sig2
    m3=mu*m2+2*sig2*m1
    m4=mu*m3+3*sig2*m2
    return m1,m2,m3,m4

def log_parts(t,s):
    r=1+s
    logA=float(log_ndtr(-t))
    logp=float(log_ndtr(t))
    logB=-0.5*math.log(r)-s*t*t/(2*r)+float(log_ndtr(t/math.sqrt(r)))
    logF=float(np.logaddexp(logA,logB))
    q=math.exp(logB-logF)
    return logA,logp,logB,logF,q

def qpos(t,s):
    return log_parts(t,s)[4]

def positive_path(t,a):
    def integrand(s):
        _,m2,_,m4=moments(t,s); q=qpos(t,s)
        return 0.25*s*(q*m4-q*q*m2*m2)
    return quad(integrand,0,a,epsabs=1e-13,epsrel=1e-13,limit=200)[0]

def sign_chain(t,a):
    logA,logp,logB,logF,q=log_parts(t,a)
    _,m2,_,_=moments(t,a)
    kplus=logp-logB-0.5*a*m2
    # Exact Bernoulli chain term, written without subtracting 1-p or 1-q.
    ber=(1-q)*(-logF)+q*(logB-logF-logp)
    return ber+q*kplus

def subtractive(t,a):
    logA,logp,logB,logF,q=log_parts(t,a)
    _,m2,_,_=moments(t,a)
    return -0.5*a*q*m2-logF

a=2.526254483411193
max_stable=0.0
for t in (-8.,-4.,-2.,-1.,0.,1.,2.,4.,8.):
    kp=positive_path(t,a); kc=sign_chain(t,a); kd=subtractive(t,a)
    e=abs(kp-kc); max_stable=max(max_stable,e)
    print('T',t,'POSPATH',format(kp,'.17e'),'SIGNCHAIN',format(kc,'.17e'),
          'STABLE_ERR',format(e,'.3e'),'SUBTRACTIVE',format(kd,'.17e'),
          'SUBTRACTIVE_ERR',format(abs(kd-kp),'.3e'))
print('MAX_STABLE_ERR',format(max_stable,'.3e'))
assert max_stable < 5e-13
print('ALL_POSITIVE_KL_CHECKS_PASS')
