from explore import *
lev,ds,D=setup()
AB=[(a,tuple(i for i in range(6) if i not in a+j)) for a,j in ds];ix={x:i for i,x in enumerate(AB)}
cols=[]
for h in range(6):
 for e in range(6):
  if e==h:continue
  R=[i for i in range(6) if i not in [h,e]]
  for tri in combinations(R,3):
   z=np.zeros(90)
   for k in range(3):
    a,b=tri[k],tri[(k+1)%3]
    z[ix[(tuple(sorted([h,a])),tuple(sorted([e,b])))]]+=1
    z[ix[(tuple(sorted([h,b])),tuple(sorted([e,a])))]]-=1
   cols.append(z)
F=np.array(cols).T
print('flows',F.shape,'D residual',np.max(abs(D@F)),'rank',np.linalg.matrix_rank(F),'target kernel',90-np.linalg.matrix_rank(D))
np.save('creative-lyons-20260915/computations/C004/flows.npy',F)
