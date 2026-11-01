"""Deterministic checks supplement, rather than resample, the Monte Carlo run."""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr, roots_hermitenorm, expit, logsumexp

phi=lambda z: np.exp(-z*z/2)/np.sqrt(2*np.pi)
em, e1=quad(lambda z:z*6*phi(z)*ndtr(z)**5,-12,12,epsabs=1e-12)
em2,e2=quad(lambda z:z*z*6*phi(z)*ndtr(z)**5,-12,12,epsabs=1e-12)
out={'ground_n2_d3_exact_integral_variance':1+em2-em*em,
     'moment_quadrature_error_estimates':[e1,e2]}
# Condition on the five competing weights. The remaining site's occupation
# is logistic(4*x-log(sum(exp(4*others)))). Check Stein's identity directly.
others=np.random.default_rng(5119).normal(size=(30,5))
results=[]
for nodes in [256,512]:
    x,w=roots_hermitenorm(nodes)
    w=w/np.sqrt(2*np.pi)
    errors=[]
    for values in others:
        p=expit(4*x-logsumexp(4*values))
        errors.append(float(w@(x*p)-w@(4*p*(1-p))))
    results.append({'nodes':nodes,'conditioned_cases':len(others),'max_abs_stein_error':max(map(abs,errors))})
out['conditional_ibp_quadrature']=results
Path('deterministic_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
