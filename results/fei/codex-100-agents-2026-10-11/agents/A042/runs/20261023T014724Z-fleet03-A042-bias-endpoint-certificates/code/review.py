from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
z=F(1,3);lo=sum(2*z**(2*k+1)/(2*k+1) for k in range(40));hi=lo+2*z**81/(81*(1-z*z))
def trunc_error(r,m):
 a=F(0);b=F(0)
 for k in range(1,r+1):
  t=F(2)**(k-1-r);scale=comb(2*r,k)*F(4)**(1-k)
  phi_m=t*(1-t)*sum(2*(1-t)**j/F(j*(j+1)) for j in range(1,m+1))
  a+=scale*(2*t*(1-t)-phi_m)
  b-=scale*2*t*t*(r+1-k)
 ck(b<0)
 return a+b*hi,a+b*lo
for r in (1,2,3):
 n=2*r;walsh=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(r)) for x in range(1<<n)]
 size=1
 while size<len(walsh):
  for base in range(0,len(walsh),2*size):
   for j in range(size):
    a,b=walsh[base+j],walsh[base+j+size];walsh[base+j]=a+b;walsh[base+j+size]=a-b
  size*=2
 ck(all(abs(a)==2**r for a in walsh))
 ck(sum(F(a*a,2**(2*n)) for a in walsh)==1)
 ck(sum(F(a*a,2**(2*n))*i.bit_count() for i,a in enumerate(walsh))==r)
for r in range(1,17):
 for m in range(6):
  lower,upper=trunc_error(r,m);q=F((m+1)*(m+2))
  required=(F(2)**(-m-1)*F(9,8)**r-F(2)**(-m-r))/q
  ck(lower>=0);ck(lower>=required)
  # Tensor bank and complete normalized reference (no omitted empty atom).
  ck(sum(comb(2*r,k)*F(1,4**r) for k in range(2*r+1))==1)
growing=[(4,1),(8,1),(8,2),(12,1),(12,2),(12,4),(16,1),(16,2),(16,4),(16,8)]
for r,M in growing:
 ck(M<=2**(r//4-1))
 lower,_=trunc_error(r,M-1)
 required=(F(9,8)**r/18-F(2)**(-r-1))/M
 ck(required>0);ck(lower>=required)
d={'status':'PASS','actual_integer_Walsh_transforms':3,'fixed_order_cases':96,'growing_order_cases':10,'exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,'scope':'Independent support for A044 full analytic obstruction; no FEI disproof'}
(R/'out/REVIEW_CHECKS.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8');print(json.dumps(d))
