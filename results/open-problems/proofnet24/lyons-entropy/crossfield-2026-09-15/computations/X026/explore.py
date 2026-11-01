import numpy as np

def hess(x,y):
 u,v=x*x,y*y
 A=(1+u)*(1+v); B=(1-u)*(1-v); C=1+u*v; D=1-u*v
 fu=((1+v)*np.log(A)-(1-v)*np.log(B)+2*v*np.log(C)-4*v*np.log(D))/8
 fv=((1+u)*np.log(A)-(1-u)*np.log(B)+2*u*np.log(C)-4*u*np.log(D))/8
 fuu=((1+v)/(1+u)+(1-v)/(1-u)+2*v*v/C+4*v*v/D)/8
 fvv=((1+u)/(1+v)+(1-u)/(1-v)+2*u*u/C+4*u*u/D)/8
 fuv=(np.log(A*B*C*C/D**4)+2+2*u*v/C+4*u*v/D)/8
 return np.array([[2*fu+4*u*fuu,4*x*y*fuv],[4*x*y*fuv,2*fv+4*v*fvv]])
xx=np.r_[np.linspace(0,0.999,101),1-10.**np.arange(-2,-13,-1)]
worst=(float('inf'),None); worstdd=(float('inf'),None)
for x in xx:
 for y in xx:
  if not x+y:continue
  h=hess(x,y)
  v=np.linalg.eigvalsh(h)[0]
  dd=min(h[0,0]-abs(h[0,1]),h[1,1]-abs(h[0,1]))
  if v<worst[0]:worst=v,(x,y,h.tolist())
  if dd<worstdd[0]:worstdd=dd,(x,y,h.tolist())
print('Min eigen:',worst)
print('Min diagonal dominance:',worstdd)
