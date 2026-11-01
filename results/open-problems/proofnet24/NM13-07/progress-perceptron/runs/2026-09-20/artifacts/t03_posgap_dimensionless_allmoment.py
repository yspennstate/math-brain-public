#!/usr/bin/env python3
"""NM13-07/T03: exact positive-gap algebra + numerical dimensionless scouts.

EXACT sections use Fraction/SymPy only. NUMERICAL_ONLY sections are
Gauss-Hermite/scipy falsification checks and are not source endpoints.
"""
from fractions import Fraction as F
import math, numpy as np, sympy as sp
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp
from scipy.optimize import root

# ---------- exact source microstep inside inherited directed chart ----------
alphaL=F(315148718753,50_000_000_000)
alpha0=F(12319635,1_000_000)
alpha_before=F(61598172231,5_000_000_000)
alpha_after=F(2463926889239,200_000_000_000)
assert alpha_before-alpha_after==F(1,200_000_000_000)
dec_lo=F(1,2_000_000)-F(27,500_000_000)
dec_hi=F(1,2_000_000)+F(27,500_000_000)
delta_new=alpha0-alpha_after
assert dec_lo<=delta_new<=dec_hi
q=F(229179741,467259059)
eta=F(18671401519768819,40795417037192166)
assert eta<1-q
slope=F(4136629,105883920)
psi0=F(23584189005311,1090044380000000000000)
psi_new=psi0-slope*delta_new
assert psi_new>0
print('EXACT_SOURCE_MICROSTEP')
print('ALPHA_BEFORE',float(alpha_before))
print('ALPHA_AFTER',float(alpha_after))
print('SOURCE_GAIN',alpha_before-alpha_after,float(alpha_before-alpha_after))
print('DELTA_FROM_ANCHOR',delta_new,float(delta_new))
print('CHART_DECREMENT_RANGE',float(dec_lo),float(dec_hi))
print('PSI_NEW_LOWER',psi_new,float(psi_new))
print('WIDTH_BEFORE',float(alpha_before-alphaL))
print('WIDTH_AFTER',float(alpha_after-alphaL))
print('EXACT_SOURCE_MICROSTEP_PASS')

# ---------- exact positive-gap projective algebra ----------
w0,w1,w2,x,y,Z,lam,H1,S1,S2,DU,DH=sp.symbols(
    'w0 w1 w2 x y Z lam H1 S1 S2 DU DH',positive=True)
sqZ=sp.sqrt(Z)
c2=(x-1)*sqZ/(x*y*w0)
c3=(y-1)*sqZ/(y*w1)
B=lam*(x-1)/(2*w0)
MB=w0*H1
alpha_raw=sp.simplify(c2**2/(4*B**2*MB))
q3_raw=sp.simplify((S1/w0)/(4*B**2*MB))
q2_raw=sp.simplify((S2/w0)/(4*B**2*MB))
assert sp.simplify(alpha_raw-Z/(lam**2*x**2*y**2*w0*H1))==0
assert sp.simplify(q3_raw-S1/(lam**2*(x-1)**2*H1))==0
assert sp.simplify(q2_raw-S2/(lam**2*(x-1)**2*H1))==0
H1scale=Z*S1/(w2*lam**2*(x-1)**2)
alpha_red=sp.simplify(alpha_raw.subs(H1,H1scale))
assert sp.simplify(alpha_red-w2*(x-1)**2/(x**2*y**2*w0*S1))==0
ky=y*(y*sp.log(y)-y+1)/(y-1)**2
hx=x*(x-1-sp.log(x))/(x-1)**2
Ac3=w1*(w2+w1*ky)/(2*Z)
Ac2=w0*(1-x*y**2*w0*hx/Z)/2
RU=sp.factor((Ac3-alpha_red*DU/c3**2)*(2*Z*x**2*w0*S1*(y-1)**2)/w1)
RH=sp.factor((Ac2-alpha_red*DH/(c2*c3))*(2*Z*x*(y-1)*S1))
RUt=x**2*w0*(y-1)**2*S1*(w2+w1*ky)-2*w1*w2*(x-1)**2*DU
RHt=x*(y-1)*w0*S1*(Z-x*y**2*w0*hx)-2*w1*w2*(x-1)*DH
assert sp.simplify(RU-RUt)==0
assert sp.simplify(RH-RHt)==0
print('EXACT_POSGAP_DIMENSIONLESS_ALGEBRA_PASS')

# ---------- dimensionless numerical implementation ----------
def gh(n):
    z,w=hermgauss(n); return np.sqrt(2)*z,w/np.sqrt(np.pi)

def geom(v,delta):
    w0,w1,x,m=map(float,v); w2=1-w0-w1
    y=1+m*(x-1)*w1/(x*w0)
    Z=x*y*y*w0+y*w1+w2
    S=math.sqrt(Z)/(x*y); lam=S/(S+delta); r=1+lam*(x-1)
    return w2,y,Z,S,lam,r

