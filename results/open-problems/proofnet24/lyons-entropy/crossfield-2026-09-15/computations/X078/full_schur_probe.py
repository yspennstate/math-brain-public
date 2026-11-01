import numpy as np
from itertools import product
r=np.random.default_rng(780);best=(1e9,None); n=0
for _ in range(3000):
 U,_=np.linalg.qr(r.normal(size=(3,3)));ev=np.clip(r.beta(.5,.5,3),1e-6,1-1e-6);K=(U*ev)@U.T
 p=np.array([(-1)**(3-sum(x))*np.linalg.det(K-np.diag(1-np.array(x))) for x in product((0,1),repeat=3)])
 tau=np.log(p[[0,3,5,6]]).sum()-np.log(p[[1,2,4,7]]).sum();k=np.array([K[1,2],K[2,0],K[0,1]]);q=np.prod(k)
 if q*tau>0:continue
 a=np.diag(K);cov=np.diag(a)-K*K
 # p order x1 x2 x3; c1 pair23, c2 pair31,c3 pair12
 c=np.log([p[2]*p[1]/(p[0]*p[3]),p[4]*p[1]/(p[0]*p[5]),p[4]*p[2]/(p[0]*p[6])]);m=c+tau*a
 J=K-np.diag(a);Br=np.diag(m)-tau*J;Bi=np.diag(m)+tau*J
 L=np.array([[0,m[2],m[1]],[m[2],0,m[0]],[m[1],m[0],0]])
 V=np.linalg.inv(cov)-L-2*tau*tau*np.diag(k)@np.linalg.inv(Br)@np.diag(k)
 mn=np.linalg.eigvalsh(V)[0];n+=1
 if mn<best[0]:best=(mn,(K,tau,m,V,np.linalg.eigvalsh(Br)))
 if mn<-.01:break
print('n',n,'best',best)
