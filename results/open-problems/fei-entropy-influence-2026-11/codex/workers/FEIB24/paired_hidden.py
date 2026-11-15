"""A complementary pair of pivotal points kills every level-two coefficient through x."""
import json,math
import numpy as np
from analysis import evaluate,wht

def build(k):
 n=k+1;ix=np.arange(1<<n);y=ix&((1<<k)-1);wt=np.zeros(len(ix),dtype=np.uint8)
 for j in range(k):wt+=(y>>j&1).astype(np.uint8)
 y0=(1<<(k//2))-1;pair=(y==y0)|(y==((1<<k)-1)^y0)
 return np.where((wt>=k//2)&(~pair|(ix>>k&1==1)),1,-1)
if __name__=='__main__':
 rows=[]
 for k in range(6,20,2):
  f=build(k);s=evaluate(f);a=wht(f);delta=2.**(1-k)
  assert s['inf'][-1]==delta and s['w2'][-1]==0 and min(s['w2'][:-1])>0
  assert np.max(np.abs(np.array(s['inf'][:-1])-math.comb(k,k//2)/2**k))<1e-13
  s.update(k=k,delta=delta,xratio=s['erasure'][-1]/delta,x_w2_ratio=0,other_min_w2_ratio=min(s['w2'][i]/s['inf'][i] for i in range(k)))
  rows.append(s);print(k,s['xratio'],s['minratio'],s['other_min_w2_ratio'],flush=True)
 json.dump(rows,open('paired_hidden.json','w'),indent=2)
