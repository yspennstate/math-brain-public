from pathlib import Path
from fractions import Fraction as F
import json,time
import psutil
R=Path(__file__).resolve().parent;t0=time.monotonic();process=psutil.Process()
coords=[(x,y) for x in range(4) for y in range(4)];idx={p:i for i,p in enumerate(coords)};n=len(coords);full=(1<<n)-1
adj=[0]*n
for (x,y),i in idx.items():
 for q in [(x+1,y),(x,y+1)]:
  if q in idx:
   j=idx[q];adj[i]|=1<<j;adj[j]|=1<<i
z=[F(0)]*(1<<n);z[0]=F(1);cut=[0]*(1<<n);peak=0
for S in range(1,1<<n):
 if S%4096==0:
  peak=max(peak,process.memory_info().rss)
  if time.monotonic()-t0>180:raise RuntimeError('Stopped own computation at 180-second budget')
  if peak>800*1024**2:raise RuntimeError('Stopped own computation at 800-MiB RSS guard')
 b=S&-S;i=b.bit_length()-1;T=S^b
 cut[S]=cut[T]+4-2*(adj[i]&T).bit_count()
 total=F(0);bits=S
 while bits:
  b=bits&-bits;bits^=b;total+=z[S^b]
 z[S]=total/cut[S]
def mask(points):return sum(1<<idx[p] for p in points)
def Z(A):
 extra=full^A;sub=extra;total=F(0)
 while True:
  S=A|sub;total+=z[S]*z[full^S]
  if sub==0:break
  sub=(sub-1)&extra
 return total
A=mask([(1,1),(1,2),(2,1),(2,2)]);base=Z(A)
D=mask([(x,y) for x in range(3) for y in range(3)])
v=idx[(0,1)]
star=mask([(1,1),(0,1),(2,1),(1,2)]);path=mask([(0,1),(1,1),(2,1),(3,1)])
assert star.bit_count()==path.bit_count()==4 and cut[star]==cut[path]==10
assert z[star]==F(13,1280) and z[path]==F(19,1920)
out={
 'graph':'4x4 zero-boundary square, degree 4 retained at every subset',
 'single_adjacent_positive_probability':str(Z(A|(1<<v))/base),
 'single_adjacent_positive_float':float(Z(A|(1<<v))/base),
 'corner_radius1_positive_buffer_probability':str(Z(A|D)/base),
 'corner_radius1_positive_buffer_float':float(Z(A|D)/base),
 'all_free_vertices_positive_probability':str(z[full]/base),
 'all_free_vertices_positive_float':float(z[full]/base),
 'equal_size_cut_comparison':{'vertices':4,'cut':10,'star_z':str(z[star]),'path_z':str(z[path]),'ratio':str(z[star]/z[path])},
 'seconds':time.monotonic()-t0,'peak_sampled_RSS_bytes':peak,
}
(R/'coarea_probe.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out),flush=True)
