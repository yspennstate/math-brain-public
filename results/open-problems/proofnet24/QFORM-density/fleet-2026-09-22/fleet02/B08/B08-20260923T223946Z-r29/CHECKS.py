import math
import numpy as np

EPS=1/128
M_BIG=65536
LEAD=2**(13/6)*math.sqrt(3)

def hadamard(n):
    H=np.array([[1.0]])
    while H.shape[0] < n:
        H=np.block([[H,H],[H,-H]])
    return H/math.sqrt(n)

def build(m, eps, tau):
    H=hadamard(m)
    r1,r2,r3=H[0],H[1],H[2]
    q=math.sqrt(1-tau*tau)*r1+tau*r3
    M=np.vstack([r1,r2])
    B=np.diag([eps,-eps])
    K=M.T@np.linalg.inv(B)@M
    A=np.block([[B,M,M],[M.T,K+3*np.outer(q,q),K],[M.T,K,K]])
    return A

def roots(eps,tau):
    T=eps+2/eps+3
    P=3*(1+eps*eps+tau*tau)/eps
    d=T*T-4*P
    return (T-math.sqrt(d))/2,(T+math.sqrt(d))/2

def fixed_source_bound(eps,tau):
    prod=3*(1+eps*eps+tau*tau)*(eps*eps+2)/(eps*eps)
    return 12*prod**(-1/3)

for tau in [0,0.1,0.3,1]:
    A=build(16,EPS,tau)
    vals=np.linalg.eigvalsh(A)
    nz=vals[np.abs(vals)>1e-8]
    tm,tp=roots(EPS,tau)
    expected=np.array([-(EPS+2/EPS),tm,tp])
    err=np.max(np.abs(np.sort(nz)-np.sort(expected)))
    assert err < 1e-10
    assert tm>1
    print(f"spectral tau={tau:.1f}: maxerr={err:.3e}, theta-={tm:.12f}, theta+={tp:.12f}")

for tau in [0,0.3,1]:
    A=build(16,EPS,tau)
    vals,V=np.linalg.eigh(A)
    V=V[:,np.abs(vals)>1e-8]
    lev=np.diag(V@V.T)
    assert lev.max() < 0.5
    print(f"leverage tau={tau:.1f}: max={lev.max():.12f}")

pair_hub=EPS
pair_hl=math.sqrt(1/M_BIG+36/M_BIG**2)
pair_ll=2/(EPS*M_BIG)+12/M_BIG
assert max(pair_hub,pair_hl,pair_ll) < 1/64
print(f"pair gate: hub={pair_hub:.12f}, hub-light={pair_hl:.12f}, light-light={pair_ll:.12f}, gate={1/64:.12f}")

for tau in [0,0.01,0.1,0.3,1]:
    tm,tp=roots(EPS,tau)
    F=fixed_source_bound(EPS,tau)
    if tau==0:
        partner="undefined(tau=0)"
    else:
        partner=LEAD*(3*tau)**(-1/3)*(1-6/M_BIG)**(-1/6)
        partner=f"{partner:.12f}"
    print(f"tau={tau:.2f}: theta-={tm:.12f}, fixedF={F:.12f}, partner={partner}")

prev22=LEAD*(1-3/22)**(-1/6)
prev64=LEAD*(1-3/64)**(-1/6)
assert prev22 < 7.9691
print(f"previous perpendicular stress paid: m=22 {prev22:.12f}, m=64 {prev64:.12f}")
print("QFORM_B08_R29_CHECK_PASS")
