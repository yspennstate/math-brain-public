import numpy as np
from scipy.optimize import minimize_scalar
from itertools import combinations
pairs=list(combinations(range(3),2))
masks=np.arange(8)
N=np.array([int(s).bit_count() for s in masks])
def calc(xs,ell):
 u=np.array([((xs[i]-xs[j])/(xs[i]+xs[j]))**2 for i,j in pairs])
 c=-np.log(u)
 weights=np.array([np.prod([ell[i] for i in range(3) if s>>i&1])*np.prod([u[k] for k,(i,j) in enumerate(pairs) if s>>i&1 and s>>j&1]) for s in masks])
 p=weights/weights.sum(); v=np.dot(p,(N-p@N)**2)
 sq=np.sqrt(p); nn=sq*(N-p@N); Ps=[]; Cs=[]
 for i,j in pairs:
  lab=np.array([int(s>>i&1)+2*int(s>>j&1) for s in masks]); marg=np.bincount(lab,weights=p)
  T=(marg[1]+marg[2])/(2*np.sqrt(marg[0]*marg[3])); Cs.append(2*(1+T))
  Ps.append(np.array([[sq[s]*sq[t]/marg[lab[s]] if lab[s]==lab[t] else 0 for t in masks] for s in masks])-np.outer(sq,sq))
 Cs=np.array(Cs); Ps=np.array(Ps)
 def B(t): return np.einsum('i,ijk->jk',(c-t)/Cs,Ps)+t*np.outer(nn,nn)
 def obj(t):return np.linalg.eigvalsh(B(t))[-1]
 res=minimize_scalar(obj,bounds=(0,c.min()),method='bounded')
 return {'scalar0':sum(c/Cs),'scalarmin':sum((c-c.min())/Cs)+c.min()*v,'t':res.x,'rho':min(res.fun,obj(0),obj(c.min())),'c':c.tolist(),'v':v,'p':p.tolist(),'Cs':Cs.tolist()}
if __name__=='__main__':
 rng=np.random.default_rng(45045); best=[]
 for k in range(5000):
  xs=np.array([1,1+10**rng.uniform(-2,.5),1+10**rng.uniform(-2,.5)])
  ell=np.exp(rng.uniform(-2,9,3))
  a=calc(xs,ell)
  if min(a['scalar0'],a['scalarmin'])>1 and a['rho']<.99:
   best.append((a['rho'],xs.tolist(),ell.tolist(),a))
   if len(best)>8:break
 print(best)
