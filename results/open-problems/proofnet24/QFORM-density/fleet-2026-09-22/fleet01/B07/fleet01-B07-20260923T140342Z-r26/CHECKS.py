import itertools, math
import numpy as np

rng=np.random.default_rng(260923)

# Check g_i <= ||row_s||^2 ||row_i||^2 for the anchored E2 bank.
mx=0.0
for _ in range(300):
    C=rng.normal(size=(6,7)); s=j=0
    Rs2=float(C[s]@C[s])
    for i in range(1,6):
        gi=sum((C[s,j]*C[i,k]-C[s,k]*C[i,j])**2 for k in range(1,7))
        Wi=float(C[i]@C[i])
        ratio=gi/(Rs2*Wi)
        mx=max(mx,ratio)
        assert ratio <= 1+1e-10

# Brute-force the four-bank selector on small matrices.
def selector_ok(c,r,E):
    C=np.linalg.norm(c); R=np.linalg.norm(r); F=np.linalg.norm(E)
    p=c*c/C**2; q=r*r/R**2
    u=(E*E).sum(1)/F**2; v=(E*E).sum(0)/F**2
    Ac=float(p@u); Ar=float(q@v)
    if Ac>=.25:
        return np.max(np.abs(c)) >= C/2-1e-10
    if Ar>=.25:
        return np.max(np.abs(r)) >= R/2-1e-10
    best=0.0; m,n=E.shape
    for mr in range(1<<m):
        L0=np.array([(mr>>i)&1 for i in range(m)],dtype=bool); L1=~L0
        for mc in range(1<<n):
            R0=np.array([(mc>>j)&1 for j in range(n)],dtype=bool); R1=~R0
            best=max(best,np.linalg.norm(c[L0])*np.linalg.norm(r[R0])*np.linalg.norm(E[np.ix_(L1,R1)]))
    return best >= C*R*F/(4*math.sqrt(2))-1e-10

for _ in range(80):
    assert selector_ok(rng.normal(size=4),rng.normal(size=4),rng.normal(size=(4,4)))

h=.75; r=1+h; q=2*h
kap=h**(-h)*(1-h)**(-(1-h))
C21=4*r*math.sqrt(math.e/2)/(r-q)*q**(-.25)*kap**(-1/(4*r))
assert abs(C21-27.219429843778478)<1e-12
Capp=math.sqrt(2)*C21*(4/3)**(1/7)
assert abs(Capp-40.10905342317083)<1e-12
print(f"max_shadow_ratio={mx:.12f}")
print(f"C21={C21:.12f}")
print(f"scalar_application_constant={Capp:.12f}")
print("QFORM_R26_CHECKS_PASS")
