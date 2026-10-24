from pathlib import Path
from fractions import Fraction as F
from math import comb
from functools import lru_cache
import argparse,json,time
R=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x
 checks+=1
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 return x
def write(name,obj):(R/'out'/name).write_text(json.dumps(encode(obj),indent=2),encoding='utf-8')
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def series(z):
 t=z;s=F(0)
 for j in range(32):s+=2*t/(2*j+1);t*=z*z
 return s,s+2*t/(65*(1-z*z))
LN=series(F(1,3));D=1<<80;Z=1<<128
@lru_cache(None)
def lg(x):
 ck(x>0);y=x;k=0
 while y<1:y*=2;k-=1
 while y>=2:y/=2;k+=1
 z=(y-1)/(y+1);loz=F((z*Z).__floor__(),Z);hiz=F((z*Z).__ceil__(),Z)
 lo=k+series(loz)[0]/LN[1];hi=k+series(hiz)[1]/LN[0]
 return F((lo*D).__floor__(),D),F((hi*D).__ceil__(),D)
def entropy(vals):
 ans=(F(0),F(0))
 for p in vals:
  if p:ans=sub(ans,scale(lg(p),p))
 return ans
def fwht(t):
 a=list(t);s=1
 while s<len(a):
  for j in range(0,len(a),2*s):
   for i in range(j,j+s):u,v=a[i],a[i+s];a[i],a[i+s]=u+v,u-v
  s*=2
 return a
def poly_mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def peval(c,x):
 ans=F(0)
 for z in c[::-1]:ans=ans*x+z
 return ans
NEG={0,1,2,4,8,16,32,6,17,40}
H=[-1 if x in NEG else 1 for x in range(64)]
J=[-H[x^1] for x in range(64)]
gates={'h':H,'J':J};w={k:[F(x,64) for x in fwht(v)] for k,v in gates.items()}
T=[12,-28,27,-12,2];A=[1,4,-2]
AT=poly_mul(A,T);gap=[F(4),F(-28),F(109),F(-152),F(100),F(-32),F(4)]
ck(gap==[F(16 if j==0 else -8 if j==1 else 0)-AT[j] for j in range(7)])
boxes=[]
for b in range(16):
 a=F(b,16);width=F(1,16)
 power=[sum(gap[j]*comb(j,k)*a**(j-k)*width**k for j in range(k,7)) for k in range(7)]
 bern=[sum(power[j]*F(comb(k,j),comb(6,j)) for j in range(k+1)) for k in range(7)]
 ck(min(bern)>0);boxes.append({'left':a,'right':a+width,'bernstein_coefficients':bern})
write('BERNSTEIN.json',{'polynomial':gap,'boxes':boxes,'verdict':'STRICTLY_POSITIVE on [0,1]; hence Q_h*v >=(3/2)*Var(h)'})
ck(F(313875,262144)>F(19,16));ck(F(1003275,8388608)>F(1,9))
ck(F(76,15)<8);ck(F(120,11)*F(15,32)==F(225,44));ck(3*(8+F(225,44))==F(1731,44)<40)
def outer(which,p):
 m=1-2*p;v=4*p*(1-p);coef=w[which];mass=[];raw=[]
 for s in range(64):
  a=sum(coef[t]*m**((t^s).bit_count()) for t in range(64) if t&s==s)
  raw.append(a);mass.append(v**s.bit_count()*a*a)
 ck(sum(mass)==1);ck(all(abs(x)<=1 for x in raw))
 var=1-raw[0]**2;qs=[]
 for j in range(6):
  phys=F(0)
  for x in range(64):
   if x&(1<<j):continue
   k=x.bit_count();weight=p**k*(1-p)**(5-k)
   phys+=weight*F((gates[which][x]-gates[which][x|(1<<j)])**2,4)
  ck(sum(mass[s] for s in range(64) if s&(1<<j))==v*phys);qs.append(phys)
 Q=sum(qs);ck(Q*v>=var)
 if which=='h':
  q=2*p*(1-p)**3*(2-p);ck(all(x==q for x in qs));ck(2*Q*v>=3*var)
 else:
  outp=(1-raw[0])/2
  sig=4*p-10*p*p+18*p**3-19*p**4+10*p**5-2*p**6
  ck(outp==sig)
  if p<=F(1,16):
   ck(3*p<outp<4*p);ck(Q>=F(11,4));ck(all(min(q,1-q)<=5*p for q in qs))
 Hp=entropy(mass);C=sub(Hp,scale(entropy([v,1-v]),Q))
 return mass,raw,qs,Q,var,C
