"""One-thread, bounded-time stratum search. All output is NUMERICAL."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[k]='1'
import time, json, argparse, warnings, resource
import numpy as np
from scipy.optimize import minimize
warnings.filterwarnings('ignore', message='.*encountered in matmul')
RAW = False


def setup(n):
    ij=np.array([(i,j) for i in range(n) for j in range(i+1,n)])
    B=np.eye(n)[ij[:,0]]-np.eye(n)[ij[:,1]]
    return ij,B,np.eye(n)-np.ones((n,n))/n


def evaluate(L, U, D, ij, H):
    n=len(L); lam=np.trace(U.T@L@U)/D
    Pi=U@U.T; G=lam*H-L
    a=np.diag(Pi); h=np.diag(G); i,j=ij.T
    w=-L[i,j]; tau=a[i]+a[j]-2*Pi[i,j]
    gamma=h[i]+h[j]-2*G[i,j]
    X1=D*np.sum(L*G)
    S2=a@h; S3=np.sum(L*Pi*G); S4=D*np.trace(G)
    c=2*n/(n-2)
    X2=c*(lam*S2-S3); X3=(1-lam)/(n-2)*(S4-c*S2)
    Q=2*np.sum(w*tau*gamma); P=X1+X2+X3
    return Q/P if P>1e-10 else 0., dict(lam=float(lam),P=float(P),Q=float(Q),X1=float(X1),X2=float(X2),X3=float(X3),diagPi=a.tolist())


def project(z,n,D,ij,B,H):
    if RAW:
        w=z/max(np.linalg.norm(z),1e-100)
    else:
        z=z/max(np.max(np.abs(z)),1e-100)
        w=z*z; w=w/max(w.sum(),1e-200)
    L=np.zeros((n,n)); i,j=ij.T
    L[i,j]=L[j,i]=-w
    np.fill_diagonal(L,-L.sum(1))
    # Diagonalize on 1-perp so signed raw variables are also allowed.
    R=np.zeros((n,n-1))
    for k in range(n-1):
        R[:k+1,k]=1/np.sqrt((k+1)*(k+2))
        R[k+1,k]=-(k+1)/np.sqrt((k+1)*(k+2))
    ev,V=np.linalg.eigh(R.T@L@R); U=R@V
    top=U[:,-D:]; av=ev[-D:].mean()
    L=L+(top*(av-ev[-D:]))@top.T
    shift=max(0.,n*np.max(L[ij[:,0],ij[:,1]]))
    L=L+shift*H
    tr=np.trace(L)
    if tr<1e-13: L=2/(n-1)*H
    else: L=L*(2/tr)
    assert np.isfinite(L).all()
    return L,top


def seeds(n,rng):
    ij,B,H=setup(n); lookup={tuple(e):k for k,e in enumerate(ij)}
    def edges(es):
        w=np.zeros(len(ij))
        for i,j,a in es:
            if i!=j: w[lookup[tuple(sorted((int(i),int(j))))]]+=a
        return w
    out=[]
    for k in [5,7,n]:
        if k>n: continue
        cyc=[(i,(i+1)%k,1.) for i in range(k)]
        out.append((f'C{k}-isolates',edges(cyc)))
        if k<n:
            pendant=cyc+[(i-1,i,.5) for i in range(k,n)]
            out.append((f'C{k}-pendant',edges(pendant)))
        out.append((f'C{k}-chord',edges(cyc+[(0,2,.4)])))
        out.append((f'C{k}-heavy',edges(cyc+[(0,1,1.)])))
        if k%2==1 and k+2<=n:
            cyclic_top=2-2*np.cos(2*np.pi*(k//2)/k)
            out.append((f'C{k}-balanced-edge',edges(cyc+[(k,k+1,cyclic_top/2)])))
    out.append(('wheel',edges([(i,1+i%(n-1),1.) for i in range(1,n)]+[(0,i,.7) for i in range(1,n)])))
    if n>=9:
        out.append(('two-odd-shared',edges([(i,(i+1)%5,1.) for i in range(5)]+[(0,5,1.),(5,6,1.),(6,7,1.),(7,8,1.),(8,0,1.)]+[(j-1,j,.2) for j in range(9,n)])))
    if n>=10:
        out.append(('two-odd-joined',edges([(i,(i+1)%5,1.) for i in range(5)]+[(5+i,5+(i+1)%5,1.) for i in range(5)]+[(0,5,.5)]+[(j-1,j,.2) for j in range(10,n)])))
    out.append(('mobius-minus-edge',edges([(i,(i+1)%n,1.) for i in range(n-1)]+[(i,(i+n//2)%n,.7) for i in range(n//2)])))
    groups=np.array_split(np.arange(n),5)
    es=[]
    for t,A in enumerate(groups):
        es += [(i,j,1.) for i in A for j in groups[(t+1)%5]]
        es += [(i,j,.2) for i in A for j in A if i<j]
    out.append(('C5-blowup',edges(es)))
    out.append(('near-bipartite',np.array([rng.uniform(.2,1.) if (i<n//2)!=(j<n//2) else .015*rng.random() for i,j in ij])))
    for k in range(4):
        out.append((f'random{k}',rng.random(len(ij))**(1+k)))
    return out


def direct_check(n=8,D=2):
    rng=np.random.default_rng(610); ij,B,H=setup(n)
    err=[]
    for _ in range(20):
        L,U=project(rng.normal(size=len(ij)),n,D,ij,B,H)
        R,terms=evaluate(L,U,D,ij,H)
        ev,V=np.linalg.eigh(L-np.ones((n,n))/n); lam=ev[-1]
        lo=V[:,1:n-D]; mu=ev[1:n-D]; g=lam-mu
        P=Q=0.; c=2*n/(n-2); w=-L[ij[:,0],ij[:,1]]
        for l in range(len(g)):
            for u in V[:,-D:].T:
                v=lo[:,l]; p=u*v
                P+=g[l]*(mu[l]+c*(lam*(p@p)-p@L@p)+(1-lam)*(1-c*(p@p))/(n-2))
                Q+=g[l]*2*np.sum(w*(B@u)**2*(B@v)**2)
        err.append(max(abs(P-terms['P']),abs(Q-terms['Q'])))
        assert min(w)>-1e-12
        assert (ev[-1]-ev[-D])/ev[-1]<1e-12
    return max(err)


def main():
    global RAW
    ap=argparse.ArgumentParser(); ap.add_argument('n',type=int); ap.add_argument('D',type=int)
    ap.add_argument('--seconds',type=float,default=100); ap.add_argument('--seed',type=int,default=1940)
    ap.add_argument('--maxiter',type=int,default=100)
    ap.add_argument('--raw',action='store_true')
    ap.add_argument('--random',type=int,default=4)
    a=ap.parse_args(); RAW=a.raw
    t0=time.monotonic(); rng=np.random.default_rng(a.seed)
    ij,B,H=setup(a.n); best=-1.; count=0; checks=direct_check(a.n,a.D)
    path=f'search_n{a.n}_D{a.D}.json'; deadline=t0+min(a.seconds,270)
    old=None
    if os.path.exists(path):
        old=json.load(open(path)); best=old['ratio']
    print('NUMERICAL direct-versus-trace max error',checks,flush=True)
    def obj(z):
        if time.monotonic()>deadline: raise TimeoutError
        L,U=project(z,a.n,a.D,ij,B,H); r,_=evaluate(L,U,a.D,ij,H)
        if r>best+1e-10: save(z,name+' intermediate')
        return -r
    def save(z,name):
        nonlocal best,count
        L,U=project(z,a.n,a.D,ij,B,H); r,t=evaluate(L,U,a.D,ij,H); count+=1
        if r>best:
            ev=np.linalg.eigvalsh(L)
            if (ev[-a.D]-ev[-a.D-1])/ev[-1]<1e-8: return r
            best=r
            info=dict(status='NUMERICAL',n=a.n,D=a.D,ratio=r,relative_gap=float((ev[-1]-ev[-a.D])/ev[-1]),next_relative_gap=float((ev[-a.D]-ev[-a.D-1])/ev[-1]),source=name,weights=[[int(i),int(j),float(-L[i,j])] for i,j in ij],terms=t,elapsed=time.monotonic()-t0,seed=a.seed)
            with open(path,'w') as f: json.dump(info,f,indent=2)
            print(f'best {best:.12f} start {name} gap {info["relative_gap"]:.2e}',flush=True)
        return r
    starts=seeds(a.n,rng)
    if old is not None:
        ww=np.array([max(0.,row[2]) for row in old['weights']])
        starts=[('previous-best',ww)] + [(f'previous-perturb{j}',ww+10**(-4+j/2)*rng.random(len(ij))) for j in range(7)] + starts
    if a.random>4:
        starts += [(f'extra{k}',rng.random(len(ij))**rng.uniform(.4,6)) for k in range(a.random-4)]
    # Evaluate every structured start before spending the budget on optimization.
    for seed_name,w in starts:
        zz=w.copy() if RAW else np.sqrt(w+1e-10)
        save(zz,seed_name+' initial survey')
    for name,w in starts:
        z=w.copy() if RAW else np.sqrt(w+1e-10)
        save(z,name+' raw')
        try:
            res=minimize(obj,z,method='L-BFGS-B',options=dict(maxiter=a.maxiter,ftol=2e-13,gtol=1e-7,maxls=25))
            save(res.x,name+' optimized')
            print('finished',name,'ratio',-res.fun,'nfev',res.nfev,flush=True)
        except TimeoutError:
            print('time limit',flush=True); break
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024**2
    print('SUMMARY',a.n,a.D,best,'saved',path,'elapsed',time.monotonic()-t0,'peak RSS MiB',rss,flush=True)
    with open('LOG.md','a') as f: f.write(f'\nNUMERICAL search n={a.n}, D={a.D}, signed raw mode={RAW}: best ratio {best:.15g}, saved in {path}; elapsed {time.monotonic()-t0:.1f} s; {count} saved/intermediate or endpoint checks; peak RSS {rss:.1f} MiB. Direct-versus-trace maximum discrepancy {checks:.3g}. Weights and measured gaps are in the JSON file. These are search results, not proof.\n')

if __name__=='__main__': main()
