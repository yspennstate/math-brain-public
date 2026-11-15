"""Independent referee checks; no code or data imports from claim_files.

One numerical thread. Exact substitutions, numerical orbit screens, and an
outer state-space search whose inner problem is a linear program in the tensor.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import itertools
import json
import math
from pathlib import Path
import resource
import sys
import time
import numpy as np
import sympy as s
from scipy.optimize import differential_evolution, linprog, minimize

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'data'
OUT.mkdir(exist_ok=True)
RNG = np.random.default_rng(130065)

def bounds(m):
    return ((1 - 1/math.sqrt(m+1))/(2*m),
            2/(3*m+2+math.sqrt(m*m+12*m+4)))

def pairs(m):
    return list(itertools.combinations_with_replacement(range(m), 2))

def weights(x):
    return np.array([x[i]*x[j]*(1 if i == j else 2) for i,j in pairs(len(x))])

def image(P, x):
    # This scalar summation also audits the vectorized LP formulation.
    return np.array([math.fsum(float(P[r,k])*float(x[i])*float(x[j])*
                    (1 if i == j else 2) for r,(i,j) in enumerate(pairs(len(x))))
                    for k in range(len(x))])

def family(m, floor, exact=False):
    one = s.Integer(1) if exact else 1.0
    t = one - m*floor
    P = [[floor]*m for _ in pairs(m)]
    for row,(i,j) in zip(P, pairs(m)):
        ci = 'A' if i == 0 else ('C' if i == 2 else 'B')
        cj = 'A' if j == 0 else ('C' if j == 2 else 'B')
        cc = sorted((ci,cj))
        k = 2 if cc in [['A','A'],['A','B']] else (
            0 if cc in [['C','C'],['B','C']] else 1)
        row[k] += t
    z = one/t-one
    total = one-z
    rad = total**2-4*floor/t
    root = s.sqrt(rad) if exact else math.sqrt(float(rad))
    u,v = (total+root)/2,(total-root)/2
    x = [u,z-(m-3)*floor,v]+[floor]*(m-3)
    y = [v,z-(m-3)*floor,u]+[floor]*(m-3)
    return P,x,y

def exact_checks():
    x,a,b,c = s.symbols('x a b c', real=True)
    A,B = a-2*b+c,2*(b-c)
    f = a*x*x+2*b*x*(1-x)+c*(1-x)**2
    g = s.expand(f-x)
    D = s.discriminant(g,x)
    H = A*A*x*x+A*(B+1)*x+A*c+B+1
    tests = {}
    tests['discriminant'] = s.simplify(D-((2*b-1)**2+4*c*(1-a))) == 0
    tests['factorization'] = s.expand(f.subs(x,f)-x-g*H) == 0
    tests['square_completion'] = s.expand(H-(A*x+(B+1)/2)**2-(4-D)/4) == 0
    d = s.symbols('d', positive=True)
    ds = (3-s.sqrt(7))/4
    tests['binary_threshold'] = s.simplify((5-12*d+8*d*d-4).subs(d,ds)) == 0
    t = 1-2*d
    xp = (2*t-1+s.sqrt(4*t*(1-d)-3))/(2*t)
    xm = (2*t-1-s.sqrt(4*t*(1-d)-3))/(2*t)
    fd = d+t*(1-x)**2
    tests['binary_cycle_plus'] = s.simplify(fd.subs(x,xp)-xm) == 0
    tests['binary_cycle_minus'] = s.simplify(fd.subs(x,xm)-xp) == 0
    tests['binary_endpoint_H_double_root'] = s.simplify((4-(5-12*d+8*d*d)).subs(d,ds)) == 0
    m,tt = s.symbols('m tt', positive=True)
    ell = (1-tt)/m
    tests['general_cycle_discriminant'] = s.factor((2-1/tt)**2-4*ell/tt-((m+1)*(2*tt-1)**2-1)/(m*tt**2)) == 0
    C = 2/(3*m+2+s.sqrt(m*m+12*m+4))
    tests['upper_root'] = s.simplify(2*m*m*C*C-(3*m+2)*C+1) == 0
    tests['C2'] = s.simplify(C.subs(m,2)-(2-s.sqrt(2))/4) == 0
    cases = []
    for mm,dd in [(3,s.Rational(2,25)),(4,s.Rational(11,160)),(5,s.Rational(7,120))]:
        P,xx,yy = family(mm,dd,True)
        vv = lambda state: [s.simplify(sum(P[r][k]*state[i]*state[j]*(1 if i==j else 2)
                                       for r,(i,j) in enumerate(pairs(mm)))) for k in range(mm)]
        residuals = [s.simplify(v-w) for v,w in zip(vv(xx)+vv(yy), yy+xx)]
        tests[f'cycle_{mm}'] = all(v == 0 for v in residuals)
        tests[f'rows_{mm}'] = all(s.simplify(sum(row)-1)==0 for row in P)
        tests[f'points_{mm}'] = s.simplify(sum(xx)-1)==0 and all(v>0 for v in xx) and xx!=yy
        # Independently differentiate the reduced map and multiply Jacobians.
        ddvar,zz = s.symbols('ddvar zz')
        tv = 1-mm*dd
        F = s.Matrix([-tv*(1+zz)*ddvar,
                      (mm-2)*dd+tv*(zz**2+((1-zz)**2-ddvar**2)/2)])
        J = F.jacobian([ddvar,zz])
        zzv = sum(xx[i] for i in range(mm) if i not in (0,2))
        diff = xx[0]-xx[2]
        M = s.simplify(J.subs({ddvar:-diff,zz:zzv})*J.subs({ddvar:diff,zz:zzv}))
        trace,det = s.simplify(s.trace(M)),s.simplify(M.det())
        schur = [s.simplify(1-trace+det), s.simplify(1+trace+det),s.simplify(1-det)]
        tests[f'attracting_{mm}'] = all(v>0 for v in schur)
        cases.append(dict(m=mm,floor=str(dd),X=list(map(str,xx)),Y=list(map(str,yy)),
                          entries=sorted(set(str(v) for row in P for v in row)),
                          trace=str(trace),determinant=str(det),schur=list(map(str,schur))))
    assert all(tests.values()), tests
    return dict(tests=tests,cases=cases)

def binary_numerics():
    critical = (3-math.sqrt(7))/4
    delta_list = [0.02,critical-1e-4,critical+1e-4,0.12,0.2,0.4]
    results = []
    for delta in delta_list:
        abc = RNG.uniform(delta,1-delta,(1500,3))
        abc[:8] = np.array(list(itertools.product([delta,1-delta],repeat=3)))
        x = np.broadcast_to(np.linspace(0,1,9),(len(abc),9)).copy()
        aa,bb,cc = [abc[:,i,None] for i in range(3)]
        def fun(xx): return aa*xx*xx+2*bb*xx*(1-xx)+cc*(1-xx)**2
        iterations = 100000 if abs(delta-critical) < 0.001 else 15000
        for _ in range(iterations):
            x = fun(x)
        step = np.max(np.abs(fun(x)-x),axis=1)
        cycle = np.max(np.abs(fun(fun(x))-x),axis=1)
        disc = (2*abc[:,1]-1)**2+4*abc[:,2]*(1-abc[:,0])
        results.append(dict(delta=delta,operators=len(abc),starts_each=9,iterations=iterations,
                            max_D=float(disc.max()),max_step=float(step.max()),
                            nonconverged=int(sum(step>1e-6)),
                            proper_cycles=int(sum((cycle<1e-9)&(step>1e-5)))))
        (OUT/'binary_partial.json').write_text(json.dumps(results,indent=2))
        if delta>critical:
            assert step.max()<1e-6, results[-1]
    # Endpoint is slow: use exact identities for convergence, never a finite-step verdict.
    return dict(critical=critical,grid=results,endpoint_numerics_not_used=True)

def metric_numerics():
    maxima = [0.,0.]
    for m in [2,3,4,5,10]:
        for rep in range(350):
            x = RNG.dirichlet(np.ones(m)*0.6)
            h = RNG.normal(size=m); h -= h.mean()
            Q = RNG.dirichlet(np.ones(m)*0.4, size=len(pairs(m)))
            if rep%3==0:
                Q = np.eye(m)[RNG.integers(m,size=len(pairs(m)))]
            q = image(Q,x)
            dw = np.array([math.fsum(Q[r,k]*(h[i]*x[j]+x[i]*h[j])*(1 if i==j else 2)
                                    for r,(i,j) in enumerate(pairs(m))) for k in range(m)])
            mask = q>0
            rhs = 2*sum(h*h/x)
            lhs = sum(dw[mask]**2/q[mask])
            maxima[0] = max(maxima[0],lhs/rhs)
            mu = RNG.uniform(.0001,1/m)
            t = 1-m*mu
            # Constant residual operators have exact derivative zero. Dividing
            # their roundoff-sized derivative energies creates meaningless ratios.
            ratio = (sum(dw*dw/(mu+t*q))*(t+2*mu)/lhs) if lhs>1e-20 else 0
            maxima[1] = max(maxima[1],ratio)
            assert lhs<=rhs*(1+1e-10) and ratio<=1+1e-10, dict(m=m,rep=rep,q=q,dw=dw,lhs=lhs,rhs=rhs,ratio=ratio)
    return dict(checks=1750,max_lemma1_ratio=maxima[0],max_lemma2_ratio=maxima[1])

def random_orbits():
    report=[]
    for m in [3,4]:
        L,C=bounds(m)
        for floor in [L+1e-4,(L+C)/2,C+1e-4]:
            for concentration in [.04,.4,2.]:
                n=240
                q=RNG.dirichlet(np.full(m,concentration),size=(n,len(pairs(m))))
                # Also sample vertices of the residual coefficient polytope.
                q[:80]=np.eye(m)[RNG.integers(m,size=(80,len(pairs(m))))]
                P=floor+(1-m*floor)*q
                starts=np.concatenate([np.eye(m),RNG.dirichlet(np.ones(m),4)])
                x=np.broadcast_to(starts,(n,len(starts),m)).copy()
                def fun(xx):
                    w=np.stack([xx[:,:,i]*xx[:,:,j]*(1 if i==j else 2) for i,j in pairs(m)],axis=2)
                    yy=np.einsum('nsr,nrk->nsk',w,P,optimize=False)
                    assert np.isfinite(yy).all() and np.min(yy)>=0
                    # The homogeneous polynomial has normal multiplier 2 at
                    # sum(x)=1. Project roundoff back to the invariant simplex.
                    return yy/yy.sum(axis=2,keepdims=True)
                for _ in range(1200): x=fun(x)
                one=fun(x);two=fun(one)
                step=np.max(abs(one-x),axis=(1,2))
                diameter=np.max(np.ptp(x,axis=1),axis=1)
                initial_flags=int(sum((step>1e-7)|(diameter>1e-7)))
                # Near a flip bifurcation finite-time alternation is not a
                # certificate. Continue only the flagged tensors much longer.
                followup=[]
                for index in np.flatnonzero((step>1e-7)|(diameter>1e-7)):
                    state=x[index].copy();tensor=P[index]
                    for iteration in range(1,200001):
                        ww=np.stack([state[:,i]*state[:,j]*(1 if i==j else 2) for i,j in pairs(m)],axis=1)
                        nxt=ww@tensor;nxt/=nxt.sum(axis=1,keepdims=True)
                        err=np.max(abs(nxt-state));state=nxt
                        if iteration%500==0 and err<1e-11: break
                    # Verify with scalar sums, separately from continuation.
                    scalar_next=np.array([image(tensor,z) for z in state])
                    scalar_next/=scalar_next.sum(axis=1,keepdims=True)
                    step[index]=np.max(abs(scalar_next-state))
                    diameter[index]=np.max(np.ptp(state,axis=0))
                    x[index]=state
                    followup.append(dict(index=int(index),extra_iterations=iteration,
                        final_step=float(step[index]),final_start_diameter=float(diameter[index]),
                        actual_floor=float(tensor.min()),P=tensor.tolist(),states=state.tolist()))
                count=int(sum((step>1e-7)|(diameter>1e-7)))
                report.append(dict(m=m,requested_floor=floor,concentration=concentration,
                                   operators=n,starts_each=len(starts),iterations=1200,
                                   nonconverged=count,max_step=float(step.max()),
                                   max_start_diameter=float(diameter.max()),
                                   initially_flagged=initial_flags,followup=followup,
                                   min_actual_floor=float(P.min()),
                                   max_two_step=float(np.max(abs(fun(fun(x))-x)))))
                (OUT/'random_partial.json').write_text(json.dumps(report,indent=2))
    return report

def lp_tensor(m,x,y,margin=0.):
    """Max floor over all symmetric stochastic tensors mapping x<->y."""
    pp=pairs(m); r=len(pp); n=r*m+1
    eq=[]; rhs=[]
    for row in range(r):
        z=np.zeros(n);z[row*m:(row+1)*m]=1;eq.append(z);rhs.append(1.)
    for u,target in [(x,y),(y,x)]:
        w=weights(u)
        for k in range(m-1):
            z=np.zeros(n);z[k:r*m:m]=w;eq.append(z);rhs.append(target[k])
    ine=np.zeros((r*m,n));ine[:,:r*m]=-np.eye(r*m);ine[:,-1]=1
    cost=np.zeros(n);cost[-1]=-1
    sol=linprog(cost,A_ub=ine,b_ub=np.zeros(r*m),A_eq=np.array(eq),b_eq=np.array(rhs),
                bounds=[(margin,1)]*(r*m)+[(margin,1/m)],method='highs',
                options={'threads':1,'primal_feasibility_tolerance':1e-9,
                         'dual_feasibility_tolerance':1e-9})
    return sol

def state_pair(parameters,m,gap):
    # Any ordered state pair with x_1-y_1 >= gap is representable.
    x0=gap+(1-gap)*parameters[0]
    y0=(x0-gap)*parameters[1]
    states=[]
    for first,pars in [(x0,parameters[2:m]),(y0,parameters[m:])]:
        tail=[];rem=1-first
        for u in pars:
            tail.append(rem*u);rem*=1-u
        states.append(np.array([first]+tail+[rem]))
    return states

def optimize_cycles():
    reports=[]
    for m in [3,4]:
        for gap in [.04,.008]:
            memo={};calls=0
            def objective(v):
                nonlocal calls
                x,y=state_pair(v,m,gap)
                sol=lp_tensor(m,x,y)
                calls+=1
                return -sol.x[-1] if sol.success else .05
            # Independent outer state-space optimisation; no tensor seed from the claim.
            res=differential_evolution(objective,[(0.,1.)]*(2*m-2),
                  seed=130065+m+int(gap*1000),popsize=9,maxiter=65,tol=2e-6,
                  polish=False,workers=1,updating='immediate')
            local=minimize(objective,res.x,method='Nelder-Mead',
                           options={'maxiter':900,'xatol':1e-9,'fatol':1e-10},
                           bounds=[(0.,1.)]*(2*m-2))
            v=local.x if local.fun<res.fun else res.x
            x,y=state_pair(v,m,gap);sol=lp_tensor(m,x,y)
            rec=dict(m=m,gap_required=gap,lp_calls=calls,success=bool(sol.success))
            if sol.success:
                P=sol.x[:-1].reshape(-1,m);floor=float(sol.x[-1])
                residual=max(np.max(abs(image(P,x)-y)),np.max(abs(image(P,y)-x)))
                rec.update(floor=floor,L=bounds(m)[0],C=bounds(m)[1],
                           state_gap=float(x[0]-y[0]),residual=float(residual),
                           row_residual=float(np.max(abs(P.sum(axis=1)-1))),
                           min_entry=float(P.min()),X=x.tolist(),Y=y.tolist(),P=P.tolist())
                assert residual<2e-8 and P.min()>floor-2e-8
                assert floor<bounds(m)[1]
                # Targeted attempt above both bounds, holding optimized distinct states.
                rec['LP_feasible_floor_L_plus_1e4']=bool(lp_tensor(m,x,y,bounds(m)[0]+1e-4).success)
                rec['LP_feasible_floor_C_plus_1e4']=bool(lp_tensor(m,x,y,bounds(m)[1]+1e-4).success)
            reports.append(rec)
            print(json.dumps(rec),flush=True)
            (OUT/'optimized_cycles.json').write_text(json.dumps(reports,indent=2))
    return reports

def refine_cycles():
    reports=[]
    for record in json.loads((OUT/'optimized_cycles.json').read_text()):
        m=record['m'];r=len(pairs(m));n=r*m
        initial=np.r_[np.array(record['P']).ravel(),record['X'],record['Y'],record['floor']]
        def unpack(z): return z[:n].reshape(r,m),z[n:n+m],z[n+m:n+2*m],z[-1]
        def equality(z):
            P,x,y,_=unpack(z)
            return np.r_[P.sum(axis=1)-1, x.sum()-1, y.sum()-1,
                         weights(x)@P[:,:m-1]-y[:m-1],weights(y)@P[:,:m-1]-x[:m-1]]
        def inequality(z):
            P,x,y,ell=unpack(z)
            return np.r_[P.ravel()-ell,x[0]-y[0]-record['gap_required']]
        sol=minimize(lambda z:-z[-1], initial,method='SLSQP',
            bounds=[(0,1)]*(n+2*m)+[(0,1/m)],
            constraints=[{'type':'eq','fun':equality},{'type':'ineq','fun':inequality}],
            options={'maxiter':1000,'ftol':1e-12})
        P,x,y,ell=unpack(sol.x)
        residual=float(max(abs(equality(sol.x))))
        scalar_residual=float(max(np.max(abs(image(P,x)-y)),np.max(abs(image(P,y)-x))))
        rec=dict(m=m,gap=record['gap_required'],floor=float(ell),L=bounds(m)[0],C=bounds(m)[1],
                 success=bool(sol.success),message=sol.message,iterations=int(sol.nit),
                 residual=residual,scalar_residual=scalar_residual,
                 min_inequality=float(min(inequality(sol.x))),X=x.tolist(),Y=y.tolist(),P=P.tolist())
        reports.append(rec)
        assert residual<1e-8 and scalar_residual<1e-8 and min(inequality(sol.x))>-1e-8
        print(json.dumps(rec),flush=True)
    return reports

if __name__=='__main__':
    start=time.time()
    which=sys.argv[1] if len(sys.argv)>1 else 'verify'
    if which=='verify':
        output=dict(exact=exact_checks(),binary=binary_numerics(),metric=metric_numerics(),
                    random=random_orbits())
    elif which=='search': output=dict(optimized=optimize_cycles())
    elif which=='refine': output=dict(refined=refine_cycles())
    else: raise ValueError(which)
    output['runtime']=dict(seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        numpy=np.__version__,sympy=s.__version__,seed=130065,threads=1)
    (OUT/(which+'.json')).write_text(json.dumps(output,indent=2))
    print(json.dumps(output,indent=2),flush=True)
