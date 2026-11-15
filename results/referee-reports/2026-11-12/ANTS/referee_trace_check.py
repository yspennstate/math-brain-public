"""Second independent evaluation: solve the walk augmented by its entire trace."""
from referee_checks import *

def trace_prob(K,w):
    V=sorted(set(K.G)-{K.F}); ix={x:i for i,x in enumerate(V)}; m=len(w); q=len(V)
    P=np.zeros((q,q)); deg={x:0. for x in K.G}
    for (u,v),a in zip(K.E,w):deg[u]+=a;deg[v]+=a
    dp=np.zeros((1<<m,q,m))
    for mask in range((1<<m)-1,-1,-1):
        A=np.eye(q); B=np.zeros((q,m))
        for j,((u,v),a) in enumerate(zip(K.E,w)):
            for x,z in ((u,v),(v,u)):
                if x==K.F:continue
                i=ix[x]; prob=a/deg[x]; nxt=mask|(1<<j)
                if z==K.F:B[i]+=prob*np.array([(nxt>>s)&1 for s in range(m)])
                elif nxt==mask:A[i,ix[z]]-=prob
                else:B[i]+=prob*dp[nxt,ix[z]]
        dp[mask]=np.linalg.solve(A,B)
    return dp[0,ix[K.N]]

if __name__=='__main__':
    budget(); rng=np.random.default_rng(1846)
    for name,G in examples():
        K=Kernel(G,'N','F')
        for tag,w in [('unit',np.ones(len(K.E))),('weighted',rng.uniform(.1,1,len(K.E)))]:
            a=K(w); b=trace_prob(K,w)
            # Occupation visits and directed crossings provide a separate voltage check.
            V=list(set(G)-{'F'}); ix={x:i for i,x in enumerate(V)}; L=np.zeros((len(V),len(V))); deg={x:0. for x in G}
            for (u,v),ww in zip(K.E,w):
                deg[u]+=ww;deg[v]+=ww
                for x,z in ((u,v),(v,u)):
                    if x in ix:
                        L[ix[x],ix[x]]+=ww
                        if z in ix:L[ix[x],ix[z]]-=ww
            rhs=np.zeros(len(V));rhs[ix['N']]=1;volt=np.linalg.solve(L,rhs);vv={x:volt[ix[x]] for x in V};vv['F']=0
            expected=np.array([ww*(vv[u]+vv[v]) for (u,v),ww in zip(K.E,w)])
            fooderr=max(abs(a[i]-expected[i]) for i,e in enumerate(K.E) if 'F' in e)
            print(name,tag,'augmented-trace error',max(abs(a-b)),'min(expected-p)',min(expected-a),'food identity error',fooderr,flush=True)
