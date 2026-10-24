"""Bounded finite checks of the geometric synthesis; not a proof certificate."""
from __future__ import annotations
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import quad


def no_pivot(a: np.ndarray, tau: float) -> bool:
    diagonal = np.diag(a)
    determinants = diagonal[:,None]*diagonal[None,:]-a*a
    mask = ~np.eye(len(a),dtype=bool)
    return bool(np.max(np.abs(diagonal)) < tau and np.max(np.abs(determinants[mask])) < tau)


def main() -> None:
    rng=np.random.default_rng(230923)
    assert 7.5*math.log(2.) < 5.2
    log_errors=[]
    for b in (1e-4,.1,.5,1.,2.,5.,100.,1e4):
        cutoff=max(0.,4.*math.log(b))
        exact=4.*b if b<=1 else cutoff+4.
        # Include the known branch change rather than letting quadrature miss it.
        numerical=cutoff+quad(lambda u:min(1.,b*math.exp(-u/4.)),cutoff,np.inf)[0]
        log_errors.append(abs(numerical-exact)/(1.+exact))
        assert log_errors[-1] < 1e-9
        assert exact <= 4.+4.*max(0.,math.log(b))+1e-12
    kernel_errors=[]
    for delta in (1e-4,.01,.2,1.,2.,100.):
        exact=delta**(-.5) if delta>=1 else 1.+.5*math.log(1./delta)
        split=max(1.,delta**(-.5))
        numerical=(math.log(split) if split>1 else 0.)+quad(
            lambda z: z**(-2)/math.sqrt(delta),split,np.inf)[0]
        kernel_errors.append(abs(numerical-exact))
        assert kernel_errors[-1] < 1e-8
    scalar_checks=0
    for _ in range(1000):
        a=10.**rng.uniform(-4.,4.)
        u=10.**rng.uniform(-5.,2.)
        delta=float(rng.uniform(-2.,10.)*u)
        if delta+u<=0:
            length=0.
        elif delta>u:
            length=4.*u/(math.sqrt(a)*(math.sqrt(delta+u)+math.sqrt(delta-u)))
        else:
            length=2.*math.sqrt((delta+u)/a)
        bound=4.*u/math.sqrt(a*max(abs(delta),u))
        assert length <= bound*(1.+1e-12)
        scalar_checks+=1
    padding=[]
    for tau in (1.,.1,.01):
        leaves=max(3,math.floor(2./tau)+1)
        base=np.zeros((leaves+1,leaves+1))
        base[0,1:]=1./math.sqrt(leaves)
        base[1:,0]=base[0,1:]
        assert no_pivot(base,tau)
        n=math.floor(1./tau)+1
        for sign in (-1.,1.):
            block=np.zeros((len(base)+n,len(base)+n))
            block[:len(base),:len(base)]=base
            block[len(base):,len(base):]=sign*np.ones((n,n))/n
            eig=np.linalg.eigvalsh(block)
            third=sorted(np.abs(eig),reverse=True)[2]
            assert no_pivot(block,tau)
            assert third >=1.-1e-10
            padding.append({'tau':tau,'auxiliary_count':n,'sign':int(sign),'third_abs_eigenvalue':float(third),'no_pivot':True})
    ds=np.geomspace(1e-12,1e8,500)
    bounds=(9.2+np.maximum(0.,np.log(10000.*np.sqrt(ds))))/np.sqrt(ds)
    assert np.all(np.diff(bounds)<0)
    threshold=3501./64000.
    pair_bound=(9.2+math.log(10000.*math.sqrt(threshold)))/math.sqrt(threshold)
    assert pair_bound<73.
    l0=4.+4.*math.log(5.)
    for tau in np.geomspace(1e-9,1.,100):
        k=2./math.sqrt(tau)*(6.2+max(0.,math.log(16.*math.sqrt(tau))))
        assert 4./math.sqrt(tau)*(1.+.5*l0)<3.*k
        pair=(9.2+max(0.,math.log(10000.*math.sqrt(tau))))/math.sqrt(tau)
        assert pair<(1.+3.*k)/math.sqrt(tau)
    result={
        'status':'PASS',
        'scope':'Finite constants, integrals and class-preservation checks; remaining no-pivot theorem is not proved.',
        'hyperbolic_constant':7.5*math.log(2.),
        'logarithmic_potential_bound':l0,
        'max_log_integral_relative_error':max(log_errors),
        'max_scalar_kernel_integral_error':max(kernel_errors),
        'scalar_sublevel_length_checks':scalar_checks,
        'padding_checks':padding,
        'determinant_bound_monotonicity_grid':len(ds),
        'two_pivot_threshold':threshold,
        'two_pivot_density_bound':pair_bound,
        'reduction_constant_checks':100,
        'full_conjecture_verified':False,
        'no_pivot_hypothesis_proved':False,
        'independent_review_completed':False,
    }
    text=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_name('geometric_check_results.json').write_text(text,encoding='utf-8')
    print(text)


if __name__=='__main__':
    main()
