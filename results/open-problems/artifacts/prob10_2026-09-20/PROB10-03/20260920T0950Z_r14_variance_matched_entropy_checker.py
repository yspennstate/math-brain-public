import math
import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss
from scipy.special import log_ndtr, logsumexp

# Exact symbolic checks for the projective-cage obstruction.
w0,w1,w2,x,y,Z,k,h = sp.symbols('w0 w1 w2 x y Z k h', positive=True)
q3 = w2/Z
q2 = (y*w1+w2)/Z
Ac3 = w1*(w2+w1*k)/(2*Z)
a = x*y**2*w0/Z
Ac2 = w0*(1-a*h)/2
checks = {
    'AC3_MINUS_OLD_LOWER': sp.simplify(Ac3-w1*q3/2-w1**2*k/(2*Z)),
    'OLD_UPPER_MINUS_AC3': sp.simplify(w1*q2/2-Ac3-w1**2*(y-k)/(2*Z)),
    'AC2_MINUS_OLD_LOWER': sp.simplify(Ac2-w0*(1-a)/2-w0*a*(1-h)/2),
    'OLD_UPPER_MINUS_AC2': sp.simplify(w0/2-Ac2-w0*a*h/2),
}
assert all(v == 0 for v in checks.values())

# Exact bookkeeping for the matched-Gaussian Fisher decomposition.
mu,v,I = sp.symbols('mu v I', positive=True)
G = sp.Rational(1,2)*(mu**2+v-1-sp.log(v))
J = I-mu**2-(v-1)**2/v
assert sp.simplify((G+v*J/2-G)-v*J/2) == 0
Ig = mu**2+(v-1)**2/v
assert sp.simplify(J-(I-Ig)) == 0

# Numerical-only falsification scout at the NM13-03 supported GH240 point.
p3=0.59916661152315709
p2=0.96911590889423460
c3=2.8674016670255789
c2=13.103472674779855
gamma_sq=.076564610980229264
m0=c3/c2
B=c2/(4*gamma_sq)
s=math.sqrt(1-p2)
d=math.sqrt(p2-p3)
A=1+2*B*s*s
LOGSQ2PI=.5*math.log(2*math.pi)

def inner_closed(xv):
    z=xv/(s*math.sqrt(A))
    logneg=float(log_ndtr(-xv/s))
    logpos=-.5*math.log(A)-B*xv*xv/A+float(log_ndtr(z))
    logf=float(logsumexp([logneg,logpos]))
    P=math.exp(logpos-logf)
    if z > -35:
        lam=math.exp(-.5*z*z-LOGSQ2PI-float(log_ndtr(z)))
    else:
        # Used only in astronomically tiny Gaussian-Hermite tail nodes.
        zz=-z
        lam=zz+1/zz
    mu0=xv/A
    tau=s/math.sqrt(A)
    e1pos=mu0+tau*lam
    e2pos=mu0*mu0+tau*tau+mu0*tau*lam
    e1=P*e1pos
    e2=P*e2pos
    ux=-2*B*e1
    uxx=-2*B*P+4*B*B*(e2-e1*e1)
    return logf,ux,uxx,e2

def gh_nodes(n):
    z0,w=hermgauss(n)
    return math.sqrt(2)*z0, w/math.sqrt(math.pi)

def refined_cages(n):
    U,wu=gh_nodes(n)
    V,wv=gh_nodes(n)
    DU_lo=DU_hi=DH_lo=DH_hi=0.0
    old_M1=old_M2=old_MB=0.0
    min_vu=min_vh=1.0
    for vv,wvv in zip(V,wv):
        xs=d*U+math.sqrt(p3)*vv-1
        arr=np.array([inner_closed(float(xx)) for xx in xs])
        us,uxs,uxxs,mbs=arr.T
        lw=m0*us
        ww=wu*np.exp(lw-lw.max())
        ww/=ww.sum()
        meanux=float(np.sum(ww*uxs))
        meanux2=float(np.sum(ww*uxs**2))
        meanuxx=float(np.sum(ww*uxxs))
        varux=max(0.0,meanux2-meanux**2)

        muU=m0*d*meanux
        vU=1+m0*d*d*meanuxx+m0*m0*d*d*varux
        IU=m0*m0*d*d*meanux2
        GU=.5*(muU*muU+vU-1-math.log(vU))
        JU=IU-muU*muU-(vU-1)**2/vU
        DU_lo += wvv*GU
        DU_hi += wvv*(GU+.5*vU*JU)
        min_vu=min(min_vu,vU)

        vH=1+s*s*uxxs
        muH=s*uxs
        IH=4*B*B*s*s*mbs
        GH=.5*(muH*muH+vH-1-np.log(vH))
        JH=IH-muH*muH-(vH-1)**2/vH
        DH_lo += wvv*m0*float(np.sum(ww*GH))
        DH_hi += wvv*m0*float(np.sum(ww*(GH+.5*vH*JH)))
        min_vh=min(min_vh,float(vH.min()))

        old_M1 += wvv*meanux**2
        old_M2 += wvv*meanux2
        old_MB += wvv*float(np.sum(ww*mbs))

    old_DU_lo=.5*m0*m0*d*d*old_M1
    old_DU_hi=.5*m0*m0*d*d*old_M2
    old_DH_lo=.5*m0*s*s*old_M2
    old_DH_hi=2*m0*B*B*s*s*old_MB
    return old_DU_lo,old_DU_hi,DU_lo,DU_hi,old_DH_lo,old_DH_hi,DH_lo,DH_hi,min_vu,min_vh

print('EXACT_PROJECTIVE_CAGE_IDENTITIES_PASS')
for key,val in checks.items():
    print(key,val)
print('EXACT_MATCHED_GAUSSIAN_DECOMPOSITION_BOOKKEEPING_PASS')
print('NUMERICAL_ONLY_GH_SCOUT')
rows=[]
for n in [60,80,120]:
    r=refined_cages(n)
    rows.append((n,r))
    print('GH',n)
    print('OLD_DU',repr(r[0]),repr(r[1]))
    print('NEW_DU',repr(r[2]),repr(r[3]))
    print('OLD_DH',repr(r[4]),repr(r[5]))
    print('NEW_DH',repr(r[6]),repr(r[7]))
    print('MIN_VU',repr(r[8]),'MIN_VH',repr(r[9]))
r=rows[-1][1]
old_du_w=r[1]-r[0]
new_du_w=r[3]-r[2]
old_dh_w=r[5]-r[4]
new_dh_w=r[7]-r[6]
print('NUMERICAL_ONLY_DU_WIDTH_REDUCTION',repr(1-new_du_w/old_du_w))
print('NUMERICAL_ONLY_DH_WIDTH_REDUCTION',repr(1-new_dh_w/old_dh_w))
print('ALL_SELF_CHECKS_PASS')
