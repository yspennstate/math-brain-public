from fractions import Fraction as F
from pathlib import Path
import math,json,time,hashlib
R=Path(__file__).resolve().parents[1];START=time.perf_counter();COUNT=0
def ck(x):
 global COUNT
 assert x
 COUNT+=1
 if time.perf_counter()-START>55:raise TimeoutError('frozen55s')
def spectrum(t):
 p={}
 for s in range(len(t)):
  h=sum(v*(-1 if (z&s).bit_count()%2 else 1) for z,v in enumerate(t))
  if h:p[s]=F(h*h,len(t)**2)
 ck(sum(p.values())==1);return p
def restriction(t,j,b):return tuple(v for z,v in enumerate(t) if (z>>j)&1==b)
def fresh(p,a):
 full=0
 for s in p:full|=s
 q={s:(1-a)*v for s,v in p.items()};q[0]=p.get(0,F(0));q[full]=q.get(full,F(0))+a*(1-p.get(0,F(0)))
 return {s:v for s,v in q.items() if v}
def erased(p,j):
 out={}
 for s,v in p.items():
  k=s%(1<<j)+((s>>(j+1))<<j);out[k]=out.get(k,F(0))+v
 return out
def lift(t,q,eps):
 mu=F(sum(t),len(t));d={0:(eps+mu)**2/4,1:(eps-mu)**2/4}
 for s,v in q.items():
  if s:d[2*s]=v/4;d[2*s+1]=v/4
 return {s:v for s,v in d.items() if v}
def construct(r,balanced):
 t=[]
 for v in range(1<<(r+1+int(balanced))):
  a=v%2;z=(v//2)%(1<<r);b=z%2;c=(z//2)%2;d=(z//4)%2
  value=1-2*(d if b else c)
  if z==1 or (a and z in [4,5]):value=-value
  if balanced and v>>(r+1):value=-value
  t.append(value)
 return tuple(t)
rows=[]
for r in [4,5]:
 for a in [F(1,6),F(1,7)]:
  for balanced in [False,True]:
   core=construct(r,balanced);pc=spectrum(core);qc=fresh(pc,a)
   children=[restriction(core,0,b) for b in [0,1]];childps=[spectrum(z) for z in children]
   full=(1<<(r+int(balanced)))-1;t0=childps[0][full];t1=childps[1][full];E=(t0+t1)/2
   ck(t0==F(4,1<<(2*r)) and t1==F(36,1<<(2*r)))
   ck(sum(core[z]!=core[z^1] for z in range(len(core)))==len(core)*F(2,1<<r))
   for mode in [0,-1,1]:
    if mode:
     t=tuple(mode if not z%2 else core[z//2] for z in range(2*len(core)));q=lift(core,qc,mode);j=1
     freshlaws=[lift(z,fresh(p,a),mode) for z,p in zip(children,childps)]
    else:t=core;q=qc;j=0;freshlaws=[fresh(p,a) for p in childps]
    p=spectrum(t);ck(set(p)==set(q));pe=erased(p,j);qe=erased(q,j)
    cps=[spectrum(restriction(t,j,b)) for b in [0,1]];out=[];old=[]
    for b in [0,1]:
     joint={s:v*cps[b].get(s,F(0))/(2*pe[s]) for s,v in qe.items()}
     rb=sum(joint.values());out.append(rb);old.append({s:v/rb for s,v in joint.items() if v})
    u=0 if balanced else F(4,1<<(2*r));c=a*(1-u);eta=F(4,5)*c/(2 if mode else 1)
    ck(out==[(1-eta)/2,(1+eta)/2])
    den=math.lcm(*(2*v.denominator for p in cps for v in p.values()));product=F(1)
    for b in [0,1]:
     ck(set(cps[b])==set(old[b])==set(freshlaws[b]))
     for s,v in cps[b].items():
      target=s//2 if mode else s;tb=t0 if b==0 else t1
      ratio=((1-a+c/E)/(1-a+c/tb) if target==full else F(1))/(2*out[b])
      ck(old[b][s]/freshlaws[b][s]==ratio)
      exponent=den*v/2;ck(exponent.denominator==1);product*=ratio**int(exponent)
    ck(product>1)
    if a==F(1,6):
     bound=512 if mode else 128;ck(den%bound==0);ck(product>2**(den//bound))
    def digest(n):return hashlib.sha256(n.to_bytes((n.bit_length()+7)//8,'big')).hexdigest()
    rows.append({'r':r,'alpha':str(a),'balanced':balanced,'mode':mode,'exact_sigma':'log2(numerator/denominator)/'+str(den),'product_numerator_sha256':digest(product.numerator),'product_denominator_sha256':digest(product.denominator),'product_numerator_bits':product.numerator.bit_length(),'product_denominator_bits':product.denominator.bit_length(),'reference_outcomes':list(map(str,out)),'positive_integer_comparison':True,'strict_frozen_threshold_at1/6':a==F(1,6)})
result={'status':'PASS','cases':len(rows),'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'method':'independent literal characters, actual rational coherent kernels, exact normalized atom likelihoods and rational-power integer sign, no producer/helper import','rows':rows}
(R/'out/REPRODUCTION.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'));print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
