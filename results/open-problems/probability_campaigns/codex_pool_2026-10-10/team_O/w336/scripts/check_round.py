"""Short, reproducible checks; save and stage each completed item immediately."""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, combinations
import json
import math
import random
import time
import numpy as np
from numpy.polynomial import Polynomial as Poly
from package_result import ROOT, IDS, begin, save

def simpson(func, low=-10., high=10., count=16000):
    h=(high-low)/count
    total=func(low)+func(high)
    for i in range(1,count):
        total+=(4 if i%2 else 2)*func(low+i*h)
    return total*h/3

def p0458():
    phi=lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi)
    Phi=lambda z: (1+math.erf(z/math.sqrt(2)))/2
    g=lambda z: phi(z)+z*Phi(z)
    a=1/math.sqrt(math.pi)
    v=1/3+(math.sqrt(3)-2)/(2*math.pi)
    mean=simpson(lambda z: g(z)*phi(z))
    second=simpson(lambda z: g(z)**2*phi(z))
    variance=second-mean*mean
    norm=simpson(phi)
    assert abs(mean-a)<1e-10 and abs(variance-v)<1e-10
    assert abs(norm-1)<1e-10
    inverse_errors=[]
    for z0 in (-4.,-2.,0.,2.,4.):
        value=g(z0); low,high=-10.,10.
        for _ in range(100):
            mid=(low+high)/2
            if g(mid)<value: low=mid
            else: high=mid
        z=(low+high)/2
        inverse_errors.append(abs(z-z0))
        step=1e-5
        assert abs((g(z0+step)-g(z0-step))/(2*step)-Phi(z0))<1e-8
        assert g(z0)>0
    assert max(inverse_errors)<1e-8
    return dict(quadrature_panels=16000,mean=mean,mean_error=abs(mean-a),
                variance=variance,variance_error=abs(variance-v),normalization_error=abs(norm-1),
                upper_endpoint=a/math.sqrt(v),inverse_round_trips=5,max_inverse_error=max(inverse_errors),
                scope='Normal transform proved; prior graph convergence remains a hypothesis.')

def cookie_moments(probabilities, m):
    M=len(probabilities)
    @lru_cache(None)
    def rec(i,k):
        if k==0: return F(0),F(0)
        if i==M: return F(k),F(k*k+2*k)
        p=probabilities[i]
        a,b=rec(i+1,k-1)
        c,d=rec(i+1,k)
        return p*a+(1-p)*(1+c),p*b+(1-p)*(1+2*c+d)
    mean,second=rec(0,m)
    return mean,second-mean*mean

def c0129():
    cases=0
    for M in range(5):
        for probs in product((F(1,4),F(1,2),F(3,4)),repeat=M):
            s=sum(probs,F(0)); t=sum((p*(1-p) for p in probs),F(0))
            delta=2*s-M
            for m in sorted(set((max(1,M),M+1,M+4))):
                mean,var=cookie_moments(probs,m)
                assert mean==m-delta
                assert var==2*(m-s)+4*t
                assert cookie_moments(probs,m+1)[0]-mean==1
                cases+=1
    for probs in [(F(0),F(1),F(0),F(1)),(F(1),)*4,(F(0),)*4]:
        m=4; mean,var=cookie_moments(probs,m)
        s=sum(probs); t=sum(p*(1-p) for p in probs)
        assert mean==m-(2*s-4) and var==2*(m-s)+4*t
        cases+=1
    boundary=cookie_moments((F(3,4),F(3,4)),1)[0]
    assert boundary==F(3,8)
    return dict(exact_rational_moment_cases=cases,max_error='0',boundary_M=2,boundary_m=1,
                actual_boundary_mean=str(boundary),invalid_affine_prediction='0',
                scope='No recurrence/transience criterion or periodic-case certificate.')

def stationary_pi(Q):
    d=len(Q); A=Q.T-np.eye(d); A[-1]=1; b=np.zeros(d); b[-1]=1
    pi=np.linalg.solve(A,b)
    assert np.max(np.abs(pi@Q-pi))<1e-12
    return pi

def urn_cov(Q,p,r,c):
    d=len(Q); f=c*r*r
    assert r+f<=1
    z=np.linalg.solve((r+f)*np.eye(d)-r*Q,f*p)
    s=Q@z; B=(1-r-f)*np.eye(d)+r*Q
    def op(V):
        return V-B@V@B.T+r*r*np.diag(np.diag(Q@V@Q.T))
    cols=[]
    for k in range(d*d):
        E=np.zeros(d*d); E[k]=1
        cols.append(op(E.reshape(d,d)).ravel())
    M=np.column_stack(cols)
    rhs=r*r*np.diag(s*(1-s))
    V=np.linalg.solve(M,rhs.ravel()).reshape(d,d)
    residual=float(np.max(np.abs(op(V)-rhs)))
    assert residual<1e-12
    assert np.max(np.abs(V-V.T))<1e-10
    assert np.linalg.eigvalsh((V+V.T)/2).min()>-1e-10
    return z,V,residual

