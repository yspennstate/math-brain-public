"""Small exact algebra checks for the accompanying manuscript (no sampling)."""
import os
for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
import json
from pathlib import Path
import sympy as s

checks = {}
for n in range(1, 5):
    d = s.symbols(f"d1:{n+1}", positive=True)
    ell = s.symbols(f"l1:{n}", positive=True)
    src, dst = [], []
    for i in range(n):
        src.append(d[i])
        dst.append(d[i]**2 + (ell[i-1]**2 if i else 0))
        if i < n-1:
            src.append(ell[i])
            dst.append(d[i]*ell[i])
    determinant = s.factor(s.Matrix(dst).jacobian(src).det())
    expected = 2**n*d[-1]*s.prod(x**2 for x in d[:-1])
    assert s.simplify(determinant-expected) == 0
    checks[f"Cholesky_Jacobian_n={n}"] = str(determinant)

lam1, lam2, q = s.symbols("lambda1 lambda2 q", real=True)
gap = lam2-lam1
b = gap*s.sqrt(q*(1-q))
coords = s.Matrix([q*lam1+(1-q)*lam2, (1-q)*lam1+q*lam2, b])
det = s.simplify(coords.jacobian([lam1,lam2,q]).det())
assert s.simplify(det**2-(gap**2/(2*b))**2) == 0
checks["canonical_size_two_Jacobian_squared"] = "gap^4/(4 b^2)"

n, i, theta, a = s.symbols("n i theta a", positive=True)
trace_shape = s.summation(theta*(a+i),(i,1,n))+s.summation(theta*i,(i,1,n-1))
assert s.simplify(trace_shape-theta*n*(n+a)) == 0
checks["trace_gamma_shape"] = str(s.factor(trace_shape))
# E tr L^2 from independent primitive gamma moments, compared with
# integration by parts in the eigenvalue density.
entry_p2 = s.summation((a+i)**2+(a+i)/theta,(i,1,n))
entry_p2 += s.summation(i**2+i/theta+2*(a+i+1)*i+2*(a+i)*i,(i,1,n-1))
spectral_p2 = n*(n+a)*(2*n+a-1+1/theta)
assert s.simplify(entry_p2-spectral_p2) == 0
checks["second_spectral_moment"] = str(s.factor(spectral_p2))

S = s.symbols("S", positive=True)
var = (4*S*(S+1)/((S+theta)*(S+theta+1))/(S+1)
       +4*theta*(theta+1)/((S+theta)*(S+theta+1))/(S+2*theta+1))/16
assert s.simplify(var-1/(4*(S+2*theta+1))) == 0
checks["reversed_symmetric_Jacobi_variance"] = str(s.factor(var))

u1,u2,v1,v2 = s.symbols("u1 u2 v1 v2", positive=True)
D1=u1+v1
E1=v1*u2/D1
w2=u1*u2/D1
D2=w2+v2
assert s.simplify(D2+E1-(u2+v2)) == 0
assert s.simplify(D1*E1-v1*u2) == 0
checks["odd_antisymmetric_Gram_Cholesky_m=2"] = "exact diagonal and off-diagonal-square identities"
checks["antisymmetric_powers"] = {"even": str(2*(theta/2-1)+1),
                                      "odd": str(2*(3*theta/2-1)+1)}
try:
    checks["inherited_niceness"] = os.getpriority(os.PRIO_PROCESS, 0)
except (AttributeError, PermissionError) as exc:
    checks["inherited_niceness"] = str(exc)
Path("exact-checks.json").write_text(json.dumps(checks, indent=2)+"\n")
print(json.dumps(checks, indent=2))
