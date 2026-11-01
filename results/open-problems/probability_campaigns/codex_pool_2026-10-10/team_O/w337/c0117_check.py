from fractions import Fraction as F
from pathlib import Path
import json
import math
import time

ROOT=Path(__file__).resolve().parent

def geometric_cumulant(m,theta):
    lam=theta/m
    total=0.0
    for k in range(1,m+1):
        p=k/m
        q=1-p
        total+=math.log(p)+lam-math.log1p(-q*math.exp(lam))-lam/p
    return total

def exponential_cumulant(m,theta):
    return sum(-math.log1p(-theta/k)-theta/k for k in range(1,m+1))

def main():
    start=time.perf_counter()
    harmonic=F(0); harmonic2=F(0)
    rows=[]
    for m in range(1,201):
        harmonic+=F(1,m); harmonic2+=F(1,m*m)
        discrete=harmonic2-harmonic/m
        continuous=harmonic2
        assert discrete>=0 and continuous>=discrete
        if m==5:
            assert discrete==F(145,144)
        if m==2:
            assert continuous==F(5,4)
        for theta in (-0.25,0.25):
            kg=geometric_cumulant(m,theta)
            ke=exponential_cumulant(m,theta)
            assert kg<=4*theta**2+1e-10
            assert ke<=4*theta**2+1e-10
        if m in (1,2,5,10,100,200):
            rows.append({'n':m+1,'t_hit_exact':str(m),'mean_exact':str(m*harmonic),
                         'discrete_variance_over_t_hit_squared_exact':str(discrete),
                         'continuous_variance_over_t_hit_squared_exact':str(continuous),
                         'discrete_sd_over_t_hit':math.sqrt(float(discrete)),
                         'continuous_sd_over_t_hit':math.sqrt(float(continuous))})
    result={'command':'python -X utf8 c0117_check.py','exact_harmonic_cases':200,
            'cumulant_checks':800,'discrete_unit_bound_counterexample':'K_6: 145/144',
            'continuous_unit_bound_counterexample':'K_3: 5/4','cases':rows,
            'elapsed_seconds':time.perf_counter()-start}
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/'c0117.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))

if __name__=='__main__':
    main()
