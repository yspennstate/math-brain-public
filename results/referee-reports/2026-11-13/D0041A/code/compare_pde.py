"""Evidence only. BV PDE vs known beta=2,4 Lax formulas and unspiked beta=1.
This does NOT evaluate Mo's finite-spike beta=1 contour formula.
Run: python3 code/compare_pde.py
"""
import os
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
import resource, time, json, csv
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.special import airy, ndtr
from scipy.linalg import solve_banded
assert os.getpriority(os.PRIO_PROCESS,0)>=10, 'Run at nice >=10'
# Arrays are O(n), with n<=2400; record peak resident memory at completion.
# macOS rejects RLIMIT_DATA changes in this managed sandbox.
ROOT=Path(__file__).resolve().parents[1]
TS=np.arange(-4.,3.01,.5)
WS=np.array([-3.,-2.,-1.,0.,1.,2.,3.,np.inf])

def painleve(left=-14.,tol=2e-10):
    grid=np.linspace(left,10,700)
    q0=np.where(grid<0,np.sqrt(np.maximum(-grid/2,0)),airy(grid)[0])
    p0=np.gradient(q0,grid)
    qleft=np.sqrt(-left/2)*(1+1/(8*left**3)-73/(128*left**6))
    def fun(x,y): return np.array([y[1],x*y[0]+2*y[0]**3])
    def bc(a,b): return np.array([a[0]-qleft,b[0]-airy(10)[0]])
    sol=solve_bvp(fun,bc,grid,np.array([q0,p0]),tol=tol,max_nodes=16000)
    assert sol.success,sol.message
    def accum(x,y):
        q=sol.sol(x)[0]
        return [-q*q,q,y[0]]
    ints=solve_ivp(accum,[10,left],[0,0,0],method='DOP853',rtol=2e-11,atol=2e-13,dense_output=True,max_step=.1)
    assert ints.success
    return sol,ints

def formula(beta,t,w,qsol,ints,zright=8.,laxtol=2e-11):
    s=(2**(2/3)*t if beta==4 else t)
    z=(2**(1/3)*w if beta==4 else w)
    q,p=qsol.sol(s);v,loge,logf=ints.sol(s)
    E=np.exp(loge);F=np.exp(logf)
    if np.isinf(w):
        if beta==1:return np.sqrt(E*F)
        if beta==2:return F
        return np.sqrt(F)*.5*(E**(-.5)+E**.5)
    assert beta in [2,4]
    if z==0:f,g=E,E
    elif z>0:
        # Forward integration excites the exp(z^3/3-s*z) parasitic mode.
        # Solve a separated BVP instead. The right condition at z=8 has
        # exponentially small influence at the largest requested z<3.8.
        grid=np.linspace(0.,zright,250)
        def rhs(x,y):
            f,g=y
            return np.array([q*q*f+(-x*q-p)*g,(-x*q+p)*f+(x*x-s-q*q)*g])
        def bc(a,b):return np.array([a[0]-E,b[1]])
        guess=np.array([E+(1-E)*grid/zright,E*np.exp(-grid)])
        sol=solve_bvp(rhs,bc,grid,guess,tol=laxtol,max_nodes=12000)
        assert sol.success,sol.message
        f,g=sol.sol(z)
    else:
        def rhs(x,y):
            f,g=y
            return [q*q*f+(-x*q-p)*g,(-x*q+p)*f+(x*x-s-q*q)*g]
        sol=solve_ivp(rhs,[0,z],[E,E],method='DOP853',rtol=2e-12,atol=2e-14,max_step=.03)
        assert sol.success
        f,g=sol.y[:,-1]
    if beta==2:return F*f
    return np.sqrt(F)*.5*((f+g)*E**(-.5)+(f-g)*E**.5)

