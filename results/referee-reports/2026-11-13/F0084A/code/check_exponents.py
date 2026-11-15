#!/usr/bin/env python3
"""Check HPPS (2009), equation (21), using independent quadratures.

No allocation simulation is run: the user requested stopping on a literature
resolution. Both methods below use the published equation, not fitted data.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import json, math, time
from pathlib import Path
import mpmath as mp
from scipy.integrate import quad
from scipy.optimize import brentq
mp.mp.dps = 40

def sphere(d):
    return 2*mp.pi**(mp.mpf(d)/2)/mp.gamma(mp.mpf(d)/2)

def equation_mp(s,d):
    # Right integral in (21), evaluated by the beta integral.
    left = 2*sphere(d)*mp.quad(lambda t: (t-1)**(d-1)*t**(-s),[1,2])
    right = sphere(d-1)/(d-1)*2**(-s)*mp.beta((1-s)/2,mp.mpf(d+1)/2)
    return left-right

def equation_scipy(s,d):
    # Independent real quadrature; t = 2*u**(1/(1-s)) removes
    # the integrable singularity at t = 0 from the right integral.
    wd = 2*math.pi**(d/2)/math.gamma(d/2)
    wm = 2*math.pi**((d-1)/2)/math.gamma((d-1)/2)
    left=2*wd*quad(lambda t:(t-1)**(d-1)*t**(-s),1,2,epsabs=1e-11)[0]
    right=wm/(d-1)*2**(1-s)/(1-s)*quad(lambda u:(1-u**(2/(1-s)))**((d-1)/2),0,1,epsabs=1e-11)[0]
    return left-right

rows=[]
for d in (2,3,10,100):
    b=brentq(lambda s:equation_scipy(s,d),.01,.95,xtol=1e-13)
    a=mp.findroot(lambda s:equation_mp(s,d),(mp.mpf(str(b))-.01,mp.mpf(str(b))+.01))
    row={'dimension':d,'root_beta_mpmath':str(a),'root_quadrature_scipy':b,'absolute_difference':float(abs(a-b)),'residual_beta':str(equation_mp(a,d))}
    assert abs(a-b)<mp.mpf('1e-9')
    if d==2:
        gamma_res=mp.sqrt(mp.pi)*(2**a-2*a)*mp.gamma((2-a)/2)-mp.gamma((3-a)/2)
        assert abs(gamma_res)<mp.mpf('1e-30')
        row['residual_d2_gamma_equation']=str(gamma_res)
    rows.append(row)
result={'time':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'niceness':os.getpriority(os.PRIO_PROCESS,0),'threads':1,'method':'Equation (21): beta formula vs transformed direct numerical quadrature; d=2 also gamma identity','results':rows}
assert result['niceness']>=10
Path('data/exponent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
