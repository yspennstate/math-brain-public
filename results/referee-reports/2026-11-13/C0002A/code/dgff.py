"""Dirichlet DGFF with covariance (I-P)^{-1}, sampled with sine transforms.

N is the boundary-to-boundary side length; there are (N-1)^2 random sites.
Only one FFT worker is used. Large arrays are not retained between samples.
"""
import os
for _var in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS']:
    os.environ[_var] = '1'
import ctypes
import resource
import numpy as np
from scipy.fft import dstn, dctn

G = 2 / np.pi
CAP = 4_000_000_000

def check_resources(N, dtype=np.float64):
    # Conservative preflight: three full grids and 200 MB of small workspaces.
    need = 3 * (N-1)**2 * np.dtype(dtype).itemsize + 200_000_000
    if need >= CAP:
        raise MemoryError(f'preflight {need} bytes >= {CAP}')
    lib = ctypes.CDLL(None, use_errno=True)
    ctypes.set_errno(0)
    priority = lib.getpriority(0, 0)
    if ctypes.get_errno():
        raise OSError('could not read process priority')
    if priority < 10:
        if lib.setpriority(0, 0, 10) != 0:
            raise PermissionError('cannot ensure nice >=10')
    return dict(nice=lib.getpriority(0, 0), threads=1,
                preflight_bytes=need, cap_bytes=CAP)

def peak_bytes():
    # On macOS ru_maxrss is bytes; on Linux it is KiB.
    import sys
    v = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(v if sys.platform == 'darwin' else 1024*v)

def eigen_1d(N, dtype=np.float64):
    k = np.arange(1, N, dtype=np.float64)
    # I-P eigenvalue = sin^2(pi*k/(2N)) + sin^2(pi*l/(2N)).
    return (np.sin(np.pi*k/(2*N))**2).astype(dtype)

def sample(N, rng, dtype=np.float64, coefficients=None):
    check_resources(N, dtype)
    n = N-1
    h = (rng.standard_normal((n, n), dtype=dtype) if coefficients is None
         else np.array(coefficients, dtype=dtype, copy=True))
    ev = eigen_1d(N, dtype)
    for start in range(0, n, 32):
        weights = ev[start:start+32, None] + ev[None, :]
        np.sqrt(weights, out=weights)
        h[start:start+32] /= weights
    h = dstn(h, type=1, norm='ortho', overwrite_x=True, workers=1)
    if peak_bytes() >= CAP:
        raise MemoryError('observed peak reached 4 GB')
    return h

def diagonal(N):
    """All diagonal entries of G_N via the sin^2 identity and a cosine FFT.

    A type-I cosine transform of w[k,l]=1/eigenvalue, padded with zero
    endpoint rows and columns, yields 4 sum w cos(pi*k*i/N)cos(pi*l*j/N).
    sin^2(a)=(1-cos(2a))/2 then gives each variance. The result is a
    generator of row blocks, avoiding a second full grid.
    """
    check_resources(N)
    ev = eigen_1d(N)
    w = np.zeros((N+1, N+1), dtype=np.float64)
    for start in range(0, N-1, 32):
        w[1+start:1+min(start+32,N-1), 1:N] = 1/(ev[start:start+32, None]+ev[None, :])
    w = dctn(w, type=1, norm='backward', overwrite_x=True, workers=1)
    ids = 2*np.arange(1, N)
    ids = np.minimum(ids, 2*N-ids)
    for start in range(0, N-1, 32):
        ii = ids[start:start+32]
        v = (w[0, 0]-w[ii, 0, None]-w[0, ids][None, :]
             +w[ii[:, None], ids[None, :]]) / (4*N*N)
        yield start, v

def observables(h, N, lambdas):
    L = np.log(N)
    t = G*L
    result = {}
    for lam in lambdas:
        beta = 2*lam/np.sqrt(G)
        cb = 1/(beta*np.sqrt(2*np.pi*G))
        count = int(np.count_nonzero(h >= beta*t))
        x = np.sqrt(L)*np.exp(beta*beta*t/2)*count/N**2
        mass = deriv1 = deriv2 = 0.
        for start in range(0, N-1, 32):
            block = h[start:start+32].astype(np.float64)
            z = block-beta*t
            e = np.exp(beta*block-beta*beta*t/2)
            mass += e.sum()
            deriv1 += (e*z).sum()
            deriv2 += (e*(z*z-t)).sum()
        mass /= N*N
        qmass = (-.5*deriv2+deriv1/beta-N*N*mass/beta**2)/(N*N)
        result[lam] = dict(count=count, X=float(x), Y=float(cb*mass),
                           D=float(L*(x-cb*mass)),
                           Q=float(cb*qmass/G))
    return result
