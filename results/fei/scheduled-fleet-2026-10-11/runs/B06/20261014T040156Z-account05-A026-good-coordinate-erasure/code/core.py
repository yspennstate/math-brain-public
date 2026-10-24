import sys,json
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'out').mkdir(exist_ok=True)
OLD=ROOT.parent/'20261011T232716Z-account05-A026-good-coordinate-erasure'/'code'
sys.path.insert(0,str(OLD))
import transitive as b
import transitive_v2 as v
b.logint=v.logint;b.LN2=v.LN2
def add(e,f,scale=F(1)):
 for p,c in f.items():
  e[p]=e.get(p,F(0))+scale*c
  if not e[p]:del e[p]
def const(x):return {2:F(x)} if x else {}
def phi(x,y):
 e={};b.phi(e,x,y);return e
@lru_cache(None)
def fast_iv(items):
 if not items:return F(0),F(0)
 D=max(c.denominator for _,c in items);assert not D&(D-1)
 lo=hi=0;Q=b.Q
 for p,c in items:
  l,h=b.logint(p);a=l.numerator*(Q//l.denominator);z=h.numerator*(Q//h.denominator)
  n=c.numerator*(D//c.denominator)
  lo+=n*(a if n>0 else z);hi+=n*(z if n>0 else a)
 return F(lo,D*Q),F(hi,D*Q)
def interval(e):return fast_iv(tuple(sorted(e.items())))
def positive(e):
 if e:assert interval(e)[0]>=0,('unproved sign',b.serial(e),str(interval(e)))
def canonical(raw,D):
 e={}
 for k,c in raw.items():
  if k>1 and c:b.addlog(e,k,F(c,D))
 return e
def rawadd(raw,k,c):
 if k>1 and c:raw[k]=raw.get(k,0)+c
def erasure(W,i):
 N=len(W);raw={}
 for t in range(N):
  if not t&(1<<i):
   a,z=W[t]**2,W[t|(1<<i)]**2
   if a and z:rawadd(raw,a+z,a+z);rawadd(raw,a,-a);rawadd(raw,z,-z)
 return canonical(raw,N*N)
def entropy(W):
 N=len(W);n=N.bit_length()-1;raw={2:2*n*N*N}
 for w in W:rawadd(raw,w*w,-w*w)
 return canonical(raw,N*N)
def tables(n):
 for mask in range(1<<(1<<n)):
  yield mask,tuple(1 if mask&(1<<x) else -1 for x in range(1<<n))
def split(f,i,bit):
 return tuple(f[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(len(f)//2))
def shadow_compute(f,check=True):
 gp,gm=f[1::2],f[0::2];N=len(gp);nr=N.bit_length()-1
 p=tuple(a*z for a,z in zip(gp,gm));delta=F(sum(a!=z for a,z in zip(gp,gm)),N)
 ap=[];am=[];ip=[];im=[];common=[]
 for j in range(nr):
  dp=[gp[x]!=gp[x^(1<<j)] for x in range(N)];dm=[gm[x]!=gm[x^(1<<j)] for x in range(N)]
  ap.append(F(sum(a and not z for a,z in zip(dp,dm)),N))
  am.append(F(sum(z and not a for a,z in zip(dp,dm)),N))
  ip.append(F(sum(dp),N));im.append(F(sum(dm),N));common.append(F(sum(a and z for a,z in zip(dp,dm)),N))
 B=erasure(b.walsh(f),0);hb=phi(delta,1-delta);Ip=sum(ap)+sum(am)
 assert Ip==sum(F(sum(p[x]!=p[x^(1<<j)] for x in range(N)),N) for j in range(nr))
 assert sum(ip)+sum(im)-Ip==2*sum(common)
 if check:
  margin=dict(hb);add(margin,B,-1);positive(margin)
  margin=const(Ip);add(margin,hb,-1);positive(margin)
 return {'delta':delta,'B':B,'h2':hb,'Ip':Ip,'ap':tuple(ap),'am':tuple(am),'ip':tuple(ip),'im':tuple(im),'gp':gp,'gm':gm}
shadow=lru_cache(None)(shadow_compute)
@lru_cache(None)
def physical(f):
 N=len(f);n=N.bit_length()-1;W=b.walsh(f)
 assert sum(w*w for w in W)==N*N
 ds=[];bs=[]
 for i in range(n):
  d=F(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N)
  assert d==F(sum(W[t]**2 for t in range(N) if t&(1<<i)),N*N)
  ds.append(d);bs.append(erasure(W,i))
 return {'mu':F(sum(f),N),'d':tuple(ds),'B':tuple(bs),'I':sum(ds),'H':entropy(W),'W':tuple(W)}
def compose(f,h):
 NH=len(h);nh=NH.bit_length()-1
 return tuple(f[2*(x>>nh)+(h[x&(NH-1)]==1)] for x in range(NH*(len(f)//2)))
def dump(name,x):(ROOT/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
