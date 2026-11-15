"""Independent checks of the supplied records, combinatorial counts and boundary claims."""
from referee_checks import *
from collections import Counter
from itertools import permutations
import glob

def boundary():
    import sympy as sp
    s=sp.symbols('s',positive=True)
    G=examples()[4][1]; K=Kernel(G,'N','F')
    w=[1,1,s,s,s]
    print('pocket simultaneous epsilon perturbation',list(zip(K.E,map(str,map(sp.factor,K(w,True))))))
    print('single attachment perturbation',list(zip(K.E,map(str,map(sp.factor,K([1,1,s,0,0],True))))))
    G=examples()[0][1]; K=Kernel(G,'N','F'); X,B=sp.symbols('X B',positive=True)
    # a=1-B cannot be ordered symbolically by the support finder, so use A then substitute.
    A=sp.symbols('A',positive=True); p=K([1,X,A,B],True)
    print('paw p',list(zip(K.E,map(str,map(sp.factor,p)))))
    print('paw Xprime a=1-B',sp.factor((p[1]-X).subs(A,1-B)))
    print('paw Bprime a=1-B',sp.factor((p[3]-B).subs(A,1-B)))
    print('paw yF alone from dead equilibrium',K([1,0,1,s],True))

def records():
    counts=Counter(); maxres=0; errors=[]; examples_bad=[]; t=time.time(); conn={}; smallest=1.; stored_max=-10.
    for path in ['data/ex5.jsonl','data/ex6.jsonl','data/ex7.jsonl']:
        for line in open(path):
            r=json.loads(line); G=nx.Graph();G.add_nodes_from(range(r['n']));G.add_edges_from(r['E']); N,F=r['N'],r['F']
            H=G.copy(); H.remove_node(F); R=set(nx.node_connected_component(H,N)); red=len(R)==len(G)-1
            tag='adjacent' if G.has_edge(N,F) else 'distance2plus'; counts[(tag,'cases')]+=1
            counts[(tag,'reduced')]+=red
            Hr=G.subgraph(R|{F}).copy(); D=dead_rule(Hr,N,F)
            counts[(tag,'reduced_D_nonempty')]+=red and bool(D)
            counts[(tag,'one_solution')]+=len(r['sols'])==1
            if red and tag=='distance2plus':
                J=H.copy();J.remove_nodes_from(G.neighbors(F));I=set(nx.node_connected_component(J,N))
                shadow=any(not I.intersection(G.neighbors(x)) for x in G.neighbors(F))
                counts[('distance2plus','shadow_hypothesis')]+=shadow
                branch=False
                for u,y in nx.bridges(H):
                    B=H.copy();B.remove_edge(u,y);C=set(nx.node_connected_component(B,N))
                    if y in C:u,y=y,u
                    if G.has_edge(u,F):branch=True
                counts[('distance2plus','dead_hypothesis')]+=branch
                key=tuple(sorted(tuple(sorted(e)) for e in G.edges()))
                if key not in conn:conn[key]=nx.node_connectivity(G)
                if D:
                    counts[('distance2plus','dead_2connected')]+=conn[key]>=2
                    counts[('distance2plus','dead_3connected')]+=conn[key]>=3
            K=Kernel(G,N,F)
            for sol in r['sols']:
                w=np.array(sol['w']); res=max(abs(K(w)-w)); maxres=max(maxres,res)
                # Compare only reduced edges; unreachable edges are a separate set.
                numeric={frozenset(e) for e,a in zip(K.E,w) if a<1e-8 and set(e)<=R|{F}}
                if numeric!=D: examples_bad.append((r['cid'],r['n'],r['N'],r['F'],sol['starts'],res,sorted(map(sorted,numeric^D))))
                if res>1e-9: errors.append((r['cid'],res))
                if len(r['sols'])==1:
                    smallest=min(smallest,min(w[w>1e-8]));stored_max=max(stored_max,sol['maxre'])
    print('record counts',dict((str(k),v) for k,v in counts.items()))
    print('max residual',maxres,'residual errors',errors[:10],'zero-set discrepancies',examples_bad,'seconds',time.time()-t)
    print('smallest positive weight in single-solution records',smallest,'largest STORED support eigenvalue',stored_max)

def orbit_counts():
    counts=Counter(); t=time.time()
    for G in nx.graph_atlas_g():
        n=len(G)
        if n<3 or not nx.is_connected(G): continue
        unseen=set(permutations(G.nodes(),2)); autos=list(nx.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
        while unseen:
            N,F=min(unseen); orb={(a[N],a[F]) for a in autos}; unseen.difference_update(orb)
            counts[(n,'adjacent' if G.has_edge(N,F) else 'distance2plus')]+=1
    print('independently enumerated ordered-pair orbits',dict((str(k),v) for k,v in counts.items()),'total',sum(counts.values()),'seconds',time.time()-t)

def sample_summary():
    rows=[json.loads(s) for p in glob.glob('referee_census_*.jsonl') for s in open(p)]
    print('sample cases',len(rows),'unique ids',len({r['cid'] for r in rows}),'by_n',dict(Counter(r['n'] for r in rows)))
    print('reduced',sum(r['reduced'] for r in rows),'D_nonempty',sum(bool(r['target']) for r in rows))
    print('mismatches',[(r['cid'],r['target'],[s['zero'] for s in r['sols']]) for r in rows if not r['match']])
    print('max residual',max(s['res'] for r in rows for s in r['sols']),'max start disagreement',max(r['agreement'] for r in rows))

def spectral():
    candidates=[]
    for path in ['data/ex5.jsonl','data/ex6.jsonl','data/ex7.jsonl']:
        for line in open(path):
            r=json.loads(line)
            if len(r['sols'])==1:candidates.append(r)
    # Independently test the worst stored case, using two difference scales.
    r=max(candidates,key=lambda r:r['sols'][0]['maxre'])
    G=nx.Graph();G.add_nodes_from(range(r['n']));G.add_edges_from(r['E']);K=Kernel(G,r['N'],r['F'])
    w=np.array(r['sols'][0]['w']);S=np.flatnonzero(w>0)
    for scale in (1e-5,1e-6):
        J=np.empty((len(S),len(S)))
        for j,e in enumerate(S):
            h=scale*w[e];a=w.copy();b=w.copy();a[e]+=h;b[e]-=h
            J[:,j]=(K(a)[S]-K(b)[S])/(2*h)
        print('worst stored case',r['cid'],'central difference scale',scale,'independent maxRe',max(np.linalg.eigvals(J-np.eye(len(S))).real),flush=True)

if __name__=='__main__':
    budget()
    {'boundary':boundary,'records':records,'orbits':orbit_counts,'summary':sample_summary,'spectral':spectral}[sys.argv[1]]()
