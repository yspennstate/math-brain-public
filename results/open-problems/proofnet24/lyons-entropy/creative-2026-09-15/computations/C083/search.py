"""Bounded full-Hermitian Hessian search at frustrated cycle/chiral kernels.

Run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python search.py.
Deterministic seeds and every optimization endpoint are saved. Floating point
results are candidates only; certify.py performs separate rational checks.
"""
from pathlib import Path
import json, time, argparse
import numpy as np
from scipy.optimize import minimize

OUT=Path(__file__).resolve().parent

def basis(n):
    b=[]; labels=[]
    for i in range(n):
        e=np.zeros((n,n),complex);e[i,i]=1;b.append(e);labels.append(f'd{i}')
    for part in [1,1j]:
        for i in range(n):
            for j in range(i+1,n):
                e=np.zeros((n,n),complex);e[i,j]=part/np.sqrt(2);e[j,i]=np.conj(part)/np.sqrt(2)
                b.append(e);labels.append(('re' if part==1 else 'im')+f'{i}{j}')
    return np.array(b),labels

CACHE={}
def jets(K):
    n=len(K)
    if n not in CACHE:
        E,labels=basis(n);bits=np.array([[(mask>>i)&1 for i in range(n)] for mask in range(2**n)])
        CACHE[n]=(E,labels,bits)
    E,labels,bits=CACHE[n]
    M=np.tile(K,(2**n,1,1));M[:,np.arange(n),np.arange(n)]-=1-bits
    sign,logp=np.linalg.slogdet(M)
    p=(sign*((-1.)**(n-bits.sum(1)))).real*np.exp(logp)
    if p.min()<=0:raise FloatingPointError('nonpositive atom')
    T=np.linalg.inv(M)
    R=np.einsum('sij,ajk->saik',T,E,optimize=True)
    tr=np.trace(R,axis1=2,axis2=3).real
    rr=np.einsum('saij,sbji->sab',R,R,optimize=True).real
    g=p[:,None]*tr
    h=p[:,None,None]*(tr[:,:,None]*tr[:,None,:]-rr)
    return E,labels,p,g,h

def hessian(K,details=False):
    E,labels,p,g,h=jets(K)
    F=np.einsum('si,sj,s->ij',g,g,1/p)
    J=-np.einsum('sij,s->ij',h,np.log(p))
    H=J-F;H=(H+H.T)/2
    val,vec=np.linalg.eigh(H)
    if not details:return val[-1]
    a=vec[:,-1];A=np.einsum('a,aij->ij',a,E)
    L=K@np.linalg.inv(np.eye(len(K))-K)
    # An explicit negative-real normalized odds triangle excludes C071.
    triangles=[]
    for i in range(len(K)):
        for j in range(i+1,len(K)):
            for k in range(j+1,len(K)):
                q=-L[i,j]*L[j,k]*L[k,i]
                if q.real < -1e-12:triangles.append([i,j,k,float(q.real),float(q.imag)])
    # In one physical line through a diagonal, all existing off-diagonals
    # would be proportional; the residual also tests the optimized direction.
    off=K-np.diag(np.diag(K));ao=A-np.diag(np.diag(A))
    c=np.vdot(ao,off).real/np.vdot(ao,ao).real
    line_res=np.linalg.norm(off-c*ao)
    probs_by_size=[]
    for sz in range(len(K)+1):
        pp=p[[mask.bit_count()==sz for mask in range(2**len(K))]]
        probs_by_size.append(float(np.ptp(pp)))
    return {'n':len(K),'lambda_max':float(val[-1]),'hessian_eigenvalues':val.tolist(),
        'kernel_eigenvalues':np.linalg.eigvalsh(K).tolist(),'min_probability':float(p.min()),
        'F_along_max':float(a@F@a),'J_along_max':float(a@J@a),
        'atom_mass_error':float(abs(p.sum()-1)),
        'gradient_mass_error':float(abs(g.sum(0)).max()),
        'second_mass_error':float(abs(h.sum(0)).max()),
        'negative_real_odds_triangles':triangles[:3],
        'count_level_probability_ranges':probs_by_size,
        'diagonal_line_residual':float(line_res),
        'K_real':K.real.tolist(),'K_imag':K.imag.tolist(),
        'A_real':A.real.tolist(),'A_imag':A.imag.tolist()}

def cycle(x,n):
    # Unequal cycle moduli and one gauge-invariant phase. Spectral scaling
    # gives exactly prescribed lower/upper gaps for every iterate.
    r=np.exp(x[:n]);phi=x[n]
    B=np.zeros((n,n),complex)
    for i in range(n):
        j=(i+1)%n;z=r[i]*(np.exp(1j*phi) if i==n-1 else 1)
        B[i,j]=z;B[j,i]=z.conjugate()
    # Diagonal heterogeneity excludes the count-uniform locus and expands
    # beyond balanced bipartite families, with only n+1 shape parameters.
    B+=np.diag(np.linspace(-.13,.17,n))
    eig=np.linalg.eigvalsh(B);lo=10**x[n+1];hi=10**x[n+2]
    return lo*np.eye(n)+(1-lo-hi)*(B-eig[0]*np.eye(n))/(eig[-1]-eig[0])

