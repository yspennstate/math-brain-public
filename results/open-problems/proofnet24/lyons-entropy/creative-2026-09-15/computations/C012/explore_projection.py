from explore_bloch import D,H,G,J,bc,linprog,np,Path
from scipy.spatial import ConvexHull
from fractions import Fraction
Aeq=np.column_stack([D,-H,-G,-J])
verts=[];couplings=[]
def support(d):
 res=linprog(np.r_[np.zeros(90),-np.array(d)],A_eq=Aeq,b_eq=bc,bounds=[(0,None)]*90+[(None,None)]*3,method='highs')
 assert res.success,res.message
 v=res.x[-3:]
 if not any(np.linalg.norm(v-w)<1e-7 for w in verts):
  verts.append(v);couplings.append(res.x[:90]);return True
 return False
for d in np.r_[np.eye(3),-np.eye(3)]:support(d)
rng=np.random.default_rng(12012)
for _ in range(100):support(rng.standard_normal(3))
for step in range(30):
 hull=ConvexHull(verts); old=len(verts)
 for equ in hull.equations:support(equ[:3])
 print('step',step,'vertices',len(verts),'facets',len(hull.simplices))
 if len(verts)==old:break
hull=ConvexHull(verts)
# Ellipsoid support sqrt(dx^2+dy^2+3 dz^2).
margins=[-e[-1]-np.sqrt(e[0]**2+e[1]**2+3*e[2]**2) for e in hull.equations]
print('ellipsoid containment min margin',min(margins),'negatives',sum(m<-1e-7 for m in margins))
print('vertices',[[str(Fraction(float(a)).limit_denominator(1000)) for a in v] for v in verts])
print('bad facets',[(hull.equations[i].tolist(),m) for i,m in enumerate(margins) if m<-1e-7])
np.savez(Path(__file__).resolve().parent/'projected_polytope.npz',vertices=verts,weights=couplings,equations=hull.equations)
