exec(open('computations/C070/channel_explore.py').read().split('for n in [3')[0])
for n in [3,4,5,6]:
    xs=np.array([x for x in product([0,1],repeat=n) if sum(x)==n//2])
    mins=np.full(4,np.inf)
    for k in range(400):
        w=rng.dirichlet(np.ones(len(xs))*.7);a,b=rng.uniform(.005,.995,size=2)
        h=hess_channel(w,xs,a,b);hu=hess_channel(np.ones(len(xs))/len(xs),xs,a,b);d=hu-h
        vals=[d[0,0],d[1,1],d[0,1],min(np.array([z,1.])@d@np.array([z,1.]) for z in np.logspace(-2,2,50))]
        mins=np.minimum(mins,vals)
        if vals[3]<-1e-7:
            print('FAIL',n,w,a,b,d,flush=True);break
    print(n,mins,flush=True)
