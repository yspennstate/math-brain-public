from pathlib import Path
from collections import defaultdict
from fractions import Fraction as F
import time,json

def parts(n=4):
 out=[]
 def gen(a):
  if len(a)==n:out.append(tuple(a));return
  for z in range(max(a,default=-1)+2):gen(a+[z])
 gen([]);return out
PARTS=parts()
def orbit(a):
 sizes=sorted(a.count(v) for v in set(a))
 if sizes==[1,1,1,1]:return 's'
 if sizes==[4]:return 'e'
 if sizes==[1,3]:return 'd'
 if sizes==[2,2]:return 'cross' if a[0]==a[2] else 'g'
 i=[i for i in range(4) if a.count(a[i])==2];return 'b' if i[1]-i[0]==2 else 'a'
PARTS=[a for a in PARTS if orbit(a)!='cross']
def score(a,p):
 q=1-p;k=orbit(a)
 return {'s':q*p,'a':q*2*p*(3-2*p)/4,'b':q*(2*p-1)/2,'g':p*q*q*(2-p),'d':q*(2*p**3-7*p*p+8*p-2)/4,'e':-q**4}[k]
def admissible(part,hit):
 # A block not touching the boundary cannot join any different block.
 out=[]
 for r in PARTS:
  if any(part[i]==part[j] and r[i]!=r[j] for i in range(4) for j in range(i)):continue
  if any(r[i]==r[j] and part[i]!=part[j] and not(hit[i] and hit[j]) for i in range(4) for j in range(i)):continue
  out.append(r)
 assert part in out
 return out

def canon(tokens):
 d={};return tuple((d.setdefault(z>>1,len(d))<<1)|(z&1) for z in tokens)

def exact_joint(R,num=1,den=2,poly=False,reverse=False):
 marks=[(-1,0),(0,1),(1,0),(0,-1)];edges=[]
 for x in range(-R,R+1):
  for y in range(-R,R+1):
   if (x,y)==(0,0):continue
   if x>-R and (x-1,y)!=(0,0):edges.append(((x-1,y),(x,y)))
   if y>-R and (x,y-1)!=(0,0):edges.append(((x,y-1),(x,y)))
 if reverse:edges.reverse()
 active=marks.copy();last={v:i for i,ed in enumerate(edges) for v in ed}
 initial=tuple(2*i+int(max(abs(v[0]),abs(v[1]))==R) for i,v in enumerate(active))
 states={initial:[1] if poly else 1};peak=0;start=time.time()
 for j,(v,w) in enumerate(edges):
  new=[]
  for z in [v,w]:
   if z not in active:active.append(z);new.append(z)
  i1=active.index(v);i2=active.index(w)
  keep=[i for i,z in enumerate(active) if z in marks or last[z]>j]
  nxt={}
  for st,weight in states.items():
   a=list(st);ma=max(v>>1 for v in a)+1
   a.extend(2*(ma+i)+int(max(abs(z[0]),abs(z[1]))==R) for i,z in enumerate(new))
   cl=canon([a[i] for i in keep]);aa=a[i1]>>1;bb=a[i2]>>1;flag=(a[i1]|a[i2])&1
   b=[2*aa+flag if (z>>1) in [aa,bb] else z for z in a];op=canon([b[i] for i in keep])
   if poly:
    c=nxt.setdefault(cl,[0]*(j+2));o=nxt.setdefault(op,[0]*(j+2))
    for k,val in enumerate(weight):c[k]+=val;o[k+1]+=val
   else:
    nxt[cl]=nxt.get(cl,0)+weight*(den-num);nxt[op]=nxt.get(op,0)+weight*num
  states=nxt;active=[active[i] for i in keep];peak=max(peak,len(states))
  if len(states)>350000:raise RuntimeError('State budget exceeded; stop below 1 GB')
  if time.time()-start>160:raise RuntimeError('Time budget exceeded')
 m=len(edges)
 if poly:
  from math import comb
  assert [sum(w[k] for w in states.values()) for k in range(m+1)]==[comb(m,k) for k in range(m+1)]
 else:assert sum(states.values())==den**m
 out={'R':R,'edges':m,'num':num,'den':den,'poly':poly,'peak':peak,'seconds':time.time()-start,'states':[{'tokens':list(k),'weight':v} for k,v in states.items()]}
 return out

def evaluate(data,p):
 m=data['edges'];total=F(0);naive=F(0);alter=F(0)
 for st in data['states']:
  tokens=st['tokens'];part=tuple(v>>1 for v in tokens);hit=tuple(v&1 for v in tokens)
  poss=admissible(part,hit);vals=[score(a,p) for a in poss]
  if data['poly']:prob=sum(F(c)*p**k*(1-p)**(m-k) for k,c in enumerate(st['weight']))
  else:
   assert p==F(data['num'],data['den']);prob=F(st['weight'],data['den']**m)
  total+=prob*min(vals);naive+=prob*score(part,p)
  if len(poss)>1:alter+=prob
 return {'lower':str(total),'lower_float':float(total),'free_signed':str(naive),'alterable_probability':str(alter),'alterable_float':float(alter)}

if __name__=='__main__':
 for R in [1,2,3]:
  data=exact_joint(R,poly=(R<=2));ev=evaluate(data,F(1,2));data['evaluation']=ev
  Path(f'joint_R{R}.json').write_text(json.dumps(data,indent=2),encoding='utf8');print('R',R,'peak',data['peak'],'seconds',data['seconds'],ev,flush=True)
