"""Check key finite weighted-flow inequalities, not simulate the infinite tail."""
from pathlib import Path
import numpy as np, json, math, time
from scipy.integrate import quad
root=Path(__file__).resolve().parent
start=time.time(); rng=np.random.default_rng(84002)
def gs(dist, cap):
 n,k=dist.shape; order=np.argsort(dist,axis=1); choice=np.zeros(n,dtype=int)
 assigned=np.full(n,-1,dtype=int)
 while True:
  free=np.flatnonzero((assigned<0)&(choice<k))
  if not len(free):return assigned
  prop=order[free,choice[free]]; choice[free]+=1
  for j in np.unique(prop):
   applicants=np.concatenate([np.flatnonzero(assigned==j),free[prop==j]])
   ranked=applicants[np.argsort(dist[applicants,j])]
   assigned[ranked[:cap]]=j; assigned[ranked[cap:]]=-1
def td(x,y):
 delta=np.abs(x-y); delta=np.minimum(delta,4-delta)
 return np.sqrt((delta**2).sum(axis=-1))
grid=np.array([(i/4,j/4) for i in range(16) for j in range(16)])
checks=0; positive_a=0;positive_d=0;both_zero=0
for trial in range(30):
 centres=rng.random((16,2))*4
 dist=td(grid[:,None,:],centres[None,:,:]); assigned=gs(dist,16)
 assert np.all(assigned>=0)
 lengths=dist[np.arange(256),assigned]
 assert all(np.count_nonzero(assigned==j)==16 for j in range(16))
 for origin in rng.random((20,2))*4:
  sx=td(grid,origin); cx=td(centres,origin)
  for radius in [.125,.25,.5,.75,1,1.5]:
   ins=sx<radius; inc=cx<radius
   a=int(np.count_nonzero(ins&(lengths>radius+sx)))
   d=int(np.count_nonzero(inc[assigned]&(lengths>radius+cx[assigned])))
   qo=int(np.count_nonzero(ins&~inc[assigned]))
   qi=int(np.count_nonzero(~ins&inc[assigned]))
   z=int(ins.sum())-16*int(inc.sum())
   assert qo==qi+z
   assert a<=qo and d<=qi
   assert a==0 or d==0
   assert a+d<=qi+max(z,0)
   checks+=1;positive_a+=a>0;positive_d+=d>0;both_zero+=(a==0 and d==0)
moments=[]
for dim in [2,3,4,10,50,100]:
 s=1/(4*dim)
 moment,error=quad(lambda w:dim*(1-w)**(dim-1)*w**(-s),0,1,epsabs=1e-11)
 contraction=2**(s-1)*moment
 bound=(2*dim)**s/(2*(1-s))
 assert contraction<=bound+1e-9 and bound<=16/21
 moments.append({'d':dim,'s':s,'negative_moment':moment,'quadrature_error':error,'contraction':contraction,'analytic_upper_bound':bound})
out={'seed':84002,'trials':30,'checked_origin_radius_combinations':checks,'positive_A_cases':positive_a,'positive_D_cases':positive_d,'both_zero_cases':both_zero,'matrix_bytes':int(dist.nbytes),'elapsed_seconds':time.time()-start,'finite_model':'critical torus; 256 sites of mass 1/16, 16 centres with appetite 1; not infinite Poisson–Lebesgue','scope':'flow balance and exclusion checked exactly as integer counts; numerical negative moments checked separately','moments':moments}
(root/'second_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
