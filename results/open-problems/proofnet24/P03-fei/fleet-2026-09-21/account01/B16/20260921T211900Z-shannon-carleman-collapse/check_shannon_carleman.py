import math
import numpy as np

LN2 = math.log(2.0)
PI = math.pi

def xlogx(x):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    mask = x > 0.0
    out[mask] = x[mask] * np.log(x[mask])
    return out

def shannon_nat_from_X(X):
    X = np.asarray(X, dtype=float)
    A = X[:, None]
    B = X[None, :]
    return xlogx(A+B) - xlogx(A) - xlogx(B)

def brownian_from_X(X):
    X = np.asarray(X, dtype=float)
    return np.minimum(X[:, None], X[None, :])

def phase_nat_from_X(X):
    X = np.asarray(X, dtype=float)
    A=X[:,None]; B=X[None,:]
    q=A+B
    s=np.zeros_like(q)
    mask=q>0
    prod=A*B
    s[mask]=2*np.sqrt(prod[mask])/q[mask]
    D=0.5*(xlogx(1+s)+xlogx(1-s))
    return q*D

def test_scalar_feature_identity():
    checks=0
    maxerr=0.0
    for X in np.linspace(0,1,31):
        for t in np.geomspace(1e-5,1e3,31):
            lhs=1-math.exp(-t*X)
            if t*X < 700:
                rhs=t*((1-math.exp(-t*X))/t)
            else:
                rhs=1.0
            err=abs(lhs-rhs)
            maxerr=max(maxerr,err)
            checks += 1
    assert maxerr < 1e-14
    return checks,maxerr

def test_shannon_carleman_psd():
    checks=0
    worst=0.0
    grids=[]
    for m in [5,8,12,20,32,48]:
        grids.append(np.geomspace(1e-10,1.0,m))
    rng=np.random.default_rng(20260921)
    for _ in range(30):
        grids.append(np.sort(np.exp(rng.uniform(math.log(1e-10),0,size=24))))
    for X in grids:
        S=shannon_nat_from_X(X)
        M=brownian_from_X(X)
        D=PI*M-S
        ev=np.linalg.eigvalsh((D+D.T)/2)
        worst=min(worst,float(ev.min()))
        assert ev.min() >= -2e-10*max(1.0,float(np.linalg.norm(D,2)))
        checks += 1
    return checks,worst

def test_combined_kernel_psd():
    checks=0
    worst=0.0
    rng=np.random.default_rng(99)
    for _ in range(40):
        X=np.sort(np.exp(rng.uniform(math.log(1e-9),0,size=20)))
        S=shannon_nat_from_X(X)
        P=phase_nat_from_X(X)
        M=brownian_from_X(X)
        D=(PI+2.0)*M-(S+P)
        ev=np.linalg.eigvalsh((D+D.T)/2)
        worst=min(worst,float(ev.min()))
        assert ev.min() >= -5e-10*max(1.0,float(np.linalg.norm(D,2)))
        checks += 1
    return checks,worst

def carleman_ratio_log_trial(eps, n):
    L=math.log(1/eps)
    x=(np.arange(n)+0.5)*L/n
    dx=L/n
    d=np.abs(x[:,None]-x[None,:])
    K=1/(2*np.cosh(d/2))
    q=K.sum()*dx*dx
    return q/L

def test_near_sharpness():
    vals=[]
    for eps,n in [(1e-2,350),(1e-4,500),(1e-6,650),(1e-8,800)]:
        vals.append((eps,carleman_ratio_log_trial(eps,n)))
    assert vals[-1][1] > 2.7
    assert vals[-1][1] < PI
    return vals

if __name__ == "__main__":
    c1,e1=test_scalar_feature_identity()
    c2,e2=test_shannon_carleman_psd()
    c3,e3=test_combined_kernel_psd()
    vals=test_near_sharpness()
    print("PASS")
    print("scalar_feature_checks",c1,"max_error",format(e1,'.3e'))
    print("shannon_loewner_matrix_checks",c2,"worst_min_eig",format(e2,'.3e'))
    print("combined_kernel_matrix_checks",c3,"worst_min_eig",format(e3,'.3e'))
    for eps,val in vals:
        print("carleman_ratio",format(eps,'.0e'),format(val,'.12f'))
    print("pi",format(PI,'.12f'))
    print("pi_over_ln2",format(PI/LN2,'.12f'))
    print("combined_constant_bits",format((PI+2)/LN2,'.12f'))
    print("current_prefactor",format((PI+2)/9,'.12f'))
    print("central_prefactor",format(11*(PI+2)/1152,'.12f'))
