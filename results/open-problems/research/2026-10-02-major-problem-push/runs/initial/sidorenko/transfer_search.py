"""Numerical exploration, not a proof: Sidorenko for the ten-vertex Mobius ladder.

The matrix identity is checked independently against direct enumeration below.
All experiments use a deterministic seed and preserve the best host matrix.
"""
import argparse
import itertools
import json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize


def transfer(W):
    n = len(W)
    root = np.sqrt(W)
    M = (root[:, :, None, None] * root[None, None, :, :]
         * W[:, None, None, :] * W[None, :, :, None])
    return M.reshape(n*n, n*n)


def regularize(W):
    n = len(W)
    scale = np.ones(n)
    for _ in range(1000):
        rows = scale*(W@scale)
        if np.max(np.abs(rows/n-1)) < 1e-12:
            break
        scale *= np.sqrt(n/rows)
    return scale[:,None]*W*scale[None,:]


def matrix_gradient(W, M, L):
    n = len(W)
    root = np.sqrt(W)
    root_part = np.sum(L*M, axis=1).reshape(n,n)/W
    T = L.reshape(n,n,n,n)
    cross1 = np.einsum('ijkl,ij,kl,kj->il', T, root, root, W)
    cross2 = np.einsum('ijkl,ij,kl,il->kj', T, root, root, W)
    return root_part + cross1 + cross2


def objective(z, n, target='sidorenko'):
    upper = np.triu_indices(n)
    W = np.empty((n,n))
    W[upper] = np.exp(z)
    W[(upper[1], upper[0])] = W[upper]
    regular = target.startswith('regular_')
    if regular:
        W = regularize(W)
        target = target.removeprefix('regular_')
    M = transfer(W)
    M2 = M @ M
    M4 = M2 @ M2
    F = np.sum(M4*M)
    if target == 'spectral5':
        lam, U = np.linalg.eigh(M)
        v = U[:, -1]
        val = np.log(F)-5*np.log(lam[-1])
        L = 5*M4/F - 5*np.outer(v,v)/lam[-1]
        gradW = matrix_gradient(W,M,L)
    else:
        p = W.mean()
        val = np.log(F)-15*np.log(p)-10*np.log(n)
        L = 5*M4/F
        gradW = matrix_gradient(W,M,L)-15/(n*n*p)
    if regular:
        gradW=(gradW+gradW.T)/2
        h=2*np.sum(gradW*W,axis=1)
        k=np.linalg.solve(n*np.eye(n)+W,h)
        gradW -= (k[:,None]+k[None,:])/2
    G = gradW*W
    g = G[upper].copy()
    mask = upper[0] != upper[1]
    g[mask] += G[(upper[1][mask],upper[0][mask])]
    return val,g


def direct(W):
    """Integrate one color class first; O(n^5), distinct from transfer."""
    n=len(W)
    A=np.einsum('ai,bi,ci->abc',W,W,W)/n
    result=0
    for x in itertools.product(range(n), repeat=5):
        result += np.prod([A[x[i],x[(i+1)%5],x[(i+2)%5]] for i in range(5)])
    return result/n**5


def verify():
    rng=np.random.default_rng(39891)
    for n in [2,3,4]:
        W=np.exp(rng.normal(size=(n,n)))
        W=(W+W.T)/2
        M=transfer(W)
        got=np.trace(np.linalg.matrix_power(M,5))/n**10
        want=direct(W)
        assert np.allclose(got,want,rtol=1e-11,atol=1e-12),(n,got,want)
        z=np.log(W[np.triu_indices(n)])
        for target in ['sidorenko','spectral5','regular_sidorenko','regular_spectral5']:
            value,grad=objective(z,n,target)
            for k in range(len(z)):
                dz=np.zeros_like(z);dz[k]=1e-5
                fd=(objective(z+dz,n,target)[0]-objective(z-dz,n,target)[0])/2e-5
                assert abs(fd-grad[k])<1e-6,(n,target,k,fd,grad[k])
    print('Transfer/direct identity and analytic gradients verified',flush=True)


def main():
    p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=5)
    p.add_argument('--runs',type=int,default=50)
    p.add_argument('--target',default='sidorenko')
    p.add_argument('--seed',type=int,default=39891)
    p.add_argument('--output',default='transfer_search_result.json')
    args=p.parse_args();verify();rng=np.random.default_rng(args.seed)
    best=None;records=[]
    for r in range(args.runs):
        sigma=[.3,1,2,4,8][r%5]
        z=rng.normal(0,sigma,args.n*(args.n+1)//2)
        out=minimize(objective,z,args=(args.n,args.target),jac=True,
                     method='L-BFGS-B',bounds=[(-15,15)]*len(z),
                     options={'maxiter':400,'ftol':1e-13,'gtol':1e-9})
        record={'run':r,'initial_sigma':sigma,'value':float(out.fun),
                'iterations':out.nit,'success':bool(out.success)}
        records.append(record)
        if best is None or out.fun<best['value']:
            upper=np.triu_indices(args.n);W=np.empty((args.n,args.n))
            W[upper]=np.exp(out.x);W[(upper[1],upper[0])]=W[upper]
            if args.target.startswith('regular_'):
                W = regularize(W)
            best=record|{'matrix_normalized_mean_one':(W/W.mean()).tolist()}
        Path(args.output).write_text(json.dumps({'args':vars(args),
                                                'best':best,'records':records},indent=2))
        print(r,record['value'],out.nit,out.success,flush=True)


if __name__=='__main__':main()
