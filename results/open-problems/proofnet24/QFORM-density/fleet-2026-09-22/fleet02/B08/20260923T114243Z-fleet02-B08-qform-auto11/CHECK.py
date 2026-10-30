import math
import numpy as np

def hadamard(n):
    H=np.array([[1.0]])
    while H.shape[0] < n:
        H=np.block([[H,H],[H,-H]])
    return H

beta=(3/16)*math.sqrt(3/5)
c1=0.5*math.sqrt(3/5)
macro=math.sqrt(15)/17
d5=5*math.sqrt(2*math.e)*beta**(-2/5)*(1/64)**(-3/5)
pair_router=17.281*64
fresnel=6*(125/36)**(1/6)

assert abs(beta-0.14523687548277814)<1e-14
assert abs(c1-0.3872983346207417)<1e-14
assert abs(macro-0.22782254977690689)<1e-14
assert d5 < 306
assert pair_router < 1106
assert fresnel < 7.384

def gamma(d): return 1/5+2*d
def Gamma(d): return 64*(7*d-2)**2/(25*(10*d+1)**2)
def pair_const(d):
    return 16.511 * 3**(-9/38) * gamma(d)**(-0.5) * Gamma(d)**(-5/76)

assert Gamma(0.1) > 1.0815 and Gamma(0.1) < 1.0817
assert Gamma(1e-12) > 10.239999
assert pair_const(1e-12) < 24.423
assert pair_const(0.1) < pair_const(1e-12)

for m in (8,16,32):
    H=hadamard(m)/math.sqrt(m)
    U=H[:,:3]
    d=0.07
    P=np.diag([1-d,1/5,1/5])
    Q=np.eye(3)-P
    D=U@P@U.T
    C=U@Q@U.T
    A=np.block([[D,C],[C,D]])
    piv=[0,m]
    pair=A[np.ix_(piv,piv)]
    pe=np.linalg.eigvalsh(pair)
    g=gamma(d)
    assert np.max(np.abs(pe-np.array([-g/m,3/m])))<1e-12
    rest=[i for i in range(2*m) if i not in piv]
    S=A[np.ix_(rest,rest)]-A[np.ix_(rest,piv)]@np.linalg.inv(pair)@A[np.ix_(piv,rest)]
    M=S[:m-1,m-1:]
    sv=np.linalg.svd(M,compute_uv=False)
    expected=sorted([4/5,abs((14*d-4)/(10*d+1))], reverse=True)
    assert max(abs(sv[j]-expected[j]) for j in range(2))<1e-12
    assert sv[2] < 1e-12
    E2=sum((sv[i]*sv[j])**2 for i in range(len(sv)) for j in range(i+1,len(sv)))
    assert abs(E2-Gamma(d))<1e-10

print(f"beta={beta:.15f}")
print(f"c1={c1:.15f}")
print(f"macro_fraction={macro:.15f}")
print(f"D5_k1_eta_1_64={d5:.12f}")
print(f"pair_tail_tau_rho_1_64={pair_router:.12f}")
print(f"pair_hadamard_constant_sup_lt={pair_const(1e-12):.12f}")
print(f"fresnel_uniform_bound={fresnel:.12f}")
print("QFORM_B08_AUTO11_CHECK_PASS")
