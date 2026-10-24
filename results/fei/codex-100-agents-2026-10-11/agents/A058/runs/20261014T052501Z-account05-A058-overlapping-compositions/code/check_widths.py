import sys
sys.dont_write_bytecode=True
import check as c
import arithmetic as a
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
import json,time
R=Path(__file__).resolve().parents[1]
def main():
 start=time.perf_counter();limit=6 if sys.argv[1]=='pilot' else 54;cases=0
 for (uc,vc),r,t in product(((7,13),(7,7),(7,8),(0,7),(15,7),(3,5)),range(1,4),range(1,4)):
  if cases>=limit:break
  p,q=Q(1,1<<r),Q(1,1<<t);n=2+r+t
  g=tuple((1 if uc&1<<(x&3) else -1) if (x>>2)&((1<<r)-1)==0 else 1 for x in range(1<<n))
  h=tuple((1 if vc&1<<(x&3) else -1) if x>>(2+r)==0 else 1 for x in range(1<<n))
  f=a.wrapper(g,h);ag=a.fft(g);ah=a.fft(h)
  c.ck(a.absle(a.erase(f,0),20*a.inf(f,0)))
  for i in range(n):
   jg,jh=a.inf(g,i),a.inf(h,i);jf=a.inf(f,i+1);c.ck(jf==(jg+jh)/2)
   D=a.add(a.erase(f,i+1),a.scale(a.add(a.erase(g,i),a.erase(h,i)),Q(-1,2)))
   c.ck(a.absle(D,(6 if i<2 else 5)*jf));c.ck(a.absle(a.erase(f,i+1),(14 if i<2 else 9)*jf))
   if i>=2:
    coeff,j,prob=(ag,jg,p) if i<2+r else (ah,jh,q)
    J=sum((coeff[z|1<<i]**2 for z in range(4)),Q(0));c.ck(J==2*prob*j)
  cases+=1
  if cases%6==0:
   a.fft.cache_clear();a.ent.cache_clear();a.bounds.cache_clear()
 out={'mode':sys.argv[1],'cases':cases,'exact_assertions':c.count,'seconds':time.perf_counter()-start,'failures':0,'maximum_physical_bits':9}
 (R/'out'/('widths_'+sys.argv[1]+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
