from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,argparse
R=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
start=time.perf_counter();checks=0
def ck(b):
 global checks
 assert b
 checks+=1
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [enc(v) for v in x]
 return x
def write(n,x):(R/'out'/n).write_text(json.dumps(enc(x),indent=2),encoding='utf-8')
def series(z):
 t=z;s=F(0)
 for j in range(32):s+=2*t/(2*j+1);t*=z*z
 return s,s+2*t/(65*(1-z*z))
LN=series(F(1,3));D=1<<80;Z=1<<128
@lru_cache(None)
def lg(x):
 y=x;k=0
 while y<1:y*=2;k-=1
 while y>=2:y/=2;k+=1
 z=(y-1)/(y+1)
 lo=k+series(F((z*Z).__floor__(),Z))[0]/LN[1]
 hi=k+series(F((z*Z).__ceil__(),Z))[1]/LN[0]
 return F((lo*D).__floor__(),D),F((hi*D).__ceil__(),D)
def ent(vals):
 lo=hi=F(0)
 for p in vals:
  if p:
   l,h=lg(p);lo-=p*h;hi-=p*l
 return lo,hi
def walsh(tab):
 a=list(tab);s=1
 while s<len(a):
  for j in range(0,len(a),2*s):
   for i in range(j,j+s):u,v=a[i],a[i+s];a[i],a[i+s]=u+v,u-v
  s*=2
 return [F(x,len(a)) for x in a]
records=[]
for mask in ([1,6] if args.pilot else range(1,15)):
 seed=[-1 if mask>>x&1 else 1 for x in range(4)]
 sw=walsh(seed);sp=[x*x for x in sw];Hs=ent(sp)
 Is=sum(s.bit_count()*sp[s] for s in range(4))
 for t in ([1] if args.pilot else [1,2,3]):
  nt=2*t
  G=[]
  for x in range(1<<nt):
   val=1
   for j in range(t):val*=seed[(x>>(2*j))&3]
   G.append(val)
  gw=walsh(G);gp=[x*x for x in gw];p=F(G.count(-1),len(G));m=1-2*p
  Ig=sum(s.bit_count()*gp[s] for s in range(len(gp)))
  ck(Ig==t*Is);ck(gw[0]==sw[0]**t)
  for k in ([1,2] if args.pilot else [1,2,3]):
   a=F(1,1<<k);tab=[G[x&((1<<nt)-1)] if x>>nt==0 else 1 for x in range(1<<(nt+k))]
   fw=walsh(tab);fp=[x*x for x in fw];expected=[]
   for T in range(1<<k):
    for S in range(1<<nt):
     expected.append((1-2*a*p)**2 if T==S==0 else (4*a*a*p*p if S==0 else a*a*gp[S]))
   ck(fp==expected);ck(sum(fp)==1)
   If=sum(s.bit_count()*fp[s] for s in range(len(fp)))
   ck(If==a*(t*Is+2*k*p));ck(F(tab.count(-1),len(tab))==a*p)
   for j in range(nt+k):
    edge=F(sum(tab[x]!=tab[x^(1<<j)] for x in range(len(tab))),len(tab))
    pred=2*a*p if j>=nt else a*sum(gp[s] for s in range(len(gp)) if s>>j&1)
    ck(edge==pred);ck(edge==sum(fp[s] for s in range(len(fp)) if s>>j&1))
   HF=ent(fp)
   # Exact mass identity gives H(F)>=a(t H(seed)-1).
   ck(HF[0]>=a*(t*Hs[1]-1))
   # Complete entropy formula, independent grouped evaluation.
   HG=ent(gp);em=ent([m*m]);e0=ent([(1-2*a*p)**2]);sel=ent([4*a*a*p*p])
   lo=a*(HG[0]-em[1]+2*k*(1-m*m))+e0[0]+((1<<k)-1)*sel[0]
   hi=a*(HG[1]-em[0]+2*k*(1-m*m))+e0[1]+((1<<k)-1)*sel[1]
   ck(max(lo,HF[0])<=min(hi,HF[1]))
   outp=a*p;hb=ent([outp,1-outp]);gap=(If-hb[1],If-hb[0])
   if outp<=F(1,16):ck(gap[0]>=F(5,16)*If)
   records.append({'seed_mask':mask,'t':t,'k':k,'p':outp,'I':If,'H_interval':HF,'output_gap_interval':gap})
   write('PILOT_CASES.json' if args.pilot else 'CASES.json',records)
# Analytic schedules: verify ceiling and uniform vanishing envelope on fixed cases.
schedule=[]
for mask in range(1,15):
 sw=walsh([-1 if mask>>x&1 else 1 for x in range(4)]);Is=sum(s.bit_count()*sw[s]**2 for s in range(4))
 for k in [4,8,16,32]:
  t=(F(k*k)/Is).__ceil__();TI=t*Is;a=F(1,1<<k)
  ck(k*k<=TI<=k*k+k);ck(a*(TI+2*k)<=a*(k*k+3*k))
  schedule.append({'mask':mask,'k':k,'t':t,'I_upper':a*(k*k+3*k),'bias_upper':a})
write('SCHEDULE.json',schedule)
ck(time.perf_counter()-start<60)
write('PILOT.json' if args.pilot else 'VALIDATION.json',{'verdict':'PASS','case_count':len(records),'assertions':checks,'elapsed_seconds':time.perf_counter()-start,'peak_memory':'unmeasured; estimate50MB','schedule_cases':len(schedule)})
print(json.dumps({'verdict':'PASS','case_count':len(records),'assertions':checks,'elapsed_seconds':time.perf_counter()-start}))