def kernel(t,r):
    t=np.asarray(t,float)
    l1=log_ndtr(-t); z=t/math.sqrt(r)
    l2=-0.5*math.log(r)-(r-1)*t*t/(2*r)+log_ndtr(z)
    U=np.logaddexp(l1,l2); f2=np.exp(l2-U)
    phF=np.exp(-0.5*t*t-0.5*math.log(2*math.pi)-U)
    mu1=(t*f2+phF)/r; mu2=(t*mu1+f2)/r
    Ut=-(r-1)*mu1; K=-(r-1)*0.5*mu2-U
    return U,Ut,mu2,K

def conditional(vpar,vv,delta,n):
    w0,w1,x,m=map(float,vpar); w2,y,Z,S,lam,r=geom(vpar,delta)
    Uq,wu=gh(n); lwu=np.log(wu)
    T=math.sqrt(w1/w0)*Uq+math.sqrt(w2/w0)*vv-1/math.sqrt(w0)
    U,Ut,H,K=kernel(T,r)
    lt=lwu+m*U; lz=logsumexp(lt); tw=np.exp(lt-lz)
    g=float(np.dot(tw,Ut))
    return np.array([g*g,float(np.dot(tw,Ut*Ut)),float(np.dot(tw,H)),
                     m*float(np.dot(tw,U))-float(lz),m*float(np.dot(tw,K))])

def moments(vpar,delta,n):
    V,wv=gh(n); z=np.zeros(5)
    for vv,ov in zip(V,wv): z+=ov*conditional(vpar,float(vv),delta,n)
    return z

def kfun(y): return y*(y*math.log(y)-y+1)/(y-1)**2
def hfun(x): return x*(x-1-math.log(x))/(x-1)**2

def residual(vpar,delta,n):
    w0,w1,x,m=map(float,vpar); w2,y,Z,S,lam,r=geom(vpar,delta)
    if min(w0,w1,w2)<=0 or x<=1 or not (0<m<1): return np.ones(4)*1e3
    S1,S2,H1,DU,DH=moments(vpar,delta,n)
    return np.array([
      S2/S1-(1+y*w1/w2),
      Z*S1-w2*lam*lam*(x-1)**2*H1,
      x*x*w0*(y-1)**2*S1*(w2+w1*kfun(y))-2*w1*w2*(x-1)**2*DU,
      x*(y-1)*w0*S1*(Z-x*y*y*w0*hfun(x))-2*w1*w2*(x-1)*DH])

def alpha_of(vpar,delta,n):
    w0,w1,x,m=map(float,vpar); w2,y,Z,S,lam,r=geom(vpar,delta)
    S1=moments(vpar,delta,n)[0]
    return w2*(x-1)**2/(x*x*y*y*w0*S1)

# archived delta=1e-3 waypoint -> global strict chart (w0,w1,x,m)
p2=0.967828984055228; p3=0.597722018031788
q2=0.638663550092673; q3=0.229918637629570
ww0=1-p2; ww1=p2-p3
r2=q3/p3; r1=(q2-q3)/(p2-p3); r0=(1-q2)/(1-p2)
xx=r0*r2/r1**2; yy=r1/r2; ZZ=xx*yy*yy*ww0+yy*ww1+p3
cc2=(xx-1)*math.sqrt(ZZ)/(xx*yy*ww0)
cc3=(yy-1)*math.sqrt(ZZ)/(yy*ww1)
v0=np.array([ww0,ww1,xx,cc3/cc2]); DEL=1e-3
last=v0.copy()
for n in (40,60,80,100,120,160,200):
    sol=root(lambda z:residual(z,DEL,n),last,method='hybr',
             options={'xtol':1e-12,'maxfev':1000})
    assert np.linalg.norm(residual(sol.x,DEL,n),np.inf)<2e-11
    last=sol.x.copy(); *_,rv=geom(last,DEL)
    print('NUMERICAL_ONLY_DIMENSIONLESS',n,
          'w0',format(last[0],'.15g'),'w1',format(last[1],'.15g'),
          'x',format(last[2],'.15g'),'m',format(last[3],'.15g'),
          'xi',format(rv,'.15g'),'alpha',format(alpha_of(last,DEL,n),'.15g'),
          'maxres',format(float(np.linalg.norm(residual(last,DEL,n),np.inf)),'.3e'))

# ---------- analytic conditional-moment Jacobian ----------
def geom_der(v,delta):
    w0,w1,x,m=map(float,v); w2=1-w0-w1
    y=1+m*(x-1)*w1/(x*w0)
    yd=np.array([-(y-1)/w0,(y-1)/w1,m*w1/(w0*x*x),(y-1)/m])
    e0=np.array([1.,0,0,0]); e1=np.array([0.,1.,0,0.]); ex=np.array([0.,0.,1.,0.]); dw2=np.array([-1.,-1.,0,0.])
    Z=x*y*y*w0+y*w1+w2; Zd=np.zeros(4)
    for j in range(4): Zd[j]=ex[j]*y*y*w0+x*2*y*yd[j]*w0+x*y*y*e0[j]+yd[j]*w1+y*e1[j]+dw2[j]
    S=math.sqrt(Z)/(x*y); dlogS=.5*Zd/Z-ex/x-yd/y
    lam=S/(S+delta); ld=lam*(1-lam)*dlogS
    r=1+lam*(x-1); rd=(x-1)*ld+lam*ex
    return w2,y,Z,r,rd

