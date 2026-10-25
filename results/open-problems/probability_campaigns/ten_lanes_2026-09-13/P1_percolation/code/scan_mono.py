import sys, time, itertools
sys.setrecursionlimit(100000)
from fk_lib import profile, min_over_upsets
from graphs_iso import connected_iso

def run(nmax=5, mmax=10, ps=None, qs=None):
    if ps is None: ps=[0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95]
    if qs is None: qs=[0.001,0.01,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.99]
    worst=(1e9,None); worstcov=(-1e9,None)
    t0=time.time(); ng=0
    for n in range(2,nmax+1):
        for edges in connected_iso(n, mmax=mmax):
            ng+=1
            m=len(edges); pc,kk=profile(n,edges)
            N=1<<m
            for q in qs:
                qp=[q**kk[x] for x in range(N)]
                for p in ps:
                    w=[(p**pc[x])*((1-p)**(m-pc[x]))*qp[x] for x in range(N)]
                    Z=sum(w); mu=[x/Z for x in w]
                    E=sum(mu[x]*pc[x] for x in range(N))
                    val=[mu[x]*(pc[x]-E) for x in range(N)]
                    v,A=min_over_upsets(m,val)
                    if v<worst[0]:
                        worst=(v,(n,tuple(edges),p,q,len(A)))
                    # pairwise covariance
                    for i in range(m):
                        pi=sum(mu[x] for x in range(N) if x>>i&1)
                        for j in range(i+1,m):
                            pij=sum(mu[x] for x in range(N) if (x>>i&1) and (x>>j&1))
                            pj=sum(mu[x] for x in range(N) if x>>j&1)
                            c=pij-pi*pj
                            if c>worstcov[0]:
                                worstcov=(c,(n,tuple(edges),i,j,p,q))
    print("graphs:",ng,"time %.1fs"%(time.time()-t0))
    print("MOST NEGATIVE min_A Cov(1_A,|w|) :", worst[0])
    print("   witness:", worst[1])
    print("MOST POSITIVE pairwise Cov(e,f)  :", worstcov[0])
    print("   witness:", worstcov[1])

if __name__=="__main__":
    run(nmax=int(sys.argv[1]) if len(sys.argv)>1 else 5,
        mmax=int(sys.argv[2]) if len(sys.argv)>2 else 10)
