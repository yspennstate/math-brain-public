from fractions import Fraction as F
from pathlib import Path
import math,json,time
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0
def ck(x):
 global checks
 assert x; checks+=1
def log2i(x):
 x=F(x); shift=x.numerator.bit_length()-x.denominator.bit_length(); x/=F(2)**shift
 if x<1:x*=2;shift-=1
 grid=2**96;q=x.numerator*grid//x.denominator;low=F(q,grid);high=F(q+1,grid)
 def ln(v):
  t=(v-1)/(v+1); n=18
  lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
  return lo,lo+2*t**(2*n+1)/((2*n+1)*(1-t*t))
 a=ln(low)[0];b=ln(high)[1]; c,d=ln(F(2))
 return a/d+shift,b/c+shift
def ent(x):
 if not x:return F(0),F(0)
 a,b=log2i(1/x); return x*a,x*b
def h(x):
 a,b=ent(x);c,d=ent(1-x);return a+c,b+d
def mid(z):return float((z[0]+z[1])/2)
rows=[]
for k in [4,6,8,12,16,24,32]:
 delta=F(1,2**k); s=F(1,2**(k//2)); d=F(1,2)+2*delta
 plus=delta*(1-2*s)**2; minus=delta*(1+2*s)**2
 np=(2**k+2**(k//2))//2; nm=2**k-np
 ck(np*plus+nm*minus==1)
 Hi=tuple(np*ent(plus)[j]+nm*ent(minus)[j] for j in (0,1))
 # mate bit absent: same-sign coefficient pairs; mate present: opposite-sign pairs.
 same_plus=(2**(k-2)+2**((k-2)//2))//2; same_minus=2**(k-2)-same_plus
 opposite=2**(k-2)
 mass_same=same_plus*2*plus+same_minus*2*minus
 mass_opp=opposite*(plus+minus)
 ck(mass_same+mass_opp==1)
 Bi=tuple(mass_same+mass_opp*h(plus/(plus+minus))[j] for j in (0,1))
 mi=(h(d)[0]-Bi[1],h(d)[1]-Bi[0]); tc=(k*h(d)[0]-Hi[1],k*h(d)[1]-Hi[0])
 ck(mi[0]>0);ck(tc[0]>0);ck(plus>0)
 v=16*delta**2-256*delta**4;ck(0<v<1)
 Ti=tuple(k*v*log2i(1/v)[j]/(1+2*v) for j in (0,1));ck(Ti[0]>0)
 rows.append({'k':k,'H':mid(Hi),'TC':mid(tc),'TC_over_H':mid(tc)/mid(Hi),'MI':mid(mi),'MI_over_B':mid(mi)/mid(Bi),'MI_over_delta':mid(mi)/float(delta),'B_over_d':mid(Bi)/float(d),'T':mid(Ti),'T_over_sum_B':mid(Ti)/(k*mid(Bi)),'all_coordinates_equal':True})
(ROOT/'out'/'bent_repair.json').write_text(json.dumps({'rows':rows,'checks':checks,'runtime_seconds':time.monotonic()-start,'interval_method':'exact range-reduced 18-term atanh series with rational remainder; floats illustrative'},indent=2),encoding='utf-8')
print(json.dumps({'checks':checks,'runtime_seconds':time.monotonic()-start,'output':'out/bent_repair.json'}))
