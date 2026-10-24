from pathlib import Path
import json, math
import numpy as np
from scipy.optimize import root, brentq
from scipy.special import roots_hermitenorm
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parent
components=[(2/3,-1,.5),(1/3,2,1)]
v=2.5; c3=3.5; c5=44.375
records=[]
for t in [1000.,10000.,100000.]:
    def ch(h):
        return sum(w*(a-h)/(t+sd*sd)**1.5*math.exp(-(h-a)**2/(2*(t+sd*sd))) for w,a,sd in components)
    h=brentq(ch,-1,1,xtol=1e-15)
    results=[]
    for n in [100,200]:
        nodes,weights=roots_hermitenorm(n); weights/=math.sqrt(2*math.pi)
        ys=np.concatenate([a+sd*nodes for w,a,sd in components])
        ws=np.concatenate([w*weights for w,a,sd in components])
        def equations(z):
            u,r=z; q=u-ys; den=r+q*q/t
            return [np.dot(ws,1/den)-1,np.dot(ws,q/den**2)]
        sol=root(equations,[-2*c3/t,1-v/t],tol=1e-11)
        assert np.max(np.abs(equations(sol.x)))<1e-12
        u,r=sol.x; physical=u+np.dot(ws,(u-ys)/(r+(u-ys)**2/t))
        results.append(float(physical))
    assert abs(results[0]-results[1])<1e-12
    # Independently check the Hermite expectation with integration on the real line.
    def E(f):
        return sum(w*quad(lambda y:math.exp(-((y-a)/sd)**2/2)/(sd*math.sqrt(2*math.pi))*f(y),-np.inf,np.inf,epsabs=1e-12)[0] for w,a,sd in components)
    residual=max(abs(E(lambda y:1/(r+(u-y)**2/t))-1),abs(E(lambda y:(u-y)/(r+(u-y)**2/t)**2)))
    assert residual<1e-11
    row={'t':t,'classical':h,'free':results[1],'t3_classical_error':t**3*(h-(-c3/(2*t)+(c5-6*v*c3)/(8*t*t))), 't3_free_error':t**3*(results[1]-(-3*c3/t+(5*c5-22*v*c3)/(t*t))), 'quadrature_residual':residual,'Hermite_difference':abs(results[0]-results[1])}
    records.append(row); print(row,flush=True)
(ROOT/'unbounded_results.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print('Unbounded Gaussian-mixture verification PASS',flush=True)
