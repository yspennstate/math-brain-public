#!/usr/bin/env python3
"""
PROB10-03 / R14 self-check for the second-order tilted-moment compiler.
Exact algebraic checks are SymPy identities. The Gauss-Hermite finite-difference
comparison is NUMERICAL_ONLY and is used only as a falsification test.
"""
import math
import numpy as np
import sympy as sp
from scipy.special import ndtr
from numpy.polynomial.hermite import hermgauss

# ---------- exact algebraic checks ----------
p=sp.symbols('p', positive=True)
E_m2, E_mm2, E_m2mm = sp.symbols('E_m2 E_mm2 E_m2mm')
E_mmm2,E_mm3,E_mmmix,E_m2mm2,E_m3mmm = sp.symbols(
    'E_mmm2 E_mm3 E_mmmix E_m2mm2 E_m3mmm'
)
Kp = E_m2 + p*(E_mm2-2*E_m2mm)
Ktt = (4*p**3*E_mmm2 + 12*p**2*E_mm2 + 4*p*E_m2
       -16*p**3*E_mm3 -24*p**3*E_mmmix -24*p**2*E_m2mm
       +24*p**3*E_m2mm2 +8*p**3*E_m3mmm)
Kpp_from_t = sp.expand((Ktt-4*p*Kp)/(4*p**2))
Kpp_claim = (p*E_mmm2 + 2*E_mm2 - 4*p*E_mm3 - 6*p*E_mmmix
             -4*E_m2mm +6*p*E_m2mm2 +2*p*E_m3mmm)
assert sp.simplify(Kpp_from_t-Kpp_claim)==0

# Hermite factorization behind B=0 transversality, finite symbolic truncation.
s0,s1,s2,s3,s4=sp.symbols('s0 s1 s2 s3 s4')
F=s0+s1*p+s2*p**2+s3*p**3+s4*p**4-p*(s0+s1+s2+s3+s4)
G=s0-s2*p-s3*p*(1+p)-s4*p*(1+p+p**2)
assert sp.expand(F-(1-p)*G)==0

print('EXACT_KPP_TRANSFORM_IDENTITY=PASS')
print('EXACT_B0_FACTOR_IDENTITY=PASS')

# ---------- numerical-only falsification test ----------
def make_nodes(n):
    x,w=hermgauss(n)
    return np.sqrt(2)*x, w/np.sqrt(np.pi)

def moment_data(mu,s,B,maxr=6):
    A=1+2*B*s*s
    ph=np.exp(-0.5*(mu/s)**2)/np.sqrt(2*np.pi)
    J=np.zeros((maxr+1,mu.size))
    J[0]=A**-0.5*np.exp(-B*mu*mu/A)*ndtr(mu/(s*np.sqrt(A)))
    J[1]=(mu*J[0]+s*ph)/A
    for r in range(2,maxr+1):
        J[r]=(mu/A)*J[r-1]+((r-1)*s*s/A)*J[r-2]
    f=ndtr(-mu/s)+J[0]
    return f,J,ph/s

def u_derivs(pv,Bv,n=80):
    z,w=make_nodes(n)
    s=math.sqrt(1-pv)
    mu=math.sqrt(pv)*z-1
    f,J,rho0=moment_data(mu,s,Bv,6)
    fB=-J[2]; fBB=J[4]; fBBB=-J[6]
    fmu=-2*Bv*J[1]
    fmuB=-2*J[1]+2*Bv*J[3]
    fmuBB=4*J[3]-2*Bv*J[5]
    fmumu=-2*Bv*J[0]+4*Bv**2*J[2]
    fmumuB=-2*J[0]+10*Bv*J[2]-4*Bv**2*J[4]
    fmumumu=-2*Bv*rho0+12*Bv**2*J[1]-8*Bv**3*J[3]
    uB=fB/f
    uBB=fBB/f-uB*uB
    uBBB=fBBB/f-3*fBB*fB/f**2+2*(fB/f)**3
    umu=fmu/f
    umuB=fmuB/f-umu*uB
    umuBB=(fmuBB/f-fmu*fBB/f**2-2*fB*fmuB/f**2
           +2*fmu*fB**2/f**3)
    umumu=fmumu/f-umu*umu
    umumuB=(fmumuB/f-fmumu*fB/f**2-2*fmu*fmuB/f**2
            +2*fmu*fmu*fB/f**3)
    umumumu=fmumumu/f-3*fmumu*fmu/f**2+2*(fmu/f)**3
    return w,(uB,uBB,uBBB,umu,umuB,umuBB,umumu,umumuB,umumumu)

def K_derivs(pv,Bv,n=80):
    w,d=u_derivs(pv,Bv,n)
    uB,uBB,uBBB,um,umB,umBB,umm,ummB,ummm=d
    E=lambda a: float(np.sum(w*a))
    K=pv*E(um**2)
    KB=2*pv*E(um*umB)
    KBB=2*pv*E(umB**2+um*umBB)
    Kp=E(um**2)+pv*E(umm**2-2*um**2*umm)
    KpB=(2*E(um*umB)+pv*E(2*umm*ummB-4*um*umB*umm-2*um**2*ummB))
    Kpp=(pv*E(ummm**2)+2*E(umm**2)-4*pv*E(umm**3)
         -6*pv*E(um*umm*ummm)-4*E(um**2*umm)
         +6*pv*E(um**2*umm**2)+2*pv*E(um**3*ummm))
    IBBB=E(uBBB)
    return K,KB,KBB,Kp,KpB,Kpp,IBBB

pc=0.645767064689
Bc=4.9292292009
K,KB,KBB,Kp,KpB,Kpp,IBBB=K_derivs(pc,Bc,80)
print('NUMERICAL_ONLY_center_K',repr(K))
print('NUMERICAL_ONLY_center_KB',repr(KB))
print('NUMERICAL_ONLY_center_KBB',repr(KBB))
print('NUMERICAL_ONLY_center_Kp',repr(Kp))
print('NUMERICAL_ONLY_center_KpB',repr(KpB))
print('NUMERICAL_ONLY_center_Kpp',repr(Kpp))
print('NUMERICAL_ONLY_center_IBBB',repr(IBBB))

def K_only(pv,Bv):
    return K_derivs(pv,Bv,80)[0]

h=2e-4
K0=K_only(pc,Bc)
fd_p=(K_only(pc+h,Bc)-K_only(pc-h,Bc))/(2*h)
fd_pp=(K_only(pc+h,Bc)-2*K0+K_only(pc-h,Bc))/h**2
fd_B=(K_only(pc,Bc+h)-K_only(pc,Bc-h))/(2*h)
fd_BB=(K_only(pc,Bc+h)-2*K0+K_only(pc,Bc-h))/h**2
fd_pB=(K_only(pc+h,Bc+h)-K_only(pc+h,Bc-h)
       -K_only(pc-h,Bc+h)+K_only(pc-h,Bc-h))/(4*h*h)
errs=[abs(fd_p-Kp),abs(fd_pp-Kpp),abs(fd_B-KB),abs(fd_BB-KBB),abs(fd_pB-KpB)]
print('NUMERICAL_ONLY_fd_errors',*[f'{e:.6e}' for e in errs])
assert errs[0] < 1e-5
assert errs[1] < 1e-4
assert errs[2] < 1e-7
assert errs[3] < 1e-7
assert errs[4] < 1e-6
print('ALL_SELF_CHECKS_PASS')
