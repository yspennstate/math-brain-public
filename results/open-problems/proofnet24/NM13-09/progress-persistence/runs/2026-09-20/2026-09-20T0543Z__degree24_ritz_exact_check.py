from fractions import Fraction as F
from math import isqrt, comb, factorial
from functools import lru_cache
DEG=24; SCALE=10**46; DROOT=10**60
PC=[-414621789477675456,1000000000000000000,-273778362816309984,-565208570593089728,36663157927992624,295348556586466816,5756877035723137,-84327490026495296,-3565873229965740,13966990718191704,667718287196173,-1413141087386069,-67418858850133,90091922500818,4116450587658,-3660393427946,-157716525124,93840583382,3791803080,-1458683036,-55208244,12468759,442396,-44698,-1489]
r=F(7,8); s=F(24861,25000); c=s*F(1+r,2)
def fl(x):return x.numerator//x.denominator
def ce(x):return -((-x.numerator)//x.denominator)
def C(x): x=F(x); return fl(x*SCALE),ce(x*SCALE)
def I(lo,hi):return fl(lo*SCALE),ce(hi*SCALE)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 v=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]); lo,hi=min(v),max(v); return lo//SCALE,-((-hi)//SCALE)
def sc(a,q):
 q=F(q); lo,hi=(F(a[0])*q,F(a[1])*q) if q>=0 else (F(a[1])*q,F(a[0])*q); return fl(lo),ce(hi)
def inv(a): return fl(F(SCALE*SCALE,a[1])),ce(F(SCALE*SCALE,a[0]))
def div(a,b):return mul(a,inv(b))
def pw(a,n):
 out=C(1)
 for _ in range(n):out=mul(out,a)
 return out
def ats(x,m):
 x=F(x); z=F(0)
 for k in range(m+1): z+=F((-1)**k,2*k+1)*x**(2*k+1)
 nx=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1); return min(z,z+nx),max(z,z+nx)