def chiral(x,n):
    # Balanced bipartite with a complex 2x2 or 3x3 block, asymmetric
    # singular values, and sparse endpoint vectors when epsilon is small.
    a=n//2;b=n-a;size=a*b
    B=np.exp(x[:size]).reshape(a,b)*np.exp(1j*x[size:2*size].reshape(a,b))
    U,s,V=np.linalg.svd(B,full_matrices=False)
    gap=10**x[-1]
    B=B*((.5-gap)/s[0])
    K=.5*np.eye(n,dtype=complex);K[:a,a:]=B;K[a:,:a]=B.conj().T
    return K

def gauge_weights(K):
    E,labels,p,g,h=jets(K);grad=-g.T@np.log(p)
    n=len(K);w=[]
    for i in range(n):
        j=(i+1)%n;R=np.zeros_like(K);R[i,j]=K[i,j];R[j,i]=K[j,i]
        coords=np.einsum('aij,ji->a',E,R).real
        w.append(float(grad@coords))
    return w

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--boundary',action='store_true');args=parser.parse_args()
    filename='search_boundary_results.json' if args.boundary else 'search_results.json'
    start=time.time();rng=np.random.default_rng(830915);rows=[]
    # Six structured initial cycle points: multiscale and near saturated;
    # four initial chiral points. Bounds are predeclared, no adaptive sweep.
    jobs=[]
    for n in [4,5,6]:
        for variant in range(2):
            x=np.r_[rng.uniform(-.8,.5,n),(.35+variant*.4)*np.pi,
                     -3.0-2*variant,-.55-2.0*variant]
            bounds=[(-2.,.8)]*n+[(.08*np.pi,.92*np.pi),(-7,-.31),(-7,-.31)]
            if args.boundary:
                x[-2:]=[-3.-2*variant,-2.-3*variant]
                bounds[-2:]=[(-7,-2),(-7,-2)]
            jobs.append(('cycle',n,variant,x,bounds,cycle))
    for n in [4,6]:
        for variant in range(2):
            sz=(n//2)*(n-n//2)
            x=np.r_[rng.uniform(-1.6,.4,sz),rng.uniform(-np.pi,np.pi,sz),-3.-2*variant]
            bounds=[(-3.,.8)]*sz+[(-np.pi,np.pi)]*sz+[(-7,-.6)]
            if args.boundary:bounds[-1]=(-7,-2)
            jobs.append(('chiral',n,variant,x,bounds,chiral))
    for family,n,variant,x,bounds,constructor in jobs:
        calls=[0];best=[-np.inf,None]
        def fun(y):
            calls[0]+=1
            try:
                K=constructor(y,n);v=hessian(K)
                if v>best[0]:best[:]=[v,y.copy()]
                return -v
            except (np.linalg.LinAlgError,FloatingPointError):return 1e6
        initial=-fun(x)
        # Two Powell passes, hard function cap: local directed optimization,
        # not an exhaustive sweep. Record the best actual evaluated iterate.
        res=minimize(fun,x,method='Powell',bounds=bounds,
                     options={'maxfev':240,'maxiter':2,'xtol':2e-3,'ftol':2e-5})
        xx=best[1];K=constructor(xx,n);row=hessian(K,True)
        row.update({'family':family,'variant':variant,'initial_lambda_max':float(initial),
                    'parameters':xx.tolist(),'initial_parameters':x.tolist(),'bounds':bounds,
                    'evaluations':calls[0],'optimizer_status':int(res.status),
                    'optimizer_message':str(res.message)})
        if family=='cycle':row['radial_edge_entropy_derivatives']=gauge_weights(K)
        rows.append(row)
        (OUT/filename).write_text(json.dumps({'seed':830915,'boundary_spread_guard':args.boundary,'rows':rows,
             'elapsed_seconds':time.time()-start,'status':'in_progress'},indent=2)+'\n')
        print(f'{family} n={n} v={variant} initial={initial:.8g} best={row["lambda_max"]:.8g} evals={calls[0]}',flush=True)
    (OUT/filename).write_text(json.dumps({'seed':830915,'boundary_spread_guard':args.boundary,'rows':rows,
         'elapsed_seconds':time.time()-start,'status':'complete','any_positive':any(r['lambda_max']>1e-8 for r in rows)},indent=2)+'\n')

if __name__=='__main__':main()
