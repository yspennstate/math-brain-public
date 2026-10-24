import numpy as np
from math import comb

def b(m,a):return np.array([comb(m,j)*a**j*(1-a)**(m-j) for j in range(m+1)])
def go(n,a,c):
 m=n-1
 q=np.convolve(b(m,a),[1-c,c])
 lp=np.log(q)-np.log(np.array([comb(n,j) for j in range(n+1)],float))
 da=m*np.convolve(np.convolve(b(m-1,a),[-1,1]),[1-c,c]);dc=np.convolve(b(m,a),[-1,1])
 daa=m*(m-1)*np.convolve(np.convolve(b(m-2,a),[1,-2,1]),[1-c,c])
 dac=m*np.convolve(b(m-1,a),[1,-2,1])
 F=np.array([[np.sum(da*da/q),np.sum(da*dc/q)],[np.sum(da*dc/q),np.sum(dc*dc/q)]])
 R=-np.array([[daa@lp,dac@lp],[dac@lp,0]])
 return F,R,q,np.array([da,dc]).T
if __name__=='__main__':
 rng=np.random.default_rng(75)
 for n in [3,4,5,8,12,20,40]:
  best=[1e10,None]; bestC=[1e10,None]
  for j in range(4000):
   a=1/(1+np.exp(rng.uniform(-13,13))); c=a+(1-a)/(1+np.exp(rng.uniform(-13,13)))
   if c-a<1e-8:continue
   F,R,q,D=go(n,a,c)
   H=F-R
   val=np.linalg.det(H)/(np.linalg.norm(H)**2)
   if val<best[0]:best=[val,(a,c)]
   if np.linalg.eigvalsh(H)[0] < -1e-6:print('fail',n,a,c,H)
  print(n,best,flush=True)
