"""Critical-profile discretizations and the genuine quartic tridiagonal target.

All matrix storage and target/gradient evaluation are linear in matrix dimension.
"""
import os
for key in ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"]:
    os.environ[key] = "1"
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import minimize
from scipy.linalg import cholesky_banded,cho_solve_banded

def bottom(diagonal, offdiag, count=3):
    return eigh_tridiagonal(diagonal, offdiag, select="i", select_range=(0, count-1),
                            eigvals_only=True, check_finite=False, lapack_driver="stebz")

def profile(n, beta, rng, k=1, noise="chi", h=None):
    """H=-Delta_h+t^p+cell-averaged weighted noise, exact cell variance.

    T=2I-h^2 H has constant off-diagonal 1 and deterministic diagonal -(j/n)^p
    if h=n^(-1/(4k+3)). Gaussian and centered chi_1 noise have the same variance.
    """
    p = 1/(2*k+1)
    if h is None:
        h = n**(-1/(4*k+3))
    t = h*np.arange(1,n+1,dtype=float)
    # Difference formula avoids cancellation for far-away cells.
    left = t-h
    cell_var = np.empty(n)
    cell_var[0] = h**p/p
    cell_var[1:] = left[1:]**p*np.expm1(p*np.log1p(h/left[1:]))/p
    if noise == "chi":
        xi = (np.abs(rng.normal(size=n))-np.sqrt(2/np.pi))/np.sqrt(1-2/np.pi)
    elif noise == "gaussian":
        xi = rng.normal(size=n)
    elif noise == "none":
        xi = np.zeros(n)
    else:
        raise ValueError(noise)
    delta_w = (2/np.sqrt(beta))*np.sqrt(cell_var)*xi
    d = 2/h**2 + t**p + delta_w/h
    return d, np.full(n-1,-1/h**2), h

def quartic_U(x):
    return x**4/20-4*x**3/15+x*x/5+8*x/5

def quartic_action_grad(a,q):
    """Returns E/(n beta), its a and log(b) gradient.

    KRV V=U/2, density in da dq proportional to
       exp[-n beta tr(U(T))/2 + beta sum_i (n-i)q_i].
    The +1 in the log(b) Jacobian has already been included.
    """
    n=len(a)
    b=np.exp(q); b2=b*b
    neighbor=np.zeros(n);neighbor[:-1]+=b2;neighbor[1:]+=b2
    c=a*a+neighbor
    d=b*(a[:-1]+a[1:])
    e=b[:-1]*b[1:]
    tr2=np.sum(a*a)+2*np.sum(b2)
    tr3=np.sum(a*a*a)+3*np.sum(b2*(a[:-1]+a[1:]))
    tr4=np.dot(c,c)+2*np.dot(d,d)+2*np.dot(e,e)
    trU=tr4/20-4*tr3/15+tr2/5+8*np.sum(a)/5
    mass=(n-np.arange(1,n))/n
    action=trU/2-np.dot(mass,q)
    cube_diag=a**3+2*a*neighbor
    cube_diag[:-1]+=b2*a[1:];cube_diag[1:]+=b2*a[:-1]
    grad_a=(cube_diag-4*c+2*a+8)/10
    off_b_neighbors=np.zeros(n-1)
    off_b_neighbors[1:]+=b2[:-1];off_b_neighbors[:-1]+=b2[1:]
    cube_off=b*(a[:-1]**2+a[:-1]*a[1:]+a[1:]**2+b2+off_b_neighbors)
    grad_q=b*(cube_off-4*d+2*b)/5-mass
    return action,grad_a,grad_q

def quartic_mode(n, maxiter=1500):
    # Smooth start, then minimize the exact finite-dimensional log-density.
    a=np.full(n,-.8)
    q=np.log(.7*np.sqrt((n-np.arange(1,n))/n))
    start=np.r_[a,q]
    def fun(z):
        value,ga,gq=quartic_action_grad(z[:n],z[n:])
        return value,np.r_[ga,gq]
    result=minimize(fun,start,jac=True,method="L-BFGS-B",
                    options=dict(maxiter=maxiter,ftol=1e-14,gtol=2e-8,maxls=40,maxcor=12))
    return result.x[:n],result.x[n:],dict(success=bool(result.success),
        message=str(result.message),iterations=int(result.nit),
        gradient_max=float(np.max(np.abs(result.jac))),action=float(result.fun))