def scalar_urn_moments(r,c,p,count=4):
    f=c*r*r; a=1-r-f; b=f*p
    base=Poly([b,a]); z=Poly([0.,1.])
    mu=[1.]
    for k in range(1,count+1):
        transition=base**k+z*((base+r)**k-base**k)
        coeff=list(transition.coef)+[0.]*(k+2-len(transition.coef))
        assert abs(coeff[k+1])<1e-12
        mu.append(sum(coeff[j]*mu[j] for j in range(k))/(1-coeff[k]))
    return mu

def p0087():
    rows=[]; max_resid=0.; scalar_checks=0
    for Q,p,c in [(np.array([[.2,.5,.3],[.1,.6,.3],[.4,.2,.4]]),np.array([.2,.7,.4]),1.3),
                  (np.array([[0.,1.],[1.,0.]]),np.array([.2,.7]),.8)]:
        pi=stationary_pi(Q); pbar=float(pi@p); K=float(pi@pi)
        limit=K*pbar*(1-pbar)/(2*c+K)
        errors=[]
        for r in (.2,.1,.05,.025,.0125,.00625):
            mean,V,resid=urn_cov(Q,p,r,c)
            error=float(np.max(np.abs(V-limit)))
            errors.append(error); max_resid=max(max_resid,resid)
            assert abs(float(pi@mean)-pbar)<1e-11
            scalar_identity=(2*c-c*c*r*r)*float(pi@V@pi)
            s=Q@mean
            rhs=float(np.sum(pi*pi*(s*(1-s)-np.diag(Q@V@Q.T))))
            assert abs(scalar_identity-rhs)<1e-10
        assert errors[-1]<errors[0]/15
        rows.append(dict(dimension=len(Q),pi=pi.tolist(),pbar=pbar,K=K,
                         limiting_common_covariance=limit,r_values=[.2,.1,.05,.025,.0125,.00625],
                         max_entry_errors=errors,improvement_factor=errors[0]/errors[-1]))
    c=1.3;p=.37
    beta=[]
    for k in range(1,5):
        value=1.
        for j in range(k): value*= (2*c*p+j)/(2*c+j)
        beta.append(value)
    moment_rows=[]; generator_rows=[]
    for r in (.1,.05,.025,.0125,.00625):
        _,V,resid=urn_cov(np.ones((1,1)),np.array([p]),r,c)
        exact=p*(1-p)/(1+2*c-c*c*r*r)
        assert abs(float(V[0,0])-exact)<1e-11
        mu=scalar_urn_moments(r,c,p)
        assert abs(mu[1]-p)<1e-11
        assert abs(mu[2]-p*p-exact)<1e-10
        moment_rows.append(dict(r=r,moments=mu[1:],candidate_beta_moments=beta,
                                max_moment_error=max(abs(x-y) for x,y in zip(mu[1:],beta))))
        f=c*r*r; gen_error=0.
        for z in np.linspace(0,1,41):
            for k in (2,3,4):
                z0=(1-r-f)*z+f*p; z1=z0+r
                actual=((1-z)*z0**k+z*z1**k-z**k)/(r*r)
                target=c*(p-z)*k*z**(k-1)+.5*z*(1-z)*k*(k-1)*z**(k-2)
                gen_error=max(gen_error,abs(actual-target)); scalar_checks+=1
        generator_rows.append(dict(r=r,max_polynomial_generator_error=gen_error))
    assert moment_rows[-1]['max_moment_error']<moment_rows[0]['max_moment_error']/10
    assert generator_rows[-1]['max_polynomial_generator_error']<generator_rows[0]['max_polynomial_generator_error']/10
    return dict(network_covariance_cases=12,scalar_covariance_cases=5,max_linear_system_residual=max_resid,
                network_limits=rows,scalar_stationary_moments=moment_rows,
                polynomial_generator_checks=scalar_checks,generator_errors=generator_rows,
                scope='Stationary moments and scalar generator only; functional convergence not claimed.')

def p0294():
    tests=0; models=[]
    for lam,mu in [(F(1,5),F(1)),(F(1,2),F(1)),(F(4,5),F(1)),(F(3,4),F(2))]:
        rho=lam/mu; mean=lam/(mu*(mu-lam))
        assert mean==lam*(2/(mu*mu))/(2*(1-rho))
        for s in (F(1,10),F(1),F(3)):
            beta=mu/(mu+s)
            mixture=(1-rho)+rho*(mu-lam)/(mu-lam+s)
            assert s*(mixture-(1-rho))+lam*(beta-1)*mixture==0
            tests+=1
        for N in (1,2,10,100):
            # Joint marked-Poisson exponent factors into independent queue exponents.
            vals=np.linspace(.2,.8,N)
            joint=float(N*float(lam)*(float(vals.mean())-1))
            factored=float(np.sum(float(lam)*(vals-1)))
            assert abs(joint-factored)<1e-12
            tests+=1
        models.append(dict(lam=str(lam),mu=str(mu),stationary_mean=str(mean),finite_N_bias='0'))
    return dict(exact_laplace_generator_checks=12,total_checks=tests,models=models,
                first_order_bias='0 exactly for d=1',scope='Independent random routing, not d>=2.')

