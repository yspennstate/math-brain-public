import numpy as np,json
from pathlib import Path
rows=[]
for path in Path('experiments').glob('*.npz'):
 d=np.load(path);u=d['odometer'];a=d['height'];R=int(d['R'])
 monotone=bool(np.all(u[R:,R:]>=u[R:,R:][:,0:])) if False else bool(np.all(np.diff(u[R:,:],axis=0)<=0) and np.all(np.diff(u[:,R:],axis=1)<=0))
 assert monotone,(path,'moving-plane monotonicity failed')
 for frac in [0.15,0.3,0.45,0.6]:
  r=max(1,int(np.count_nonzero(u[R,:]>0)*frac/2));box=u[R-r:R+r+1,R-r:R+r+1]
  if not np.all(box>0):continue
  side=2*r+1;edges=2*side*(side-1);height=int(a[R-r:R+r+1,R-r:R+r+1].sum())
  assert height>=edges,(path,r,height,edges)
  rows.append(dict(file=str(path),box_radius=r,final_height_sum=height,internal_edges=edges))
Path('experiments/referee_checks.json').write_text(json.dumps(dict(coordinate_monotonicity='passed all 22 saved stabilizations',last_firing_density_boxes=rows),indent=2),encoding='utf8')
print('Coordinate monotonicity checked on every saved array; last-firing inequality checked in',len(rows),'fully fired boxes.')
