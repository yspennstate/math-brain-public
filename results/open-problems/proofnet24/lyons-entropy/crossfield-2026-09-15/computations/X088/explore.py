import numpy as np
from itertools import product
from scipy.special import xlogy
# atoms: empty,single class,four adjacent pairs,two opposite pairs,triple class,full
bits=np.array(list(product([0,1],repeat=4)))
T=np.zeros((6,16))
for k,b in enumerate(bits):
 n=sum(b)
 if n!=2: T[{0:0,1:1,3:4,4:5}[n],k]=1
 elif b[0]==b[2] and b[1]==b[3]: T[2,k]=1
 else: T[2,k]=.5;T[3,k]=.5
weights=np.array([1,4,4,2,4,1])
def jets(l):
 q=np.prod(np.where(bits,l,1-l),axis=1)
 s=(bits-l)/(l*(1-l))
 p=T@q;g=T@(q[:,None]*s)
 hh=np.zeros((6,4,4))
 for i in range(4):
  for j in range(4):
   if i!=j:hh[:,i,j]=T@(q*s[:,i]*s[:,j])
 Q=g.T@(g/p[:,None])+np.einsum('a,aij->ij',np.log(p/weights),hh)
 return p,g,hh,Q
if __name__=='__main__':
 rng=np.random.default_rng(88)
 worst=[1,None]
 for j in range(3000):
  l=rng.beta(.5,.5,4)*.9998+.0001
  p,g,h,Q=jets(l)
  m=np.linalg.eigvalsh(Q)[0]
  if m<worst[0]:worst=[float(m),l.tolist()]
 print(worst)
 for l in [[.2,.3,.5,.7],[.1,.8,.1,.8],[.01,.2,.7,.99]]:
  p,g,hh,Q=jets(np.array(l)); print(l,p,Q,np.linalg.eigvalsh(Q))
