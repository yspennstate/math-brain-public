"""Reproducible D0036 finite-window evidence; one thread, inherited nice >=10.

Small-window maxima exhaust every support S, using maximal allowed T by
monotonicity of canonical correlation. Larger windows use specified support
families only and are LOWER BOUNDS, not estimates with certified error bars.
All covariances used in the computations are analytic, with no FFT aliasing.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import csv
import json
import math
from pathlib import Path
import platform
import resource
import time
import numpy as np
from scipy import integrate, linalg
import scipy

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT/'data'
START = time.time()
assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
A = .7

def covariance(name, h):
    h = np.asarray(h, dtype=int)
    x = np.abs(h)
    if name == 'white': return (x == 0).astype(float)
    if name == 'ar07': return A**x
    if name == 'difference': return 2.*(x == 0)-1.*(x == 1)
    if name == 'difference_ar07':
        return 2*A**x-A**np.abs(h-1)-A**np.abs(h+1)
    if name == 'second_difference':
        return 6.*(x == 0)-4.*(x == 1)+1.*(x == 2)
    if name == 'cusp': return 1./(1.-4.*x*x)
    if name == 'step':
        out = np.zeros(h.shape)
        nz = x != 0
        out[nz] = 1.2/np.pi*np.sin(np.pi*x[nz]/2)/x[nz]
        out[x == 0] = 1.
        return out
    if name == 'white_plus_atom': return 1.+1.*(x == 0)
    raise ValueError(name)

MODELS = ['white','ar07','difference','difference_ar07',
          'second_difference','cusp','step','white_plus_atom']

def density(name, theta):
    z = np.exp(1j*theta)
    g = (1-A*A)/abs(1-A*z)**2
    return {'white': 1., 'ar07': g, 'difference': abs(1-z)**2,
            'difference_ar07': abs(1-z)**2*g,
            'second_difference': abs(1-z)**4,
            'cusp': np.pi/4*abs(1-z),
            'step': 1.+.6*np.sign(np.cos(theta))}[name]

def cca_matrix(G, S, T):
    S,T = np.asarray(S,int),np.asarray(T,int)
    assert len(S) and len(T)
    Css,Ctt,Cst = G[np.ix_(S,S)],G[np.ix_(T,T)],G[np.ix_(S,T)]
    Ls = linalg.cholesky(Css,lower=True,check_finite=False)
    Lt = linalg.cholesky(Ctt,lower=True,check_finite=False)
    C = linalg.solve_triangular(Ls,Cst,lower=True,check_finite=False)
    C = linalg.solve_triangular(Lt,C.T,lower=True,check_finite=False).T
    r = float(linalg.svdvals(C,check_finite=False)[0])
    assert -.0000001 <= r <= 1.0000001, r
    return r

def gram(name, W):
    ii = np.arange(W)
    return covariance(name,ii[:,None]-ii[None,:])

def exact_supports(W,n):
    """Every nonempty S; T is every index at allowed distance from S."""
    pairs = set()
    full = (1<<W)-1
    for mask in range(1,full):
        forbidden = mask
        for shift in range(1,n):
            forbidden |= (mask<<shift)|(mask>>shift)
        tmask = full & ~forbidden
        if not tmask: continue
        pair = tuple(sorted((mask,tmask)))
        pairs.add(pair)
    for sm,tm in sorted(pairs):
        S = np.array([i for i in range(W) if sm>>i&1])
        T = np.array([i for i in range(W) if tm>>i&1])
        assert np.min(abs(S[:,None]-T[None,:])) >= n
        yield S,T

def sampled_supports(W,n):
    """Two ordered blocks, regular sparse alternating sets, and alternating runs."""
    L = (W-n+1)//2
    if L>0:
        yield 'two_blocks',np.arange(L),np.arange(L+n-1,2*L+n-1)
    for b in sorted(set([1,2,4,8,16,32,64,128])):
        selected = [(k,k+b) for k in range(0,W-b+1,b+n-1)]
        if len(selected)<2: continue
        S = np.concatenate([np.arange(a,c) for a,c in selected[::2]])
        T = np.concatenate([np.arange(a,c) for a,c in selected[1::2]])
        if len(S) and len(T):
            assert np.min(abs(S[:,None]-T[None,:])) >= n
            yield 'alternating_runs_'+str(b),S,T

def write_csv(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)

checks=[]
# Independent quadrature of Fourier coefficients, including oscillatory tails.
for name in MODELS[:-1]:
    for k in (0,1,2,3,10,31):
        val,err=integrate.quad(lambda t: density(name,t)*math.cos(k*t)/np.pi,
                               0,np.pi,points=[np.pi/2],epsabs=2e-11,limit=160)
        exact=float(covariance(name,k))
        checks.append({'kind':'fourier_quadrature','model':name,'k':k,
                       'absolute_error':abs(val-exact),'quadrature_error':err})
        assert abs(val-exact)<2e-10,(name,k,val,exact)

small=[]
W=12
for n in (1,2,3,4,6):
    supports=list(exact_supports(W,n))
    for name in MODELS:
        G=gram(name,W)
        vals=[cca_matrix(G,S,T) for S,T in supports]
        idx=int(np.argmax(vals));S,T=supports[idx]
        small.append({'model':name,'window':W,'gap':n,'maximum':vals[idx],
                      'pairs_evaluated':len(supports),
                      'S':' '.join(map(str,S)),'T':' '.join(map(str,T))})
write_csv(DATA/'exhaustive_window12.csv',small)
print('Exact window 12 finished',flush=True)

sampled=[]
for W in (64,128,256,512):
    for n in (1,2,4,8,16,32,64):
        if n>=W: continue
        supports=list(sampled_supports(W,n))
        for name in MODELS:
            G=gram(name,W)
            for label,S,T in supports:
                r=cca_matrix(G,S,T)
                sampled.append({'model':name,'window':W,'gap':n,
                                'family':label,'size_S':len(S),'size_T':len(T),
                                'correlation':r})
write_csv(DATA/'sampled_correlations.csv',sampled)
print('Sampled windows through 512 finished',flush=True)

# Exact cusp block identities independently checked by covariance summation.
def V(L):
    j=np.arange(1,L+1,dtype=float)
    return float(np.sum(1/(2*j-1)))

def cusp_block_cov(L,n):
    # k = t-s, multiplicity L-|k-(L+n-1)|, with k=n,...,2L+n-2.
    # These are all negative cross covariances: no cancellation.
    k=np.arange(n,2*L+n-1,dtype=np.int64)
    multiplicity=L-np.abs(k-(L+n-1))
    return float(np.sum(multiplicity/(1.-4.*k*k)))

blocks=[]
for L in (16,64,256,1024,4096,16384,65536,262144):
    for n in (1,2,8,32,128):
        cc=cusp_block_cov(L,n)/V(L)
        blocks.append({'model':'cusp','block_length':L,'gap':n,
                       'signed_correlation':cc,'absolute_correlation':abs(cc),
                       'variance':V(L),'limiting_absolute_correlation':.5})
        if n==1:
            assert abs(cc-(V(2*L)-2*V(L))/(2*V(L)))<3e-12
for L in (1,2,5,16,64,256):
    h=np.arange(L)
    direct=float(np.sum(covariance('cusp',h[:,None]-h[None,:])))
    assert abs(direct-V(L))<2e-11
write_csv(DATA/'cusp_block_sums.csv',blocks)

# Cross-check whitening with a generalized symmetric eigenvalue problem.
for name in MODELS:
    G=gram(name,24);S=np.arange(0,24,2);T=np.arange(1,24,2)
    Css,Ctt,Cst=G[np.ix_(S,S)],G[np.ix_(T,T)],G[np.ix_(S,T)]
    M=np.einsum('ik,kj->ij',Cst,linalg.solve(Ctt,Cst.T,assume_a='pos'),optimize=False)
    assert np.isfinite(M).all()
    r2=float(linalg.eigvalsh(M,Css)[-1])
    r=cca_matrix(G,S,T)
    assert abs(r*r-r2)<2e-10,(name,r,r2)
    checks.append({'kind':'generalized_eigenvalue','model':name,'k':24,
                   'absolute_error':abs(r*r-r2),'quadrature_error':0.})

for W in (12,64,128,256,512):
    G=gram('difference',W)
    val=cca_matrix(G,np.arange(0,W,2),np.arange(1,W,2))
    err=abs(val-math.cos(math.pi/(W+1)))
    assert err<2e-12
    checks.append({'kind':'difference_checkerboard','model':'difference','k':W,
                   'absolute_error':err,'quadrature_error':0.})

for n in (1,8,32):
    L=100;W=2*L+n-1;G=gram('white_plus_atom',W)
    val=cca_matrix(G,np.arange(L),np.arange(L+n-1,2*L+n-1))
    err=abs(val-L/(1+L))
    assert err<2e-12
    checks.append({'kind':'atom_block_formula','model':'white_plus_atom','k':n,
                   'absolute_error':err,'quadrature_error':0.})
write_csv(DATA/'validation.csv',checks)
meta={'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
      'nice':os.getpriority(os.PRIO_PROCESS,0),'threads':1,
      'elapsed_seconds':time.time()-START,
      'peak_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
      'window12_support_maximum_is_exhaustive':True,
      'large_windows_are_sampled_lower_bounds':True,
      'maximum_absolute_validation_error':max(x['absolute_error'] for x in checks)}
(DATA/'run_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2),flush=True)
