"""Finite algebra checks of the affine extension, not a universal proof.
Run with Python 3.10+ and scipy/sympy installed. No network or input data.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
import sympy as sp
from scipy.integrate import quad


def main() -> None:
    s,z,beta,gamma,delta,d,l0 = sp.symbols('s z beta gamma delta d l0', real=True)
    original = beta*s*s + 2*gamma*s*z + delta*z*z + d*s+l0
    residual = (beta*delta-gamma**2)*z*z/beta-gamma*d*z/beta-d*d/(4*beta)+l0
    completed = beta*(s+gamma*z/beta+d/(2*beta))**2+residual
    assert sp.simplify(original-completed) == 0
    assert sp.simplify(sp.diff(residual,z,2)/2-(beta*delta-gamma**2)/beta) == 0

    k,B,D = sp.symbols('k B D', positive=True)
    expr = k/sp.sqrt(B)*(k*k*D/(B*B))**(-sp.Rational(1,4))
    assert sp.simplify(expr-sp.sqrt(k)*D**(-sp.Rational(1,4))) == 0

    v = .25
    c_rank1 = math.exp(.75)*math.gamma(.25)
    assert c_rank1 < math.exp(.75)*(4+math.exp(-1)) < 10
    c_rank2 = 32*math.sqrt(10)*2**.25
    assert c_rank2 < 128
    gaussian_cases = []
    for rho in [.001,.1,1.,10.,1000.]:
        # Substitute t=2 sqrt(v) u/rho, then u=w^2 to remove u^-1/2.
        radial = quad(lambda w: 2*math.exp(-w**4),0,math.inf,epsabs=1e-10)[0]
        integral = 2*(2*math.sqrt(v)/rho)**.5*radial
        numeric = math.exp(v)*rho/(2*math.sqrt(math.pi*v))*math.sqrt(math.e*math.pi)*integral
        exact = c_rank1*math.sqrt(rho)
        error = abs(numeric/exact-1)
        assert error < 1e-10
        gaussian_cases.append({'rho':rho,'relative_error':error})
    result = {
        'scope':'finite symbolic and scalar checks, not independent or universal proof verification',
        'status':'PASS',
        'affine_square_completion':'PASS',
        'residual_rank_one_quadratic_coefficient':'PASS',
        'beta_cancellation':'PASS',
        'rank_one_fourier_constant':c_rank1,
        'rank_one_elementary_upper_bound':math.exp(.75)*(4+math.exp(-1)),
        'rank_two_heavy_bound_before_rounding':c_rank2,
        'rank_two_stated_constant':128,
        'gaussian_majorant_cases':gaussian_cases,
    }
    output = Path(__file__).with_name('affine_check_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