def hmc_chain(n,beta,mode,rng,burn=200,draws=160,thin=2,chain=0):
    """Metropolis-corrected HMC; diagnostics are required before using draws.

    A global diagonal preconditioner accounts for the n beta stiffness and the
    small b_i at the opposite endpoint. No claim of exact independent sampling.
    """
    a0,q0=mode
    scale=np.r_[np.full(n,np.sqrt(2/(n*beta))),
                1/np.sqrt(beta*(n-np.arange(1,n)))]
    origin=np.r_[a0,q0]
    def target(z):
        point=origin+scale*z
        with np.errstate(over="ignore",invalid="ignore"):
            value,ga,gq=quartic_action_grad(point[:n],point[n:])
            return n*beta*value,n*beta*np.r_[ga,gq]*scale
    z=rng.normal(size=2*n-1)*(.25 if chain==0 else 1.)
    value,grad=target(z)
    eps=.45*n**(-.25)
    accepted=0; accepted_post=0; divergences=0
    output=[];actions=[];step_history=[]
    total=burn+draws*thin
    for it in range(total):
        momentum=rng.normal(size=len(z)); old_kinetic=.5*np.dot(momentum,momentum)
        zz=z.copy(); pp=momentum.copy();gg=grad.copy()
        # Randomized trajectory length reduces periodicity.
        steps=int(rng.integers(max(3,int(.6/eps)),max(4,int(1.2/eps))))
        pp-=.5*eps*gg
        vv=np.inf
        for j in range(steps):
            zz+=eps*pp
            vv,gg=target(zz)
            if not np.isfinite(vv) or not np.all(np.isfinite(gg)):
                break
            pp-=eps*gg*(.5 if j==steps-1 else 1.)
        change=vv-value+.5*np.dot(pp,pp)-old_kinetic
        prob=float(np.exp(min(0.,-change))) if np.isfinite(change) else 0.
        if not np.isfinite(change) or abs(change)>1000:divergences+=1
        accept=rng.random()<prob
        if accept:
            z,value,grad=zz,vv,gg
            accepted+=1
            if it>=burn:accepted_post+=1
        if it<burn:
            eps*=np.exp(.025*(prob-.8))
            eps=float(np.clip(eps,.005,.5))
        if it>=burn and (it-burn)%thin==0:
            point=origin+scale*z
            a=point[:n];b=np.exp(point[n:])
            top=-bottom(-a,-b,3)
            output.append(top)
            actions.append(value)
        if it%50==0: step_history.append([it,eps,prob])
    return np.asarray(output),dict(acceptance=accepted/total,
        acceptance_post=accepted_post/(draws*thin),divergences=divergences,
        final_step=eps,adaptation=step_history,actions=actions)

def diagnostics(chains):
    """Basic split R-hat and initial-positive-pair autocorrelation ESS."""
    chains=np.asarray(chains)
    m,n=chains.shape
    half=n//2
    split=np.concatenate([chains[:,:half],chains[:,n-half:]],axis=0)
    W=np.mean(np.var(split,axis=1,ddof=1))
    B=half*np.var(np.mean(split,axis=1),ddof=1)
    rhat=np.sqrt(((half-1)/half*W+B/half)/W)
    centered=chains-chains.mean(axis=1,keepdims=True)
    var=np.mean(np.sum(centered*centered,axis=1))/n
    ac=[1.]
    for lag in range(1,min(n,150)):
        ac.append(np.mean(np.sum(centered[:,:n-lag]*centered[:,lag:],axis=1))/(n-lag)/var)
    tau=1.
    for lag in range(1,len(ac)-1,2):
        pair=ac[lag]+ac[lag+1]
        if pair<=0:break
        tau+=2*pair
    return dict(split_rhat=float(rhat),ess_within_chains=float(min(m*n,m*n/max(1,tau))),
                lag1=float(ac[1]),chain_means=chains.mean(axis=1).tolist())

