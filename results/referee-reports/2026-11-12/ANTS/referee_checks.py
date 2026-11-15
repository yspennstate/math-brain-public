"""Independent audit. No imports from the authors' code. All outputs local."""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import sys, json, time, signal, random
from fractions import Fraction as Q
import numpy as np
import networkx as nx
from scipy.optimize import root, brentq

def budget():
    try: os.nice(10)
    except PermissionError: pass  # sandbox denies setpriority, even to lower priority
    signal.signal(signal.SIGALRM, lambda *_: sys.exit('240-second computation limit'))
    signal.alarm(240)

class Kernel:
    def __init__(self, G, N, F):
        self.G, self.N, self.F = G, N, F
        self.E = list(G.edges())
    def __call__(self, w, exact=False):
        # Vertices reachable BEFORE F, not through F. Kill at the first
        # crossing of the queried edge; its transition becomes success.
        G,N,F,E = self.G,self.N,self.F,self.E
        H = nx.Graph(); H.add_nodes_from(G); H.add_edges_from(e for e,a in zip(E,w) if a>0)
        H.remove_node(F)
        V = sorted(nx.node_connected_component(H,N)); ix={v:i for i,v in enumerate(V)}
        if exact:
            import sympy as sp
            L=sp.zeros(len(V)); rhs=sp.zeros(len(V),len(E))
        else:
            L=np.zeros((len(V),len(V))); rhs=np.zeros((len(E),len(V)))
        for j,((u,v),a) in enumerate(zip(E,w)):
            for x,z in ((u,v),(v,u)):
                if x in ix:
                    L[ix[x],ix[x]]+=a
                    if z in ix: L[ix[x],ix[z]]-=a
                    if exact: rhs[ix[x],j]=a
                    else: rhs[j,ix[x]]=a
        if exact:
            out=[]
            for j,((u,v),a) in enumerate(zip(E,w)):
                A=L.copy()
                if u in ix and v in ix: A[ix[u],ix[v]]=A[ix[v],ix[u]]=0
                out.append(A.inv().multiply(rhs[:,j])[ix[N]])
            return out
        A=np.broadcast_to(L,(len(E),len(V),len(V))).copy()
        for j,(u,v) in enumerate(E):
            if u in ix and v in ix: A[j,ix[u],ix[v]]=A[j,ix[v],ix[u]]=0
        return np.linalg.solve(A,rhs[...,None])[:,ix[N],0]

class InteriorKernel:
    """Same killed-edge equations, prebuilt tensor for positive flow weights."""
    def __init__(self,K):
        self.K=K; self.E=K.E; V=sorted(set(K.G)-{K.F}); self.ix={x:i for i,x in enumerate(V)}
        self.source=self.ix[K.N]; m=len(self.E); q=len(V)
        self.L=np.zeros((m,q,q)); self.B=np.zeros((m,q)); self.off=[]
        for j,(u,v) in enumerate(self.E):
            for x,z in ((u,v),(v,u)):
                if x in self.ix:
                    i=self.ix[x]; self.L[j,i,i]+=1; self.B[j,i]=1
                    if z in self.ix: self.L[j,i,self.ix[z]]-=1
            if u in self.ix and v in self.ix: self.off.append((j,self.ix[u],self.ix[v]))
    def __call__(self,w):
        L=np.einsum('i,ijk->jk',w,self.L)
        A=np.broadcast_to(L,(len(w),)+L.shape).copy()
        for j,u,v in self.off: A[j,u,v]=A[j,v,u]=0
        return np.linalg.solve(A,(w[:,None]*self.B)[...,None])[:,self.source,0]

def dead_rule(G,N,F):
    H=G.copy(); H.remove_node(F)
    if G.has_edge(N,F): I=set(); front={N}
    else:
        J=H.copy(); J.remove_nodes_from(list(G.neighbors(F)))
        I=set(nx.node_connected_component(J,N))
        front={x for x in G.neighbors(F) if I.intersection(G.neighbors(x))}
    D={frozenset((x,F)) for x in G.neighbors(F) if x not in front}
    for u,y in list(nx.bridges(H)):
        J=H.copy(); J.remove_edge(u,y)
        C=set(nx.node_connected_component(J,N))
        if y in C: u,y=y,u
        if u in I: continue
        far=set(nx.node_connected_component(J,y))
        D.update(frozenset(e) for e in G.edges() if far.intersection(e))
    return D

def integrate(K,w,steps):
    for _ in range(steps): w=(w+K(w))*0.5
    return w

def infer(K,seed,steps=1600):
    fast=InteriorKernel(K); rng=np.random.default_rng(seed)
    w=np.exp(rng.uniform(-3,0,len(K.E)))
    a=integrate(fast,w,steps); b=integrate(fast,a,steps)
    zero=(b<0.10)&(b<0.77*a); S=np.flatnonzero(~zero)
    def expand(x):
        z=np.zeros(len(K.E)); z[S]=x; return z
    def fun(x):
        if np.min(x)<=0: return np.ones(len(S))*1e3+np.abs(x)
        z=expand(x); return (K(z)-z)[S]
    rr=root(fun,b[S],tol=1e-10); z=expand(rr.x)
    res=float(np.max(np.abs(K(z)-z))) if np.min(rr.x)>0 else 1e3
    return dict(w=z.tolist(),zero=np.flatnonzero(zero).tolist(),res=res,ok=res<1e-9,
                raw=b.tolist(),ratio=(b/a).tolist())

