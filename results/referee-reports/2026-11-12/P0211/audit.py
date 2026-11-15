"""Independent generators and checks. Run with numerical threads limited to one."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import sys, json, math, time, signal, resource
signal.alarm(280)
from fractions import Fraction as F
import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal
from scipy.integrate import solve_ivp
from scipy.sparse import diags
from scipy.special import gammaln, logsumexp

def partitions(n, lo=1):
    if n==0:
        yield ()
    for i in range(lo,n+1):
        for p in partitions(n-i,i): yield (i,)+p

def polymer(n,beta,kernel=None,ewens=False):
    states=[]
    for p in partitions(n):
        states.append(tuple(p.count(j) for j in range(1,n+1)))
    ix={m:i for i,m in enumerate(states)}
    q=[[F(0) for _ in states] for m in states]
    def add(a,m,rate): q[a][ix[tuple(m)]]+=rate
    for a,m in enumerate(states):
        for j in range(2,n+1):
            for i in range(1,j//2+1):
                if not m[j-1]: continue
                v=list(m);v[j-1]-=1;v[i-1]+=1;v[j-i-1]+=1
                fac=j if ewens else (kernel(i,j-i) if kernel else 1)
                add(a,v,beta*m[j-1]*(1 if 2*i==j else 2)*fac)
        for i in range(1,n+1):
            for j in range(i,n-i+1):
                pairs=m[i-1]*(m[j-1]-(i==j))
                if not pairs: continue
                v=list(m);v[i-1]-=1;v[j-1]-=1;v[i+j-1]+=1
                fac=i*j if ewens else (kernel(i,j) if kernel else 1)
                add(a,v,F(pairs*(1 if i==j else 2),n)*fac)
        q[a][a]=-sum(q[a])
    w=[(beta*n)**sum(m)/math.prod(math.factorial(x) for x in m) for m in states]
    if ewens:w=[x/math.prod(j**m[j-1] for j in range(1,n+1)) for x,m in zip(w,states)]
    return states,q,w

def radial(n,beta,ell=0,derivative=False):
    if derivative:
        k=np.arange(1,n,dtype=float);up=beta*(n-k-1);down=k*(k-1)/n;kill=beta+2*k/n
    elif ell:
        k=np.arange(ell,n-ell+1,dtype=float)
        up=beta*(n-k-ell);down=(k-1)*(k-ell)/n;kill=ell*beta+ell*(k-1)/n
    else:
        k=np.arange(1,n+1,dtype=float);up=beta*(n-k);down=k*(k-1)/n;kill=k*0
    diag=up+down+kill
    off=-np.sqrt(up[:-1]*down[1:])
    return diag,off

def gapq(n,b):
    d,e=radial(n,b,derivative=True)
    return float(eigh_tridiagonal(d,e,select='i',select_range=(0,0))[0][0])

def eta(n,b):
    d,e=radial(n,b,ell=1)
    return float(eigh_tridiagonal(d,e,select='i',select_range=(0,0))[0][0])

def sharp(n,b):
    d=math.sqrt(b*b+4*b)
    a=(b*n+1+math.sqrt((b*n+1)**2+4*b*n*(n+1)))/2
    c=2*a/n-b
    return c-6*(a-1)/(n*(a+3)),c-6*a*(a-1)/(n*(n+a-2)*(n+a+1)),d

def step13():
    rows=[]
    for n in range(2,11):
        for b in (F(1,50),F(1,7),F(1),F(3)):
            states,q,w=polymer(n,b)
            assert all(w[i]*q[i][j]==w[j]*q[j][i] for i in range(len(q)) for j in range(len(q)))
            reached={0}; stack=[0]
            while stack:
                i=stack.pop()
                for j,x in enumerate(q[i]):
                    if j!=i and x and j not in reached: reached.add(j);stack.append(j)
            assert len(reached)==len(q)
            wf=np.array([float(x) for x in w]);wf/=sum(wf)
            Q=np.array(q,dtype=float)
            H=-np.sqrt(wf[:,None]/wf[None,:])*Q
            vals,vec=eigh(H)
            gap=float(vals[1]);gq=gapq(n,float(b));fun=vec[:,1]/np.sqrt(wf)
            K=np.array([sum(m) for m in states]);means=np.array([np.mean(fun[K==k]) for k in range(1,n+1)])
            residual=max(abs(fun[i]-means[K[i]-1]) for i in range(len(K)))
            delta=np.diff(means);mono=bool(np.all(delta>0) or np.all(delta<0))
            assert abs(gap-gq)<1e-9 and residual<1e-8 and mono
            separation=float(vals[2]-vals[1]) if len(vals)>2 else None
            rows.append(dict(n=n,beta=str(b),states=len(states),gap_M=gap,gap_Q=gq,error=abs(gap-gq),simple_separation=separation,count_residual=residual,monotone=mono,exact_balance=True,irreducible=True))
    with open('step1_3a.json','w') as f:json.dump(rows,f,indent=2)
    rows=[];slacks={}
    def check(name,slack,n,b):
        if name not in slacks or slack<slacks[name]['slack']:slacks[name]=dict(slack=slack,n=n,beta=b)
        assert slack>=-2e-8,(name,n,b,slack)
    for n in (2,3,5,10,50,200,1000):
        for b in (1e-6,1e-4,1e-2,n**-2,1/n,1.,10.,1000.):
            g=gapq(n,b);lo,hi,d=sharp(n,b);s=b+math.sqrt(b)+1/n
            for name,slack in [('sharp_lower',g-lo),('sharp_upper',hi-g),('additive_lower',g-d+5/n),('additive_upper',d+4/n-g),('main_lower',g-s/6),('main_upper',4*s-g),('elementary_lower',g-b-2/n),('elementary_upper',b+4*max(math.sqrt(b),1/n)-g)]:check(name,slack,n,b)
            rows.append(dict(n=n,beta=b,gap_Q=g,sharp_lower=lo,sharp_upper=hi,eta1=eta(n,b)))
    with open('step3b.json','w') as f:json.dump(dict(rows=rows,minimum_slacks=slacks),f,indent=2)
    print('step1/3a:',len(rows),'grid rows; max polymer/count error',max(x['error'] for x in json.load(open('step1_3a.json'))))
    print(json.dumps(slacks,indent=2))

def critical_bracket(b,M=80,degree_one=False):
    # Bound the entire trailing block, even for R>200 million, by Gershgorin.
    # Its least diagonal-minus-row-sum is >= (M+2)(M+1-2sqrt(b)).
    # A Schur complement bounds its last-coordinate correction on the
    # leading M block by e_M^2/(tail_lower-U). No large array is allocated.
    k=np.arange(1,M+1,dtype=float)
    d=k*(k+1)+b;e=-np.sqrt(b*k[:-1]*(k[:-1]+1))
    U=2+b/2
    tail_lower=(M+2)*(M+1-2*math.sqrt(b))
    correction=b*M*(M+1)/(tail_lower-U)
    upper=float(eigh_tridiagonal(d,e,select='i',select_range=(0,0))[0][0])
    dl=d.copy();dl[-1]-=correction
    lower=float(eigh_tridiagonal(dl,e,select='i',select_range=(0,0))[0][0])
    return lower,upper,correction

def step4():
    rows=[]
    for b in (.1,1.,10.,100.):
        R=math.floor(2*b/1e-6)+1
        lo,hi,corr=critical_bracket(b)
        rho=(lo+hi)/2
        finite=[]
        for n in (10,100,1000):
            ng=n*gapq(n,b/n**2)
            assert abs(ng-rho)<=b/n+1e-9
            finite.append(dict(n=n,n_gap=ng,error=ng-rho,error_bound=b/n))
        assert rho>2 and rho<=2+b/2
        rows.append(dict(b=b,R=R,truncation_width=2*b/(R+3),rho_R=rho,schur_lower=lo,schur_upper=hi,tail_correction=corr,finite=finite))
    for x,y in zip(rows,rows[1:]):assert 0<=y['rho_R']-x['rho_R']<=(y['b']-x['b'])/2
    with open('step4.json','w') as f:json.dump(rows,f,indent=2)
    print(json.dumps(rows,indent=2))

def count_tv(n,b,rtol=2e-9,atol=2e-13):
    k=np.arange(1,n+1,dtype=float);up=b*(n-k)/n;down=k*(k-1)/n
    Qtranspose=diags((up[:-1],-up-down,down[1:]),(-1,0,1),format='csc')
    logs=(gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)+k*math.log(b)-gammaln(k))
    p=np.exp(logs-logsumexp(logs))
    tn=math.sqrt(n)*math.log(n)/(8*math.sqrt(b));cs=(-4,-2,-1,0,1,2,4)
    times=np.array([tn+c*math.sqrt(n) for c in cs]);valid=times>=0
    rows=[]
    for endpoint in (1,n):
        q0=np.zeros(n);q0[endpoint-1]=1
        sol=solve_ivp(lambda t,y:Qtranspose@y,(0,float(max(times))),q0,method='BDF',jac=Qtranspose,t_eval=times[valid],rtol=rtol,atol=atol)
        assert sol.success
        tv=.5*np.sum(np.abs(sol.y-p[:,None]),axis=0)
        assert max(abs(sol.y.sum(axis=0)-1))<1e-7
        assert np.min(sol.y)>-1e-9
        j=0
        for c,t in zip(cs,times):
            val=float(tv[j]) if t>=0 else None
            if t>=0:j+=1
            rows.append(dict(b=b,n=n,start=endpoint,c=c,time=float(t),tv=val))
        print('count',b,n,endpoint,'nfev',sol.nfev,'mass_error',max(abs(sol.y.sum(axis=0)-1)),flush=True)
    return rows

def step5():
    rows=[]
    for b in (.5,2.):
        for n in (100,400,1600,6400):
            rows.extend(count_tv(n,b))
            with open('step5.json','w') as f:json.dump(rows,f,indent=2)
    check=count_tv(400,.5,rtol=2e-11,atol=2e-15)
    err=max(abs(a['tv']-next(x['tv'] for x in rows if (x['b'],x['n'],x['start'],x['c'])==(a['b'],a['n'],a['start'],a['c']))) for a in check if a['tv'] is not None)
    print('tight_tolerance_crosscheck_error',err)

def graphs(n):
    return {'path':[(i,i+1,1.) for i in range(n-1)],
            'cycle':[(i,(i+1)%n,1.) for i in range(n)],
            'star':[(0,i,1.) for i in range(1,n)],
            'complete':[(i,j,1.) for i in range(n) for j in range(i+1,n)],
            'unequal_path':[(i,i+1,(i+1)/3) for i in range(n-1)]}

def cut_generator(n,b,edges=(),D=0.):
    masks=list(range(1,2**n));ix={s:i for i,s in enumerate(masks)}
    q=np.zeros((len(masks),len(masks)))
    weights=[]
    for a,s in enumerate(masks):
        k=s.bit_count();weights.append((b*n)**k/math.factorial(k-1))
        for i in range(n):
            t=s^(1<<i)
            if t: q[a,ix[t]]+=((k-1)/n if s&(1<<i) else b)
        for i,j,c in edges:
            if bool(s&(1<<i))!=bool(s&(1<<j)):
                q[a,ix[s^(1<<i)^(1<<j)]]+=D*c
        q[a,a]=-sum(q[a])
    w=np.array(weights);w/=sum(w)
    return masks,q,w

def reversible_spectrum(q,w):
    H=-np.sqrt(w[:,None]/w[None,:])*np.array(q,dtype=float)
    assert np.max(abs(H-H.T))<1e-10
    return eigh(H)

def step7():
    rows=[]
    for n in (4,5,6,7):
        for name,edges in graphs(n).items():
            lap=np.zeros((n,n))
            for i,j,c in edges:
                lap[i,i]+=c;lap[j,j]+=c;lap[i,j]-=c;lap[j,i]-=c
            lg=float(eigh(lap,eigvals_only=True)[1])
            for b in (.05,1.):
                for D in (0.,.1,1.,10.):
                    _,q,w=cut_generator(n,b,edges,D)
                    val=reversible_spectrum(q,w)[0][1]
                    prediction=min(gapq(n,b),eta(n,b)+D*lg)
                    err=abs(val-prediction)
                    assert err<1e-9
                    rows.append(dict(n=n,graph=name,beta=b,D=D,lambda_G=lg,gap=float(val),prediction=prediction,error=float(err),dimension=len(q)))
    grid=json.load(open('step3b.json'))['rows'];slacks={}
    for row in grid:
        n=row['n'];b=row['beta'];et=row['eta1'];a=n*(b+math.sqrt(b*b+4*b))/2;c=a/n
        lo=c-2*a/(n*(a+2));hi=c-2*a*a/(n*(n+a-2)*(n+a))
        u=b+min(n*b,math.sqrt(b));c0=1-2**-.5
        checks={'endpoint_lower':et-lo,'endpoint_upper':hi-et,'additive_lower':et-c+2/n,'additive_upper':c-et,'scale_lower':et-u/8,'scale_upper':u-et,'aux_lower':et-max(b,min(c0*n*b,1/(2*n))),'aux_upper':min(n*b/2,b+math.sqrt(b))-et,'below_count':row['gap_Q']-2/n-et}
        for name,value in checks.items():
            if name not in slacks or value<slacks[name]['slack']:slacks[name]=dict(slack=value,n=n,beta=b)
            assert value>=-2e-8,(name,n,b,value)
    with open('step7.json','w') as f:json.dump(dict(rows=rows,minimum_slacks=slacks),f,indent=2)
    print('spatial cases',len(rows),'max error',max(x['error'] for x in rows))
    print(json.dumps(slacks,indent=2))

def step8():
    rows=[]
    for n in (4,5,6,7):
        for b in (F(1,5),F(1)):
            states,q,w=polymer(n,b);z=sum(w);p=[v/z for v in w];ix={m:i for i,m in enumerate(states)}
            def state(parts):return tuple(parts.count(j) for j in range(1,n+1))
            cyc=[state([2]+[1]*(n-2)),state([2,2]+[1]*(n-4)),state([4]+[1]*(n-4)),state([3]+[1]*(n-3))]
            J=[[0 for _ in states] for m in states]
            eps=min(p[ix[a]]*q[ix[a]][ix[bb]] for a,bb in zip(cyc,cyc[1:]+cyc[:1]))/2
            for a,bb in zip(cyc,cyc[1:]+cyc[:1]):J[ix[a]][ix[bb]]=1;J[ix[bb]][ix[a]]=-1
            qe=[[q[i][j]+eps*J[i][j]/p[i] for j in range(len(q))] for i in range(len(q))]
            assert all(qe[i][j]>=0 for i in range(len(q)) for j in range(len(q)) if i!=j)
            assert all(sum(qe[i])==0 for i in range(len(q)))
            assert all(sum(p[i]*qe[i][j] for i in range(len(q)))==0 for j in range(len(q)))
            assert all(p[i]*qe[i][j]+p[j]*qe[j][i]==2*p[i]*q[i][j] for i in range(len(q)) for j in range(len(q)))
            vals=np.linalg.eigvals(-np.array(qe,dtype=float));nonzero=sorted([v for v in vals if abs(v)>1e-9],key=lambda v:v.real)
            rate=float(nonzero[0].real);gap=gapq(n,float(b))
            assert rate>gap
            rows.append(dict(n=n,beta=float(b),epsilon=float(eps),gap=gap,spectral_rate=rate,improvement=rate-gap,exact_nonnegative=True,exact_invariant=True,exact_symmetric_part=True))
    with open('step8.json','w') as f:json.dump(rows,f,indent=2)
    print(json.dumps(rows,indent=2))

def step9():
    rows=[]
    for n in range(2,10):
        for b in (F(1,50),F(1,7),F(1),F(3)):
            states,q,w=polymer(n,b,ewens=True)
            assert all(w[i]*q[i][j]==w[j]*q[j][i] for i in range(len(q)) for j in range(len(q)))
            vals,_=reversible_spectrum(q,np.array(w,dtype=float));gap=float(vals[1]);expected=float(2*b+F(2*(n-1),n))
            spectrum=[]
            for part in partitions(n):
                lam=sorted(part,reverse=True)
                spectrum.append(float(F(2,n)*(F(n*(n-1),2)-sum(F(x*(x-1),2) for x in lam)+b*n*sum(i*x for i,x in enumerate(lam)))))
            specerr=float(max(abs(vals-np.array(sorted(spectrum)))))
            assert abs(gap-expected)<1e-9 and specerr<1e-9
            growing={}
            for name,kernel in [('product',lambda i,j:i*j),('additive',lambda i,j:i+j)]:
                st,qg,wg=polymer(n,b,kernel=kernel)
                assert all(wg[i]*qg[i][j]==wg[j]*qg[j][i] for i in range(len(qg)) for j in range(len(qg)))
                X=[m[0] for m in st];K=[sum(m) for m in st]
                if name=='product':
                    assert all(sum(qg[i][j]*X[j] for j in range(len(st)))==2*b*(n-K[i])-F(2*(n-1),n)*X[i] for i in range(len(st)))
                vg,_=reversible_spectrum(qg,np.array(wg,dtype=float));gg=float(vg[1]);base=gapq(n,float(b));factor=1 if name=='product' else 2
                assert factor*base<=gg+1e-9 and gg<=factor*expected+1e-9
                growing[name]=gg
            rows.append(dict(n=n,beta=str(b),ewens_gap=gap,formula=expected,error=abs(gap-expected),full_spectrum_error=specerr,product_gap=growing['product'],additive_gap=growing['additive']))
    with open('step9.json','w') as f:json.dump(rows,f,indent=2)
    print('Ewens cases',len(rows),'max gap error',max(x['error'] for x in rows),'max full spectrum error',max(x['full_spectrum_error'] for x in rows))

if __name__=='__main__':
    start=time.monotonic()
    if sys.argv[1]=='step13':step13()
    elif sys.argv[1]=='step4':step4()
    elif sys.argv[1]=='step5':step5()
    elif sys.argv[1]=='step7':step7()
    elif sys.argv[1]=='step8':step8()
    elif sys.argv[1]=='step9':step9()
    print('elapsed_seconds',time.monotonic()-start,'peak_rss',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
