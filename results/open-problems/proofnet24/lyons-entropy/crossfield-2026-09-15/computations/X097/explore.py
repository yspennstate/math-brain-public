import numpy as np
from scipy.optimize import minimize

def vals(x,l):
 t=1-2*x; z=1-2*l
 X=np.arctanh(t); L=np.arctanh(z); C=np.logaddexp(X-L,L-X)-np.log(2)
 P=np.array([X+L-z*C,X+L-t*C])
 J=np.array([[2*(1-2*t*z+z*z)/((1-t*t)*(1-t*z)),2/(1-t*z)-2*C],[2/(1-t*z)-2*C,2*(1-2*t*z+t*t)/((1-z*z)*(1-t*z))]])
 return P,J

def opt(x,y,l):
 p,J=vals(x,l);r,K=vals(y,l)
 if min(abs(x-l),abs(y-l))<1e-8:return None
 Ji=np.linalg.inv(J);Ki=np.linalg.inv(K)
 g=p[0]-r[0];d=y-x;s=1+d*g/2
 # center coordinates relative to midpoint avoid cancellation
 mid=(p+r)/2; diff=(p-r)/2
 def con(v,P,inv):
  q=P-v[:2];return v[2]-q@inv@q
 def fun(v):return v[2]+2*d/g*v[0]**2
 ret=minimize(fun,[0,0,1],method='SLSQP',constraints=[{'type':'ineq','fun':lambda v:con(v,diff,Ji)},{'type':'ineq','fun':lambda v:con(v,-diff,Ki)}],options={'ftol':1e-11,'maxiter':300})
 return ret.fun/s, ret.x, s,mid,ret.success
if __name__=='__main__':
 cases=[(.1,.9,.1),(.01,.5,.1),(.01,.2,.03),(.001,.5,.99),(.001,.9,.01),(.07,.09,.08),(.4,.6,.08),(.001,.999,.5),(.05,.7,.3)]
 for c in cases:
  v=opt(*c);print(c,v)
 rng=np.random.default_rng(970)
 top=[]
 for i in range(200):
  x,y=sorted(1/(1+np.exp(-rng.uniform(-8,8,2))));l=1/(1+np.exp(-rng.uniform(-8,8)))
  out=opt(x,y,l)
  if out:top.append((out[0],x,y,l,out[4]))
 print('largest ratios',sorted(top,reverse=True)[:10])
