"""Independent numerical reproduction. Run with single-thread BLAS settings."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import time, json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
import mpmath as mp

START = time.monotonic()
LIMIT = 230
RNG = np.random.default_rng(20261111)

def normal(v):
    v = np.asarray(v, float)
    v = v-v.mean()
    return v / np.linalg.norm(v)

def quantities(x):
    n=len(x); q=sum(x**4); p=sum(x**3)
    m=max(x[i]*x[j] for i in range(n) for j in range(i))
    S=max(abs(x))
    if max(x) < S-1e-14: x=-x; p=-p
    K=n*n-6*n+6+2*n*q; D=q-1/n-p*p
    A=n*(n-1)*S*S-1
    M=(1-q+2*S*p-S*S)/A
    N=n*(n-1)*(1-q+2*S*p-2*S*S)+1
    psi=(n-4)*(2*q-1)-2*(n-3)*p*p+(n-1)*K*m
    return dict(q=float(q),p3=float(p),m=float(m),S=float(S),K=float(K),D=float(D),M=float(M),
                psi=float(psi),split=float(K*((n-1)*m-1/n)+2*(n-3)*D),
                phi=float(K*N+2*n*(n-3)*A*D), A=float(A))

def obj(z):
    x=z[:-1]; n=len(x); q=sum(x**4); p=sum(x**3); m=z[-1]
    return (n-4)*(2*q-1)-2*(n-3)*p*p+(n-1)*(n*n-6*n+6+2*n*q)*m

def jac(z):
    x=z[:-1]; n=len(x); p=sum(x**3); q=sum(x**4); m=z[-1]
    return np.r_[(8*(n-4)+8*n*(n-1)*m)*x**3-12*(n-3)*p*x*x,
                 (n-1)*(n*n-6*n+6+2*n*q)]

def constraints(n):
    pairs=[(i,j) for i in range(n) for j in range(i)]
    def eq(z): return np.array([sum(z[:-1]),sum(z[:-1]**2)-1])
    def eqjac(z): return np.array([np.r_[np.ones(n),0], np.r_[2*z[:-1],0]])
    def ine(z): return np.array([z[-1]-z[i]*z[j] for i,j in pairs])
    def injac(z):
        J=np.zeros((len(pairs),n+1)); J[:,-1]=1
        for k,(i,j) in enumerate(pairs): J[k,i]=-z[j]; J[k,j]=-z[i]
        return J
    return [{'type':'eq','fun':eq,'jac':eqjac},{'type':'ineq','fun':ine,'jac':injac}]

def high_precision(x):
    mp.mp.dps=65
    v=[mp.mpf(float(t)) for t in x]; mu=sum(v)/len(v); v=[t-mu for t in v]
    r=mp.sqrt(sum(t*t for t in v)); v=[t/r for t in v]; n=len(v)
    q=sum(t**4 for t in v); p=sum(t**3 for t in v)
    m=max(v[i]*v[j] for i in range(n) for j in range(i))
    psi=(n-4)*(2*q-1)-2*(n-3)*p*p+(n-1)*(n*n-6*n+6+2*n*q)*m
    return {'x':[str(t) for t in v],'psi':str(psi)}

def log(s):
    print(s,flush=True)
    with open('LOG.md','a') as f: f.write('\n'+s+'\n')

def main():
    log('## 2. NUMERICAL reproduction (reproduce.py)')
    worst_id=0.; worst_bound=float('inf'); worst_phi=float('inf')
    for n in range(5,10):
        star=normal([n-1]+[-1]*(n-1)); edge=normal([1,-1]+[0]*(n-2))
        print(json.dumps({'n':n,'star':quantities(star),'edge':quantities(edge)}),flush=True)
        for _ in range(300):
            x=normal(RNG.normal(size=n)); a=quantities(x)
            worst_id=max(worst_id,abs(a['psi']-a['split']))
            worst_bound=min(worst_bound,a['m']-a['M'])
            worst_phi=min(worst_phi,n*a['A']*a['psi']-a['phi'])
    log(f'NUMERICAL: 1500 random tests: maximum split error {worst_id:.3g}; minimum m-M {worst_bound:.3g}; minimum n*A*Psi-Phi {worst_phi:.3g}. The two specified vectors have Psi and m-M zero to floating-point rounding (details in reproduce.out).')
    with open('minimizations_scaled.jsonl','w') as out:
      for n in range(5,10):
        starts=[]
        for _ in range(44): starts.append(('random',normal(RNG.normal(size=n))))
        for k in range(2,n):
            for _ in range(3):
                v=np.zeros(n); v[:k]=RNG.normal(size=k); v[:k]-=v[:k].mean()
                starts.append(('zeros',normal(v)))
        for _ in range(14):
            v=RNG.normal(size=n)*10**RNG.uniform(-6,-1)
            v[0]+=1;v[1]-=1; starts.append(('edge-near',normal(v)))
        for _ in range(14):
            counts=RNG.multinomial(n-3,[1/3]*3)+1
            v=np.repeat(RNG.normal(size=3),counts); starts.append(('three-values',normal(v)))
        for _ in range(6):
            starts.append(('star-near',normal(np.r_[n-1,-np.ones(n-1)]+RNG.normal(size=n)*10**RNG.uniform(-6,-1))))
        best=1e100; bestx=None; counts={}; iterations=0; success=0
        for kind,x in starts:
            if time.monotonic()-START>LIMIT: log('NUMERICAL: internal runtime limit reached; remaining starts omitted.'); break
            m=quantities(x)['m']
            scale=(n-1)*(n*n-6*n+6+2*n)
            res=minimize(lambda v:obj(v)/scale,np.r_[x,m],jac=lambda v:jac(v)/scale,constraints=constraints(n),method='SLSQP',
                         bounds=[(-1,1)]*n+[(0,.5)],
                         options={'maxiter':220,'ftol':2e-14})
            v=normal(res.x[:-1]); a=quantities(v)
            row={'n':n,'kind':kind,'success':bool(res.success),'iterations':res.nit,'psi':a['psi'],'x':v.tolist(),
                 'sum_residual':float(sum(v)),'norm_residual':float(sum(v*v)-1)}
            out.write(json.dumps(row)+'\n');out.flush()
            counts[kind]=counts.get(kind,0)+1;iterations+=res.nit;success+=int(res.success)
            if a['psi']<best:best=a['psi'];bestx=v
            if best < -1e-9:
                candidate=high_precision(bestx)
                Path('counterexample_candidate.json').write_text(json.dumps(candidate,indent=2))
                log('NUMERICAL negative candidate: '+json.dumps(candidate))
                if mp.mpf(candidate['psi']) < -mp.mpf('1e-9'): return
        log(f'NUMERICAL n={n}: {sum(counts.values())} starts {counts}, optimizer success {success}; minimum recomputed feasible Psi={best:.17g}; iterations={iterations}.')
        print('best 65-digit re-evaluation',n,json.dumps(high_precision(bestx)),flush=True)
    log(f'NUMERICAL reproduction ended after {time.monotonic()-START:.1f} seconds. No verified counterexample found.')

if __name__=='__main__': main()
