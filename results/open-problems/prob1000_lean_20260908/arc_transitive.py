import itertools
def build(m):
    V=[(j,e) for j in range(m) for e in range(2)]
    idx={v:i for i,v in enumerate(V)}
    E=set()
    for (j,e) in V:
        for dj in (-1,1):
            for e2 in (0,1):
                E.add((idx[(j,e)],idx[((j+dj)%m,e2)]))
    return V,idx,E

def perm_from(V,idx,f):
    return tuple(idx[f(v)] for v in V)

def is_auto(p,E):
    return all((p[a],p[b]) in E for (a,b) in E)

for m in [5,7,9]:
    V,idx,E=build(m); n=2*m
    gens=[]
    # rotation
    gens.append(perm_from(V,idx,lambda v:((v[0]+1)%m,v[1])))
    # reflection
    gens.append(perm_from(V,idx,lambda v:((-v[0])%m,v[1])))
    # twin swap at fibre 0 only
    gens.append(perm_from(V,idx,lambda v:(v[0],1-v[1]) if v[0]==0 else v))
    assert all(is_auto(g,E) for g in gens), f"m={m}: a generator is not an automorphism"
    # orbit of one arc under the generated group (BFS on arcs, closing under gens)
    start=(idx[(0,0)],idx[(1,0)])
    seen={start}; stack=[start]
    # need the full group: close the generator set into a group first
    G={tuple(range(n))}; frontier=[tuple(range(n))]
    while frontier:
        new=[]
        for g in frontier:
            for h in gens:
                c=tuple(h[g[i]] for i in range(n))
                if c not in G: G.add(c); new.append(c)
        frontier=new
    arcs={(a,b) for (a,b) in E}
    orbit={(g[start[0]],g[start[1]]) for g in G}
    print(f"m={m}: |Aut-subgroup generated|={len(G)} (expect {2**m * 2*m}), arcs={len(arcs)} (expect {8*m}), "
          f"arc-orbit={len(orbit)}, ARC-TRANSITIVE={orbit==arcs}")
