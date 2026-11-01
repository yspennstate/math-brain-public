from fractions import Fraction as F
from pathlib import Path
import json
depth=10
points=[F(0)]
for j in range(1,depth+1):points=[x+b*F(2,3**j) for x in points for b in [0,1]]
points.sort();out=[]
for m in range(1,depth+1):
 width=F(1,3**m);j=0;best=0
 for i,x in enumerate(points):
  while j<len(points) and points[j]-x<=width:j+=1
  best=max(best,j-i)
 bound=2**(depth-m+1)
 assert best<=bound,(m,best,bound)
 out.append({'scale':m,'width':str(width),'max_points_in_closed_interval':best,'theoretical_bound':bound})
Path(__file__).with_name('cantor_checks.json').write_text(json.dumps({'depth':depth,'points':len(points),'checks':out,'scope':'Exact rational finite approximant check at scales no finer than construction depth; the infinite Cantor small-ball theorem is proved separately on paper.'},indent=2),encoding='utf8')
print('EXACT_CANTOR_CHECKS_PASS',len(out),'scales',len(points),'points')