def quartic_hessian_banded(a,q):
    """Hessian of E/(n beta), interleaved a_0,q_0,a_1,q_1,...; bandwidth 2."""
    n=len(a);b2=np.exp(2*q)
    neighbor=np.zeros(n);neighbor[:-1]+=b2;neighbor[1:]+=b2
    qqneighbor=np.zeros(n-1);qqneighbor[:-1]+=b2[1:];qqneighbor[1:]+=b2[:-1]
    band=np.zeros((3,2*n-1))
    band[0,::2]=(3*a*a+2*neighbor-8*a+2)/10
    band[0,1::2]=2*b2/5*(a[:-1]**2+a[:-1]*a[1:]+a[1:]**2+2*b2+qqneighbor-4*(a[:-1]+a[1:])+2)
    band[1,0:2*n-2:2]=b2*(4*a[:-1]+2*a[1:]-8)/10
    band[1,1:2*n-2:2]=b2*(2*a[:-1]+4*a[1:]-8)/10
    band[2,0:2*n-3:2]=b2/10
    band[2,1:2*n-3:2]=2*b2[:-1]*b2[1:]/5
    return band

def hmc_banded(n,beta,mode,rng,burn=300,draws=400,thin=2,chain=0):
    """Fixed Hessian mass, exact Metropolis correction, linear storage/work per step."""
    a0,q0=mode
    z=np.empty(2*n-1);z[::2]=a0;z[1::2]=q0
    band=quartic_hessian_banded(a0,q0)
    shift=0.
    for attempt in range(8):
        trial=band.copy();trial[0]+=shift
        try:
            chol=cholesky_banded(n*beta*trial,lower=True,check_finite=False)
            break
        except np.linalg.LinAlgError:
            shift=1e-9 if shift==0 else shift*10
    else:
        raise RuntimeError('Mode Hessian is not sufficiently positive')
    def solve(p):return cho_solve_banded((chol,True),p,check_finite=False)
    def momentum():
        x=rng.normal(size=2*n-1)
        y=chol[0]*x
        y[1:]+=chol[1,:-1]*x[:-1]
        y[2:]+=chol[2,:-2]*x[:-2]
        return y
    def target(point):
        with np.errstate(over='ignore',invalid='ignore'):
            value,ga,gq=quartic_action_grad(point[::2],point[1::2])
            grad=np.empty_like(point);grad[::2]=ga;grad[1::2]=gq
            return n*beta*value,n*beta*grad
    # Distinct dispersed starts; an accepted warm-up phase follows.
    z+=solve(momentum())*(.2 if chain==0 else .6)
    value,grad=target(z)
    eps=.5*n**(-.25)
    accepted_post=0;divergences=0;output=[];history=[]
    total=burn+draws*thin
    for it in range(total):
        pp=momentum();oldK=.5*np.dot(pp,solve(pp))
        zz=z.copy();gg=grad.copy()
        steps=int(rng.integers(max(3,int(1./eps)),max(4,int(2.5/eps))))
        pp-=.5*eps*gg;vv=np.inf
        for j in range(steps):
            zz+=eps*solve(pp)
            vv,gg=target(zz)
            if not np.isfinite(vv) or not np.all(np.isfinite(gg)):break
            pp-=eps*gg*(.5 if j==steps-1 else 1.)
        change=vv-value+.5*np.dot(pp,solve(pp))-oldK
        prob=float(np.exp(min(0.,-change))) if np.isfinite(change) else 0.
        if not np.isfinite(change) or abs(change)>1000:divergences+=1
        if rng.random()<prob:
            z,value,grad=zz,vv,gg
            if it>=burn:accepted_post+=1
        if it<burn:eps=float(np.clip(eps*np.exp(.025*(prob-.8)),.002,.5))
        elif (it-burn)%thin==0:
            output.append(-bottom(-z[::2],-np.exp(z[1::2]),3))
        if it%100==0:history.append([it,eps,prob])
    return np.asarray(output),dict(acceptance_post=accepted_post/(draws*thin),
        divergences=divergences,hessian_shift=shift,final_step=eps,adaptation=history),z
