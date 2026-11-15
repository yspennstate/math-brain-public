"""Small finite-set operations. Masks use bit i for coordinate i."""
import numpy as np

def mv(a,x):
    # Small matrices: avoid Accelerate's spurious floating-point matmul flags on this Mac.
    return np.einsum('ij,j->i',a,x,optimize=False)

def tables(n):
    m = 1 << n
    pc = np.array([s.bit_count() for s in range(m)])
    z = np.array([[(u & r) == r for u in range(m)] for r in range(m)], dtype=float)
    rows, rhs, meta = [], [], []
    for r in range(1, m):
        for k in range(n - pc[r] + 1):
            rows.append(z[r] * (pc <= pc[r] + k))
            rhs.append(3.0**k * 2.0**pc[r])
            meta.append((r,k))
    return pc, z, np.array(rows), np.array(rhs), meta

def quantities(mu, pc, z):
    up = mv(z,mu)
    ok = mu > 0
    A = -np.dot(mu[ok], np.log2(up[ok]))
    H = -np.dot(mu[ok], np.log2(mu[ok]))
    I = np.dot(mu, pc)
    return {'A':float(A), 'B':float(H-A), 'H':float(H), 'I':float(I),
            'A_I':float(A/I) if I > 0 else 0., 'B_I':float((H-A)/I) if I > 0 else 0.}

def fwht(x):
    a=np.array(x,dtype=float,copy=True)
    h=1
    while h<a.shape[-1]:
        b=a.reshape(*a.shape[:-1],-1,2*h)
        lo=b[...,:h].copy(); hi=b[...,h:].copy()
        b[...,:h]=lo+hi; b[...,h:]=lo-hi
        h*=2
    return a

def check(mu,n):
    pc,z,lhs,fac,meta=tables(n)
    up=mv(z,mu)
    rr=np.array([r for r,k in meta])
    right=fac*up[rr]**1.5
    left=mv(lhs,mu)
    diff=left-right
    j=int(np.argmax(diff))
    return {'max_violation':float(diff[j]),'witness':meta[j], **quantities(mu,pc,z)}