def c0020():
    rows=[]; inputs=0
    for N in range(1,13):
        total=0; reveal=[0]*N
        for bits in product((0,1),repeat=N):
            cost=0; out=0
            for i,b in enumerate(bits):
                cost+=1;reveal[i]+=1
                if b: out=1;break
            assert out==int(any(bits))
            total+=cost;inputs+=1
        cost=F(total,2**N)
        assert cost==2*(1-F(1,2**N))
        assert reveal[0]==2**N
        ratio=F(N,1)/cost
        rows.append(dict(N=N,expected_cost=str(cost),first_revealment='1',ratio_to_average=float(ratio)))
    return dict(exhaustive_inputs=inputs,algorithm_sizes=12,largest_ratio_to_average=rows[-1]['ratio_to_average'],
                rows=rows,scope='Refuted uniformity shortcut; no new percolation exponent.')

def c0074():
    rows=[]; max_eigen=0.;max_hit=0.;max_corr=0.
    for n in (7,8,15,16,31,32):
        c=1 if n%2 else 2
        L=np.zeros((n+1,n+1))
        for i in range(n): L[i,i+1]=c;L[i+1,i]=c
        L-=np.diag(L.sum(axis=1))
        u=np.cos(math.pi*(np.arange(n+1)+.5)/(n+1))
        eigen=2*c*(1-math.cos(math.pi/(n+1)))
        max_eigen=max(max_eigen,float(np.max(np.abs(L@u+eigen*u))))
        hitting=np.linalg.solve(-L[:n,:n],np.ones(n))
        hit_error=abs(float(hitting[0])-n*(n+1)/(2*c));max_hit=max(max_hit,hit_error)
        vals,vec=np.linalg.eigh(L); t=.1
        transformed=vec@((vec.T@u)*np.exp(vals*n*n*t))
        correlation=float(u@transformed/(n+1))
        expected=.5*math.exp(-n*n*eigen*t)
        max_corr=max(max_corr,abs(correlation-expected))
        rows.append(dict(n=n,conductance=c,scaled_endpoint_hitting=float(hitting[0]/(n*n)),correlation=correlation))
    assert max_eigen<1e-12 and max_hit<1e-8 and max_corr<1e-12
    limits=[.5*math.exp(-math.pi**2*.1),.5*math.exp(-2*math.pi**2*.1)]
    return dict(path_cases=6,max_eigenvector_residual=max_eigen,max_hitting_error=max_hit,
                max_correlation_error=max_corr,predicted_two_subsequence_correlations=limits,rows=rows,
                scope='Weighted path route check; no IIC counterexample.')

def rational_solve(A,b):
    size=len(b); aug=[list(row)+[b[i]] for i,row in enumerate(A)]
    for k in range(size):
        pivot=next(i for i in range(k,size) if aug[i][k])
        aug[k],aug[pivot]=aug[pivot],aug[k]
        scale=aug[k][k];aug[k]=[v/scale for v in aug[k]]
        for i in range(size):
            if i!=k and aug[i][k]:
                scale=aug[i][k]
                aug[i]=[v-scale*w for v,w in zip(aug[i],aug[k])]
    return [row[-1] for row in aug]

def cover_oracle(adj):
    n=len(adj);full=(1<<n)-1
    values={full:{u:F(0) for u in range(n)}}
    for S in sorted(range(1,full),key=int.bit_count,reverse=True):
        verts=[u for u in range(n) if S>>u&1]
        A=[[F(int(i==j)) for j in range(len(verts))] for i in range(len(verts))]
        b=[F(1) for _ in verts]
        index={u:i for i,u in enumerate(verts)}
        for i,u in enumerate(verts):
            prob=F(1,len(adj[u]))
            for v in adj[u]:
                if v in index: A[i][index[v]]-=prob
                else: b[i]+=prob*values[S|(1<<v)][v]
        result=rational_solve(A,b)
        for i in range(len(verts)):
            assert sum(A[i][j]*result[j] for j in range(len(verts)))==b[i]
        values[S]=dict(zip(verts,result))
    return [values[1<<u][u] for u in range(n)]

def connected(adj):
    seen={0};stack=[0]
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:seen.add(v);stack.append(v)
    return len(seen)==len(adj)