profiles=[]
domain=[('h',x if x<=F(7,32) else 1-x) for x in [F(1,16),F(1,8),F(7,32),F(1,4),F(3,8),F(1,2),F(1,32),F(1,64)]]+[('J',F(1,2**k)) for k in [4,5,6,8]]
if args.pilot:domain=[domain[0],domain[3],domain[6],domain[8]]
else:
 prior=R.parents[0]/'20261014T005622Z-account05-A080-universal-counterexample-standard/out/VALIDATION.json'
 old=json.loads(prior.read_text(encoding='utf-8'));domain.append(('J',F(old['records'][3]['minority'])))
for which,p in domain:
 mass,raw,qs,Q,var,C=outer(which,p);v=4*p*(1-p)
 if which=='h':ck(C[1]<=8*Q*v)
 else:
  # Certified upper bound using ln2 interval for log2(e), not its float value.
  logbound=sub((1/LN[1],1/LN[0]),lg(5*p))
  rhs=scale(logbound,F(120,11)*p)
  ck(C[1]/(Q*v)<=rhs[0])
 profiles.append({'gate':which,'p':p,'Q':Q,'input_variance':v,'output_variance':var,'mu_contraction':var/(Q*v),'C_interval':C,'C_over_Qv_interval':scale(C,1/(Q*v))})
 write('PILOT_PROFILES.json' if args.pilot else 'PROFILES.json',{'profiles':profiles,'assertions':checks})
 ck(time.perf_counter()-start<(60 if args.pilot else 180))
physical=[]
core_masks=[1] if args.pilot else list(range(1,15))
for mask in core_masks:
 truth=[-1 if mask&(1<<x) else 1 for x in range(4)]
 sw=fwht(truth);sp=[F(x*x,16) for x in sw];v=1-sp[0];pg=F(mask.bit_count(),4)
 Ig=sum(s.bit_count()*z for s,z in enumerate(sp));Hg=entropy(sp)
 for which in ['h','J']:
  mass,raw,qs,Q,var,C=outer(which,pg)
  parent=[]
  for x in range(1<<12):
   index=sum((truth[(x>>(2*j))&3]<0)<<j for j in range(6));parent.append(gates[which][index])
  pw=fwht(parent);pp=[F(x*x,1<<24) for x in pw]
  ck(sum(pp)==1); Ip=sum(s.bit_count()*z for s,z in enumerate(pp));ck(Ip==Q*Ig)
  ck(1-pp[0]==var);ck(var/Ip<=v/Ig)
  if which=='h':ck(var/Ip<=F(2,3)*v/Ig)
  for s in range(1<<12):
   occupied=sum(bool(s&(3<<(2*j)))<<j for j in range(6));expected=mass[occupied]
   for j in range(6):
    inner=(s>>(2*j))&3
    if inner:expected*=sp[inner]/v
   ck(pp[s]==expected)
  for j in range(6):
   for i in range(2):
    di=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(4)),4)
    dpi=F(sum(parent[x]!=parent[x^(1<<(2*j+i))] for x in range(1<<12)),1<<12)
    ck(dpi==qs[j]*di)
  direct=entropy(pp);predicted=add(scale(Hg,Q),C)
  ck(max(direct[0],predicted[0])<=min(direct[1],predicted[1]))
  physical.append({'core_mask':mask,'gate':which,'I':Ip,'variance':var,'mu':var/Ip})
 ck(time.perf_counter()-start<(60 if args.pilot else 180))
write('PILOT_PHYSICAL.json' if args.pilot else 'PHYSICAL.json',{'cases':physical})
out={'status':'PASS','assertions':checks,'runtime_seconds':time.perf_counter()-start,'bernstein_boxes':len(boxes),'scalar_profiles':len(profiles),'physical_compositions':len(physical),'all_dimensional_upper_budget':'R_out<=R_seed+(1731/44)*Var(seed)/I(seed)<R_seed+40; for the named common-policy/complete one-flip escape strategy only'}
write('PILOT.json' if args.pilot else 'VALIDATION.json',out);print(json.dumps(out,indent=2))
