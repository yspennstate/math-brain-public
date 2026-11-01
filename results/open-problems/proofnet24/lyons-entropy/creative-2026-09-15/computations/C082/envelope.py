import numpy as np
from itertools import product
from scipy.optimize import differential_evolution

def env(x,tlo=.5,thi=2):
 r=np.array(x[:3]);z=x[3]; u=1-r*r;D=1-sum(r*r)+2*np.prod(r)*z
 if D<=0:return 1e6
 c=-np.log(u);tau=np.log(np.prod(u)/D)
 def kval(t):
  Z=1+sum(t)+sum(u[i]*t[(i+1)%3]*t[(i+2)%3] for i in range(3))+np.prod(t)*D
  return np.array([t[i]*(1+t[(i+1)%3]*u[(i+2)%3]+t[(i+2)%3]*u[(i+1)%3]+t[(i+1)%3]*t[(i+2)%3]*D)/Z for i in range(3)])
 kl=np.array([kval(np.array([tlo if h==i else thi for h in range(3)]))[i] for i in range(3)])
 ku=np.array([kval(np.array([thi if h==i else tlo for h in range(3)]))[i] for i in range(3)])
 dl=c+tau*(kl if tau>=0 else ku);du=c+tau*(ku if tau>=0 else kl)
 v=np.minimum(.25, np.maximum(kl*(1-kl),ku*(1-ku)))
 v=np.where((kl<=.5)&(ku>=.5),.25,v)
 w=[]
 for i in range(3):
  j,h=[a for a in range(3) if a!=i]
  s=np.linspace(tlo/(1+tlo),thi/(1+thi),30)
  rho=(r[i]**2-2*s*np.prod(r)*z+s*s*r[j]**2*r[h]**2)/((1-s*r[j]**2)*(1-s*r[h]**2))
  rhom=max(rho)
  w.append(rhom/(4*(2-rhom)**2))
 if min(dl)<=0:return 1e5
 return sum(v[i]*du[(i+1)%3]*du[(i+2)%3]/dl[i] for i in range(3))+2*tau*tau*sum(w[i]/(dl[(i+1)%3]*dl[(i+2)%3]) for i in range(3))

if __name__=='__main__':
 for lo,hi in [(.2,.3),(.2,.35),(.2,.4),(.25,.4),(.2,.45),(.25,.45),(.15,.35),(.1,.3)]:
  opt=differential_evolution(lambda x:-env(x),[(lo,hi)]*3+[(-1,1)],tol=1e-9,popsize=10,maxiter=100,seed=82)
  print(lo,hi,'max U',-opt.fun,'x',opt.x,flush=True)
