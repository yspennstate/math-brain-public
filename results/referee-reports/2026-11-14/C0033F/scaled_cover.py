"""Scaled-margin interval cover of the inherited SMALL box only."""
import json,time,resource
from fractions import Fraction as F
from pathlib import Path
from bnb import SMALL,ORDER,enclosure
from interval_core import iv,interval,full_certificate,bounds,pos,rat

def main():
 iv.dps=70;start=time.monotonic();root=SMALL;stack=[root];out=dict(root=root,coordinate_order=ORDER,target='m*(Lambda+6)>=1/8',nodes=0,certified=[],pending=[],splits=0)
 widths=[F(h)-F(l) for l,h in root]
 def save():
  out.update(pending=stack,complete=not stack,seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
  path=Path('data/scaled_cover.json');tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(out,separators=(',',':'))+'\n');tmp.replace(path)
 while stack and out['nodes']<2000:
  cell=stack.pop();out['nodes']+=1
  a,b,c,x,y,z,t=[interval(lo,hi) for lo,hi in cell];xx=[a,b,c,x,iv.mpf(0),y,iv.mpf(0),z,t]
  certified=False
  try:
   status,cert=enclosure(cell)
   if status!='certified':raise ArithmeticError('split')
   lower=rat(cert['margin_lower_bound'][0]);scaled=lower*(iv.log(8)+6)
   if pos(scaled-iv.mpf(1)/8):
    out['certified'].append(dict(box=cell,margin=cert['margin_lower_bound'],scaled_lower=bounds(scaled),method='inherited cardinality bound; Lambda >= log(8)'));certified=True
  except (ArithmeticError,ValueError,ZeroDivisionError):pass
  if not certified:
   size=[(F(h)-F(l))/widths[i] for i,(l,h) in enumerate(cell)];i=max(range(7),key=lambda k:size[k]);mid=str((F(cell[i][0])+F(cell[i][1]))/2)
   left=[v[:] for v in cell];right=[v[:] for v in cell];left[i][1]=mid;right[i][0]=mid;stack.extend([right,left]);out['splits']+=1
  if out['nodes']%100==0:save();print(out['nodes'],len(out['certified']),len(stack),flush=True)
 save();print('complete',out['complete'],'nodes',out['nodes'],'leaves',len(out['certified']),'pending',len(stack),flush=True)
if __name__=='__main__':main()
