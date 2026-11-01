import numpy as np,itertools
from scipy.optimize import minimize
sets=list(itertools.combinations(range(4),2));eps=np.array(list(itertools.product([-1,1],repeat=4)))
W=np.array([np.prod(eps[:,S],axis=1) for S in sets]).T

def E(v):
 v=np.maximum(v,1e-300);return -np.dot(v,np.log(v))
def gap(c):
 c=c/np.linalg.norm(c);return E((W@c)**2/16)-E(c*c)
def disc(c):
 A=c[0]*c[5];B=c[1]*c[4];C=c[2]*c[3];return (A+B+C)**2-4*(A*B+A*C+B*C)
rng=np.random.default_rng(12)
best=(1,None)
for j in range(12):
 x=rng.normal(size=6);x/=np.linalg.norm(x)
 r=minimize(gap,x,method='SLSQP',constraints=[{'type':'ineq','fun':disc},{'type':'eq','fun':lambda c:c@c-1}],options={'maxiter':500,'ftol':1e-12})
 print(j,r.fun,disc(r.x),r.success,flush=True)
 if r.success and r.fun<best[0]:best=(r.fun,r.x)
print('BEST',best)
