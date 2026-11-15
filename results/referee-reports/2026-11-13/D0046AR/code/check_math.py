"""Independent numerical audits of differentiation, clocks and quotient fibers."""
import json
import os
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import numpy as np
from scipy.linalg import eigh_tridiagonal
from threadpoolctl import threadpool_limits

OUT = Path(__file__).resolve().parents[1] / 'data'
rng = np.random.default_rng(46202613)

def lanczos(h):
    n = len(h)
    q = np.eye(n, dtype=complex)[:,0]
    previous = np.zeros(n, dtype=complex)
    beta = 0.
    basis, a, b = [], [], []
    for j in range(n):
        basis.append(q.copy())
        r = h@q-beta*previous
        alpha = float(np.vdot(q,r).real)
        r -= alpha*q
        # Reorthogonalization avoids accumulating a duplicate Krylov direction.
        for v in basis:
            r -= np.vdot(v,r)*v
        a.append(alpha)
        if j < n-1:
            beta = float(np.linalg.norm(r))
            b.append(beta)
            previous, q = q, r/beta
    return np.diag(a)+np.diag(b,1)+np.diag(b,-1), np.column_stack(basis)

def hermitian(n):
    z = rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    return (z+z.conj().T)/2

def main():
    assert os.getpriority(os.PRIO_PROCESS,0) >= 10
    result = {}
    # Gradient in actual independent Gaussian coordinates, with b=||Z||/sqrt(2).
    n = 12
    a = rng.normal(size=n)
    z = [rng.normal(size=2*(n-i-1)) for i in range(n-1)]
    b = np.array([np.linalg.norm(v)/np.sqrt(2) for v in z])
    vals, vecs = eigh_tridiagonal(a,b)
    v = vecs[:,-1]
    analytic = np.r_[v*v, *[np.sqrt(2)*v[i]*v[i+1]*zz/np.linalg.norm(zz) for i,zz in enumerate(z)]]
    coords = np.r_[a,*z]
    def value(c):
        aa = c[:n]
        offset=n
        bb=[]
        for zz in z:
            bb.append(np.linalg.norm(c[offset:offset+len(zz)])/np.sqrt(2))
            offset+=len(zz)
        return eigh_tridiagonal(aa,np.array(bb),select='i',select_range=(n-1,n-1),eigvals_only=True)[0]
    eps=1e-5
    gradient=[]
    for i in range(len(coords)):
        perturb = np.zeros(len(coords)); perturb[i]=eps
        gradient.append((value(coords+perturb)-value(coords-perturb))/(2*eps))
    result['gradient_max_error']=float(np.max(np.abs(gradient-analytic)))
    result['Gamma_gaussian_coordinates']=float(np.dot(gradient,gradient))
    result['Gamma_eigenvector_formula']=float(np.sum(v**4)+2*np.sum((v[:-1]*v[1:])**2))
    assert result['gradient_max_error'] < 1e-7

    # Small edge-time increment divided by ds tends to 2 E Gamma, rather than
    # 4 E Gamma. Matrix counterpart has Gamma=1 identically.
    for model in ['tri','matrix']:
        repetitions=6000
        n=20
        ds=1e-4
        dt=ds*n**(-1/3)
        rho=np.exp(-dt); sd=np.sqrt(-np.expm1(-2*dt))
        squares=[]; gammas=[]
        for rep in range(repetitions):
            if model=='matrix':
                h=hermitian(n)
                h2=rho*h+sd*hermitian(n)
                x=np.linalg.eigvalsh(h)[-1]; y=np.linalg.eigvalsh(h2)[-1]
                gammas.append(1.)
            else:
                aa=rng.normal(size=n)
                d=2*np.arange(n-1,0,-1)
                rr=np.sqrt(rng.chisquare(d))
                bb=rr/np.sqrt(2)
                val,vec=eigh_tridiagonal(aa,bb,select='i',select_range=(n-1,n-1))
                x=val[0]; vv=vec[:,0]
                gammas.append(np.sum(vv**4)+2*np.sum((vv[:-1]*vv[1:])**2))
                aa2=rho*aa+sd*rng.normal(size=n)
                rr2=np.sqrt((rho*rr+sd*rng.normal(size=n-1))**2+sd**2*rng.chisquare(d-1))
                y=eigh_tridiagonal(aa2,rr2/np.sqrt(2),select='i',select_range=(n-1,n-1),eigvals_only=True)[0]
            squares.append(n**(1/3)*(y-x)**2/ds)
        result[model+'_MSE_over_ds']=float(np.mean(squares))
        result[model+'_MSE_over_ds_SE']=float(np.std(squares,ddof=1)/np.sqrt(repetitions))
        result[model+'_predicted_2EGamma']=float(2*np.mean(gammas))
        assert abs(np.mean(squares)-2*np.mean(gammas)) < 5*np.std(squares,ddof=1)/np.sqrt(repetitions)

    # Orbit equivalence and measurable-section identities on a sample cyclic fiber.
    n=8
    h=hermitian(n)
    un,_=np.linalg.qr(rng.normal(size=(n-1,n-1))+1j*rng.normal(size=(n-1,n-1)))
    u=np.eye(n,dtype=complex); u[1:,1:]=un
    j,q=lanczos(h)
    j2,q2=lanczos(u@h@u.conj().T)
    result['orbit_representative_error']=float(np.max(np.abs(j-j2)))
    # Independent explicit contraction also avoids stale floating-point status
    # warnings from the platform BLAS after the preceding eigensolver calls.
    reconstructed=np.einsum('ji,jk,kl->il',q.conj(),h,q,optimize=False)
    result['lanczos_identity_error']=float(np.max(np.abs(reconstructed-j)))
    result['basis_equivariance_error']=float(np.max(np.abs(q2-u@q)))
    assert result['orbit_representative_error']<1e-10
    assert result['lanczos_identity_error']<1e-10
    result['nice']=os.getpriority(os.PRIO_PROCESS,0)
    OUT.mkdir(exist_ok=True)
    (OUT/'independent_math_checks.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    with threadpool_limits(limits=1):
        main()
