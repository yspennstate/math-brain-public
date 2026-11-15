"""Independent finite checks. Exact rational algebra; no submitted code imported."""
from fractions import Fraction as F
from itertools import product
from math import factorial, prod
from pathlib import Path
import json
import os

ROOT = Path(__file__).resolve().parents[1]
try:
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
except (AttributeError, PermissionError):
    pass

def multi(n, degree):
    return [a for a in product(range(degree + 1), repeat=n) if sum(a) == degree]

def coefficient(alpha, t, theta):
    return theta ** sum(a*a for a in alpha) * prod(x**a for x, a in zip(t, alpha))

def shifted(a, i, j=None):
    b = list(a)
    b[i] += 1
    if j is not None:
        b[j] += 1
    return tuple(b)

def run(n, degree):
    # Dense triangular matrices, including a non-unit diagonal.
    R = ([[F(2), 0], [F(3), F(5)]] if n == 2 else
         [[F(2), 0, 0], [F(3), F(5), 0], [F(7), F(11), F(13)]])
    theta = F(8)
    t = [F(1)] * n
    for i in range(n-2, -1, -1):
        t[i] = theta**(2*(degree-1)) * (1 + sum(R[j][i]/R[j][j] * t[j] for j in range(i+1, n)))
    c = lambda a: coefficient(a, t, theta)
    cone_checks = 0
    for beta in multi(n, degree-1):
        v = [c(shifted(beta, i)) for i in range(n)]
        eta = [F(0)] * n
        for i in range(n-1, -1, -1):
            eta[i] = (v[i] - sum(R[j][i]*eta[j] for j in range(i+1, n)))/R[i][i]
        assert min(eta) >= 0
        assert all(sum(R[j][i]*eta[j] for j in range(i, n)) == v[i] for i in range(n))
        cone_checks += 1
    midpoint_checks = 0
    for beta in multi(n, degree-2):
        for i in range(n):
            for j in range(i):
                assert c(shifted(beta, i, j))**2 == theta**(-4)*c(shifted(beta, i, i))*c(shifted(beta, j, j))
                midpoint_checks += 1
    differential_checks = 0
    form_checks = 0
    for y in [tuple(F(i+1, 3) for i in range(n)), tuple(F(0) for _ in range(n)),
              *[tuple(F(i == j) for i in range(n)) for j in range(n)]]:
        phi = F(0)
        grad = [F(0)] * n
        H = [[F(0)] * n for _ in range(n)]
        for a in multi(n, degree):
            mult = factorial(degree) // prod(factorial(k) for k in a)
            A = mult*c(a)
            phi += A*prod(yj**aj for yj, aj in zip(y, a))
            for i in range(n):
                if not a[i]:
                    continue
                power = list(a)
                power[i] -= 1
                grad[i] += A*a[i]*prod(yj**aj for yj, aj in zip(y, power))
                for j in range(n):
                    if power[j]:
                        power2 = power.copy()
                        power2[j] -= 1
                        H[i][j] += A*a[i]*power[j]*prod(yj**aj for yj, aj in zip(y, power2))
        assert phi > 0 if any(y) else phi == 0
        assert sum(y[i]*grad[i] for i in range(n)) == degree*phi
        assert sum(y[i]*H[i][j]*y[j] for i in range(n) for j in range(n)) == degree*(degree-1)*phi
        for i in range(n):
            for j in range(n):
                decomp = degree*(degree-1)*sum(
                    F(factorial(degree-2), prod(factorial(k) for k in beta))*
                    prod(yj**bj for yj, bj in zip(y, beta))*c(shifted(beta, i, j))
                    for beta in multi(n, degree-2))
                assert H[i][j] == decomp
                differential_checks += 1
        # Opposite transports; then unequal diffusivities and two Brownian modes.
        for unequal in [False, True]:
            nu = [F(i+1) if unequal else F(1) for i in range(n)]
            b = [F((-1)**i) for i in range(n)]
            second = [F(i,n+1) if unequal else F(0) for i in range(n)]
            assert all(2*nu[i]-b[i]**2 >= 1 and 2*nu[i]-second[i]**2 >= 1 for i in range(n))
            assert theta**(-2)*(max(nu)+F(1,2)*(1+max(second)**2))*(n-1) <= F(1,4)
            for z in product([-1, 0, 1], repeat=2*n):
                Q = sum(H[i][j]*((nu[i]+nu[j])/2*(z[2*i]*z[2*j]+z[2*i+1]*z[2*j+1])-
                                F(1,2)*(b[i]*b[j]*z[2*i]*z[2*j]+
                                        second[i]*second[j]*z[2*i+1]*z[2*j+1]))
                        for i in range(n) for j in range(n))
                D = sum(H[i][i]*(z[2*i]**2+z[2*i+1]**2) for i in range(n))
                assert Q >= D/4
                form_checks += 1
    return dict(species=n, degree=degree, cone_checks=cone_checks,
                midpoint_checks=midpoint_checks, differential_checks=differential_checks,
                full_ito_form_checks=form_checks, passed=True)

def generic_counterexample():
    # Phi=(u1+u2)^2/2, H_ij=1; nu=1, b=(1,-1), z=(1,-1).
    b, z = [1, -1], [1, -1]
    diffusion = sum(z[i]*z[j] for i in range(2) for j in range(2))
    correction = F(1, 2)*sum(b[i]*z[i]*b[j]*z[j] for i in range(2) for j in range(2))
    assert diffusion - correction == -2
    # The constructed m=2 Hessian, in normalized gradient coordinates, has
    # diagonal 1 and off-diagonal theta^-2. For theta=3 its Q has eigenvalues
    # 1/2 +/- 3/(2*9), so the lower bound 1/4 holds.
    rho = F(1,9)
    minimum = F(1,2)-F(3,2)*rho
    assert minimum >= F(1,4)
    return dict(generic_Q=str(diffusion-correction), correct_margin_mu=1,
                constructed_normalized_minimum=str(minimum), constructed_target="1/4")

if __name__ == '__main__':
    records = [run(n, degree) for n, degree in [(2,2), (2,3), (2,5), (3,2), (3,3), (3,4)]]
    result = dict(cases=records, counterexample=generic_counterexample(),
                  counted_checks=sum(sum(v for k,v in r.items() if k.endswith('_checks')) for r in records),
                  nice=os.getpriority(os.PRIO_PROCESS,0))
    (ROOT/'data'/'independent_algebra.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
