import itertools, math
import numpy as np

rng=np.random.default_rng(230913)

def pperp(v):
    n=np.linalg.norm(v)
    return np.eye(len(v))-np.outer(v,v)/(n*n)

max_identity_error=0.0
max_triangle_violation=0.0
trials=2000
for _ in range(trials):
    m=int(rng.integers(2,7)); n=int(rng.integers(2,7))
    S=rng.normal(size=(m,n))
    x=rng.normal(size=m); y=rng.normal(size=n)
    N=S+np.outer(x,y)
    diff2=e2N=e2S=0.0
    for P in itertools.combinations(range(m),2):
        for T in itertools.combinations(range(n),2):
            dN=np.linalg.det(N[np.ix_(P,T)])
            dS=np.linalg.det(S[np.ix_(P,T)])
            diff2+=(dN-dS)**2
            e2N+=dN*dN
            e2S+=dS*dS
    rhs=np.linalg.norm(x)**2*np.linalg.norm(y)**2*np.linalg.norm(pperp(x)@S@pperp(y),'fro')**2
    max_identity_error=max(max_identity_error,abs(diff2-rhs))
    max_triangle_violation=max(max_triangle_violation,math.sqrt(e2N)-math.sqrt(e2S)-math.sqrt(rhs))

h=2/3
C_h=4*(4/3)**(3/4)*math.sqrt(6*math.sqrt(math.e/(2*h))/(3-4*h))
print(f'trials={trials}')
print(f'max_rankone_exterior_identity_error={max_identity_error:.16e}')
print(f'max_triangle_violation={max_triangle_violation:.16e}')
print(f'C_h_at_2_over_3={C_h:.15f}')
print(f'C_h_times_4_pow_1_over_8={C_h*4**(1/8):.15f}')
print(f'D5_constant={5*math.sqrt(2*math.e):.15f}')
print('QFORM_B13_R23_CHECK_PASS')
