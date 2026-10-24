import numpy as np

def q(r,s):
    L=np.log((1+r*s)**2/((1-r*r)*(1-s*s)))
    tau=2*L-8*np.log((1+r*s)/(1-r*s))
    B=(2+r+s)/(1-r*s)-np.log((1+r*s)/((1-r)*(1-s)))
    u=(r-s)**2/((1-r)*(1-r*s))+L/2+s*tau/4
    v=(r-s)**2/((1-s)*(1-r*s))+L/2+r*tau/4
    return np.array([[B+u,B],[B,B+v]])
for r,s in [(0.9,.1),(.99,.1),(.9,.8),(.4,.1),(.99,.99),(.9999,.01)]:
 print(r,s,'eig',np.linalg.eigvalsh(q(r,s)), 'diff',np.linalg.eigvalsh(q(r,s)-q(r,0)))