a5=ats(F(1,5),70); a239=ats(F(1,239),20); PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
def sqb(x):
 x=F(x); m=isqrt((DROOT*DROOT*x.numerator)//x.denominator); lo,hi=F(m,DROOT),F(m+1,DROOT); assert lo*lo<=x<hi*hi; return lo,hi
def atp(t):
 t=F(t)
 if t<0: lo,hi=atp(-t);return -hi,-lo
 if t<=F(1,2):return ats(t,80)
 if t<=2:
  u=(t-1)/(t+1);lo,hi=ats(u,80);return PI[0]/4+lo,PI[1]/4+hi
 lo,hi=ats(1/t,80);return PI[0]/2-hi,PI[1]/2-lo
sq2pi=(sqb(2*PI[0])[0],sqb(2*PI[1])[1]); tI=I(1/sq2pi[1],1/sq2pi[0]); piI=I(*PI)
def sm(k):
 if k%2:return 0
 z=1
 for j in range(1,k,2):z*=j
 return z
def tnm(k):
 if k%2==0:return C(F(sm(k),2))
 m=(k-1)//2;return sc(tI,-(2**m)*factorial(m))
@lru_cache(None)
def bm0(i,j,vn,vd,hn,hd):
 v=F(vn,vd);h=F(hn,hd)
 if i<0 or j<0:return F(0)
 if i==0:return F(sm(j))*v**(j//2) if j%2==0 else F(0)
 return F(i-1)*v*bm0(i-2,j,vn,vd,hn,hd)+F(j)*h*bm0(i-1,j-1,vn,vd,hn,hd)
def bm(i,j,v,h):return bm0(i,j,v.numerator,v.denominator,h.numerator,h.denominator)
q=0
for i,ci in enumerate(PC):
 for j,cj in enumerate(PC):q+=ci*cj*sm(i+j)
qI=C(q)
sqrtcI=I(*sqb(c)); sqrtcP=[pw(sqrtcI,k) for k in range(2*DEG+1)];v1=1-c;h1=r-c;mI=(0,0)
for i,ci in enumerate(PC):
 for j,cj in enumerate(PC):
  pair=(0,0)
  for aa in range(i+1):
   for bb in range(j+1):
    res=bm(i-aa,j-bb,v1,h1)
    if res: pair=add(pair,sc(mul(sqrtcP[aa+bb],tnm(aa+bb)),F(comb(i,aa)*comb(j,bb))*res))
  mI=add(mI,sc(pair,F(ci*cj)))
muI=div(mI,qI)
MAX=2*DEG+2;EXT=3*DEG+12;s2=1-c*c;sqb2=sqb(s2);sI=I(*sqb2);ratioI=I(c/sqb2[1],c/sqb2[0]);ac=(atp(c/sqb2[1])[0],atp(c/sqb2[0])[1]);asinI=I(*ac)
BB=[None]*EXT;BB[0]=sc(mul(sI,tI),F(1,2));BB[1]=sc(mul(tI,tI),s2)
for k in range(2,EXT):BB[k]=sc(BB[k-2],F(k-1)*s2)
AA=[None]*EXT;AA[0]=add(C(F(1,4)),sc(div(asinI,piI),F(1,2)));AA[1]=add(sc(tI,F(1,2)),mul(ratioI,BB[0]))
for k in range(2,EXT):AA[k]=add(sc(AA[k-2],k-1),mul(ratioI,BB[k-1]))
Q=[[None]*EXT for _ in range(MAX+1)]
for n in range(EXT):Q[0][n]=AA[n]
for n in range(EXT-1):Q[1][n]=add(sc(AA[n+1],c),mul(sI,BB[n]))
for mm in range(2,MAX+1):
 for n in range(EXT-mm):Q[mm][n]=add(sc(Q[mm-1][n+1],c),sc(Q[mm-2][n],F(mm-1)*s2))
def qn(a,b):
 z=Q[a][b];return neg(z) if (a+b)%2 else z
den=1-c*c;al=(1-r*c)/den;be=(r-c)/den;alI=sc(sqrtcI,al);beI=sc(sqrtcI,be);alP=[pw(alI,k) for k in range(DEG+1)];beP=[pw(beI,k) for k in range(DEG+1)];v2=F(1)-c*(1+r*r-2*r*c)/den;h2=r*r-c*(2*r-c*(1+r*r))/den
MM=[[None]*(DEG+1) for _ in range(DEG+1)]
for p in range(DEG+1):
 for qq in range(DEG+1):
  tot=(0,0)
  for ia in range(p+1):
   ib=p-ia;cf1=mul(alP[ia],beP[ib])
   for ja in range(qq+1):
    jb=qq-ja;cf=mul(cf1,mul(beP[ja],alP[jb]));tot=add(tot,sc(mul(cf,qn(ia+ja,ib+jb)),F(comb(p,ia)*comb(qq,ja))))
  MM[p][qq]=tot
CM=[[None]*(DEG+1) for _ in range(DEG+1)]
for p in range(DEG+1):
 for qq in range(DEG+1):
  tot=(0,0)
  for e in range(p+1):
   for h in range(qq+1):
    rm=bm(e,h,v2,h2)
    if rm:tot=add(tot,sc(MM[p-e][qq-h],F(comb(p,e)*comb(qq,h))*rm))
  CM[p][qq]=tot
nI=(0,0)
for i,ci in enumerate(PC):
 for j,cj in enumerate(PC):nI=add(nI,sc(CM[i][j],F(ci*cj)))
norm=div(nI,qI);eps=sub(norm,mul(muI,muI))
print('mu',muI[0]/SCALE,muI[1]/SCALE)
print('eps2',eps[0]/SCALE,eps[1]/SCALE)
mu_lo=F(4559822947,5000000000);mu_hi=F(1139955737,1250000000);eps_hi=F(57783,250000000)
assert muI[0] > fl(mu_lo*SCALE);assert muI[1] < ce(mu_hi*SCALE);assert eps[1] < ce(eps_hi*SCALE)
trace_cap=F(54089303,50000000);theta_old=F(8399,50000);theta=F(2109,12500);x0=F(18276473,20000000);beta=F(78742027,100000000)
def nlb(a,N):
 z=(1-a)/(1+a);lo=sum(F(2)*z**(2*k+1)/F(2*k+1) for k in range(N+1));tail=F(2)*z**(2*N+3)/(F(2*N+3)*(1-z*z));return lo,lo+tail
Lx,Ux=nlb(x0,5);Lr,Ur=nlb(r,5);logm=Lx-4*theta*Ur
assert logm>0;assert x0>mu_hi>mu_lo>beta
tailm=beta**4-(trace_cap-x0**4);assert tailm>0
temple=(x0-mu_hi)*(mu_lo-beta)-eps_hi;assert temple>0
assert theta>theta_old
print('mu coarse',mu_lo,mu_hi,float(mu_lo),float(mu_hi))
print('eps2 coarse upper',eps_hi,float(eps_hi))
print('trace cap',trace_cap,float(trace_cap))
print('theta old/new',theta_old,float(theta_old),theta,float(theta))
print('width old/new',float(F(1,4)-theta_old),float(F(1,4)-theta))
print('x0 beta',float(x0),float(beta))
print('log margin',float(logm));print('tail margin',float(tailm));print('temple margin',float(temple))
print('ALL_EXACT_CHECKS_PASS = True')
