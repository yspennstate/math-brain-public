import numpy as np
from itertools import combinations,product,permutations
from scipy.optimize import linprog
from explore import pairs,triples,cols,D
# coordinates first2rows first2cols of rowcolsum1
base=np.array([[0.,0,1],[0,0,1],[1,1,-1]])
B=[]
for i,j in product(range(2),repeat=2):
 x=np.zeros((3,3));x[i,j]=x[2,2]=1;x[i,2]=x[2,j]=-1;B.append(x)
B=np.stack(B,axis=-1).reshape(9,4);b=base.flatten()
verts={}
for ids in combinations(range(18),4):
 idx=[i//2 for i in ids];lhs=B[idx];rhs=np.array([0 if i%2==0 else 2/3 for i in ids])-b[idx]
 if np.linalg.matrix_rank(lhs)<4:continue
 q=np.linalg.solve(lhs,rhs);x=(b+B@q).reshape(3,3)
 if x.min()>=-1e-9 and x.max()<=2/3+1e-9:verts[tuple(np.rint(x.flatten()*3).astype(int))]=x
print('vertices',len(verts))
ps=list(permutations(range(3)))
def orbit(v):
 x=np.array(v).reshape(3,3)
 return {tuple(y.flatten()) for p in ps for q in ps for y in [x[list(p)][:,list(q)],x.T[list(p)][:,list(q)]]}
remaining=set(verts); reps=[]
while remaining:
 r=min(remaining);o=orbit(r);reps.append((r,len(o)));remaining-=o
print('orbits',reps)
# pair color matrix, x nonnegative; force symmetry A,B isn't needed since marg symmetric
P=np.zeros((45,90))
for k,(a,b_) in enumerate(cols):
 P[pairs.index(a),k]=1;P[15+pairs.index(b_),k]=1;P[30+pairs.index(tuple(sorted(set(range(6))-set(a)-set(b_)))),k]=1
for v,size in reps:
 C=np.array(v).reshape(3,3)/3
 a=np.array([1/12 if (i<3)==(j<3) else C[i,j-3]/6 for i,j in pairs])
 h=np.array([0 if (i<3)==(j<3) else 1/9 for i,j in pairs])
 res=linprog(np.zeros(90),A_eq=P,b_eq=np.r_[a,a,h],bounds=(0,None),method='highs')
 print(v,size,res.success)
 if res.success: print([(cols[k],round(w*36,7)) for k,w in enumerate(res.x) if w>1e-9])
