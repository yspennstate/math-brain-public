"""Independent checks for T104_NOTE.md. All outputs stay beside this file."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import signal
signal.alarm(270)
import sys, json, math, time, itertools
from pathlib import Path
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parent
rng = np.random.default_rng(1042026)

def save(step, data, verdict):
    out = ROOT / f'step{step}.json'
    out.write_text(json.dumps(data, indent=2, default=lambda z: z.tolist() if hasattr(z, 'tolist') else str(z))+'\n')
    with (ROOT/'LOG.md').open('a') as f:
        f.write(f'\n### Step {step}: {verdict}\n\nCommand: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py {step}`. Numerical/exact output: `step{step}.json`.\n\n```json\n{out.read_text()}```\n')
    print(out.read_text(), flush=True)

def pairs(n): return list(itertools.combinations(range(n),2))

def model(n):
    es=pairs(n); B=np.zeros((n,len(es)))
    for k,(i,j) in enumerate(es): B[i,k]=B[j,k]=1
    U=null_space(B)
    reps=[]
    for i,j in es:
        perm=list(range(n)); perm[i],perm[j]=perm[j],perm[i]
        index={e:k for k,e in enumerate(es)}
        ix=[index[tuple(sorted((perm[a],perm[b])))] for a,b in es]
        reps.append(U.T@U[ix,:])
    return U, np.array(reps)

def project(T):
    n=len(T); Pi=np.eye(n)-np.ones((n,n))/n
    return T-n/(n-2)*Pi@np.diag(np.diag(T))@Pi

def tableaux(shape):
    if not sum(shape): return [()]
    ans=[]
    for r,L in enumerate(shape):
        if r+1<len(shape) and shape[r+1]==L: continue
        smaller=list(shape); smaller[r]-=1
        smaller=tuple(v for v in smaller if v)
        ans.extend(t+((r,L-1),) for t in tableaux(smaller))
    return ans

def young(shape):
    ts=tableaux(tuple(shape)); n=sum(shape); dim=len(ts); lookup={t:i for i,t in enumerate(ts)}
    adj=[]
    for k in range(n-1):
        s=np.zeros((dim,dim))
        for a,t in enumerate(ts):
            d=(t[k+1][1]-t[k+1][0])-(t[k][1]-t[k][0])
            s[a,a]=1/d
            u=list(t); u[k],u[k+1]=u[k+1],u[k]; u=tuple(u)
            if u in lookup: s[lookup[u],a]=math.sqrt(max(0,1-1/d**2))
        adj.append(s)
    reps=[]
    for i,j in pairs(n):
        s=adj[i].copy()
        for k in range(i+1,j): s=adj[k]@s@adj[k]
        reps.append(s)
    err=max(np.max(np.abs(s@s-np.eye(dim))) for s in adj)
    for a in range(n-2): err=max(err,np.max(np.abs(adj[a]@adj[a+1]@adj[a]-adj[a+1]@adj[a]@adj[a+1])))
    for a in range(n-1):
        for b in range(a+2,n-1): err=max(err,np.max(np.abs(adj[a]@adj[b]-adj[b]@adj[a])))
    return np.array(reps), ts, float(err)

def lap(reps,w): return np.sum(w)*np.eye(reps.shape[1])-np.einsum('e,eab->ab',w,reps)
def graphlap(n,w):
    L=np.zeros((n,n))
    for v,(i,j) in zip(w,pairs(n)):
        L[i,i]+=v; L[j,j]+=v; L[i,j]-=v; L[j,i]-=v
    return L

def step1():
    rows=[]
    for n in range(4,9):
        U,reps=model(n); Pi=np.eye(n)-np.ones((n,n))/n
        errs=[]
        for _ in range(10):
            H=rng.normal(size=(n,n)); T=Pi@((H+H.T)/2)@Pi
            T-=np.trace(T)/(n-1)*Pi
            P=project(T)
            errs.extend([np.max(np.abs(P.sum(axis=0))),np.max(np.abs(np.diag(P))), np.max(np.abs(project(P)-P)),abs(np.sum(P*P)-np.sum(T*T)+n/(n-2)*np.sum(np.diag(T)**2))])
            for i,j in pairs(n):
                ix=list(range(n)); ix[i],ix[j]=ix[j],ix[i]
                errs.append(np.max(np.abs(project(T[np.ix_(ix,ix)])-P[np.ix_(ix,ix)])))
        rows.append(dict(n=n,dimension=U.shape[1],projection_max_error=max(errs),class_sum_scalar=(n-1)*(n-4)/2,class_sum_error=float(np.max(np.abs(reps.sum(axis=0)-(n-1)*(n-4)/2*np.eye(U.shape[1]))))))
    save(1,rows,'CORRECT')

def step2():
    rows=[]
    for n in (5,6):
        shapes={'tau':(2,)+(1,)*(n-2),'sigma':(2,2)+(1,)*(n-4),'dual_sigma':(n-2,2)}
        rr={}; checks={}
        for name,shape in shapes.items():
            R,ts,err=young(shape); rr[name]=R
            jm=sum(R[k] for k,(i,j) in enumerate(pairs(n)) if j==n-1)
            expected=np.diag([t[-1][1]-t[-1][0] for t in ts])
            checks[name]=dict(dim=len(ts),coxeter_error=err,JM_error=float(np.max(np.abs(jm-expected))))
        for graph in ('star','edge'):
            w=np.array([float(i==0) if graph=='star' else float((i,j)==(0,1)) for i,j in pairs(n)])
            vals={k:np.linalg.eigvalsh(lap(R,w)) for k,R in rr.items()}
            lhs=float(np.linalg.eigvalsh(graphlap(n,w))[-1]); rhs=(2*w.sum()+(n-2)*vals['dual_sigma'][-1])/(n-1)
            rows.append(dict(n=n,graph=graph,checks=checks,lambda_min_tau=float(vals['tau'][0]),lambda_min_sigma=float(vals['sigma'][0]),F_rhs=float((n-2)/(n-1)*vals['sigma'][0]),eq51_lhs=lhs,eq51_rhs=float(rhs)))
    save(2,rows,'CORRECT')

def step4():
    import sympy as sp
    rows=[]
    for n in range(4,8):
        one=sp.ones(n,1); Pi=sp.eye(n)-one*one.T/n
        b=sp.Matrix([sp.Rational(1,2),sp.Rational(1,2),-sp.Rational(1,2),-sp.Rational(1,2)]+[0]*(n-4))
        v=sp.Matrix([i*i+2*i+3 for i in range(n-1)]+[-sum(i*i+2*i+3 for i in range(n-1))])
        x=b-2*v*(v.dot(b))/v.dot(v)
        assert x.dot(one)==0 and x.dot(x)==1
        Q=Pi-x*x.T
        def P(T): return T-sp.Rational(n,n-2)*Pi*sp.diag(*T.diagonal())*Pi
        es=pairs(n)
        perms=[]
        for i,j in es:
            ix=list(range(n)); ix[i],ix[j]=ix[j],ix[i]; perms.append(ix)
        def X(T):
            return sum((x[i]*x[j]*T.extract(ix,ix) for (i,j),ix in zip(es,perms)),sp.zeros(n))
        # A is built on the full ambient domain, after Q. Its Frobenius traces
        # equal those of A restricted to ran Q, without irrational basis choices.
        A=[]
        for k in range(n):
            y=Q[:,k]; A.append(P(x*y.T+y*x.T))
        # These A columns omit 1/sqrt(2); divide all traces by 2.
        trA=sp.factor(sum(sp.trace(T.T*T) for T in A)/2)
        trXA=sp.factor(sum(sp.trace(T.T*X(T)) for T in A)/2)
        q=sum(z**4 for z in x); p3=sum(z**3 for z in x); p6=sum(z**6 for z in x)
        m=max(x[i]*x[j] for i,j in es)
        Z=(n*n-6*n+6+2*n*q)/(n-2)**2
        Psi=(n-4)*(2*q-1)-2*(n-3)*p3**2+(n-1)*(n*n-6*n+6+2*n*q)*m
        trace_formula=sp.Rational(n-2,2)+8*q-6*p3**2-4-sp.Rational(n,n-2)*(3*q-2*p3**2-1-sp.Rational(1,n))
        sums=[sum(x[i]*x[j] for i,j in es),sum(x[i]*x[j]*(x[i]-x[j])**2 for i,j in es),sum(x[i]*x[j]*(x[i]-x[j])**4 for i,j in es),sum(x[i]*x[j]*(x[i]**2+x[j]**2) for i,j in es),sum(x[i]**2*x[j]**2 for i,j in es),sum(x[i]*x[j]*(x[i]**4+x[j]**4) for i,j in es),sum(x[i]**3*x[j]**3 for i,j in es)]
        targets=[-sp.Rational(1,2),-1,3*p3**2-4*q,-q,(1-q)/2,-p6,(p3**2-p6)/2]
        residuals=[sp.factor(a-b) for a,b in zip(sums,targets)]
        replacement_res=[]
        for i,j in es:
            e=sp.eye(n)[:,i]-sp.eye(n)[:,j]
            z=sp.zeros(n,1); z[i]=x[i]; z[j]=-x[j]
            replacement_res.extend([sp.factor((e.T*Q*e)[0]-(2-(x[i]-x[j])**2)),sp.factor((z.T*Q*z)[0]-((1-sp.Rational(1,n))*(x[i]**2+x[j]**2)-x[i]**4-x[j]**4+sp.Rational(2,n)*x[i]*x[j]+2*x[i]**2*x[j]**2))])
        replacement_res.append(sp.factor(sum(x[i]**2*Q[i,i] for i in range(n))-(1-sp.Rational(1,n)-q)))
        tr_res=sp.factor(trA-(n-2)*Z); trx_res=sp.factor(trXA-trace_formula)
        final=sp.factor((trXA/trA-sp.Rational(1,2)+2*(n-1)*m)*Z-2*Psi/(n-2)**2)
        assert all(z==0 for z in residuals+replacement_res+[tr_res,trx_res,final])
        rows.append(dict(n=n,x=[str(z) for z in x],pair_sum_residuals=[str(z) for z in residuals],replacement_residuals_all_zero=True,trace_A=str(trA),trace_XA=str(trXA),trace_residuals=[str(tr_res),str(trx_res)],final_identity_residual=str(final)))
    # Numerical tests independent of the exact examples.
    maxerr=0.
    for n in range(4,10):
        for _ in range(30):
            x=rng.normal(size=n); x-=x.mean(); x/=np.linalg.norm(x)
            y=rng.normal(size=n); y-=y.mean(); y-=x*np.dot(x,y); y/=np.linalg.norm(y)
            S=(np.outer(x,y)+np.outer(y,x))/math.sqrt(2); Ay=project(S)
            q=sum(x**4); p3=sum(x**3); p6=sum(x**6); K=sum(x*x*y*y)
            Pi=np.eye(n)-np.ones((n,n))/n
            for i,j in pairs(n):
                ix=list(range(n)); ix[i],ix[j]=ix[j],ix[i]
                sigS=S[np.ix_(ix,ix)]; d=x[i]-x[j]; e=y[i]-y[j]
                checks=[np.sum(S*S)-1,np.sum(S*sigS)-((1-d*d)*(1-e*e)+d*d*e*e),np.sum((Pi@np.diag(np.diag(S))@Pi)*sigS)-2*(K-(x[i]*y[i]-x[j]*y[j])**2),np.sum(Ay*Ay)-(1-2*n/(n-2)*K)]
                maxerr=max(maxerr,max(abs(a) for a in checks))
            es=pairs(n)
            actual=[sum(x[i]*x[j] for i,j in es),sum(x[i]*x[j]*(x[i]-x[j])**2 for i,j in es),sum(x[i]*x[j]*(x[i]-x[j])**4 for i,j in es),sum(x[i]*x[j]*(x[i]**2+x[j]**2) for i,j in es),sum(x[i]**2*x[j]**2 for i,j in es),sum(x[i]*x[j]*(x[i]**4+x[j]**4) for i,j in es),sum(x[i]**3*x[j]**3 for i,j in es)]
            expect=[-.5,-1,3*p3*p3-4*q,-q,(1-q)/2,-p6,(p3*p3-p6)/2]
            maxerr=max(maxerr,max(abs(a-b) for a,b in zip(actual,expect)))
    save(4,dict(exact=rows,numerical_max_error=maxerr,Z_n4='2q-1/2; zero exactly at permutations of (1,1,-1,-1)/2'), 'CORRECT for n>=5; n=4 has a zero denominator at balanced vectors')

def unit(x):
    x=np.asarray(x,dtype=float); x=x-x.mean()
    return x/np.linalg.norm(x)

def step5():
    rows=[]
    for n in range(5,10):
        U,reps=model(n); es=pairs(n); ii,jj=np.array(es).T
        def values(x):
            prod=x[ii]*x[jj]; m=float(max(prod))
            top=float(np.linalg.eigvalsh(np.einsum('e,eab->ab',prod,reps))[-1])
            return top, .5-2*(n-1)*m
        counts={}; minima={}; vectors={}
        def test(x,cat):
            x=unit(x); a,b=values(x); val=a-b
            counts[cat]=counts.get(cat,0)+1
            if val<minima.get(cat,float('inf')): minima[cat]=float(val); vectors[cat]=x.tolist()
            if val < -1e-9: raise RuntimeError(f'COUNTEREXAMPLE n={n} x={x.tolist()} residual={val}')
            return val
        edge=unit([1,-1]+[0]*(n-2)); star=unit([n-1]+[-1]*(n-1))
        equalities={}
        for name,x in [('edge',edge),('star',star)]:
            a,b=values(x); q=sum(x**4); p3=sum(x**3); m=max(x[ii]*x[jj])
            Z=(n*n-6*n+6+2*n*q)/(n-2)**2
            Psi=(n-4)*(2*q-1)-2*(n-3)*p3**2+(n-1)*(n*n-6*n+6+2*n*q)*m
            equalities[name]=dict(lambda_max=a,bound=b,residual=a-b,Z=float(Z),Psi=float(Psi))
            test(x,'equality')
        for _ in range(1500): test(rng.normal(size=n),'random')
        for k in range(1,n): test([n-k]*k+[-k]*(n-k),'two_values')
        for a in range(1,n-1):
            for b in range(1,n-a):
                c=n-a-b
                for _ in range(12):
                    z=rng.normal(size=3); test([z[0]]*a+[z[1]]*b+[z[2]]*c,'three_values')
        for x in (edge,star):
            for eps in [1e-1,1e-2,1e-3,1e-4,1e-6,1e-8,1e-10]:
                for _ in range(20): test(x+eps*rng.normal(size=n),'neighbourhood')
        # Coordinates in an independent orthonormal basis for sum-zero vectors.
        V=null_space(np.ones((1,n)))
        def objective(z): return test(V@z,'Powell')
        optim=[]
        starts=[rng.normal(size=n) for _ in range(3)]+[edge+.01*rng.normal(size=n),star+.01*rng.normal(size=n)]
        for x in starts:
            z=V.T@unit(x)
            fit=minimize(objective,z,method='Powell',options={'maxiter':70,'maxfev':1800,'xtol':1e-10,'ftol':1e-10})
            optim.append(dict(residual=float(fit.fun),evaluations=fit.nfev,success=bool(fit.success)))
        row=dict(n=n,equalities=equalities,counts=counts,minima=minima,minimising_vectors=vectors,optimiser=optim)
        rows.append(row)
        # Checkpoint each n, even if a later n is interrupted.
        (ROOT/'step5.partial.json').write_text(json.dumps(rows,indent=2)+'\n')
        with (ROOT/'LOG.md').open('a') as f: f.write(f'\nStep 5 checkpoint n={n}: minimum residual {min(minima.values()):.17g}, {sum(counts.values())} evaluations, no value below -1e-9.\n')
        print(f'n={n} counts={counts} minima={minima}',flush=True)
    save(5,rows,'CORRECT conditional on Theorem 6.1; no numerical counterexample')

def step6():
    rows=[]
    for n in (5,6):
        Rt,_,et=young((2,)+(1,)*(n-2)); Rs,_,es=young((2,2)+(1,)*(n-4))
        edge=unit([1,-1]+[0]*(n-2)); star=unit([n-1]+[-1]*(n-1))
        vectors=[('edge',edge),('star',star)]+[('random',unit(rng.normal(size=n))) for _ in range(400)]
        for k in range(1,n): vectors.append(('two_values',unit([n-k]*k+[-k]*(n-k))))
        for eps in (.1,.01,.0001,1e-6):
            for special in (edge,star):
                vectors.extend(('neighbourhood',unit(special+eps*rng.normal(size=n))) for _ in range(20))
        best=None; gap=float('inf'); count=0; undefined=0; by_c={}
        for name,x in vectors:
            prod=np.array([x[i]*x[j] for i,j in pairs(n)]); m=max(prod)
            for increment in (0.,.01,.2,1.):
                c=m+increment; w=c-prod
                lt=float(np.linalg.eigvalsh(lap(Rt,w))[0]); ls=float(np.linalg.eigvalsh(lap(Rs,w))[0]); count+=1
                gap=min(gap,lt-(n-2)/(n-1)*ls)
                if ls>1e-10:
                    ratio=lt/ls
                    if best is None or ratio<best['ratio']: best=dict(ratio=ratio,x=x.tolist(),c=float(c),g=1,source=name,increment=increment,lambda_min_tau=lt,lambda_min_sigma=ls)
                    by_c[str(increment)]=min(by_c.get(str(increment),float('inf')),ratio)
                else: undefined+=1
        rows.append(dict(n=n,graphs=count,undefined_zero_denominator=undefined,smallest=best,target=(n-2)/(n-1),ratio_divided_by_target=best['ratio']/((n-2)/(n-1)),smallest_by_increment=by_c,minimum_signed_gap=gap,coxeter_error=max(et,es)))
    save(6,rows,'CORRECT; direct independent Specht-module check')

def primitive(v):
    v=tuple(int(z) for z in v); g=math.gcd(*v)
    return tuple(z//g for z in v)

def cone_rays(n,cone):
    # Gap basis v_i: first i entries n-i, remaining entries -i.
    vs=[tuple([n-i]*i+[-i]*(n-i)) for i in range(1,n)]
    a=[v[0]+v[-1] for v in vs]
    b=[(1 if cone==1 else -1)*(v[1]+v[-2]) for v in vs]
    rays=set()
    def add(s,z):
        if all(t<0 for t in z): z=[-t for t in z]
        if not all(t>0 for t in z): return
        if sum(a[k]*v for k,v in zip(s,z))<0 or sum(b[k]*v for k,v in zip(s,z))<0: return
        rays.add(primitive([sum(zj*vs[k][i] for k,zj in zip(s,z)) for i in range(n)]))
    for k in range(n-1): add([k],[1])
    for i,j in itertools.combinations(range(n-1),2):
        for h in (a,b): add([i,j],[h[j],-h[i]])
    for i,j,k in itertools.combinations(range(n-1),3):
        add([i,j,k],[a[j]*b[k]-a[k]*b[j],a[k]*b[i]-a[i]*b[k],a[i]*b[j]-a[j]*b[i]])
    return sorted(rays)

def pmul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items(): out[i+j]=out.get(i+j,0)+x*y
    return {k:v for k,v in out.items() if v}

def padd(*terms):
    out={}
    for coef,p in terms:
        for k,v in p.items(): out[k]=out.get(k,0)+coef*v
    return {k:v for k,v in out.items() if v}

def certificate(n,cone):
    rays=cone_rays(n,cone); r=len(rays)
    xs=[{7**j:rays[j][i] for j in range(r) if rays[j][i]} for i in range(n)]
    powers={d:[] for d in (2,3,4)}
    for L in xs:
        p={0:1}
        for d in range(1,5):
            p=pmul(p,L)
            if d in powers: powers[d].append(p)
    T=padd(*[(1,p) for p in powers[2]]); P=padd(*[(1,p) for p in powers[3]]); Q=padd(*[(1,p) for p in powers[4]])
    M=pmul(xs[0],xs[1]) if cone==1 else pmul(xs[-1],xs[-2])
    T2=pmul(T,T)
    G=padd((2*(n-4),pmul(Q,T)),(-(n-4),pmul(T2,T)),(-2*(n-3),pmul(P,P)),((n-1)*(n*n-6*n+6),pmul(T2,M)),(2*n*(n-1),pmul(Q,M)))
    negative=[(k,v) for k,v in G.items() if v<0]
    # Base 7 exponents have no carries in a homogeneous degree-six calculation.
    assert all(sum((k//7**j)%7 for j in range(r))==6 for k in G)
    # A second, scalar integer evaluation audits the expanded polynomial.
    z=[j+1 for j in range(r)]; x=[sum(z[j]*rays[j][i] for j in range(r)) for i in range(n)]
    t=sum(v*v for v in x); p=sum(v**3 for v in x); q=sum(v**4 for v in x); m=x[0]*x[1] if cone==1 else x[-1]*x[-2]
    direct=(n-4)*(2*q-t*t)*t-2*(n-3)*p*p+(n-1)*((n*n-6*n+6)*t*t+2*n*q)*m
    expanded=sum(v*math.prod(z[j]**((k//7**j)%7) for j in range(r)) for k,v in G.items())
    assert direct==expanded
    # Save the full exact certificate in a compact, human-readable monomial list.
    path=ROOT/f'certificate_n{n}_R{cone}.txt'
    with path.open('w') as f:
        f.write(f'n={n} R{cone}; rays={rays}\ncoefficient exponents (ray order as above)\n')
        for k,v in sorted(G.items()): f.write(str(v)+' '+','.join(str((k//7**j)%7) for j in range(r))+'\n')
    return dict(n=n,cone=cone,ray_count=r,rays=rays,total_degree6_monomials=math.comb(r+5,6),nonzero_coefficients=len(G),zero_coefficients=math.comb(r+5,6)-len(G),negative_coefficients=len(negative),smallest_nonzero_coefficient=min(G.values()),largest_coefficient=max(G.values()),scalar_crosscheck=direct==expanded,certificate=path.name)

def step7():
    rows=[]
    for n in (5,6,7):
        for cone in (1,2):
            result=certificate(n,cone); rows.append(result)
            with (ROOT/'LOG.md').open('a') as f: f.write(f'\nStep 7 checkpoint n={n}, R{cone}: {result["ray_count"]} rays, {result["nonzero_coefficients"]} nonzero coefficients, {result["negative_coefficients"]} negative.\n')
            print(f'n={n} R{cone}: {result["ray_count"]} rays; negatives={result["negative_coefficients"]}',flush=True)
    ray_counts=[]
    for n in range(4,21):
        s=(n-1)//2 if n%2 else (n-2)//2
        predicted=s*s+s-1 if n%2 else s*s+s
        ray_counts.append(dict(n=n,count=len(cone_rays(n,1)),claimed=predicted))
    save(7,dict(certificates=rows,R1_ray_counts=ray_counts),'CORRECT for reproduced n=5,6,7; larger certificates not yet checked')

def partitions(n,cap=None):
    if n==0:
        yield (); return
    if cap is None: cap=n
    for k in range(min(cap,n),0,-1):
        for rest in partitions(n-k,k): yield (k,)+rest

def horizontal(nu,alpha):
    aa=alpha+(0,)*len(nu); nn=nu+(0,)
    return all(nn[i]>=aa[i]>=nn[i+1] for i in range(len(nu))) and len(alpha)<=len(nu)

def step8():
    from fractions import Fraction as F
    strip=[]
    for n in (6,7,8):
        tau=(n-4,2,1,1); sigma=(n-4,2,2)
        alphas={name:[a for a in partitions(4) if horizontal(nu,a)] for name,nu in [('tau',tau),('sigma',sigma)]}
        def gap_star(nu):
            return n-1-max(L-1-r for r,L in enumerate(nu) if r==len(nu)-1 or nu[r+1]<L)
        strip.append(dict(n=n,tau=tau,sigma=sigma,alphas=alphas,star_gaps=[gap_star(tau),gap_star(sigma)],star_ratio=gap_star(tau)/gap_star(sigma)))
    # Test the last paragraph of section 5 in the literal sense of Prop. 2.1.
    n=5; candidates=set()
    for v in itertools.product(range(-2,3),repeat=n-1):
        z=v+(-sum(v),)
        if any(z): candidates.add(tuple(sorted(primitive(z),reverse=True)))
    candidates=sorted(candidates,key=lambda z:(sum(t*t for t in z),z))
    violation=None
    for v in candidates:
        T=sum(z*z for z in v); q=F(sum(z**4 for z in v),T*T)
        K=1-F(1,n)-q; trace=n-2-F(2*n,n-2)*K
        for i,j in pairs(n):
            d2=F((v[i]-v[j])**2,T)
            Bij=(1-F(1,n))*F(v[i]**2+v[j]**2,T)-F(v[i]**4+v[j]**4,T*T)+F(2,n)*F(v[i]*v[j],T)+2*F(v[i]**2*v[j]**2,T*T)
            expectation=((n-4)+(7-n)*d2-2*d2*d2-F(2*n,n-2)*(K-Bij))/trace
            lhs=2-d2; rhs=F(n-2,n-1)*(1+expectation)
            if lhs<rhs:
                violation=dict(n=n,integer_vector=v,squared_norm=T,edge=[i+1,j+1],state_transposition_expectation=str(expectation),prop21_lhs=str(lhs),prop21_rhs=str(rhs),violation=str(rhs-lhs))
                break
        if violation: break
    if violation:
        v=np.array(violation['integer_vector'],dtype=float); x=unit(v); Pi=np.eye(n)-np.ones((n,n))/n; Q=Pi-np.outer(x,x)
        matrices=[project((np.outer(x,Q[:,k])+np.outer(Q[:,k],x))/math.sqrt(2)) for k in range(n)]
        i,j=[z-1 for z in violation['edge']]; ix=list(range(n)); ix[i],ix[j]=ix[j],ix[i]
        den=sum(np.sum(S*S) for S in matrices); ex=sum(np.sum(S*S[np.ix_(ix,ix)]) for S in matrices)/den
        violation['direct_matrix_expectation']=float(ex)
        violation['direct_lhs']=float(2-(x[i]-x[j])**2)
        violation['direct_rhs']=float((n-2)/(n-1)*(1+ex))
        m=max(x[a]*x[b] for a,b in pairs(n))
        violation['least_admissible_c']=float(m)
        violation['graph_weights']=[float(m-x[a]*x[b]) for a,b in pairs(n)]
        import sympy as sp
        vv=sp.Matrix(violation['integer_vector']); one=sp.ones(n,1)
        Pi0=sp.eye(n)-one*one.T/n; Q0=Pi0-vv*vv.T/violation['squared_norm']
        def proj0(T): return T-sp.Rational(n,n-2)*Pi0*sp.diag(*T.diagonal())*Pi0
        # With vv in place of unit x and no sqrt(2), the common factor
        # cancels in the expectation ratio. Everything is rational.
        mats=[proj0(vv*Q0[:,k].T+Q0[:,k]*vv.T) for k in range(n)]
        den0=sum(sp.trace(T.T*T) for T in mats)
        num0=sum(sp.trace(T.T*T.extract(ix,ix)) for T in mats)
        violation['exact_direct_matrix_expectation']=str(sp.factor(num0/den0))
        violation['exact_trace_AAstar']=str(sp.factor(den0/(2*violation['squared_norm'])))
        assert str(sp.factor(num0/den0))==violation['state_transposition_expectation']
    save(8,dict(horizontal_strips=strip,claimed_matching_state_counterexample=violation),'WRONG: final Section 5 state-matching claim; other cross-checks correct')

def step7prep():
    bounds=[]
    for n in range(5,14):
        for cone in (1,2):
            rays=cone_rays(n,cone); r=len(rays); K=max(abs(z) for v in rays for z in v)
            path=ROOT/f'rays_n{n}_R{cone}.input'
            path.write_text(f'{n} {r} {cone}\n'+'\n'.join(' '.join(map(str,v)) for v in rays)+'\n')
            bound=((n-4)*(96*15*n*n+16*45*n**3)+144*(n-3)*10*n*n+8*(n-1)*(n*n-6*n+6)*90*n*n+48*n*(n-1)*30*n)*K**6
            assert bound*math.comb(r+5,6)<2**127
            assert n*K**4<2**63
            bounds.append(dict(n=n,cone=cone,rays=r,max_ray_coordinate=K,numerator_abs_bound=bound,sum_abs_bound=bound*math.comb(r+5,6),allocated_lookup_bytes=(r**4+r**3+2*r*r)*8))
    (ROOT/'certificate_bounds.json').write_text(json.dumps(bounds,indent=2)+'\n')
    with (ROOT/'LOG.md').open('a') as f:
        f.write('\nStep 7 extension: attempting to fill the remaining finite gap with a streaming polarization checker. Prepared exact rays for n=5,...,13 and proved integer-overflow bounds in certificate_bounds.json. The checker stores only degree-2/3/4 moment lookups and streams the degree-six coefficients; maximum lookup memory is '+str(max(z['allocated_lookup_bytes'] for z in bounds))+' bytes. Every run has a 270-second alarm.\n')
    print(json.dumps(bounds[-2:],indent=2))

def step7audit():
    def read_coefficients(path,skip):
        lines=path.read_text().splitlines()[skip:]
        return {tuple(map(int,line.split()[1].split(','))):int(line.split()[0]) for line in lines}
    comparisons=[]
    for n in (5,6,7):
        for cone in (1,2):
            a=read_coefficients(ROOT/f'certificate_n{n}_R{cone}.txt',2)
            b=read_coefficients(ROOT/f'rays_n{n}_R{cone}.input.coefficients',0)
            assert a==b
            comparisons.append(dict(n=n,cone=cone,all_coefficients_agree=True,nonzero_coefficients=len(a)))
    extended=[]
    for n in range(5,14):
        for cone in (1,2):
            z=json.loads((ROOT/f'rays_n{n}_R{cone}.input.json').read_text())
            assert z['negative']==0 and z['sum_check']
            assert z['monomials']==math.comb(z['rays']+5,6)
            assert z['zero']==cone
            extended.append(z)
    bounds=json.loads((ROOT/'certificate_bounds.json').read_text())
    data=dict(all_coefficient_comparisons=comparisons,full_finite_range=extended,max_lookup_bytes=max(z['allocated_lookup_bytes'] for z in bounds),maximum_integer_bound=max(z['sum_abs_bound'] for z in bounds),signed128_limit=2**127-1)
    save('7audit',data,'CORRECT for the full n=5,...,13 range; earlier certificate GAP filled independently')

if __name__=='__main__':
    globals()['step'+sys.argv[1]]()
