from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from collections import defaultdict
import json,time,sys,hashlib
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';OUT.mkdir(exist_ok=True)
CASES=[(r,m) for r,m in [(2,1),(3,1),(4,1),(5,1),(2,2),(3,2)]]
def dump(n,v):(OUT/n).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
if '--freeze' in sys.argv:
 dump('FROZEN_SPEC.json',{'helper_version':'check.py-v1','sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'F_h priority selector with m disjoint width-r point defects; initial full-spike1/8 lift; b then a, reset both a children to full-spike1/7 lift; query first data bit on any subset of the two a children and reset queried children to full-spike1/7 lift','domain':CASES,'cases':18,'symmetry':'homogeneous factor and coordinate permutations; first physical data coordinate represents all data coordinates; all three nonempty subsets of a branches queried','arithmetic':'integer Walsh, Fraction probabilities, exact atomwise likelihood chain, rational logarithm intervals with geometric tails','memory_estimate_mb':80,'maximum_runtime_seconds':55,'pilot':'r2m1,r3m1; six policies, below60s','dimension_cap':9})
 print('FROZEN');sys.exit()
START=time.perf_counter();NCK=0
def ck(v):
 global NCK
 assert v;NCK+=1
 if time.perf_counter()-START>55:raise TimeoutError('frozen runtime cap')
def add(*a):return sum((x[0] for x in a),F()),sum((x[1] for x in a),F())
def scale(a,k):return (k*a[0],k*a[1]) if k>=0 else (k*a[1],k*a[0])
def exact(x):return (F(x),F(x))
def rawln(x):
 z=(x-1)/(x+1);p=z;s=F()
 for j in range(32):s+=2*p/(2*j+1);p*=z*z
 return s,s+2*p/(65*(1-z*z))
LN2=rawln(F(2));GRID=1<<80
def roundout(a):return F(a[0].numerator*GRID//a[0].denominator,GRID),F(-((-a[1].numerator*GRID)//a[1].denominator),GRID)
@lru_cache(None)
def lg(x):
 assert x>0
 k=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**k
 if y<1:k-=1;y*=2
 lo,hi=rawln(y)
 return roundout((k+lo/LN2[1],k+hi/LN2[0]))
def H(p):return add(*(scale(lg(v),-v) for v in p.values() if v))
def KL(p,q):
 ck(sum(p.values())==sum(q.values())==1);ck(all(q.get(s,0)>0 for s in p))
 return add(*(scale(lg(v/q[s]),v) for s,v in p.items()))
def enc(a):return [str(v) for v in roundout(a)]
def spec(t):
 a=list(t);n=len(a);h=1
 while h<n:
  for b in range(0,n,2*h):
   for j in range(b,b+h):x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
  h*=2
 p={s:F(x*x,n*n) for s,x in enumerate(a) if x};ck(sum(p.values())==1);return p
def restrict(t,j,b):return tuple(t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(t)//2))
def infl(t):
 return sum((F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(len(t).bit_length()-1)),F())
def erase(s,j):return (s&((1<<j)-1))|((s>>(j+1))<<j)
def push(p,j):
 q=defaultdict(F)
 for s,v in p.items():q[erase(s,j)]+=v
 return dict(q)
def query(t,q,j):
 p=spec(t);pe=push(p,j);qe=push(q,j);child=[];E=exact(0);O=exact(0)
 # Conditional-erasure KL, retaining all source/reference rows.
 for s,v in p.items():E=add(E,scale(lg((v/pe[erase(s,j)])/(q[s]/qe[erase(s,j)])),v))
 for b in (0,1):
  tt=restrict(t,j,b);pp=spec(tt)
  kernel={s:pp.get(s,F())/(2*pe[s]) if pe.get(s,0) else F(1,2) for s in qe}
  z=sum((qe[s]*kernel[s] for s in qe),F());ck(z>0)
  qq={s:qe[s]*kernel[s]/z for s in qe if qe[s]*kernel[s]};ck(sum(qq.values())==1)
  for s,v in p.items():
   T=erase(s,j)
   if kernel.get(T,0):ck(v/q[s]==((v/pe[T])/(q[s]/qe[T]))*F(1,2)/z*pp[T]/qq[T])
  O=add(O,scale(lg(F(1,2)/z),F(1,2)))
  child.append((tt,qq))
 return child,E,O
def core(r,m):return tuple((-1)**sum((z>>(r*j))&((1<<r)-1)==(1<<r)-1 for j in range(m)) for z in range(1<<(r*m)))
def coreq(widths,alpha):
 q={0:F(1)};shift=0
 for w in widths:
  if w==0:p={0:F(1)}
  elif w==1:p={1:F(1)}
  else:
   d=F(1,1<<w);var=4*d*(1-d);p={0:(1-2*d)**2}
   for s in range(1,1<<w):p[s]=(1-alpha)*4*d*d+(alpha*var if s==(1<<w)-1 else 0)
  q={s|(u<<shift):v*z for s,v in q.items() for u,z in p.items() if v*z};shift+=w
 ck(sum(q.values())==1);return q
def Jtable(h,sign):return tuple(sign if not u&1 else h[u>>1] for u in range(2*len(h)))
def Jref(h,widths,sign):
 p=spec(Jtable(h,sign));q=coreq(widths,F(1,7));out={s:v for s,v in p.items() if s>>1==0}
 for s,v in q.items():
  if s:
   out[s<<1]=v/4;out[(s<<1)|1]=v/4
 ck(sum(out.values())==1);return out
def Ftable(h):return tuple((-1 if u&2 else 1) if not u&1 else h[u>>3] if u&4 else 1 for u in range(8*len(h)))
def Fref(h,widths):
 p=spec(Ftable(h));q=coreq(widths,F(1,8));out={s:v for s,v in p.items() if not s>>3}
 for s,v in q.items():
  if s:
   for c in (0,1,4,5):out[(s<<3)|c]=v/16
 ck(sum(out.values())==1);return out
def calc(r,m):
 h=core(r,m);root=Ftable(h);qroot=Fref(h,[r]*m);p0=spec(root);H0=H(p0);I0=infl(root);A0=KL(p0,qroot)
 bc,Eb,Ob=query(root,qroot,2);ab,Ea,Oa=query(*bc[1],1)
 incoming=[];sigma1=exact(0)
 for c in (0,1):
  tt,old=ab[c];sign=1-2*c;fresh=Jref(h,[r]*m,sign);ck(tt==Jtable(h,sign))
  kold=KL(spec(tt),old);knew=KL(spec(tt),fresh)
  sigma1=add(sigma1,scale(add(knew,scale(kold,-1)),F(1,4)));incoming.append((tt,fresh))
 rows=[]
 for mask in (1,2,3):
  leaves=[(bc[0][0],bc[0][1],F(1,2))];sigma2=exact(0);branch_delta=[];E2=exact(0);O2=exact(0)
  for c in (0,1):
   tt,qq=incoming[c]
   if not mask>>c&1:leaves.append((tt,qq,F(1,4)));continue
   ch,ee,oo=query(tt,qq,1);E2=add(E2,scale(ee,F(1,4)));O2=add(O2,scale(oo,F(1,4)))
   for b in (0,1):
    tch,old=ch[b];hh=restrict(h,0,b)
    widths=[0 if b==0 else r-1]+[r]*(m-1)
    # Inactive first block loses all r-1 dummy bits, but masks must preserve them.
    compact=coreq([r-1]+[r]*(m-1),F(1,7)) if b else {s<<(r-1):v for s,v in coreq([r]*(m-1),F(1,7)).items()}
    pp=spec(tch);fresh={s:v for s,v in pp.items() if not s>>1}
    for s,v in compact.items():
     if s:fresh[s<<1]=v/4;fresh[(s<<1)|1]=v/4
    ck(tch==Jtable(hh,1-2*c));ck(sum(fresh.values())==1)
    oldKL=KL(pp,old);newKL=KL(pp,fresh);delta=add(newKL,scale(oldKL,-1));branch_delta.append({'a':c,'data':b,'delta':enc(delta)})
    sigma2=add(sigma2,scale(delta,F(1,8)));leaves.append((tch,fresh,F(1,8)))
  Hf=add(*(scale(H(spec(tt)),w) for tt,qq,w in leaves));If=sum((w*infl(tt) for tt,qq,w in leaves),F());S=add(exact(4*If),scale(Hf,-1));e=add(H0,scale(Hf,-1),exact(-4*(I0-If)))
  liability=add(A0,e,sigma1,sigma2);positive=(max(F(0),liability[0]),max(F(0),liability[1]));remaining=add(S,scale(positive,-1),exact(-F(1,4)))
  ck(remaining[0]>F(3,4));ck(S[0]>1)
  fullchain=add(Eb,Ob,scale(add(Ea,Oa),F(1,2)),E2,O2,add(*(scale(KL(spec(tt),qq),w) for tt,qq,w in leaves)))
  reset_source=add(A0,sigma1,sigma2);ck(fullchain[0]<=reset_source[1] and reset_source[0]<=fullchain[1])
  rows.append({'r':r,'m':m,'mask':mask,'n':3+r*m,'sigma1':enc(sigma1),'sigma2':enc(sigma2),'S':enc(S),'old_quarter':str(F(1,4)),'remaining':enc(remaining),'branch_delta':branch_delta})
 return rows
rows=[]
for r,m in (CASES[:2] if '--pilot' in sys.argv else CASES):rows+=calc(r,m)
res={'status':'PASS','cases':len(rows),'assertions':NCK,'seconds':time.perf_counter()-START,'rows':rows}
dump('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json',res)
print('PASS',len(rows),NCK,res['seconds'])
for x in rows:print(x['r'],x['m'],x['mask'],'sigma2',*[float(F(t)) for t in x['sigma2']],'remaining',float(F(x['remaining'][0])))
