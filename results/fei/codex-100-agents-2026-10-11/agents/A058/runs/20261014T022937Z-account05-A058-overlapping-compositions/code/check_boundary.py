import sys
sys.dont_write_bytecode=True
import arithmetic as a
from fractions import Fraction as Q
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
def main():
 start=time.perf_counter();rows=[];checks=0
 def ck(v):
  nonlocal checks
  checks+=1
  assert v,checks
 for k in (2,4,6,8,10,12,14,16):
  N=1<<k;aa=Q(1,N);bb=Q(1,1<<(k//2));p=bb
  ng=2-2*aa;nh=1-p+p/bb
  ck(ng<2);ck(nh<2);ck(p/bb==1)
  D=a.add(a.scale(a.shift(-aa,aa,bb),N-1),a.shift(1-aa,aa,bb));inf=aa/2
  if k>=4:
   cert=a.add(D,((2,-(k-4)*inf),));ck(not cert or a.bounds(cert)[0]>=0)
  violation=False
  if k==14:
   cert=a.add(D,((2,-8*inf),));ck(a.bounds(cert)[0]>0);violation=True
  if k in (2,4):
   bent=tuple((-1)**sum(((t>>j)&1)*((t>>(j+1))&1) for j in range(0,k,2)) for t in range(N))
   ck(all(abs(c)==bb for c in a.fft(bent)))
   mg=tuple(1-Q(t==0) for t in range(N));mh=tuple(1-p+p*v for v in bent)
   ck(sum(map(abs,a.fft(mg)))==ng);ck(sum(map(abs,a.fft(mh)))==nh)
  lo,hi=a.bounds(a.scale(D,1/inf));rows.append({'k':k,'r':k//2,'reach_probability':str(p),'root_G_norm':str(ng),'root_H_norm':str(nh),'leaf_H_norm':str(1/bb),'D_over_inf_interval':[str(lo),str(hi)],'price8_violation':violation})
 out={'cases':len(rows),'exact_assertions':checks,'seconds':time.perf_counter()-start,'failures':0,'rows':rows,'scope':'root-only admission does not imply frozen pointwise adaptive price; no aggregate-tree or FEI refutation'}
 (ROOT/'out/boundary.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':main()