def pde(beta,n,dt,T):
    # theta=arctan(w), [-pi/2,pi/2]; degenerate endpoint at +infinity.
    th=np.linspace(-np.pi/2,np.pi/2,n+1);h=np.pi/n
    c=np.cos(th);s=np.sin(th)
    diff=2/beta*c**4
    u=np.ones(n+1);u[0]=0
    neg=(th<0)&(th>-np.pi/2)
    w=np.tan(th[neg]);u[neg]=ndtr((T-w*w)/np.sqrt(4/beta*(-w)))
    out={}
    targets=np.sort(TS)[::-1]
    t=float(T)
    def generator(tm):
        drift=tm*c*c-s*s-4/beta*s*c**3
        # Centered where rates are nonnegative; upwind in degenerate tails.
        lo=diff/h**2-drift/(2*h);hi=diff/h**2+drift/(2*h)
        switch=(lo<0)|(hi<0)
        lo[switch]=diff[switch]/h**2+np.maximum(-drift[switch],0)/h
        hi[switch]=diff[switch]/h**2+np.maximum(drift[switch],0)/h
        lo[0]=hi[0]=0;lo[-1]=1/h;hi[-1]=0
        diag=-lo-hi
        return lo,diag,hi
    steps=0
    for target in targets:
        while t>target+1e-10:
            step=min(dt,t-target)
            lo,d,hi=generator(t-step/2)
            weight=1. if steps<4 else .5
            rhs=(1+(1-weight)*step*d)*u
            rhs[1:]+=(1-weight)*step*lo[1:]*u[:-1]
            rhs[:-1]+=(1-weight)*step*hi[:-1]*u[1:]
            ab=np.zeros((3,n+1));ab[1]=1-weight*step*d
            ab[0,1:]=-weight*step*hi[:-1];ab[2,:-1]=-weight*step*lo[1:]
            u=solve_banded((1,1),ab,rhs,overwrite_ab=True,overwrite_b=True,check_finite=False)
            t-=step;steps+=1
        angles=np.arctan(WS)
        out[float(target)]=np.interp(angles,th,u)
    return out

def main():
    begin=time.time();qsol,ints=painleve()
    qa,ia=painleve(-12.,5e-10)
    qdiff=max(abs(qsol.sol(x)[0]-qa.sol(x)[0]) for x in np.linspace(-6.4,5,100))
    xs=np.linspace(-6.4,5,100)
    ham=max(abs(ints.sol(x)[0]-(qsol.sol(x)[1]**2-x*qsol.sol(x)[0]**2-qsol.sol(x)[0]**4)) for x in xs)
    rows=[];metrics={'painleve_left_boundary_refinement_max_q_difference':float(qdiff),'painleve_hamiltonian_max_residual':float(ham),'nice':os.getpriority(os.PRIO_PROCESS,0),'threads':'one BLAS thread'}
    formulas={}
    for beta in [1,2,4]:
        formulas[beta]={(float(t),float(w)):formula(beta,t,w,qsol,ints) for t in TS for w in WS if beta!=1 or np.isinf(w)}
    for beta in [1,2,4]:
        runs=[]
        for n,dt,T in [(600,.004,12),(1200,.002,12),(2400,.001,12),(2400,.001,16)]:
            start=time.time();out=pde(beta,n,dt,T);runs.append(out)
            print('PDE',beta,n,dt,T,'seconds',round(time.time()-start,2),flush=True)
        errors=[];refines=[];terrors=[]
        for t in TS:
            for j,w in enumerate(WS):
                key=(float(t),float(w));exact=formulas[beta].get(key)
                vals=[r[float(t)][j] for r in runs]
                err=abs(vals[2]-exact) if exact is not None else None
                if err is not None:errors.append(err)
                refines.append(abs(vals[2]-vals[1]));terrors.append(abs(vals[3]-vals[2]))
                rows.append({'beta':beta,'t':float(t),'w':'inf' if np.isinf(w) else float(w),'pde_n600':vals[0],'pde_n1200':vals[1],'pde_n2400':vals[2],'pde_T16':vals[3],'painleve_control':exact,'abs_error':err,'is_Mo_evaluation':False})
        metrics[str(beta)]={'points':len(TS)*len(WS),'control_points':len(errors),'max_control_abs_error_n2400':float(max(errors)),'max_n1200_n2400_difference':float(max(refines)),'max_T12_T16_difference':float(max(terrors)),'coarse_control_max_errors':[float(max(abs(r[float(t)][j]-formulas[beta][(float(t),float(w))]) for t in TS for j,w in enumerate(WS) if (float(t),float(w)) in formulas[beta])) for r in runs[:3]]}
    with (ROOT/'data/pde_comparison.csv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    metrics['seconds']=time.time()-begin;metrics['maxrss_bytes_macos']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    (ROOT/'data/numerics_summary.json').write_text(json.dumps(metrics,indent=2))
    print(json.dumps(metrics,indent=2),flush=True)
if __name__=='__main__':main()
