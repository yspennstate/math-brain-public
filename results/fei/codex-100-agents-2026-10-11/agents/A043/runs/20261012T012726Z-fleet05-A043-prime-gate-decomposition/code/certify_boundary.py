from fractions import Fraction as F
from pathlib import Path
import itertools,json,time
OUT=Path(__file__).resolve().parents[1]/'out'; start=time.perf_counter()
def ln_bounds(x):
 z=(x-1)/(x+1); z2=z*z; t=z; s=F(0)
 for j in range(32): s+=2*t/(2*j+1); t*=z2
 return s,s+2*t/(65*(1-z2))
ln2lo,ln2hi=ln_bounds(F(2))
def log_bounds(x):
 k=x.numerator.bit_length()-x.denominator.bit_length(); y=x/F(2)**k
 if y<1: k-=1; y*=2
 if y>=2: k+=1; y/=2
 assert 1<=y<2
 lo,hi=ln_bounds(y)
 return F(k)+lo/ln2hi,F(k)+hi/ln2lo
rows=[]; assertions=0
for k in range(1,13):
 q=F(1,2**k); r=q**3; probs=[1-r,q,q]; sig2=[4*p*(1-p) for p in probs]
 spectrum=[]
 for S in range(8):
  moment=F(0)
  for x in range(8):
   val=1 if x.bit_count()>=2 else -1; weight=F(1); char=F(1)
   for i,p in enumerate(probs):
    y=(x>>i)&1; weight*=p if y else 1-p
    if S&(1<<i): char*=y-p
   moment+=val*weight*char
  v=F(1)
  for i,p in enumerate(probs):
   if S&(1<<i): v*=p*(1-p)
  spectrum.append(moment**2/v)
 p1=16*r*(1-r)*q*q*(1-q)**2
 p2=4*q*(1-q)*(1-r-q+2*r*q)**2
 p12=4*r*(1-r)*q*(1-q)*(1-2*q)**2
 p23=4*q*q*(1-q)**2*(1-2*r)**2
 p123=16*r*(1-r)*q*q*(1-q)**2
 closed=[None,p1,p2,p12,p2,p12,p23,p123]
 for S in range(1,8): assert spectrum[S]==closed[S]; assertions+=1
 assert sum(spectrum)==1;assertions+=1
 deficit=sum((S.bit_count()-1)*spectrum[S] for S in range(1,8)); assert deficit>0;assertions+=1
 lo=hi=F(0)
 for S in range(1,8):
  p=spectrum[S]
  if not p: continue
  sigma=F(1)
  for i in range(3):
   if S&(1<<i): sigma*=sig2[i]
  assert sigma>=p;assertions+=1
  l,u=log_bounds(sigma/p);lo+=p*l;hi+=p*u
 # Export concise decimal rational brackets, certified by exact comparisons.
 scale=10**10; a=(lo/deficit)*scale; b=(hi/deficit)*scale
 lower=a.numerator//a.denominator; upper=-((-b.numerator)//b.denominator)
 row={'k':k,'q':str(q),'r':str(r),'deficit':str(deficit),'spectrum':[str(x) for x in spectrum],'ratio_lower':str(F(lower,scale)),'ratio_upper':str(F(upper,scale))}
 rows.append(row)
 assert time.perf_counter()-start<50
 data={'helper':'A043-prime-majority-boundary-v1','complete':False,'arithmetic':'exact Fraction and rational log intervals','rows':rows,'assertions':assertions}
 (OUT/'boundary_certificate.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
data.update(complete=True,runtime_seconds=time.perf_counter()-start)
(OUT/'boundary_certificate.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'assertions':assertions,'runtime_seconds':data['runtime_seconds'],'rows':[{k:v for k,v in x.items() if k in ['k','ratio_lower','ratio_upper']} for x in rows]},indent=2))
