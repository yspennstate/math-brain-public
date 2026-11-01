"""Exact polynomial identities and rational bounds for QSO_GLOBAL_051.md.

The universal dynamical argument is in the note. This script checks its finite
algebra using the standard library, without floating-point evidence.
"""
from fractions import Fraction as F
from math import comb
import json


def evaluate(coefficients, x):
    return sum((F(c)*x**i for i, c in enumerate(coefficients)), F(0))


def derivative(coefficients):
    return [i*F(c) for i,c in enumerate(coefficients) if i]


def main():
    # Lambda-polynomial coefficients, in increasing degree, for each u degree.
    power = [[1,-2,1,1],[-1,2,1,-2],[0,2,-3,-1],
             [0,0,-2,2],[0,0,0,1]]
    bernstein = [[1,-2,1,1], [F(3,4),F(-3,2),F(5,4),F(1,2)],
                 [F(1,2),F(-2,3),1,F(-1,6)],
                 [F(1,4),F(1,2),F(-1,4),F(-1,2)], [0,2,-3,1]]
    reconstructed = [[F(0) for _ in range(4)] for _ in range(5)]
    for k, polynomial in enumerate(bernstein):
        for j in range(5-k):
            factor = comb(4,k)*comb(4-k,j)*(-1)**j
            for degree,c in enumerate(polynomial):
                reconstructed[k+j][degree] += factor*c
    assert reconstructed == power
    lo, hi = F(1,2), F(51,100)
    first = [derivative(p) for p in bernstein]
    second = [derivative(p) for p in first]
    # Each second derivative is affine; endpoint signs prove monotonicity of b'.
    increasing_derivatives = [0,1,2]
    decreasing_derivatives = [3,4]
    for k in increasing_derivatives:
        assert evaluate(second[k],lo)>0 and evaluate(second[k],hi)>0
    for k in decreasing_derivatives:
        assert evaluate(second[k],lo)<0 and evaluate(second[k],hi)<0
    assert evaluate(first[0],hi)<0
    assert evaluate(first[1],lo)>0 and evaluate(first[2],lo)>0
    assert evaluate(first[3],lo)<0 and evaluate(first[4],lo)<0
    upper = [evaluate(bernstein[k],hi if k in (1,2) else lo)
             for k in range(5)]
    assert upper == [F(3,8),F(752901,2000000),F(795983,2000000),F(3,8),F(3,8)]
    assert max(upper)<F(2,5)
    assert hi**2*(2-hi)==F(387549,1000000)<F(2,5)
    epsilon, d = F(1,50), F(1,5)
    theta = epsilon/(d-F(100,49)*epsilon)**2
    h = (d-epsilon)*(1-theta)
    assert theta==F(2401,3042)<1
    assert h==F(641,16900)>epsilon
    rate = 2*hi*(1-epsilon)
    assert rate==F(2499,2500)<1
    assert 1-lo/5==F(9,10)<rate
    assert 3*hi-1==F(53,100)<rate
    # Earlier perturbative proof, retained independently in the archive.
    endpoint = F(251,500)
    perturbation_constant=3+2*(1+(1+endpoint)+(1+endpoint)**2)
    assert perturbation_constant==F(1564501,125000)<13
    assert F(7967,8192)+F(13,500)==F(1022499,1024000)<1
    return {'status':'all exact checks passed',
            'bernstein_lambda_coefficients':[[str(c) for c in p] for p in bernstein],
            'bernstein_upper_bounds':[str(x) for x in upper],
            'v_zero_upper':'387549/1000000',
            'theta_upper':str(theta),'small_coordinate_overlap_lower':str(h),
            'uniform_overlap':str(epsilon),'contraction_factor':str(rate),
            'limitation':'finite algebra check; the full proof is in QSO_GLOBAL_051.md'}


if __name__=='__main__':
    print(json.dumps(main(),indent=2))
