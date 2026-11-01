import math
import numpy as np

TOL=1e-11
K0=(4*math.sqrt(2/math.e))**0.25
H0=K0*2**(1/8)
Cmix=5*2**(9/5)*math.exp(-1/10)
alpha=1/8

print(f"K0={K0:.15f}")
print(f"H0={H0:.15f}")
print(f"Cmix={Cmix:.15f}")

# 1. Exact completion/cross-block algebra on deterministic pseudo-random data.
rng=np.random.default_rng(20260924)
maxerr=0.0
for _ in range(1000):
    H=rng.normal(size=2)
    Y=rng.normal(size=4)
    B=rng.normal(size=(2,4))
    a=rng.normal(size=2)
    b=rng.normal(size=2)
    ell=rng.normal(size=4)
    m=rng.normal(size=4)
    beta,gamma=rng.normal(size=2)
    c=float(rng.uniform(.2,2.0))*float(rng.choice([-1,1]))
    Au=2*a@H+ell@Y+beta
    Av=2*b@H+m@Y+gamma
    Bstar=B-(np.outer(a,m)+np.outer(b,ell))/(2*c)
    lhs=2*H@B@Y-Au*Av/(2*c)
    FH=-2*(a@H)*(b@H)/c-(gamma*(a@H)+beta*(b@H))/c
    GY=-((ell@Y)*(m@Y)+gamma*(ell@Y)+beta*(m@Y))/(2*c)
    const=-beta*gamma/(2*c)
    rhs=FH+2*H@Bstar@Y+GY+const
    maxerr=max(maxerr,abs(lhs-rhs))
print(f"completion_identity_max_abs_error={maxerr:.3e}")
assert maxerr<1e-11

# 2. Optimizer and closed constant.
def optimized(c,sigma):
    H=H0*sigma**(-1/8)
    A0=2*math.sqrt(2)
    B0=(H/alpha)*2**alpha*abs(c)**(-1-alpha)
    rstar=(A0/(2*alpha*B0))**(1/(2*alpha+1))
    direct=A0/rstar+B0*rstar**(2*alpha)
    closed=Cmix*abs(c)**(-9/10)*sigma**(-1/10)
    return rstar,direct,closed
rstar,direct,closed=optimized(.7,1.0134476961160863)
print(f"optimizer_r={rstar:.15f}")
print(f"optimizer_direct={direct:.15f}")
print(f"optimizer_closed={closed:.15f}")
print(f"optimizer_abs_error={abs(direct-closed):.3e}")
assert abs(direct-closed)<TOL

# 3. Homogeneity check.
lam=7.3
c=.7
sigma=1.0134476961160863
orig=Cmix*abs(c)**(-.9)*sigma**(-.1)
scaled=Cmix*abs(lam*c)**(-.9)*abs(lam*sigma)**(-.1)
print(f"scaling_ratio={scaled/(orig/lam):.15f}")
assert abs(scaled-orig/lam)<TOL

# 4. Target-valid six-coordinate stress matrix.
B=np.eye(2)
a=np.array([.4,.1])
b=np.array([.1,-.3])
ell=np.array([.3,-.2])
m=np.array([-.1,.4])
c=.7
A=np.zeros((6,6))
A[:2,2:4]=B; A[2:4,:2]=B.T
A[:2,4]=a; A[4,:2]=a
A[:2,5]=b; A[5,:2]=b
A[2:4,4]=ell/2; A[4,2:4]=ell/2
A[2:4,5]=m/2; A[5,2:4]=m/2
A[4,5]=c; A[5,4]=c
eigs=np.linalg.eigvalsh(A)
Bstar=B-(np.outer(a,m)+np.outer(b,ell))/(2*c)
sigma=np.linalg.norm(Bstar,2)
bound=Cmix*abs(c)**(-.9)*sigma**(-.1)
print("stress_eigenvalues="+",".join(f"{x:.12f}" for x in eigs))
print(f"stress_large_eigenvalue_count={int(np.sum(np.abs(eigs)>=1-1e-12))}")
print(f"stress_Bstar_sigma={sigma:.15f}")
print(f"stress_density_bound={bound:.15f}")
assert np.sum(np.abs(eigs)>=1-1e-12)>=3
assert sigma>0

# 5. Partner L2 / averaged-frequency constants.
phi_l2=2*math.sqrt(math.pi) # ||phi||_2 <= this * |c|^-1/2
fejer=math.sqrt(2/(3*math.pi)) # sup_y |D_T| <= this * sqrt(T/|c|)
print(f"partner_phi_L2_constant={phi_l2:.15f}")
print(f"partner_Fejer_L2_constant={fejer:.15f}")

print("STATUS=PASS")
