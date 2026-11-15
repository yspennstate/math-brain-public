"""Seven kernel parameters; the scalar criterion retains all nine directions.

Parameters are (a,b,c,x,y,r,phi), with Q12=x, Q13=y, Q23=r*exp(i phi).
Polynomial derivatives use the full, unnormalized nine-entry Hermitian basis.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import numpy as np

PAIRS=((0,1),(0,2),(1,2))
B=np.zeros((9,3,3),complex)
for i in range(3): B[i,i,i]=1
for k,(i,j) in enumerate(PAIRS):
    B[3+2*k,i,j]=B[3+2*k,j,i]=1
    B[4+2*k,i,j]=1j; B[4+2*k,j,i]=-1j
SIG=np.array([(-1)**(3-s.bit_count()) for s in range(8)])
BITS=((np.arange(8)[:,None]>>np.arange(3))&1)

def kernel(t):
    a,b,c,x,y,r,phi=t; z=r*np.exp(1j*phi)
    return np.array([[a,x,y],[x,b,z],[y,z.conjugate(),c]],complex)

def parameters(q):
    # Phase on a missing edge has no invariant meaning. Return phi=0 there.
    tri=q[0,1]*q[1,2]*q[2,0]
    return np.r_[q.diagonal().real,abs(q[0,1]),abs(q[0,2]),abs(q[1,2]),abs(np.angle(tri))]

def gauge(q): return kernel(parameters(q))

def atoms_grad(q, extended=True):
    dt=np.clongdouble if extended else np.complex128
    q=np.asarray(q,dtype=dt)
    u=q[0,0].real-(1-BITS[:,0]);v=q[1,1].real-(1-BITS[:,1]);w=q[2,2].real-(1-BITS[:,2])
    x,y,z=q[0,1],q[0,2],q[1,2]
    det=u*v*w-u*abs(z)**2-v*abs(y)**2-w*abs(x)**2+2*(x*z*y.conjugate()).real
    p=SIG*det
    # C_s is the Hermitian gradient matrix: Dp_s[A]=tr(C_s A).
    C=np.empty((8,3,3),dtype=dt)
    C[:,0,0]=v*w-abs(z)**2;C[:,1,1]=u*w-abs(y)**2;C[:,2,2]=u*v-abs(x)**2
    C[:,0,1]=y*z.conjugate()-x*w
    C[:,0,2]=x*z-y*v
    C[:,1,2]=y*x.conjugate()-z*u
    for i,j in PAIRS: C[:,j,i]=C[:,i,j].conjugate()
    C*=SIG[:,None,None]
    return np.asarray(p,float),np.asarray(C,complex)

def R_matrix(q,p):
    ell0=[];ell1=[]
    for i,j,k in ((1,2,0),(0,2,1),(0,1,2)):
        si,sj,sk=1<<i,1<<j,1<<k
        # Conditional negative association gives stable log1p formulas.
        prod=q[i,k]*q[k,j]
        ell0.append(np.log1p(abs((1-q[k,k].real)*q[i,j]+prod)**2/(p[0]*p[si|sj])))
        ell1.append(np.log1p(abs(q[k,k].real*q[i,j]-prod)**2/(p[sk]*p[7])))
    ell0=np.array(ell0);ell1=np.array(ell1)
    gamma=float(np.mean(ell0-ell1))
    # Choose the representation adding PSD matrices, avoiding cancellation.
    R=np.diag(ell0)-gamma*q if gamma<=0 else np.diag(ell1)+gamma*(np.eye(3)-q)
    return R,gamma,float(np.ptp(ell0-ell1))

def criterion(q, details=False):
    p,C=atoms_grad(q)
    if min(p)<=0: raise ArithmeticError('nonpositive atom')
    R,gamma,discrep=R_matrix(q,p)
    vals,U=np.linalg.eigh(R)
    if vals[0]<=0: raise ArithmeticError('R not positive numerically')
    root=np.einsum('ik,jk,k->ij',U,U.conj(),np.sqrt(vals),optimize=False)
    T=np.einsum('ij,bjk,kl->bil',root,B,root,optimize=False)
    dp=np.einsum('sij,bji->sb',C,T,optimize=False).real
    d=float(np.prod(vals))
    F=np.einsum('sb,sc,s->bc',dp,dp,1/(p*d),optimize=False)
    # B is not normalized; tr(B_i B_j)=diag(1,1,1,2,...,2).
    M=np.diag([1.,1.,1.,2.,2.,2.,2.,2.,2.])+F
    tau=np.r_[np.ones(3),np.zeros(6)]
    v=np.linalg.solve(M,tau);theta=float(tau@v)
    if not np.isfinite(theta):raise ArithmeticError('nonfinite theta')
    if not details:return theta
    A=np.einsum('b,bij->ij',v,T,optimize=False);A=(A+A.conj().T)/2
    A/=np.linalg.norm(A)
    grad=np.einsum('sij,bji->sb',C,B,optimize=False).real
    return dict(theta=theta,margin=1-theta,p=p,R=R,R_eigenvalues=vals,
                gamma=gamma,gamma_spread=discrep,A=A,grad=grad,
                parameters=parameters(q),spectrum=np.linalg.eigvalsh(q),
                condition=float(np.linalg.cond(M)))

def probability_criterion(q):
    """Woodbury's identity: theta=3-b^T(d diag(p)+K)^(-1)b."""
    p,C=atoms_grad(q);R,_,_=R_matrix(q,p);d=np.linalg.det(R).real
    RC=np.einsum('ij,sjk->sik',R,C,optimize=False)
    K=np.einsum('sij,tji->st',RC,RC,optimize=False).real
    b=np.trace(RC,axis1=1,axis2=2).real
    return 3-float(b@np.linalg.solve(d*np.diag(p)+K,b))

def seven_criterion(q):
    """Seven atoms; W^-1=diag(p_nonempty)-p_nonempty p_nonempty^T."""
    p,C=atoms_grad(q);R,_,_=R_matrix(q,p);d=np.linalg.det(R).real
    RC=np.einsum('ij,sjk->sik',R,C[1:],optimize=False)
    K=np.einsum('sij,tji->st',RC,RC,optimize=False).real
    b=np.trace(RC,axis1=1,axis2=2).real
    M=K+d*(np.diag(p[1:])-np.outer(p[1:],p[1:]))
    return 3-float(b@np.linalg.solve(M,b))

def jsonable(v):
    if isinstance(v,np.ndarray):
        return {'real':v.real.tolist(),'imag':v.imag.tolist()} if np.iscomplexobj(v) else v.tolist()
    if isinstance(v,(np.floating,np.integer)):return v.item()
    if isinstance(v,dict):return {k:jsonable(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [jsonable(x) for x in v]
    return v
