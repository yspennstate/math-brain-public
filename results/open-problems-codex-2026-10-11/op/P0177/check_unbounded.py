import numpy as np, scipy.special as sp, scipy.optimize as opt, math,json,pathlib
# Two unit-variance normal components, weighted 2/3 and 1/3, centered at -1 and 2.
# This is an unbounded law with finite exponential quadratic moment for eps<1/2.
weights=np.array([2/3,1/3]); means=np.array([-1.,2.]); var=1.
mom={k:sum(w*sum(math.comb(k,j)*a**(k-j)*math.prod(range(1,j,2)) for j in range(0,k+1,2)) for w,a in zip(weights,means)) for k in range(2,8)}
rows=[]
for n in [80,160]:
 z,w=sp.roots_hermitenorm(n); w=w/np.sqrt(2*np.pi);nodes=np.concatenate([z+a for a in means]);probs=np.concatenate([w*p for p in weights]);probs/=sum(probs)
 for t in [100.,1000.,10000.]:
  def eq(v):
   u,r=v;q=u-nodes;d=r+q*q/t
   return np.array([sum(probs/d)-1,sum(probs*q/d**2)])
  root=opt.root(eq,[-2*mom[3]/t,1-mom[2]/t],tol=1e-11)
  u,r=root.x;q=u-nodes;mode=u+sum(probs*q/(r+q*q/t))
  # Independent classical convolution: mixture of normals of variance t+1.
  h=opt.brentq(lambda h:sum(weights*(means-h)*np.exp(-(means-h)**2/(2*(t+1)))), -1,2,xtol=1e-14)
  f2=-3*mom[3]/t+(5*mom[5]-22*mom[2]*mom[3])/t**2
  c2=-mom[3]/(2*t)+(mom[5]-6*mom[2]*mom[3])/(8*t**2)
  row={'quadrature_nodes_per_component':n,'t':t,'mu':mom,'classical_mode':h,'free_mode':mode,'classical_error_times_t3':(h-c2)*t**3,'free_error_times_t3':(mode-f2)*t**3,'root_residual':float(np.max(np.abs(eq(root.x))))}
  rows.append(row);print(n,t,'scaled errors',row['classical_error_times_t3'],row['free_error_times_t3'],'residual',row['root_residual'])
pathlib.Path('numerics_unbounded.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
