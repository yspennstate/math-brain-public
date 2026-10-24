from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,sys
R=Path(__file__).resolve().parents[1]; GRID=1<<110; checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
def rnd(a,b):return (F((a.numerator*GRID)//a.denominator,GRID),F(-((-b.numerator*GRID)//b.denominator),GRID))
def add(a,b):return rnd(a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 q=[x*y for x in a for y in b];return rnd(min(q),max(q))
def div(a,b):
 ck(b[0]>0);return mul(a,(1/b[1],1/b[0]))
def iv(x):return (F(x),F(x))
def scale(x,a):return mul(iv(x),a)
def total(vs):
 a=iv(0)
 for v in vs:a=add(a,v)
 return a
def ln_series(x):
 z=(x-1)/(x+1);s=F(0);power=z
 for j in range(24):s+=power/F(2*j+1);power*=z*z
 return (2*s,2*s+2*power/(49*(1-z*z)))
LN2=ln_series(F(2))
@lru_cache(None)
def logpoint(x):
 ck(x>0);k=x.numerator.bit_length()-x.denominator.bit_length();y=x/(F(2)**k)
 if y<1:y*=2;k-=1
 if y>=2:y/=2;k+=1
 ck(1<=y<2);return add(iv(k),div(ln_series(y),LN2))
def log(a):return (logpoint(a[0])[0],logpoint(a[1])[1])
def phi(a):
 if a[1]==0:return iv(0)
 ck(a[0]>0);return neg(mul(a,log(a)))
def h(a):
 if a==iv(0) or a==iv(1):return iv(0)
 return add(phi(a),phi(sub(iv(1),a)))
def entropy(p):return total(phi(iv(x)) for x in p if x)
def kl(p,q):return total(scale(x,log(div(iv(x),y))) for x,y in zip(p,q) if x)
def overlaps(a,b):return a[0]<=b[1] and b[0]<=a[1]
def fwht(t):
 a=t[:];s=1
 while s<len(a):
  for j in range(0,len(a),2*s):
   for k in range(j,j+s):a[k],a[k+s]=a[k]+a[k+s],a[k]-a[k+s]
  s*=2
 return a
def law(t):return [F(x*x,len(t)**2) for x in fwht(t)]
def marg(p):
 n=len(p).bit_length()-1;return [sum((x for k,x in enumerate(p) if k>>j&1),F(0)) for j in range(n)]
def restrict(t,i,y):return [t[k] for k in range(len(t)) if k>>i&1==y]
def facts(t):
 p=law(t);d=marg(p);H=entropy(p);M=total(h(iv(x)) for x in d)
 ck(sum(p)==1)
 for j,x in enumerate(d):ck(x==F(sum(t[k]!=t[k^(1<<j)] for k in range(len(t))),len(t)))
 return p,d,H,sub(M,H)
def rootref(p,d):
 z=1-p[0];r=[x/z for x in d]
 def g(c):
  w=F(1)
  for x in r:w*=1-c*x
  return 1-c-w
 lo,hi=F(0),F(1);ck(sum(r)>1 and g(hi)<0)
 for _ in range(60):
  m=(lo+hi)/2
  if g(m)>0:lo=m
  else:hi=m
 ck(lo>0 and g(lo)>0 and g(hi)<0)
 c=(lo,hi);theta=[scale(x,c) for x in r];q=[]
 for k in range(len(p)):
  if k==0:q.append(iv(p[0]));continue
  a=iv(z)
  for j,t in enumerate(theta):a=mul(a,t if k>>j&1 else sub(iv(1),t))
  q.append(div(a,c))
 ck(total(q)[0]<=1<=total(q)[1])
 for j,x in enumerate(d):
  s=total(q[k] for k in range(len(q)) if k>>j&1);ck(s[0]<=x<=s[1])
 HM=add(h(iv(z)),mul(div(iv(z),c),sub(total(h(t) for t in theta),h(c))))
 return q,c,HM
def step(tab,q,i):
 p=law(tab);ts=[restrict(tab,i,y) for y in [0,1]];ps=[law(t) for t in ts]
 fused=[p[k]+p[k|(1<<i)] for k in range(len(p)) if not k>>i&1]
 ck(fused==[(x+y)/2 for x,y in zip(*ps)])
 qr=[add(q[k],q[k|(1<<i)]) for k in range(len(q)) if not k>>i&1]
 kernels=[[ps[y][k]/(2*fused[k]) if fused[k] else F(1,2) for k in range(len(fused))] for y in [0,1]]
 outs=[total(scale(kernels[y][k],qr[k]) for k in range(len(qr))) for y in [0,1]]
 ck(total(outs)[0]<=1<=total(outs)[1])
 qc=[[div(scale(kernels[y][k],qr[k]),outs[y]) for k in range(len(qr))] for y in [0,1]]
 for v in qc:ck(total(v)[0]<=1<=total(v)[1])
 O=scale(F(-1,2),log(scale(4,mul(*outs))))
 E=sub(kl(p,q),kl(fused,qr))
 ck(overlaps(kl(p,q),add(E,add(O,scale(F(1,2),total(kl(pp,qq) for pp,qq in zip(ps,qc)))))))
 return ts,qc,O,outs,sum(x==0 for x in fused),E
def enc(a):return [str(x) for x in a]
def run(n):
 delta=F(1,2**n);v=[-1]+[1]*(2**n-1)
 tab=[-1 if not (k&1) and k&2 else (v[k>>3] if k&1 and k&4 else 1) for k in range(2**(n+3))]
 p,d,H,TC=facts(tab);q,c,HM=rootref(p,d);A=sub(HM,H)
 ck(overlaps(A,kl(p,q)));ck(overlaps(HM,total(phi(x) for x in q)))
 ck(d==[F(1,2),F(1,2)]+[delta/2]*(n+1))
 expected=[F(1,4)]*2+[((1-delta)/2)**2]*2+[delta**2/4]*(len(p)//2-2)
 ck(sorted(x for x in p if x)==sorted(expected))
 ts,qs,O0,out0,rows0,E0=step(tab,q,1);leaves=[];refs=[];O=O0;Etot=E0;normal=[list(map(enc,out0))];rows=[rows0]
 for t,qq in zip(ts,qs):
  ls,rs,o,out,rr,ee=step(t,qq,2);leaves+=ls;refs+=rs;O=add(O,scale(F(1,2),o));Etot=add(Etot,scale(F(1,2),ee));normal.append(list(map(enc,out)));rows.append(rr)
 ff=[facts(t) for t in leaves]
 Hend=scale(F(1,4),total(f[2] for f in ff));TCend=scale(F(1,4),total(f[3] for f in ff));Iend=sum((sum(f[1]) for f in ff),F(0))/4
 D=sub(add(O,TCend),A);S=sub(iv(4*Iend),Hend)
 Kend=scale(F(1,4),total(kl(f[0],qq) for f,qq in zip(ff,refs)));sigma=sub(TCend,Kend)
 ck(overlaps(A,add(Etot,add(O,Kend))));ck(overlaps(D,sub(sigma,Etot)))
 pt=[-1]+[1]*(2**(n+1)-1);ph=entropy(law(pt))
 ck(Hend[0]<=scale(F(1,2),ph)[1] and scale(F(1,2),ph)[0]<=Hend[1])
 ck(Iend==F(1,2)+n*delta/2)
 TCformula=scale(F(1,2),sub(scale(n+1,h(iv(delta))),ph))
 ck(TCend[0]<=TCformula[1] and TCformula[0]<=TCend[1])
 return {'n':n,'delta':str(delta),'c':enc(c),'root_A':enc(A),'erasure_KL_total':enc(Etot),'inherited_terminal_KL':enc(Kend),'conversion_sigma':enc(sigma),'outcome_KL_total':enc(O),'outcome_normalizers':normal,'source_zero_rows':rows,'terminal_H':enc(Hend),'terminal_I':str(Iend),'terminal_TC':enc(TCend),'terminal_S4':enc(S),'D_end':enc(D),'terminal_individual_S4':[enc(sub(iv(4*sum(f[1])),f[2])) for f in ff]}
def main():
 start=time.perf_counter();domain=[2] if '--pilot' in sys.argv else range(2,8);results=[]
 for n in domain:
  results.append(run(n));logpoint.cache_clear()
  (R/'out'/('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json')).write_text(json.dumps({'results':results,'checks':checks,'runtime_seconds':time.perf_counter()-start},indent=2),encoding='utf-8')
  print(json.dumps({'n':n,'D_end':results[-1]['D_end'],'checks':checks,'seconds':time.perf_counter()-start}),flush=True)
 ck(time.perf_counter()-start<(60 if '--pilot' in sys.argv else 600))
if __name__=='__main__':main()
