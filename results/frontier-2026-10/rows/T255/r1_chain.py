"""T255 rank-one check on the EXACT finite network: start with only token 1 nonzero (V0 = a0 e1 e1^T); tokens 2..m stay
exactly zero (their query rows are zero, so their softmax rows are uniform and A row i = e_i). Token 1's covariance a follows
  a' = a [lam^2 + 2 lam gam A11 Z/sqrt n + gam^2 A11^2 (Z^2 + chi2_{n-1})/n],  A11 = 1 + softmax_11 - 1/m,
  softmax_11 = e^{y}/(e^{y} + m - 1),  y = a g1 g2 / (tau0 sqrt n)   (n_k = 1).
Compared with the SDE on the rank-one stratum at u = e1: da = a^3 f dt + a sqrt(2c + B^2 a^2) dW,
  f = (g2/tau0^2)(m-1)(m^2-m-1)/m^4, B = 2 g2 (m-1)/(m^2 tau0): P(hit K before eps) = int_eps^a0 s'/int_eps^K s', s' = (2c+B^2 y^2)^(-f/B^2).
usage: python r1_chain.py m g2 n a0 K eps reps"""
import sys, numpy as np
from scipy.integrate import quad
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
m=int(sys.argv[1]); g2=float(sys.argv[2]); n=int(sys.argv[3]); a0=float(sys.argv[4]); K=float(sys.argv[5]); eps=float(sys.argv[6]); R=int(sys.argv[7])
tau0=1.0; lam=np.sqrt(1-g2); gam=np.sqrt(g2); c=g2*(2-g2)
f=g2/tau0**2*(m-1)*(m*m-m-1)/m**4; B=2*g2*(m-1)/(m*m*tau0)
sp=lambda y:(2*c+B*B*y*y)**(-f/(B*B))
pred=quad(sp,eps,a0,limit=200)[0]/quad(sp,eps,K,limit=200)[0]
rng=np.random.default_rng(5+m+int(10*g2))
a=np.full(R,a0); res=np.zeros(R,int); alive=np.arange(R); step=0
while len(alive) and step<400*n:
    x=a[alive]; k=len(x)
    y=x*rng.standard_normal(k)*rng.standard_normal(k)/(tau0*np.sqrt(n))
    sm=1.0/(1.0+(m-1)*np.exp(-np.clip(y,-50,50))); A11=1+sm-1.0/m
    Z=rng.standard_normal(k); chi=rng.chisquare(n-1,k)
    x=x*(lam**2+2*lam*gam*A11*Z/np.sqrt(n)+g2*A11**2*(Z*Z+chi)/n)
    a[alive]=x; up=x>=K; dn=x<=eps
    res[alive[up]]=1; res[alive[dn]]=-1; alive=alive[~(up|dn)]; step+=1
p=np.mean(res==1); se=np.sqrt(p*(1-p)/R)
print("m %d g2 %.2f n %d a0 %g K %g eps %g reps %d: chain P(hit K first) %.4f +- %.4f (unresolved %d, t_max %.1f) | rank-one SDE %.4f | 2f/B^2 = %.3f"%(m,g2,n,a0,K,eps,R,p,se,len(alive),step/n,pred,2*f/B**2),flush=True)