def graph(n,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    return adj

def harmonic(n): return sum((F(1,j) for j in range(1,n+1)),F(0))

def c0116():
    small=0;controls=0;records=[]
    for n in range(2,5):
        edges=list(combinations(range(n),2))
        for mask in range(1<<len(edges)):
            adj=graph(n,[e for i,e in enumerate(edges) if mask>>i&1])
            if connected(adj):
                result=cover_oracle(adj)
                assert min(result)>=n-1
                small+=1
    for n in range(2,8):
        complete=cover_oracle(graph(n,list(combinations(range(n),2))))
        expected=(n-1)*harmonic(n-1)
        assert complete==[expected]*n;controls+=1
        L=n-1
        path=cover_oracle(graph(n,[(i,i+1) for i in range(L)]))
        assert path==[F(L*L+i*(L-i)) for i in range(n)];controls+=1
        k=n-1
        star=cover_oracle(graph(n,[(0,i) for i in range(1,n)]))
        expected_star=[2*k*harmonic(k)-1]+[F(1) if k==1 else 2*k*harmonic(k-1)]*k
        assert star==expected_star;controls+=1
        records.append(dict(n=n,complete=str(expected),path_worst=str(max(path)),star_worst=str(max(star))))
    cycles=[]
    for n in (5,6,7):
        answer=cover_oracle(graph(n,[(i,(i+1)%n) for i in range(n)]))
        assert len(set(answer))==1
        cycles.append(dict(n=n,cover_time=str(answer[0])))
    return dict(all_connected_labeled_graphs_n2_to_n4=small,independent_family_controls=controls,
                cycle_oracles=cycles,max_exact_bellman_residual='0',records=records,
                scope='Exponential exact oracle; no polynomial-time algorithm.')

def p0007():
    times=[]
    for k in range(64):
        angle=2*math.pi*k/64;vx=math.cos(angle);vy=math.sin(angle)
        if abs(vx)<1e-12:
            t=2/abs(vy)
        elif vx<0:
            t=2/(-vx)
        else:
            a=vx*vx;b=vy-2*vx;disc=math.sqrt(b*b+4*a)
            root=(b+disc)/(2*a) if b>=0 else 2/(disc-b)
            t=root*1.01+1
        x=1+t*vx;y=1+t*vy
        assert not (x>0 and abs(y-x*x)<1)
        times.append(t)
    assert abs(5-2**2)>=1
    return dict(angle_grid=64,all_grid_rays_exit=True,largest_checked_exit_time=max(times),
                nonconvex_pair=[[1,1],[3,9]],midpoint=[2,5],
                scope='Geometric corridor and convex special case; no trapping mirror configuration.')

def p0034():
    trials=200;steps=2000;records=[];all_steps=0
    for seed in range(trials):
        rng=random.Random(seed)
        hs=[1 if rng.getrandbits(1) else -1 for _ in range(steps)]
        vs=[1 if rng.getrandbits(1) else -1 for _ in range(steps)]
        H=V=x=y=0;departed=set();hzeros=vzeros=0
        for _ in range(steps):
            pos=(x,y)
            if pos not in departed:
                departed.add(pos);x+=hs[H];H+=1
                hzeros+=int(x==0)
            else:
                y+=vs[V];V+=1
                vzeros+=int(y==0)
            all_steps+=1
        assert H==len(departed) and H+V==steps
        assert x==sum(hs[:H]) and y==sum(vs[:V])
        records.append(dict(H=H,V=V,horizontal_stream_zero_visits=hzeros,vertical_stream_zero_visits=vzeros))
    return dict(trials=trials,steps_per_trial=steps,pathwise_steps=all_steps,
                min_horizontal_clock=min(r['H'] for r in records),max_horizontal_clock=max(r['H'] for r in records),
                min_vertical_clock=min(r['V'] for r in records),max_vertical_clock=max(r['V'] for r in records),
                time_change_mismatches=0,distinct_departure_mismatches=0,
                scope='Construction checks only; no finite-simulation recurrence conclusion.')

CHECKS={'P0458':p0458,'C0129':c0129,'P0087':p0087,'P0294':p0294,'C0020':c0020,
        'C0074':c0074,'C0116':c0116,'P0007':p0007,'P0034':p0034}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--only',choices=list(CHECKS))
    parser.add_argument('--check-only',action='store_true',help='Run checks without staging or editing drafts.')
    args=parser.parse_args()
    for pid in ([args.only] if args.only else IDS[1:]):
        if not args.check_only: begin(pid)
        start=time.perf_counter()
        metrics=CHECKS[pid]()
        metrics['seconds']=round(time.perf_counter()-start,4)
        if args.check_only:
            print(json.dumps(dict(problem=pid,metrics=metrics)),flush=True)
        else:
            save(pid,metrics)
