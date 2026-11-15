"""Independent covariance, normalization, precision, and asymptotic checks."""
import json
from pathlib import Path
from dgff import sample, diagonal, G, check_resources, peak_bytes
import numpy as np
from scipy.linalg import eigh
from scipy.integrate import quad, dblquad

root = Path(__file__).resolve().parents[1]
rng = np.random.default_rng(20261113)
out = dict(resources=check_resources(16), checks=[])
for N in [4, 7, 12]:
    n = N-1
    T = np.diag(np.full(n, 2.)) - np.diag(np.ones(n-1), 1)-np.diag(np.ones(n-1), -1)
    Q = (np.kron(np.eye(n), T)+np.kron(T, np.eye(n)))/4
    exact = np.linalg.inv(Q)
    # Deterministic transform matrix, not a Monte Carlo covariance estimate.
    cols = []
    for i in range(n*n):
        e = np.zeros((n,n)); e.flat[i]=1
        cols.append(sample(N, rng, coefficients=e).ravel())
    B = np.array(cols).T
    err = float(np.max(np.abs(np.einsum('ik,jk->ij',B,B)-exact)))
    vd = np.vstack([v for _,v in diagonal(N)]).ravel()
    derr = float(np.max(np.abs(vd-exact.diagonal())))
    assert err < 1e-12 and derr < 1e-12
    out['checks'].append(dict(N=N, covariance_max_error=err,
                               diagonal_max_error=derr))
N=128
co = rng.standard_normal((N-1,N-1))
h64=sample(N,rng,coefficients=co)
h32=sample(N,rng,np.float32,coefficients=co)
out['float32'] = dict(N=N, max_error=float(np.max(abs(h64-h32))),
                      rms_error=float(np.mean((h64-h32)**2)**.5))
# Check the saddle expansion against direct Gaussian density integrals, for a
# nontrivial covariance and several increasing t. No DGFF code is used here.
beta=.8; q=-.7; r=.3; c=1.2
rows=[]
for t in [50,100,200,400]:
    sig=np.array([[t+q,c],[c,t+r]])
    inv=np.linalg.inv(sig)
    Raa=(t/np.sqrt(np.linalg.det(sig)))*dblquad(
        lambda z,s: beta**2*np.exp(-beta*(s+z)-.5*(np.array([s-beta*(q+c),z-beta*(r+c)])@inv@np.array([s-beta*(q+c),z-beta*(r+c)]))),
        0,np.inf,lambda s:0,lambda s:np.inf,epsabs=1e-11,epsrel=1e-10)[0]
    def mixed(z):
        return np.sqrt(t/(t+z))*quad(lambda s:beta*np.exp(-beta*s-(s-beta*(z+c))**2/(2*(t+z))),0,np.inf,epsabs=1e-12)[0]
    diff=Raa-mixed(q)-mixed(r)+1
    rows.append(dict(t=t, cancelled_kernel=diff, t2_kernel=t*t*diff))
assert max(abs(x['t2_kernel']) for x in rows)<100
assert abs(rows[-1]['cancelled_kernel']) < abs(rows[0]['cancelled_kernel'])/30
out['gaussian_cancellation']=rows
out['peak_bytes']=peak_bytes()
(root/'data'/'validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
