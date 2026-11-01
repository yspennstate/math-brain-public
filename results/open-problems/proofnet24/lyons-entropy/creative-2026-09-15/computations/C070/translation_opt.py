exec(open('computations/C070/translation_explore.py').read().split('for n in range')[0])
from scipy.optimize import minimize
for n in [3,4,5]:
    best=1e99
    for k in range(20):
        z=rng.normal(size=2**n)*rng.uniform(.3,3)
        def fun(v):
            p=np.exp(v-v.max());p/=p.sum()
            return np.linalg.eigvalsh(trans_hess(p,n))[0]
        res=minimize(fun,z,method='L-BFGS-B',options={'maxiter':150,'ftol':1e-10})
        if res.fun<best:
            best=res.fun;print(n,k,best,flush=True)
        if best<0:
            p=np.exp(res.x-res.x.max());p/=p.sum();print(p,flush=True);break
