import numpy as np
rng=np.random.default_rng(66431);R=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)
worst=1e9
for tr in range(30000):
 v=rng.dirichlet([.4,.4,.4,.1])[:3];s=R@v;w=1-s
 if w.min()<1e-7:continue
 D=R-v;M=np.zeros((3,3))
 for r,d,ss,ww in zip(R,D,s,w):
  M+=-(np.outer(v,d)+np.outer(d,v))/ww+ss*np.outer(d,d)/ww**2-ss/ww*(np.outer(r,r)-np.eye(3))
 val=np.linalg.eigvalsh(M)[0]
 if val<worst:worst=val;ws=v.tolist()
 if val<-.0001:break
print(worst,ws)
