import numpy as np, itertools as it, json
from pathlib import Path
from scipy.optimize import linprog
E=range(6); levels=[list(it.combinations(E,k)) for k in (2,3,4)]; sets=sum(levels,[]); ix={s:k for k,s in enumerate(sets)}
AB=[(A,B) for A in levels[0] for B in it.combinations([i for i in E if i not in A],2)]; abix={ab:k for k,ab in enumerate(AB)}
D=np.zeros((50,90))
for k,(A,B) in enumerate(AB):
 J=[i for i in E if i not in A+B];T=tuple(i for i in E if i not in B)
 for X,s in [(A,1),(T,1)]+[(tuple(sorted(A+(j,))),-1) for j in J]:D[ix[X],k]=s
cert=json.loads((Path(__file__).resolve().parents[1]/'C004/exact_certificate.json').read_text())
x0=np.array(cert['fourier']['weight_numerators'])/216
F=np.exp(2j*np.pi*np.outer(list(E),list(E))/6)/np.sqrt(6)
def contrast(Q):
 def p(A,cols):return abs(np.linalg.det(Q[np.ix_(A,cols)]))**2
 return np.array([p(A,(0,1)) for A in levels[0]]+[-p(M,(0,1,2))-p(M,(0,1,3)) for M in levels[1]]+[p(T,(0,1,2,3)) for T in levels[2]])
def rotate(Q,p,q,theta):
 ans=Q.copy();c=np.cos(theta);s=np.sin(theta)
 ans[p]=c*Q[p]+s*Q[q];ans[q]=-s*Q[p]+c*Q[q]
 return ans
b0=contrast(F)
def permute(x,p,q):
 f=lambda A:tuple(sorted(q if i==p else p if i==q else i for i in A))
 return np.array([x[abix[(f(A),f(B))]] for A,B in AB])
def first():
 x1=permute(x0,0,3); b1=contrast(rotate(F,0,3,np.pi/2)); bm=contrast(rotate(F,0,3,np.pi/4)); h=bm-(b0+b1)/2
 print('h',[(sets[i],round(v*216)) for i,v in enumerate(h) if abs(v)>1e-8])
 bounds=np.minimum(x0,x1);print('D perm',np.max(abs(D@x1-b1)))
 res=linprog(np.zeros(90),A_eq=D,b_eq=h,bounds=list(zip(-bounds,bounds)),method='highs')
 print('minimum-capacity feasible',res.success)
 if res.success:
  y=res.x;print('y216',np.round(y*216).tolist());print('min eigen cap',np.min(x0*x1-y*y))
 else:
  bounds=np.sqrt(x0*x1)
  res=linprog(np.zeros(90),A_eq=D,b_eq=h,bounds=list(zip(-bounds,bounds)),method='highs')
  print('geometric-capacity feasible',res.success)
  if res.success:print('y216',np.round(res.x*216,6).tolist())
 return res
if __name__=='__main__': first()
