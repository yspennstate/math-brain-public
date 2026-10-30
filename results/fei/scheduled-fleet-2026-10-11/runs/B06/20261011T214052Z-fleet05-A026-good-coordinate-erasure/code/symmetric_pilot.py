import json,time
from math import comb
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def c(n,k):return comb(n,k) if 0<=k<=n else 0
def main():
 start=time.perf_counter(); out=[]
 for n in [8,16,32,64]:
  for offset in [0,1,2,4,8]:
   t=n//2+offset
   if t>n:continue
   w=[]
   for k in range(n+1):
    w.append(sum((1 if j>=t else -1)*sum((-1)**l*c(k,l)*c(n-k,j-l) for l in range(k+1)) for j in range(n+1)))
   assert sum(c(n,k)*w[k]**2 for k in range(n+1))==1<<(2*n)
   num=2*sum(c(n-1,k)*abs(w[k]*w[k+1]) for k in range(n))
   den=sum(c(n-1,k)*w[k+1]**2 for k in range(n))
   ratio=Fraction(num,den)
   out.append({'n':n,'t':t,'ratio':str(ratio),'ratio_display':float(ratio),'walsh_by_level':w})
   if time.perf_counter()-start>55:raise RuntimeError('frozen limit')
 result={'helper_version':'A026-symmetric-amplitude-v1','elapsed_seconds':time.perf_counter()-start,'results':out}
 (ROOT/'out'/'symmetric_pilot.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({**result,'results':[{k:v for k,v in r.items() if k!='walsh_by_level'} for r in out]},indent=2))
if __name__=='__main__':main()
