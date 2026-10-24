from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(v):
 global checks
 checks+=1
 assert v, checks
def add(*terms):
 d={}
 for e in terms:
  for p,c in e:d[p]=d.get(p,Q(0))+c
 return tuple(sorted((p,c) for p,c in d.items() if c))
def scale(e,c):return tuple((p,x*c) for p,x in e if x*c)
@lru_cache(None)
def factor(n):
 d=[];p=2
 while p*p<=n:
  k=0
  while n%p==0:n//=p;k+=1
  if k:d.append((p,Q(k)))
  p+=1
 if n>1:d.append((n,Q(1)))
 return tuple(d)
@lru_cache(None)
def phi(p):
 if not p:return ()
 return scale(add(factor(p.numerator),scale(factor(p.denominator),-1)),-p)
def Phi(p,q):return add(phi(p),phi(q),scale(phi(p+q),-1))
@lru_cache(None)
def logbound(p):
 k=0;y=Q(p)
 while y>=2:y/=2;k+=1
 def ln(y):
  t=(y-1)/(y+1);n=24
  lo=2*sum((t**(2*j+1)/Q(2*j+1) for j in range(n)),Q(0))
  return lo,lo+2*t**(2*n+1)/(Q(2*n+1)*(1-t*t))
 a,b=ln(y);c,d=ln(Q(2))
 return k+a/d,k+b/c
@lru_cache(None)
def bounds(e):
 lo=hi=Q(0)
 for p,c in e:
  a,b=logbound(p);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 return lo,hi
def absle(e,c):
 if not e:return True
 lo,hi=bounds(e);return lo>=-c and hi<=c
@lru_cache(None)
def fft(v):
 a=list(v);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return tuple(Q(x,len(a)) for x in a)
@lru_cache(None)
def ent(v):return add(*(phi(a*a) for a in fft(v)))
def inf(v,i):return Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
def erase(v,i):
 a=fft(v);b=1<<i
 return add(*(Phi(a[j]**2,a[j|b]**2) for j in range(len(a)) if not j&b))
