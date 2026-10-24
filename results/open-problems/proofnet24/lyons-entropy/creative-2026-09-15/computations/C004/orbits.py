from explore import *
from fractions import Fraction as F
Q=np.exp(2j*np.pi*np.arange(6)[:,None]*np.arange(6)[None,:]/6)/np.sqrt(6)
levels,diamonds,D=setup(); p,b=laws(Q)
AB=[(a,tuple(i for i in range(6) if i not in a+j)) for a,j in diamonds]
lookup={p:k for k,p in enumerate(AB)}
def transforms(a,b):
 for shift in range(6):
  for sig in [-1,1]:
   aa=tuple(sorted((sig*i+shift)%6 for i in a));bb=tuple(sorted((sig*i+shift)%6 for i in b))
   yield (aa,bb);yield(bb,aa)
orbits={}
for k,(a,b_) in enumerate(AB):
 key=min(transforms(a,b_));orbits.setdefault(key,[]).append(k)
O=np.zeros((90,len(orbits)))
for j,ks in enumerate(orbits.values()):O[ks,j]=1
res=linprog(np.r_[np.zeros(len(orbits)),-1],A_eq=np.c_[D@O,np.zeros(50)],b_eq=b,A_ub=np.c_[-np.eye(len(orbits)),np.ones(len(orbits))],b_ub=np.zeros(len(orbits)),bounds=(0,None),method='highs')
print('orbits',len(orbits),'min',F(-res.fun).limit_denominator())
for (ab,ks),w in zip(orbits.items(),res.x): print(ab,len(ks),F(w).limit_denominator())
print('left inverse norms')
P=np.linalg.pinv(D);print(np.max(np.sum(abs(P),axis=1)),np.linalg.matrix_rank(D))
np.savez('creative-lyons-20260915/computations/C004/fourier_data.npz',Q=Q,b=b,x=O@res.x[:-1],P=P)
