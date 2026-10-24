import itertools
import math
import numpy as np

rng=np.random.default_rng(1902302)
max_expansion_relative_error=0.0
for trial in range(25):
    m,n=5,6
    B=rng.normal(size=(m,n))
    y=rng.random(n)+0.2
    z=rng.random(m)+0.2
    a=1.3+rng.random()
    lhs=float(np.linalg.det(np.diag(y)+a*a*B.T@np.diag(z)@B))
    rhs=0.0
    for r in range(min(m,n)+1):
        for R in itertools.combinations(range(m),r):
            for S in itertools.combinations(range(n),r):
                det=1.0 if r==0 else float(np.linalg.det(B[np.ix_(R,S)]))
                Sset=set(S)
                py=np.prod([y[j] for j in range(n) if j not in Sset]) if n-r else 1.0
                pz=np.prod([z[i] for i in R]) if r else 1.0
                rhs += (a**(2*r))*det*det*py*pz
    err=abs(lhs-rhs)/max(1.0,abs(lhs))
    max_expansion_relative_error=max(max_expansion_relative_error,err)

cs=np.linspace(0.0,1.0,10001)
G=(2.0**cs)*(1.0+cs)**(-(1.0+cs)/2.0)
tangent=np.exp((1.0-math.log(2.0))*(1.0-cs)/2.0)
max_tangent_violation=float(np.max(G-tangent))

density_constant=3.0*math.e/math.sqrt(2.0)
tail_constant=(math.pi**1.5)*(math.e**1.5)*(2.0**(-0.75))

print(f'max_expansion_relative_error={max_expansion_relative_error:.17g}')
print(f'max_G_tangent_violation={max_tangent_violation:.17g}')
print(f'density_constant_3e_over_sqrt2={density_constant:.15f}')
print(f'tail_constant={tail_constant:.15f}')
assert max_expansion_relative_error < 1e-12
assert max_tangent_violation < 1e-12
assert abs(density_constant-5.766346542238675) < 1e-12
print('STATUS=PASS')
