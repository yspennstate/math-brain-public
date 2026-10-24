#!/usr/bin/env python3
"""
PROB10-03 R14 dimensionless capacity-chart checker.

Exact sections are symbolic/algebraic.
Numerical sections are Gauss-Hermite / finite-difference scouts only and are
NOT directed interval certificates or source endpoints.
"""
import math
import sympy as sp
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp

# ---------- EXACT algebra ----------
w0,w1,w2,x,y,H1,S1,S2,DU,DH = sp.symbols(
    "w0 w1 w2 x y H1 S1 S2 DU DH", positive=True)
Z = x*y**2*w0 + y*w1 + w2
c2 = (x-1)*sp.sqrt(Z)/(x*y*w0)
c3 = (y-1)*sp.sqrt(Z)/(y*w1)
B = (x-1)/(2*w0)
m = sp.simplify(c3/c2)
assert sp.simplify(m - x*w0*(y-1)/((x-1)*w1)) == 0
print("EXACT_M_RATIO_PASS")

# Capacity thermal stiffness: 1+2 B w0 = x.
assert sp.simplify(1+2*B*w0-x) == 0
print("EXACT_THERMAL_STIFFNESS_PASS")

# Dimensionless score-energy conversion.
M1=S1/w0
M2=S2/w0
MB=w0*H1
alpha = sp.simplify(c2**2/(4*B**2*MB))
assert sp.simplify(alpha - Z/(x**2*y**2*w0*H1)) == 0
print("EXACT_ALPHA_DIMENSIONLESS_PASS")

q3=w2/Z
q2=(y*w1+w2)/Z
R3_old=sp.simplify(q3-M1/(4*B**2*MB))
R2_old=sp.simplify(q2-M2/(4*B**2*MB))
assert sp.simplify(R3_old - (q3-S1/((x-1)**2*H1))) == 0
assert sp.simplify(R2_old - (q2-S2/((x-1)**2*H1))) == 0
print("EXACT_SCORE_RESIDUAL_PASS")

k=y*(y*sp.log(y)-y+1)/(y-1)**2
h=x*(x-1-sp.log(x))/(x-1)**2
Ac3=w1*(w2+w1*k)/(2*Z)
Ac2=w0*sp.Rational(1,2)*(1-x*y**2*w0*h/Z)

RU_old=sp.simplify(Ac3-alpha*DU/c3**2)
RH_old=sp.simplify(Ac2-alpha*DH/(c2*c3))
RU_dim=sp.Rational(1,2)*w1*((w2+w1*k)/Z
        -2*w1*DU/(x**2*w0*(y-1)**2*H1))
RH_dim=sp.Rational(1,2)*(w0*(1-x*y**2*w0*h/Z)
        -2*w1*DH/(x*(x-1)*(y-1)*H1))
assert sp.simplify(RU_old-RU_dim)==0
assert sp.simplify(RH_old-RH_dim)==0
print("EXACT_KL_RESIDUAL_PASS")

# Division-light system follows when R3=0, i.e. Z S1=w2(x-1)^2 H1.
Rscale = Z*S1-w2*(x-1)**2*H1
Rratio = S2*w2-S1*(w2+y*w1)
RU_cross = x**2*w0*(y-1)**2*S1*(w2+w1*k)-2*w1*w2*(x-1)**2*DU
RH_cross = x*(y-1)*w0*S1*(Z-x*y**2*w0*h)-2*w1*w2*(x-1)*DH

# Algebraically check cross-multiplied consequences modulo Rscale.
# Substitute H1 = Z*S1/[w2(x-1)^2] directly.
Hsub=Z*S1/(w2*(x-1)**2)
RU_sub=sp.factor(RU_dim.subs(H1,Hsub))
RH_sub=sp.factor(RH_dim.subs(H1,Hsub))
assert sp.simplify(RU_sub - w1*RU_cross/(2*Z*x**2*w0*(y-1)**2*S1))==0
assert sp.simplify(RH_sub - RH_cross/(2*Z*x*(y-1)*S1))==0
print("EXACT_CROSS_MULTIPLIED_SYSTEM_PASS")

# ---------- NUMERICAL-ONLY scout ----------
def gh(n):
    z,w=hermgauss(n)
    return np.sqrt(2.0)*z, w/np.sqrt(np.pi)

def reconstruct_from_projective(v):
    w0,w1,x,y=map(float,v)
    w2=1-w0-w1
    Z=x*y*y*w0+y*w1+w2
    c2=(x-1)*math.sqrt(Z)/(x*y*w0)
    c3=(y-1)*math.sqrt(Z)/(y*w1)
    B=(x-1)/(2*w0)
    m=c3/c2
    return w2,Z,c2,c3,B,m

