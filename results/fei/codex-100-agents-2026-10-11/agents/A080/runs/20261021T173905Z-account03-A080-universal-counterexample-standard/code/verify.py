from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import argparse, json, time, hashlib, sys
sys.set_int_max_str_digits(100000)
R=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
start=time.perf_counter();checks=0
def ck(b):
 global checks
 assert b
 checks+=1
def dump(n,x):
 (R/'out'/n).write_text(json.dumps(x,indent=2,default=str),encoding='utf-8')
def series(z):
 s=F(0);w=z
 for j in range(32):s+=2*w/(2*j+1);w*=z*z
 return s,s+2*w/(65*(1-z*z))
LN=series(F(1,3));Z=1<<128;D=1<<80
@lru_cache(None)
def lg(x):
 assert x>0
 k=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**k
 if y<1:y*=2;k-=1
 z=(y-1)/(y+1)
 lo=k+series(F((z*Z).__floor__(),Z))[0]/LN[1]
 hi=k+series(F((z*Z).__ceil__(),Z))[1]/LN[0]
 return F((lo*D).__floor__(),D),F((hi*D).__ceil__(),D)
def ell(x):
 if not x:return F(0),F(0)
 if x>F(1,2):
  # Avoid cancellation and fixed absolute errors when x is 1-O(2^-k).
  # ln(1/x)=2*atanh((1-x)/(1+x)); the positive tail scales with 1-x.
  l,h=series((1-x)/(1+x))
  return x*l/LN[1],x*h/LN[0]
 l,h=lg(x);return -x*h,-x*l
def add(*xs):return sum(x[0] for x in xs),sum(x[1] for x in xs)
def scale(c,x):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def ent(xs):return add(*(ell(x) for x in xs))
def overlap(x,y):return max(x[0],y[0])<=min(x[1],y[1])
def walsh(tab):
 w=list(tab);s=1
 while s<len(w):
  for j in range(0,len(w),2*s):
   for i in range(j,j+s):u,v=w[i],w[i+s];w[i],w[i+s]=u+v,u-v
  s*=2
 return [F(x,len(w)) for x in w]
def grouped(H,p,k):
 a=F(1,1<<k);m=1-2*p
 return add(scale(a,sub(H,ell(m*m))), (2*a*k*(1-m*m),)*2,
            ell((1-2*a*p)**2),scale((1<<k)-1,ell(4*a*a*p*p)))
def normalized(H,I,p,k):
 a=F(1,1<<k);v=4*a*p*(1-a*p);hf=grouped(H,p,k)
 hb=ent([a*p,1-a*p]);hv=ent([v,1-v]);gap=sub((I,I),hb)
 ck(gap[0]>0)
 # Uniform errors are certified with outward rational entropy intervals.
 er=sub(scale(1/a,hf),add(H,(8*k*p,)*2))
 ck(er[0]>=-32 and er[1]<=32)
 c=sub(scale(1/a,hb),(k*p,)*2);ck(c[0]>=0 and c[1]<=3)
 ec=sub(scale(1/a,hv),(4*k*p,)*2);ck(ec[0]>=-16 and ec[1]<=16)
 cn=sub(scale(1/a,sub(hf,hv)),add(H,(4*k*p,)*2))
 ck(cn[0]>=-48 and cn[1]<=48)
 return hf,gap,hv
records=[]
for mask in ([1,6] if args.pilot else range(1,15)):
 seed=[-1 if mask>>i&1 else 1 for i in range(4)]
 sw=walsh(seed);sp=[x*x for x in sw];hs=ent(sp);Is=sum(i.bit_count()*sp[i] for i in range(4))
 for t in ([1] if args.pilot else [1,2,3]):
  nt=2*t;gt=[]
  for x in range(1<<nt):
   v=1
   for j in range(t):v*=seed[(x>>(2*j))&3]
   gt.append(v)
  gw=walsh(gt);gp=[x*x for x in gw];p=F(gt.count(-1),len(gt))
  ck(gw[0]==sw[0]**t);ck(overlap(ent(gp),scale(t,hs)))
  for k in ([1,3] if args.pilot else [1,2,3,5]):
   a=F(1,1<<k);tab=[gt[x&((1<<nt)-1)] if x>>nt==0 else 1 for x in range(1<<(nt+k))]
   fw=walsh(tab);fp=[x*x for x in fw];pred=[]
   for T in range(1<<k):
    for S in range(1<<nt):pred.append((1-2*a*p)**2 if T==S==0 else 4*a*a*p*p if S==0 else a*a*gp[S])
   ck(fp==pred);ck(sum(fp)==1)
   I=sum(i.bit_count()*fp[i] for i in range(len(fp)));ck(I==a*(t*Is+2*k*p))
   for j in range(nt+k):
    edge=F(sum(tab[x]!=tab[x^(1<<j)] for x in range(len(tab))),len(tab))
    ck(edge==sum(fp[i] for i in range(len(fp)) if i>>j&1))
   hf,gap,hv=normalized(scale(t,hs),I,p,k);ck(overlap(hf,ent(fp)))
   records.append({'mask':mask,'t':t,'k':k,'I':I,'H':hf,'gap':gap,'h2_variance':hv})
   dump('PILOT_CASES.json' if args.pilot else 'BOOLEAN_CASES.json',records)
scalar=[]
for p in ([F(1,2)] if args.pilot else [F(1,16),F(1,8),F(1,4),F(1,2),F(3,4),F(15,16)]):
 for k in ([4] if args.pilot else [1,2,4,8,16,32,64]):
  # Scalar remainder checks do not claim every p,H pair is Boolean.
  a=F(1,1<<k);normalized((F(0),F(0)),a*(4+2*k*p),p,k)
  scalar.append({'p':p,'k':k})
# An independent closed spectrum: activate a dictator tensor, which is a parity.
# Its data law has one atom, and the two nonempty categories have equal masses.
phases=[]
for k in ([8] if args.pilot else [8,32,128,512]):
 for t in ([1] if args.pilot else [1,k,k*k]):
  a=F(1,1<<k);hf=add(ell((1-a)**2),scale((1<<(k+1))-1,ell(a*a)))
  I=a*(t+k);v=2*a-a*a;gap=sub((I,I),ent([a/2,1-a/2]))
  cn=sub(hf,ent([v,1-v]));den=t+F(k,2);K=F(8)
  ck(overlap(hf,grouped((F(0),F(0)),F(1,2),k)))
  ck(hf[1]/I<=4+F(32,t+k))
  ck(cn[1]/I<=2+F(48,t+k))
  if den>3:ck(hf[1]/gap[0]<=K+(32+3*K)/(den-3))
  phases.append({'k':k,'t':t,'ordinary':scale(1/I,hf),'gap_ratio':(hf[0]/gap[1],hf[1]/gap[0]),'conditioned':scale(1/I,cn)})
dump('PILOT_PHASES.json' if args.pilot else 'PHASES.json',phases)
ck(time.perf_counter()-start<55)
out={'verdict':'PASS','boolean_fixtures':len(records),'scalar_cases':len(scalar),'closed_parity_cases':len(phases),'assertions':checks,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh, Fraction, outward 80-bit log bounds; 32 positive atanh terms with geometric tail','memory':'estimated <100 MB; not measured'}
dump('PILOT.json' if args.pilot else 'VALIDATION.json',out);print(json.dumps(out))
