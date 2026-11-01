import itertools, math
import numpy as np

rng=np.random.default_rng(20260923)

def det_minor(M,R,T):
    return float(np.linalg.det(M[np.ix_(R,T)]))

def Ek(M,k):
    if k==0: return 1.0
    if M.shape[0]<k or M.shape[1]<k: return 0.0
    return sum(det_minor(M,R,T)**2
               for R in itertools.combinations(range(M.shape[0]),k)
               for T in itertools.combinations(range(M.shape[1]),k))

max_v_ratio=0.0
max_tri_ratio=0.0
nchecks=0
for trial in range(250):
    m=4+(trial%3)
    n=4+((trial//3)%3)
    b=float(rng.normal())
    r=rng.normal(size=n)
    c=rng.normal(size=m)
    D=rng.normal(size=(m,n))
    M=np.block([[np.array([[b]]),r[None,:]],[c[:,None],D]])
    G=V=0.0
    for R0 in itertools.combinations(range(m),3):
        for T0 in itertools.combinations(range(n),3):
            full=det_minor(M,(0,)+tuple(i+1 for i in R0),(0,)+tuple(j+1 for j in T0))
            d3=det_minor(D,R0,T0)
            psi=b*d3-full
            G += full*full
            V += psi*psi
    bound=np.linalg.norm(c)**2*np.linalg.norm(r)**2*Ek(D,2)
    tri=abs(b)*math.sqrt(Ek(D,3))+math.sqrt(bound)
    if bound>1e-15: max_v_ratio=max(max_v_ratio,V/bound)
    if tri>1e-15: max_tri_ratio=max(max_tri_ratio,math.sqrt(G)/tri)
    assert V <= bound*(1+2e-9)+2e-8
    assert math.sqrt(G) <= tri*(1+2e-9)+2e-8
    nchecks += 1

h=(2*math.sqrt(2)-1)/1572864
beta=math.sqrt(63)/16
Pmin=beta*h*h
amin=16*math.sqrt(Pmin/4617)
gmin=math.sqrt(3)*amin/64
tmin=gmin/(4*math.sqrt(5))
tau0=h*h/128
C0=3*400**(1/3)*(32/9)**(1/6)
pair_bound=C0*tmin**(-5/6)
print(f"bordered_random_checks={nchecks}")
print(f"max_V_over_bound={max_v_ratio:.12f}")
print(f"max_triangle_ratio={max_tri_ratio:.12f}")
print(f"h={h:.16e}")
print(f"beta={beta:.16e}")
print(f"Pmin={Pmin:.16e}")
print(f"amin={amin:.16e}")
print(f"gmin={gmin:.16e}")
print(f"tmin={tmin:.16e}")
print(f"2tau0={2*tau0:.16e}")
print(f"tmin_over_2tau0={tmin/(2*tau0):.9f}")
print(f"pair_bound_at_partner_floor={pair_bound:.9f}")
print(f"sixbank_constant=1/(864sqrt6)={1/(864*math.sqrt(6)):.16e}")
print("STATUS=PASS")