def kernel_der(t,r):
    U,Ut,H,K=kernel(t,r); t=np.asarray(t,float)
    l1=log_ndtr(-t); l2=-.5*math.log(r)-(r-1)*t*t/(2*r)+log_ndtr(t/math.sqrt(r)); LF=np.logaddexp(l1,l2)
    f2=np.exp(l2-LF); phF=np.exp(-.5*t*t-.5*math.log(2*math.pi)-LF)
    m1=(t*f2+phF)/r; m2=H; m3=(t*m2+2*m1)/r; m4=(t*m3+3*m2)/r
    Ht=2*m1-(r-1)*(m3-m2*m1); Hr=-.5*(m4-m2*m2)
    Utt=-(r-1)*(f2-(r-1)*(m2-m1*m1)); Utr=-.5*Ht; Ur=-.5*H
    Kt=-(r-1)*.5*Ht-Ut; Kr=-(r-1)*.5*Hr
    return U,Ut,H,K,Ur,Utt,Utr,Ht,Hr,Kt,Kr

def moment_jac(v,delta,n):
    w0,w1,x,m=map(float,v); w2,y,Z,r,rd=geom_der(v,delta)
    Uq,wu=gh(n); Vq,wv=gh(n); lwu=np.log(wu)
    a=math.sqrt(w1/w0); b=math.sqrt(w2/w0); c=1/math.sqrt(w0)
    ad=np.array([-a/(2*w0),a/(2*w1),0,0.]); bd=np.array([-b*.5*(1/w2+1/w0),-b/(2*w2),0,0.]); cd=np.array([-c/(2*w0),0,0,0.]); md=np.array([0.,0.,0.,1.])
    val=np.zeros(5); J=np.zeros((5,4))
    for vv,ov in zip(Vq,wv):
        T=a*Uq+b*vv-c; Td=np.outer(Uq,ad)+np.outer(np.ones_like(Uq),bd*vv-cd)
        U,Ut,H,K,Ur,Utt,Utr,Ht,Hr,Kt,Kr=kernel_der(T,r)
        lt=lwu+m*U; lz=logsumexp(lt); tw=np.exp(lt-lz); mean=lambda A:float(np.dot(tw,A))
        g=mean(Ut); e2=mean(Ut*Ut); hh=mean(H); uu=mean(U); kk=mean(K)
        val+=ov*np.array([g*g,e2,hh,m*uu-lz,m*kk])
        for j in range(4):
            Uth=Ut*Td[:,j]+Ur*rd[j]; L=md[j]*U+m*Uth; ml=mean(L)
            A=Utt*Td[:,j]+Utr*rd[j]; dg=mean(A)+mean(Ut*L)-g*ml
            de2=mean(2*Ut*A)+mean(Ut*Ut*L)-e2*ml
            Hth=Ht*Td[:,j]+Hr*rd[j]; dhh=mean(Hth)+mean(H*L)-hh*ml
            ddu=m*(mean(U*L)-uu*ml)
            Kth=Kt*Td[:,j]+Kr*rd[j]; dkk=mean(Kth)+mean(K*L)-kk*ml
            J[:,j]+=ov*np.array([2*g*dg,de2,dhh,ddu,md[j]*kk+m*dkk])
    return val,J

def fj(fun,z,h=2e-6):
    y=np.asarray(fun(z)); J=np.zeros((len(y),len(z)))
    for j in range(len(z)):
        hh=h*max(1.,abs(z[j])); zp=z.copy(); zm=z.copy(); zp[j]+=hh; zm[j]-=hh
        J[:,j]=(np.asarray(fun(zp))-np.asarray(fun(zm)))/(2*hh)
    return J

val,Ja=moment_jac(last,DEL,100); Jf=fj(lambda z:moments(z,DEL,100),last)
err=float(np.max(np.abs(Ja-Jf))); rel=float(np.max(np.abs(Ja-Jf)/(1e-10+np.abs(Jf))))
print('NUMERICAL_ONLY_ANALYTIC_MOMENT_JAC_MAX_ABS_ERR',err)
print('NUMERICAL_ONLY_ANALYTIC_MOMENT_JAC_MAX_REL_ERR',rel)
assert err<1e-6 and rel<1e-5
C=np.array([conditional(last,float(v),DEL,120) for v in np.linspace(-6,6,601)])
mins=np.min(np.diff(C,axis=0),axis=0)
print('NUMERICAL_ONLY_ALL_MOMENT_MONOTONE_MIN_DIFF',*[format(float(t),'.17g') for t in mins])
print('NUMERICAL_ONLY_FINAL_ALPHA',format(alpha_of(last,DEL,200),'.17g'))
print('ALL_EXACT_AND_NUMERICAL_CHECKS_PASS')
