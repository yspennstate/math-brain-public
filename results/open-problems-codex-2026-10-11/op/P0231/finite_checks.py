"""Bounded checks of prefix-permutation invariance, refinement, and a 1D control.
No dimension estimator: finite checks cannot certify the limiting dimension.
"""
import random, json, time
from pathlib import Path
random.seed(231)
def roots(points,n):
 r=list(range(n+2))
 for t in range(n+2,len(points)):
  p=min(range(t),key=lambda j:sum((a-b)**2 for a,b in zip(points[t],points[j])))
  r.append(r[p])
 return r
def trial():
 points=[(0.2,0.5),(0.8,0.5)]+[(random.random(),random.random()) for _ in range(80)]
 n=12
 order=list(range(2,n+2)); random.shuffle(order)
 perm=[0,1]+order+list(range(n+2,len(points)))
 moved=[points[i] for i in perm]
 a,b=roots(points,n),roots(moved,n)
 assert all(perm[b[t]]==a[t] for t in range(n+2,len(points)))
 fine=roots(points,n+1)
 assert all(a[t]==a[fine[t]] for t in range(len(points)))
 # Every binary grouping overlaps exactly at cross-group root pairs (finite sets).
 memberships=[{i for i in range(n+2) if random.random()<0.2} for _ in range(30)]
 colors=[random.randrange(2) for _ in range(n+2)]
 for members in memberships:
  overlap=any(colors[i]==0 for i in members) and any(colors[i]==1 for i in members)
  cross=any(colors[i]!=colors[j] for i in members for j in members)
  assert overlap==cross
def one_dim():
 points=[0.25,0.75]; colors=[0,1]
 for _ in range(500):
  x=random.random(); p=min(range(len(points)),key=lambda i:abs(points[i]-x))
  colors.append(colors[p]); points.append(x)
  left=max(x for x,c in zip(points,colors) if c==0)
  right=min(x for x,c in zip(points,colors) if c==1)
  assert left<right
 return right-left
start=time.monotonic()
for _ in range(100): trial()
gaps=[one_dim() for _ in range(20)]
result={'seed':231,'permutation_and_refinement_trials':100,'points_per_trial':82,
 'one_dimensional_trials':20,'one_dimensional_arrivals':500,'one_dimensional_final_gaps':gaps,
 'assertions':'all passed','seconds':time.monotonic()-start,
 'scope':'Finite algebra and genealogy only; no limiting dimension evidence.'}
Path(__file__).with_name('finite_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