def shift(u,d,v):return add(scale(add(Phi((u+v)**2,d*d),Phi((u-v)**2,d*d)),Q(1,4)),scale(Phi(u*u,d*d),Q(-1,2)))
def restrict(v,i,b):
 mask=(1<<i)-1
 return tuple(v[(x&mask)|((x>>i)<<(i+1))|(b<<i)] for x in range(len(v)//2))
def wrapper(g,h):return tuple(g[x>>1] if not x&1 else h[x>>1] for x in range(2*len(g)))
def rows(kinds):return [c for c in range(1<<len(kinds)) if all(not c&(1<<i) or k=='S' for i,k in enumerate(kinds))]
def potential(g,h,kinds):
 a,b=fft(g),fft(h);cs=rows(kinds)
 return add(((2,2-sum((a[c]**2+b[c]**2 for c in cs),Q(0))),),*(add(phi((a[c]+b[c])**2/4),phi((a[c]-b[c])**2/4),scale(add(phi(a[c]**2),phi(b[c]**2)),Q(-1,2))) for c in cs))
@lru_cache(None)
def node(g,h,kinds):
 f=wrapper(g,h);a,b=fft(g),fft(h);cs=rows(kinds);r=potential(g,h,kinds)
 ck(sum((abs(a[c]) for c in cs),Q(0))<=1);ck(sum((abs(b[c]) for c in cs),Q(0))<=1)
 ck(ent(f)==add(scale(add(ent(g),ent(h)),Q(1,2)),r))
 data=Q(0)
 for i,k in enumerate(kinds):
  ig,ih=inf(g,i),inf(h,i);ii=inf(f,i+1);data+=ii
  ck(ii==(ig+ih)/2)
  direct=add(erase(f,i+1),scale(add(erase(g,i),erase(h,i)),Q(-1,2)))
  if k=='S':
   formula=add(*(add(scale(add(Phi((a[c]+b[c])**2,(a[c|1<<i]+b[c|1<<i])**2),Phi((a[c]-b[c])**2,(a[c|1<<i]-b[c|1<<i])**2)),Q(1,4)),scale(add(Phi(a[c]**2,a[c|1<<i]**2),Phi(b[c]**2,b[c|1<<i]**2)),Q(-1,2))) for c in cs if not c&(1<<i)))
  else:
   u,v=(a,b) if k=='X' else (b,a)
   formula=add(*(shift(u[c],u[c|1<<i],v[c]) for c in cs))
  ck(direct==formula);ck(absle(direct,(4 if k=='S' else 2)*ii))
  child=[]
  for ans in (0,1):
   gg,hh=restrict(g,i,ans),restrict(h,i,ans);kk=kinds[:i]+kinds[i+1:]
   child.append(potential(gg,hh,kk))
  dr=add(r,scale(add(*child),Q(-1,2)))
  ck(absle(dr,7*ii))
 ck(bounds(r)[0]>=0 if r else True);ck(absle(r,7*data))
 if not kinds:ck(not r)
def main():
 if sys.argv[1].startswith('indexed'):return indexed()
 start=time.perf_counter();limit=16 if sys.argv[1]=='pilot' else 256;roots=visits=0
 kinds=('S','S','X','Y')
 for A,B,gcode,hcode in product(range(4),range(4),range(4),range(4)):
  if roots>=limit:break
  g=tuple(((-1)**((t&A).bit_count()))*(1 if gcode&(1<<((t>>2)&1)) else -1) for t in range(16))
  h=tuple(((-1)**((t&B).bit_count()))*(1 if hcode&(1<<((t>>3)&1)) else -1) for t in range(16))
  for assignment in product((-1,0,1),repeat=4):
   gg,hh,kk=g,h,kinds
   for i in range(3,-1,-1):
    if assignment[i]>=0:
     gg,hh=restrict(gg,i,assignment[i]),restrict(hh,i,assignment[i]);kk=kk[:i]+kk[i+1:]
   node(gg,hh,kk);visits+=1
  roots+=1
 # Actual nonadmitted bent mean: (-1)^(s0*s1 in 0/1 convention).
 bent=(1,1,1,-1);ck(sum(map(abs,fft(bent)))==2)
 out={'mode':sys.argv[1],'roots':roots,'restriction_visits':visits,'distinct_nodes':node.cache_info().currsize,'exact_checks':checks,'seconds':time.perf_counter()-start,'failures':0,'arithmetic':'Fraction and prime logarithms, 24-term rational atanh enclosures with geometric tail','nonadmitted_bent_mean_l1':'2'}
 (ROOT/'out'/('check_'+sys.argv[1]+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
def indexed():
 start=time.perf_counter();limit=64 if sys.argv[1]=='indexed_pilot' else 4096;roots=visits=0;kinds=('S','S','X','Y')
 for ga,gb,ha,hb in product(range(8),repeat=4):
  if roots>=limit:break
  def signed_char(c,t):return (-1 if c&4 else 1)*((-1)**((c&t&3).bit_count()))
  g=tuple(signed_char(gb if t&4 else ga,t) for t in range(16))
  h=tuple(signed_char(hb if t&8 else ha,t) for t in range(16))
  node(g,h,kinds);visits+=1
  for i in range(4):
   for b in (0,1):
    node(restrict(g,i,b),restrict(h,i,b),kinds[:i]+kinds[i+1:]);visits+=1
  roots+=1
 out={'mode':sys.argv[1],'roots':roots,'node_visits':visits,'distinct_nodes':node.cache_info().currsize,'exact_checks':checks,'seconds':time.perf_counter()-start,'failures':0,'arithmetic':'Fraction and prime logarithms; rational log enclosures'}
 (ROOT/'out'/('check_'+sys.argv[1]+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
