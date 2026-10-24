"""Exact finite-state checks and an analytic, non-Monte-Carlo CLT obstruction."""
from fractions import Fraction as F
from pathlib import Path
import json
import math
import time

ROOT = Path(__file__).resolve().parent

def case(s):
    a = 1 - F(1, s*s)
    e = (1-a*a)/(5-4*a)
    b = (5-4*a)/(2-a)
    r = F(s**4)
    states = [(y,z) for y in (0,1) for z in (-1,1)]
    pi = [(e if y else 1-e)/2 for y,z in states]
    q = [[F(0) for _ in states] for _ in states]
    for i,(y,z) in enumerate(states):
        for j,(v,w) in enumerate(states):
            if v == 1-y and w == z:
                q[i][j] = 1-e if y else e
            elif v == y and w == -z:
                q[i][j] = r/2
        q[i][i] = -sum(q[i])
    obs = [a*z + b*(y-e) for y,z in states]
    assert all(sum(row) == 0 for row in q)
    assert all(pi[i]*q[i][j] == pi[j]*q[j][i] for i in range(4) for j in range(4))
    assert sum(pi[i]*obs[i] for i in range(4)) == 0
    assert sum(pi[i]*obs[i]**2 for i in range(4)) == 1
    assert max(map(abs,obs)) == 2
    assert max(-q[i][i]/r for i in range(4))<=1
    # A basis of eigenfunctions, not a floating-point eigensolver.
    for vector,eigenvalue in [([F(1)]*4,F(0)),([y-e for y,z in states],F(1)),
                              ([F(z) for y,z in states],r),
                              ([(y-e)*z for y,z in states],r+1)]:
        assert all(sum(q[i][j]*vector[j] for j in range(4)) == -eigenvalue*vector[i] for i in range(4))
    sig2 = 2*a*a/r + 2*b*b*e*(1-e)
    af,bf,ef,rf,sf = map(float,(a,b,e,r,sig2))
    center = -bf*ef*math.sqrt(s)/math.sqrt(sf)
    delta = 1/math.sqrt(s)
    fast_var_bound = float((2*a*a/r)/sig2)
    no_visit = (1-ef)*math.exp(-ef*s)
    x = center+delta
    phi = 0.5*(1+math.erf(x/math.sqrt(2)))
    lower = no_visit-fast_var_bound/delta**2-phi
    # Exact covariance integral for BOTH chains, not a Gaussian replacement.
    var_integral = 2*af*af*(s/rf + math.expm1(-rf*s)/rf**2) + 2*bf*bf*ef*(1-ef)*(s+math.expm1(-s))
    second = var_integral/(sf*s)
    assert lower > 0 if s>=10 else math.isfinite(lower)
    return {"s":s,"epsilon_exact":str(e),"gap_exact":"1","observable_sup_exact":"2",
            "observable_variance_exact":"1","no_visit_probability":no_visit,
            "threshold":x,"chebyshev_fast_error_bound":fast_var_bound/delta**2,
            "kolmogorov_lower_bound":lower,"normalized_second_moment":second,
            "scaled_max_total_jump_rate":float(max(-q[i][i]/r for i in range(4))),
            "exact_checks_per_case":7}

def main():
    start=time.perf_counter()
    rows=[case(s) for s in (10,30,100,300,1000,10000)]
    output={"command":"python -X utf8 p0209_check.py","label":"exact finite algebra plus analytic probability bound",
            "random_samples":0,"gaussian_surrogate":False,"cases":rows,
            "elapsed_seconds":time.perf_counter()-start}
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/'p0209.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output,indent=2))

if __name__=='__main__':
    main()
