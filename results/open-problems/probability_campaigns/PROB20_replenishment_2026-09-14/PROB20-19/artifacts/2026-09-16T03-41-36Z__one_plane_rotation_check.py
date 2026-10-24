import math
import numpy as np

L = math.pi/2

def H(u, s, tau):
    return np.maximum(0.5*s*(1.0 + np.abs(np.cos(2.0*u))) - tau, 0.0)

def conv_value(kappa, s, tau, theta, n=32768):
    u = (np.arange(n) + 0.5) * (L/n)
    G = np.cosh(kappa*np.cos(2.0*u))
    return L*np.mean(G * H(u-theta, s, tau))

def check_conditional_convolution():
    worst = -1e100
    worst_case = None
    total = 0
    for kappa in [0.0, 0.03, 0.2, 0.8, 2.5, 7.0]:
        for s in [0.2, 1.0, 5.0]:
            for frac in [-0.3, 0.2, 0.55, 0.8, 0.98, 1.2]:
                tau = frac*s
                base = conv_value(kappa,s,tau,0.0)
                for theta in np.linspace(0.0,L,33):
                    val = conv_value(kappa,s,tau,float(theta))
                    diff = val-base
                    if diff > worst:
                        worst = diff
                        worst_case=(kappa,s,tau,float(theta),base,val)
                    assert diff <= 2e-9*max(1.0,abs(base)), (diff,worst_case)
                    total += 1
    return total,worst,worst_case

def topd_energy(sq,d):
    return np.partition(sq, -d, axis=1)[:,-d:].sum(axis=1)

def check_full_objective_mc():
    rng=np.random.default_rng(20260916)
    cases=[([4.0,1.0,0.5,0.2],0,1),([5.0,2.0,1.1,0.4,0.1],0,1),([3.0,1.7,0.8,0.3,0.09],1,3),([2.0,1.2,0.6,0.25],0,2)]
    records=[]
    N=120000
    for lam,i,j in cases:
        lam=np.asarray(lam,float)
        Z=rng.standard_normal((N,len(lam)))
        X=Z*np.sqrt(lam)
        base_sq=X*X
        for d in range(1,len(lam)):
            base=topd_energy(base_sq,d)
            for theta in [0.08,0.2,0.45,math.pi/4]:
                Y=X.copy(); c,s=math.cos(theta),math.sin(theta)
                xi=X[:,i].copy(); xj=X[:,j].copy()
                Y[:,i]=c*xi+s*xj; Y[:,j]=-s*xi+c*xj
                val=topd_energy(Y*Y,d)
                delta=val-base
                mean=float(delta.mean()); se=float(delta.std(ddof=1)/math.sqrt(N))
                assert mean <= 6.0*se + 2e-4, (lam.tolist(),i,j,d,theta,mean,se)
                records.append((lam.tolist(),i,j,d,theta,mean,se))
    return records

def check_zero_variance_pointwise():
    rng=np.random.default_rng(7); N=30000; p=6
    svals=rng.exponential(size=N); others=rng.exponential(size=(N,p-2))
    max_violation=0.0; checks=0
    for theta in np.linspace(0,L,17):
        x=svals*np.cos(theta)**2; y=svals*np.sin(theta)**2
        base=np.concatenate([svals[:,None],np.zeros((N,1)),others],axis=1)
        rot=np.concatenate([x[:,None],y[:,None],others],axis=1)
        for d in range(1,p):
            b=topd_energy(base,d); v=topd_energy(rot,d)
            max_violation=max(max_violation,float(np.max(v-b)))
            assert np.all(v <= b + 1e-12)
            checks += N
    return checks,max_violation

if __name__ == '__main__':
    total,worst,wcase=check_conditional_convolution()
    print('conditional convolution checks:',total)
    print('worst numerical shifted-minus-aligned value:',repr(worst))
    print('worst case:',wcase)
    rec=check_full_objective_mc()
    print('paired Monte Carlo cases:',len(rec))
    print('largest z = mean/se among rotated-minus-KL differences:',max(m/s for *_,m,s in rec if s>0))
    print('smallest z:',min(m/s for *_,m,s in rec if s>0))
    checks,mv=check_zero_variance_pointwise()
    print('zero-variance pointwise scalar comparisons:',checks)
    print('zero-variance max violation:',mv)
    print('ALL CHECKS PASSED')
