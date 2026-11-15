"""High precision ambient criterion from the eight atom polynomials.

Coordinate order is (a,b,c,Re12,Im12,Re13,Im13,Re23,Im23).
Polynomial generation is inherited from C0033D/interval_core.py.
This variant of C0033E/mp_core.py selects the smallest conditional-log-odds
pair for gamma instead of averaging all three, to avoid subtracting large
internal block odds in an extremely weakly connected collar.
All solves here use mpmath, with diagonal scaling and no binary atom arithmetic.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'): os.environ[k]='1'
import sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
import mpmath as mp
from interval_core import poly,grad,hess
PAIRS=((0,1),(0,2),(1,2))

def coordinates(q):
    return [mp.re(q[i,i]) for i in range(3)]+[z for i,j in PAIRS for z in (mp.re(q[i,j]),mp.im(q[i,j]))]

def kernel(x):
    q=mp.diag(x[:3])
    for k,(i,j) in enumerate(PAIRS):
        q[i,j]=mp.mpc(x[3+2*k],x[4+2*k]); q[j,i]=mp.conj(q[i,j])
    return q

B=[]
for k in range(9):
    x=[mp.mpf(0)]*9;x[k]=mp.mpf(1);B.append(kernel(x))

def tr(a):return sum(a[i,i] for i in range(a.rows))

def scaled_solve(a,b):
    scale=[mp.sqrt(a[i,i]) for i in range(a.rows)]
    if any(mp.im(z) or z<=0 for z in scale):raise ArithmeticError('nonpositive solve diagonal')
    aa=mp.matrix([[a[i,j]/(scale[i]*scale[j]) for j in range(a.rows)] for i in range(a.rows)])
    bb=mp.matrix([b[i]/scale[i] for i in range(a.rows)])
    y=mp.lu_solve(aa,bb)
    return mp.matrix([y[i]/scale[i] for i in range(a.rows)])

def evaluate(q,full=False):
    x=coordinates(q);p=list(map(mp.mpf,poly(*x)));g=mp.matrix(grad(*x))
    if min(p)<=0:raise ArithmeticError('nonpositive atom')
    ell0=[];ell1=[]
    for i,j,k in ((1,2,0),(0,2,1),(0,1,2)):
        si,sj,sk=1<<i,1<<j,1<<k;prod=q[i,k]*q[k,j]
        ell0.append(mp.log1p(abs((1-q[k,k])*q[i,j]+prod)**2/(p[0]*p[si|sj])))
        ell1.append(mp.log1p(abs(q[k,k]*q[i,j]-prod)**2/(p[sk]*p[7])))
    selected=min(range(3),key=lambda i:max(abs(ell0[i]),abs(ell1[i])))
    gamma=ell0[selected]-ell1[selected]
    R=mp.diag(ell0)-gamma*q if gamma<=0 else mp.diag(ell1)+gamma*(mp.eye(3)-q)
    rscale=[mp.sqrt(mp.re(R[i,i])) for i in range(3)]
    RR=mp.matrix([[R[i,j]/(rscale[i]*rscale[j]) for j in range(3)] for i in range(3)])
    RRI=RR**-1
    d=mp.re(mp.det(RR))*mp.fprod(t*t for t in rscale)
    ri=mp.matrix([[RRI[i,j]/(rscale[i]*rscale[j]) for j in range(3)] for i in range(3)])
    if d<=0:raise ArithmeticError('nonpositive R determinant')
    f=g.T*mp.diag([1/z for z in p])*g
    rb=[ri*b for b in B];z=mp.matrix([mp.re(tr(a)) for a in rb])
    J=f+mp.matrix([[d*mp.re(tr(rb[i]*rb[j])) for j in range(9)] for i in range(9)])
    v=scaled_solve(J,z);theta=d*(z.T*v)[0];margin=1-theta
    logscale=-mp.log(min(p))
    out=dict(margin=margin,theta=theta,logscale=logscale,scaled=margin*(logscale+4),pmin=min(p),gamma=gamma)
    if full:
        hh=hess(*x)
        nh=f+mp.matrix([[sum(mp.log(p[s])*hh[s][i][j] for s in range(8)) for j in range(9)] for i in range(9)])
        out.update(p=p,R=R,J=J,z=z,negative_hessian=nh,direction=sum((v[i]*B[i] for i in range(9)),mp.zeros(3)))
    return out

def cyclic(L):
    k=mp.exp(L);r=mp.sqrt((k-1)/(4*(3*k+1)))
    return kernel([mp.mpf('.5')]*3+[0,r,0,-r,0,r])

def rotation(i,j,angle,phase=0):
    u=mp.eye(3);c=mp.cos(angle);s=mp.sin(angle);e=mp.exp(mp.j*phase)
    u[i,i]=u[j,j]=c;u[i,j]=s*e;u[j,i]=-s*mp.conj(e)
    return u

def spectral(params,L):
    """Seven real parameters, endpoints exp(-L) times positive factors.

    params=(theta12,theta13,theta23,phase,log_gap0_factor,
            log_gap1_factor,logit_middle).
    """
    a,b,c,phase,g0,g1,mid=map(mp.mpf,params)
    e0=mp.exp(-mp.mpf(L)+g0);e1=mp.exp(-mp.mpf(L)+g1)
    t=1/(1+mp.exp(-mid))
    if not 0<e0<t<1-e1<1:raise ArithmeticError('spectrum out of domain')
    u=rotation(1,2,c)*rotation(0,2,b,phase)*rotation(0,1,a)
    q=u*mp.diag([e0,t,1-e1])*u.H
    return (q+q.H)/2

def mixed(t,alpha=1,beta=2,eta=2,ratio=1,phase=0):
    """Q11=1-t^alpha, Q23=-1/2+t^beta, Q12=t^eta,
    Q13=ratio exp(i phase)t^eta. Feasibility must be checked.
    """
    t=mp.mpf(t)
    alpha,beta,eta,ratio,phase=[mp.mpf(str(v)) if isinstance(v,float) else mp.mpf(v) for v in (alpha,beta,eta,ratio,phase)]
    e=t**eta
    return kernel([1-t**alpha,mp.mpf('.5'),mp.mpf('.5'),e,0,
                   ratio*mp.cos(phase)*e,ratio*mp.sin(phase)*e,-mp.mpf('.5')+t**beta,0])

def strict(q):
    for a in (q,mp.eye(3)-q):
        for n in (1,2,3):
            if mp.re(mp.det(a[:n,:n]))<=0:return False
    return True

def strings(x,digits=45):
    if isinstance(x,dict):return {k:strings(v,digits) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [strings(v,digits) for v in x]
    if isinstance(x,(mp.mpf,mp.mpc)):return mp.nstr(x,digits)
    return x
