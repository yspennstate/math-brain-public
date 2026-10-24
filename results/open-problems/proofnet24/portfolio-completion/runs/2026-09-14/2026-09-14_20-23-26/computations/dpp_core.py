"""Determinantal atom probabilities and analytic entropy derivatives.

Floating point exploration only; no universal or interval certificate.
The mixed-column determinant is valid for complex Hermitian contractions.
"""
import itertools
import numpy as np

def atom_matrices(K):
    K = np.asarray(K)
    n = K.shape[0]
    bits = np.array(list(itertools.product((0, 1), repeat=n)))
    signs = 2 * bits - 1
    eye = np.eye(n, dtype=K.dtype)
    mats = K[None, :, :] * signs[:, None, :] + eye[None, :, :] * (1 - bits[:, None, :])
    return mats, signs

def probabilities(K):
    mats, _ = atom_matrices(K)
    values = np.linalg.det(mats)
    if np.max(np.abs(np.imag(values))) > 1e-8:
        raise ArithmeticError('Atom determinants have nonnegligible imaginary parts')
    return values.real

def entropy(K):
    p = probabilities(K)
    if p.min() < -1e-10 or abs(p.sum() - 1) > 1e-8:
        raise ArithmeticError('Invalid probabilities')
    pos = p > 0
    return -float(np.dot(p[pos], np.log(p[pos])))

def direction_derivatives(K, A):
    mats, signs = atom_matrices(K)
    p = np.linalg.det(mats).real
    if p.min() <= 0:
        raise ValueError('Analytic derivative routine requires positive atoms')
    R = np.linalg.solve(mats, np.asarray(A)[None, :, :] * signs[:, None, :])
    trace = np.trace(R, axis1=1, axis2=2).real
    squaretrace = np.einsum('bij,bji->b', R, R).real
    dp = p * trace
    ddp = p * (trace**2 - squaretrace)
    fisher = float(np.sum(dp**2 / p))
    curvature = float(-np.dot(ddp, np.log(p)))
    return {'p':p, 'dp':dp, 'ddp':ddp, 'H2':-fisher+curvature,
            'fisher':fisher, 'curvature':curvature,
            'normalization_error':float(abs(p.sum()-1)),
            'first_sum_error':float(abs(dp.sum())),
            'second_sum_error':float(abs(ddp.sum()))}

def hermitian_basis(n, complex_case=False):
    out=[]
    for i in range(n):
        A=np.zeros((n,n),dtype=complex if complex_case else float)
        A[i,i]=1
        out.append(A)
    for i in range(n):
        for j in range(i+1,n):
            A=np.zeros((n,n),dtype=complex if complex_case else float)
            A[i,j]=A[j,i]=1/np.sqrt(2)
            out.append(A)
            if complex_case:
                A=np.zeros((n,n),dtype=complex)
                A[i,j]=1j/np.sqrt(2)
                A[j,i]=-1j/np.sqrt(2)
                out.append(A)
    return np.array(out)

def entropy_hessian(K, complex_case=False):
    mats, signs=atom_matrices(K)
    p=np.linalg.det(mats).real
    if p.min()<=0:
        raise ValueError('Positive atoms required')
    basis=hermitian_basis(len(K),complex_case)
    R=np.linalg.inv(mats)[:,None,:,:] @ (basis[None,:,:,:]*signs[:,None,None,:])
    tr=np.trace(R,axis1=2,axis2=3).real
    gram=np.einsum('sbxy,scyx->sbc',R,R).real
    H=-np.einsum('s,sb,sc->bc',p*(1+np.log(p)),tr,tr)+np.einsum('s,sbc->bc',p*np.log(p),gram)
    return (H+H.T)/2,basis

def random_contraction(rng,n,complex_case=False,spectrum='uniform'):
    G=rng.normal(size=(n,n))
    if complex_case:
        G=G+1j*rng.normal(size=(n,n))
    U,_=np.linalg.qr(G)
    vals=rng.uniform(.02,.98,n) if spectrum=='uniform' else np.clip(rng.beta(.35,.35,n),1e-4,1-1e-4)
    return (U*vals)@U.conj().T
