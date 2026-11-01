import numpy as np
from itertools import combinations
from scipy.optimize import linprog
pairs=list(combinations(range(6),2)); triples=list(combinations(range(6),3)); E=set(range(6))
cols=[(a,b) for a in pairs for b in pairs if not set(a)&set(b)]
D=np.zeros((50,90))
for k,(a,b) in enumerate(cols):
 D[pairs.index(a),k]=1;D[15+pairs.index(b),k]=1
 for j in E-set(a)-set(b):D[30+triples.index(tuple(sorted(a+(j,)))),k]=1
X=np.array([[np.sqrt(2/3),0],[-1/np.sqrt(6),1/np.sqrt(2)],[-1/np.sqrt(6),-1/np.sqrt(2)]])
u=np.ones(3)/np.sqrt(3)
def law(F,sets):return np.array([abs(np.linalg.det(F[list(s),:]))**2 for s in sets])
for theta in np.linspace(0,np.pi,13):
 R=np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
 Y=X@R
 W=np.vstack((X,Y))/np.sqrt(2);Z=np.vstack((X,-Y))/np.sqrt(2)
 U=np.zeros((6,2));U[:3,0]=u;U[3:,1]=u
 a=law(W,pairs);c=law(Z,pairs)
 g=law(np.column_stack((W,U[:,0])),triples)+law(np.column_stack((W,U[:,1])),triples)
 res=linprog(np.zeros(90),A_eq=D,b_eq=np.r_[a,c,g],bounds=(0,None),method='highs')
 print(theta/np.pi,res.success)
 if not res.success:
  np.savez('computations/C042/infeasible.npz',W=W,U=U,Z=Z,a=a,c=c,g=g,D=D)
