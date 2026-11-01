from collections import defaultdict
from pathlib import Path
from math import comb
import time,json

def canon(a):
 d={};return tuple(d.setdefault(v,len(d)) for v in a)
def exact(R,n):
 verts=[(x,y) for x in range(-R,R+1) for y in range(-R,R+1)]
 edges=[]
 for x in range(-R,R+1):
  for y in range(-R,R+1):
   if x>-R:edges.append(((x-1,y),(x,y)))
   if y>-R:edges.append(((x,y-1),(x,y)))
 src=(0,0);tar=(n,0);active=[src,tar]
 last={v:i for i,ed in enumerate(edges) for v in ed}
 states={(0,1):[1]};peak=0
 for j,(v,w) in enumerate(edges):
  new=[]
  for z in [v,w]:
   if z not in active:active.append(z);new.append(z)
  i1=active.index(v);i2=active.index(w)
  keep=[i for i,z in enumerate(active) if z in [src,tar] or last[z]>j]
  nxt={}
  for state,poly in states.items():
   a=list(state);a.extend(range(max(a)+1,max(a)+1+len(new)))
   cl=canon([a[i] for i in keep]);b=[a[i1] if z==a[i2] else z for z in a];op=canon([b[i] for i in keep])
   c=nxt.setdefault(cl,[0]*(j+2));o=nxt.setdefault(op,[0]*(j+2))
   for k,val in enumerate(poly):c[k]+=val;o[k+1]+=val
  states=nxt;active=[active[i] for i in keep];peak=max(peak,len(states))
 m=len(edges);total=[sum(poly[k] for poly in states.values()) for k in range(m+1)]
 assert total==[comb(m,k) for k in range(m+1)]
 ans=[sum(poly[k] for st,poly in states.items() if st[0]==st[1]) for k in range(m+1)]
 return {'radius':R,'n':n,'edges':m,'peak_states':peak,'counts':ans}

if __name__=='__main__':
 allr=[];start=time.time()
 for R in [1,2,3]:
  rr=[]
  for n in range(1,min(R,3)+1):
   t=time.time();r=exact(R,n);rr.append(r);allr.append(r);print('R',R,'n',n,'peak',r['peak_states'],'secs',time.time()-t,flush=True)
   Path('exact_boxes.json').write_text(json.dumps(allr,indent=2),encoding='utf8')
  for a,b in zip(rr,rr[1:]):
   dif=[u-v for u,v in zip(a['counts'],b['counts'])]
   print('comparison',a['n'],b['n'],'min Bernstein count',min(dif),'negative count',sum(v<0 for v in dif),flush=True)
  if time.time()-start>150:break
 print('TOTAL_SECS',time.time()-start,flush=True)
