from explore import E,sets,ix,AB,abix,np,it,Path
p=np.load(Path(__file__).resolve().parent/'projected_polytope.npz')
# Coefficients constructed from numerical determinants only for discovery.
from explore_bloch import bc,H,G,J
B=np.round(72*np.column_stack([bc,H,G,J])).astype(int)
sym={}
for perm in it.permutations(E):
 for swap in [False,True]:
  psets=[]
  for X in sets:
   Y=tuple(sorted(perm[i] for i in X))
   if swap:Y=tuple(i for i in E if i not in Y)
   psets.append(ix[Y])
  T=B[psets]
  if not np.array_equal(T[:,0],B[:,0]):continue
  signs=[]
  for j in range(1,4):
   if np.array_equal(T[:,j],B[:,j]):signs.append(1)
   elif np.array_equal(T[:,j],-B[:,j]):signs.append(-1)
   else:break
  if len(signs)==3 and tuple(signs) not in sym:sym[tuple(signs)]={'perm':perm,'swap':swap}
print(sym)
