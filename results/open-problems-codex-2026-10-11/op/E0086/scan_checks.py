from pathlib import Path
import json,math
out=[]
for alpha in [.3,.375,.45]:
 for N in [256,4096,65536]:
  lower=(2*N)**alpha;upper=2*N**alpha;bound=math.ceil(upper)
  pts=[(x,y) for x in range(-bound,bound+1) for y in range(-bound,bound+1) if lower*lower<x*x+y*y<=upper*upper]
  pts.sort();count=len(pts);fits=count<=N
  if fits:
   for i,(x,y) in enumerate(pts):
    n=N+i;norm2=x*x+y*y;assert n**(2*alpha)<norm2<=(2*n**alpha)**2
  L=2**alpha;c=(L+2)/2;d=(2-L)/4;q=math.floor(c*N**alpha);r=d*N**alpha;rad=math.ceil(r)
  disc=[(x,y) for x in range(q-rad,q+rad+1) for y in range(-rad,rad+1) if (x-q)**2+y*y<=r*r]
  if r>1:
   assert all(lower*lower<x*x+y*y<=upper*upper for x,y in disc)
  out.append({'alpha':alpha,'N':N,'annulus_points':count,'fits_block':fits,'contained_disc_radius':r,'contained_disc_points':len(disc),'geometry_checked':r>1})
Path('scan_checks.json').write_text(json.dumps(out,indent=2));print('nine scan geometry cases passed',out)
