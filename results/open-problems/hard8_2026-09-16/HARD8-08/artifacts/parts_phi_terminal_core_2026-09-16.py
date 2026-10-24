#!/usr/bin/env python3
"""Exact graph-coloring verifier for a reduction around Parts's two-distance gadget.

The 16-vertex graph G16 is from Jaan Parts, arXiv:2010.12656.
E1 are edges realized at Euclidean distance 1; Ephi are edges realized at
phi=(1+sqrt(5))/2.  The verifier uses only the published exact edge lists.

Claims checked:
1. G16 is 5-colorable and every proper 5-coloring has c(1)=c(16).
2. G16 is relation-edge-critical: deleting ANY one of its 56 edges admits a
   proper 5-coloring with c(1)!=c(16).
3. The abstract 31-vertex Parts construction G31 (two G16 copies sharing
   vertex 1, plus one edge joining their copies of vertex 16) is 6-chromatic
   and edge-critical.  The 5-color witnesses after deletion are constructed
   from the G16 witnesses, so no floating-point geometry is used.

This does NOT solve Hadwiger-Nelson: G16/G31 use two allowed distances 1,phi.
"""

E1 = [
(1,2),(1,3),(2,4),(2,5),(3,4),(3,6),(4,7),(4,8),(5,6),(5,8),(5,9),
(6,7),(6,10),(7,9),(7,12),(7,13),(8,10),(8,11),(8,13),(9,11),(10,12),
(11,12),(11,14),(12,15),(13,14),(13,15),(14,16),(15,16)]
EPHI = [
(1,5),(1,6),(2,3),(2,6),(2,7),(2,9),(3,5),(3,8),(3,10),(4,9),(4,10),
(4,11),(4,12),(5,13),(6,13),(7,10),(7,14),(8,9),(8,15),(9,13),(9,14),
(10,13),(10,15),(11,15),(11,16),(12,14),(12,16),(14,15)]

E1 = [(a-1,b-1) for a,b in E1]
EPHI = [(a-1,b-1) for a,b in EPHI]
N=16


def proper(col, edges):
    return all(col[a] != col[b] for a,b in edges)


def find_coloring(edges, k=5, require_diff=None):
    """Deterministic DSATUR backtracking. Fix vertex 0 to color 0 by symmetry."""
    adj=[set() for _ in range(N)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    color=[-1]*N
    color[0]=0

    def dfs(done):
        if done==N:
            if require_diff is not None:
                a,b=require_diff
                if color[a]==color[b]:
                    return None
            return tuple(color)
        cand=[]
        for v in range(N):
            if color[v] >= 0: continue
            sat=len({color[u] for u in adj[v] if color[u]>=0})
            cand.append((sat,len(adj[v]),-v,v))
        v=max(cand)[-1]
        forbidden={color[u] for u in adj[v] if color[u]>=0}
        for c in range(k):
            if c in forbidden: continue
            if require_diff is not None:
                a,b=require_diff
                if v==a and color[b]>=0 and c==color[b]: continue
                if v==b and color[a]>=0 and c==color[a]: continue
            color[v]=c
            out=dfs(done+1)
            if out is not None:
                return out
            color[v]=-1
        return None
    return dfs(1)


def relabel_to_match(col, old_color, new_color):
    if old_color==new_color:
        return tuple(col)
    out=[]
    for c in col:
        if c==old_color: out.append(new_color)
        elif c==new_color: out.append(old_color)
        else: out.append(c)
    return tuple(out)


def embed_copyA(col16):
    return {i:col16[i] for i in range(16)}


def embed_copyB(col16):
    d={0:col16[0]}
    for j in range(1,16):
        d[15+j]=col16[j]
    return d


def g31_edges():
    A=[]; B=[]
    for typ,Es in [('1',E1),('p',EPHI)]:
        for a,b in Es:
            A.append((a,b,typ,'A'))
            ga=0 if a==0 else 15+a
            gb=0 if b==0 else 15+b
            B.append((ga,gb,typ,'B'))
    cross=(15,30,'1','X')
    return A+B+[cross]


def verify_g31_coloring(assign, edges):
    if set(assign) != set(range(31)):
        return False
    return all(assign[a] != assign[b] for a,b,_,_ in edges)


def main():
    full=E1+EPHI
    K=[0,1,2,4,5]
    edge_set={(min(x,y),max(x,y)) for x,y in full}
    assert all((min(a,b),max(a,b)) in edge_set for a in K for b in K if a<b)

    base=find_coloring(full,5,None)
    assert base is not None and proper(base,full)
    bad=find_coloring(full,5,(0,15))
    assert bad is None, "terminal equality failed"
    print("G16: chi=5 and every 5-coloring has c(1)=c(16): VERIFIED")
    print("one 5-coloring:", ' '.join(map(str,base)))

    witnesses=[]
    for idx,e in enumerate(full):
        reduced=full[:idx]+full[idx+1:]
        w=find_coloring(reduced,5,(0,15))
        assert w is not None
        assert proper(w,reduced)
        assert w[0] != w[15]
        assert w[e[0]] == w[e[1]]
        witnesses.append(w)
        kind='unit' if idx < len(E1) else 'phi'
        print(f"delete {kind} edge {e[0]+1}-{e[1]+1}: terminal-different witness "
              + ' '.join(map(str,w)))
    print("G16: all 56 edges are relation-critical: VERIFIED")

    G31=g31_edges()
    assert len(G31)==113
    print("G31: 31 vertices, 113 listed edges; non-5-colorability follows from G16 relation + cross edge")

    bbase=relabel_to_match(base,base[0],base[0])
    assign={}
    assign.update(embed_copyA(base)); assign.update(embed_copyB(bbase))
    assert verify_g31_coloring(assign,G31[:-1])

    for idx in range(56):
        wa=witnesses[idx]
        bb=relabel_to_match(base,base[0],wa[0])
        assert bb[15]==wa[0]
        a={}; a.update(embed_copyA(wa)); a.update(embed_copyB(bb))
        reduced=G31[:idx]+G31[idx+1:]
        assert verify_g31_coloring(a,reduced)

    for j in range(56):
        wb=witnesses[j]
        aa=relabel_to_match(base,base[0],wb[0])
        assert aa[15]==wb[0]
        a={}; a.update(embed_copyA(aa)); a.update(embed_copyB(wb))
        idx=56+j
        reduced=G31[:idx]+G31[idx+1:]
        assert verify_g31_coloring(a,reduced)

    print("G31: deleting any one of its 113 edges yields a proper 5-coloring: VERIFIED")
    print("Therefore G31 is 6-chromatic and edge-critical (given the published two-distance embedding).")

if __name__=='__main__':
    main()
