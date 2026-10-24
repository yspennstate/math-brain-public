from pathlib import Path
from fractions import Fraction as F
from joint_boundary import canon,parts
import json,time

def attempt_n2(R=2):
 xmin,xmax,ymin,ymax=1-R,R+2,-R,R
 marks=[(0,0),(1,0),(2,0),(3,0)]
 edges=[]
 for x in range(xmin,xmax+1):
  for y in range(ymin,ymax+1):
   if x>xmin:edges.append(((x-1,y),(x,y)))
   if y>ymin:edges.append(((x,y-1),(x,y)))
 def boundary(z):return z[0] in [xmin,xmax] or z[1] in [ymin,ymax]
 active=marks.copy();last={v:i for i,ed in enumerate(edges) for v in ed};states={tuple(2*i for i in range(4)):1};start=time.time();peak=0
 for j,(v,w) in enumerate(edges):
  new=[]
  for z in [v,w]:
   if z not in active:active.append(z);new.append(z)
  i1=active.index(v);i2=active.index(w);keep=[i for i,z in enumerate(active) if z in marks or last[z]>j];nxt={}
  for st,c in states.items():
   a=list(st);ma=max(v>>1 for v in a)+1;a.extend(2*(ma+i)+int(boundary(z)) for i,z in enumerate(new))
   cl=canon([a[i] for i in keep]);aa=a[i1]>>1;bb=a[i2]>>1;flag=(a[i1]|a[i2])&1
   b=[2*aa+flag if (z>>1) in [aa,bb] else z for z in a];op=canon([b[i] for i in keep]);nxt[cl]=nxt.get(cl,0)+c;nxt[op]=nxt.get(op,0)+c
  states=nxt;active=[active[i] for i in keep];peak=max(peak,len(states))
  if peak>350000 or time.time()-start>160:raise RuntimeError('Budget cap reached')
 m=len(edges);assert sum(states.values())==2**m;low=0;fr=0;alt=0
 def fun(r):return F(int(r[0]==r[2])+int(r[3]==r[1]),2)-int(r[0]==r[3])
 for tok,c in states.items():
  p=tuple(v>>1 for v in tok);hit=tuple(v&1 for v in tok);possible=[]
  for r in parts():
   if any(p[i]==p[j] and r[i]!=r[j] for i in range(4) for j in range(i)):continue
   if any(r[i]==r[j] and p[i]!=p[j] and not(hit[i] and hit[j]) for i in range(4) for j in range(i)):continue
   possible.append(r)
  assert p in possible
  low+=c*min(map(fun,possible));fr+=c*fun(p);alt+=c*int(len(possible)>1)
 out={'n':2,'p':'1/2','box':[xmin,xmax,ymin,ymax],'edges':m,'peak':peak,'seconds':time.time()-start,'lower':str(low/2**m),'lower_float':float(low/2**m),'free_averaged_difference':str(fr/2**m),'free_difference_float':float(fr/2**m),'alterable_probability':str(F(alt,2**m))}
 Path(f'next_distance_R{R}_diagnostic.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(out)
if __name__=='__main__':
 for R in [2,3]:
  try:attempt_n2(R)
  except RuntimeError as exc:
   Path(f'next_distance_R{R}_budget.txt').write_text(str(exc),encoding='utf8');print('R',R,str(exc),flush=True)