def examples():
    return [
      ('paw',nx.Graph([('N','x'),('x','y'),('x','F'),('y','F')])),
      ('detour',nx.Graph([('N','a'),('a','F'),('F','b'),('b','N'),('a','y'),('y','F')])),
      ('shadow',nx.Graph([('N','a'),('N','b'),('a','F'),('b','F'),('a','c'),('b','c'),('c','F')])),
      ('K33',nx.Graph([(u,v) for u in ['a','b','c'] for v in ['N','F','x']]+[('x','F')])),
      ('pocket',nx.Graph([('N','u'),('u','F'),('u','y'),('u','z'),('y','z')]))]

def named():
    import sympy as sp
    for name,G in examples():
        K=Kernel(G,'N','F'); ex=K([Q(1)]*len(K.E),True)
        print(name,'edges',K.E,'exact p(1)',list(map(str,ex)),flush=True)
        allsol=[]
        for seed in (11,22,33):
            r=infer(K,seed,2500); allsol.append(r)
        print('equilibria',json.dumps(allsol),flush=True)
        print('connectivity',nx.node_connectivity(G),'dist',nx.shortest_path_length(G,'N','F'),flush=True)
    # Exact symmetric shadow equilibrium equations from the killed-chain solve.
    G=examples()[2][1]; K=Kernel(G,'N','F')
    A,C=sp.symbols('A C',positive=True)
    w=[A if 'N' in e else sp.Rational(1,2) if 'F' in e else C for e in K.E]
    # cF is zero, rather than one half.
    w=[0 if set(e)=={'c','F'} else v for e,v in zip(K.E,w)]
    p=K(w,True)
    print('shadow symbolic',[(e,str(sp.factor(x))) for e,x in zip(K.E,p)],flush=True)
    polys=[sp.factor(sp.together(x-v)).as_numer_denom()[0] for e,x,v in zip(K.E,p,w) if e in [('N','a'),('a','c')]]
    print('shadow equilibrium polynomials',list(map(str,polys)))
    print('Groebner',sp.groebner(polys,A,C))
    for lengths in [(2,2),(3,3,3),(2,3),(2,4),(2,3,4),(2,2,2,5),(3,3,5),(2,8)]:
        def alpha(c,L): return brentq(lambda a:sum(a**j for j in range(L))-1/c,0,1,xtol=5e-15)
        def total(c): return sum(alpha(c,L)**L for L in lengths)-1
        c=brentq(total,max(1/L for L in lengths)+1e-13,1-1e-13,xtol=5e-15)
        aa=[alpha(c,L) for L in lengths]; G=nx.Graph(); weights={}
        for i,(L,a) in enumerate(zip(lengths,aa)):
            path=['N']+[f'{i}:{j}' for j in range(1,L)]+['F']
            for j,e in enumerate(zip(path,path[1:]),1): G.add_edge(*e); weights[frozenset(e)]=a**j
        K=Kernel(G,'N','F'); w=np.array([weights[frozenset(e)] for e in K.E])
        print('theta',lengths,'alpha',aa,'sum',sum(a**L for a,L in zip(aa,lengths)),'residual',max(abs(K(w)-w)),flush=True)

def make_cases():
    rng=random.Random(20261112); cases=[]; seen=set(); buckets={}
    while len(cases)<320:
        n=rng.choice([4,5,6,7]); prob=rng.uniform(.17,.85)
        G=nx.gnp_random_graph(n,prob,seed=rng.randrange(2**32))
        if not nx.is_connected(G): continue
        N,F=rng.sample(range(n),2); key=(n,tuple(sorted(G.edges())),N,F)
        if key in seen: continue
        seen.add(key)
        nx.set_node_attributes(G,{x:'N' if x==N else 'F' if x==F else 'other' for x in G},'role')
        h=nx.weisfeiler_lehman_graph_hash(G,node_attr='role')
        match=nx.algorithms.isomorphism.categorical_node_match('role','other')
        if any(nx.is_isomorphic(G,J,node_match=match) for J in buckets.get(h,[])):continue
        buckets.setdefault(h,[]).append(G.copy())
        cases.append(dict(n=n,E=list(G.edges()),N=N,F=F))
    with open('referee_cases.json','w') as f: json.dump(cases,f)

def census(lo,hi):
    cases=json.load(open('referee_cases.json')); start=time.time()
    with open(f'referee_census_{lo}_{hi}.jsonl','w') as out:
        for cid in range(lo,hi):
            cs=cases[cid]; G=nx.Graph(); G.add_nodes_from(range(cs['n'])); G.add_edges_from(cs['E'])
            N,F=cs['N'],cs['F']; H=G.copy(); H.remove_node(F); R=set(nx.node_connected_component(H,N))
            reduced=len(R)==len(G)-1; G=G.subgraph(R|{F}).copy(); K=Kernel(G,N,F)
            D=dead_rule(G,N,F); target=sorted(i for i,e in enumerate(K.E) if frozenset(e) in D)
            sols=[infer(K,10000+cid*2+s) for s in range(2)]
            match=all(r['ok'] and r['zero']==target for r in sols)
            agreement=max(abs(np.array(sols[0]['w'])-sols[1]['w']))
            row=dict(cid=cid,**cs,reduced=reduced,Er=K.E,target=target,sols=sols,match=match,agreement=agreement)
            out.write(json.dumps(row)+'\n'); out.flush()
            if (cid-lo)%10==0 or not match: print('case',cid,'match',match,'res',max(r['res'] for r in sols),'elapsed',round(time.time()-start,2),flush=True)

if __name__=='__main__':
    budget()
    if sys.argv[1]=='named': named()
    elif sys.argv[1]=='cases': make_cases()
    elif sys.argv[1]=='census': census(int(sys.argv[2]),int(sys.argv[3]))
