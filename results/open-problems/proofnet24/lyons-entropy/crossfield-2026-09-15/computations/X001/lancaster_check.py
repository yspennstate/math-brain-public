import numpy as np
rng=np.random.default_rng(1001)
minimum=(1e9,None)
for z in range(1000):
 p=rng.dirichlet(np.ones(3));q=rng.dirichlet(np.ones(4))
 x=rng.normal(size=3);y=rng.normal(size=4)
 x-=p@x;y-=q@y
 xy=x[:,None]*y
 c=(.01+.98*rng.random())/xy.max()
 x*=np.sqrt(c);y*=np.sqrt(c);xy=x[:,None]*y
 w=p[:,None]*q
 F=np.stack([x[:,None]+np.zeros_like(xy),y+np.zeros_like(xy),-2*xy],axis=-1)
 G=np.einsum('ij,ijk,ijl->kl',w/(1-xy),F,F)
 D=np.sum(-w*xy*np.log(1-xy))
 T=np.array([[0,1,0],[1,0,0],[0,0,-2]])
 H=G-D*T
 m=np.linalg.eigvalsh(H)[0]
 if m<minimum[0]: minimum=(float(m),(p,q,x,y,D,H))
 if m< -1e-9:
  print('FAIL',z,minimum);break
else: print('PASS exploratory',minimum)
