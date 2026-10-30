from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,sys,time,itertools
ROOT=Path(__file__).resolve().parents[1]
N=0
def ck(x):
 global N
 N+=1
 assert x,N
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def sub(x,y):return add(x,neg(y))
def scale(x,t):return (x[0]*t,x[1]*t) if t>=0 else (x[1]*t,x[0]*t)
def ln_unit(x):
 z=(x-1)/(x+1); total=F(0)
 for k in range(30): total+=2*z**(2*k+1)/(2*k+1)
 return total,total+2*z**61/(61*(1-z*z))
LN2=ln_unit(F(2))
@lru_cache(None)
def lg(x):
 ck(x>0); k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 lo,hi=ln_unit(x)
 return F(k)+lo/LN2[1],F(k)+hi/LN2[0]
def ce(p,q):
 out=(F(0),F(0))
 for x,y in zip(p,q):
  if x: ck(y>0);out=add(out,scale(lg(y),-x))
 return out
def ent(p):return ce(p,p)
def ins(x,j):return (x&((1<<j)-1))|((x>>j)<<(j+1))
def marginal(q,j):return [q[ins(x,j)]+q[ins(x,j)|(1<<j)] for x in range(len(q)//2)]
def child(f,j,v):return [f[ins(x,j)|(v<<j)] for x in range(len(f)//2)]
def spectrum(f):
 m=len(f)
 w=[sum(v*(-1 if (x&t).bit_count()%2 else 1) for x,v in enumerate(f)) for t in range(m)]
 p=[F(z*z,m*m) for z in w];ck(sum(p)==1)
 return p
def influence(f):
 n=(len(f)-1).bit_length()
 return sum(F(sum(v!=f[x^(1<<j)] for x,v in enumerate(f)),len(f)) for j in range(n))
def truth(a,b,r):
 n=a+b+r
 return [1-2*int((x&((1<<a)-1))==0)+2*int(x==0) for x in range(1<<n)]
def source(a,b):return [1-2*int((x&((1<<a)-1))==0) for x in range(1<<(a+b))]
def calibrate(q,m):
 if m==1:return [F(1)]+[F(0)]*(len(q)-1)
 ck(q[0]<1)
 return [m]+[v*(1-m)/(1-q[0]) for v in q[1:]]
def floor(a,b,r,R):
 n=a+b;s=F(1,1<<a);t=F(1,1<<n);e=2*t*F(1,1<<r);mu=1-2*s
 P=spectrum(truth(a,b,r));q=[sum(P[T+(U<<n)] for U in range(1<<r)) for T in range(1<<n)]
 rp=[(1-e/s)*R[T]+(e/s)*mu*int(T==0)+2*e*t for T in range(1<<n)]
 ck(sum(rp)==sum(q)==1);ck(rp[0]==q[0])
 Q=[rp[T]*P[T+(U<<n)]/q[T] for U in range(1<<r) for T in range(1<<n)]
 ck(sum(Q)==1)
 return P,Q
def phi(x,y):
 out=scale(lg(x+y),x+y)
 if x:out=sub(out,scale(lg(x),x))
 if y:out=sub(out,scale(lg(y),y))
 return out
HIST=0;POSDEBT=0;RESET=0
def node(a,b,r,R):
 global HIST,POSDEBT,RESET
 HIST+=1
 f=truth(a,b,r);P,Q=floor(a,b,r,R)
 s=F(1,1<<a);t=F(1,1<<(a+b));e=2*t*F(1,1<<r);mu=1-2*s
 c=ce(spectrum(source(a,b)),R);W=add(c,(10*e*(a+b+r),)*2)
 ck(ce(P,Q)[1]<=W[0])
 for j in range(a):
  M=marginal(Q,j);on=child(f,j,0);off=child(f,j,1)
  ck(all(z==1 for z in off));ck(on==truth(a-1,b,r) if a>1 else on==[-1+2*int(x==0) for x in range(len(on))])
  B=sub(ent(P),ent(marginal(P,j)))
  if a==1:
   # Reset to the explicit point spectrum: CE=H, so no hidden oracle.
   Pon=spectrum(on);u=F(1,len(on));ck(Pon==[(1-2*u)**2]+[4*u*u]*(len(on)-1))
   k=ce(spectrum(off),M)
   lhs=add(B,scale(add(ent(Pon),k),F(1,2)))
   ck(lhs[1]<=W[0]);RESET+=1
   continue
  Pg=spectrum(source(a,b));Bg=sub(ent(Pg),ent(marginal(Pg,j)))
  ck(B[1]<=Bg[0])
  # Exact multiplicities certify the erasure formula independently of logs.
  pairs=sorted(tuple(sorted((P[ins(x,j)],P[ins(x,j)|(1<<j)]))) for x in range(len(P)//2))
  expected=[tuple(sorted(((mu+e)**2,(2*s-e)**2)))]+[((2*s-e)**2,)*2]*((1<<(a-1))-1)+[(e*e,)*2]*((1<<(a+b+r-1))-(1<<(a-1)))
  ck(pairs==sorted(expected))
  V=marginal(R,j);Rnext=calibrate(V,(1-4*s)**2)
  Pc,Qc=floor(a-1,b,r,Rnext);ck(Pc==spectrum(on))
  k=ce(spectrum(off),M);cconst=scale(lg(V[0]),-1)
  qj=4*s*s-4*s*e+2*e*t;kap=(2*s-e)**2/qj
  qs=(mu+e)**2+kap*((1-e/s)*R[1<<j]+2*e*t)
  ck(M[0]==qs)
  excess=sub(k,cconst);ck(excess[1]<18*e)
  if excess[0]>0:POSDEBT+=1
  cnext=ce(spectrum(source(a-1,b)),Rnext)
  Wnext=add(cnext,(20*e*(a-1+b+r),)*2)
  lhs=add(B,scale(add(Wnext,k),F(1,2)))
  ck(lhs[1]<=W[0]-e)
  # The actual prescribed reset can have either sign; do not assume a refund.
  Z=sub(ce(Pc,Qc),ce(Pc,M));RESET+=1
  ck(add(B,scale(add(ce(Pc,Qc),k),F(1,2)))[1]<=W[0])
  node(a-1,b,r,Rnext)
def algebra():
 count=0
 for a in range(2,15):
  s=F(1,1<<a);mu=1-2*s
  for ih in range(13):
   h=F(ih,12);e=s*h
   for z in (F(0),F(1,2),F(1)):
    t=e+(s-e)*z;qj=4*s*s-4*s*e+2*e*t;kap=(2*s-e)**2/qj
    vmax=1-mu*mu;qmax=(mu+e)**2+kap*((1-h)*vmax+2*e*t)
    lower=(mu+e)**2+(1-h)**2*vmax
    polynomial=1-F(5,4)*h+F(13,16)*h*h
    ck(qmax>=lower>=polynomial>=F(27,52));ck(qmax<=1);ck(1-qmax<=6*e)
    ck(polynomial-F(27,52)==F(13,16)*(h-F(10,13))**2)
    ck(lower-polynomial==(F(1,4)-s)*h*((6-4*h)-(s+F(1,4))*(4-3*h)))
    old=F(-1)
    for iv in range(5):
     v=vmax*F(iv,4);qstar=(mu+e)**2+kap*((1-h)*v+2*e*t)
     ratio=(mu*mu+v)/qstar;ck(ratio>=old);ck(ratio<=1/qmax);old=ratio
    count+=1
 return count
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv
 cases=list(itertools.product((2,3),(0,1),(1,2),range(3)))
 if pilot:cases=cases[:2]
 for a,b,r,kind in cases:
  Pg=spectrum(source(a,b));m=Pg[0]
  if kind==0:R=Pg
  elif kind==1:R=[m]+[(1-m)/((1<<(a+b))-1)]*((1<<(a+b))-1)
  else:
   R=[x/64 for x in Pg];R[0]=m
   R[1]+=(1-m)*F(63,64)
  ck(sum(R)==1);node(a,b,r,R)
  # Root physical influence independently checks erased-edge and control accounts.
  s=F(1,1<<a);e=F(2,1<<(a+b+r));ck(influence(truth(a,b,r))==2*a*s+e*(b-a+r))
 count=algebra()
 result=dict(status='PASS',roots=len(cases),active_prefix_nodes=HIST,reset_calls=RESET,strict_positive_complementary_debts=POSDEBT,algebraic_boxes=count,assertions=N,elapsed_seconds=time.perf_counter()-start,arithmetic='Fraction/direct characters/30-term rational atanh intervals; finite checks do not replace analytic induction')
 (ROOT/('out/PILOT.json' if pilot else 'out/CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
