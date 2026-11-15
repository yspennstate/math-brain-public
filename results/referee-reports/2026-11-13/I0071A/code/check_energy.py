"""Exact finite algebra checks for REPORT.md (not a simulation or a proof)."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def indices(total, ell):
    if ell == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in indices(total - first, ell - 1):
                yield (first,) + tail

def plus(alpha, i, j=None):
    out = list(alpha)
    out[i] += 1
    if j is not None:
        out[j] += 1
    return tuple(out)

def multinomial(alpha):
    out = factorial(sum(alpha))
    for a in alpha:
        out //= factorial(a)
    return out

def value(alpha, y):
    out = F(1)
    for a, yi in zip(alpha, y):
        out *= yi ** a
    return out

def run(ell, m):
    theta = F(8)
    # A dense, nonnegative, invertible triangular matrix, not just partial sums.
    R = [[F(0) if j > i else F(1 + ((i + 2*j) % 4), j + 1)
          for j in range(ell)] for i in range(ell)]
    t = [F(1)] * ell
    for i in reversed(range(ell - 1)):
        t[i] = theta ** (2*(m-1)) * (1 + sum(R[j][i]/R[j][j]*t[j]
                                           for j in range(i+1, ell)))
    def coefficient(a):
        return theta ** sum(ai*ai for ai in a) * value(a, t)
    checks = 0
    for beta in indices(m-1, ell):
        v = [coefficient(plus(beta, i)) for i in range(ell)]
        eta = [F(0)] * ell
        for i in reversed(range(ell)):
            eta[i] = (v[i] - sum(R[j][i]*eta[j] for j in range(i+1, ell)))/R[i][i]
        assert min(eta) >= 0
        assert all(sum(R[j][i]*eta[j] for j in range(i, ell)) == v[i]
                   for i in range(ell))
        checks += 1
    for beta in indices(m-2, ell):
        for i in range(ell):
            for j in range(i+1, ell):
                assert coefficient(plus(beta, i, j))**2 * theta**4 == (
                    coefficient(plus(beta, i, i))*coefficient(plus(beta, j, j)))
                checks += 1
    # Differentiate the original polynomial directly and compare with (7)
    # and with Euler's two identities, including boundary points.
    for y in [tuple(F(i+1, 3) for i in range(ell)),
              tuple(F(int(i == ell-1)) for i in range(ell)), (F(0),)*ell]:
        phi = F(0)
        grad = [F(0)]*ell
        H = [[F(0) for j in range(ell)] for i in range(ell)]
        for alpha in indices(m, ell):
            c = multinomial(alpha)*coefficient(alpha)
            phi += c*value(alpha, y)
            for i in range(ell):
                if alpha[i]:
                    a = list(alpha)
                    a[i] -= 1
                    grad[i] += c*alpha[i]*value(a, y)
                    for j in range(ell):
                        if a[j]:
                            b = a.copy()
                            b[j] -= 1
                            H[i][j] += c*alpha[i]*a[j]*value(b, y)
        assert sum(y[i]*grad[i] for i in range(ell)) == m*phi
        assert sum(y[i]*H[i][j]*y[j] for i in range(ell) for j in range(ell)) == m*(m-1)*phi
        for i in range(ell):
            for j in range(ell):
                decomp = m*(m-1)*sum(multinomial(beta)*value(beta, y)*
                                    coefficient(plus(beta, i, j))
                                    for beta in indices(m-2, ell))
                assert H[i][j] == decomp
                checks += 1
        # Independent evaluation of the full leading Itô form with unequal
        # species coefficients, two spatial directions and two Brownian modes.
        nu = [F(1) + F(i, 4) for i in range(ell)]
        b = [[[F((((n+1)*(i+2)+k) % 3)-1, 5) for k in range(2)]
              for i in range(ell)] for n in range(2)]
        z = [(F(i+1, 3), F((-1)**i, 2)) for i in range(ell)]
        dot = lambda a, bb: sum(x*yy for x, yy in zip(a, bb))
        # sum_n |b_ni|^2 <= 4/25 and 2nu_i >= 2, so mu=1 works.
        assert all(sum(dot(b[n][i], b[n][i]) for n in range(2)) <= F(4,25)
                   for i in range(ell))
        K = max(nu) + F(1,2)  # overestimate B^2 by 1
        assert theta**-2 * K * (ell-1) <= F(1,4)
        Q = sum(H[i][j]*((nu[i]+nu[j])/2 * dot(z[i],z[j]) -
                        F(1,2)*sum(dot(b[n][i],z[i])*dot(b[n][j],z[j])
                                   for n in range(2)))
                for i in range(ell) for j in range(ell))
        D = sum(H[i][i]*dot(z[i], z[i]) for i in range(ell))
        assert Q >= D/4
        checks += 1
    return {'species': ell, 'energy_degree': m, 'theta': str(theta),
            'exact_identity_and_cone_checks': checks, 'passed': True}

if __name__ == '__main__':
    records = [run(2, 2), run(2, 5), run(3, 4), run(4, 6)]
    (ROOT/'data'/'energy_checks.json').write_text(json.dumps(records, indent=2)+'\n')
    print(json.dumps(records))
