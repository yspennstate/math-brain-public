import json,time,hashlib
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
Q=1<<140; M=48

def walsh(a):
 a=list(a);h=1
 while h<len(a):
  for base in range(0,len(a),2*h):
   for j in range(base,base+h):
    u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
  h*=2
 return a

def ln_norm(v,d):
 # 1 <= v/d <=2, z=(v-d)/(v+d). Each summand is rounded DOWN.
 a=v-d;b=v+d; total=0
 for k in range(M):
  power=2*k+1
  total+=(2*Q*pow(a,power))//((2*k+1)*pow(b,power))
 z=F(a,b)
 tail=2*z**(2*M+1)/((2*M+1)*(1-z*z))
 return F(total,Q),F(total+M,Q)+tail
LN2=ln_norm(2,1)
@lru_cache(None)
def logint(v):
 assert v>0
 k=v.bit_length()-1;lo,hi=ln_norm(v,1<<k)
 return F(k)+lo/LN2[1],F(k)+hi/LN2[0]
@lru_cache(None)
def factors(v):
 r=[];d=2
 while d*d<=v:
  count=0
  while v%d==0:v//=d;count+=1
  if count:r.append((d,count))
  d=3 if d==2 else d+2
 if v>1:r.append((v,1))
 return tuple(r)
def addlog(e,v,c):
 if not c or v==1:return
 for p,k in factors(v):
  e[p]=e.get(p,F(0))+c*k
  if not e[p]:del e[p]
def lograt(e,v,c):
 v=F(v);addlog(e,v.numerator,c);addlog(e,v.denominator,-c)
def phi(e,a,b,scale=F(1)):
 a=F(a);b=F(b)
 if not a or not b:return
 lograt(e,a,-a*scale);lograt(e,b,-b*scale);lograt(e,a+b,(a+b)*scale)
def interval(e):
 lo=hi=F(0)
 for v,c in e.items():
  l,h=logint(v)
  lo+=c*(l if c>0 else h);hi+=c*(h if c>0 else l)
 return lo,hi
def mul(e,s):return {p:c*s for p,c in e.items() if c*s}
def serial(e):return {str(p):str(c) for p,c in sorted(e.items())}
def iv(i):return {'lower':str(i[0]),'upper':str(i[1]),'display_midpoint':float((i[0]+i[1])/2)}
def divide(a,b):
 assert b[0]>0
 corners=[a[i]/b[j] for i in [0,1] for j in [0,1]]
 return min(corners),max(corners)

def statistics(name,f,n,meta):
 N=1<<n;D=N*N;W=walsh(f);assert sum(v*v for v in W)==D
 H={}
 addlog(H,2,2*n)
 for v in W:
  if v: addlog(H,v*v,-F(v*v,D))
 bi=[]; influences=[]
 for i in range(n):
  bit=1<<i;e={};d=F(sum(W[s]**2 for s in range(N) if s&bit),D)
  physical=F(sum(f[x]!=f[x^bit] for x in range(N)),N);assert physical==d
  for t in range(N):
   if not t&bit:phi(e,F(W[t]**2,D),F(W[t|bit]**2,D))
  bi.append(e);influences.append(d)
 assert all(d==influences[0] for d in influences)
 assert all(e==bi[0] for e in bi)
 B=mul(bi[0],n);I=sum(influences);HH=interval(H);BB=interval(B)
 result={'name':name,'n':n,**meta,'I':str(I),'I_i':str(influences[0]),'H_prime_log':serial(H),'B_prime_log':serial(B),'H_interval':iv(HH),'B_interval':iv(BB),'H_over_I':iv((HH[0]/I,HH[1]/I)),'B_over_I':iv((BB[0]/I,BB[1]/I)),'B_over_H':iv(divide(BB,HH)) if HH[0]>0 else None,'support_count':sum(v!=0 for v in W),'Walsh':W}
 return result,H,B,influences[0],W

def tribes_expr(w,m):
 p=F(1,1<<w);b=1-p;t=b**(m-1)
 e={};addlog(e,2,4*p*(1-2*p)*t)
 phi(e,b*b,p*p,4*(t-t*t))
 phi(e,(1-2*b**m)**2,4*p*p*t*t)
 return e
def maj(bits):
 if len(bits)==1:return bits[0]
 m=len(bits)//3;v=[maj(bits[k*m:(k+1)*m]) for k in range(3)]
 return 1 if sum(v)>0 else -1
def main():
 start=time.perf_counter(); rows=[];assertions=0
 for w in range(1,5):
  for m in range(1,5):
   n=w*m
   if n>12:continue
   N=1<<n;mask=(1<<w)-1
   f=[1 if any(((x>>(j*w))&mask)==mask for j in range(m)) else -1 for x in range(N)]
   r,H,B,d,W=statistics(f'tribes-{w}-{m}',f,n,{'family':'tribes','w':w,'m':m})
   predicted=tribes_expr(w,m);assert B==mul(predicted,n)
   p=F(1,1<<w);b=1-p;assert d==2*p*b**(m-1)
   rows.append(r);assertions+=2+n*2
 for depth in [1,2]:
  n=3**depth;f=[maj([1 if (x>>i)&1 else -1 for i in range(n)]) for x in range(1<<n)]
  r,H,B,d,W=statistics(f'maj3-depth-{depth}',f,n,{'family':'recursive_majority','depth':depth})
  assert not B;assert H=={2:4*(F(3,2)**depth-1)}
  assert n*d==F(3,2)**depth
  assert all(not W[s] or s.bit_count()%2 for s in range(1<<n))
  rows.append(r);assertions+=3+n*2
 for n in [6,8,10]:
  for w in [2,3]:
   counts=[sum(all((x>>((j+k)%n))&1 for k in range(w)) for j in range(n)) for x in range(1<<n)]
   for t in range(1,n+1):
    f=[1 if count>=t else -1 for count in counts]
    r,H,B,d,W=statistics(f'cyclic-window-{n}-{w}-{t}',f,n,{'family':'cyclic_window_threshold','window':w,'threshold':t})
    rows.append(r);assertions+=n*2
    if time.perf_counter()-start>55:raise RuntimeError('frozen pilot limit')
 for n in [5,7,9,11]:
  f=[]
  for x in range(1<<n):
   signs=[1 if (x>>j)&1 else -1 for j in range(n)]
   f.append(1 if sum(signs[j]*signs[(j+1)%n]*signs[(j+2)%n] for j in range(n))>0 else -1)
  r,H,B,d,W=statistics(f'odd-cyclic-{n}',f,n,{'family':'odd_cyclic_threshold'})
  assert not B;rows.append(r);assertions+=1+n*2
 assert len(rows)==69
 result={'helper_version':'A026-transitive-true-erasure-v1','status':'PASS','elapsed_seconds':time.perf_counter()-start,'cases':len(rows),'assertions':assertions,'arithmetic':'integer Walsh; exact rational prime logs; outward atanh intervals','rounding_scale_bits':140,'series_terms':48,'records':rows}
 (ROOT/'out'/'transitive_certificates.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 summary={**result,'records':[{k:v for k,v in r.items() if k in ['name','n','I','support_count','H_over_I','B_over_I','B_over_H']} for r in rows]}
 (ROOT/'out'/'transitive_summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'status':'PASS','cases':len(rows),'assertions':assertions,'elapsed_seconds':result['elapsed_seconds'],'log_cache':logint.cache_info()._asdict(),'max_H_over_I':max((r['H_over_I']['display_midpoint'],r['name'],r['B_over_H']['display_midpoint'] if r['B_over_H'] else None) for r in rows)},indent=2))
if __name__=='__main__':main()
