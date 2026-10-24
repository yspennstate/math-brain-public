"""Exact symbolic identities and polynomial-convention optimizers after Lean admission failed."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json
import math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
out={'command':'python -X utf8 check_algebra.py','lean_status':'UNAVAILABLE_COMPUTE_ADMISSION; no Lean claim'}
try:
    import sympy as s
    a,b,l,m,t,p=s.symbols('a b l m t p')
    atom=s.expand((a*b)*((1-a)*(1-b))-(a*(1-b))*((1-a)*b))
    cycle=m/(l*(m-l))*(1+l*t*p)
    area=m/(m-l)**2*(1+m*t*p+l*(m-l)*t**2*p/2)
    wait=l/(m*(m-l))+t*(1+l*t/2)*p/(1+l*t*p)
    difference=s.factor(s.together(area/cycle/l-1/m-wait))
    busy=s.factor(s.together(((1+l*t*p)/(m-l))/cycle-l/m))
    assert atom==0 and difference==0 and busy==0
    out['symbolic_checks']={'tool':'SymPy','atom_product_difference':str(atom),'queue_wait_difference':str(difference),'busy_fraction_difference':str(busy),'conditions':['lambda != 0','mu != 0','mu-lambda != 0','1+lambda*tau*p != 0']}
except ModuleNotFoundError:
    out['symbolic_checks']={'tool':'unavailable','status':'SymPy not installed; handwritten algebra proof retained'}

rng=np.random.default_rng(34010012)
errors=[]
for r in [2,3,4]:
    for p in [2.,3.,4.,5.,6.,8.,12.,math.inf]:
        for trial in range(30):
            a=rng.normal(size=7)
            if p<=r:
                expected=float(np.max(abs(a)))
                x=np.zeros(7)
                j=int(np.argmax(abs(a)))
                x[j]=1.
            else:
                q=1. if math.isinf(p) else p/(p-r)
                if r%2:
                    chosen=abs(a)
                    expected=float(np.linalg.norm(a,ord=q))
                else:
                    pos=np.maximum(a,0.)
                    neg=np.maximum(-a,0.)
                    pn=float(np.linalg.norm(pos,ord=q))
                    nn=float(np.linalg.norm(neg,ord=q))
                    chosen=pos if pn>=nn else neg
                    expected=max(pn,nn)
                if math.isinf(p):
                    x=(chosen>0).astype(float)
                else:
                    x=chosen**(1/(p-r))
                    x=x/np.linalg.norm(x,ord=p)
                if r%2: x=x*np.sign(a)
            achieved=float(abs(np.sum(a*x**r)))
            errors.append(abs(achieved-expected))
            assert abs(achieved-expected)<1e-10
            if p>r:
                q=1. if math.isinf(p) else p/(p-r)
                multilinear=float(np.linalg.norm(a,ord=q))
                assert expected<=multilinear+1e-12 and multilinear<=2**(1/q)*expected+1e-12
out['polynomial_convention']={'optimizer_checks':len(errors),'max_error':max(errors),'odd_and_even_degrees':True,'mixed_sign_cases':True,'norm_comparison_factor':'at most 2^(1/q) <= 2'}
(ROOT/'algebra_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
