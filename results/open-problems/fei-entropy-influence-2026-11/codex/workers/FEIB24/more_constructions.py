import json,math,time,resource,os
from pathlib import Path
import numpy as np
from analysis import evaluate,wht,phi
# Separate constructors; importing structured.py would rerun its search.
def hid(k):
 n=k+1;ix=np.arange(1<<n);y=ix&((1<<k)-1);wt=np.zeros(len(ix),dtype=np.uint8)
 for j in range(k):wt+=(y>>j&1).astype(np.uint8)
 y0=(1<<(k//2))-1
 return np.where((wt>k//2)|((ix>>k&1==1)&((y&y0)==y0)),1,-1)
def thr(n,t):return np.array([1 if x.bit_count()>=t else -1 for x in range(1<<n)],dtype=np.int64)
def comp(outer,inner):
 k=len(outer).bit_length()-1;m=len(inner).bit_length()-1;n=k*m
 ix=np.arange(1<<n);o=np.zeros(len(ix),dtype=np.int32)
 for j in range(k):o|=(inner[(ix>>(j*m))&((1<<m)-1)]>0).astype(np.int32)<<j
 return outer[o]
rows=[];best=None
for k in [3,5]:
 inner=hid(k)
 for b in range(2,20//(k+1)+1):
  for t in range(1,b+1):
   for dual in [False,True]:
    g=-inner[::-1] if dual else inner;f=comp(thr(b,t),g);s=evaluate(f);s.update(tag='threshold_of_hidden',hidden_k=k,blocks=b,threshold=t,dual=dual);rows.append(s)
    if best is None or s['minratio']>best['minratio']:
     best=s;np.savez_compressed('witnesses/hidden_tribes_best.npz',f=f.astype(np.int8))
for dualouter in [False,True]:
 for dualinner in [False,True]:
  g=hid(3);f=comp(-g[::-1] if dualouter else g,-g[::-1] if dualinner else g);s=evaluate(f);s.update(tag='hidden_selfcomposition',dualouter=dualouter,dualinner=dualinner);rows.append(s)
  if s['minratio']>best['minratio']:best=s;np.savez_compressed('witnesses/hidden_tribes_best.npz',f=f.astype(np.int8))
json.dump(dict(rows=rows,best=best),open('more_constructions.json','w'),indent=2);print('rows',len(rows),'best',best)
