from explore import output
import numpy as np
rng=np.random.default_rng(69323);J=np.ones((3,3))/3
families={'flatcol':lambda x:J+x*np.array([[1,-1,0],[-1,1,0],[0,0,0]]),'dupcol':lambda w:np.column_stack(((1-w)/2,(1-w)/2,w)),'depolar':lambda x:(1-x)*np.eye(3)+x*J}
for name,bb in families.items():
 worst=(1e9,None)
 for k in range(10000):
  p=rng.uniform(.003,.997,3)
  x=rng.uniform(0,.2886) if name=='flatcol' else rng.uniform(0,1)
  if name=='dupcol':x=rng.dirichlet(np.ones(3))
  B=bb(x)
  d=output(p,J)-output(p,B); ev=np.linalg.eigvalsh(d)[0]
  if ev<worst[0]:worst=ev,(p,x,np.linalg.eigh(d)[1][:,0])
 print(name,worst,flush=True)