def moments(v,n):
    w0,w1,x,y=map(float,v)
    w2,Z,c2,c3,B,m=reconstruct_from_projective(v)
    U,wu=gh(n); V,wv=gh(n); logwu=np.log(wu)
    rtA=math.sqrt(x)
    s=math.sqrt(w0); sd=math.sqrt(w1); sp3=math.sqrt(w2)
    logphi0=-0.5*math.log(2*math.pi)
    Q=M1=M2=MB=QM=0.0
    for vv,ov in zip(V,wv):
        z=sd*U+sp3*vv-1.0
        a=z/s
        b=z/(s*rtA)
        logt1=log_ndtr(-a)
        logt2=-0.5*math.log(x)-B*z*z/x+log_ndtr(b)
        logf=np.logaddexp(logt1,logt2)
        frac1=np.exp(logt1-logf); frac2=np.exp(logt2-logf)
        mills_mina=np.exp(logphi0-0.5*a*a-log_ndtr(-a))
        ux1=-mills_mina/s
        mills_b=np.exp(logphi0-0.5*b*b-log_ndtr(b))
        ux2=-2*B*z/x+mills_b/(s*rtA)
        ux=frac1*ux1+frac2*ux2
        uB2=-w0/x-z*z/(x*x)-z*s*(x**-1.5)*mills_b
        uB=frac2*uB2
        lt=logwu+m*logf
        lz=logsumexp(lt)
        tw=np.exp(lt-lz)
        meanux=float(np.dot(tw,ux))
        Q += ov*lz
        M1 += ov*meanux*meanux
        M2 += ov*float(np.dot(tw,ux*ux))
        MB += ov*(-float(np.dot(tw,uB)))
        QM += ov*float(np.dot(tw,logf))
    QB=-m*MB
    DU=m*QM-Q
    DH=B*QB-m*QM
    return dict(Q=Q,M1=M1,M2=M2,MB=MB,QM=QM,DU=DU,DH=DH,m=m)

def kfun(y):
    return y*(y*math.log(y)-y+1)/(y-1)**2

def hfun(x):
    return x*(x-1-math.log(x))/(x-1)**2

def reduced_res(v,n=120,normalize=True):
    w0,w1,x,y=map(float,v); w2=1-w0-w1
    if not (w0>0 and w1>0 and w2>0 and x>1 and y>1):
        return np.ones(4)*1e3
    Z=x*y*y*w0+y*w1+w2
    d=moments(v,n)
    S1=w0*d["M1"]; S2=w0*d["M2"]; H1=d["MB"]/w0
    DU,DH=d["DU"],d["DH"]
    r=np.array([
       S2/S1-(1+y*w1/w2),
       Z*S1-w2*(x-1)**2*H1,
       x*x*w0*(y-1)**2*S1*(w2+w1*kfun(y))-2*w1*w2*(x-1)**2*DU,
       x*(y-1)*w0*S1*(Z-x*y*y*w0*hfun(x))-2*w1*w2*(x-1)*DH
    ],float)
    if not normalize:
        return r
    scales=np.array([
       S2/S1+(1+y*w1/w2),
       Z*S1+w2*(x-1)**2*H1,
       x*x*w0*(y-1)**2*S1*(w2+w1*kfun(y))+2*w1*w2*(x-1)**2*DU,
       x*(y-1)*w0*S1*(Z-x*y*y*w0*hfun(x))+2*w1*w2*(x-1)*DH
    ])
    return r/scales

def eta_to_v(e):
    a,b,c,d=map(float,e)
    ea,eb=math.exp(a),math.exp(b)
    den=1+ea+eb
    w0=ea/den; w1=eb/den
    return np.array([w0,w1,1+math.exp(c),1+math.exp(d)],float)

def v_to_eta(v):
    w0,w1,x,y=map(float,v); w2=1-w0-w1
    return np.array([math.log(w0/w2),math.log(w1/w2),
                     math.log(x-1),math.log(y-1)])

def jac(f,z,h=1e-6):
    z=np.array(z,float); J=np.zeros((len(z),len(z)))
    for j in range(len(z)):
        hh=h*max(1.0,abs(z[j]))
        zp=z.copy(); zm=z.copy(); zp[j]+=hh; zm[j]-=hh
        J[:,j]=(f(zp)-f(zm))/(2*hh)
    return J

# inherited numerical-only GH200 capacity point
p2=0.969115912465513
p3=0.599166615543999
q2=0.638436831267365
q3=0.228698051519619
w0v=1-p2; w1v=p2-p3; w2v=p3
r2=q3/p3; r1=(q2-q3)/(p2-p3); r0=(1-q2)/(1-p2)
xv=r0*r2/(r1*r1); yv=r1/r2
v=np.array([w0v,w1v,xv,yv])
e=v_to_eta(v)

for n in (80,120,160):
    rr=reduced_res(v,n,True)
    print("NUMERICAL_ONLY_NORMALIZED_RESID_INF",n,
          format(float(np.linalg.norm(rr,np.inf)),".12g"))

J=jac(lambda ee: reduced_res(eta_to_v(ee),120,True),e)
sv=np.linalg.svd(J,compute_uv=False)
print("NUMERICAL_ONLY_LOG_CHART_SINGULAR_VALUES",
      *(format(float(t),".12g") for t in sv))
print("NUMERICAL_ONLY_LOG_CHART_CONDITION",
      format(float(sv[0]/sv[-1]),".12g"))

# Compare inherited old overlap-coordinate condition as recorded by the old
# checker; do not recompute it as an exact statement.
print("INHERITED_NUMERICAL_ONLY_OLD_4D_CONDITION", "2840.90831657")
print("NUMERICAL_ONLY_CONDITION_IMPROVEMENT_FACTOR",
      format(2840.90831657/float(sv[0]/sv[-1]),".12g"))

# candidate hierarchy margin
mval=reconstruct_from_projective(v)[-1]
margin=(xv-1)*w1v-xv*(yv-1)*w0v
print("NUMERICAL_ONLY_PROJECTIVE_POINT",
      "w0",format(w0v,".15g"),"w1",format(w1v,".15g"),
      "w2",format(w2v,".15g"),"x",format(xv,".15g"),
      "y",format(yv,".15g"),"m",format(mval,".15g"),
      "hierarchy_margin",format(margin,".15g"))
print("ALL_EXACT_DIMENSIONLESS_CHECKS_PASS")
print("ALL_NUMERICAL_SCOUTS_COMPLETE")
