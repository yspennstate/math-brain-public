"""Small independent checks; no imports from peer proof/checker files."""
from fractions import Fraction
import json
import math
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent

def simpson(fn, a, b, n=10000):
    step = (b-a)/n
    return step/3 * (fn(a)+fn(b)+sum((4 if i%2 else 2)*fn(a+i*step) for i in range(1,n)))

def main():
    begin=time.perf_counter()
    checks=[]
    for d in range(1,65):
        squared=(Fraction(math.factorial(2*d),math.factorial(d)**2)
                 -2*Fraction(math.factorial(2*d-1),math.factorial(d)*math.factorial(d-1))
                 +Fraction(math.factorial(2*d-2),math.factorial(d-1)**2))
        expected=math.comb(2*d-2,d-1)
        assert squared==expected and expected<=4**(d-1)
        checks.append({'degree':d,'squared_norm':str(squared),'expected':str(expected)})
    moments={str(k):simpson(lambda s,k=k:s**(k+1)*math.exp(-s),0,40) for k in range(5)}
    for k,value in moments.items():
        assert abs(value-math.factorial(int(k)+1))<2e-8
    e_s,e_s2=moments['1'],moments['2']
    covariance={'var_x':(e_s2-e_s**2)/2,'var_z':e_s2/6,'cov_x_z':0.0}
    assert abs(covariance['var_x']-1)<1e-8 and abs(covariance['var_z']-1)<1e-8
    widths=[1,2,4,8]
    fibres=[{'width':a,'conditional_variance':str(Fraction(a*a,3))} for a in widths]
    x=8-math.sqrt(2)
    eps=1e-5
    mean=lambda x:(x+math.sqrt(2))**2/3
    derivative=(mean(x+eps)-mean(x-eps))/(2*eps)
    expected_derivative=16/3
    assert abs(derivative-expected_derivative)<1e-8
    tilted=[{'s':s,'variance':1/(1-s)**2} for s in [0.0,0.5,0.9,0.99]]
    damped=[{'t':t,'theta':1-t,'variance':(1-2/math.pi)/t} for t in [1,0.1,0.01]]
    report={'command':'python -X utf8 ~/brain_workers/w359/verify_math.py',
            'exact_degree_checks':len(checks),'degree_checks':checks,'gamma_moments':moments,
            'cone_covariance':covariance,'conditional_fibres':fibres,
            'conditional_derivative':derivative,'conditional_partial_derivative':0,
            'linear_tilt_variances':tilted,'gaussian_damped_tilt_variances':damped,
            'elapsed_seconds':time.perf_counter()-begin,'formal_proof':False}
    assert report['elapsed_seconds']<30
    (ROOT/'MATH_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['exact_degree_checks','cone_covariance','conditional_fibres','conditional_derivative','conditional_partial_derivative','elapsed_seconds']},indent=2))

if __name__=='__main__':
    main()
