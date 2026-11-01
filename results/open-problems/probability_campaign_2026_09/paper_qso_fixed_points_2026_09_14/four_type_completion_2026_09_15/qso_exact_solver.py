"""Certified fixed point of a four-type strictly non-Volterra QSO.

Python 3, standard library only. Input coefficients must be exact rational
numbers (ints, fractions, or strings such as '2/3'); floats are rejected.
solve(P, epsilon) returns exact integer counts and a rational error certificate.
Run this file to reproduce the accompanying example_results.json.
"""
from fractions import Fraction
from math import lcm
import json
from pathlib import Path


def exact(value):
    if isinstance(value, float):
        raise TypeError('Use exact rational input, not a float.')
    return Fraction(value)


def validate(P):
    if len(P) != 4 or any(len(a) != 4 for a in P):
        raise ValueError('Expected a 4 by 4 by 4 tensor.')
    if any(len(P[i][j]) != 4 for i in range(4) for j in range(4)):
        raise ValueError('Expected four output coefficients in each row.')
    P = [[[exact(v) for v in row] for row in plane] for plane in P]
    for i in range(4):
        for j in range(4):
            row = P[i][j]
            if any(v < 0 for v in row) or sum(row) != 1:
                raise ValueError('Every coefficient row must be a probability vector.')
            if row != P[j][i] or row[i] or row[j]:
                raise ValueError('Parent symmetry or strict exclusion failed.')
    return P


def solve(P, epsilon):
    P = validate(P)
    eps = exact(epsilon)
    if eps <= 0:
        raise ValueError('Tolerance must be positive.')
    a, b = eps.numerator, eps.denominator
    N = 20 * max(1, (75*b+a-1)//a)
    goal = max(1, (60*b+a-1)//a)
    k = (goal-1).bit_length()
    horizon = 9*k
    D = lcm(*(P[i][j][r].denominator
              for i in range(4) for j in range(i,4) for r in range(4)))
    C = [[[int(D*v) for v in row] for row in plane] for plane in P]
    n = [N//4]*4
    for step in range(horizon+1):
        S = [sum((1 if i == j else 2)*C[i][j][r]*n[i]*n[j]
                 for i in range(4) for j in range(i,4)) for r in range(4)]
        residual = Fraction(sum(abs(S[r]-D*N*n[r]) for r in range(4)), D*N*N)
        certificate = 5*residual
        if certificate <= eps:
            return {'counts': n, 'denominator': N,
                    'point': [str(Fraction(v,N)) for v in n],
                    'residual': str(residual), 'error_bound_l1': str(certificate),
                    'tolerance': str(eps), 'steps': step, 'proved_horizon': horizon}
        if step == horizon:
            raise ArithmeticError('The proved exact-arithmetic guarantee was violated.')
        qr = [divmod(3*D*N*n[r]+2*S[r],5*D*N) for r in range(4)]
        next_n = [v[0] for v in qr]
        remaining = N-sum(next_n)
        order = sorted(range(4), key=lambda r:(-qr[r][1],r))
        for r in order[:remaining]:
            next_n[r] += 1
        if sum(next_n) != N or min(next_n) < 0 or max(next_n)*5 > 2*N:
            raise ArithmeticError('Rounding left the invariant capped simplex.')
        n = next_n


def tensor(rule):
    P = [[[Fraction(0) for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(i,4):
            row = rule(i,j)
            for r,v in row.items():
                P[i][j][r] = P[j][i][r] = exact(v)
    return validate(P)


def cap_rule(i,j):
    if i != 0 and j != 0:
        return {0:1}
    allowed = [r for r in range(4) if r not in (i,j)]
    return {r:Fraction(1,len(allowed)) for r in allowed}


def boundary_rule(i,j):
    allowed = [r for r in range(3) if r not in (i,j)]
    return {r:Fraction(1,len(allowed)) for r in allowed}


def asymmetric_rule(i,j):
    allowed = [r for r in range(4) if r not in (i,j)]
    total = sum(r+1 for r in allowed)
    return {r:Fraction(r+1,total) for r in allowed}


def evaluate(P,x):
    return [sum(P[i][j][r]*x[i]*x[j] for i in range(4) for j in range(4))
            for r in range(4)]


def run_examples():
    output = {}
    for name,P,eps in [('sharp_cap',tensor(cap_rule),'1/100000000'),
                       ('boundary',tensor(boundary_rule),'7/1000000'),
                       ('asymmetric',tensor(asymmetric_rule),'1/100000000')]:
        result = solve(P,eps)
        x = list(map(Fraction,result['point']))
        independent_residual = sum(abs(u-v) for u,v in zip(evaluate(P,x),x))
        assert str(independent_residual) == result['residual']
        assert 5*independent_residual <= Fraction(eps)
        result['independent_fraction_residual_verified'] = True
        if name == 'boundary':
            p = [Fraction(1,3)]*3+[Fraction(0)]
            assert evaluate(P,p) == p
            err = sum(abs(u-v) for u,v in zip(x,p))
            assert err <= 5*independent_residual
            result['known_fixed_point_error_l1'] = str(err)
        output[name] = {'result':result,'coefficients':[[[str(v) for v in row]
                                      for row in plane] for plane in P]}
    swap = {0:1,1:0,2:3,3:2}
    def cycle_rule(i,j):
        if i == j:
            return {swap[i]:1}
        return {r:Fraction(1,2) for r in range(4) if r not in (i,j)}
    P = tensor(cycle_rule)
    e1 = [Fraction(1),Fraction(0),Fraction(0),Fraction(0)]
    e2 = [Fraction(0),Fraction(1),Fraction(0),Fraction(0)]
    u = [Fraction(1,4)]*4
    assert evaluate(P,e1) == e2 and evaluate(P,e2) == e1 and evaluate(P,u) == u
    output['raw_two_cycle'] = {'e1_maps_to_e2':True,'e2_maps_to_e1':True,
                              'uniform_is_fixed':True}
    target = Path(__file__).with_name('example_results.json')
    target.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({name:v.get('result',v) for name,v in output.items()},indent=2))


if __name__ == '__main__':
    run_examples()
