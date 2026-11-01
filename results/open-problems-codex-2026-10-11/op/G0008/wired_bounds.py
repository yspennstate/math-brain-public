from collections import defaultdict
from pathlib import Path
from math import comb
import time,json

def canon(a):
 d={};return tuple(d.setdefault(v,len(d)) for v in a)
def exact(R,n,wired=False):
 verts=[(x,y) for x in range(-R,R+1) for y in range(-R,R+1)]
 edges=[]
 for x in range(-R,R+1):
  for y in range(-R,R+1):
   if x>-R:edges.append(((x-1,y),(x,y)))
   if y>-R:edges.append(((x,y-1),(x,y)))
 src=(0,0);tar=(n,0);active=[src,tar]+([("wired",)] if wired else [])
 last={v:i for i,ed in enumerate(edges) for v in ed}
 states={(0,1,2) if wired else (0,1):[1]};peak=0
 for j,(v,w) in enumerate(edges):
  new=[]
  for z in [v,w]:
   if z not in active:active.append(z);new.append(z)
  i1=active.index(v);i2=active.index(w)
  keep=[i for i,z in enumerate(active) if z in [src,tar] or (wired and z==("wired",)) or last[z]>j]
  nxt={}
  for state,poly in states.items():
   a=list(state);a.extend(range(max(a)+1,max(a)+1+len(new)))
   if wired:
    for i,z in enumerate(active):
     if len(z)==2 and max(abs(z[0]),abs(z[1]))==R:
      old=a[i];a=[a[2] if val==old else val for val in a]
   cl=canon([a[i] for i in keep]);b=[a[i1] if z==a[i2] else z for z in a];op=canon([b[i] for i in keep])
   c=nxt.setdefault(cl,[0]*(j+2));o=nxt.setdefault(op,[0]*(j+2))
   for k,val in enumerate(poly):c[k]+=val;o[k+1]+=val
  states=nxt;active=[active[i] for i in keep];peak=max(peak,len(states))
 m=len(edges);total=[sum(poly[k] for poly in states.values()) for k in range(m+1)]
 assert total==[comb(m,k) for k in range(m+1)]
 ans=[sum(poly[k] for st,poly in states.items() if st[0]==st[1]) for k in range(m+1)]
 return {'radius':R,'n':n,'edges':m,'peak_states':peak,'wired':wired,'counts':ans}


if __name__=='__main__':
 import sympy as S
 R=3;n=2;start=time.time();r=exact(R,n,True)
 Path('wired_box.json').write_text(json.dumps(r,indent=2),encoding='utf8')
 f=next(v for v in json.loads(Path('exact_boxes.json').read_text()) if v['radius']==R and v['n']==1)
 dif=[a-b for a,b in zip(f['counts'],r['counts'])];m=r['edges']
 print('WIRED peak',r['peak_states'],'seconds',time.time()-start,flush=True)
 print('SIGNED Bernstein min',min(dif),'negatives',sum(v<0 for v in dif),flush=True)
 for p in [.1,.2,.3,.4,.5,.6,.7,.8,.9,.95,.99]:
  val=sum(float(d)*p**k*(1-p)**(m-k) for k,d in enumerate(dif));print(p,val,flush=True)
 x=S.symbols('x');pol=S.Poly(sum(d*x**k*(1-x)**(m-k) for k,d in enumerate(dif)),x)
 coeff=pol.all_coeffs();print('degree',pol.degree(),flush=True)
 fac=S.factor(pol.as_expr());Path('free_wired_polynomial.txt').write_text(str(fac),encoding='utf8');print('factor prefix',str(fac)[:1200],flush=True)
 Path('free_wired_counts.json').write_text(json.dumps(dif),encoding='utf8')
